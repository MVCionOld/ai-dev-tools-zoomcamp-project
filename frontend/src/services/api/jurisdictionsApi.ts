import { httpClient } from "./httpClient";
import { ApiResponse } from "../../types/api";
import { Jurisdiction } from "../../types/jurisdiction";

export const fetchJurisdictions = async () => {
  const response = await httpClient.get<ApiResponse<Jurisdiction[]>>("/jurisdictions");
  return response.data;
};
