"""Middleware for consistent API response metadata."""
from __future__ import annotations

import uuid
from typing import Any

from rest_framework.response import Response


class ResponseMetaMiddleware:
    """Attach request metadata to API responses."""

    def __init__(self, get_response: Any) -> None:
        self.get_response = get_response

    def __call__(self, request: Any) -> Any:
        request.request_id = str(uuid.uuid4())
        response = self.get_response(request)
        if request.path.startswith("/api/"):
            response["X-Request-Id"] = request.request_id
            if isinstance(response, Response):
                if isinstance(response.data, dict) and "success" in response.data:
                    response.data.setdefault("meta", {})
                    response.data["meta"].setdefault("request_id", request.request_id)
        return response
