import { InputProps } from "./Input.types";

export const Input = ({ id, label, type = "text", placeholder, value, onChange, error }: InputProps) => {
  return (
    <div className="flex flex-col gap-2">
      <label htmlFor={id} className="text-sm font-medium text-slate-700">
        {label}
      </label>
      <input
        id={id}
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={(event) => onChange(event.target.value)}
        className={`rounded-lg border px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary ${
          error ? "border-red-400" : "border-slate-200"
        }`}
      />
      {error && <span className="text-xs text-red-500">{error}</span>}
    </div>
  );
};
