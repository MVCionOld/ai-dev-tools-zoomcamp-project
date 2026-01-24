"""Global pytest fixtures."""
from __future__ import annotations

import factory
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from apps.jurisdictions.models import Jurisdiction

User = get_user_model()


class JurisdictionFactory(factory.django.DjangoModelFactory):
    """Factory for Jurisdiction."""

    class Meta:
        model = Jurisdiction

    code = factory.Sequence(lambda n: f"J{n}")
    name = factory.Sequence(lambda n: f"Jurisdiction {n}")
    languages = ["en"]
    default_language = "en"
    is_active = True


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for User."""

    class Meta:
        model = User
        skip_postgeneration_save = True

    email = factory.Sequence(lambda n: f"user{n}@example.com")

    @factory.post_generation
    def password(self, create: bool, extracted: str | None, **kwargs) -> None:
        """Set and hash the user's password."""
        raw_password = extracted or "SecurePass123!"
        self.set_password(raw_password)
        if create:
            self.save()


import pytest  # noqa: E402


@pytest.fixture
def api_client() -> APIClient:
    """Return DRF API client."""
    return APIClient()


@pytest.fixture
def user_factory() -> type[UserFactory]:
    """Return user factory."""
    return UserFactory


@pytest.fixture
def jurisdiction_factory() -> type[JurisdictionFactory]:
    """Return jurisdiction factory."""
    return JurisdictionFactory
