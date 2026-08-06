---
name: opportunity-handover
description: Prepare an evidence-led handover when a live opportunity or account moves from one salesperson to another salesperson, a delivery or account management team, or another operational owner, so the receiving person understands the real position rather than an optimistic summary. Use when ownership is genuinely changing and the new owner needs to get up to speed quickly and accurately. Do not use this for ordinary post-call follow-up where the same person keeps the opportunity; use the extract-post-call-evidence and draft-follow-up-email skills for that. Do not use this for a routine pipeline review where nobody's ownership is changing; use the pipeline-evidence-review skill for that.
---

# Opportunity Handover

> Landed here directly rather than clicking through from a guide? This file is the instruction sheet an AI assistant follows, not written for a first read start to finish. [What is a sales AI skill?](../../../guides/what-is-a-sales-ai-skill.md) has the plain-English version.

You do not need to install anything to try this once. The lines between the dashes at the very top are just this file's label; leave them in. On GitHub, copy this using the **Raw** button near the top of the page rather than selecting the rendered text, so the tables and links below paste in cleanly. Send the whole file as your first message in any AI chat tool, then follow it with your actual inputs.

A handover is where a deal's real position most often gets rounded up: a possible next step reads as an agreed plan, a stalled approval reads as basically confirmed, or a contact who has just been replaced still gets listed as the person to speak to. This skill exists to carry the evidence across intact, not a tidier version of it.

## Gather the Inputs

- Recent call notes, transcripts, CRM history including stage history, and relevant emails, from approved sources only
- Who is receiving the handover, in what role, and why the opportunity or account is moving to them now
- Confirmed people involved, including whether anyone's role or involvement has changed since the earlier evidence was recorded
- The date of each source, or its position relative to the others, since a handover evaluates the current position, not just the available content

## Confirm the Handover Before Building It

If the recipient or the reason for the handover is not known, stop and ask rather than guessing who this is for or writing generic content that could suit anyone.

## Weigh the Sources and Show Disagreement

Use the source order already set out in [the methodology](../../../METHODOLOGY.md), direct customer statements first, then agreed actions and dates, then CRM stage history, then email, then meeting notes, then public information, then AI interpretation. A handover does not get its own separate hierarchy. Record the date or relative position of each important source, since the point of a handover is showing the newest reliable position, not the most complete-sounding one. When sources disagree, for example a CRM stage that reads further along than the emails support, show the disagreement in the output rather than quietly picking one.

## Separate Facts From Judgement

Label every important point as confirmed, a customer estimate, a reasonable inference that still needs checking, unknown, or conflicting where reliable sources disagree and nothing resolves it. Keep these separate in the output rather than blending them into one confident paragraph.

## Preserve Commitments, Dates and Ownership

Preserve conditional wording exactly (subject to approval, if agreed) and keep relative and absolute dates as they were given rather than converting a discussed date into a booked one. Treat a change of contact or receiving owner on the customer side as itself something to report, not something to update quietly in the background. Distinguish what the customer has actually said they want from any AI-generated suggestion about what to do next; a suggested project or next step stays provisional until the receiving person and the customer have actually accepted it, not from the moment it is written down.

Give every action exactly one accountable owner, never a compound name or an external party alone. When the party who must actually act is external, uncertain, or not yet assigned, name the internal person responsible for chasing it, not "the customer" or "unassigned" by itself. A handover that leaves an action without one clear internal owner has not actually handed it over.

## Keep Only What the Next Person Needs

Include personal information only where it helps the receiving person carry on the relationship: confirmed roles, stated preferences, agreed involvement. Leave out anything that does not serve continuity.

## Apply the Guardrails

- Never invent customer intent, urgency, authority, budget, dates or commitments that were not actually given.
- Never describe an opportunity as qualified while a material condition, budget, authority, timeline or procurement, remains open.
- Never treat an internal suggestion, or a possible next step, as something the customer has agreed to.
- Never resolve a material conflict between sources by silently picking one; show it.
- Never describe an external action, a message sent, a CRM record changed, ownership transferred, as completed unless the evidence actually confirms it.
- Never invent a person's gender, pronouns or other personal characteristics. If the evidence does not state someone's pronouns, use their name or neutral wording instead of guessing from a name, role or surrounding text, and never carry one person's stated pronouns over to someone else.

Load [the output contract](references/output-contract.md) for the full list of what this skill must and must not do, including the sending, drafting and system-change restrictions. Use [the output template](templates/output-template.md) to format the finished handover. Run [the human review checklist](checks/checklist.md) before the receiving person accepts ownership.

## Stop When the Task Is Unsafe

Do not produce a handover when:

- The recipient or the reason for the handover is not known
- There is not enough evidence to establish the current position with any confidence
- An unresolved conflict between sources materially changes what was actually promised or agreed
- It cannot be confirmed that the information being used is approved for the chosen AI tool
- The request depends on exposing confidential information the receiving person does not need for continuity

Explain the limitation and ask for the minimum missing detail rather than filling the gap with a plausible guess.

## Require Human Review

This produces a draft handover, not a completed one. The salesperson preparing it must check every claim against the actual sources, and the receiving person must accept ownership before it is treated as complete. Sending anything, changing CRM ownership or system records, and creating any task or calendar event, stay outside this skill; a person does all of that directly.

For a fictional test, read [the Hartwell example](references/hartwell-example.md).
