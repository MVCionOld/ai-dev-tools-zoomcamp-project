"""User views."""
from __future__ import annotations

from rest_framework import permissions, status
from rest_framework.views import APIView

from apps.users.serializers import (
    LoginSerializer,
    LogoutSerializer,
    PreferencesSerializer,
    RefreshSerializer,
    RegisterSerializer,
    UserSerializer,
)
from apps.users.services import UserService
from core.responses import success_response


class RegisterView(APIView):
    """Register a new user."""

    permission_classes = [permissions.AllowAny]

    def post(self, request):  # type: ignore[override]
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return success_response(
            {
                "id": user.id,
                "email": user.email,
                "requires_verification": True,
            },
            status_code=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    """Log in a user."""

    permission_classes = [permissions.AllowAny]

    def post(self, request):  # type: ignore[override]
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return success_response(serializer.validated_data)


class RefreshView(APIView):
    """Refresh JWT access token."""

    permission_classes = [permissions.AllowAny]

    def post(self, request):  # type: ignore[override]
        serializer = RefreshSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return success_response(serializer.validated_data)


class LogoutView(APIView):
    """Log out a user by blacklisting refresh token."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):  # type: ignore[override]
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return success_response(None)


class MeView(APIView):
    """Return current user."""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):  # type: ignore[override]
        return success_response(UserSerializer(request.user).data)


class PreferencesView(APIView):
    """Update user preferences."""

    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):  # type: ignore[override]
        serializer = PreferencesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = UserService()
        user = service.update_preferences(
            user=request.user,
            jurisdiction_code=serializer.validated_data.get("preferred_jurisdiction"),
            language=serializer.validated_data.get("preferred_language"),
        )
        return success_response(
            {
                "preferred_jurisdiction": user.preferred_jurisdiction.code if user.preferred_jurisdiction else None,
                "preferred_language": user.preferred_language,
            }
        )
