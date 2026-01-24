# Backend — Driving License Exam Prep API

Django REST Framework backend providing authentication, quiz management, RAG-powered explanations, and learning intelligence.

> **Technology:** Django 5.0 + Django REST Framework + PostgreSQL + pgvector + Celery + Redis

## External Dependencies

| Service | Purpose | Local Setup |
|---------|---------|-------------|
| PostgreSQL 16 + pgvector | Primary database, vector store | `docker compose up -d postgres` |
| Redis 7 | Caching, sessions, Celery broker | `docker compose up -d redis` |
| OpenAI API | LLM for explanations, embeddings | API key in `.env` |

> **Important:** PostgreSQL and Redis must be run via Docker Compose. See [SETUP.md](../SETUP.md) for instructions.

## Responsibilities

- REST API endpoints for all platform features
- User authentication (JWT)
- Quiz session management
- RAG-powered explanation generation
- Spaced repetition scheduling
- Legal document ingestion and embedding
- Background task processing

---

**UX Reference:** [Getting an Explanation](../docs/ux-scenarios.md#scenario-5-getting-an-explanation-rag)

---

## API Response Format

**Success:**
```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "timestamp": "2026-01-17T10:00:00Z",
    "request_id": "uuid-here"
  }
}
```

**Error:**
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable message",
    "details": {
      "field": ["Error for this field"]
    }
  }
}
```

**Error Codes:**
| Code | HTTP Status | Description |
|------|-------------|-------------|
| `VALIDATION_ERROR` | 400 | Invalid request data |
| `AUTHENTICATION_REQUIRED` | 401 | Missing/invalid token |
| `PERMISSION_DENIED` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource doesn't exist |
| `RATE_LIMITED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Server error |

---

## Background Tasks (Celery)

| Task | Trigger | Purpose |
|------|---------|---------|
| `generate_embeddings` | Document ingestion | Create embeddings for new legal docs |
| `refresh_embeddings` | Scheduled (weekly) | Re-embed documents if models updated |
| `pregenerate_explanations` | Scheduled (nightly) | Cache explanations for frequently missed questions |
| `cleanup_expired_cache` | Scheduled (daily) | Remove stale cache entries |
| `send_review_reminders` | Scheduled (daily) | Email users with due reviews |

---

## Security

| Concern | Implementation |
|---------|----------------|
| Authentication | JWT with 15-min access, 7-day refresh tokens |
| Password Storage | Argon2 hashing via Django |
| Rate Limiting | DRF throttling: 100/hour anon, 1000/hour authenticated |
| AI Rate Limiting | 20 explanations/user/hour |
| Input Validation | DRF serializers + Pydantic |
| SQL Injection | Django ORM parameterized queries |
| CORS | Whitelist frontend origin only |

---

## Environment Variables

> **Note:** External services (PostgreSQL, Redis) run in Docker containers. Start them with `docker compose up -d` from the project root.

```bash
# .env.example
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (Docker: driving_prep_postgres)
DATABASE_URL=postgresql://user:pass@localhost:5432/driving_prep
POSTGRES_DB=driving_prep
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# Redis (Docker: driving_prep_redis)
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/1

# OpenAI (external cloud service)
OPENAI_API_KEY=sk-...
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
OPENAI_CHAT_MODEL=gpt-4-turbo-preview

# JWT
JWT_ACCESS_TOKEN_LIFETIME_MINUTES=15
JWT_REFRESH_TOKEN_LIFETIME_DAYS=7

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

---

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=apps --cov-report=html

# Run specific app tests
pytest tests/test_quiz/

# Run with verbose output
pytest -v
```

**Test Categories:**
- Unit tests: Business logic in services
- Integration tests: API endpoints with database
- RAG tests: Mocked LLM responses

---

## Related Documentation

- [ARCHITECTURE.md](../ARCHITECTURE.md) — System design and data flow
- [PROJECT.md](../PROJECT.md) — Feature roadmap
- [docs/ux-scenarios.md](../docs/ux-scenarios.md) — User experience flows
- [frontend/README.md](../frontend/README.md) — Frontend integration
