import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useMutation } from "@tanstack/react-query";
import { AxiosError } from "axios";

import { Button } from "../../components/Button";
import { Card } from "../../components/Card";
import { Input } from "../../components/Input";
import { loginUser } from "../../services/api/authApi";
import { ApiErrorResponse } from "../../types/api";
import { useAuthStore } from "../../stores/authStore";

export const LoginPage = () => {
  const navigate = useNavigate();
  const setAuth = useAuthStore((state) => state.setAuth);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  const mutation = useMutation({
    mutationFn: () => loginUser(email, password),
    onSuccess: (response) => {
      if (!response.success) {
        setError(response.error.message);
        return;
      }
      setAuth({
        accessToken: response.data.access_token,
        refreshToken: response.data.refresh_token,
        user: response.data.user,
      });
      navigate("/onboarding", { replace: true });
    },
    onError: (error) => {
      const axiosError = error as AxiosError<ApiErrorResponse>;
      const message = axiosError.response?.data?.error?.message;
      setError(message ?? "Unable to log in. Please try again.");
    },
  });

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="mx-auto grid max-w-5xl gap-10 px-6 py-16 lg:grid-cols-[1.2fr_0.8fr]">
        <div className="flex flex-col justify-center gap-5">
          <span className="text-xs font-semibold uppercase tracking-[0.2em] text-primary">DriveReady</span>
          <h1 className="text-3xl font-bold">Welcome back</h1>
          <p className="text-slate-600">Your next practice session is queued up and ready.</p>
          <div className="rounded-2xl bg-white p-5 shadow-sm">
            <p className="text-sm text-slate-500">Recent activity</p>
            <p className="mt-2 text-lg font-semibold">Road signs refresher</p>
            <p className="text-xs text-slate-400">7 questions • 4 minutes</p>
          </div>
        </div>
        <Card>
          <form
            className="flex flex-col gap-4"
            onSubmit={(event) => {
              event.preventDefault();
              setError(null);
              mutation.mutate();
            }}
          >
            <Input id="email" label="Email" type="email" value={email} onChange={setEmail} />
            <Input id="password" label="Password" type="password" value={password} onChange={setPassword} />
            <div className="flex items-center justify-between text-sm">
              <span className="text-slate-500">Forgot password?</span>
              <Link className="text-primary" to="/register">
                Reset it
              </Link>
            </div>
            {error && <p className="text-sm text-red-500">{error}</p>}
            <Button label={mutation.isPending ? "Signing in..." : "Sign In"} type="submit" />
            <p className="text-sm text-slate-600">
              Don&apos;t have an account? <Link className="text-primary" to="/register">Create one</Link>
            </p>
          </form>
        </Card>
      </div>
    </div>
  );
};
