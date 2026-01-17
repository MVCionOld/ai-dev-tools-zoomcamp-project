# GitHub Copilot Instructions

Constrain Copilot to work within established architectural patterns.

## Core Constraints

### 1. Respect the Architecture

**ALWAYS:**
- Review `ARCHITECTURE.md` before suggesting code
- Maintain frontend/backend separation
- Respect component boundaries
- Follow established patterns
- Use defined interfaces for communication

**NEVER:**
- Violate architectural principles
- Bypass component boundaries
- Mix layer concerns
- Propose tight coupling
- Ignore documented architecture

### 2. Ask Before Adding Tools

**REQUIRED APPROVAL:**
- Frameworks or libraries
- Build/bundling tools
- Testing frameworks
- Linters/formatters
- Database systems
- External services/APIs
- Development dependencies

**NEVER:**
- Add dependencies without approval
- Install packages silently
- Change build configs without discussion

### 3. Avoid Silent Refactors

**WHEN REFACTORING:**
- Announce intention
- Explain benefits and risks
- Identify affected components
- Update documentation
- Get approval for large changes

**NEVER:**
- Refactor without notification
- Change working code without justification
- Modify multiple components silently
- Restructure without updating docs

### 4. Update Documentation on Structural Changes

**UPDATE:**
- `ARCHITECTURE.md` for architectural changes
- Component READMEs for features
- `CONTRIBUTING.md` for process changes

**STRUCTURAL CHANGES:**
- New directories/components
- Modified boundaries
- API interface changes
- New patterns
- Data flow updates
- Security model changes

## Code Generation

### Quality
- Readable, maintainable code
- Follow language conventions
- Descriptive names
- Necessary error handling
- Comments for complex logic only

### Consistency
- Match existing style
- Follow component patterns
- Respect `.editorconfig`
- Consistent naming

### Security
- Validate inputs
- No hardcoded credentials
- Secure communication
- Proper authentication
- Prevent XSS, SQL injection

## Suggestions

### Encouraged
- Boilerplate following patterns
- Error handling per conventions
- Tests matching structure
- Documentation updates
- Code completion within bounds

### Discouraged
- Violating constraints
- Requiring new dependencies
- Large refactors without approval
- Config file changes
- Interface modifications without review

## Component Constraints

**Frontend:**
- Separate UI/business logic
- Established state management
- Validate before API calls
- Handle API errors

**Backend:**
- Input validation
- RESTful/GraphQL conventions
- Business logic in service layer
- Repository pattern for data
- Appropriate HTTP status codes

**Documentation:**
- Clear, concise language
- Markdown best practices
- Consistent formatting

## Testing

- Match existing structure
- Cover edge cases
- Mock dependencies
- No new frameworks without approval
- Descriptive test names

## API Development

- Define contracts first
- Document endpoints
- Version appropriately
- Validate inputs
- Consistent responses
- Meaningful errors
- Never break contracts without discussion
- Document breaking changes

## Review Checklist

Before accepting suggestions:
- [ ] Aligns with ARCHITECTURE.md
- [ ] No new dependencies without approval
- [ ] Follows conventions
- [ ] Includes error handling
- [ ] Documentation updated if needed
- [ ] Respects boundaries
- [ ] Matches code style
- [ ] No security vulnerabilities
- [ ] Not premature optimization
- [ ] No silent refactoring

## Escalation

**STOP and ask for review when:**
- Violates constraints
- Requires architectural discussion
- Needs tool approval
- Involves major refactoring
- Changes interfaces
- Has security implications