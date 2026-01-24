# API Contract

Base URL: `/api/v1`

All responses follow format:
```json
{ "success": true, "data": {...}, "meta": {"timestamp": "...", "request_id": "..."} }
{ "success": false, "error": {"code": "...", "message": "...", "details": {...}} }
```

---

## Authentication

### POST /auth/register

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "password_confirm": "SecurePass123!"
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "email": "user@example.com",
    "requires_verification": true
  }
}
```

### POST /auth/login

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJ...",
    "refresh_token": "eyJ...",
    "expires_in": 900,
    "user": {
      "id": 1,
      "email": "user@example.com",
      "preferred_jurisdiction": "DE",
      "preferred_language": "en"
    }
  }
}
```

### POST /auth/refresh

**Request:**
```json
{ "refresh_token": "eyJ..." }
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJ...",
    "expires_in": 900
  }
}
```

### POST /auth/logout

**Request:**
```json
{ "refresh_token": "eyJ..." }
```

**Response (200):**
```json
{ "success": true, "data": null }
```

### GET /auth/me

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "email": "user@example.com",
    "preferred_jurisdiction": "DE",
    "preferred_language": "en",
    "created_at": "2026-01-24T10:00:00Z"
  }
}
```

### PATCH /users/preferences

**Request:**
```json
{
  "preferred_jurisdiction": "DE",
  "preferred_language": "en"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "preferred_jurisdiction": "DE",
    "preferred_language": "en"
  }
}
```

---

## Jurisdictions

### GET /jurisdictions

**Response (200):**
```json
{
  "success": true,
  "data": [
    {
      "code": "DE",
      "name": "Germany",
      "languages": ["de", "en", "tr", "pt"],
      "default_language": "de"
    },
    {
      "code": "ES",
      "name": "Spain",
      "languages": ["es", "en", "ca"],
      "default_language": "es"
    },
    {
      "code": "PT",
      "name": "Portugal",
      "languages": ["pt", "en"],
      "default_language": "pt"
    }
  ]
}
```

---

## Quiz

### POST /quiz/start

**Request:**
```json
{
  "jurisdiction": "DE",
  "mode": "practice",
  "question_count": 20
}
```

**mode:** `"practice"` | `"exam"`  
**question_count:** 10-30 (default 20)

**Response (201):**
```json
{
  "success": true,
  "data": {
    "quiz_id": "uuid-here",
    "mode": "practice",
    "total_questions": 20,
    "time_limit_seconds": null,
    "current_question": {
      "id": 123,
      "index": 1,
      "type": "multiple_choice",
      "content": {
        "text": "What does this sign mean?",
        "image_url": "/media/signs/de_stop.png",
        "options": [
          {"key": "A", "text": "Stop and give way"},
          {"key": "B", "text": "Slow down"},
          {"key": "C", "text": "No entry"},
          {"key": "D", "text": "End of restrictions"}
        ]
      },
      "topic": "road_signs",
      "difficulty": "beginner"
    }
  }
}
```

### POST /quiz/{quiz_id}/answer

**Request:**
```json
{
  "question_id": 123,
  "answer": "A"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "is_correct": true,
    "correct_answer": "A",
    "has_next": true,
    "next_question": {
      "id": 124,
      "index": 2,
      ...
    }
  }
}
```

### GET /quiz/{quiz_id}/results

**Response (200):**
```json
{
  "success": true,
  "data": {
    "quiz_id": "uuid",
    "score": 18,
    "total": 20,
    "percentage": 90,
    "passed": true,
    "pass_threshold": 70,
    "duration_seconds": 842,
    "by_topic": {
      "road_signs": {"correct": 8, "total": 10},
      "right_of_way": {"correct": 5, "total": 5},
      "speed_limits": {"correct": 5, "total": 5}
    },
    "weak_areas": ["road_signs"],
    "incorrect_questions": [123, 127]
  }
}
```

---

## Questions

### POST /questions/{id}/explain

**Request:**
```json
{
  "jurisdiction": "DE"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "question_id": 123,
    "explanation": "The octagonal red sign with 'STOP' requires you to come to a complete stop...",
    "citations": [
      {
        "law_code": "StVO",
        "section": "§41",
        "text": "Wer ein Fahrzeug führt, muss...",
        "source_id": "DE-StVO-§41-2024"
      }
    ],
    "cached": false
  }
}
```

### POST /questions/{id}/bookmark

**Response (201):**
```json
{
  "success": true,
  "data": {
    "bookmark_id": 456,
    "question_id": 123
  }
}
```

---

## Progress

### GET /progress

**Response (200):**
```json
{
  "success": true,
  "data": {
    "total_questions_attempted": 150,
    "total_correct": 120,
    "accuracy_percentage": 80,
    "current_streak": 5,
    "longest_streak": 12,
    "readiness_score": 72,
    "last_activity": "2026-01-24T10:00:00Z"
  }
}
```

### GET /progress/weak-areas

**Response (200):**
```json
{
  "success": true,
  "data": {
    "weak_areas": [
      {
        "topic": "right_of_way",
        "accuracy": 45,
        "questions_attempted": 20,
        "recommendation": "Focus on intersection priority rules"
      },
      {
        "topic": "parking",
        "accuracy": 55,
        "questions_attempted": 15,
        "recommendation": "Review parking distance requirements"
      }
    ]
  }
}
```

### GET /progress/review-queue

**Response (200):**
```json
{
  "success": true,
  "data": {
    "due_count": 12,
    "questions": [
      {
        "id": 123,
        "due_date": "2026-01-24",
        "interval_days": 3,
        "topic": "road_signs"
      }
    ]
  }
}
```

---

## Error Codes

| Code | HTTP | Meaning |
|------|------|---------|
| `VALIDATION_ERROR` | 400 | Invalid input |
| `AUTHENTICATION_REQUIRED` | 401 | Missing/invalid token |
| `PERMISSION_DENIED` | 403 | Not allowed |
| `NOT_FOUND` | 404 | Resource missing |
| `QUIZ_COMPLETED` | 400 | Quiz already finished |
| `RATE_LIMITED` | 429 | Too many requests |
| `EXPLANATION_LIMIT` | 429 | 20/hour explanation limit hit |
| `INTERNAL_ERROR` | 500 | Server error |
