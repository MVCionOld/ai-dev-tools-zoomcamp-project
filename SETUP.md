# Setup Guide

## Prerequisites

- Python 3.12+
- Node.js 20+
- PostgreSQL 16 with pgvector extension
- Redis 7+
- uv (Python package manager)

---

## Quick Start

### 1. Clone & Environment

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

### 2. Database

```bash
# Create database
createdb driving_prep

# Enable pgvector
psql driving_prep -c "CREATE EXTENSION vector;"

# Run migrations
cd backend
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 3. Run Services

```bash
# Terminal 1: Redis (if not running)
redis-server

# Terminal 2: Backend
cd backend
python manage.py runserver

# Terminal 3: Celery worker
cd backend
celery -A config worker -l info

# Terminal 4: Frontend
cd frontend
npm run dev
```

### 4. Verify

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/api/v1/
- Admin: http://localhost:8000/admin/

---

## Environment Variables

### Backend (`backend/.env`)

```bash
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/driving_prep
REDIS_URL=redis://localhost:6379/0
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
| pgvector not found | `CREATE EXTENSION vector;` in psql |
| CORS errors | Check `CORS_ALLOWED_ORIGINS` matches frontend URL |
| Redis connection refused | Start Redis: `redis-server` |
| OpenAI rate limit | Check API key, reduce request frequency |
