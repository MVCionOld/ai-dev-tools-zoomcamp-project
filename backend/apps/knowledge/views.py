"""Knowledge views."""
from __future__ import annotations

from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from apps.jurisdictions.repositories import JurisdictionRepository
from apps.knowledge.serializers import (
    DocumentIngestSerializer,
    ExplanationRequestSerializer,
    ExplanationResponseSerializer,
)
from apps.knowledge.services import KnowledgeService
from apps.questions.models import Question
from core.responses import success_response


class DocumentIngestView(APIView):
    """Ingest legal document content."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):  # type: ignore[override]
        serializer = DocumentIngestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        jurisdiction = JurisdictionRepository().get_by_code(data["jurisdiction"])
        if not jurisdiction:
            raise ValidationError({"jurisdiction": ["Invalid jurisdiction code."]})

        service = KnowledgeService()
        chunks = service.ingest_document(
            jurisdiction=jurisdiction,
            title=data["title"],
            content_text=data["content_text"],
            source_url=data.get("source_url"),
            language=data.get("language", "en"),
            effective_date=data.get("effective_date"),
        )

        return success_response(
            {
                "document_title": data["title"],
                "chunk_count": len(chunks),
            }
        )


class ExplanationView(APIView):
    """Generate explanation for a question."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):  # type: ignore[override]
        serializer = ExplanationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        question = Question.objects.filter(id=data["question_id"]).first()
        if not question:
            raise ValidationError({"question_id": ["Question not found."]})

        service = KnowledgeService()
        result = service.explain_question(
            question=question,
            jurisdiction_code=data["jurisdiction"],
        )

        response = ExplanationResponseSerializer(
            {
                "explanation": result.explanation,
                "source": result.source,
                "citations": result.citations,
            }
        )
        return success_response(response.data)
