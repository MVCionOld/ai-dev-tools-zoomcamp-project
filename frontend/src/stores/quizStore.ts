import { create } from "zustand";
import { QuizMode, QuizQuestion } from "../types/quiz";

interface QuizState {
  quizId: string | null;
  mode: QuizMode | null;
  totalQuestions: number;
  timeLimitSeconds: number | null;
  currentQuestion: QuizQuestion | null;
  setSession: (payload: {
    quizId: string;
    mode: QuizMode;
    totalQuestions: number;
    timeLimitSeconds: number | null;
    currentQuestion: QuizQuestion;
  }) => void;
  setCurrentQuestion: (question: QuizQuestion | null) => void;
  clearQuiz: () => void;
}

export const useQuizStore = create<QuizState>((set) => ({
  quizId: null,
  mode: null,
  totalQuestions: 0,
  timeLimitSeconds: null,
  currentQuestion: null,
  setSession: (payload) =>
    set({
      quizId: payload.quizId,
      mode: payload.mode,
      totalQuestions: payload.totalQuestions,
      timeLimitSeconds: payload.timeLimitSeconds,
      currentQuestion: payload.currentQuestion,
    }),
  setCurrentQuestion: (question) => set({ currentQuestion: question }),
  clearQuiz: () =>
    set({
      quizId: null,
      mode: null,
      totalQuestions: 0,
      timeLimitSeconds: null,
      currentQuestion: null,
    }),
}));
