"""Quiz serializers."""
from __future__ import annotations

from typing import Any

from rest_framework import serializers

from apps.questions.models import Question


class QuizStartSerializer(serializers.Serializer):
    """Serializer for starting a quiz."""

    jurisdiction = serializers.CharField()
    mode = serializers.ChoiceField(choices=["practice", "exam"])
    question_count = serializers.IntegerField(required=False, min_value=10, max_value=30)


class QuizAnswerSerializer(serializers.Serializer):
    """Serializer for answering a quiz question."""

    question_id = serializers.IntegerField()
    answer = serializers.CharField()


class QuestionResponseSerializer(serializers.Serializer):
    """Serializer for question responses."""

    id = serializers.IntegerField()
    index = serializers.IntegerField()
    type = serializers.CharField()
    content = serializers.DictField()
    topic = serializers.CharField()
    difficulty = serializers.CharField()


def build_question_payload(question: Question, index: int) -> dict[str, Any]:
    """Build a question payload for API responses."""
    return {
        "id": question.id,
        "index": index,
        "type": question.type,
        "content": question.content_json,
        "topic": question.topic,
        "difficulty": question.difficulty,
    }
