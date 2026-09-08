# 🔎 Recipe: Find the Next Prospect

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Picking a cold target worth approaching and drafting a first-touch message worth a reply, without a generic industry observation or a meeting-led ask.

## You need

- Your ideal customer profile
- Whatever tracker or CRM record already exists
- A specific public signal for the target you have in mind

## You'll get

A scored read on whether the target is worth approaching, and a short first-touch message built from a real, verifiable signal.

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/outbound-prospecting-prompt.md -->
```text
Act as a careful outbound prospecting adviser.

Use only the information I provide. Do not invent a company signal, a hook, or a fact about the target that was not actually found. If nothing specific and verifiable exists, say so rather than writing a generic opener anyway.

1. Score the target
Assess whether this is worth approaching:
- Is there a named, reachable buyer with plausible authority over this kind of decision?
- Is there a specific, verifiable public signal tied to the actual problem, not a generic industry trend?
- Is there a workable route to a real contact, not only a best-guess address?

Score it down if the only hook is a generic trend with nothing company-specific behind it, or if the company's size makes procurement and politics likely to slow everything down without an unusually strong contact route.

2. Draft the first-touch message
- Open with a question tied to the buyer's actual role and the specific signal found, not a generic observation.
- Offer something small and genuinely useful that can be produced quickly, not a meeting ask.
- State what that offer is worth to the reader in their own terms, in one sentence.
- End with a single, low-friction next step, usually a short reply.

Rules:
- Never fabricate a company signal or hook
- Never lead with a meeting ask unless I have told you that is the deliberate approach for this prospect
- Keep the message short; it should not read like a pitch deck
- Never claim a capability, statistic, or outcome that has not actually been confirmed
- If the contact's email is an unverified guess, say so rather than treating it as confirmed
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/09-outbound-prospecting.md)**  
Also: [Prompt](../templates/outbound-prospecting-prompt.md) · [Skill](../.agents/skills/outbound-prospecting/SKILL.md) · [Worked example](../examples/cedarwell-outbound-output.md) · [Weak example, for contrast](../examples/cedarwell-outbound-weak-example.md)

## The AI cannot decide

- Whether a signal is actually specific and verifiable rather than a generic trend
- Whether the named contact genuinely has authority
- Whether to actually send the message

## You must check

- The hook is built from a real, verifiable signal, not a generic observation
- The contact route has actually been verified, not just guessed
- Nothing in the message was invented to sharpen the hook

## Then

Verify the contact route, confirm every claim, log the send so it never goes out twice, and stop the sequence immediately on any reply.

---

Want the fuller method, the guardrails, or the scoring logic? Open the [workflow](../workflows/09-outbound-prospecting.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
