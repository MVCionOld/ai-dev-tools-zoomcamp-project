import { act, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it } from "vitest";

import { renderWithProviders } from "../../test/test-utils";
import { useAuthStore } from "../../stores/authStore";
import { useQuizStore } from "../../stores/quizStore";
import { QuizPage } from "./QuizPage";

const sampleQuestion = {
  id: 12,
  index: 1,
  type: "multiple_choice",
  content: {
    text: "What does this sign mean?",
    options: [
      { key: "A", text: "Stop and give way" },
      { key: "B", text: "Slow down" },
    ],
  },
  topic: "road_signs",
  difficulty: "beginner",
};

describe("QuizPage", () => {
  beforeEach(async () => {
    await act(async () => {
      useAuthStore.setState({
        isAuthenticated: true,
        accessToken: "token",
        refreshToken: "refresh",
        user: {
          id: 1,
          email: "test@example.com",
          preferred_jurisdiction: "DE",
          preferred_language: "en",
        },
      });
      useQuizStore.getState().setSession({
        quizId: "quiz-123",
        mode: "practice",
        totalQuestions: 20,
        timeLimitSeconds: null,
        currentQuestion: sampleQuestion,
      });
    });
  });

  afterEach(async () => {
    await act(async () => {
      useQuizStore.getState().clearQuiz();
      useAuthStore.setState({
        isAuthenticated: false,
        accessToken: null,
        refreshToken: null,
        user: null,
      });
    });
  });

  it("renders the current question", () => {
    renderWithProviders(<QuizPage />);
    expect(screen.getByText(/question 1 of 20/i)).toBeInTheDocument();
    expect(screen.getByText(/what does this sign mean/i)).toBeInTheDocument();
    expect(screen.getByText("Stop and give way")).toBeInTheDocument();
    expect(screen.getByText("Slow down")).toBeInTheDocument();
  });
});
