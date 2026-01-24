"""Jurisdiction repository."""
from __future__ import annotations

from typing import Optional

from apps.jurisdictions.models import Jurisdiction


class JurisdictionRepository:
    """Data access for jurisdictions."""

    @staticmethod
    def list_active() -> list[Jurisdiction]:
        """Return active jurisdictions."""
        return list(Jurisdiction.objects.filter(is_active=True).order_by("code"))

    @staticmethod
    def get_by_code(code: str) -> Optional[Jurisdiction]:
        """Return jurisdiction by code."""
        return Jurisdiction.objects.filter(code=code).first()
