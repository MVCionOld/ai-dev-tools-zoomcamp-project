# Copilot Instructions

Django + React full-stack app. Be direct.

---

## Prime Directives

1. **Read ARCHITECTURE.md first**
2. **Ask before adding dependencies**
3. **Announce refactors** — no silent changes
4. **Stay in your layer** — Views→Services→Repositories
5. **Frontend-backend contact changes** - reflect them in `../docs/api-contract.md`

---

## Stop and Ask Before

- Adding any package
- Changing API contracts
- Modifying config files
- Cross-component refactors
- Security-related changes

---

## Stack-Specific Rules

| Stack | File |
|-------|------|
| Backend | `backend/.instructions.md` |
| Frontend | `frontend/.instructions.md` |

---

## Code Standards

- Readable > clever
- Handle errors
- Match existing patterns

---

## Checklist

- [ ] Aligns with ARCHITECTURE.md
- [ ] No unapproved dependencies
- [ ] Layer boundaries respected
- [ ] Errors handled