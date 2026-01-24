import { screen } from "@testing-library/react";

import { renderWithProviders } from "../../test/test-utils";
import { RegisterPage } from "./RegisterPage";

const renderRegister = () => renderWithProviders(<RegisterPage />);

describe("RegisterPage", () => {
  it("renders register form fields", () => {
    renderRegister();
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/^password$/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/confirm password/i)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /create account/i })).toBeInTheDocument();
  });
});
