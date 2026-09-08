# 🙅 Recipe: Handle an Objection

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Working out what is actually driving a stated objection, so you respond to the real concern instead of arguing with the surface wording.

## You need

- The objection as it was actually said
- What you know about the person's role and authority
- Whether you need a fast spoken answer or a considered written one

## You'll get

- A diagnosis of the real driver
- A structured response (Acknowledge, Isolate, Reframe, Ask)
- An honest pipeline decision, including disqualification where that is the right call

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/objection-handling-prompt.md -->
```text
Act as a careful sales objection handler.

Use only the information I provide. Do not invent a fact, a statistic, a guarantee, or a commitment such as a discount or a timeline that I have not told you is authorised.

First, restate the objection exactly as I gave it, without softening it.

Then work through the following:

1. Diagnose the real driver
Decide which of these is actually driving the objection, and explain why using what I have told you about the person's role, authority, and stage:
- circumstances (timing, budget, too busy, not now)
- other people (needs sign-off, a stakeholder to convince, someone to check with)
- self (needs to think it over, wants more information, genuine uncertainty)
- competitor or tooling (already has something in place, sees this as redundant)
- information (a specific factual question, wants proof, wants to understand a risk)
- disqualification (this genuinely does not fit)

The same words can sit in different buckets depending on who is saying them. Do not just match the surface wording.

2. Respond using Acknowledge, Isolate, Reframe, Ask
- Acknowledge: show it was heard, without agreeing it is fatal
- Isolate: confirm whether this is the only thing in the way, or one of several
- Reframe: address the real driver you diagnosed, not the surface wording
- Ask: end with a specific question or a concrete next step

3. Pipeline decision
State honestly what should happen next: progress, a dated follow-up, a longer nurture, or a genuine disqualification.

Rules:
- Never invent a fact, statistic, guarantee, or commitment to win the objection
- Never argue with a genuine disqualification
- Do not turn a single-issue objection into a full pitch; answer only what was raised
- Keep any competitor or existing tool neutral; never disparage it by name
- If the real driver is still unclear, or answering would need something not authorised, say so instead of answering around it
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/05-objection-handling.md)**  
Also: [Prompt](../templates/objection-handling-prompt.md) · [Skill](../.agents/skills/objection-response/SKILL.md) · [Worked example](../examples/hartwell-objection-response.md) · [Harder test: a contractual stop condition](../examples/wrenford-objection-response.md) · [Third test: the correct answer is the wrong move](../examples/thornbury-objection-response.md) · [Stability test across models](../evaluations/hartwell-objection-ambiguous-test.md)

## The AI cannot decide

- Which bucket the objection is really in when the evidence is genuinely ambiguous
- Whether this is truly a disqualification rather than a harder sell
- What you are actually willing to say or send

## You must check

- The real driver was diagnosed, not just the surface words answered
- Every claim in the response is one you can stand behind, with nothing invented
- Any competitor mentioned stays positioning-neutral

## Then

Send only what you have checked, and end with a dated next step: progress, a follow-up, a move to nurture, or an honest disqualification.

---

Want the fuller method, the guardrails, or a second worked test? Open the [workflow](../workflows/05-objection-handling.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
