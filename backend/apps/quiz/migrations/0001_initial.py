"""Initial migrations for quiz."""
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    """Create quiz models."""

    initial = True

    dependencies = [
        ("questions", "0001_initial"),
        ("users", "0001_initial"),
        ("jurisdictions", "0002_seed_jurisdictions"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuizSession",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("mode", models.CharField(choices=[("practice", "Practice"), ("exam", "Exam")], max_length=20)),
                ("started_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("score", models.IntegerField(default=0)),
                ("total_questions", models.IntegerField(default=0)),
                ("time_limit_seconds", models.IntegerField(blank=True, null=True)),
                ("question_ids", models.JSONField(default=list)),
                ("current_index", models.IntegerField(default=0)),
                (
                    "jurisdiction",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="quiz_sessions", to="jurisdictions.jurisdiction"),
                ),
                (
                    "user",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="quiz_sessions", to="users.user"),
                ),
            ],
            options={
                "indexes": [models.Index(fields=["user", "started_at"], name="quiz_session_user_started_idx")],
            },
        ),
        migrations.CreateModel(
            name="QuizAnswer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_answer", models.CharField(max_length=50)),
                ("is_correct", models.BooleanField(default=False)),
                ("answered_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("time_spent_sec", models.IntegerField(blank=True, null=True)),
                (
                    "question",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="questions.question"),
                ),
                (
                    "session",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="answers", to="quiz.quizsession"),
                ),
            ],
            options={
                "indexes": [models.Index(fields=["session", "question"], name="quiz_ans_session_question_idx")],
                "unique_together": {("session", "question")},
            },
        ),
    ]
