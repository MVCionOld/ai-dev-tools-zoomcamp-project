import { screen } from "@testing-library/react";

import { renderWithProviders } from "../../test/test-utils";
import { LoginPage } from "./LoginPage";

const renderLogin = () => renderWithProviders(<LoginPage />);

describe("LoginPage", () => {
  it("renders login form fields", () => {
    renderLogin();
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /sign in/i })).toBeInTheDocument();
  });
});
