import { CardProps } from "./Card.types";

export const Card = ({ children, className }: CardProps) => {
  return <div className={`rounded-2xl bg-white p-6 shadow-sm ${className ?? ""}`}>{children}</div>;
};
