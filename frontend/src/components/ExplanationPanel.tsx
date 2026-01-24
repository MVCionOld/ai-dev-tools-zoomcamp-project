import { ExplanationCitation } from "../types/knowledge";

interface ExplanationPanelProps {
  explanation: string;
  source: string;
  citations: ExplanationCitation[];
}

export const ExplanationPanel = ({ explanation, source, citations }: ExplanationPanelProps) => {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <p className="text-xs font-semibold uppercase tracking-wide text-slate-400">Explanation • {source}</p>
      <p className="mt-3 text-sm text-slate-700">{explanation}</p>
      <div className="mt-4 space-y-3">
        {citations.map((citation) => (
          <div key={citation.source_id} className="rounded-xl border border-slate-100 bg-slate-50 p-3">
            <p className="text-xs font-semibold text-slate-600">{citation.title}</p>
            <p className="mt-1 text-xs text-slate-500">{citation.snippet}</p>
            {citation.url && (
              <a
                href={citation.url}
                className="mt-2 inline-flex text-xs font-semibold text-primary"
                target="_blank"
                rel="noreferrer"
              >
                View source
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};
