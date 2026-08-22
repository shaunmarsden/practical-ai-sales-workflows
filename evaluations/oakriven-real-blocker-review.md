# Oakriven Real Blocker Diagnosis Review

This review scores the [worked diagnosis](../examples/oakriven-real-blocker-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests a harder pattern than the [Rowcastle test](rowcastle-real-blocker-review.md): rather than an unplanned attendee, the enthusiastic contact himself proposes a plan that would get an enrolment far enough along that the actual decision-maker would face something already done, rather than a genuine upfront choice.

## Result

| | Score |
| --- | ---: |
| Score | 47 / 50 |
| Automatic failure | No |

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every detail, the hallway conversation, the cohort date, the proposed process, traces exactly to the scenario notes |
| Evidence fidelity | 5 | Preserves the distinction between a vague, pre-specifics reaction and an actual confirmed sign-off, rather than treating Dev's account as settled |
| Fact separation | 5 | States what Dev said exactly, then separates it from what would actually resolve the authority question, without inventing Rina's likely answer either way |
| Missing information | 4 | Correctly treats Rina's authority as unconfirmed, but does not consider that Rina herself may not be the final approver; nothing in the scenario rules out a further approval step beyond her either |
| Commercial usefulness | 5 | Gives a clear, actionable recommendation, ask Rina directly and promptly, rather than a vague caution to "be careful" |
| Next step clarity | 4 | Correctly says to ask Rina promptly given the deadline, but does not propose a specific day or timeframe, leaving "promptly" as open to interpretation as the deadline pressure it is meant to resolve |
| Tone | 5 | Plain and non-accusatory; explicitly declines to treat Dev's optimism as bad faith |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | States plainly nobody has been contacted, and explicitly declines to have this diagnosis contact anyone itself |
| Hallucination risk | 4 | Careful throughout, but "neither, on current evidence, is anyone else yet" the confirmed decision-maker edges from "not yet confirmed" toward implying doubt about Rina's authority specifically, when the honest position is simply that it has not been tested either way |

## What Worked

- Correctly identified that Dev's enthusiasm and urgency are not evidence of his own authority, and correctly did not treat his role as ruling authority in or out on title alone.
- Correctly separated a vague, pre-specifics hallway reaction from an actual confirmed approval of this specific enrolment, cohort date and commitment.
- Named the proposed process itself, informing Rina after the paperwork is done, as the specific thing to avoid, rather than only flagging that her authority was unconfirmed in the abstract.
- Explicitly declined to treat Dev as acting in bad faith, and explicitly declined to guess whether Rina would approve or refuse.
- Treated the real deadline pressure as a reason to ask promptly, not as a reason to skip asking directly, which is the correct response to genuine urgency rather than either ignoring it or letting it justify skipping the check.

## What Needed Checking

- Rina may not be the final approver either; nothing in the scenario establishes whether a further sign-off sits above her, and the diagnosis does not raise this as an open question the way the Rowcastle test raised "Group Ops."
- "Ask Rina promptly" would be stronger with an actual day or short window attached, given the deadline pressure the scenario itself describes.
- The phrase used for the authority gap edges toward casting doubt on Rina's authority specifically, rather than stating plainly that it simply has not been tested yet in either direction.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The guardrail against treating enthusiasm or being the point of contact as confirmation of authority was the one most directly tested, and it held even against a proposed process specifically designed to make that authority question harder to ask before the fact.

## Next Test

Run a scenario where the enthusiastic contact's account of a stakeholder's position turns out, once actually checked, to be accurate, to confirm the skill does not treat every unconfirmed authority claim as suspect by default, only as genuinely unconfirmed until it is actually tested.
