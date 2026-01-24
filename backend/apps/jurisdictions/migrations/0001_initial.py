"""Initial migrations for jurisdictions."""
from django.db import migrations, models


class Migration(migrations.Migration):
    """Create jurisdiction model."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jurisdiction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=5, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("languages", models.JSONField(default=list)),
                ("default_language", models.CharField(max_length=10)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "indexes": [models.Index(fields=["code"], name="jurisdiction_code_idx")],
            },
        ),
    ]
