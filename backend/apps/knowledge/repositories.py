"""Knowledge repository layer."""
from __future__ import annotations

from apps.knowledge.models import DocumentChunk, LegalDocument


class KnowledgeRepository:
    """Data access for knowledge models."""

    @staticmethod
    def create_document(**kwargs) -> LegalDocument:
        """Create a legal document."""
        return LegalDocument.objects.create(**kwargs)

    @staticmethod
    def bulk_create_chunks(chunks: list[DocumentChunk]) -> list[DocumentChunk]:
        """Bulk create document chunks."""
        return list(DocumentChunk.objects.bulk_create(chunks))

    @staticmethod
    def list_chunks_for_jurisdiction(jurisdiction_code: str):
        """List chunks by jurisdiction code."""
        return DocumentChunk.objects.filter(document__jurisdiction__code=jurisdiction_code)
