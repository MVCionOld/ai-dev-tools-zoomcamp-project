"""Quiz app configuration."""
from django.apps import AppConfig


class QuizConfig(AppConfig):
    """Quiz app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.quiz"
