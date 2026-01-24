"""Jurisdiction API tests."""
from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestJurisdictions:
    """Jurisdiction list tests."""

    def test_list_jurisdictions(self, api_client):
        """List returns seeded jurisdictions."""
        response = api_client.get("/api/v1/jurisdictions")
        assert response.status_code == 200
        assert response.data["success"] is True
        codes = {item["code"] for item in response.data["data"]}
        assert {"DE", "ES", "PT"}.issubset(codes)
