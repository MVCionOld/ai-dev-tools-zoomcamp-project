import { useMemo } from "react";
import { Link, useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";

import { Card } from "../../components/Card";
import { ProgressBar } from "../../components/ProgressBar";
import { fetchResults } from "../../services/api/quizApi";
import { useAuthStore } from "../../stores/authStore";

export const ResultsPage = () => {
  const { id } = useParams();
  const accessToken = useAuthStore((state) => state.accessToken);

  const { data, isLoading } = useQuery({
    queryKey: ["quiz-results", id],
    queryFn: () => {
      if (!accessToken || !id) {
        throw new Error("Missing quiz info");
      }
      return fetchResults(accessToken, id);
    },
    enabled: Boolean(accessToken && id),
  });

  const result = useMemo(() => (data && data.success ? data.data : null), [data]);
  const errorMessage = useMemo(() => (data && !data.success ? data.error.message : null), [data]);

  if (!id) {
    return (
      <div className="min-h-screen bg-slate-50">
        <div className="mx-auto flex max-w-3xl flex-col gap-6 px-6 py-16">
          <h1 className="text-3xl font-bold">Missing quiz results</h1>
          <Link to="/dashboard" className="text-primary">Return to dashboard</Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="mx-auto flex max-w-4xl flex-col gap-6 px-6 py-16">
        <header className="flex items-center justify-between">
          <h1 className="text-3xl font-bold">Results</h1>
          <Link to="/dashboard" className="text-primary">Back to dashboard</Link>
        </header>

        {isLoading && <p className="text-slate-500">Loading results...</p>}

        {errorMessage && <p className="text-sm font-semibold text-rose-600">{errorMessage}</p>}

        {result && (
          <>
            <Card>
              <div className="flex flex-col gap-3">
                <h2 className="text-2xl font-bold">
                  {result.score}/{result.total} - {result.percentage}%
                </h2>
                <p className={`text-sm font-semibold ${result.passed ? "text-emerald-600" : "text-rose-600"}`}>
                  {result.passed ? "PASSED" : "FAILED"}
                </p>
                <p className="text-sm text-slate-600">Pass threshold: {result.pass_threshold}%</p>
              </div>
            </Card>

            <Card>
              <h3 className="text-lg font-semibold">Topic breakdown</h3>
              <div className="mt-4 space-y-4">
                {Object.entries(result.by_topic).map(([topic, stats]) => {
                  const percentage = stats.total ? Math.round((stats.correct / stats.total) * 100) : 0;
                  return (
                    <div key={topic} className="space-y-2">
                      <div className="flex items-center justify-between text-sm">
                        <span className="font-medium text-slate-700">{topic}</span>
                        <span className="text-slate-500">{stats.correct}/{stats.total}</span>
                      </div>
                      <ProgressBar value={percentage} />
                    </div>
                  );
                })}
              </div>
            </Card>
          </>
        )}
      </div>
    </div>
  );
};
