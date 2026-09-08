# 🕵️ Recipe: Spot the Real Blocker

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Checking whether the person on a call is actually the decision-maker, and whether their stated objection is the real one or standing in for something unstated, using only what was actually said.

## You need

- Who was expected on the call, and who actually attended
- Each attendee's role, where known
- What each attendee actually said, especially anything raised as a concern
- Anything already confirmed about who holds sign-off authority

## You'll get

- Who was actually on the call, with any unplanned attendee named explicitly
- Each attendee's role checked against what they actually said
- The stated reason kept separate from what would actually resolve it
- An honest read on who actually decides
- A specific next question, not a generic follow-up

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/real-blocker-diagnosis-prompt.md -->
```text
Act as a careful sales call diagnostician.

Use only the information I provide. Do not invent a hidden motive, a reason, or a decision-maker that I have not actually described.

Produce the following sections:

1. Who was actually on the call
Compare who was expected with who actually attended. Name any unplanned or last-minute attendee explicitly.

2. Role against stated concern
For each attendee, compare their role or title against what they actually said. Flag any mismatch plainly. If someone's stated concern shifted partway through, say what changed and which concern stayed open.

3. Stated reason versus checkable fact
For each concern raised, state it exactly as given, then note separately what would actually resolve it. Do not guess at an underlying motive with nothing behind it.

4. Who actually decides
Do not treat enthusiasm or being the point of contact as confirmation of authority. If nobody has explicitly confirmed holding budget or sign-off authority, say so, and name anyone else who was mentioned as a further approver, without assuming they are definitely the real blocker.

5. Recommended next step
Name the specific next question or person to identify, not a generic follow-up.

Rules:
- Do not assert a hidden motive the evidence does not support; flag the mismatch, do not invent the explanation for it
- Do not treat a plausible-sounding answer as proof an objection is fully resolved if the underlying authority or motive question was never tested
- Do not contact anyone not already on the thread; recommend the next question, do not draft it as if sending it
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/15-real-blocker-diagnosis.md)**  
Also: [Prompt](../templates/real-blocker-diagnosis-prompt.md) · [Skill](../.agents/skills/real-blocker-diagnosis/SKILL.md) · [Worked example](../examples/rowcastle-real-blocker-output.md) · [Honest review](../evaluations/rowcastle-real-blocker-review.md) · [Harder test: enrolling by stealth](../examples/oakriven-real-blocker-output.md)

## The AI cannot decide

- What an attendee's real, unstated motive actually is, if one exists
- Whether a named further approver is genuinely the real blocker or just the first name mentioned
- How, or whether, to actually raise a flagged mismatch with the prospect

## You must check

- Every flagged mismatch is supported by something someone said or did, not speculation
- A concern that shifted partway through the call is still treated as open, not folded into the one that got answered
- Nobody's authority is being assumed from enthusiasm or being the point of contact

## Then

Decide yourself whether and how to raise anything flagged, and confirm authority directly before treating the deal as further along than it is; nothing here contacts anyone.

---

Want the fuller method or the worked Rowcastle test? Open the [workflow](../workflows/15-real-blocker-diagnosis.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
