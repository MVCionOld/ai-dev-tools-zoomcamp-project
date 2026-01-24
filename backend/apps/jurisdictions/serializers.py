"""Jurisdiction serializers."""
from __future__ import annotations

from rest_framework import serializers

from apps.jurisdictions.models import Jurisdiction


class JurisdictionSerializer(serializers.ModelSerializer):
    """Serializer for jurisdictions."""

    class Meta:
        model = Jurisdiction
        fields = ["code", "name", "languages", "default_language"]
