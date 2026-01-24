import { BadgeProps } from "./Badge.types";

const variantClasses: Record<string, string> = {
  primary: "bg-primary/10 text-primary",
  secondary: "bg-slate-100 text-slate-700",
  success: "bg-emerald-100 text-emerald-700",
  warning: "bg-amber-100 text-amber-700",
};

export const Badge = ({ label, variant = "secondary" }: BadgeProps) => {
  return (
    <span className={`rounded-full px-3 py-1 text-xs font-semibold ${variantClasses[variant]}`}>{label}</span>
  );
};
