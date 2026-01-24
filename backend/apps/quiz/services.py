"""Quiz service layer."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta

from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.jurisdictions.repositories import JurisdictionRepository
from apps.progress.services import ProgressService
from apps.questions.models import Question
from apps.questions.repositories import QuestionRepository
from apps.quiz.models import QuizMode, QuizSession
from apps.quiz.repositories import QuizAnswerRepository, QuizSessionRepository


@dataclass
class QuizStartResult:
    """Result of starting a quiz."""

    session: QuizSession
    first_question: Question


class QuizService:
    """Business logic for quizzes."""

    def __init__(self) -> None:
        self.session_repository = QuizSessionRepository()
        self.answer_repository = QuizAnswerRepository()
        self.question_repository = QuestionRepository()
        self.jurisdiction_repository = JurisdictionRepository()
        self.progress_service = ProgressService()

    def start_quiz(self, *, user, jurisdiction_code: str, mode: str, question_count: int | None) -> QuizStartResult:
        """Start a new quiz session."""
        jurisdiction = self.jurisdiction_repository.get_by_code(jurisdiction_code)
        if not jurisdiction:
            raise ValidationError({"jurisdiction": ["Invalid jurisdiction code."]})

        if mode not in {QuizMode.PRACTICE, QuizMode.EXAM}:
            raise ValidationError({"mode": ["Invalid mode."]})

        count = question_count or 20
        if count < 10 or count > 30:
            raise ValidationError({"question_count": ["Question count must be 10-30."]})

        questions = list(
            self.question_repository.list_by_jurisdiction(jurisdiction.code).order_by("?")[:count]
        )
        if len(questions) < count:
            raise ValidationError({"question_count": ["Not enough questions available."]})

        time_limit_seconds = 2700 if mode == QuizMode.EXAM else None
        session = self.session_repository.create(
            user=user,
            jurisdiction=jurisdiction,
            mode=mode,
            total_questions=count,
            time_limit_seconds=time_limit_seconds,
            question_ids=[question.id for question in questions],
            current_index=0,
        )

        return QuizStartResult(session=session, first_question=questions[0])

    def answer_question(self, *, session: QuizSession, question_id: int, answer: str) -> dict:
        """Answer a quiz question."""
        if session.completed_at:
            raise ValidationError({"quiz": ["Quiz already completed."]})

        if session.current_index >= len(session.question_ids):
            raise ValidationError({"quiz": ["Quiz already completed."]})

        expected_question_id = session.question_ids[session.current_index]
        if question_id != expected_question_id:
            raise ValidationError({"question_id": ["Question is out of order."]})

        question = Question.objects.filter(id=question_id).first()
        if not question:
            raise ValidationError({"question_id": ["Question not found."]})

        is_correct = answer == question.correct_answer
        self.answer_repository.create(
            session=session,
            question=question,
            user_answer=answer,
            is_correct=is_correct,
        )

        self.progress_service.record_attempt(user=session.user, question=question, is_correct=is_correct)

        next_index = session.current_index + 1
        has_next = next_index < len(session.question_ids)
        next_question = None
        if has_next:
            session.current_index = next_index
            session.save(update_fields=["current_index"])
            next_question = Question.objects.filter(id=session.question_ids[next_index]).first()
        else:
            score = session.answers.filter(is_correct=True).count()
            session.completed_at = timezone.now()
            session.score = score
            session.save(update_fields=["completed_at", "score"])

        return {
            "is_correct": is_correct,
            "correct_answer": question.correct_answer,
            "has_next": has_next,
            "next_question": next_question,
        }

    def build_results(self, session: QuizSession) -> dict:
        """Build quiz results payload."""
        answers = list(session.answers.select_related("question"))
        total = session.total_questions
        score = session.score or sum(1 for answer in answers if answer.is_correct)
        percentage = int((score / total) * 100) if total else 0
        pass_threshold = 90 if session.mode == QuizMode.EXAM else 70
        passed = percentage >= pass_threshold

        by_topic: dict[str, dict[str, int]] = {}
        incorrect_questions: list[int] = []
        for answer in answers:
            topic = answer.question.topic
            if topic not in by_topic:
                by_topic[topic] = {"correct": 0, "total": 0}
            by_topic[topic]["total"] += 1
            if answer.is_correct:
                by_topic[topic]["correct"] += 1
            else:
                incorrect_questions.append(answer.question.id)

        weak_areas = [
            topic
            for topic, stats in by_topic.items()
            if stats["total"] > 0 and (stats["correct"] / stats["total"]) < 0.7
        ]

        duration_seconds = None
        if session.completed_at:
            duration_seconds = int((session.completed_at - session.started_at).total_seconds())

        return {
            "quiz_id": str(session.id),
            "score": score,
            "total": total,
            "percentage": percentage,
            "passed": passed,
            "pass_threshold": pass_threshold,
            "duration_seconds": duration_seconds,
            "by_topic": by_topic,
            "weak_areas": weak_areas,
            "incorrect_questions": incorrect_questions,
        }
