# Frontend

User interface and client-side logic. Communicates with backend through defined APIs.

## Responsibilities

- UI rendering and management
- User interaction handling
- Client-side validation
- State management
- API consumption
- Client-side routing
- Error display

## Structure

```
frontend/
├── components/       # Reusable UI components
├── pages/           # Page-level components
├── services/        # API client
├── utils/           # Utility functions
└── styles/          # Global styles
```

## Principles

1. **Component-Based**: Small, reusable components
2. **Separation of Concerns**: Presentation vs business logic
3. **Unidirectional Data Flow**: Predictable state updates
4. **API Abstraction**: Isolate API calls in services
5. **Responsive Design**: Multi-device support

## Components

**Presentational:**
- Focus on appearance
- Receive data via props
- No business logic
- Reusable

**Container:**
- Focus on functionality
- Manage state and effects
- Handle data fetching
- Compose presentational components

## State Management

- Keep state close to usage
- Lift when shared across components
- Use appropriate patterns
- Avoid unnecessary global state
- Document structure

## API Integration

- Centralize in service layer
- Handle loading states
- Proper error handling
- Consistent formats
- Cache when appropriate

Pattern:
```
Service → Request → Backend
        ← Response ←
Component ← State Update ←
```

## Styling

- Consistent naming
- Mobile-first responsive
- Design system consistency
- Performance optimization

## Code Standards

**File Naming:**
- Clear, descriptive names
- Follow conventions
- Be consistent

**Organization:**
- One component per file
- Collocate related files
- Small, focused files

## Testing

**Unit Tests:**
- Test components in isolation
- Mock dependencies
- Focus on behavior

**Integration Tests:**
- Component interactions
- API integration
- User workflows

## Security

- Validate user input
- Sanitize data before display
- Secure authentication flows
- No exposed secrets
- Prevent XSS, CSRF

## API Communication

**Request:**
- Consistent HTTP methods
- Proper headers
- Auth tokens
- Formatted bodies

**Response:**
- Handle success/errors
- Retry logic where appropriate
- User-friendly messages
- Update UI

## Performance

- Code splitting
- Lazy loading
- Bundle optimization
- Minimize re-renders
- Caching strategies

## Accessibility

- WCAG guidelines
- Semantic HTML
- ARIA labels
- Keyboard navigation
- Screen reader support

## Integration with Backend

**Protocol:**
- RESTful or GraphQL
- JSON format
- Proper HTTP status codes
- Auth via headers

**Contract:**
- Document endpoints used
- Define schemas
- Specify error handling
- Version contracts
- Coordinate changes

## Resources

- `ARCHITECTURE.md` - System design
- `CONTRIBUTING.md` - Contribution guidelines
- `.editorconfig` - Coding standards
- `.github/copilot-instructions.md` - Copilot usage
- `backend/README.md` - API documentation
