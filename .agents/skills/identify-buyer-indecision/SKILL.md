---
name: identify-buyer-indecision
description: Diagnose whether a late-stage buyer's delay is genuine indecision, a fear of making the wrong call, rather than an ordinary objection, missing information, a timing issue, an approval dependency, a reduced business rationale, a soft no, or a genuine disqualification. Use when a positive, unblocked buyer keeps deferring the final decision with no specific stated concern. Do not use this to draft the customer-facing reply; use the buyer indecision workflow's prompt for that once the diagnosis is confirmed.
---

# Identify Buyer Indecision

> Landed here directly rather than clicking through from a guide? This file is the instruction sheet an AI assistant follows, not written for a first read start to finish. [What is a sales AI skill?](../../../guides/what-is-a-sales-ai-skill.md) has the plain-English version.

## Purpose

Distinguish genuine late-stage fear of making the wrong decision from an ordinary objection, missing information, a timing issue, an approval dependency, a reduced business rationale, a soft no, or a genuine disqualification.

## Inputs Required

- Transcript, call notes, or email threads.
- Current CRM context (stage, stakeholders, timeline).

## Core Directives

1. **Isolate the Driver.** Do not accept "we need to think about it" at face value. Drill down to find the specific risk the buyer fears.
2. **Reduce Risk, Don't Push.** If it is genuine indecision, the goal is to make the decision feel safer, not to apply pressure.
3. **Separate Fact from Inference.** Clearly label what the buyer explicitly said versus what you are inferring from their tone or context.
4. **No Invented Commercials.** Never invent pilots, discounts, contract flexibility, or implementation promises to soothe the buyer.

## Execution

Load [the output contract](references/output-contract.md) for strict behavioural boundaries.
Use [the output template](templates/output-template.md) to format your final analysis.
Run [the human review checklist](checks/checklist.md) before anything from this analysis is acted on.

This skill diagnoses only. For drafting the actual customer-facing response once genuine indecision is confirmed, use the [buyer indecision workflow](../../../workflows/07-buyer-indecision.md) and its [prompt template](../../../templates/buyer-indecision-prompt.md).

Read [the fictional example](references/fictional-example.md) for a test.
