export type QuizMode = "practice" | "exam";

export interface QuizQuestionOption {
  key: string;
  text: string;
}

export interface QuizQuestionContent {
  text: string;
  image_url?: string;
  options: QuizQuestionOption[];
}

export interface QuizQuestion {
  id: number;
  index: number;
  type: string;
  content: QuizQuestionContent;
  topic: string;
  difficulty: string;
}

export interface QuizStartResponse {
  quiz_id: string;
  mode: QuizMode;
  total_questions: number;
  time_limit_seconds: number | null;
  current_question: QuizQuestion;
}

export interface QuizAnswerResponse {
  is_correct: boolean;
  correct_answer: string;
  has_next: boolean;
  next_question: QuizQuestion | null;
}

export interface QuizResultsResponse {
  quiz_id: string;
  score: number;
  total: number;
  percentage: number;
  passed: boolean;
  pass_threshold: number;
  duration_seconds: number | null;
  by_topic: Record<string, { correct: number; total: number }>;
  weak_areas: string[];
  incorrect_questions: number[];
}
