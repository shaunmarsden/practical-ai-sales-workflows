# Composing Longer Workflows

Workflows here are starting to chain together. [Pre-call prep](../recipes/prepare-for-a-sales-call.md) feeds [post-call evidence and follow-up](../recipes/follow-up-after-a-sales-call.md), evidence feeds a business case, and a business case feeds a champion's package. Whatever the sales problem, the same few questions come up:

- Where does the material a run produces live?
- How does a person see where a longer run has got to?
- When does spending real money on enrichment need a checkpoint before it goes on?
- How much should connect to a platform, and how much should stay a manual, paste-it-in route?
- Whose job is judgement, and whose is mechanics?

I've written these down as rules to build to, not as new software. Nothing here runs by itself today. Every workflow is a set of instructions a person runs, in a chat, on material they gathered. Two pieces already exist: the [Workflow Router](workflow-router.md) and [Skill Handoff Contracts](skill-handoff-contracts.md). [Build an Approval-Gated Sales Copilot](build-an-approval-gated-sales-copilot.md) is a first example that covers some of the rest, mainly a manual route and approval gates. It doesn't yet keep a working folder, a run log or a spending checkpoint.

The rest of this page is what should hold if any of this becomes a more joined-up tool later. That way a future build gets these decisions right from the start, rather than bolting them on once something less careful is already working.

## Keep a Working Folder and a Run Log

Some workflows produce more than one piece of material worth keeping along the way: extracted evidence, a draft, a revised draft. For those, a simple split helps more than it costs:

```text
input/
intermediate/
output/
run-log.md
```

The run log should record what was used, what was produced, what was skipped and why, any correction made on the way, and which actions were done rather than only proposed. It's a habit for any longer run, whether by hand today or through a tool later. This repository doesn't create the folders for you.

## Show Where a Run Has Reached

In a longer task, a person should be able to see where the work has got to, not just wait for the final answer:

```text
Sources loaded
Evidence extracted
Conflicts found
Draft produced
Human review required
```

A future tool built on these workflows should let a person stop, retry or change the instructions before an outside action happens, not only after. A failed run should leave enough behind to show what happened. It shouldn't present a partial result as if it finished cleanly.

## Add a Checkpoint Before Spending Money

If a workflow might use a paid enrichment, research or automation tool, add a review point before the next round of spending or the next outside action. Don't let the whole thing run unattended:

```text
collect
review quality
filter
review again
enrich
human approval
act
```

Each review is a real pause, not a formality. The point is to catch a bad list, a wrong signal or a poor source before it costs more to enrich or reaches a prospect.

## Keep a Manual Route

Every joined-up workflow should keep a manual route that works from pasted or uploaded material. A platform connector should make it quicker, not be required. Say plainly what the connector can't do and what to fall back on, rather than assuming it always behaves like the manual route. Someone without a particular CRM or enrichment tool should still be able to run the workflow by hand.

## Choose Method Before Platform

Decide the sales method first, then find or build the platform adapter that carries it out. The adapter's job is to carry out a method you already understand. It shouldn't become the source of the method just because the platform offers a handy API or connector. If a tool's defaults start quietly changing how a workflow here works, the platform has taken over a decision that belonged to the method.

## Separate Judgement from Mechanics

Give the AI the things only judgement can do: sorting, drafting, and spotting a gap in the evidence. Give code or automation the repeatable mechanics: handling files, scheduling and API calls. Don't automate a workflow until its manual version has proved stable and you know how it fails. Automating it before then just repeats an unstable process faster.

## Keep Instructions Visible Even When Configurable

Give each workflow a safe default instruction, and let people read and adapt it, rather than hiding what produced a result. Record when someone used a custom instruction instead of the default. Never hide the instruction behind a recommendation, a score or a customer-facing draft. If the wording changed, the person reading the output should be able to see what changed and why.

## What This Is Not

These are rules for turning these workflows into something more joined-up later. They don't describe software that exists here now. Nothing in this repository schedules a run, spends money by itself, or runs a workflow without a person present at every step that [RESPONSIBLE-USE.md](../RESPONSIBLE-USE.md) and each skill's own guardrails already require. Writing them down now, before any of it is built, gives a future build something to check its decisions against. Otherwise it would be working them out for the first time, under pressure from a platform that already exists.
