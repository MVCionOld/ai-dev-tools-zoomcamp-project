"""Quiz views."""
from __future__ import annotations

from rest_framework import permissions, status
from rest_framework.views import APIView

from apps.quiz.repositories import QuizSessionRepository
from apps.quiz.serializers import (
    QuizAnswerSerializer,
    QuizStartSerializer,
    build_question_payload,
)
from apps.quiz.services import QuizService
from core.responses import success_response


class QuizStartView(APIView):
    """Start a quiz session."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):  # type: ignore[override]
        serializer = QuizStartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = QuizService()
        result = service.start_quiz(
            user=request.user,
            jurisdiction_code=serializer.validated_data["jurisdiction"],
            mode=serializer.validated_data["mode"],
            question_count=serializer.validated_data.get("question_count"),
        )
        payload = {
            "quiz_id": str(result.session.id),
            "mode": result.session.mode,
            "total_questions": result.session.total_questions,
            "time_limit_seconds": result.session.time_limit_seconds,
            "current_question": build_question_payload(result.first_question, 1),
        }
        return success_response(payload, status_code=status.HTTP_201_CREATED)


class QuizAnswerView(APIView):
    """Submit an answer for a quiz session."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, quiz_id: str):  # type: ignore[override]
        serializer = QuizAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        repository = QuizSessionRepository()
        session = repository.get_by_id(quiz_id)
        if not session or session.user_id != request.user.id:
            return success_response(None, status_code=status.HTTP_404_NOT_FOUND)

        service = QuizService()
        result = service.answer_question(
            session=session,
            question_id=serializer.validated_data["question_id"],
            answer=serializer.validated_data["answer"],
        )
        payload = {
            "is_correct": result["is_correct"],
            "correct_answer": result["correct_answer"],
            "has_next": result["has_next"],
            "next_question":
                build_question_payload(result["next_question"], session.current_index + 1)
                if result["next_question"]
                else None,
        }
        return success_response(payload)


class QuizResultsView(APIView):
    """Return quiz results."""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, quiz_id: str):  # type: ignore[override]
        repository = QuizSessionRepository()
        session = repository.get_by_id(quiz_id)
        if not session or session.user_id != request.user.id:
            return success_response(None, status_code=status.HTTP_404_NOT_FOUND)

        service = QuizService()
        payload = service.build_results(session)
        return success_response(payload)
