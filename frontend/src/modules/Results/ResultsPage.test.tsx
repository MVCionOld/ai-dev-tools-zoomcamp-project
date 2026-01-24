import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { act, render, screen } from "@testing-library/react";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { ResultsPage } from "./ResultsPage";
import { useAuthStore } from "../../stores/authStore";
import { fetchResults } from "../../services/api/quizApi";

vi.mock("../../services/api/quizApi", () => ({
  fetchResults: vi.fn(),
}));

const renderResults = (quizId: string) => {
  const client = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
    },
  });
  return render(
    <QueryClientProvider client={client}>
      <MemoryRouter initialEntries={[`/results/${quizId}`]}>
        <Routes>
          <Route path="/results/:id" element={<ResultsPage />} />
        </Routes>
      </MemoryRouter>
    </QueryClientProvider>
  );
};

describe("ResultsPage", () => {
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
    });
  });

  afterEach(async () => {
    await act(async () => {
      useAuthStore.setState({
        isAuthenticated: false,
        accessToken: null,
        refreshToken: null,
        user: null,
      });
    });
    vi.clearAllMocks();
  });

  it("renders quiz results", async () => {
    vi.mocked(fetchResults).mockResolvedValue({
      success: true,
      data: {
        quiz_id: "quiz-123",
        score: 18,
        total: 20,
        percentage: 90,
        passed: true,
        pass_threshold: 70,
        duration_seconds: 842,
        by_topic: {
          road_signs: { correct: 8, total: 10 },
        },
        weak_areas: ["road_signs"],
        incorrect_questions: [1, 2],
      },
      meta: {},
    });

    await act(async () => {
      renderResults("quiz-123");
    });
    expect(await screen.findByText(/18\/20/i)).toBeInTheDocument();
    expect(screen.getByText(/passed/i)).toBeInTheDocument();
    expect(screen.getByText(/road_signs/i)).toBeInTheDocument();
  });
});
