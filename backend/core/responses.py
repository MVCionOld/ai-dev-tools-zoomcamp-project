"""API response helpers."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from rest_framework.response import Response


def success_response(data: Any, status_code: int = 200) -> Response:
    """Return a standardized success response."""
    return Response(
        {
            "success": True,
            "data": data,
            "meta": {
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
        },
        status=status_code,
    )
