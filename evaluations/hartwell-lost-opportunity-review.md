# Hartwell Lost Opportunity Review

This review scores the [worked analysis](../examples/hartwell-lost-opportunity-analysis.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Names, roles, and the stated email content match the evidence exactly |
| Evidence fidelity | 5 | "This cycle" and "later in the year" are preserved as Priya's own conditional wording, not flattened into a firm no |
| Fact separation | 5 | Alex's departure as a possible factor is clearly labelled inference, not fact |
| Missing information | 4 | Correctly flags the unknown about a new Head of Revenue Operations, though could also flag whether Priya's own role or authority has changed |
| Commercial usefulness | 5 | Gives Shaun a genuinely actionable read rather than a generic "circle back later" |
| Next step clarity | 4 | The next step is clear in spirit, but "a point later in the year" is deliberately vague, mirroring Priya's own vagueness rather than resolving it |
| Tone | 5 | Measured and honest, neither falsely optimistic nor unnecessarily bleak |
| Privacy | 5 | No information beyond what is relevant to the sales decision is included |
| Approval discipline | 5 | Nothing is presented as decided; the CRM and calendar suggestions are explicitly left for Shaun |
| Hallucination risk | 4 | Does not invent a firm reason or a specific return date, though the classification itself is necessarily a judgement call presented with appropriate hedging |

## What Worked

- The three blended factors in Priya's email were kept separate rather than collapsed into one tidy reason.
- Alex's departure was treated as a plausible but unconfirmed contributor, not as the confirmed cause.
- The pilot's measured result was correctly identified as durable evidence that survives the loss of the original champion.
- The classification, timing with a secondary stakeholder change, matched the actual wording used rather than defaulting to a harsher or softer read.
- No specific return date was invented where Priya only gave a vague one.

## What Needed Checking

- Whether Priya's own role or authority at Hartwell has changed is worth checking alongside the Head of Revenue Operations question.
- Shaun should decide for himself what "later in the year" should actually mean on his own calendar, since the analysis correctly declines to invent a date.
- Worth periodically checking whether the underlying pilot evidence would still resonate with a new stakeholder, or whether it needs updating.

## What I Changed in the Prompt

Nothing needed changing in the workflow for this run. The one thing worth testing further: a case where the stated reason is genuinely a single clear factor, to check the workflow does not manufacture ambiguity where none exists, the same way this run correctly avoided false simplicity.

## Next Test

Run a second lost opportunity scenario where the loss is a genuine disqualification, a real budget or compliance blocker with no plausible route back, and check that the workflow calls it clearly rather than manufacturing hope that is not supported by the evidence.
