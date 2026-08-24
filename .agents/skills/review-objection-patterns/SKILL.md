---
name: review-objection-patterns
description: Review objections across several sales deals and separate genuine repeated drivers from similar wording that hides different causes. Use when a sales manager, account executive or revenue operations team wants to learn from an objection log, decide whether a recurring issue deserves a prepared response or playbook item, or check whether a supposed pattern is actually supported. Do not use for answering one live objection; use the objection response skill instead.
---

# Review Objection Patterns

> Landed here directly rather than clicking through from a guide? This file is the instruction sheet an AI assistant follows, not written for a first read start to finish. [What is a sales AI skill?](../../../guides/what-is-a-sales-ai-skill.md) has the plain-English version.

You do not need to install anything to try this once. The lines between the dashes at the very top are just this file's label; leave them in. On GitHub, copy this using the **Raw** button near the top of the page rather than selecting the rendered text, so the tables and links below paste in cleanly. Send the whole file as your first message in any AI chat tool, then follow it with your actual inputs.

Find what genuinely recurs across deals without turning a repeated phrase into a made-up root cause.

## Gather the Inputs

Use a log containing:

- a deal or company identifier;
- the objection's exact wording;
- stage and speaker role;
- the diagnosed driver and the evidence for it, if known;
- the response and outcome; and
- the period and source covered by the log.

Keep repeated objections from one deal as separate occurrences but only one distinct deal. If deal identity is unclear, say so before counting.

## Check the Log Before Finding Patterns

State what is missing, inconsistent or too vague. A diagnosed driver is evidence only when the log explains how it was established. If the log records wording but not the driver, label the driver unknown rather than inferring it confidently.

Do not treat a hand-picked log as representative of the whole pipeline without evidence that it is.

## Build Candidate Groups

Group the log twice:

1. by similar wording or topic;
2. by the underlying driver recorded in the evidence.

Compare the two views. Similar words with different drivers are a misleading surface pattern. Different words with the same driver may be a genuine pattern.

Count both occurrences and distinct deals. Do not let two objections from one deal look like two independent examples.

## Judge Each Pattern

For every candidate, show:

- the entries supporting it;
- evidence that the driver is the same or different;
- evidence against the pattern;
- confidence specific to that finding; and
- whether the evidence justifies a human action, more logging or no action.

Use low, medium or high confidence and explain the choice. Do not apply a fixed numerical threshold. Sample size, distinct deals, source quality and consistency of the driver all matter.

## Produce the Review

Use this order:

1. input quality and limitations;
2. a summary table with occurrences, distinct deals, driver consistency, confidence and action status;
3. genuine patterns;
4. misleading surface patterns;
5. isolated signals that are not patterns yet;
6. suggested actions for human approval; and
7. what the sample cannot tell you.

Follow the [Writing Style and Formatting guide](../../../guides/writing-style-and-formatting.md). Keep titles free of hyphens, do not use em dashes and do not use bold labels followed by colons inside bullet lists. Before returning, scan every heading and rewrite any hyphenated compound, such as "Financial-Year" to "Financial Year".

## Apply the Guardrails

- Never report a percentage, win rate or loss rate from a small or mixed sample.
- Never merge different drivers because the wording shares a product, competitor or price term.
- Never split the same driver merely because people described it differently.
- Treat outcomes as supporting context, not proof of why a deal progressed or failed.
- Do not present a product, pricing, enablement or playbook change as decided.
- Do not change a CRM, playbook or customer message.
- Exclude unnecessary personal or confidential information.

## Stop When the Evidence Is Too Thin

If fewer than two distinct deals support a candidate, call it an isolated signal. If the driver is unknown across most entries, report the missing diagnosis work instead of inventing patterns. If duplicate deal identity cannot be resolved, show ranges rather than a false exact count.

## Require Human Review

A person checks the diagnoses, decides whether a finding is commercially meaningful and approves any response, playbook or process change.

Read the [first fictional log](../../../examples/fictional-objection-pattern-log.md), the [harder second log](../../../examples/fictional-objection-pattern-log-two.md), its [skill output](../../../examples/fictional-objection-pattern-review-two.md) and the [second evaluation](../../../evaluations/fictional-objection-pattern-second-eval.md) for worked tests. A [third log](../../../examples/fictional-objection-pattern-log-three.md) tests two decoy entries that share the surface shape of the genuine pattern, someone else's input being needed, but not its actual driver; see its [skill output](../../../examples/fictional-objection-pattern-review-three.md) and [evaluation](../../../evaluations/fictional-objection-pattern-third-eval.md). A [fourth log](../../../examples/fictional-objection-pattern-log-four.md) inverts the trap: two entries with opposite-looking behaviour share the same driver, at the smallest sample size this skill's own rules treat as a candidate; see its [skill output](../../../examples/fictional-objection-pattern-review-four.md) and [evaluation](../../../evaluations/fictional-objection-pattern-fourth-eval.md).
