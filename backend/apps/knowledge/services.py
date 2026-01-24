"""Knowledge service layer."""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

from apps.knowledge.models import DocumentChunk
from apps.knowledge.repositories import KnowledgeRepository
from apps.questions.models import Question


@dataclass
class ExplanationResult:
    """Result of generating an explanation."""

    explanation: str
    citations: list[dict[str, Any]]
    source: str


class KnowledgeService:
    """Business logic for knowledge retrieval."""

    def __init__(self) -> None:
        self.repository = KnowledgeRepository()

    def ingest_document(
        self,
        *,
        jurisdiction,
        title: str,
        content_text: str,
        source_url: str | None,
        language: str,
        effective_date,
    ) -> list[DocumentChunk]:
        """Ingest a legal document and create chunks."""
        document = self.repository.create_document(
            jurisdiction=jurisdiction,
            title=title,
            source_url=source_url,
            language=language,
            effective_date=effective_date,
            content_text=content_text,
        )

        chunks: list[DocumentChunk] = []
        for index, chunk in enumerate(self._chunk_text(content_text)):
            chunks.append(
                DocumentChunk(
                    document=document,
                    chunk_index=index,
                    content=chunk,
                    embedding=None,
                )
            )

        return self.repository.bulk_create_chunks(chunks)

    def explain_question(self, *, question: Question, jurisdiction_code: str) -> ExplanationResult:
        """Generate explanation for a question using RAG."""
        api_key = os.getenv("LLM_API_KEY")
        chunks = list(self.repository.list_chunks_for_jurisdiction(jurisdiction_code)[:5])

        if not api_key:
            citations = self._mock_citations(chunks)
            return ExplanationResult(
                explanation=(
                    "Mock explanation: Always stop fully and yield to traffic when a stop sign is present. "
                    "Review right-of-way basics for this jurisdiction."
                ),
                citations=citations,
                source="mock",
            )

        citations = self._mock_citations(chunks)
        return ExplanationResult(
            explanation=(
                "Placeholder explanation: This answer is based on the applicable road safety rules. "
                "Replace with real LLM output when provider integration is enabled."
            ),
            citations=citations,
            source="placeholder",
        )

    def _chunk_text(self, text: str) -> list[str]:
        """Split document text into chunks."""
        parts = [part.strip() for part in text.split("\n\n") if part.strip()]
        return parts or [text.strip()]

    def _mock_citations(self, chunks: list[DocumentChunk]) -> list[dict[str, Any]]:
        """Build mock citations from stored chunks."""
        citations: list[dict[str, Any]] = []
        for chunk in chunks[:3]:
            citations.append(
                {
                    "source_id": f"DOC-{chunk.document_id}-{chunk.chunk_index}",
                    "title": chunk.document.title,
                    "url": chunk.document.source_url,
                    "snippet": chunk.content[:180],
                }
            )
        if not citations:
            citations.append(
                {
                    "source_id": "MOCK-REF-1",
                    "title": "Mock Road Rules",
                    "url": None,
                    "snippet": "Always obey traffic signs and yield where required.",
                }
            )
        return citations
