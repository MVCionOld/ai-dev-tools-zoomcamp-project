export type BadgeVariant = "primary" | "secondary" | "success" | "warning";

export interface BadgeProps {
  label: string;
  variant?: BadgeVariant;
}
