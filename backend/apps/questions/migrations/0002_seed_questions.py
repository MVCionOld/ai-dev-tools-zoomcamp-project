"""Seed mock questions for MVP."""
from __future__ import annotations

from django.db import migrations


def seed_questions(apps, schema_editor) -> None:
    """Create mock questions for each jurisdiction."""
    Jurisdiction = apps.get_model("jurisdictions", "Jurisdiction")
    Question = apps.get_model("questions", "Question")

    for code in ["DE", "ES", "PT"]:
        jurisdiction = Jurisdiction.objects.filter(code=code).first()
        if not jurisdiction:
            continue

        existing = Question.objects.filter(jurisdiction=jurisdiction).count()
        target = 20
        if existing >= target:
            continue

        questions = []
        for index in range(existing + 1, target + 1):
            questions.append(
                Question(
                    jurisdiction=jurisdiction,
                    type="multiple_choice",
                    difficulty="beginner",
                    topic="rules_basics",
                    content_json={
                        "text": f"{code} practice question {index}: What should you do at a stop sign?",
                        "image_url": None,
                        "options": [
                            {"key": "A", "text": "Stop completely and proceed when safe"},
                            {"key": "B", "text": "Slow down only"},
                            {"key": "C", "text": "Honk and continue"},
                            {"key": "D", "text": "Stop only if pedestrians"},
                        ],
                    },
                    correct_answer="A",
                    source="seed",
                    validated=True,
                    explanation_cache=None,
                )
            )

        if questions:
            Question.objects.bulk_create(questions)


def unseed_questions(apps, schema_editor) -> None:
    """Remove seeded mock questions."""
    Question = apps.get_model("questions", "Question")
    Question.objects.filter(source="seed", topic="rules_basics").delete()


class Migration(migrations.Migration):
    """Seed mock questions for MVP."""

    dependencies = [
        ("questions", "0001_initial"),
        ("jurisdictions", "0002_seed_jurisdictions"),
    ]

    operations = [
        migrations.RunPython(seed_questions, reverse_code=unseed_questions),
    ]