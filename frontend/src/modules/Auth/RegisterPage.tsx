import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useMutation } from "@tanstack/react-query";
import { AxiosError } from "axios";

import { Button } from "../../components/Button";
import { Card } from "../../components/Card";
import { Input } from "../../components/Input";
import { registerUser } from "../../services/api/authApi";
import { ApiErrorResponse } from "../../types/api";

export const RegisterPage = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirm, setPasswordConfirm] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [passwordError, setPasswordError] = useState<string | null>(null);
  const [isRegistered, setIsRegistered] = useState(false);

  const mutation = useMutation({
    mutationFn: () => registerUser(email, password, passwordConfirm),
    onSuccess: (response) => {
      if (!response.success) {
        setError(response.error.message);
        return;
      }
      setIsRegistered(true);
    },
    onError: (error) => {
      const axiosError = error as AxiosError<ApiErrorResponse>;
      const message = axiosError.response?.data?.error?.message;
      setError(message ?? "Unable to register. Please try again.");
    },
  });

  const validatePassword = () => {
    const hasMinLength = password.length >= 8;
    const hasUppercase = /[A-Z]/.test(password);
    const hasNumber = /\d/.test(password);
    if (!hasMinLength || !hasUppercase || !hasNumber) {
      setPasswordError("Password must be 8+ chars with 1 uppercase and 1 number.");
      return false;
    }
    setPasswordError(null);
    return true;
  };

  if (isRegistered) {
    return (
      <div className="min-h-screen bg-slate-50">
        <div className="mx-auto flex max-w-xl flex-col gap-6 px-6 py-16">
          <h1 className="text-3xl font-bold">Check your inbox</h1>
          <Card>
            <div className="flex flex-col gap-4">
              <p className="text-sm text-slate-600">
                We sent a verification link to <span className="font-semibold">{email}</span>.
              </p>
              <Button label="Go to login" onClick={() => navigate("/login", { replace: true })} />
            </div>
          </Card>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="mx-auto grid max-w-5xl gap-10 px-6 py-16 lg:grid-cols-[1.2fr_0.8fr]">
        <div className="flex flex-col justify-center gap-5">
          <span className="text-xs font-semibold uppercase tracking-[0.2em] text-primary">Get started</span>
          <h1 className="text-3xl font-bold">Create your account</h1>
          <p className="text-slate-600">
            Set up your personalized practice plan and stay ready for exam day.
          </p>
          <div className="rounded-2xl bg-white p-5 shadow-sm">
            <p className="text-sm text-slate-500">What you get</p>
            <ul className="mt-3 space-y-2 text-sm text-slate-600">
              <li>• Practice sessions tailored to your pace</li>
              <li>• Quick progress summaries</li>
              <li>• Multi-language support</li>
            </ul>
          </div>
        </div>
        <Card>
          <form
            className="flex flex-col gap-4"
            onSubmit={(event) => {
              event.preventDefault();
              setError(null);
              if (!validatePassword()) {
                return;
              }
              mutation.mutate();
            }}
          >
            <Input id="email" label="Email" type="email" value={email} onChange={setEmail} />
            <Input
              id="password"
              label="Password"
              type="password"
              value={password}
              onChange={setPassword}
              error={passwordError ?? undefined}
            />
            <Input
              id="passwordConfirm"
              label="Confirm password"
              type="password"
              value={passwordConfirm}
              onChange={setPasswordConfirm}
            />
            <p className="text-xs text-slate-500">Min 8 characters, 1 uppercase letter, 1 number.</p>
            {error && <p className="text-sm text-red-500">{error}</p>}
            <Button label={mutation.isPending ? "Creating account..." : "Create account"} type="submit" />
            <p className="text-sm text-slate-600">
              Already have an account? <Link className="text-primary" to="/login">Log in</Link>
            </p>
          </form>
        </Card>
      </div>
    </div>
  );
};
