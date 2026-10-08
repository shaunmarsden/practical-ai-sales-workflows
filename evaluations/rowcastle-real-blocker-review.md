# Rowcastle Real Blocker Diagnosis Review

This review scores the [worked diagnosis](../examples/rowcastle-real-blocker-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). The [scenario](../examples/rowcastle-real-blocker-input.md) is entirely fictional.

## Result

| | Score |
| --- | ---: |
| Score | 47 / 50 |
| Automatic failure | No |

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every attendee, role and stated question traces exactly to the scenario notes |
| Evidence fidelity | 5 | Keeps the answered data question apart from the consistency question that's still open, rather than merging them into one settled outcome |
| Fact separation | 5 | States each concern exactly as given, then separates it from what would resolve it, and refuses to guess at Marcus's motive |
| Missing information | 4 | Rightly flags that Naomi's authority is unconfirmed. But it doesn't split authority over a Leeds-only trial from authority over the wider commercial figure, and the scenario notes that difference as open |
| Commercial usefulness | 5 | Gives two separate next steps you can act on, rather than one generic "follow up" |
| Next step clarity | 4 | Both next steps are specific, but neither says who should ask them or by when |
| Tone | 5 | Plain and measured, with no invented urgency about the unplanned attendee or the open question |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | Says plainly that nobody has been contacted and nothing has been sent |
| Hallucination risk | 4 | Mostly careful, but "Group Ops has not been identified by name, role or contact route" moves from "not yet confirmed" towards a claim about Rowcastle's own structure that the scenario doesn't rule out |

## What Worked

- It named Marcus as an unplanned attendee straight away, not only once his questions turned out to matter.
- It saw that the data-handling question was answered and not pressed, and flagged the cross-office question as the one still open. It didn't treat the exchange as settled once the first question got a clean answer.
- It refused to guess why cross-office consistency mattered to Marcus. It also refused to claim Naomi lacks real authority, or that Group Ops is confirmed as the blocker.
- It gave two separate next steps rather than one vague "circle back."

## What Needed Checking

- The authority question could have been split more precisely: authority over a Leeds-only trial, against authority over the wider commercial number Naomi mentioned. The scenario leaves both open, and the output only fully covers the second.
- "Group Ops has not been identified by name, role or contact route" fairly sums up what's missing. But it reads a little more like a finding about Rowcastle's structure than a note of what this call didn't establish. Worth rewording if the pattern comes up again.
- The output says Naomi "sounded ready to proceed". The scenario never describes how she sounded, so that detail is the output's own, and the 5 for factual accuracy above is a little generous.

## What I Changed in the Prompt

Nothing in the skill needed changing for this run. This run tested most directly the guardrail against inventing a motive for the cross-office question, and it held with no new rule.

## Next Test

Run a second scenario where the unplanned attendee's title doesn't match what they raise at all, rather than fitting the first question and only drifting on the second. That checks whether the skill still catches the mismatch when it's less subtle than this one.
