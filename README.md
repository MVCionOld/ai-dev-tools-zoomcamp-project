# AI-Powered Driving License Exam Prep Platform

See [PROJECT.md](./PROJECT.md) for problem statement and features.

## Quick Links

| Document | Purpose |
|----------|---------|
| [SETUP.md](./SETUP.md) | **Start here** — Prerequisites, install, run |
| [docs/MVP.md](./docs/MVP.md) | Sprint 1-2 scope, Definition of Done |
| [docs/api-contract.md](./docs/api-contract.md) | Full API request/response schemas |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | System design, tech stack, layers |
| [CONTRIBUTING.md](./CONTRIBUTING.md) | Git workflow, PR process |

## Repository Structure

```
├── backend/           # Django + DRF API
├── frontend/          # React + TypeScript SPA
├── docs/              # API contract, MVP scope, UX scenarios
└── .github/           # Copilot instructions
```

## Development

```bash
# Backend
cd backend && uv sync && uv run python manage.py runserver

# Frontend  
cd frontend && npm install && npm run dev
```

See [SETUP.md](./SETUP.md) for complete instructions.
