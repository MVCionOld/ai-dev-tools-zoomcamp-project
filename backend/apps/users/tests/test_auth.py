"""Authentication tests."""
from __future__ import annotations

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestAuth:
    """Authentication endpoints tests."""

    def test_register_user(self, api_client):
        """Register creates user and returns expected payload."""
        response = api_client.post(
            "/api/v1/auth/register",
            {
                "email": "newuser@example.com",
                "password": "SecurePass123!",
                "password_confirm": "SecurePass123!",
            },
            format="json",
        )
        assert response.status_code == 201
        assert response.data["success"] is True
        assert response.data["data"]["email"] == "newuser@example.com"
        assert User.objects.filter(email="newuser@example.com").exists()

    def test_login_returns_tokens(self, api_client, user_factory):
        """Login returns access and refresh tokens."""
        user_factory(email="login@example.com")
        response = api_client.post(
            "/api/v1/auth/login",
            {"email": "login@example.com", "password": "SecurePass123!"},
            format="json",
        )
        assert response.status_code == 200
        assert response.data["success"] is True
        assert "access_token" in response.data["data"]
        assert "refresh_token" in response.data["data"]

    def test_me_requires_auth(self, api_client):
        """Me endpoint requires authentication."""
        response = api_client.get("/api/v1/auth/me")
        assert response.status_code == 401

    def test_me_returns_user(self, api_client, user_factory):
        """Me returns user profile."""
        user = user_factory(email="me@example.com")
        api_client.force_authenticate(user=user)
        response = api_client.get("/api/v1/auth/me")
        assert response.status_code == 200
        assert response.data["data"]["email"] == "me@example.com"
