"""User serializers."""
from __future__ import annotations

from typing import Any

from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.services import UserService

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    """Serializer for user registration."""

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        """Validate password confirmation."""
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        return attrs

    def create(self, validated_data: dict[str, Any]) -> User:
        """Create a new user."""
        service = UserService()
        return service.register_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user profile."""

    preferred_jurisdiction = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "email", "preferred_jurisdiction", "preferred_language", "created_at"]

    def get_preferred_jurisdiction(self, obj: User) -> str | None:
        """Return jurisdiction code."""
        if obj.preferred_jurisdiction:
            return obj.preferred_jurisdiction.code
        return None


class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        """Validate credentials and return tokens."""
        user = authenticate(username=attrs["email"], password=attrs["password"])
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        refresh = RefreshToken.for_user(user)
        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "expires_in": int(refresh.access_token.lifetime.total_seconds()),
            "user": {
                "id": user.id,
                "email": user.email,
                "preferred_jurisdiction": user.preferred_jurisdiction.code if user.preferred_jurisdiction else None,
                "preferred_language": user.preferred_language,
            },
        }


class RefreshSerializer(TokenRefreshSerializer):
    """Serializer for token refresh."""

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        """Return refreshed access token."""
        data = super().validate(attrs)
        refresh_token = data.get("refresh")
        if refresh_token:
            refresh = RefreshToken(refresh_token)
            expires_in = int(refresh.access_token.lifetime.total_seconds())
        else:
            expires_in = int(self.token_class(attrs["refresh"]).access_token.lifetime.total_seconds())
        return {
            "access_token": data["access"],
            "expires_in": expires_in,
        }


class LogoutSerializer(serializers.Serializer):
    """Serializer for logout."""

    refresh_token = serializers.CharField()

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        """Blacklist refresh token."""
        try:
            token = RefreshToken(attrs["refresh_token"])
            token.blacklist()
        except Exception as exc:  # noqa: BLE001
            raise serializers.ValidationError("Invalid token.") from exc
        return attrs


class PreferencesSerializer(serializers.Serializer):
    """Serializer for user preferences."""

    preferred_jurisdiction = serializers.CharField(required=False)
    preferred_language = serializers.CharField(required=False)
