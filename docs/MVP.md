# MVP Scope — Sprint 1-2

**Goal:** User can register, take a quiz, and see results. No AI features yet.

---

## Sprint 1: Foundation (Week 1-2)

### Backend
- [ ] Django project setup with settings split (base/dev/prod)
- [ ] User model with email auth
- [ ] JWT authentication (register, login, refresh)
- [ ] Jurisdiction model with seed data (DE, ES, PT)
- [ ] Question model with seed data (30 curated questions)
- [ ] Basic API response format middleware

### Frontend
- [ ] Vite + React + TypeScript setup
- [ ] TanStack Query + Zustand configuration
- [ ] Auth pages: Login, Register
- [ ] Jurisdiction selection (onboarding)
- [ ] Basic routing

### Deliverable
User can register, log in, select jurisdiction.

---

## Sprint 2: Core Quiz (Week 3-4)

### Backend
- [ ] Quiz session model
- [ ] Start quiz endpoint
- [ ] Submit answer endpoint
- [ ] Quiz results endpoint
- [ ] Basic progress tracking (attempts, correct count)

### Frontend
- [ ] Quiz start flow (select mode, question count)
- [ ] Question display component
- [ ] Answer selection + submission
- [ ] Results page with score breakdown
- [ ] Basic dashboard showing stats

### Deliverable
User can complete a full quiz and see results.

---

## NOT in MVP

- RAG explanations (Sprint 5-6)
- Spaced repetition (Sprint 7)
- AI question generation
- Bookmarks
- Gamification
- Admin portal

---

## Definition of Done

- [ ] All endpoints return standard response format
- [ ] Frontend handles loading/error states
- [ ] Basic test coverage (>50%)
- [ ] Can complete full user flow: register → quiz → results
