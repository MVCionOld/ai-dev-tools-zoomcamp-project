"""Custom exception handling for API responses."""
from __future__ import annotations

from typing import Any

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc: Exception, context: dict[str, Any]) -> Response:
    """Return standardized error responses."""
    response = drf_exception_handler(exc, context)
    if response is None:
        return Response(
            {
                "success": False,
                "error": {
                    "code": "INTERNAL_ERROR",
                    "message": "Unexpected server error.",
                    "details": {},
                },
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if isinstance(exc, APIException):
        code = getattr(exc, "default_code", "error").upper()
    else:
        code = "ERROR"

    message = "Request failed."
    if isinstance(response.data, dict):
        if "detail" in response.data:
            message = response.data.get("detail", message)
        else:
            for value in response.data.values():
                if isinstance(value, list) and value:
                    message = str(value[0])
                    break
                if isinstance(value, str):
                    message = value
                    break

    return Response(
        {
            "success": False,
            "error": {
                "code": code,
                "message": message,
                "details": response.data,
            },
        },
        status=response.status_code,
    )
