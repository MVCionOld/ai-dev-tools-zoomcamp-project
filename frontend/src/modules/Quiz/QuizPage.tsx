import { useMemo, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { useMutation } from "@tanstack/react-query";

import { Button } from "../../components/Button";
import { Card } from "../../components/Card";
import { submitAnswer } from "../../services/api/quizApi";
import { useAuthStore } from "../../stores/authStore";
import { useQuizStore } from "../../stores/quizStore";

export const QuizPage = () => {
  const navigate = useNavigate();
  const { id } = useParams();
  const accessToken = useAuthStore((state) => state.accessToken);
  const { quizId, currentQuestion, totalQuestions, mode, setCurrentQuestion, clearQuiz } = useQuizStore();
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<{ isCorrect: boolean; correctAnswer: string } | null>(null);
  const [error, setError] = useState<string | null>(null);

  const activeQuizId = id ?? quizId;

  const question = currentQuestion;

  const mutation = useMutation({
    mutationFn: async () => {
      if (!accessToken || !activeQuizId || !question || !selectedAnswer) {
        throw new Error("Missing quiz data");
      }
      return submitAnswer(accessToken, activeQuizId, {
        question_id: question.id,
        answer: selectedAnswer,
      });
    },
    onSuccess: (response) => {
      if (!response.success || !question) {
        setError(response.success ? null : response.error.message);
        return;
      }
      setError(null);
      setFeedback({
        isCorrect: response.data.is_correct,
        correctAnswer: response.data.correct_answer,
      });

      if (response.data.has_next && response.data.next_question) {
        setTimeout(() => {
          setFeedback(null);
          setSelectedAnswer(null);
          setCurrentQuestion(response.data.next_question);
        }, 500);
      } else {
        clearQuiz();
        navigate(`/results/${activeQuizId}`);
      }
    },
    onError: () => {
      setError("Unable to submit answer. Please try again.");
    },
  });

  const options = useMemo(() => question?.content.options ?? [], [question]);

  if (!question || !activeQuizId) {
    return (
      <div className="min-h-screen bg-slate-50">
        <div className="mx-auto flex max-w-3xl flex-col gap-6 px-6 py-16">
          <h1 className="text-3xl font-bold">No active quiz</h1>
          <p className="text-slate-600">Start a quiz from the dashboard to continue.</p>
          <Link to="/dashboard" className="text-primary">Return to dashboard</Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="mx-auto flex max-w-4xl flex-col gap-6 px-6 py-16">
        <header className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <p className="text-sm font-semibold text-primary">{mode === "exam" ? "Mock Exam" : "Practice Mode"}</p>
            <h1 className="text-2xl font-bold">
              Question {question.index} of {totalQuestions}
            </h1>
          </div>
          <Button
            label="Exit Quiz"
            variant="secondary"
            onClick={() => {
              clearQuiz();
              navigate("/dashboard");
            }}
          />
        </header>

        <Card>
          <div className="flex flex-col gap-5">
            <p className="text-lg font-semibold text-slate-900">{question.content.text}</p>
            {question.content.image_url && (
              <div className="rounded-xl border border-slate-200 bg-white p-4">
                <img src={question.content.image_url} alt="question visual" className="mx-auto max-h-56" />
              </div>
            )}

            <div className="grid gap-3">
              {options.map((option) => {
                const isSelected = selectedAnswer === option.key;
                return (
                  <button
                    key={option.key}
                    type="button"
                    onClick={() => setSelectedAnswer(option.key)}
                    className={`flex items-center justify-between rounded-xl border px-4 py-3 text-left text-sm transition ${
                      isSelected ? "border-primary bg-primary/10 text-primary" : "border-slate-200 bg-white"
                    }`}
                  >
                    <span className="font-semibold">{option.key}</span>
                    <span className="text-slate-700">{option.text}</span>
                  </button>
                );
              })}
            </div>

            {feedback && (
              <p className={`text-sm font-semibold ${feedback.isCorrect ? "text-emerald-600" : "text-rose-600"}`}>
                {feedback.isCorrect ? "Correct!" : `Incorrect. Correct answer: ${feedback.correctAnswer}`}
              </p>
            )}

            {error && <p className="text-sm font-semibold text-rose-600">{error}</p>}

            <Button
              label={mutation.isPending ? "Submitting..." : "Submit Answer"}
              onClick={() => mutation.mutate()}
              disabled={!selectedAnswer || mutation.isPending}
            />
          </div>
        </Card>
      </div>
    </div>
  );
};
