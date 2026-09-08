# 📉 Recipe: Review a Lost Opportunity

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Working out honestly whether a deal that did not close is actually over, or just blocked, before deciding whether there is a real way back in.

## You need

CRM history, the final message or stated reason, and anything you know about what changed on the prospect's side.

## You'll get

- What was actually said kept separate from what is being assumed
- The most likely reason it did not close
- Whether the underlying problem still exists
- What, if anything, would justify approaching it again

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/lost-opportunity-review-prompt.md -->
```text
Act as a careful, honest sales opportunity reviewer.

Use only the information I provide. Do not use outside knowledge and do not invent a reason for the loss, a future date, or a commitment that was not actually given.

Produce the following sections:

1. What was actually said
State the stated reason or final message exactly as given. If it blends more than one factor, say so rather than picking the one that makes the tidiest story.

2. What's being inferred, not confirmed
List anything I know or suspect that was not directly confirmed by the prospect, such as a stakeholder change or a reorganisation, and label it clearly as inference.

3. Whether the underlying problem still exists
Check whether the business problem this deal was solving is still real, independent of who raised it, championed it, or is no longer involved.

4. Classification
Classify this as one of: genuine disqualification, timing, stakeholder change, or unresolved objection. Explain which specific words or evidence support that classification, not a generic default.

5. What would justify coming back
Name a specific, real trigger if one exists in what was said. If nothing specific was given, say so plainly rather than inventing a hopeful plan.

6. What not to do next
List anything that would contradict what was actually said, such as chasing again immediately after being told to wait, or assuming a reason that was never confirmed.

Rules:

- Do not invent a reason, a date, or a commitment that was not given
- Keep confirmed statements and inferences clearly separate
- Do not default to either extreme: writing this off forever, or scheduling an immediate follow-up
- Flag anything reusable, such as a proof point or pilot result, that survives this particular loss
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/04-lost-opportunity-review.md)**  
Also: [Prompt](../templates/lost-opportunity-review-prompt.md) · [Skill](../.agents/skills/review-lost-opportunity/SKILL.md) · [Worked example](../examples/hartwell-lost-opportunity-analysis.md)

## The AI cannot decide

Whether this is genuinely a disqualification versus a paused opportunity, when the stated reason blends more than one factor together.

## You must check

- The stated reason is kept separate from what you are inferring
- A genuine disqualification is labelled that only because the evidence actually supports it
- Any reason to revisit later is specific, not vague hope

## Then

Decide whether and when to re-approach yourself; do not let this become a reason to chase someone who has clearly said no.

---

Want the fuller method or how to classify the type of loss? Open the [workflow](../workflows/04-lost-opportunity-review.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
