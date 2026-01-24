"""Rename question indexes to shorter names."""
from __future__ import annotations

from django.db import migrations


class Migration(migrations.Migration):
    """Rename question indexes to shorter names."""

    dependencies = [
        ("questions", "0002_seed_questions"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="question",
            old_name="question_jurisdiction_topic_idx",
            new_name="q_jur_topic_idx",
        ),
        migrations.RenameIndex(
            model_name="question",
            old_name="question_difficulty_idx",
            new_name="q_difficulty_idx",
        ),
    ]