import { Link } from "react-router-dom";

import { Button } from "../../components/Button";
import { Card } from "../../components/Card";

const countries = [
  { code: "DE", name: "Germany", flag: "🇩🇪" },
  { code: "ES", name: "Spain", flag: "🇪🇸" },
  { code: "PT", name: "Portugal", flag: "🇵🇹" },
];

const highlights = [
  {
    title: "Smarter prep",
    description: "Daily practice plans that fit your schedule.",
  },
  {
    title: "Clear explanations",
    description: "Learn the rule behind every answer.",
  },
  {
    title: "Study in your language",
    description: "Switch languages whenever you need.",
  },
];

export const LandingPage = () => {
  return (
    <div className="min-h-screen bg-slate-50">
      <div className="mx-auto flex max-w-6xl flex-col gap-14 px-6 py-16">
        <section className="rounded-3xl bg-gradient-to-br from-slate-900 via-slate-900 to-primary p-10 text-white shadow-lg">
          <div className="grid gap-10 lg:grid-cols-[1.1fr_0.9fr]">
            <div className="flex flex-col gap-5">
              <p className="text-xs font-semibold uppercase tracking-[0.2em] text-slate-200">DriveReady</p>
              <h1 className="text-4xl font-semibold leading-tight">
                Build exam confidence with a clean, structured study plan
              </h1>
              <p className="text-lg text-slate-200">
                Practice the right topics at the right time. Track momentum and stay ready.
              </p>
              <div className="flex flex-wrap gap-4">
                <Link to="/register">
                  <Button label="Create Free Account" />
                </Link>
                <Link to="/login">
                  <Button label="Try Sample Quiz" variant="secondary" />
                </Link>
              </div>
            </div>
            <div className="rounded-2xl bg-white/10 p-6 backdrop-blur">
              <p className="text-sm text-slate-200">Today&apos;s focus</p>
              <h3 className="text-2xl font-semibold">15-minute sprint</h3>
              <div className="mt-4 space-y-3 text-sm">
                <div className="flex items-center justify-between rounded-xl bg-white/10 px-4 py-2">
                  <span>Road signs</span>
                  <span className="text-slate-200">10 Qs</span>
                </div>
                <div className="flex items-center justify-between rounded-xl bg-white/10 px-4 py-2">
                  <span>Right of way</span>
                  <span className="text-slate-200">5 Qs</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="grid gap-6 md:grid-cols-3">
          {countries.map((country) => (
            <Card key={country.code}>
              <div className="flex flex-col gap-2">
                <span className="text-3xl">{country.flag}</span>
                <h3 className="text-lg font-semibold">{country.name}</h3>
                <p className="text-sm text-slate-600">Tailored question banks</p>
              </div>
            </Card>
          ))}
        </section>

        <section className="grid gap-6 md:grid-cols-3">
          {highlights.map((item) => (
            <Card key={item.title}>
              <div className="flex flex-col gap-3">
                <h3 className="text-lg font-semibold text-slate-900">{item.title}</h3>
                <p className="text-sm text-slate-600">{item.description}</p>
              </div>
            </Card>
          ))}
        </section>
      </div>
    </div>
  );
};
