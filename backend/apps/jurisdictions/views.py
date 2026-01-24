"""Jurisdiction views."""
from __future__ import annotations

from rest_framework import permissions
from rest_framework.views import APIView

from apps.jurisdictions.serializers import JurisdictionSerializer
from apps.jurisdictions.services import JurisdictionService
from core.responses import success_response


class JurisdictionListView(APIView):
    """List jurisdictions."""

    permission_classes = [permissions.AllowAny]

    def get(self, request):  # type: ignore[override]
        service = JurisdictionService()
        jurisdictions = service.list_jurisdictions()
        data = JurisdictionSerializer(jurisdictions, many=True).data
        return success_response(data)
