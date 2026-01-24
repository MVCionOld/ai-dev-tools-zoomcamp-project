"""URL configuration for backend project."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.users.urls")),
    path("api/v1/", include("apps.jurisdictions.urls")),
    path("api/v1/", include("apps.quiz.urls")),
    path("api/v1/", include("apps.progress.urls")),
]
