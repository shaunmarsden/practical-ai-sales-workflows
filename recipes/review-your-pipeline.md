# 📊 Recipe: Review Your Pipeline

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Checking whether the stages, close dates, stakeholders and next steps in your pipeline are actually supported by the evidence you hold, rather than trusting the CRM because it is written down.

## You need

An export or list of your open deals with their recorded stage, value, close date and last activity, plus whatever notes or evidence you hold on each.

## You'll get

For each deal, the recorded position next to the evidence-supported position, the gap between them, and what to confirm, all read-only.

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/pipeline-evidence-review-prompt.md -->
```text
Act as a careful, honest pipeline reviewer.

Use only the information I provide. Do not invent a stage, a date, a stakeholder, a reason or a next step that the evidence does not support. Do not change any CRM field; this review is read-only and every suggested change is for me to approve and make myself.

For each deal, work through the following:

1. Recorded position
State the stage, value, close date and next step exactly as the CRM has them.

2. Evidence-supported position
Say what state the evidence I have actually supports, using a working state such as exploring, qualification incomplete, problem confirmed, value case incomplete, stakeholder approval required, decision process unclear, commercial review, paused with a dated reason, lost, or disqualified, whichever actually fits, not a replacement set of official CRM stages. Keep confirmed facts, inferences and unknowns separate. If a stakeholder change or a departure is only inferred, label it as an inference, not a fact.

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
Before this step, show the recorded stage and the evidence-supported state side by side and name any conflict between them. Then suggest one concrete next step, left for me to approve. Where the honest answer is that a deal is healthy and the fields match the evidence, say so plainly rather than manufacturing a problem.

Finish with a short summary table: each deal, its recorded stage, its evidence-supported state, and the main gap.

Rules:
- Do not change any CRM field; suggest, do not act
- Do not treat the recorded stage as evidence of anything; it is a claim to check
- Do not accuse me of anything; pipelines drift, that is what this is for
- Do not invent a reason, date or contact where the evidence only supports an unknown
- Flag any close date that has already passed, since it distorts the pipeline total
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/06-pipeline-evidence-review.md)**  
Also: [Prompt](../templates/pipeline-evidence-review-prompt.md) · [Worked example](../examples/fictional-pipeline-review.md)

## The AI cannot decide

- Whether a stakeholder change is real rather than inferred
- What the true state of a deal is when notes and CRM disagree and neither is checked against the other

## You must check

- Every record actually belongs in your own pipeline, not just something you attended a meeting on
- Each field is judged against real evidence, not how the deal feels
- Genuinely healthy deals are called healthy, not just the problems

## Then

Approve or reject each suggested change yourself and update the CRM directly; nothing here edits a record on its own.

---

Want the fuller method or the working states used instead of the recorded stage? Open the [workflow](../workflows/06-pipeline-evidence-review.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
