import { render, screen } from "@testing-library/react";

import { ExplanationPanel } from "./ExplanationPanel";

describe("ExplanationPanel", () => {
  it("renders explanation and citations", () => {
    render(
      <ExplanationPanel
        explanation="Mock explanation"
        source="mock"
        citations={[
          {
            source_id: "DOC-1-0",
            title: "Mock Law",
            url: "https://example.com",
            snippet: "Always stop.",
          },
        ]}
      />
    );

    expect(screen.getByText(/mock explanation/i)).toBeInTheDocument();
    expect(screen.getByText(/mock law/i)).toBeInTheDocument();
    expect(screen.getByText(/always stop/i)).toBeInTheDocument();
  });
});
