# Composing Longer Workflows

As workflows here start to chain together, [pre-call prep](../recipes/prepare-for-a-sales-call.md) feeding [post-call evidence and follow-up](what-is-a-sales-ai-skill.md), evidence feeding a business case, a business case feeding a champion's package, a few structural questions come up regardless of which specific sales problem is being solved. Where does the material a run produces actually live. How does a person see where a longer run has got to. When does spending real money on enrichment need a checkpoint before it continues. How much should connect to a specific platform versus stay a manual, paste-it-in route. Whose job is judgement, and whose is mechanics.

These are documented here as principles to build to, not as new software. Nothing in this repository executes automatically today: every workflow is a set of instructions a person runs, in a chat, on material they gathered themselves. [Workflow Router](workflow-router.md) and [Skill Handoff Contracts](skill-handoff-contracts.md) are the two pieces of this already shipped. The rest below is what should hold true if any of this becomes a more integrated tool later, so that a future build gets these decisions right from the start rather than retrofitting them once something less careful is already working.

## Keep a Working Folder and a Run Log

For a workflow that produces more than one piece of intermediate material worth keeping, evidence extracted, a draft, a revised draft, a simple separation helps more than it costs:

```text
input/
intermediate/
output/
run-log.md
```

The run log should record what was used, what was produced, what was skipped and why, any correction made along the way, and which actions were actually completed versus only proposed. This is a discipline for a longer, multi-step run to follow, whether that run happens by hand today or through a more integrated tool later; it is not a folder structure this repository currently creates for you.

## Show Where a Run Has Reached

For a longer task, a person should be able to see where the work has got to, not just wait for a final answer:

```text
Sources loaded
Evidence extracted
Conflicts found
Draft produced
Human review required
```

A future integrated tool built around these workflows should let a person stop, retry, or replace the instructions being used before an external action happens, not only after. A failed run should leave enough behind to understand what actually happened, rather than presenting a partial result as though it completed cleanly.

## Add a Checkpoint Before Spending Money

Where a workflow might use a paid enrichment, research, or automation tool, add an explicit review point before the next round of spend or the next external action, rather than letting a pipeline run end to end unattended:

```text
collect
review quality
filter
review again
enrich
human approval
act
```

Each review step is a real pause, not a formality; the point is catching a bad list, a wrong signal, or a low-quality source before it costs more to enrich or before it reaches a prospect.

## Keep a Manual Route

Every integrated workflow should keep a manual route that works from pasted or uploaded material, with any platform connector as an optional accelerator, not a requirement. State the connector's limitations and its fallback plainly rather than assuming it always behaves the same way the manual route does. Someone without access to a particular CRM or enrichment tool should still be able to run the underlying workflow by hand.

## Choose Method Before Platform

Decide the sales method first, then find or build the platform adapter that implements it. A platform adapter's job is to carry out a method that is already understood; it should not become the source of that method just because the platform happens to expose a convenient API or connector. If a tool's own defaults start quietly reshaping how a workflow here actually works, that is a sign the platform has taken over a decision that belonged to the method.

## Separate Judgement from Mechanics

Keep the AI responsible for the things only judgement can do: classification, drafting, and identifying a gap in the evidence. Keep code or automation responsible for repeatable mechanics: file handling, scheduling, and API calls. Do not automate a workflow until its manual version has actually proven stable and its failure conditions are understood; automating something before that just repeats an unstable process faster.

## Keep Instructions Visible Even When Configurable

Provide a safe default instruction for each workflow, and let a user inspect and adapt it, rather than hiding what actually produced a given result. Record when a custom instruction was used instead of the default. Never hide the instruction behind a recommendation, a score, or a customer-facing draft; if the wording changed, the person reading the output should be able to see what changed and why.

## What This Is Not

This is a set of principles for extending these workflows into something more integrated later, not a description of software that exists here now. Nothing in this repository schedules a run, spends money automatically, or executes a workflow without a person present at every step already required by [RESPONSIBLE-USE.md](../RESPONSIBLE-USE.md) and each individual skill's own guardrails. The value of writing these down now, before any of it is built, is that a future build has somewhere to check its own decisions against, rather than working them out for the first time under the pressure of a platform that already exists.
