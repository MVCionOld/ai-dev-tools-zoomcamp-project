"""Jurisdiction models."""
from __future__ import annotations

from django.db import models


class Jurisdiction(models.Model):
    """Represents a supported country/jurisdiction."""

    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)
    languages = models.JSONField(default=list)
    default_language = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [models.Index(fields=["code"], name="jurisdiction_code_idx")]

    def __str__(self) -> str:
        """Return string representation."""
        return f"{self.code} - {self.name}"
