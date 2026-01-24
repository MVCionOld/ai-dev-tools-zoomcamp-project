"""Jurisdiction routes."""
from django.urls import path

from apps.jurisdictions.views import JurisdictionListView

urlpatterns = [
    path("jurisdictions", JurisdictionListView.as_view(), name="jurisdictions-list"),
]
