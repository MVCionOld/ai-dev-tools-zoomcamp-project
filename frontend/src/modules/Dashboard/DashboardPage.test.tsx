import { screen } from "@testing-library/react";

import { renderWithProviders } from "../../test/test-utils";
import { DashboardPage } from "./DashboardPage";

describe("DashboardPage", () => {
  it("renders quiz mode cards", () => {
    renderWithProviders(<DashboardPage />);
    expect(screen.getByText(/practice mode/i)).toBeInTheDocument();
    expect(screen.getByText(/mock exam/i)).toBeInTheDocument();
  });
});
