"""Progress URLs."""
from __future__ import annotations

from django.urls import path

from apps.progress.views import ProgressSummaryView

urlpatterns = [
    path("progress", ProgressSummaryView.as_view(), name="progress-summary"),
]