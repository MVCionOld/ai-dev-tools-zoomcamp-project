# Architecture

AI-powered driving license exam preparation platform with RAG-based knowledge retrieval, adaptive learning, and multi-jurisdictional support.

## System Design

```
┌─────────────────────────────────────────────────────────────────┐
│                      Frontend Layer (React)                      │
│           User Interface & Client-Side Logic                     │
└─────────────────────────┬───────────────────────────────────────┘
                          │ REST API (JSON)
┌─────────────────────────▼───────────────────────────────────────┐
│                      Backend Layer (Django)                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │   Auth &    │  │  Question   │  │   Learning Intelligence │  │
│  │   Users     │  │   Engine    │  │        Engine           │  │
│  └─────────────┘  └──────┬──────┘  └────────────┬────────────┘  │
│                          │                      │                │
│  ┌───────────────────────▼──────────────────────▼────────────┐  │
│  │              Knowledge Retrieval Service (RAG)             │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │  │
│  │  │  Embeddings  │  │   Vector DB  │  │  LLM Service    │  │  │
│  │  │  (OpenAI)    │  │  (pgvector)  │  │  (OpenAI/Claude)│  │  │
│  │  └──────────────┘  └──────────────┘  └─────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────┬───────────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────────┐
│                      Data Layer (PostgreSQL)                     │
│  Users │ Questions │ Legal Documents │ Progress │ Jurisdictions │
└─────────────────────────────────────────────────────────────────┘
```

## Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Frontend | React 18 + TypeScript | UI components and state management |
| State Management | React Query (TanStack) | Server state, caching |
| Styling | Tailwind CSS | Utility-first styling |
| Backend | Django 5.0 + DRF | REST API, business logic |
| Task Queue | Celery + Redis | Async question generation |
| Database | PostgreSQL 16 | Primary data store |
| Vector Store | pgvector | Embeddings for RAG |
| Cache | Redis | Response caching, sessions |
| LLM | OpenAI GPT-4 | Question generation, explanations |
| Embeddings | OpenAI text-embedding-3-small | Document embeddings |

## Principles

1. **Separation of Concerns**: Independent components with defined interfaces
2. **Modularity**: Self-contained, independently developable components
3. **Documentation First**: Document all decisions and designs
4. **API-Driven**: Communication through defined REST APIs
5. **Scalability**: Support horizontal scaling
6. **RAG-First**: All AI explanations must cite source documents
7. **Multi-Jurisdiction**: Data isolation between countries/languages

---

## Core Services

### 1. Question Engine Service

Unified service for all question types (multiple-choice, scenario, image-based).

**Responsibilities:**
- Generate questions from templates + AI
- Validate AI-generated questions
- Manage question difficulty scaling
- Handle question types (text, image, scenario)

**Design Pattern:**
```
QuestionGenerator (abstract)
├── TemplateQuestionGenerator  → Curated seed questions
├── AIQuestionGenerator        → LLM-generated questions
└── ScenarioQuestionGenerator  → Branching scenario questions
```

**Data Flow:**
```
Request → Select Generator → Fetch/Generate Question
                          → Validate Question
                          → Apply Difficulty Filter
                          → Return Question Set
```

### 2. Knowledge Retrieval Service (RAG)

Powers explanations and law lookups with source citations.

**Responsibilities:**
- Embed and index legal documents
- Retrieve relevant context for questions
- Generate explanations with citations
- Handle multi-jurisdiction queries

**RAG Pipeline:**
```
1. Query Received (question + jurisdiction)
2. Embed Query → OpenAI text-embedding-3-small
3. Vector Search → pgvector (filtered by jurisdiction metadata)
4. Retrieve Top-K Document Chunks (k=5)
5. Construct Prompt with Retrieved Context
6. LLM Generates Cited Explanation
7. Post-Process: Validate Citations Against Source
8. Return Explanation with Law References
```

**Embedding Strategy:**
- Chunk legal documents by section (500-1000 tokens)
- Overlap: 50 tokens between chunks
- Metadata per chunk: `jurisdiction`, `law_id`, `section`, `effective_date`, `language`
- Filter by jurisdiction BEFORE similarity search (not after)

**Citation Format:**
```
"According to §21 StVO (German Road Traffic Act, 2024):
'Pedestrians must use sidewalks where available.'
[Source: DE-StVO-§21-2024]"
```

