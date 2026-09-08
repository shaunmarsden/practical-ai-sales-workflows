# 🤲 Recipe: Hand Over an Opportunity

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Passing an opportunity to another person, team or stage without losing useful context or making the deal sound further along than it actually is.

## You need

Recent call evidence, CRM notes, relevant emails and agreed actions.

## You'll get

A short handover, covering:

- A 30-second brief
- The current position
- People involved and their confirmed roles
- Evidence kept separate from assumptions
- A recommended next action

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/opportunity-handover-prompt.md -->
```text
Act as a careful sales opportunity handover assistant.

Use only the information I provide. Do not use outside knowledge or invent customer needs, urgency, authority, budgets, dates, commitments, meetings, stages or next steps.

Create a handover that another salesperson can understand quickly.

Produce the following sections:

1. 30 second brief
Write no more than four bullets covering the opportunity, current position, most important caution and immediate next action.

2. Opportunity at a glance
Show the company, main contact, current position, business problem, desired outcome and recommended next action. Use Unknown where the evidence is missing.

3. People involved
List each person, their confirmed role, their involvement and anything still uncertain. Do not treat a possible stakeholder as a decision maker.

4. Confirmed evidence
List only information directly supported by the supplied sources. Add a short source label to each important point.

5. Estimates, assumptions and unknowns
Keep these in three separate groups. Preserve uncertainty and conditions.

6. Actions and commitments
Use a table with Owner, Action, Timing, Status and Evidence. Do not treat a suggestion or conditional statement as an agreement.

7. Risks and cautions
List anything that could cause the receiving person to overstate the opportunity, miss an action or use information incorrectly.

8. Recommended next action
Suggest one action supported by the evidence. State what must be checked first and who currently owns it.

9. Useful sources
List the source names or links that the receiving person should keep. Do not claim to have opened or verified a link unless its contents were provided.

10. Handover check
List the three most important questions the receiving person should ask before accepting ownership.

Rules:

- Put the current position and next action first
- Separate confirmed facts, estimates, assumptions and unknowns
- Preserve conditional wording and relative timing
- Keep tentative stakeholders tentative
- Do not include irrelevant personal information
- Do not send messages, change ownership or update any system
- When evidence is missing, write Unknown
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/03-opportunity-handover.md)**  
Also: [Prompt](../templates/opportunity-handover-prompt.md) · [Skill](../.agents/skills/opportunity-handover/SKILL.md) · [Worked example](../examples/hartwell-opportunity-handover.md) · [Real-use finding](../evaluations/opportunity-handover-real-use-finding.md)

## The AI cannot decide

- Whether a stakeholder's interest is as firm as it reads in the notes
- What the receiving person still genuinely needs to check before taking this on

## You must check

- Someone could understand the current position in 30 seconds
- Every important claim traces to a source
- Tentative stakeholders are still described as tentative, not upgraded

## Then

Talk it through with the receiving person, confirm they have accepted ownership of the next action, and correct any gaps together before it is treated as complete.

---

Want the fuller method or what a complete handover should actually contain? Open the [workflow](../workflows/03-opportunity-handover.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
