# Hartwell Chase Decision Review

This review scores the [worked decision](../examples/hartwell-chase-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

> **The scenario has changed since I scored this.** The chase scenario now names the weekdays, so the promised Thursday is 9th July, and you can check its clash with the leave rather than infer it. I scored this against the version without them. The [stale-date test](chase-stale-date-test.md) explains why I added the weekdays.

> This test has since been [run again, blind](repeat-run-findings.md), and the repeat scored exactly 48 out of 50 again. That page explains why two of the three repeats scored higher than their published scores.

## Result

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Gives the dates, automatic reply, CRM task and conditional transcript approval exactly as supplied |
| Evidence fidelity | 5 | Rightly lets the newer email outweigh the older CRM reminder, while keeping the clash over transcript timing in view |
| Fact separation | 5 | Keeps confirmed information and unknowns clearly apart |
| Missing information | 5 | Leaves the transcript approval, review timing, current interest and chance of a newer reply all open |
| Commercial usefulness | 5 | Stops a badly timed chase while keeping a clear way back into the opportunity |
| Next step clarity | 5 | Gives a review date, the checks to make first and a short draft for a person to review |
| Tone | 4 | The draft is direct and specific, though "pause the test for now" may make closing a little easier than moving forward |
| Privacy | 5 | Uses only the fictional information supplied and adds no needless personal detail |
| Approval discipline | 5 | Treats nothing as sent, scheduled or changed, and leaves the CRM task for a person to check |
| Hallucination risk | 4 | Reviewing on 21st July is a sensible suggestion, not an agreed date, and the output says so |

## What Worked

- The skill didn't blindly follow an out-of-date CRM task. It compared that task with the newer automatic reply and went with the current evidence.
- It saw that silence with a known reason isn't the same as lost interest.
- It didn't use Priya's name as licence to go round Alex.
- It kept the condition attached to the transcript instead of calling it overdue.
- It kept the clashing dates in view rather than quietly picking the one that supported a chase.
- The draft for later rests on Hartwell's real problem and avoids filler or made-up urgency.

## What Needed Checking

- The 21st July review point is a suggestion, not a customer commitment.
- The draft gives Alex an easy way to pause. That may make commercial sense, but a salesperson should decide whether the real relationship supports that wording.
- An automatic reply confirms availability, not continued interest. The output rightly makes no claim either way about intent.

## What I Changed in the Skill

Nothing, for this run. The instruction to gather new signals before deciding, and to choose "wait" when a known reason makes the timing poor, got the right result.

## Next Test

Use a harder case: the prospect is back, the CRM and email agree a chase is due, but the original call gives only a weak hook. The skill should either ask for better evidence or suggest closing the loop, instead of writing a generic "checking in" message.
