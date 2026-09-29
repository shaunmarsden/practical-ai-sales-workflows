# Hartwell Lost Opportunity Review

This page scores the [worked analysis](../examples/hartwell-lost-opportunity-analysis.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Names, roles and what the email says match the evidence exactly |
| Evidence fidelity | 5 | Keeps "This cycle" and "later in the year" as Priya's own conditional wording, not flattened into a firm no |
| Fact separation | 5 | Clearly labels Alex's departure as a possible factor, an inference, not a fact |
| Missing information | 4 | Rightly flags the unknown about a new Head of Revenue Operations, though it could also ask whether Priya's own role or authority has changed |
| Commercial usefulness | 5 | Gives me a read I can act on rather than a general "circle back later" |
| Next step clarity | 4 | The next step is clear in spirit, but "a point later in the year" is vague on purpose, matching Priya's vagueness rather than resolving it |
| Tone | 5 | Measured and honest, neither falsely hopeful nor needlessly bleak |
| Privacy | 5 | Includes nothing beyond what matters to the sales decision |
| Approval discipline | 5 | Presents nothing as decided, and leaves the CRM and calendar suggestions for me |
| Hallucination risk | 4 | Doesn't invent a firm reason or a return date, though the classification is still a judgement call, hedged about right |

## What Worked

It kept the three mixed-together factors in Priya's email apart, rather than boiling them down to one tidy reason.

It treated Alex's departure as a likely but unconfirmed factor, not the confirmed cause.

It saw the pilot's measured result as lasting evidence that survives losing the original champion.

Its classification, timing with a secondary change of stakeholder, matched the wording used rather than defaulting to a harsher or softer read.

It didn't invent a return date where Priya only gave a vague one.

## What Needed Checking

It's worth checking whether Priya's own role or authority at Hartwell has changed, alongside the Head of Revenue Operations question.

I should decide for myself what "later in the year" means on my own calendar, since the analysis rightly declines to invent a date.

It's worth checking now and then whether the pilot evidence would still land with a new stakeholder, or whether it needs updating.

## What I Changed in the Prompt

Nothing in the workflow needed changing for this run. One thing is worth testing further: a case where the stated reason really is one clear factor. That checks the workflow doesn't invent doubt where there is none, just as this run avoided making things falsely simple.

## Next Test

Run a second lost opportunity scenario where the loss is a real disqualification, a budget or compliance blocker with no likely way back. Check that the workflow says so clearly rather than offering hope the evidence doesn't support.
