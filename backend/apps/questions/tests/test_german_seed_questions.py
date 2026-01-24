"""Tests for German seeded questions."""
from __future__ import annotations

import pytest
from apps.jurisdictions.models import Jurisdiction
from apps.questions.models import Question


@pytest.mark.django_db
def test_german_questions_have_explanations() -> None:
    """Ensure German mock questions include option explanations."""
    jurisdiction = Jurisdiction.objects.get(code="DE")
    questions = Question.objects.filter(jurisdiction=jurisdiction)

    assert questions.count() >= 20

    sample = questions.first()
    assert sample is not None
    content = sample.content_json
    assert "option_explanations" in content

    options = {option["key"] for option in content.get("options", [])}
    explanations = set(content.get("option_explanations", {}).keys())
    assert options.issubset(explanations)
