"""User preferences tests."""
from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestPreferences:
    """Preferences endpoint tests."""

    def test_update_preferences(self, api_client, user_factory):
        """Update preferred jurisdiction and language."""
        user = user_factory(email="prefs@example.com")
        api_client.force_authenticate(user=user)
        response = api_client.patch(
            "/api/v1/users/preferences",
            {"preferred_jurisdiction": "DE", "preferred_language": "en"},
            format="json",
        )
        assert response.status_code == 200
        assert response.data["data"]["preferred_jurisdiction"] == "DE"
        assert response.data["data"]["preferred_language"] == "en"
