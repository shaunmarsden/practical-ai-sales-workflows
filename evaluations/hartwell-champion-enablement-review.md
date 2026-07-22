# Hartwell Champion Enablement Review

This review scores the [worked enablement package](../examples/hartwell-champion-enablement-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every figure and fact traces to what was already established in the business case transcript and output |
| Evidence fidelity | 5 | Priya's evidence is built from the actual confirmed CRM-visibility concern, not a generic pitch |
| Fact separation | 5 | The outstanding compliance confirmation is kept clearly unconfirmed throughout, including in the likely-questions table |
| Missing information | 4 | Correctly flags the unconfirmed QBR date and the outstanding compliance item, but does not prepare Alex for the case where Priya raises a genuinely new concern beyond the two already on record |
| Commercial usefulness | 5 | The decision summary and internal note are both directly usable, not generic templates with brackets to fill in |
| Next step clarity | 4 | The internal note to Nadia has one clear ask; the package as a whole does not state what Alex's own next step is immediately after the QBR itself |
| Tone | 5 | Plain, no manufactured urgency, reads like something a person would actually say and send |
| Privacy | 5 | No individual account executive is named anywhere, consistent with Alex's own instruction |
| Approval discipline | 5 | Explicitly states Alex, not Shaun, sends the internal note, and nothing is presented as already sent |
| Hallucination risk | 4 | "The one item genuinely gating a full team rollout" is a reasonable characterisation of the compliance item's importance, but it is the output's own framing, not something stated outright in the source material, and a careful reviewer should treat it as an inference rather than a quoted fact |

## What Worked

- Priya's role-specific evidence is built entirely from her actual confirmed concern, the Monday pipeline meeting and CRM visibility lag, correctly avoiding the tempting but unsupported assumption that a Sales Director's real interest is AE quota or deal velocity.
- The compliance confirmation is treated as genuinely outstanding everywhere it appears, including in the answer to the question "has compliance actually confirmed this?", rather than being softened to make Alex look more prepared than the evidence supports.
- The internal note to Nadia reads as Alex's own voice asking a colleague for a status update, not as the seller reaching around the champion to contact a further stakeholder directly.
- The customer success extension, explicitly flagged elsewhere as a passing thought, correctly does not appear anywhere in the QBR material.

## What Needed Checking

- The characterisation of the compliance item as "genuinely gating" the rollout is the output's own reasonable inference from what Nadia's team asked for; it should be checked against Alex's own view before he repeats it as though it were a quoted fact.
- The package does not address what happens if Priya raises a concern that is not the CRM-visibility one already on record; a careful reviewer should treat the current role-specific evidence as a starting point, not a complete script for every question that might come up.
- The QBR date remains an estimate at roughly three weeks out and should be confirmed before this package is treated as final.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The guardrail against assuming a stakeholder's priority from their job title was the one most directly tested, and it held without needing a new rule.

## Next Test

Run a scenario with a third further stakeholder whose actual concern is genuinely unknown, nothing beyond their job title has been established, to confirm the skill says so plainly rather than filling the gap with a plausible-sounding guess.
