import { httpClient } from "./httpClient";
import { ApiResponse } from "../../types/api";
import { LoginResponse, MeResponse, PreferencesPayload, RegisterResponse } from "../../types/auth";

export const registerUser = async (email: string, password: string, passwordConfirm: string) => {
  const response = await httpClient.post<ApiResponse<RegisterResponse>>("/auth/register", {
    email,
    password,
    password_confirm: passwordConfirm,
  });
  return response.data;
};

export const loginUser = async (email: string, password: string) => {
  const response = await httpClient.post<ApiResponse<LoginResponse>>("/auth/login", {
    email,
    password,
  });
  return response.data;
};

export const fetchMe = async (accessToken: string) => {
  const response = await httpClient.get<ApiResponse<MeResponse>>("/auth/me", {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  return response.data;
};

export const updatePreferences = async (accessToken: string, payload: PreferencesPayload) => {
  const response = await httpClient.patch<ApiResponse<PreferencesPayload>>("/users/preferences", payload, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  return response.data;
};
