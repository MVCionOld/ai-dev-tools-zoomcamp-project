"""Progress views."""
from __future__ import annotations

from rest_framework import permissions
from rest_framework.views import APIView

from apps.progress.serializers import ProgressSummarySerializer
from apps.progress.services import ProgressService
from core.responses import success_response


class ProgressSummaryView(APIView):
    """Return progress summary for the authenticated user."""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):  # type: ignore[override]
        service = ProgressService()
        summary = service.get_summary(user=request.user)
        data = ProgressSummarySerializer(summary).data
        return success_response(data)