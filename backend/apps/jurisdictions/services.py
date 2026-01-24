"""Jurisdiction service layer."""
from __future__ import annotations

from apps.jurisdictions.repositories import JurisdictionRepository


class JurisdictionService:
    """Business logic for jurisdictions."""

    def __init__(self) -> None:
        self.repository = JurisdictionRepository()

    def list_jurisdictions(self):
        """List active jurisdictions."""
        return self.repository.list_active()
