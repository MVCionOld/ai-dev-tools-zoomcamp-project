"""Progress models."""
from __future__ import annotations

from django.db import models
from django.utils import timezone


class UserProgress(models.Model):
    """Track user progress per question."""

    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="progress")
    question = models.ForeignKey("questions.Question", on_delete=models.PROTECT)
    attempts = models.IntegerField(default=0)
    correct_count = models.IntegerField(default=0)
    last_attempt = models.DateTimeField(null=True, blank=True)
    next_review = models.DateTimeField(null=True, blank=True)
    easiness_factor = models.FloatField(default=2.5)
    interval_days = models.IntegerField(default=0)

    class Meta:
        unique_together = ("user", "question")
        indexes = [models.Index(fields=["user", "question"], name="progress_user_question_idx")]

    def record_attempt(self, is_correct: bool) -> None:
        """Record an attempt on this question."""
        self.attempts += 1
        if is_correct:
            self.correct_count += 1
        self.last_attempt = timezone.now()
