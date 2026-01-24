export interface AuthUser {
  id: number;
  email: string;
  preferred_jurisdiction: string | null;
  preferred_language: string | null;
}

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
  expires_in: number;
  user: AuthUser;
}

export interface RegisterResponse {
  id: number;
  email: string;
  requires_verification: boolean;
}

export interface MeResponse {
  id: number;
  email: string;
  preferred_jurisdiction: string | null;
  preferred_language: string | null;
  created_at: string;
}

export interface PreferencesPayload {
  preferred_jurisdiction?: string;
  preferred_language?: string;
}
