"""Knowledge app configuration."""
from __future__ import annotations

from django.apps import AppConfig


class KnowledgeConfig(AppConfig):
    """Knowledge app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.knowledge"
