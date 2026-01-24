"""Questions app configuration."""
from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    """Questions app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.questions"
