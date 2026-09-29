# Hartwell Champion Enablement Review

This review scores the [worked enablement package](../examples/hartwell-champion-enablement-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every figure and fact matches what the business case transcript and output had already established |
| Evidence fidelity | 5 | Priya's evidence comes from her confirmed concern about CRM visibility, not a generic pitch |
| Fact separation | 5 | Keeps the outstanding compliance confirmation clearly unconfirmed throughout, including in the table of likely questions |
| Missing information | 4 | Rightly flags the unconfirmed QBR date and the outstanding compliance item, but doesn't prepare Alex for Priya raising a new concern beyond the two on record |
| Commercial usefulness | 5 | The decision summary and internal note are both ready to use, not generic templates with brackets to fill in |
| Next step clarity | 4 | The internal note to Nadia has one clear ask, but the package doesn't say what Alex's own next step is straight after the QBR |
| Tone | 5 | Plain, with no made-up urgency. It reads like something a person would say and send |
| Privacy | 5 | Names no individual account executive anywhere, as Alex asked |
| Approval discipline | 5 | Says Alex, not Shaun, sends the internal note, and presents nothing as already sent |
| Hallucination risk | 4 | "The one item genuinely gating a full team rollout" is a fair description of how much the compliance item matters. But it's the output's own framing, not something the source material says outright, so a careful reviewer should treat it as an inference, not a quoted fact |

## What Worked

- Priya's evidence for her role comes entirely from her confirmed concern, the Monday pipeline meeting and the lag in CRM visibility. It avoids the tempting but unsupported guess that a Sales Director really cares about AE quota or deal speed.
- It treats the compliance confirmation as outstanding everywhere, including in the answer to "has compliance actually confirmed this?" It doesn't soften it to make Alex look better prepared than the evidence allows.
- The internal note to Nadia reads as Alex asking a colleague for an update in Alex's own voice. It doesn't read as the seller going round the champion to contact another stakeholder.
- The customer success extension, flagged elsewhere as a passing thought, rightly appears nowhere in the QBR material.

## What Needed Checking

- Calling the compliance item "genuinely gating" the rollout is the output's own fair inference from what Nadia's team asked for. Check it against Alex's view before Alex repeats it as if it were a quoted fact.
- The package doesn't cover Priya raising a concern other than the CRM visibility one on record. A careful reviewer should treat the evidence for her role as a starting point, not a full script for every question.
- The QBR date is still an estimate, roughly three weeks away, and needs confirming before anyone treats this package as final.

## What I Changed in the Prompt

Nothing, for this run. This run tested most directly the guardrail against assuming a stakeholder's priority from their job title, and it held without a new rule.

## Next Test

Run a scenario with a third stakeholder whose real concern is unknown, with nothing established beyond their job title. That would confirm the skill says so plainly rather than filling the gap with a guess that sounds right.
