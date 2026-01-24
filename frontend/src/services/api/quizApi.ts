import { httpClient } from "./httpClient";
import { ApiResponse } from "../../types/api";
import { QuizAnswerResponse, QuizResultsResponse, QuizStartResponse, QuizMode } from "../../types/quiz";

export const startQuiz = async (
  accessToken: string,
  payload: { jurisdiction: string; mode: QuizMode; question_count: number }
) => {
  const response = await httpClient.post<ApiResponse<QuizStartResponse>>(
    "/quiz/start",
    payload,
    {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    }
  );
  return response.data;
};

export const submitAnswer = async (
  accessToken: string,
  quizId: string,
  payload: { question_id: number; answer: string }
) => {
  const response = await httpClient.post<ApiResponse<QuizAnswerResponse>>(
    `/quiz/${quizId}/answer`,
    payload,
    {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    }
  );
  return response.data;
};

export const fetchResults = async (accessToken: string, quizId: string) => {
  const response = await httpClient.get<ApiResponse<QuizResultsResponse>>(`/quiz/${quizId}/results`, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  return response.data;
};
