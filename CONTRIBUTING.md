# Contributing Guidelines

## Overview

This project uses GitHub Copilot as the primary development assistant. All contributions must follow the established architectural patterns and guidelines.

## Development Workflow

### 1. Understand the Architecture
- Read `ARCHITECTURE.md` thoroughly before making changes
- Understand component boundaries and responsibilities
- Review existing patterns and conventions
- Consult `.github/copilot-instructions.md` for Copilot constraints

### 2. Plan Your Changes
- Identify which component(s) your changes affect
- Document the purpose and scope of your changes
- Consider impact on other components
- Ensure changes align with architectural principles

### 3. Implementation Guidelines
- Follow established coding standards (see `.editorconfig`)
- Use GitHub Copilot to assist with implementation
- Respect architectural boundaries
- Write self-documenting code with clear naming
- Add comments for complex logic

### 4. Documentation Requirements
- Update component READMEs if adding new features
- Document API changes in relevant files
- Update ARCHITECTURE.md for structural changes
- Keep documentation synchronized with code

### 5. Code Review
- Self-review changes before submitting
- Ensure no violations of architectural constraints
- Verify documentation is updated
- Test changes in isolation when possible

## Working with GitHub Copilot

### Best Practices
- Provide clear context in comments before requesting code
- Review and understand all Copilot suggestions
- Verify suggestions align with project architecture
- Modify suggestions to match project conventions
- Use Copilot for repetitive tasks and boilerplate

### Constraints
- Always ask before adding new tools or dependencies
- Respect the established architecture
- Avoid silent refactoring without documentation
- Update documentation when making structural changes
- Do not bypass architectural patterns with Copilot suggestions

## Code Standards

### General Principles
- Write clear, readable code
- Prefer explicitness over cleverness
- Keep functions small and focused
- Follow single responsibility principle
- Maintain consistent naming conventions

### File Organization
- Group related functionality together
- Use clear directory structures
- Keep component boundaries clean
- Separate concerns appropriately

### Naming Conventions
- Use descriptive names for variables and functions
- Follow language-specific conventions
- Be consistent across the codebase
- Avoid abbreviations unless widely understood

## Component-Specific Guidelines

### Frontend Development
- Follow component-based architecture
- Separate presentational and container components
- Manage state appropriately
- Optimize for performance and user experience
- Refer to `frontend/README.md` for details

### Backend Development
- Implement clean API interfaces
- Validate all inputs
- Handle errors gracefully
- Follow RESTful or GraphQL conventions
- Refer to `backend/README.md` for details

### Documentation
- Write clear, concise documentation
- Use proper markdown formatting
- Include code examples where appropriate
- Keep documentation up to date
- Refer to `docs/README.md` for details

## Adding Dependencies

Before adding any new dependency:
1. Evaluate if it is truly necessary
2. Consider security implications
3. Check for maintained and stable alternatives
4. Document the reason for addition
5. Get approval from the team
6. Update relevant documentation

## Structural Changes

Structural changes require:
1. Proposal and discussion
2. Update to ARCHITECTURE.md
3. Migration plan if needed
4. Documentation updates across all affected components
5. Team review and approval

## Quality Standards

### Code Quality
- Code must be readable and maintainable
- Follow DRY (Don't Repeat Yourself) principle
- Write modular, reusable components
- Handle edge cases appropriately
- Include error handling

### Documentation Quality
- Documentation must be clear and accurate
- Use proper grammar and formatting
- Include examples where helpful
- Keep documentation concise but complete
- Update documentation with code changes

## Git Workflow

### Commits
- Write clear, descriptive commit messages
- Make atomic commits (one logical change per commit)
- Reference issues when applicable
- Keep commits focused and small

### Branches
- Use descriptive branch names
- Keep branches focused on single features or fixes
- Regularly sync with main branch
- Delete branches after merging

## Questions and Support

- Review existing documentation first
- Check ARCHITECTURE.md for design guidance
- Consult component READMEs for specific questions
- Review .github/copilot-instructions.md for Copilot usage
- Ask the team when uncertain

## Anti-Patterns to Avoid

- Making changes without understanding architecture
- Adding dependencies without approval
- Silent refactoring across multiple components
- Ignoring established conventions
- Bypassing architectural constraints
- Updating code without updating documentation
- Using Copilot suggestions blindly without review