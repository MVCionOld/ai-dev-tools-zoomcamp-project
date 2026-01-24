"""Question service layer."""
from __future__ import annotations

from apps.questions.repositories import QuestionRepository


class QuestionService:
    """Business logic for questions."""

    def __init__(self) -> None:
        self.repository = QuestionRepository()

    def list_by_jurisdiction(self, code: str):
        """List questions by jurisdiction code."""
        return self.repository.list_by_jurisdiction(code)
