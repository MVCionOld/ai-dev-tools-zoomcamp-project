"""Question repository."""
from __future__ import annotations

from apps.questions.models import Question


class QuestionRepository:
    """Data access for questions."""

    @staticmethod
    def list_by_jurisdiction(code: str):
        """List questions by jurisdiction code."""
        return Question.objects.filter(jurisdiction__code=code, validated=True)
