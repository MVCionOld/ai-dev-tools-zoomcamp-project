"""Progress repository layer."""
from __future__ import annotations

from typing import Any

from django.db.models import Count, Max, Sum
from django.db.models.functions import Coalesce

from apps.progress.models import UserProgress


class ProgressRepository:
    """Data access for user progress."""

    @staticmethod
    def get_or_create(user, question) -> UserProgress:
        """Get or create user progress."""
        progress, _ = UserProgress.objects.get_or_create(user=user, question=question)
        return progress

    @staticmethod
    def save(progress: UserProgress) -> UserProgress:
        """Save progress model."""
        progress.save()
        return progress

    @staticmethod
    def aggregate_user_progress(user) -> dict[str, Any]:
        """Aggregate progress stats for a user."""
        return UserProgress.objects.filter(user=user).aggregate(
            total_questions_attempted=Count("id"),
            total_attempts=Coalesce(Sum("attempts"), 0),
            total_correct=Coalesce(Sum("correct_count"), 0),
            last_activity=Max("last_attempt"),
        )
