import { ProgressBarProps } from "./ProgressBar.types";

export const ProgressBar = ({ value }: ProgressBarProps) => {
  return (
    <div className="h-2 w-full rounded-full bg-slate-100">
      <div className="h-2 rounded-full bg-primary" style={{ width: `${value}%` }} />
    </div>
  );
};
