"""Quiz models."""
from __future__ import annotations

import uuid

from django.db import models
from django.utils import timezone


class QuizMode(models.TextChoices):
    """Quiz mode choices."""

    PRACTICE = "practice", "Practice"
    EXAM = "exam", "Exam"


class QuizSession(models.Model):
    """Quiz session model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="quiz_sessions")
    jurisdiction = models.ForeignKey(
        "jurisdictions.Jurisdiction", on_delete=models.PROTECT, related_name="quiz_sessions"
    )
    mode = models.CharField(max_length=20, choices=QuizMode.choices)
    started_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    time_limit_seconds = models.IntegerField(null=True, blank=True)
    question_ids = models.JSONField(default=list)
    current_index = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=["user", "started_at"], name="quiz_session_user_started_idx"),
        ]


class QuizAnswer(models.Model):
    """Quiz answer model."""

    session = models.ForeignKey(QuizSession, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey("questions.Question", on_delete=models.PROTECT)
    user_answer = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)
    answered_at = models.DateTimeField(default=timezone.now)
    time_spent_sec = models.IntegerField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["session", "question"], name="quiz_ans_session_question_idx"),
        ]
        unique_together = ("session", "question")
