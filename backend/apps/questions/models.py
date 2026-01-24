"""Question models."""
from __future__ import annotations

from django.db import models


class QuestionType(models.TextChoices):
    """Question type choices."""

    MULTIPLE_CHOICE = "multiple_choice", "Multiple Choice"
    IMAGE = "image", "Image"
    SCENARIO = "scenario", "Scenario"


class DifficultyLevel(models.TextChoices):
    """Difficulty choices."""

    BEGINNER = "beginner", "Beginner"
    INTERMEDIATE = "intermediate", "Intermediate"
    EXAM_READY = "exam_ready", "Exam Ready"


class Question(models.Model):
    """Question model."""

    jurisdiction = models.ForeignKey(
        "jurisdictions.Jurisdiction",
        on_delete=models.PROTECT,
        related_name="questions",
    )
    type = models.CharField(max_length=30, choices=QuestionType.choices)
    difficulty = models.CharField(max_length=30, choices=DifficultyLevel.choices)
    topic = models.CharField(max_length=100)
    content_json = models.JSONField()
    correct_answer = models.CharField(max_length=20)
    source = models.CharField(max_length=50, default="seed")
    validated = models.BooleanField(default=True)
    explanation_cache = models.TextField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["jurisdiction", "topic"], name="q_jur_topic_idx"),
            models.Index(fields=["difficulty"], name="q_difficulty_idx"),
        ]

    def __str__(self) -> str:
        """Return string representation."""
        return f"{self.jurisdiction.code}: {self.topic}"
