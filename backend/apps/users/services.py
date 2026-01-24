"""User service layer."""
from __future__ import annotations

from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from apps.jurisdictions.repositories import JurisdictionRepository
from apps.users.repositories import UserRepository

User = get_user_model()


class UserService:
    """Business logic for users."""

    def __init__(self) -> None:
        self.user_repository = UserRepository()
        self.jurisdiction_repository = JurisdictionRepository()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user."""
        if self.user_repository.get_by_email(email=email):
            raise ValidationError({"email": ["Email already registered."]})
        return self.user_repository.create(email=email, password=password)

    def update_preferences(self, user: User, jurisdiction_code: str | None, language: str | None) -> User:
        """Update user preferences."""
        if jurisdiction_code:
            jurisdiction = self.jurisdiction_repository.get_by_code(jurisdiction_code)
            if not jurisdiction:
                raise ValidationError({"preferred_jurisdiction": ["Invalid jurisdiction code."]})
            user.preferred_jurisdiction = jurisdiction
        if language:
            user.preferred_language = language
        user.save(update_fields=["preferred_jurisdiction", "preferred_language"])
        return user
