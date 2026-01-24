"""Seed default jurisdictions."""
from __future__ import annotations

from django.db import migrations


DEFAULT_JURISDICTIONS = [
    {
        "code": "DE",
        "name": "Germany",
        "languages": ["de", "en", "tr", "pt"],
        "default_language": "de",
        "is_active": True,
    },
    {
        "code": "ES",
        "name": "Spain",
        "languages": ["es", "en", "ca"],
        "default_language": "es",
        "is_active": True,
    },
    {
        "code": "PT",
        "name": "Portugal",
        "languages": ["pt", "en"],
        "default_language": "pt",
        "is_active": True,
    },
]


def seed_jurisdictions(apps, schema_editor) -> None:
    """Insert default jurisdictions if missing."""
    Jurisdiction = apps.get_model("jurisdictions", "Jurisdiction")
    for payload in DEFAULT_JURISDICTIONS:
        Jurisdiction.objects.update_or_create(code=payload["code"], defaults=payload)


def reverse_seed(apps, schema_editor) -> None:
    """No-op reverse migration."""
    return None


class Migration(migrations.Migration):
    """Seed jurisdictions."""

    dependencies = [
        ("jurisdictions", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_jurisdictions, reverse_seed),
    ]