### 3. Learning Intelligence Engine

Adaptive learning combining progress tracking and spaced repetition.

**Responsibilities:**
- Track user performance by topic/jurisdiction
- Calculate readiness scores
- Schedule review questions (spaced repetition)
- Identify weak areas
- Generate learning recommendations

**Spaced Repetition (SM-2 Algorithm):**
```
Input: response_quality (0-5), previous_interval, easiness_factor

if response_quality >= 3:  # Correct
    if repetitions == 0: interval = 1
    elif repetitions == 1: interval = 6
    else: interval = previous_interval * easiness_factor
    
    easiness_factor = max(1.3, EF + (0.1 - (5-q) * (0.08 + (5-q) * 0.02)))
else:  # Incorrect
    repetitions = 0
    interval = 1

next_review_date = today + interval
```

**Readiness Score Calculation:**
```
readiness = (
    0.4 * topic_mastery_score +
    0.3 * recent_accuracy_trend +
    0.2 * coverage_completeness +
    0.1 * consistency_factor
)
```

---

## Component Responsibilities

Frontend-backend API contact is located in ./docs/api-contract.md.

### Frontend (React + TypeScript)

| Component | Responsibility |
|-----------|---------------|
| `AuthModule` | Login, register, session management |
| `QuizModule` | Quiz interface, timer, answer submission |
| `DashboardModule` | Progress visualization, weak areas |
| `ExplanationModule` | RAG explanation display with citations |
| `SettingsModule` | Jurisdiction/language preferences |

### Backend (Django + DRF)

| App | Responsibility |
|-----|---------------|
| `users` | Authentication, user profiles, preferences |
| `jurisdictions` | Country/language data, supported regions |
| `questions` | Question models, generation, validation |
| `quiz` | Quiz sessions, answers, scoring |
| `progress` | User progress, spaced repetition scheduling |
| `knowledge` | RAG service, document management, embeddings |

---

## Data Flow Diagrams

### User Authentication Flow
```
User → [Login Page] → POST /api/v1/auth/login
                   → Backend validates credentials
                   → Returns JWT (access + refresh tokens)
                   → Frontend stores in memory/httpOnly cookie
                   → Subsequent requests include Authorization header
```

### Quiz Session Flow
```
User → [Start Quiz] → POST /api/v1/quiz/start {jurisdiction, mode}
                   → Backend creates QuizSession
                   → Question Engine selects questions
                   → Returns quiz_id + first question

User → [Answer] → POST /api/v1/quiz/{id}/answer {question_id, answer}
              → Backend validates answer
              → Learning Engine updates user progress
              → If wrong: trigger RAG explanation
              → Returns correct/incorrect + next question

User → [Complete] → GET /api/v1/quiz/{id}/results
                 → Returns score, weak areas, recommendations
```

### RAG Explanation Flow
```
User answers incorrectly
    → Frontend requests explanation
    → POST /api/v1/questions/{id}/explain {jurisdiction}
    → Backend extracts question topic
    → Knowledge Service embeds query
    → Vector search with jurisdiction filter
    → Top-5 chunks retrieved
    → LLM generates explanation with citations
    → Citations validated against source documents
    → Response: explanation + law_references[]
```

---

## API Design


### Response Format

**Success:**
```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "timestamp": "2026-01-17T10:00:00Z",
    "request_id": "uuid"
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
    "details": { ... }
  }
}
```

---

## Database Schema

### Core Entities

