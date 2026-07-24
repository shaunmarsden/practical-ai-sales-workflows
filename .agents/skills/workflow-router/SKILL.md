---
name: workflow-router
description: Work out which existing workflow or skill in this repository actually fits a described sales situation, and hand off to it cleanly. Use when someone describes a sales job in their own words and is not sure which of the fifteen existing workflows applies, or when two workflows sound similar and it matters which one is actually right. Do not use this to solve the underlying task yourself; it recommends a route, it does not do the work of the workflow it recommends.
---

# Workflow Router

> Landed here directly rather than clicking through from a guide? This file is the instruction sheet an AI assistant follows, not written for a first read start to finish. [What is a sales AI skill?](../../../guides/what-is-a-sales-ai-skill.md) has the plain-English version.

Someone describing a real sales situation rarely names the workflow they need; they describe the problem. This skill reads that description and hands off to the right existing workflow, without trying to solve the task itself and without inventing a new method the fifteen workflows already here do not need.

## Gather the Inputs

- The user's actual goal, in their own words, not a guess at which workflow they mean
- What stage this is at: before a call exists, around a call, mid-deal, or pipeline-wide
- What evidence is actually available (a transcript, an email thread, a CRM export, nothing yet)
- The main blocker or open question, if one is apparent
- Whether this needs the user's own private company context (see [private sales context](../../../context/README.md)) to actually run, or works from the fictional examples alone

## Route to the Right Workflow

Match the described situation against this table. Where two rows sound similar, the distinguishing detail is what actually separates them; check it explicitly rather than picking the first plausible match.

| Situation described | Route to |
| --- | --- |
| Need to find and reach a new prospect, not follow up with someone already talking to you | [Find the Next Prospect](../../../workflows/09-outbound-prospecting.md) |
| Have a call coming up and the useful context is scattered | [Prepare for a Sales Call](../../../workflows/01-pre-call-preparation.md) |
| Just finished a call and need to follow up properly | [Follow Up After a Sales Call](../../../workflows/02-post-call-follow-up.md) |
| A discovery call surfaced more than one team, role or use case, and it matters which parts genuinely fit before building anything around them | [Check Whether It Actually Fits](../../../workflows/13-fit-and-limitations-review.md) |
| A call or notes have established enough detail to justify a tailored document for the decision maker | [Build a Business Case](../../../.agents/skills/build-business-case/SKILL.md) |
| An internal champion has agreed to present or forward your case to a further stakeholder who was not on any call | [Brief Your Champion](../../../workflows/12-champion-enablement.md) |
| A prospect has gone quiet after a follow-up, and enough time has passed to justify a next message | [Chase a Quiet Prospect](../../../.agents/skills/plan-chase-sequence/SKILL.md) |
| A prospect has raised a specific concern, pushback or blocker and you need to respond, not react | [Handle an Objection](../../../workflows/05-objection-handling.md) |
| You keep hearing what sounds like the same objection across several deals and want to know if it is one real pattern | [Spot a Real Objection Pattern](../../../workflows/11-objection-pattern-review.md) |
| A late-stage buyer is positive and unblocked but keeps finding new soft reasons to delay the final yes | [Move a Stalled Decision](../../../workflows/07-buyer-indecision.md) |
| An opportunity is moving to another person, team or stage | [Hand Over an Opportunity](../../../workflows/03-opportunity-handover.md) |
| An opportunity has closed without a sale, or gone quiet long enough to deserve a proper review rather than another chase | [Review a Lost Opportunity](../../../workflows/04-lost-opportunity-review.md) |
| Your pipeline has drifted, or a forecast feels optimistic, and you want an honest read | [Review Your Pipeline](../../../workflows/06-pipeline-evidence-review.md) |
| You want to trust a CRM export before using it for a total or a report | [Keep Your CRM Honest](../../../workflows/08-crm-hygiene-review.md) |
| You want a weekly view of your own patch without building a dashboard | [Get a Weekly View](../../../workflows/10-weekly-operating-review.md) |

### Common Confusions Worth Checking Explicitly

- **Stalled decision versus objection**: a stalled decision has no specific stated concern, just soft delay; an objection names something concrete. If a specific concern exists, route to objection handling even if the person also describes general hesitation.
- **Chase versus lost opportunity review**: chase is for a prospect who has gone quiet after one follow-up; lost opportunity review is for a deal that has closed, or gone quiet long enough that another chase would be the wrong move. If several chases have already gone unanswered, check whether this has actually crossed into lost-opportunity territory rather than defaulting to another chase.
- **Fit and limitations review versus business case**: if more than one team, role or use case is in scope and it is not yet clear which ones genuinely fit, route to the fit review first. Building a business case around a use case that was never going to work is the failure this ordering exists to prevent.
- **None of these fit**: say so plainly rather than forcing the closest match. Point to the [missing-workflow request template](../../../.github/ISSUE_TEMPLATE/missing-workflow.yml) instead of inventing a method on the spot.

## Produce a Clean Handoff

Once a route is chosen, state:

- **The objective**: what the user is actually trying to achieve, in one sentence
- **Evidence currently available**: what has actually been supplied, not what would be nice to have
- **Important missing information**: what the recommended workflow will need that has not been given yet
- **The recommended workflow and skill**: named directly, with a link
- **Why this route fits**: the specific detail that pointed here rather than to a similar-sounding alternative
- **What the next skill may produce**: a short, honest preview, not a promise of the finished result
- **What still requires a person**: carried forward from the recommended workflow's own guardrails, not reset to a blank slate

## Apply the Guardrails

- Never solve the underlying task in place of the workflow being recommended. A router that also does the work stops being a clean handoff and starts guessing at a method the actual workflow already owns.
- Never force a fit when the described situation does not actually match anything in the table. Say so, and suggest the missing-workflow request template instead.
- Never assume private company context is required by default. Most fictional-example and diagnostic workflows work without it; only recommend setting it up when the actual task genuinely needs it.

## Require Human Review

This recommends a route and prepares a handoff. Running the recommended workflow, and everything it in turn requires a person to check, stays exactly as documented in that workflow.

Read [the workflow router guide](../../../guides/workflow-router.md) for a worked example of a handoff, including one that deliberately tests the stalled-decision-versus-objection confusion above.
