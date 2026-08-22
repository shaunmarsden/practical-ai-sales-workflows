# Rowcastle Real Blocker Diagnosis Review

This review scores the [worked diagnosis](../examples/rowcastle-real-blocker-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). The [scenario](../examples/rowcastle-real-blocker-input.md) is entirely fictional.

## Result

| | Score |
| --- | ---: |
| Score | 47 / 50 |
| Automatic failure | No |

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every attendee, role, and stated question traces exactly to the scenario notes |
| Evidence fidelity | 5 | Preserves the distinction between the resolved data question and the still-open consistency question, rather than collapsing them into one settled outcome |
| Fact separation | 5 | Each concern is stated exactly as given, then separated from what would actually resolve it, with an explicit refusal to guess at Marcus's motive |
| Missing information | 4 | Correctly flags that Naomi's authority is unconfirmed, but does not separately distinguish authority over a Leeds-only trial from authority over the wider commercial figure, when the scenario notes that distinction as genuinely open |
| Commercial usefulness | 5 | Gives two distinct, actionable next steps rather than one generic "follow up" |
| Next step clarity | 4 | Both next steps are specific in substance, but neither names who should ask them or by when |
| Tone | 5 | Plain and measured, no manufactured urgency about the unplanned attendee or the open question |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | States plainly that nobody has been contacted and nothing has been sent |
| Hallucination risk | 4 | Mostly careful, but "Group Ops has not been identified by name, role or contact route" edges from "not yet confirmed" toward asserting a negative about Rowcastle's own structure that the scenario does not actually rule out |

## What Worked

- Named Marcus as an unplanned attendee immediately, rather than only surfacing it once his questions turned out to matter.
- Correctly identified that the data-handling question was answered and not pushed on, and separately flagged the cross-office question as the one that stayed open, rather than treating the exchange as fully resolved once the first question got a clean answer.
- Explicitly refused to guess why cross-office consistency mattered to Marcus, and explicitly refused to claim Naomi lacks real authority or that Group Ops is confirmed as the blocker.
- Gave two distinct next steps rather than one vague "circle back."

## What Needed Checking

- The authority question could have been split more precisely: authority over a Leeds-only trial specifically, versus authority over the wider commercial number Naomi mentioned. The scenario leaves both open, and the output only fully addresses the second.
- "Group Ops has not been identified by name, role or contact route" is a fair summary of what is missing, but reads slightly more like a finding about Rowcastle's structure than a statement about what this call did not establish. Worth rephrasing if this pattern recurs.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The guardrail against inventing a motive for the cross-office question was the one most directly tested, and it held without needing a new rule.

## Next Test

Run a second scenario where the unplanned attendee's title genuinely does not match what they raise at all, rather than fitting the first question and only diverging on the second, to check the skill still catches the mismatch when it is less subtle than this one.
