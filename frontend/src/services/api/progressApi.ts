import { httpClient } from "./httpClient";
import { ApiResponse } from "../../types/api";
import { ProgressSummary } from "../../types/progress";

export const fetchProgressSummary = async (accessToken: string) => {
  const response = await httpClient.get<ApiResponse<ProgressSummary>>("/progress", {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  return response.data;
};
