export interface ProgressSummary {
  total_questions_attempted: number;
  total_correct: number;
  accuracy_percentage: number;
  current_streak: number;
  longest_streak: number;
  readiness_score: number;
  last_activity: string | null;
}
