"""Knowledge serializers."""
from __future__ import annotations

from rest_framework import serializers


class DocumentIngestSerializer(serializers.Serializer):
    """Serializer for ingesting legal documents."""

    jurisdiction = serializers.CharField(max_length=10)
    title = serializers.CharField(max_length=255)
    content_text = serializers.CharField()
    source_url = serializers.URLField(required=False, allow_null=True, allow_blank=True)
    language = serializers.CharField(max_length=10, default="en")
    effective_date = serializers.DateField(required=False, allow_null=True)


class ExplanationRequestSerializer(serializers.Serializer):
    """Serializer for explanation request."""

    question_id = serializers.IntegerField()
    jurisdiction = serializers.CharField(max_length=10)


class ExplanationResponseSerializer(serializers.Serializer):
    """Serializer for explanation response."""

    explanation = serializers.CharField()
    source = serializers.CharField()
    citations = serializers.ListField(child=serializers.DictField())
