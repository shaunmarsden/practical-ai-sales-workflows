# Northstar Opportunity Handover Review

This review scores the [finished handover](../examples/northstar-opportunity-handover.md) against the [Sales AI Output Rubric](sales-ai-output-rubric.md).

## Result

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Names, roles, systems, numbers and actions match the source material |
| Evidence fidelity | 5 | Internal approval, conditional timing and the unconfirmed meeting are preserved |
| Fact separation | 5 | Confirmed evidence, estimates, assumptions and unknowns are kept apart |
| Missing information | 5 | Buying information, approval, tools and meeting details are shown as unknown |
| Commercial usefulness | 5 | A receiving salesperson can understand the position and continue the work |
| Next step clarity | 5 | The immediate action, current owner and required check are clear |
| Tone | 4 | The language is direct, although some sections could be shortened after real use |
| Privacy | 5 | The example is fictional and includes only relevant sales information |
| Approval discipline | 5 | No message, ownership change or CRM update is treated as completed |
| Hallucination risk | 4 | Relative timing could become misleading if the handover is read without the original call date |

## What Worked

- The 30 second brief makes the current position and caution easy to find.
- The handover does not turn a possible test into a qualified sales opportunity.
- Priya remains a possible later stakeholder rather than a confirmed decision maker.
- Conditional approval and timing are carried into the actions and risks.
- The receiving person gets source links rather than being asked to trust the summary alone.

## What Needed Checking

- The call date is missing, so today and Thursday afternoon will lose meaning over time.
- Completion of Shaun's actions cannot be confirmed from the supplied evidence.
- The recommended next action must be checked against any newer email or CRM activity before use.

## What I Changed in the Prompt

The prompt now asks for a status as well as an owner and timing for each action. It also requires source labels, a handover check and a warning not to claim that links have been opened when only their addresses were supplied.

## Next Test

Use a longer fictional opportunity with several calls, conflicting notes and a change of contact. Check whether the workflow finds the newest reliable evidence without hiding earlier contradictions.
