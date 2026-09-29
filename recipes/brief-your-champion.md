# 🤝 Recipe: Brief Your Champion

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Getting an internal champion ready to make a case, backed by evidence, to other stakeholders. It doesn't guess what they care about from their job title, and you contact no one but the champion.

## You need

- What you already know for sure (the call record, and a business case if there is one)
- Who the champion is presenting to
- Anything you know about what that person cares about

## You'll get

- A decision summary the champion can speak from
- Evidence for each stakeholder, matched to their role
- Honest answers to likely questions
- An internal note the champion can send in their own name

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/champion-enablement-prompt.md -->
```text
Act as a careful sales assistant helping an internal champion prepare to carry a case to other stakeholders.

Use only the evidence I provide. Do not assume a stakeholder's priority from their job title alone; if I have not told you what a specific person actually cares about, say so rather than guessing. Do not resolve an outstanding or unconfirmed item into a settled fact.

Produce:

1. A decision summary the champion can speak from, not a document to hand over unread: the ask, the evidence behind it, and the one or two points most likely to matter in this specific meeting.

2. Role-specific evidence, one short section per further stakeholder I have named, using only what I have actually told you about their concern. If I have not told you what a stakeholder cares about beyond their title, say that plainly instead of inventing a plausible one.

3. Questions likely to come up, with an honest answer to each, including "not yet confirmed" wherever that is genuinely the answer.

4. An internal note, only if I ask for one, drafted for the champion to send in their own name to a specific further stakeholder. Never address it as though I, the seller, were sending it directly.

Rules:
- Never contact, or draft something addressed to, anyone beyond the champion
- Never assume a stakeholder's priority from their job title
- Never upgrade an unconfirmed or outstanding item to a settled fact
- Never invent a likely question that is not actually grounded in what the evidence leaves open
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/12-champion-enablement.md)**  
Also: [Prompt](../templates/champion-enablement-prompt.md) · [Skill](../.agents/skills/champion-enablement/SKILL.md) · [Worked example](../examples/hartwell-champion-enablement-output.md)

## The AI cannot decide

- What another stakeholder cares about, beyond what you already know
- How the champion should handle a question that comes up in the room

## You must check

- Each stakeholder's evidence rests on something you know, not a guess from their job title
- No open item has been quietly marked as settled to make things look further along
- Any internal note reads as the champion sending it, never you

## Then

Give the material to the champion to check and use. Nothing here contacts another stakeholder or presents anything for the champion.

---

For the fuller method, including how to match evidence to each stakeholder without guessing from titles, open the [workflow](../workflows/12-champion-enablement.md).

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
