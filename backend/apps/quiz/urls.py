"""Quiz routes."""
from django.urls import path

from apps.quiz.views import QuizAnswerView, QuizResultsView, QuizStartView

urlpatterns = [
    path("quiz/start", QuizStartView.as_view(), name="quiz-start"),
    path("quiz/<uuid:quiz_id>/answer", QuizAnswerView.as_view(), name="quiz-answer"),
    path("quiz/<uuid:quiz_id>/results", QuizResultsView.as_view(), name="quiz-results"),
]
