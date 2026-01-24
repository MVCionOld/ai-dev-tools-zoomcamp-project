"""Progress service layer."""
from __future__ import annotations

from typing import Any

from apps.progress.repositories import ProgressRepository


class ProgressService:
    """Business logic for progress tracking."""

    def __init__(self) -> None:
        self.repository = ProgressRepository()

    def record_attempt(self, *, user, question, is_correct: bool) -> None:
        """Record a user attempt for a question."""
        progress = self.repository.get_or_create(user=user, question=question)
        progress.record_attempt(is_correct)
        self.repository.save(progress)

    def get_summary(self, *, user) -> dict[str, Any]:
        """Return progress summary for a user."""
        aggregates = self.repository.aggregate_user_progress(user)
        total_attempts = int(aggregates.get("total_attempts", 0) or 0)
        total_correct = int(aggregates.get("total_correct", 0) or 0)
        accuracy_percentage = int(round((total_correct / total_attempts) * 100)) if total_attempts else 0

        return {
            "total_questions_attempted": int(aggregates.get("total_questions_attempted", 0) or 0),
            "total_correct": total_correct,
            "accuracy_percentage": accuracy_percentage,
            "current_streak": 0,
            "longest_streak": 0,
            "readiness_score": 0,
            "last_activity": aggregates.get("last_activity"),
        }
