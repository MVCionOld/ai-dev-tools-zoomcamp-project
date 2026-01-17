# Documentation

Comprehensive project documentation. Keep clear, accurate, synchronized with code.

## Structure

```
docs/
├── README.md           # This file - documentation guidelines
├── architecture/       # Architecture details
├── api/               # API specs
├── guides/            # How-to guides
└── decisions/         # Architecture Decision Records (ADRs)
```

## Standards

**Writing:**
- Clear, concise language
- Avoid unnecessary jargon
- Define technical terms
- Active voice
- Write for audience

**Structure:**
- Descriptive headings
- Logical organization
- Table of contents for long docs
- Lists and bullets
- Consistent styling

**Content Types:**
- Architecture: System design, patterns, decisions
- API: Endpoints, schemas, auth, errors
- Guides: Step-by-step instructions
- Reference: Features, config, commands, glossary

## Markdown Best Practices

**Headings:**
```
# H1 - Document Title (one per doc)
## H2 - Major Sections
### H3 - Subsections
```

**Code Blocks:**
Specify language for syntax highlighting. Example:
- Start with triple backticks and language name
- Add code content
- End with triple backticks

**Links:**
```markdown
[Descriptive text](path/to/file.md)
```

**Lists:**
```markdown
- Unordered item
  - Nested item

1. Ordered item
2. Second item
```

**Emphasis:**
```markdown
*italic*
**bold**
`inline code`
```

## Document Types

**README:**
Every directory needs README.md with:
- Purpose
- Overview of contents
- Usage instructions
- Related docs links

**ADRs:**
```markdown
# ADR [Number]: [Title]
## Status: [Proposed/Accepted/Deprecated]
## Context: Issue being addressed
## Decision: What we're doing
## Consequences: Results
```

**API Docs:**
```markdown
### [METHOD] /api/v1/resource
Description, Auth, Request, Response, Example
```

## Code Examples

**Best Practices:**
- Include necessary imports
- Complete, runnable examples
- Descriptive variable names
- Add comments for complex parts
- Keep focused
- Test all examples
- Update with API changes

### Example Template

Structure examples with:
- Title describing what is demonstrated
- Code block with language specified
- Expected output section

## Diagrams and Visual Aids

**When to Use:**
- Architecture explanations
- Data flow
- Relationships
- Processes
- Complex concepts

**Types:**
- Architecture diagrams
- Flow diagrams
- Sequence diagrams

**ASCII Example:**
```
┌─────────────┐
│  Component  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Another   │
└─────────────┘
```

## Maintenance

**Regular Reviews:**
- Quarterly documentation review
- Update immediately for code changes
- Check links periodically
- Verify examples work
- Remove outdated info

**Deprecation:**
1. Mark as deprecated
2. Explain why it is deprecated
3. Provide migration path
4. Set removal timeline
5. Update related docs

**Versioning:**
- Version with major releases
- Maintain for supported versions
- Archive old versions
- Mark version clearly

## Organization

**File Naming:**
- Lowercase with hyphens: `api-reference.md`
- Descriptive names
- Consistent conventions

**Directory:**
- Group related docs
- Shallow structure
- Clear names
- README in each directory

## Quality Standards

**Content:**
- Accurate
- Complete
- Clear
- Concise
- Current

**Technical:**
- Code examples tested
- Links verified
- Proper markdown formatting
- Consistent styling
- Correct syntax highlighting

## Templates

**Feature Documentation:**
```markdown
# Feature Name
## Overview
## Use Cases
## How It Works
## Usage
## Configuration
## Best Practices
## Troubleshooting
```

**Tutorial:**
```markdown
# Tutorial: [Title]
## What You'll Build
## Prerequisites
## Steps
## Next Steps
## Further Reading
```

## Integration with Development

**Documentation as Code:**
- Store with code in version control
- Review in PRs
- Use CI validation
- Keep in sync
- Version together

**In Pull Requests:**
- Include doc updates
- Update API docs for API changes
- Add guides for features
- Update architecture for structural changes
- Include ADRs for decisions

## Resources

- `ARCHITECTURE.md` - Architecture documentation
- `CONTRIBUTING.md` - Contribution process
- `.editorconfig` - Formatting standards
- `.github/copilot-instructions.md` - Copilot usage
- Component READMEs - Specific topics

## Continuous Improvement

**Feedback:**
- Welcome documentation feedback
- Track issues
- Conduct surveys
- Monitor usage
- Iterate

**Metrics:**
- Documentation coverage
- Outdated documents
- Broken links
- User feedback
- Common questions
