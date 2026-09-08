# 🗓️ Recipe: Get a Weekly View Without Building a Dashboard

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Pulling pipeline, meetings, outreach and new signals into one honest weekly report, composing what other reviews already found rather than redoing the analysis, and marking anything missing instead of guessing it.

## You need

- Whatever you actually have this week: a CRM export, confirmed meetings, outreach activity if you have it, new signals
- Any findings from other reviews you have already run

## You'll get

One report covering pipeline, meetings, outreach, signals and items needing attention, with missing sections marked as missing, and three evidence-backed priorities for next week.

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/weekly-operating-review-prompt.md -->
```text
Act as a careful, honest weekly operating reviewer.

Use only the information I provide. Do not invent a metric, a trend, or a comparison to an earlier period unless I have actually given you an earlier report to compare against. If a section has nothing behind it, mark it as missing rather than assuming it means zero.

Produce a report with these sections:

1. Pipeline movement
If I have given you an earlier report, compare honestly. If this is the first report, or no earlier one exists, say so plainly rather than describing a trend.

2. Meetings and commitments
State only what was actually confirmed. Do not imply a fuller calendar than what I gave you.

3. Outreach activity
If I have not provided this, say it is missing, not that no outreach happened.

4. New signals
Anything new found this week worth acting on.

5. Items needing attention
If I have given you findings from another review already run, pull the headline points through directly rather than re-analysing the same records from scratch.

6. Three priorities for next week
Specific to what this week's data actually surfaced, not generic advice. Each should name what needs to happen and, where relevant, who needs to do it.

Rules:
- Never claim movement or a trend without a genuine earlier report to compare against
- Never treat a missing section as if it means zero
- Do not repeat the full analysis from another review I have given you; link to it and summarise the headline
- Do not merge, delete, update, send or book anything; every action is a suggestion for me to approve
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/10-weekly-operating-review.md)**  
Also: [Prompt](../templates/weekly-operating-review-prompt.md) · [Worked example](../examples/fictional-weekly-operating-review-output.md)

## The AI cannot decide

- Whether a section with no data behind it should read as missing or as zero
- What this week's genuine priorities are if the underlying reviews were not actually run

## You must check

- No movement or trend is claimed without a genuine earlier report to compare against
- Every missing section is marked missing, not silently treated as zero
- The three priorities are specific to this week's findings, not generic advice

## Then

Approve every suggested action yourself; nothing here changes a CRM record, sends a message or books a meeting on its own.

---

Want the fuller method or how it composes other reviews instead of re-deriving them? Open the [workflow](../workflows/10-weekly-operating-review.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
