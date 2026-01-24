"""Knowledge URLs."""
from __future__ import annotations

from django.urls import path

from apps.knowledge.views import DocumentIngestView, ExplanationView

urlpatterns = [
    path("knowledge/ingest", DocumentIngestView.as_view(), name="knowledge-ingest"),
    path("knowledge/explain", ExplanationView.as_view(), name="knowledge-explain"),
]
