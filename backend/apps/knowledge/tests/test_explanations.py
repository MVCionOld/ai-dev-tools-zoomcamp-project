"""Tests for knowledge explanations."""
from __future__ import annotations

import pytest
from rest_framework.test import APIClient

from apps.jurisdictions.models import Jurisdiction
from apps.questions.models import Question
from apps.users.models import User


@pytest.mark.django_db
def test_explanation_returns_mock_when_api_key_missing(api_client: APIClient, user_factory) -> None:
    """Return mock explanation when API key missing."""
    user: User = user_factory(password="SecurePass123!")
    client = api_client
    client.force_authenticate(user=user)

    jurisdiction = Jurisdiction.objects.get(code="DE")
    question = Question.objects.filter(jurisdiction=jurisdiction).first()
    assert question is not None

    response = client.post(
        "/api/v1/knowledge/explain",
        {
            "question_id": question.id,
            "jurisdiction": jurisdiction.code,
        },
        format="json",
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["success"] is True
    assert payload["data"]["source"] == "mock"
    assert payload["data"]["explanation"]
    assert payload["data"]["citations"]
