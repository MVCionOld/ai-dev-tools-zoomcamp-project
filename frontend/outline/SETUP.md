# Frontend UI outline

This is instruction to clone the outline of frontend.

## Command

```bash
git clone https://github.com/MVCionOld/ai-dev-tools-zoomcamp-project-demo.git
cd ./ai-dev-tools-zoomcamp-project-demo
```

## Source

This UI is generated with help of https://lovable.dev/  

### Lovable.dev Prompt

Current project context's requirements is used  to write an effective Lovable.dev prompt, which is following:

```
Build a **driving license exam preparation web app** (React + TypeScript + Tailwind CSS) with JWT authentication and REST API integration. Desktop-first, responsive design.

## Core Tech Requirements
- React 18 + TypeScript + Vite
- TanStack Query (React Query) for server state
- Zustand for client state
- React Router for routing
- Tailwind CSS for styling
- Axios for HTTP (base URL: /api/v1)

## API Response Format
All endpoints return: `{ success: boolean, data: {...}, error?: { code, message } }`
Store JWT tokens (access_token, refresh_token) in memory/localStorage.

---

## Pages & Features

### 1. Welcome/Landing Page (public)
- Hero: "Master Your Driving Theory Test" with tagline about AI-powered practice
- 3 country cards with flags: 🇩🇪 Germany, 🇪🇸 Spain, 🇵🇹 Portugal
- Feature highlights: personalized practice, legal citations, multiple languages
- CTAs: "Try Sample Quiz" and "Create Free Account"

### 2. Auth Pages
**Login:** Email + password form, "Forgot password?" link, "Create account" link
**Register:** Email, password, confirm password with validation (min 8 chars, 1 uppercase, 1 number)
- After register, show "Check your email" verification message

### 3. Onboarding Flow (post-registration)
- Step 1: Country selection (3 cards with flags)
- Step 2: Language selection (radio buttons, varies by country - DE has de/en/pt/es)
- Progress indicator, stepper UI

### 4. Dashboard (authenticated)
- Greeting: "Welcome back, [Name]!"
- Current jurisdiction badge with "Change" link
- Two mode cards side-by-side:
  - **Practice Mode**: "No time limit, hints available" → [Start Practice]
  - **Mock Exam**: "30 questions, 45 minutes" → [Start Exam]
- Progress stats card: questions practiced, accuracy %, current streak 🔥
- Optional: weak areas summary

### 5. Quiz Configuration Modal
- Topic checkboxes: Right of Way, Speed Limits, Road Signs, Parking, etc.
- Question count dropdown (10, 15, 20, 30)
- Difficulty selector (Beginner, Mixed, Exam-ready)

### 6. Quiz Page (Practice Mode)
- Header: "Practice Mode | Question X of Y | [Exit Quiz]"
- Question text (large)
- Optional image container for road sign questions
- 4 answer options (A, B, C, D) as selectable cards
- "Hint" button (shows tooltip)
- "Submit Answer" button (disabled until selection)
- After submit: green/red feedback, "See Explanation" button for wrong answers
- "Next Question" to proceed

### 7. Quiz Page (Exam Mode)
- Header: "Mock Exam | Q X/30 | ⏱️ MM:SS remaining | [Finish Early]"
- Timer turns orange at 5min, red at 1min
- No hints, no going back
- Confirm dialog before exit

### 8. Results Page
- Large score display: "28/30 - 93% - PASSED" (or FAILED in red)
- Pass threshold: 70% for practice, 90% for exam
- Time used vs total
- Topic breakdown with progress bars per category
- Weak areas highlighted
- CTAs: [Review Mistakes] [Dashboard] [Try Again]

### 9. Explanation Modal/Panel (RAG)
- Triggered by "Why was I wrong?" button
- Loading state: "Consulting traffic regulations..."
- Display: explanation text + law citation box with:
  - Law code (e.g., StVO)
  - Section (e.g., §3(3))
  - Quoted legal text
  - Source ID badge
- Bookmark button

### 10. Settings Page
- Change jurisdiction/language
- Account preferences
- Logout

---

## UI Components Needed
- Button (primary, secondary, ghost, danger variants)
- Input with validation states
- Card component
- Modal/Dialog
- Progress bar
- Badge/Chip
- Timer display
- Toast notifications
- Skeleton loaders
- Empty states

## Design Style
- Clean, modern, educational feel
- Primary color: Blue (trust, learning)
- Success: Green, Error: Red, Warning: Orange
- Rounded corners, subtle shadows
- Clear typography hierarchy
- Icon usage: Lucide icons

## State Management
- Auth context with user, tokens, login/logout functions
- Quiz state: current question, answers, timer
- UI state: modals, loading, errors

## Routing Structure
/ → Landing
/login → Login
/register → Register
/onboarding → Onboarding wizard
/dashboard → Main dashboard (protected)
/quiz/:id → Active quiz (protected)
/results/:id → Quiz results (protected)
/settings → User settings (protected)

## Key Interactions
- Smooth page transitions
- Loading skeletons while fetching
- Optimistic UI for answer selection
- Timer countdown animation
- Answer feedback animations (correct=bounce, wrong=shake)

Do NOT implement actual API calls yet - use mock data and placeholder handlers. Focus on complete UI/UX with all states (loading, empty, error, success).
```