"""Initial migrations for progress."""
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Create progress model."""

    initial = True

    dependencies = [
        ("questions", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProgress",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("attempts", models.IntegerField(default=0)),
                ("correct_count", models.IntegerField(default=0)),
                ("last_attempt", models.DateTimeField(blank=True, null=True)),
                ("next_review", models.DateTimeField(blank=True, null=True)),
                ("easiness_factor", models.FloatField(default=2.5)),
                ("interval_days", models.IntegerField(default=0)),
                (
                    "question",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="questions.question"),
                ),
                (
                    "user",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="progress", to="users.user"),
                ),
            ],
            options={
                "unique_together": {("user", "question")},
                "indexes": [models.Index(fields=["user", "question"], name="progress_user_question_idx")],
            },
        ),
    ]