```
┌─────────────────┐     ┌─────────────────┐
│   Jurisdiction  │     │      User       │
├─────────────────┤     ├─────────────────┤
│ id              │     │ id              │
│ code (DE,ES,PT) │     │ email           │
│ name            │     │ password_hash   │
│ default_language│     │ preferred_jurisdiction
│ is_active       │     │ preferred_language
└────────┬────────┘     │ created_at      │
         │              └────────┬────────┘
         │                       │
┌────────▼────────┐     ┌────────▼────────┐
│ LegalDocument   │     │  QuizSession    │
├─────────────────┤     ├─────────────────┤
│ id              │     │ id              │
│ jurisdiction_id │     │ user_id         │
│ law_code        │     │ jurisdiction_id │
│ title           │     │ mode (practice/exam)
│ effective_date  │     │ started_at      │
│ content         │     │ completed_at    │
│ language        │     │ score           │
│ embedding_status│     │ question_ids[]  │
└────────┬────────┘     └────────┬────────┘
         │                       │
┌────────▼────────┐     ┌────────▼────────┐
│ DocumentChunk   │     │   QuizAnswer    │
├─────────────────┤     ├─────────────────┤
│ id              │     │ id              │
│ document_id     │     │ session_id      │
│ section_ref     │     │ question_id     │
│ content         │     │ user_answer     │
│ embedding[]     │     │ is_correct      │
│ token_count     │     │ answered_at     │
│ chunk_index     │     │ time_spent_sec  │
└─────────────────┘     └─────────────────┘

┌─────────────────┐     ┌─────────────────┐
│    Question     │     │  UserProgress   │
├─────────────────┤     ├─────────────────┤
│ id              │     │ id              │
│ jurisdiction_id │     │ user_id         │
│ type            │     │ question_id     │
│ difficulty      │     │ attempts        │
│ topic           │     │ correct_count   │
│ content_json    │     │ last_attempt    │
│ correct_answer  │     │ next_review     │
│ source          │     │ easiness_factor │
│ validated       │     │ interval_days   │
│ explanation_cache│    └─────────────────┘
└─────────────────┘
```

### Vector Index (pgvector)

```sql
CREATE EXTENSION vector;

CREATE TABLE document_chunks (
    id SERIAL PRIMARY KEY,
    document_id INTEGER REFERENCES legal_documents(id),
    section_ref VARCHAR(100),
    content TEXT,
    embedding vector(1536),  -- OpenAI embedding dimension
    token_count INTEGER,
    chunk_index INTEGER
);

CREATE INDEX ON document_chunks 
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);
```

---

## Security Considerations

| Concern | Mitigation |
|---------|------------|
| Authentication | JWT with short-lived access tokens (15min), refresh rotation |
| Authorization | Role-based access, resource ownership validation |
| API Rate Limiting | Per-user limits on AI endpoints (cost control) |
| SQL Injection | Django ORM parameterized queries |
| XSS | React auto-escaping, CSP headers |
| CORS | Whitelist frontend origin only |
| Secrets | Environment variables, never in code |
| GDPR | User data export, deletion endpoints |

---

## Performance & Cost Management

### LLM Cost Control

| Strategy | Implementation |
|----------|---------------|
| Explanation Caching | Cache by `question_id + jurisdiction` in Redis (24h TTL) |
| Pre-generation | Generate explanations for top 100 missed questions nightly |
| Rate Limiting | Max 20 explanations/user/hour |
| Model Selection | GPT-4 for explanations, GPT-3.5 for classification |

### Caching Strategy

| Data | Cache | TTL |
|------|-------|-----|
| JWT tokens | Redis | 15 min |
| Explanation responses | Redis | 24 hours |
| Question bank per jurisdiction | Application memory | 1 hour |
| User progress summary | Redis | 5 minutes |
| Jurisdiction list | Application memory | 24 hours |

---

## Change Management

All architectural changes must:
1. Be documented in this file
2. Include rationale and impact analysis
3. Be reviewed before implementation
4. Update related component documentation
5. Maintain backward compatibility where possible
6. Include migration plan for data changes

---

## Glossary

Mapping between PROJECT.md feature names and technical components.

| PROJECT.md Term | Technical Component | Location |
|-----------------|---------------------|----------|
| Knowledge Retrieval Service | `knowledge` app | `backend/apps/knowledge/` |
| Learning Intelligence Engine | `progress` app | `backend/apps/progress/` |
| Question Engine Service | `questions` app | `backend/apps/questions/` |
| Quiz Interface | `QuizModule` | `frontend/src/modules/Quiz/` |
| Basic Progress Dashboard | `DashboardModule` | `frontend/src/modules/Dashboard/` |

---

## Related Documentation

- [PROJECT.md](PROJECT.md) — Feature roadmap and project scope
- [docs/ux-scenarios.md](docs/ux-scenarios.md) — User experience flows
- [backend/README.md](backend/README.md) — Backend implementation details
- [frontend/README.md](frontend/README.md) — Frontend implementation details
- [docs/api/](docs/api/) — API specification