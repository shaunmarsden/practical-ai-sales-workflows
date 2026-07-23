# Workflow Router

New to this repository entirely? Start with [Where to Start](where-to-start.md) or [What Is a Sales AI Skill?](what-is-a-sales-ai-skill.md) first.

Fifteen workflows now live here, and a real situation rarely arrives labelled with the right one. The [workflow router skill](../.agents/skills/workflow-router/SKILL.md) reads a plain-English description of what is actually going on and hands off to the workflow that fits, without trying to solve the underlying task itself. Not using an AI agent directly? [The portable prompt](../templates/workflow-router-prompt.md) does the same job pasted straight into ChatGPT, Claude or Gemini.

## When to Use It

Use it when you are not sure which of the fifteen workflows applies, or when two sound similar and it genuinely matters which one is right. If you already know the job you need, [Choose a Sales Problem](../README.md#-choose-a-sales-problem) or the [recipe cards](../recipes/README.md) get you there faster than routing through this first.

## A Worked Example

**What was described:** "A prospect I've been talking to for weeks keeps agreeing everything sounds good, but won't actually sign. Every time we speak there's a new small thing, this week it's wanting to loop in someone from finance, last week it was wanting to wait until after a conference. Nothing feels like a real objection, they just won't commit."

**The clean handoff:**

- **Objective**: work out why this deal is not closing and get it moving.
- **Evidence currently available**: a pattern of soft, shifting reasons for delay across several conversations; no single stated concern about the offer itself.
- **Important missing information**: whether "looping in finance" is a real approval gate (a genuine dependency) or another soft deferral; this needs a direct question, not an assumption either way.
- **Recommended workflow and skill**: [Move a Stalled Decision](../workflows/07-buyer-indecision.md).
- **Why this route fits**: no specific, answerable concern has actually been raised, the reasons keep shifting rather than repeating, and the buyer is described as positive throughout. This is the pattern buyer indecision exists for, not objection handling, which needs one concrete thing to answer.
- **What buyer indecision may produce**: a check on whether this is genuinely indecision rather than an approval gate in disguise, and if so, a response that reduces the risk of deciding rather than pushing harder.
- **What still requires a person**: confirming whether the finance mention is a real dependency before treating this as pure indecision, and deciding what to actually send.

This is a genuine test of the confusion the router's own guardrails call out: "won't commit" reads like it could be an unstated objection, but nothing specific has actually been raised, which is exactly what separates buyer indecision from objection handling. If the finance mention turns out to be a real, confirmed approval gate rather than a soft deferral, the right route changes, and the router should say so rather than forcing the first plausible answer.

## What This Does Not Do

The router does not draft the follow-up, diagnose the objection, or build the business case itself. It hands off to the workflow that does, with enough context that the next step does not start from a blank slate. If nothing in the existing fifteen workflows actually fits what was described, it says so and points to the [missing-workflow request template](../.github/ISSUE_TEMPLATE/missing-workflow.yml) instead of forcing a route that does not belong.
