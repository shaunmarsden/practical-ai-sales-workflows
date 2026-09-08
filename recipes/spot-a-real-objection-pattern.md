# 📈 Recipe: Spot a Real Objection Pattern

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Looking across several deals for a repeated objection, and telling a genuine recurring issue apart from several unrelated situations that just sound similar.

## You need

A log of objections across multiple deals: the exact wording, the stage, who raised it, how it was handled, and the outcome.

## You'll get

Genuine patterns identified with a confidence level per pattern, and surface-level patterns explicitly flagged as not the same thing as a systemic cause.

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/objection-pattern-review-prompt.md -->
```text
Act as a careful, honest objection pattern reviewer.

Use only the information I provide. Do not invent an objection, a driver, or an outcome that is not in the log.

Work through the following:

1. Identify what recurs
Group objections by similar wording or topic, and count how often each appears and across how many distinct deals.

2. Check the driver behind each occurrence
For each recurring group, look at whether the underlying reason and outcome were actually similar each time, or only the surface wording. The same words can hide different real drivers in different deals.

3. Assign confidence per pattern
Give each identified pattern its own confidence level. A pattern built from genuinely similar underlying needs deserves higher confidence than one built only from similar wording. Do not let a strong finding lend false confidence to a weaker one.

4. Say what is worth acting on
For each pattern, state plainly whether it is worth building something from (a prepared answer, a playbook item) or whether it looks real but is not, because the underlying drivers differ.

5. Say what the sample cannot tell you
Note where the log is too small, or too narrow across deal types or sectors, to treat a finding as settled either way.

Rules:
- Never report a win rate, loss rate, or percentage from a small or mixed sample
- Never treat a shared word or phrase as proof of a shared underlying cause
- Do not suggest a product, pricing, or playbook change as if it is already decided; every action is for me to build and approve
- If a pattern's evidence is genuinely mixed, say so rather than picking the more convenient reading
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/11-objection-pattern-review.md)**  
Also: [Skill](../.agents/skills/review-objection-patterns/SKILL.md) · [Prompt](../templates/objection-pattern-review-prompt.md) · [Worked example](../examples/fictional-objection-pattern-review.md) · [Harder test](../examples/fictional-objection-pattern-review-two.md) · [Decoy-entry test](../examples/fictional-objection-pattern-review-three.md) · [Opposite-behaviour test](../examples/fictional-objection-pattern-review-four.md)

## The AI cannot decide

Whether the underlying driver behind two similar-sounding objections was genuinely the same, when the log itself does not record enough detail to tell.

## You must check

- Each pattern rests on the same underlying driver each time, not just similar wording
- The confidence level is specific to that pattern, not borrowed from a stronger one nearby

## Then

Decide what to actually do with a confirmed pattern yourself; nothing here changes a playbook, a product decision, or a CRM record on its own.

---

Want the fuller method or what a small sample genuinely cannot tell you? Open the [workflow](../workflows/11-objection-pattern-review.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
