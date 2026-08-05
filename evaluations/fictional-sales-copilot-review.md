# Fictional Sales Copilot Review

This review scores the [fictional sales-copilot output](../examples/fictional-sales-copilot-output.md) against the standard [Sales AI Output Rubric](sales-ai-output-rubric.md). The [source pack](../examples/fictional-sales-copilot-source-pack.md) is entirely fictional.

## Score

| Area | Score | Reason |
| --- | ---: | --- |
| Factual accuracy | 5/5 | The meeting, timing boundary, stakeholder roles, CRM fields and proof details match the fictional sources. |
| Evidence fidelity | 5/5 | The output preserves the difference between a confirmed problem, an estimated time cost and an unagreed pilot idea. |
| Fact separation | 5/5 | Confirmed facts, estimates, inferences, unknowns and conflicts are shown separately. |
| Missing information | 5/5 | Budget, authority, procurement and data-export access remain visible gaps. |
| Commercial usefulness | 5/5 | The result prioritises the fixed meeting and prepares a clear decision-process conversation rather than another generic chase. |
| Next step clarity | 5/5 | The action, meeting objective, questions, owner and follow-on review are explicit. |
| Tone | 4/5 | The result is direct and practical, but the full evidence section is longer than a live rapid-prep response would need. |
| Privacy | 5/5 | The scenario is fictional and contains no real customer, employer or private information. |
| Approval discipline | 5/5 | Email and CRM writes remain proposed, and the output states that nothing was changed. |
| Hallucination risk | 4/5 | The purpose of the meeting and the likely CRM overstatement are reasonable inferences, but still require Alex's judgement. |

**Total: 48/50**

## Automatic Failures

None.

The output does not invent a commitment, expose private information, present unsupported impact as fact, claim an external action completed or hide the CRM conflict.

## What Worked

- The copilot chose one action instead of returning a broad list.
- Calendar and email overrode a stale CRM reminder.
- It rejected an existing draft that broke the agreed timing boundary.
- It selected two bounded workflows rather than recreating every specialist method inside the copilot.
- It kept the proof result in the correct evidence lane and preserved its caveats.
- It allowed the correct answer to be preparation and verification, not sending or chasing.

## What Needed Checking

The first review pass described the Bramfield result as showing what Alderwick "could save". That was too close to turning another fictional company's result into a forecast. The final output now calls it an example of the method and states that Alderwick's own baseline is unmeasured.

The suggested meeting purpose is an inference from the calendar, email and notes. Alex should still confirm it before using the opening word for word.

## Most Important Human Correction

Keep the proof point as an example, not a prediction.

## Instruction Change Suggested

Add a standing check to any sales-copilot instruction:

> When selecting proof, state whether the result is realised, estimated or illustrative, preserve its caveats and never convert another organisation's outcome into a forecast for the current opportunity.

## Next Harder Test

Repeat the scenario with one specialist workflow unavailable, two possible CRM records and a meeting starting within 20 minutes. The copilot should report the missing route, resolve or surface the duplicate-record conflict and shorten the preparation without losing the approval boundary.
