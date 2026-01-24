"""User repository layer."""
from __future__ import annotations

from typing import Optional

from django.contrib.auth import get_user_model

User = get_user_model()


class UserRepository:
    """Data access for user model."""

    @staticmethod
    def get_by_email(email: str) -> Optional[User]:
        """Return user by email if exists."""
        return User.objects.filter(email=email).first()

    @staticmethod
    def create(email: str, password: str) -> User:
        """Create a new user."""
        return User.objects.create_user(email=email, password=password)
