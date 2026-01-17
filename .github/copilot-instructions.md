# GitHub Copilot Instructions

## Purpose

These instructions constrain GitHub Copilot to work within the established architectural patterns and development practices of this repository.

## Core Constraints

### 1. Respect the Architecture

**ALWAYS:**
- Review `ARCHITECTURE.md` before suggesting code changes
- Maintain separation between frontend and backend components
- Respect component boundaries and responsibilities
- Follow established design patterns
- Keep inter-component communication through defined interfaces

**NEVER:**
- Suggest code that violates architectural principles
- Bypass component boundaries
- Mix concerns between layers
- Propose tight coupling between components
- Ignore the documented architecture

### 2. Ask Before Adding Tools

**REQUIRED APPROVAL:**
- New frameworks or libraries
- Build tools or bundlers
- Testing frameworks
- Linting or formatting tools
- Database systems
- External services or APIs
- Development dependencies

**PROCESS:**
1. Explain the need for the new tool
2. Describe the problem it solves
3. Consider existing alternatives
4. Wait for explicit approval
5. Document the addition in relevant files

**NEVER:**
- Add dependencies without approval
- Install packages silently
- Change build configurations without discussion
- Introduce new tools for convenience alone

### 3. Avoid Silent Refactors

**WHEN REFACTORING:**
- Announce the intention to refactor
- Explain the benefits and risks
- Identify all affected components
- Update relevant documentation
- Get approval for large-scale changes

**NEVER:**
- Refactor code without notification
- Change working code without justification
- Modify multiple components silently
- Rename files or directories without documentation
- Restructure without updating architecture docs

### 4. Update Documentation on Structural Changes

**DOCUMENTATION REQUIREMENTS:**
- Update `ARCHITECTURE.md` for architectural changes
- Update component READMEs for feature additions
- Update `CONTRIBUTING.md` for process changes
- Keep documentation synchronized with code
- Document breaking changes clearly

**STRUCTURAL CHANGES INCLUDE:**
- New directories or components
- Modified component boundaries
- Changed API interfaces
- New architectural patterns
- Updated data flows
- Security model changes

## Code Generation Guidelines

### Code Quality
- Generate readable, maintainable code
- Follow language-specific conventions
- Use descriptive variable and function names
- Include necessary error handling
- Add comments for complex logic only
- Prefer clarity over cleverness

### Consistency
- Match existing code style in the file
- Follow patterns used in the component
- Respect `.editorconfig` settings
- Use consistent naming across suggestions
- Maintain alignment with project conventions

### Security
- Validate all user inputs
- Avoid hardcoded credentials
- Use secure communication methods
- Implement proper authentication checks
- Follow security best practices
- Prevent common vulnerabilities (XSS, SQL injection, etc.)

## Suggestion Behavior

### When Suggesting Code
1. Understand the context from surrounding code
2. Verify alignment with architecture
3. Check for existing patterns to follow
4. Consider impact on other components
5. Ensure documentation needs are met

### Types of Suggestions

**ENCOURAGED:**
- Boilerplate code following established patterns
- Error handling based on project conventions
- Unit tests matching existing test structure
- Documentation updates for new features
- Code completion within architectural bounds

**DISCOURAGED:**
- Code that violates architectural constraints
- Suggestions requiring new dependencies
- Large-scale refactoring without approval
- Changes to build or configuration files
- Modifications to shared interfaces without review

## Component-Specific Constraints

### Frontend
- Keep UI logic separate from business logic
- Use established state management patterns
- Follow component structure conventions
- Validate user input before API calls
- Handle API errors gracefully

### Backend
- Implement proper input validation
- Follow RESTful or GraphQL conventions
- Keep business logic in service layer
- Use repository pattern for data access
- Return appropriate HTTP status codes

### Documentation
- Use clear, concise language
- Follow markdown best practices
- Include code examples when helpful
- Keep formatting consistent
- Update related documents together

## Testing Guidance

### Test Generation
- Match existing test structure and style
- Cover happy paths and edge cases
- Use established testing patterns
- Mock external dependencies appropriately
- Keep tests focused and isolated

### Test Constraints
- Do not add new testing frameworks without approval
- Follow existing test organization
- Maintain test independence
- Use descriptive test names
- Keep tests maintainable

## API Development

### API Constraints
- Define clear contracts before implementation
- Document all endpoints
- Version APIs appropriately
- Validate all inputs
- Return consistent response formats
- Handle errors with meaningful messages

### API Changes
- Never break existing API contracts without discussion
- Document breaking changes clearly
- Provide migration guides when needed
- Update API documentation with code
- Consider backward compatibility

## Performance Considerations

- Suggest efficient algorithms and data structures
- Avoid premature optimization
- Consider scalability in suggestions
- Flag potential performance issues
- Recommend caching where appropriate

## Error Handling

- Always include appropriate error handling
- Use consistent error handling patterns
- Provide meaningful error messages
- Log errors appropriately
- Handle edge cases gracefully

## Review Checklist for Copilot Suggestions

Before accepting any Copilot suggestion, verify:
- [ ] Aligns with architecture documented in ARCHITECTURE.md
- [ ] Does not introduce new dependencies without approval
- [ ] Follows established coding conventions
- [ ] Includes necessary error handling
- [ ] Does not require documentation updates OR documentation is updated
- [ ] Respects component boundaries
- [ ] Matches existing code style
- [ ] Does not introduce security vulnerabilities
- [ ] Is necessary and not premature optimization
- [ ] Does not silently refactor existing working code

## Escalation

When Copilot suggests something that:
- Violates these constraints
- Requires architectural discussion
- Needs approval for new tools
- Involves major refactoring
- Changes component interfaces
- Has security implications

**STOP and ask for human review before proceeding.**

## Summary

GitHub Copilot is a powerful assistant, but must work within the established guidelines of this repository. These constraints ensure:
- Architectural integrity is maintained
- Code quality remains high
- Documentation stays synchronized
- Changes are intentional and reviewed
- The codebase remains maintainable

Use Copilot to accelerate development, not to bypass best practices.