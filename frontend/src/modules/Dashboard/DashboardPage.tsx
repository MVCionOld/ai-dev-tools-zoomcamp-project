import { useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useMutation, useQuery } from "@tanstack/react-query";
import { AxiosError } from "axios";

import { Badge } from "../../components/Badge";
import { Button } from "../../components/Button";
import { Card } from "../../components/Card";
import { fetchProgressSummary } from "../../services/api/progressApi";
import { startQuiz } from "../../services/api/quizApi";
import { useAuthStore } from "../../stores/authStore";
import { useQuizStore } from "../../stores/quizStore";
import { ApiErrorResponse } from "../../types/api";
import { QuizMode } from "../../types/quiz";

export const DashboardPage = () => {
  const navigate = useNavigate();
  const user = useAuthStore((state) => state.user);
  const accessToken = useAuthStore((state) => state.accessToken);
  const setSession = useQuizStore((state) => state.setSession);
  const [error, setError] = useState<string | null>(null);
  const preferredJurisdiction = user?.preferred_jurisdiction ?? null;
  const canStartQuiz = Boolean(accessToken && preferredJurisdiction);

  const { data: progressResponse, isLoading: isProgressLoading } = useQuery({
    queryKey: ["progress-summary"],
    queryFn: () => {
      if (!accessToken) {
        throw new Error("Missing access token");
      }
      return fetchProgressSummary(accessToken);
    },
    enabled: Boolean(accessToken),
  });

  const progress = useMemo(
    () => (progressResponse && progressResponse.success ? progressResponse.data : null),
    [progressResponse]
  );
  const progressError = useMemo(
    () => (progressResponse && !progressResponse.success ? progressResponse.error.message : null),
    [progressResponse]
  );
  const stats = {
    practiced: progress?.total_questions_attempted ?? 0,
    accuracy: progress?.accuracy_percentage ?? 0,
    streak: progress?.current_streak ?? 0,
  };

  const quizMutation = useMutation({
    mutationFn: async (mode: QuizMode) => {
      if (!accessToken || !preferredJurisdiction) {
        throw new Error("Select a jurisdiction to start a quiz.");
      }
      return startQuiz(accessToken, {
        jurisdiction: preferredJurisdiction,
        mode,
        question_count: 20,
      });
    },
    onSuccess: (response) => {
      if (!response.success) {
        setError(response.error.message);
        return;
      }
      setError(null);
      setSession({
        quizId: response.data.quiz_id,
        mode: response.data.mode,
        totalQuestions: response.data.total_questions,
        timeLimitSeconds: response.data.time_limit_seconds,
        currentQuestion: response.data.current_question,
      });
      navigate(`/quiz/${response.data.quiz_id}`);
    },
    onError: (error) => {
      const axiosError = error as AxiosError<ApiErrorResponse>;
      const message = axiosError.response?.data?.error?.message;
      setError(message ?? (error instanceof Error ? error.message : "Unable to start quiz."));
    },
  });

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="mx-auto flex max-w-5xl flex-col gap-8 px-6 py-16">
        <header className="flex flex-col gap-3">
          <p className="text-sm font-semibold text-primary">Dashboard</p>
          <div className="flex flex-wrap items-center justify-between gap-3">
            <h1 className="text-3xl font-bold">Welcome back{user?.email ? `, ${user.email}` : ""}</h1>
            <div className="flex items-center gap-2">
              <Badge label={user?.preferred_jurisdiction ?? "No jurisdiction"} variant="primary" />
              <button type="button" className="text-sm font-semibold text-primary" onClick={() => navigate("/onboarding")}>
                Update
              </button>
            </div>
          </div>
          <p className="text-sm text-slate-500">Your next session is ready when you are.</p>
        </header>

        <div className="grid gap-6 md:grid-cols-2">
          <Card>
            <h3 className="text-lg font-semibold">Practice Mode</h3>
            <p className="text-sm text-slate-600">No time limit. Focus on learning.</p>
            <div className="mt-4">
              <Button
                label={quizMutation.isPending ? "Starting..." : "Start Practice"}
                onClick={() => {
                  setError(null);
                  quizMutation.mutate("practice");
                }}
                disabled={!canStartQuiz || quizMutation.isPending}
              />
            </div>
          </Card>
          <Card>
            <h3 className="text-lg font-semibold">Mock Exam</h3>
            <p className="text-sm text-slate-600">Timed quiz to simulate the exam.</p>
            <div className="mt-4">
              <Button
                label={quizMutation.isPending ? "Starting..." : "Start Exam"}
                onClick={() => {
                  setError(null);
                  quizMutation.mutate("exam");
                }}
                disabled={!canStartQuiz || quizMutation.isPending}
              />
            </div>
          </Card>
        </div>

        {!preferredJurisdiction && (
          <p className="text-sm font-semibold text-amber-600">
            Set your preferred jurisdiction to start a quiz.
          </p>
        )}

        {error && <p className="text-sm font-semibold text-rose-600">{error}</p>}

        <Card>
          <div className="flex items-center justify-between">
            <h3 className="text-lg font-semibold">Progress overview</h3>
            <Badge label={user?.preferred_language?.toUpperCase() ?? "LANG"} variant="secondary" />
          </div>
          {isProgressLoading && <p className="mt-2 text-sm text-slate-500">Loading progress...</p>}
          {progressError && <p className="mt-2 text-sm font-semibold text-rose-600">{progressError}</p>}
          <div className="mt-4 grid gap-4 md:grid-cols-3">
            <div>
              <p className="text-sm text-slate-500">Questions practiced</p>
              <p className="text-2xl font-bold">{stats.practiced}</p>
            </div>
            <div>
              <p className="text-sm text-slate-500">Accuracy</p>
              <p className="text-2xl font-bold">{stats.accuracy}%</p>
            </div>
            <div>
              <p className="text-sm text-slate-500">Current streak</p>
              <p className="text-2xl font-bold">{stats.streak} 🔥</p>
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
};
