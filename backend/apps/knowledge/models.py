"""Knowledge models."""
from __future__ import annotations

from django.db import models
from pgvector.django import VectorField


class LegalDocument(models.Model):
    """Legal document model."""

    jurisdiction = models.ForeignKey(
        "jurisdictions.Jurisdiction",
        on_delete=models.PROTECT,
        related_name="legal_documents",
    )
    title = models.CharField(max_length=255)
    source_url = models.URLField(null=True, blank=True)
    language = models.CharField(max_length=10, default="en")
    effective_date = models.DateField(null=True, blank=True)
    content_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["jurisdiction", "language"], name="knowledge_doc_jur_lang_idx"),
        ]


class DocumentChunk(models.Model):
    """Document chunk model with embeddings."""

    document = models.ForeignKey(
        LegalDocument,
        on_delete=models.CASCADE,
        related_name="chunks",
    )
    chunk_index = models.IntegerField()
    content = models.TextField()
    embedding = VectorField(dimensions=1536, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("document", "chunk_index")
        indexes = [
            models.Index(fields=["document", "chunk_index"], name="knowledge_chunk_doc_idx"),
        ]
