"""Initial migrations for questions."""
from django.db import migrations, models


class Migration(migrations.Migration):
    """Create question model."""

    initial = True

    dependencies = [
        ("jurisdictions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("type", models.CharField(choices=[("multiple_choice", "Multiple Choice"), ("image", "Image"), ("scenario", "Scenario")], max_length=30)),
                ("difficulty", models.CharField(choices=[("beginner", "Beginner"), ("intermediate", "Intermediate"), ("exam_ready", "Exam Ready")], max_length=30)),
                ("topic", models.CharField(max_length=100)),
                ("content_json", models.JSONField()),
                ("correct_answer", models.CharField(max_length=20)),
                ("source", models.CharField(default="seed", max_length=50)),
                ("validated", models.BooleanField(default=True)),
                ("explanation_cache", models.TextField(blank=True, null=True)),
                (
                    "jurisdiction",
                    models.ForeignKey(on_delete=models.PROTECT, related_name="questions", to="jurisdictions.jurisdiction"),
                ),
            ],
            options={
                "indexes": [
                    models.Index(fields=["jurisdiction", "topic"], name="question_jurisdiction_topic_idx"),
                    models.Index(fields=["difficulty"], name="question_difficulty_idx"),
                ],
            },
        ),
    ]
