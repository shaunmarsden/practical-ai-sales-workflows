# Workflow Router

New here? Start with [Where to Start](where-to-start.md) or [What Is a Sales AI Skill?](what-is-a-sales-ai-skill.md).

There are seventeen routes here: fifteen workflows and two jobs that exist only as a skill. A real situation rarely arrives labelled with the right one. The [workflow router skill](../.agents/skills/workflow-router/SKILL.md) reads a plain-English description of what's going on and hands off to the route that fits. It doesn't try to do the task itself. Not using an AI agent? [The portable prompt](../templates/workflow-router-prompt.md) does the same job pasted straight into ChatGPT, Claude or Gemini.

## When to Use It

Use it when you're not sure which of the seventeen routes applies, or when two sound alike and it matters which one is right. If you already know the job, [Choose a Sales Problem](../README.md#-choose-a-sales-problem) or the [recipe cards](../recipes/README.md) get you there faster.

## A Worked Example

**What was described:** "A prospect I've been talking to for weeks keeps agreeing everything sounds good, but won't actually sign. Every time we speak there's a new small thing, this week it's wanting to loop in someone from finance, last week it was wanting to wait until after a conference. Nothing feels like a real objection, they just won't commit."

**The clean handoff:**

- Objective: work out why this deal isn't closing and get it moving.
- Evidence currently available: soft, shifting reasons for delay across several conversations, and no single stated concern about the offer itself.
- Important missing information: whether "looping in finance" is a real approval step (something the deal truly depends on) or another soft delay. This needs a direct question, not an assumption either way.
- Recommended workflow and skill: [Move a Stalled Decision](../workflows/07-buyer-indecision.md).
- Why this route fits: nobody has raised a specific concern you could answer, the reasons keep changing rather than repeating, and the buyer sounds positive throughout. That's the pattern buyer indecision is for. Objection handling needs one concrete thing to answer.
- What buyer indecision may produce: a check on whether this is real indecision rather than a hidden approval step, and if it is, a reply that makes deciding feel less risky rather than pushing harder.
- What still requires a person: confirming whether the finance mention is something the deal depends on before treating this as pure indecision, and deciding what to send.

This tests the very confusion the router's own guardrails warn about. The phrase "won't commit" could read as an unstated objection, but nobody has raised anything specific, and that's what separates buyer indecision from objection handling. If the finance mention turns out to be a real, confirmed approval step rather than a soft delay, the right route changes. The router should say so rather than forcing the first answer that seems to fit.

## What This Does Not Do

The router doesn't draft the follow-up, diagnose the objection or build the business case. It hands off to the workflow or skill that does, with enough context that the next step doesn't start from nothing. If none of the seventeen routes fits what you described, it says so and points to the [missing-workflow request template](../.github/ISSUE_TEMPLATE/missing-workflow.yml), rather than forcing a route that doesn't belong.
