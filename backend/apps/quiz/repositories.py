"""Quiz repository layer."""
from __future__ import annotations

from typing import Optional

from apps.quiz.models import QuizAnswer, QuizSession


class QuizSessionRepository:
    """Data access for quiz sessions."""

    @staticmethod
    def create(**kwargs) -> QuizSession:
        """Create a quiz session."""
        return QuizSession.objects.create(**kwargs)

    @staticmethod
    def get_by_id(session_id: str) -> Optional[QuizSession]:
        """Get quiz session by ID."""
        return QuizSession.objects.filter(id=session_id).first()

    @staticmethod
    def save(session: QuizSession, **fields) -> QuizSession:
        """Save quiz session updates."""
        for key, value in fields.items():
            setattr(session, key, value)
        session.save(update_fields=list(fields.keys()))
        return session


class QuizAnswerRepository:
    """Data access for quiz answers."""

    @staticmethod
    def create(**kwargs) -> QuizAnswer:
        """Create a quiz answer."""
        return QuizAnswer.objects.create(**kwargs)

    @staticmethod
    def list_for_session(session: QuizSession):
        """List answers for a session."""
        return QuizAnswer.objects.filter(session=session)
