"""Tests for knowledge ingestion."""
from __future__ import annotations

import pytest
from rest_framework.test import APIClient

from apps.users.models import User


@pytest.mark.django_db
def test_ingest_document_creates_chunks(api_client: APIClient, user_factory) -> None:
    """Ingesting a document returns chunk count."""
    user: User = user_factory(password="SecurePass123!")
    client = api_client
    client.force_authenticate(user=user)

    response = client.post(
        "/api/v1/knowledge/ingest",
        {
            "jurisdiction": "DE",
            "title": "Mock Road Act",
            "content_text": "Section 1.\n\nSection 2.",
            "source_url": "https://example.com/mock",
            "language": "de",
            "effective_date": "2024-01-01",
        },
        format="json",
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["success"] is True
    assert payload["data"]["chunk_count"] == 2
