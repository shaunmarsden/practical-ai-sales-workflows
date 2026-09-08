# ✉️ Recipe: Follow Up After a Sales Call

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Turning a transcript or clear notes into a summary, agreed actions, a follow-up email draft and CRM suggestions, without inventing commitments or momentum that were not actually there.

## You need

A transcript or clear notes from the call, plus relevant CRM or email context.

## You'll get

- A short summary
- Confirmed facts and estimates kept separate
- Agreed actions with owners and dates
- A natural-sounding email draft
- Suggested CRM updates

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/post-call-follow-up-prompt.md -->
```text
Act as a careful sales follow up assistant.

Use only the information I provide. Do not use outside knowledge and do not invent customer problems, urgency, authority, budgets, dates, commitments, meetings or next steps.

Produce the following sections:

1. Call summary
Write no more than five bullet points covering the reason for the call, the problem discussed, the desired outcome and the current position.

2. Confirmed facts
List information directly supported by the source. Keep estimates separate and label them clearly.

3. Actions and commitments
Use a table with Owner, Action, Timing and Evidence. If timing is relative, preserve the original wording. Do not convert it into a calendar date unless the call date is supplied.

4. Missing information and checks
List anything unclear, conditional or still requiring confirmation.

5. Follow up email draft
Write a concise, natural email from the salesperson. Include only supported information and agreed actions. Use a clear placeholder for anything the salesperson must check before sending.

6. Suggested CRM updates
Prepare a short call note, next step, key problem, stakeholders and risks. Label every item as a suggestion for human review. Do not claim that anything has been saved.

7. Final accuracy check
List any statement in your own output that could be mistaken for a confirmed fact or commitment. Correct it before presenting the final answer.

Rules:

- Separate confirmed facts, estimates, inferences and unknowns
- Keep the tone direct and human
- Do not include irrelevant personal information
- Do not send anything or update any system
- When evidence is missing, write Unknown
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/02-post-call-follow-up.md)**  
Also: [Prompt](../templates/post-call-follow-up-prompt.md) · [Skills: extract evidence](../.agents/skills/extract-post-call-evidence/SKILL.md) · [draft the email](../.agents/skills/draft-follow-up-email/SKILL.md) · [Worked example](../examples/hartwell-post-call-output.md)

## The AI cannot decide

- Whether a suggestion the prospect made was actually an agreement
- What tone genuinely sounds like you
- Whether a CRM field should really change

## You must check

- Every important statement is supported by the call
- Estimates are clearly labelled as estimates
- No meeting or next step has been invented
- The email sounds like you

## Then

Send the email once you have checked it, and approve any CRM changes yourself; nothing here sends or updates anything on its own.

---

Want the fuller method, the check-before-you-send list, or the cross-model comparison? Open the [workflow](../workflows/02-post-call-follow-up.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
