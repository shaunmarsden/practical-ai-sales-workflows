# Hartwell Chase Decision Review

This review scores the [worked decision](../examples/hartwell-chase-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The dates, automatic reply, CRM task and conditional transcript approval are represented exactly as supplied |
| Evidence fidelity | 5 | The newer email signal correctly outweighs the older CRM reminder, while the conflicting transcript timing stays visible |
| Fact separation | 5 | Confirmed information and unknowns are clearly separated |
| Missing information | 5 | The transcript approval, review timing, current interest and possibility of a newer reply all remain open |
| Commercial usefulness | 5 | It prevents a poorly timed chase while preserving a clear route back into the opportunity |
| Next step clarity | 5 | It gives a review date, the checks to make first and a short draft for human review |
| Tone | 4 | The draft is direct and specific, although “pause the test for now” may make it slightly easier to close than progress |
| Privacy | 5 | It uses only the fictional information supplied and adds no unnecessary personal detail |
| Approval discipline | 5 | Nothing is treated as sent, scheduled or changed, and the CRM task remains subject to a human check |
| Hallucination risk | 4 | Reviewing on 21st July is a sensible recommendation rather than an agreed date, and the output labels it as such |

## What Worked

- The skill did not obey a stale CRM task blindly. It compared that task with the newer automatic reply and used the current evidence.
- It recognised that explained silence is not the same as lost interest.
- It did not use Priya's name as permission to go around Alex.
- It preserved the condition attached to the transcript instead of calling it overdue.
- It kept the conflicting dates visible rather than quietly selecting the version that supported a chase.
- The future draft is anchored to Hartwell's actual problem and avoids filler or manufactured urgency.

## What Needed Checking

- The 21st July review point is a recommendation, not a customer commitment.
- The draft gives Alex an easy route to pause. That may be commercially sensible, but a salesperson should decide whether the live relationship supports that wording.
- An automatic reply confirms availability, not continued interest. The output correctly avoids making either a positive or negative claim about intent.

## What I Changed in the Skill

Nothing needed changing for this run. The existing instruction to gather new signals before deciding, and to choose “wait” when a known reason makes the timing poor, produced the right result.

## Next Test

Use a harder case where the prospect has returned, the CRM and email evidence agree that a chase is due, but the original call provides only a weak anchor. The skill should either ask for better evidence or recommend closing the loop instead of producing a generic “checking in” message.
