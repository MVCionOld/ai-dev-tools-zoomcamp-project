import { ButtonProps } from "./Button.types";

const variantClasses: Record<string, string> = {
  primary: "bg-primary text-white hover:bg-primary-dark",
  secondary: "bg-white text-slate-900 border border-slate-200 hover:border-slate-300",
  ghost: "bg-transparent text-slate-600 hover:text-slate-900",
  danger: "bg-red-500 text-white hover:bg-red-600",
};

export const Button = ({ label, onClick, type = "button", disabled, variant = "primary" }: ButtonProps) => {
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`rounded-lg px-4 py-2 text-sm font-semibold transition ${variantClasses[variant]} ${
        disabled ? "opacity-50 cursor-not-allowed" : ""
      }`}
    >
      {label}
    </button>
  );
};
