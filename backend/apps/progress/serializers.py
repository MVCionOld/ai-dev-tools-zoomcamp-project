"""Progress serializers."""
from __future__ import annotations

from rest_framework import serializers


class ProgressSummarySerializer(serializers.Serializer):
    """Serializer for progress summary."""

    total_questions_attempted = serializers.IntegerField()
    total_correct = serializers.IntegerField()
    accuracy_percentage = serializers.IntegerField()
    current_streak = serializers.IntegerField()
    longest_streak = serializers.IntegerField()
    readiness_score = serializers.IntegerField()
    last_activity = serializers.DateTimeField(allow_null=True)