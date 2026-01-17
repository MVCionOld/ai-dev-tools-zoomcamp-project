# Contributing Guidelines

GitHub Copilot is the primary development assistant. Follow established patterns and guidelines.

## Development Workflow

### 1. Understand the Architecture
- Read `ARCHITECTURE.md`
- Understand component boundaries
- Review patterns and conventions
- Check `.github/copilot-instructions.md`

### 2. Plan Changes
- Identify affected components
- Document purpose and scope
- Consider impact
- Align with architectural principles

### 3. Implementation
- Follow `.editorconfig` standards
- Use Copilot for assistance
- Respect architectural boundaries
- Write self-documenting code
- Comment complex logic only

### 4. Documentation
- Update component READMEs for features
- Document API changes
- Update ARCHITECTURE.md for structural changes
- Keep docs synchronized

### 5. Code Review
- Self-review before submitting
- Ensure no constraint violations
- Verify documentation updates
- Test in isolation when possible

## Copilot Usage

**Best Practices:**
- Provide clear context
- Review all suggestions
- Verify alignment with architecture
- Match project conventions
- Use for repetitive tasks

**Constraints:**
- Ask before adding tools/dependencies
- Respect architecture
- No silent refactoring
- Update docs on structural changes
- Don't bypass patterns

## Code Standards

**General:**
- Clear, readable code
- Explicitness over cleverness
- Small, focused functions
- Single responsibility
- Consistent naming

**Organization:**
- Group related functionality
- Clear directory structures
- Clean component boundaries
- Appropriate separation

## Component Guidelines

**Frontend:**
- Component-based architecture
- Separate presentational/container components
- Appropriate state management
- Performance optimization
- See `frontend/README.md`

**Backend:**
- Clean API interfaces
- Input validation
- Graceful error handling
- RESTful/GraphQL conventions
- See `backend/README.md`

**Documentation:**
- Clear, concise
- Proper markdown
- Include examples
- Keep updated
- See `docs/README.md`

## Adding Dependencies

Before adding:
1. Evaluate necessity
2. Consider security
3. Check alternatives
4. Document reason
5. Get approval
6. Update docs

## Structural Changes

Require:
1. Proposal and discussion
2. ARCHITECTURE.md update
3. Migration plan if needed
4. Documentation updates
5. Team review

## Quality Standards

**Code:**
- Readable and maintainable
- DRY principle
- Modular, reusable
- Handle edge cases
- Error handling

**Documentation:**
- Clear and accurate
- Proper formatting
- Include examples
- Concise but complete
- Update with code

## Git Workflow

**Commits:**
- Clear messages
- Atomic commits
- Reference issues
- Focused and small

**Branches:**
- Descriptive names
- Single feature/fix focus
- Sync with main regularly
- Delete after merge

## Anti-Patterns

Avoid:
- Changes without understanding architecture
- Dependencies without approval
- Silent cross-component refactoring
- Ignoring conventions
- Bypassing constraints
- Updating code without docs
- Blind Copilot acceptance