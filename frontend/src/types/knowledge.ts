export interface ExplanationCitation {
  source_id: string;
  title: string;
  url: string | null;
  snippet: string;
}

export interface ExplanationResponse {
  explanation: string;
  source: string;
  citations: ExplanationCitation[];
}
