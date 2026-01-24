"""Quiz integration tests."""
from __future__ import annotations

import pytest

from apps.jurisdictions.models import Jurisdiction
from apps.questions.models import DifficultyLevel, Question, QuestionType


def create_questions(jurisdiction, count: int = 12) -> None:
    """Create sample questions."""
    for index in range(count):
        Question.objects.create(
            jurisdiction=jurisdiction,
            type=QuestionType.MULTIPLE_CHOICE,
            difficulty=DifficultyLevel.BEGINNER,
            topic="road_signs" if index % 2 == 0 else "right_of_way",
            content_json={
                "text": f"Question {index}",
                "options": [
                    {"key": "A", "text": "Option A"},
                    {"key": "B", "text": "Option B"},
                    {"key": "C", "text": "Option C"},
                    {"key": "D", "text": "Option D"},
                ],
            },
            correct_answer="A",
        )


@pytest.mark.django_db
class TestQuizFlow:
    """Quiz flow tests."""

    def test_start_quiz(self, api_client, user_factory):
        """Start quiz returns first question."""
        user = user_factory()
        jurisdiction = Jurisdiction.objects.get(code="DE")
        create_questions(jurisdiction)
        api_client.force_authenticate(user=user)
        response = api_client.post(
            "/api/v1/quiz/start",
            {"jurisdiction": "DE", "mode": "practice", "question_count": 10},
            format="json",
        )
        assert response.status_code == 201
        assert response.data["success"] is True
        assert response.data["data"]["current_question"]["index"] == 1

    def test_answer_and_results(self, api_client, user_factory):
        """Answer question and fetch results."""
        user = user_factory()
        jurisdiction = Jurisdiction.objects.get(code="PT")
        create_questions(jurisdiction)
        api_client.force_authenticate(user=user)
        start = api_client.post(
            "/api/v1/quiz/start",
            {"jurisdiction": "PT", "mode": "practice", "question_count": 10},
            format="json",
        )
        quiz_id = start.data["data"]["quiz_id"]
        first_question = start.data["data"]["current_question"]

        answer = api_client.post(
            f"/api/v1/quiz/{quiz_id}/answer",
            {"question_id": first_question["id"], "answer": "A"},
            format="json",
        )
        assert answer.status_code == 200
        assert answer.data["data"]["is_correct"] is True

        results = api_client.get(f"/api/v1/quiz/{quiz_id}/results")
        assert results.status_code == 200
        assert results.data["data"]["total"] == 10
