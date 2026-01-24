"""Initial migrations for knowledge."""
from django.db import migrations, models
import django.db.models.deletion
import pgvector.django


class Migration(migrations.Migration):
    """Create knowledge models."""

    initial = True

    dependencies = [
        ("jurisdictions", "0002_seed_jurisdictions"),
    ]

    operations = [
        pgvector.django.VectorExtension(),
        migrations.CreateModel(
            name="LegalDocument",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("source_url", models.URLField(blank=True, null=True)),
                ("language", models.CharField(default="en", max_length=10)),
                ("effective_date", models.DateField(blank=True, null=True)),
                ("content_text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "jurisdiction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="legal_documents",
                        to="jurisdictions.jurisdiction",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(fields=["jurisdiction", "language"], name="knowledge_doc_jur_lang_idx"),
                ],
            },
        ),
        migrations.CreateModel(
            name="DocumentChunk",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("chunk_index", models.IntegerField()),
                ("content", models.TextField()),
                ("embedding", pgvector.django.VectorField(blank=True, dimensions=1536, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chunks",
                        to="knowledge.legaldocument",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(fields=["document", "chunk_index"], name="knowledge_chunk_doc_idx"),
                ],
                "unique_together": {("document", "chunk_index")},
            },
        ),
    ]
