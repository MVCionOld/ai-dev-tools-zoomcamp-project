import { httpClient } from "./httpClient";
import { ApiResponse } from "../../types/api";
import { ExplanationResponse } from "../../types/knowledge";

export const fetchExplanation = async (
  accessToken: string,
  payload: { question_id: number; jurisdiction: string }
) => {
  const response = await httpClient.post<ApiResponse<ExplanationResponse>>(
    "/knowledge/explain",
    payload,
    {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    }
  );
  return response.data;
};
