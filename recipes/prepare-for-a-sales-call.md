# 📞 Recipe: Prepare for a Sales Call

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Turning scattered account information into one short call card you can actually scan during the conversation.

## You need

- Contact name, role and company
- The purpose of the meeting
- Relevant CRM notes or previous interactions
- Approved public company information

## You'll get

- A concise call card with confirmed facts kept separate from assumptions
- Missing information flagged
- Discovery questions and conversation paths for the call

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=workflows/01-pre-call-preparation.md -->
```text
Act as a sales preparation assistant. Use only the information I provide.

Create a concise pre call card using the supplied template. Separate confirmed facts from assumptions. Do not invent company initiatives, challenges, budgets, technologies or personal details. If evidence is missing, state "Unknown" and suggest a discovery question.

Keep the card practical enough to scan during a live call. The salesperson will verify the output and decide what to use.
```
<!-- prompt:end -->

This prompt refers to a card template, which is the next block, so paste that in too.

## And the card it fills in

<!-- prompt:begin source=templates/pre-call-card.md -->
```text
## Call

- **Contact:**
- **Role:**
- **Company:**
- **Meeting purpose:**
- **Good outcome:**

The good outcome is the salesperson's objective, not an agreed customer next step.

## Source Ledger

| Source | Checked | What It Supports |
| --- | --- | --- |
| | | |

## Confirmed Context

-
-
-

## Public Background

-

State what the public information does not prove.

## Assumptions to Test

-
-

## Unknowns

-
-

## Relevance Hypothesis

If __________, then __________ may be worth exploring.

## Opening

One natural sentence connecting the reason for the meeting to the contact's context:

>

## Discovery Questions

1.
2.
3.
4.

## Conversation Paths

### The Problem Is Relevant

- Explore:
- Evidence to listen for:
- Sensible next step:

### The Hypothesis Is Wrong or Not a Priority

- Ask:
- Alternative area to explore:
- Sensible close:

### Voicemail or No Answer

>

## Human Check Before the Call

-
-
```
<!-- prompt:end -->

Paste this underneath the prompt, then your own research below that.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/01-pre-call-preparation.md)**  
Also: [Skill](../.agents/skills/prepare-for-sales-call/SKILL.md) · [Card template](../templates/pre-call-card.md) · [Worked example](../examples/hartwell-pre-call-skill-output.md) · [Honest review](../evaluations/hartwell-pre-call-review.md) · [Optional roleplay prompt](../templates/pre-call-objection-roleplay-prompt.md)

## The AI cannot decide

- Whether a public claim is actually reliable enough to use
- What is appropriate to raise with this specific contact
- Which conversation path to actually take live

## You must check

- The named person and company are correct
- Every factual claim traces back to a source
- Assumptions are clearly labelled, not stated as fact

## Then

Correct or remove anything wrong, decide what is actually appropriate to use, and optionally practise pushback with the roleplay prompt before the call.

---

Want the fuller method or the full information checklist? Open the [workflow](../workflows/01-pre-call-preparation.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
