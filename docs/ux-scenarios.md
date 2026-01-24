# UX Scenarios — Driving License Exam Prep Platform

Step-by-step user experience flows aligned with technical architecture.

> **Cross-Reference:** Technical implementation details in [ARCHITECTURE.md](../ARCHITECTURE.md)

---

## Table of Contents

1. [User Personas](#user-personas)
2. [Scenario 1: First-Time Visitor (Guest)](#scenario-1-first-time-visitor-guest)
3. [Scenario 2: User Registration & Onboarding](#scenario-2-user-registration--onboarding)
4. [Scenario 3: Starting a Practice Quiz](#scenario-3-starting-a-practice-quiz)
5. [Scenario 4: Taking a Timed Mock Exam](#scenario-4-taking-a-timed-mock-exam)
6. [Scenario 5: Getting an Explanation (RAG)](#scenario-5-getting-an-explanation-rag)
7. [Scenario 6: Reviewing Progress Dashboard](#scenario-6-reviewing-progress-dashboard)
8. [Scenario 7: Spaced Repetition Review Session](#scenario-7-spaced-repetition-review-session)
9. [Scenario 8: Bookmarking Questions](#scenario-8-bookmarking-questions)
10. [Scenario 9: Changing Jurisdiction/Language](#scenario-9-changing-jurisdictionlanguage)
11. [Scenario 10: Reporting a Question Issue](#scenario-10-reporting-a-question-issue)
12. [Error States & Edge Cases](#error-states--edge-cases)

---

## User Personas

### Maria — Immigrant Preparing for German License
- **Background:** Brazilian, moved to Germany 6 months ago
- **Goal:** Pass the German driving theory test in Portuguese
- **Pain Points:** Official materials only in German, unfamiliar with local rules
- **Tech Comfort:** Moderate, uses smartphone daily, prefers desktop for studying

### Hans — Native Refreshing Knowledge
- **Background:** German, license expired, needs to retake theory
- **Goal:** Quickly refresh knowledge and pass the exam
- **Pain Points:** Forgot many rules, wants efficient practice
- **Tech Comfort:** High, developer, appreciates good UX

### Sofia — Expat Moving Between Countries
- **Background:** Portuguese, lived in Spain, now moving to Germany
- **Goal:** Understand differences between traffic laws in different countries
- **Pain Points:** Confused about which rules apply where
- **Tech Comfort:** High, works in marketing

---

## Scenario 1: First-Time Visitor (Guest)

### User Goal
Understand what the platform offers before creating an account.

### Step-by-Step Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                        WELCOME PAGE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  🚗 Master Your Driving Theory Test                              │
│                                                                  │
│  AI-powered practice tests with real legal explanations          │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │  🇩🇪 Germany  │  │  🇪🇸 Spain    │  │  🇵🇹 Portugal │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│                                                                  │
│  ✓ Personalized practice based on your weak areas               │
│  ✓ Explanations that cite actual traffic laws                   │
│  ✓ Multiple languages available                                  │
│                                                                  │
│  [Try a Sample Quiz]        [Create Free Account]               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Step | User Action | System Response | Technical Reference |
|------|-------------|-----------------|---------------------|
| 1 | Lands on homepage | Display welcome page with value proposition | Static page, no auth required |
| 2 | Clicks "Try a Sample Quiz" | Show country selection modal | `GET /api/v1/jurisdictions` |
| 3 | Selects "Germany" | Load 5 sample questions (no account needed) | Limited guest quiz, no progress saved |
| 4 | Completes sample quiz | Show results + prompt to register | Display conversion CTA |
| 5 | Clicks "Create Free Account" | Navigate to registration page | Route to `/register` |

### UI States

- **Loading:** Skeleton cards for country options
- **Error:** "Unable to load countries. Please refresh."
- **Success:** Smooth transition to sample quiz

### Technical Notes

- Sample quiz uses pre-cached questions (no AI generation for guests)
- No progress saved for guests
- Session tracked for analytics (conversion funnel)

---

## Scenario 2: User Registration & Onboarding

### User Goal
Create an account and set up preferences for personalized learning.

### Step-by-Step Flow

```
Step 1: Registration Form
┌─────────────────────────────────────────┐
│         Create Your Account             │
├─────────────────────────────────────────┤
│  Email:      [_____________________]    │
│  Password:   [_____________________]    │
│  Confirm:    [_____________________]    │
│                                         │
│  [Create Account]                       │
│                                         │
│  Already have an account? [Log in]      │
└─────────────────────────────────────────┘

Step 2: Email Verification
┌─────────────────────────────────────────┐
│         Check Your Email 📧             │
├─────────────────────────────────────────┤
│  We sent a verification link to:        │
│  maria@example.com                      │
│                                         │
│  [Resend Email]   [Change Email]        │
└─────────────────────────────────────────┘

Step 3: Onboarding - Country Selection
┌─────────────────────────────────────────┐
│    Where are you taking your exam?      │
├─────────────────────────────────────────┤
│  ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │🇩🇪       │ │🇪🇸       │ │🇵🇹       │   │
│  │ Germany │ │ Spain   │ │Portugal │   │
│  └─────────┘ └─────────┘ └─────────┘   │
│                                         │
│  [Continue]                             │
└─────────────────────────────────────────┘

Step 4: Onboarding - Language Selection
┌─────────────────────────────────────────┐
│    What language do you prefer?         │
├─────────────────────────────────────────┤
│  Available for Germany:                 │
│  ○ Deutsch (German)                     │
│  ○ English                              │
│  ○ Português (Portuguese)               │
│  ○ Español (Spanish)                    │
│                                         │
│  [Start Learning]                       │
└─────────────────────────────────────────┘
```

| Step | User Action | System Response | API Call |
|------|-------------|-----------------|----------|
| 1 | Fills registration form | Validate email format, password strength | Client-side validation |
| 2 | Clicks "Create Account" | Create user, send verification email | `POST /api/v1/auth/register` |
| 3 | Clicks email link | Verify email, redirect to onboarding | `POST /api/v1/auth/verify-email` |
| 4 | Selects country | Store preference, show language options | `GET /api/v1/jurisdictions/{code}/languages` |
| 5 | Selects language | Save preferences, redirect to dashboard | `PATCH /api/v1/users/me/preferences` |

### Validation Rules

| Field | Rules |
|-------|-------|
| Email | Valid format, not already registered |
| Password | Min 8 chars, 1 uppercase, 1 number |
| Confirm | Must match password |

### Error States

- **Email taken:** "This email is already registered. [Log in instead]"
- **Weak password:** Show strength indicator with requirements
- **Verification expired:** "Link expired. [Resend verification email]"

---

## Scenario 3: Starting a Practice Quiz

### User Goal
Practice questions at their own pace without time pressure.

### Step-by-Step Flow

```
Step 1: Dashboard - Start Quiz
┌─────────────────────────────────────────────────────────────────┐
│  Welcome back, Maria! 👋                    [Settings] [Logout] │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  🇩🇪 Germany • Português                    [Change]             │
│                                                                  │
│  ┌─────────────────────┐  ┌─────────────────────┐               │
│  │   Practice Mode     │  │   Mock Exam         │               │
│  │   No time limit     │  │   30 questions      │               │
│  │   Hints available   │  │   45 minutes        │               │
│  │                     │  │                     │               │
│  │   [Start Practice]  │  │   [Start Exam]      │               │
│  └─────────────────────┘  └─────────────────────┘               │
│                                                                  │
│  📊 Your Progress                                                │
│  ├── Questions practiced: 145                                   │
│  ├── Accuracy: 72%                                              │
│  └── Streak: 5 days 🔥                                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

Step 2: Topic Selection (Optional)
┌─────────────────────────────────────────────────────────────────┐
│  Choose topics to practice (or leave all selected)              │
├─────────────────────────────────────────────────────────────────┤
│  ☑ Right of Way          ☑ Speed Limits                        │
│  ☑ Road Signs            ☑ Parking Rules                       │
│  ☑ Traffic Lights        ☐ Emergency Vehicles                  │
│  ☑ Pedestrians           ☑ Alcohol & Drugs                     │
│                                                                  │
│  Questions: 10 ▼    Difficulty: Mixed ▼                         │
│                                                                  │
│  [Start Practice]                                               │
└─────────────────────────────────────────────────────────────────┘

Step 3: Question Display
┌─────────────────────────────────────────────────────────────────┐
│  Practice Mode          Question 3 of 10         [Exit Quiz]    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  What is the maximum speed limit in residential areas           │
│  in Germany unless otherwise marked?                            │
│                                                                  │
│  ○ A) 30 km/h                                                   │
│  ○ B) 50 km/h                                                   │
│  ○ C) 60 km/h                                                   │
│  ○ D) 70 km/h                                                   │
│                                                                  │
│  [💡 Hint]                            [Submit Answer]           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Step | User Action | System Response | API Call |
|------|-------------|-----------------|----------|
| 1 | Clicks "Start Practice" | Show topic selection | None (client-side) |
| 2 | Selects topics, clicks Start | Create quiz session | `POST /api/v1/quiz/start` |
| 3 | Views question | Display question with options | Included in session response |
| 4 | Clicks "Hint" | Show contextual hint | Client-side, from question data |
| 5 | Selects answer, submits | Validate, show result | `POST /api/v1/quiz/{id}/answer` |
| 6 | Views feedback | Show correct/incorrect + explanation trigger | Response includes `is_correct` |

### Question Display States

- **Unanswered:** All options selectable, Submit disabled
- **Selected:** One option highlighted, Submit enabled
- **Correct:** Green highlight, "✓ Correct!" message
- **Incorrect:** Red highlight on user's choice, green on correct, "✗ Incorrect" + [See Explanation] button

---

## Scenario 4: Taking a Timed Mock Exam

### User Goal
Simulate the real exam experience with time pressure.

### Step-by-Step Flow

```
Step 1: Exam Confirmation
┌─────────────────────────────────────────────────────────────────┐
│                    Mock Exam - Germany 🇩🇪                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  This simulates the real driving theory exam:                   │
│                                                                  │
│  • 30 questions                                                 │
│  • 45 minutes time limit                                        │
│  • Pass mark: 90% (27/30)                                       │
│  • No hints available                                           │
│  • Cannot pause or go back                                      │
│                                                                  │
│  ⚠️ Starting the exam will begin the timer immediately.         │
│                                                                  │
│  [Cancel]                              [Begin Exam]             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

Step 2: Exam in Progress
┌─────────────────────────────────────────────────────────────────┐
│  Mock Exam     Q 15/30     ⏱️ 32:45 remaining      [Finish]     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  You are approaching this intersection. What must you do?       │
│                                                                  │
│  ┌─────────────────────────────────┐                            │
│  │       [Image: Intersection]     │                            │
│  │                                 │                            │
│  └─────────────────────────────────┘                            │
│                                                                  │
│  ○ A) Stop and give way to traffic from the right              │
│  ○ B) Continue without stopping                                 │
│  ○ C) Flash your lights to warn other drivers                  │
│  ○ D) Sound your horn before proceeding                        │
│                                                                  │
│                                           [Next Question →]     │
└─────────────────────────────────────────────────────────────────┘

Step 3: Exam Results
┌─────────────────────────────────────────────────────────────────┐
│                     Exam Complete! 🎉                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│         ┌─────────────────────┐                                 │
│         │       PASSED        │                                 │
│         │       28/30         │                                 │
│         │       93%           │                                 │
│         └─────────────────────┘                                 │
│                                                                  │
│  Time used: 38:22 / 45:00                                       │
│                                                                  │
│  Topic Performance:                                              │
│  ├── Right of Way:     5/5  ████████████ 100%                  │
│  ├── Speed Limits:     4/5  █████████░░░  80%                  │
│  ├── Road Signs:       6/6  ████████████ 100%                  │
│  ├── Parking:          3/4  █████████░░░  75%                  │
│  └── Pedestrians:      4/4  ████████████ 100%                  │
│                                                                  │
│  [Review Mistakes]    [Return to Dashboard]    [Try Again]      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Step | User Action | System Response | API Call |
|------|-------------|-----------------|----------|
| 1 | Clicks "Start Exam" | Show confirmation modal | None |
| 2 | Confirms | Create exam session, start timer | `POST /api/v1/quiz/start` (mode: exam) |
| 3 | Answers questions | Record answer, advance | `POST /api/v1/quiz/{id}/answer` |
| 4 | Timer expires OR finishes | Calculate score, show results | `GET /api/v1/quiz/{id}/results` |
| 5 | Clicks "Review Mistakes" | Show incorrect questions with explanations | Navigate to review view |

### Timer Behavior

- **Warning at 5 min:** Timer turns orange
- **Warning at 1 min:** Timer turns red, subtle pulse animation
- **Time up:** Auto-submit remaining questions as unanswered

---

## Scenario 5: Getting an Explanation (RAG)

### User Goal
Understand why an answer was wrong with authoritative legal reference.

### Step-by-Step Flow

```
Step 1: Wrong Answer Feedback
┌─────────────────────────────────────────────────────────────────┐
│  Practice Mode          Question 3 of 10                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  What is the maximum speed limit in residential areas           │
│  in Germany unless otherwise marked?                            │
│                                                                  │
│  ○ A) 30 km/h                                                   │
│  ● B) 50 km/h  ← Correct answer                                │
│  ○ C) 60 km/h  ← Your answer ✗                                 │
│  ○ D) 70 km/h                                                   │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ ✗ Incorrect                                                 ││
│  │                                                             ││
│  │ [Why was I wrong? 🔍]                                       ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│                                           [Next Question →]     │
└─────────────────────────────────────────────────────────────────┘

Step 2: RAG Explanation Loading
┌─────────────────────────────────────────────────────────────────┐
│  Explanation                                              [×]   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                            │
│  Consulting traffic regulations...                              │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

Step 3: RAG Explanation Displayed
┌─────────────────────────────────────────────────────────────────┐
│  Explanation                                              [×]   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  📚 Why the correct answer is 50 km/h:                          │
│                                                                  │
│  According to §3(3) of the Straßenverkehrs-Ordnung (StVO),     │
│  the German Road Traffic Regulations:                           │
│                                                                  │
│  "Within built-up areas, the permissible maximum speed          │
│  for all motor vehicles is 50 km/h."                           │
│                                                                  │
│  This applies to all residential areas unless a different       │
│  limit is posted (e.g., 30 km/h zones near schools).           │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 📖 Source: StVO §3(3) — Speed within built-up areas        ││
│  │    Effective: 2024 revision                                 ││
│  │    [View full regulation →]                                 ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  💡 Common mistake: Many people confuse the 30 km/h zones       │
│     (which require explicit signage) with the general limit.   │
│                                                                  │
│  [Was this helpful?  👍  👎]          [🔖 Bookmark Question]   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Step | User Action | System Response | API Call |
|------|-------------|-----------------|----------|
| 1 | Clicks "Why was I wrong?" | Show loading state | `POST /api/v1/questions/{id}/explain` |
| 2 | Waits (~2-3 sec) | RAG pipeline executes | See [ARCHITECTURE.md#rag-pipeline](../ARCHITECTURE.md) |
| 3 | Views explanation | Display formatted explanation with citation | Response includes `explanation`, `sources[]` |
| 4 | Clicks "View full regulation" | Open source document in new tab | Link to external/cached legal doc |
| 5 | Rates helpfulness | Record feedback | `POST /api/v1/questions/{id}/explain/feedback` |

### RAG Response Structure

```json
{
  "explanation": "According to §3(3) of the StVO...",
  "sources": [
    {
      "law_code": "StVO",
      "section": "§3(3)",
      "title": "Speed within built-up areas",
      "effective_date": "2024-01-01",
      "excerpt": "Within built-up areas, the permissible maximum speed...",
      "url": "https://..."
    }
  ],
  "common_mistake": "Many people confuse the 30 km/h zones...",
  "cached": true,
  "cache_age_hours": 12
}
```

### Error States

- **RAG timeout:** "We couldn't generate an explanation right now. [Try again]"
- **No sources found:** Show generic explanation without citation (flag for review)
- **Rate limited:** "You've reached the explanation limit. Try again in X minutes."

---

## Scenario 6: Reviewing Progress Dashboard

### User Goal
Understand learning progress and identify areas needing more practice.

### Step-by-Step Flow

```
┌─────────────────────────────────────────────────────────────────┐
│  Progress Dashboard                              🇩🇪 Germany     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  📈 Exam Readiness Score                                        │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                                                             ││
│  │              ████████████████████░░░░░                      ││
│  │                      78%                                    ││
│  │                                                             ││
│  │     "Good progress! Focus on parking rules to improve."    ││
│  │                                                             ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  📊 Performance by Topic                                        │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ Right of Way      ████████████████████  95%  ✓ Strong      ││
│  │ Speed Limits      ████████████████░░░░  80%  ✓ Good        ││
│  │ Road Signs        █████████████████░░░  85%  ✓ Good        ││
│  │ Parking Rules     ████████░░░░░░░░░░░░  45%  ⚠ Needs Work  ││
│  │ Traffic Lights    ████████████████████  92%  ✓ Strong      ││
│  │ Pedestrians       ███████████████░░░░░  72%  → Improving   ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  🔥 Current Streak: 5 days                                      │
│                                                                  │
│  📅 Activity This Week                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  Mon   Tue   Wed   Thu   Fri   Sat   Sun                   ││
│  │   █     █     █     █     █     ░     ░                    ││
│  │  23    18    31    12    25     -     -                    ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  [Practice Weak Areas]        [Review Due Questions: 8]         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Section | Data Source | API Call |
|---------|-------------|----------|
| Readiness Score | Calculated from all metrics | `GET /api/v1/progress/readiness` |
| Topic Performance | Aggregated quiz results | `GET /api/v1/progress/topics` |
| Streak | Login/practice tracking | `GET /api/v1/progress` |
| Weekly Activity | Quiz sessions count | `GET /api/v1/progress` |
| Review Due | Spaced repetition scheduler | `GET /api/v1/progress/review-queue` |

### Readiness Score Factors

| Factor | Weight | Description |
|--------|--------|-------------|
| Topic Mastery | 40% | Weighted average across all topics |
| Recent Trend | 30% | Accuracy improvement over last 7 days |
| Coverage | 20% | % of question bank attempted |
| Consistency | 10% | Practice regularity |

---

## Scenario 7: Spaced Repetition Review Session

### User Goal
Review previously missed questions at optimal intervals for retention.

### Step-by-Step Flow

```
Step 1: Review Queue Notification
┌─────────────────────────────────────────────────────────────────┐
│  Dashboard                                                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 🔔 You have 8 questions due for review                      ││
│  │                                                             ││
│  │ Reviewing these questions now will help you remember them   ││
│  │ for your exam.                                              ││
│  │                                                             ││
│  │ [Start Review Session]                    [Remind Later]    ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

Step 2: Review Question with Confidence Rating
┌─────────────────────────────────────────────────────────────────┐
│  Review Session          Q 3/8                        [Exit]    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  🔄 You last saw this question 3 days ago (answered incorrectly)│
│                                                                  │
│  When can you overtake on the right in Germany?                 │
│                                                                  │
│  ○ A) Only on highways with multiple lanes                     │
│  ○ B) Never, it is always prohibited                           │
│  ○ C) In slow-moving traffic (under 60 km/h)                   │
│  ○ D) Only when the left lane is blocked                       │
│                                                                  │
│                                             [Show Answer]       │
└─────────────────────────────────────────────────────────────────┘

Step 3: Self-Assessment After Answer
┌─────────────────────────────────────────────────────────────────┐
│  Review Session          Q 3/8                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✓ Correct! The answer is C.                                   │
│                                                                  │
│  How well did you remember this?                                │
│                                                                  │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐            │
│  │ 😰      │  │ 😐      │  │ 🙂      │  │ 😊      │            │
│  │ Forgot  │  │ Hard    │  │ Good    │  │ Easy    │            │
│  │         │  │         │  │         │  │         │            │
│  │ Review  │  │ Review  │  │ Review  │  │ Review  │            │
│  │ in 1d   │  │ in 3d   │  │ in 7d   │  │ in 14d  │            │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Step | User Action | System Response | API Call |
|------|-------------|-----------------|----------|
| 1 | Clicks "Start Review Session" | Load due questions | `GET /api/v1/progress/review-queue` |
| 2 | Thinks, clicks "Show Answer" | Reveal correct answer | Client-side |
| 3 | Rates confidence | Update spaced repetition schedule | `POST /api/v1/progress/review` |
| 4 | Completes session | Show summary, update progress | `GET /api/v1/progress` |

### Spaced Repetition Intervals

| Self-Rating | Next Review | Easiness Factor Change |
|-------------|-------------|------------------------|
| Forgot (0-1) | 1 day | Decrease by 0.2 |
| Hard (2) | 3 days | No change |
| Good (3) | Current interval × EF | Increase by 0.1 |
| Easy (4-5) | Current interval × EF × 1.3 | Increase by 0.15 |

---

## Scenario 8: Bookmarking Questions

### User Goal
Save important or tricky questions for later review.

### Step-by-Step Flow

```
Step 1: Bookmark During Quiz
┌─────────────────────────────────────────────────────────────────┐
│  Practice Mode          Question 7 of 10                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Question content...]                                          │
│                                                                  │
│  [🔖 Bookmark]                            [Submit Answer]       │
└─────────────────────────────────────────────────────────────────┘

Step 2: Bookmark Confirmation
┌─────────────────────────────────────────────────────────────────┐
│  ✓ Question bookmarked                                   [×]    │
│    You can find it in your Bookmarks.                          │
└─────────────────────────────────────────────────────────────────┘

Step 3: View Bookmarks Page
┌─────────────────────────────────────────────────────────────────┐
│  My Bookmarks (12)                                    [Filter ▼]│
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 🔖 Right of Way at Intersections                            ││
│  │    "When approaching an uncontrolled intersection..."       ││
│  │    Added: 2 days ago    Topic: Right of Way                 ││
│  │    [Practice]  [Remove]                                     ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 🔖 Parking Distance from Crosswalks                         ││
│  │    "What is the minimum distance you must park from..."     ││
│  │    Added: 5 days ago    Topic: Parking                      ││
│  │    [Practice]  [Remove]                                     ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  [Practice All Bookmarked Questions]                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Step | User Action | System Response | API Call |
|------|-------------|-----------------|----------|
| 1 | Clicks "Bookmark" | Save bookmark, show confirmation | `POST /api/v1/questions/{id}/bookmark` |
| 2 | Views bookmarks page | List all bookmarked questions | `GET /api/v1/bookmarks` |
| 3 | Clicks "Practice" on one | Start quiz with that question | `POST /api/v1/quiz/start` (question_ids) |
| 4 | Clicks "Remove" | Delete bookmark | `DELETE /api/v1/bookmarks/{id}` |

---

## Scenario 9: Changing Jurisdiction/Language

### User Goal
Switch to a different country or language for practice.

### Step-by-Step Flow

```
Step 1: Open Settings
┌─────────────────────────────────────────────────────────────────┐
│  Settings                                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Learning Preferences                                            │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ Country:   🇩🇪 Germany                          [Change]     ││
│  │ Language:  Português                            [Change]     ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ⚠️ Changing your country will:                                 │
│  • Reset your progress for the new jurisdiction                 │
│  • Load different traffic laws and questions                    │
│  • Your progress in Germany will be saved                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

Step 2: Confirm Country Change
┌─────────────────────────────────────────────────────────────────┐
│  Change Country                                           [×]   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Switch from 🇩🇪 Germany to:                                    │
│                                                                  │
│  ○ 🇪🇸 Spain                                                    │
│  ● 🇵🇹 Portugal                                                 │
│                                                                  │
│  Your German progress will be saved and you can switch back    │
│  at any time.                                                   │
│                                                                  │
│  [Cancel]                              [Confirm Change]         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Step | User Action | System Response | API Call |
|------|-------------|-----------------|----------|
| 1 | Clicks "Change" on Country | Show country selection modal | `GET /api/v1/jurisdictions` |
| 2 | Selects new country | Show confirmation with implications | None |
| 3 | Confirms change | Update preferences, reload dashboard | `PATCH /api/v1/users/me/preferences` |
| 4 | Views dashboard | Show progress for new jurisdiction | `GET /api/v1/progress` (new jurisdiction) |

### Data Handling

- Progress is stored per jurisdiction
- Switching back restores previous progress
- Bookmarks are jurisdiction-specific

---

## Scenario 10: Reporting a Question Issue

### User Goal
Flag a problematic question (incorrect, unclear, outdated).

### Step-by-Step Flow

```
Step 1: Report Button
┌─────────────────────────────────────────────────────────────────┐
│  Practice Mode          Question 5 of 10                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Question with potential issue...]                             │
│                                                                  │
│  [⚠️ Report Issue]                                              │
└─────────────────────────────────────────────────────────────────┘

Step 2: Report Form
┌─────────────────────────────────────────────────────────────────┐
│  Report Question Issue                                    [×]   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  What's wrong with this question?                               │
│                                                                  │
│  ○ Incorrect answer marked as correct                          │
│  ○ Question is unclear or confusing                            │
│  ○ Information is outdated                                     │
│  ○ Translation error                                           │
│  ○ Other                                                        │
│                                                                  │
│  Additional details (optional):                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                                                             ││
│  │                                                             ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  [Cancel]                              [Submit Report]          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

Step 3: Confirmation
┌─────────────────────────────────────────────────────────────────┐
│  ✓ Report Submitted                                             │
│                                                                  │
│  Thank you for helping improve our question bank.               │
│  Our team will review this question.                            │
│                                                                  │
│  [Continue Quiz]                                                │
└─────────────────────────────────────────────────────────────────┘
```

| Step | User Action | System Response | API Call |
|------|-------------|-----------------|----------|
| 1 | Clicks "Report Issue" | Show report form modal | None |
| 2 | Selects issue type, adds details | Enable submit button | Client-side validation |
| 3 | Submits report | Create report, show confirmation | `POST /api/v1/questions/{id}/report` |

### Report Categories

| Category | Action Triggered |
|----------|------------------|
| Incorrect answer | High priority review queue |
| Unclear | Medium priority, may need rewrite |
| Outdated | Check against current law version |
| Translation | Language team review |
| Other | Manual triage |

---

## Error States & Edge Cases

### Network Errors

```
┌─────────────────────────────────────────────────────────────────┐
│  ⚠️ Connection Lost                                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  We couldn't reach our servers. Your progress has been          │
│  saved locally and will sync when you're back online.           │
│                                                                  │
│  [Retry]                               [Continue Offline]       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Session Expiry

```
┌─────────────────────────────────────────────────────────────────┐
│  Session Expired                                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Your session has expired for security reasons.                 │
│  Please log in again to continue.                               │
│                                                                  │
│  [Log In]                                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Quiz Interruption Recovery

```
┌─────────────────────────────────────────────────────────────────┐
│  Continue Previous Quiz?                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  You have an unfinished practice session from 2 hours ago.      │
│  Question 7 of 10 • 3 questions remaining                       │
│                                                                  │
│  [Resume Quiz]                         [Start New Quiz]         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Rate Limiting

```
┌─────────────────────────────────────────────────────────────────┐
│  ⏱️ Please Wait                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  You've requested many explanations recently.                   │
│  You can request another explanation in 5 minutes.              │
│                                                                  │
│  💡 Tip: Use the bookmark feature to save questions and         │
│     review explanations later.                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [ARCHITECTURE.md](../ARCHITECTURE.md) — Technical implementation details
- [PROJECT.md](../PROJECT.md) — Feature roadmap and scope
- [frontend/README.md](../frontend/README.md) — Component implementation guide
- [docs/api/](api/) — API endpoint specifications
