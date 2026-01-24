import { useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useMutation, useQuery } from "@tanstack/react-query";

import { Button } from "../../components/Button";
import { Card } from "../../components/Card";
import { ProgressBar } from "../../components/ProgressBar";
import { fetchJurisdictions } from "../../services/api/jurisdictionsApi";
import { updatePreferences } from "../../services/api/authApi";
import { useAuthStore } from "../../stores/authStore";
import { Jurisdiction } from "../../types/jurisdiction";

export const OnboardingPage = () => {
  const navigate = useNavigate();
  const accessToken = useAuthStore((state) => state.accessToken);
  const setAuth = useAuthStore((state) => state.setAuth);
  const authUser = useAuthStore((state) => state.user);
  const [selectedJurisdiction, setSelectedJurisdiction] = useState<string | null>(null);
  const [selectedLanguage, setSelectedLanguage] = useState<string | null>(null);

  const { data: jurisdictionsResponse, isLoading } = useQuery({
    queryKey: ["jurisdictions"],
    queryFn: fetchJurisdictions,
  });

  const jurisdictions: Jurisdiction[] = useMemo(() => {
    if (!jurisdictionsResponse || !jurisdictionsResponse.success) {
      return [];
    }
    return jurisdictionsResponse.data;
  }, [jurisdictionsResponse]);

  const selected = jurisdictions.find((item) => item.code === selectedJurisdiction);
  const flags: Record<string, string> = {
    DE: "🇩🇪",
    ES: "🇪🇸",
    PT: "🇵🇹",
  };

  const mutation = useMutation({
    mutationFn: async () => {
      if (!accessToken || !selectedJurisdiction || !selectedLanguage) {
        throw new Error("Missing onboarding data");
      }
      const response = await updatePreferences(accessToken, {
        preferred_jurisdiction: selectedJurisdiction,
        preferred_language: selectedLanguage,
      });
      return response;
    },
    onSuccess: (response) => {
      if (!response.success || !authUser || !accessToken) {
        return;
      }
      setAuth({
        accessToken,
        refreshToken: useAuthStore.getState().refreshToken ?? "",
        user: {
          ...authUser,
          preferred_jurisdiction: response.data.preferred_jurisdiction ?? null,
          preferred_language: response.data.preferred_language ?? null,
        },
      });
      navigate("/dashboard", { replace: true });
    },
  });

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="mx-auto flex max-w-4xl flex-col gap-8 px-6 py-16">
        <header className="flex flex-col gap-3">
          <div className="flex items-center justify-between text-sm font-semibold uppercase text-primary">
            <span>Step 1 of 2</span>
            <span>Setup</span>
          </div>
          <ProgressBar value={50} />
          <h1 className="text-3xl font-bold">Choose your jurisdiction</h1>
          <p className="text-sm text-slate-500">Pick the ruleset you want to study first.</p>
        </header>

        {isLoading && <p className="text-slate-500">Loading jurisdictions...</p>}

        <div className="grid gap-4 md:grid-cols-3">
          {jurisdictions.map((jurisdiction) => (
            <Card key={jurisdiction.code} className="cursor-pointer">
              <button
                type="button"
                onClick={() => setSelectedJurisdiction(jurisdiction.code)}
                className={`flex w-full flex-col gap-2 text-left ${
                  selectedJurisdiction === jurisdiction.code
                    ? "text-primary"
                    : "text-slate-800"
                }`}
              >
                <span className="text-2xl">{flags[jurisdiction.code] ?? "🌍"}</span>
                <h3 className="text-lg font-semibold">{jurisdiction.name}</h3>
                <p className="text-sm text-slate-500">Default: {jurisdiction.default_language}</p>
              </button>
            </Card>
          ))}
        </div>

        <section className="flex flex-col gap-4">
          <p className="text-sm font-semibold uppercase text-primary">Step 2 of 2</p>
          <h2 className="text-2xl font-bold">Choose your language</h2>
          {!selected && (
            <p className="text-sm text-slate-500">Select a jurisdiction to see available languages.</p>
          )}
          <div className="grid gap-3 md:grid-cols-2">
            {selected?.languages.map((language) => (
              <label
                key={language}
                className={`flex items-center gap-3 rounded-lg border px-4 py-3 text-sm ${
                  selectedLanguage === language
                    ? "border-primary bg-primary/10 text-primary"
                    : "border-slate-200 bg-white"
                }`}
              >
                <input
                  type="radio"
                  name="language"
                  className="h-4 w-4"
                  checked={selectedLanguage === language}
                  onChange={() => setSelectedLanguage(language)}
                />
                {language.toUpperCase()}
              </label>
            ))}
          </div>
        </section>

        <Button
          label={mutation.isPending ? "Saving..." : "Continue"}
          onClick={() => mutation.mutate()}
          disabled={!selectedJurisdiction || !selectedLanguage || mutation.isPending}
        />
      </div>
    </div>
  );
};
