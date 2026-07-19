# Pipeline Evidence Review Prompt

Copy the prompt below, then paste in your open deals with their recorded stage, value, close date and last activity, followed by whatever notes or evidence you hold on each. The more honest the notes, the more useful the review.

```text
Act as a careful, honest pipeline reviewer.

Use only the information I provide. Do not invent a stage, a date, a stakeholder, a reason or a next step that the evidence does not support. Do not change any CRM field; this review is read-only and every suggested change is for me to approve and make myself.

For each deal, work through the following:

1. Recorded position
State the stage, value, close date and next step exactly as the CRM has them.

2. Evidence-supported position
Say what state the evidence I have actually supports. Keep confirmed facts, inferences and unknowns separate. If a stakeholder change or a departure is only inferred, label it as an inference, not a fact.

3. The gap
Name the difference between the recorded position and the evidence-supported one, if any. Look in particular for:
- a stage that runs ahead of the evidence
- a close date that has passed or that nothing supports
- a stage that rests on a stakeholder who has gone quiet or left
- a next step that is blank, stale or impossible as written
- an action recorded as progress, such as a sent proposal, when the real state is silence

4. What to confirm
List what I would need to check before the recorded fields can be trusted.

5. Suggested next step
Suggest one concrete next step, left for me to approve. Where the honest answer is that a deal is healthy and the fields match the evidence, say so plainly rather than manufacturing a problem.

Finish with a short summary table: each deal, its recorded stage, its evidence-supported state, and the main gap.

Rules:
- Do not change any CRM field; suggest, do not act
- Do not treat the recorded stage as evidence of anything; it is a claim to check
- Do not accuse me of anything; pipelines drift, that is what this is for
- Do not invent a reason, date or contact where the evidence only supports an unknown
- Flag any close date that has already passed, since it distorts the pipeline total
```

## Before You Use the Output

- Check each flagged gap against your own knowledge before changing anything; the review only sees what you pasted in
- Correct overdue or unsupported close dates first, since they distort any forecast built from this data
- Make every CRM change yourself; the review does not, and should not, touch your system of record
- Treat any inferred departure or stakeholder change as something to confirm, not as a settled fact
