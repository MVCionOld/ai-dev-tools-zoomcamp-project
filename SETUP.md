# Setup Guide

## Prerequisites

- Python 3.12+
- Node.js 20+
- Docker & Docker Compose (for external services)
- uv (Python package manager)

### External Services (via Docker)

The following external systems are required and **must be run via Docker Compose** for local development:

| Service | Image | Purpose |
|---------|-------|---------|
| PostgreSQL 16 | `pgvector/pgvector:pg16` | Primary database with vector extension |
| Redis 7 | `redis:7-alpine` | Caching, sessions, Celery broker |


---

## Quick Start

### 1. Start External Services (Docker)

```bash
# Start PostgreSQL and Redis containers
docker compose up -d

# Verify services are running
docker compose ps

# Check service health
docker compose logs postgres
docker compose logs redis
```

### 2. Clone & Environment

```bash
git clone <repo>
cd ai-dev-tools-zoomcamp-project

# Backend
cd backend
cp .env.example .env  # Edit with your values
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Frontend
cd ../frontend
cp .env.example .env
npm install
```

### 3. Database Setup

```bash
# pgvector extension is already enabled in the Docker image
# Just run migrations
cd backend
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 4. Run Application

```bash
# Terminal 1: Backend
cd backend
python manage.py runserver

# Terminal 2: Celery worker
cd backend
celery -A config worker -l info

# Terminal 3: Frontend
cd frontend
npm run dev
```

### 5. Verify

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/api/v1/
- Admin: http://localhost:8000/admin/

---

## Docker Commands Reference

```bash
# Start services
docker compose up -d

# Stop services
docker compose down

# Stop and remove volumes (reset data)
docker compose down -v

# View logs
docker compose logs -f postgres
docker compose logs -f redis

# Restart a specific service
docker compose restart postgres
```

---

## Environment Variables

### Backend (`backend/.env`)

```bash
DEBUG=True
SECRET_KEY=your-secret-key-here

# Docker services (default ports)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/driving_prep
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/1

# External API (cloud service - requires API key)
OPENAI_API_KEY=sk-...

CORS_ALLOWED_ORIGINS=http://localhost:5173
```

### Frontend (`frontend/.env`)

```bash
VITE_API_URL=http://localhost:8000/api/v1
```

---

## Seed Data (MVP)

```bash
cd backend
python manage.py loaddata fixtures/jurisdictions.json   # DE, ES, PT
python manage.py loaddata fixtures/sample_questions.json  # 10 seed questions
```

Fixtures are located in `backend/fixtures/`. Add more questions by copying the JSON structure.

---

## Common Issues

| Problem | Solution |
|---------|----------|
| Docker containers not starting | Run `docker compose logs` to check errors |
| Port 5432 already in use | Stop local PostgreSQL or change port in docker-compose.yml |
| Port 6379 already in use | Stop local Redis or change port in docker-compose.yml |
| pgvector not found | The Docker image includes pgvector; ensure using `pgvector/pgvector:pg16` |
| CORS errors | Check `CORS_ALLOWED_ORIGINS` matches frontend URL |
| Redis connection refused | Verify Redis container is running: `docker compose ps` |
| OpenAI rate limit | Check API key, reduce request frequency |
| Database connection refused | Verify Postgres container is healthy: `docker compose ps` |
