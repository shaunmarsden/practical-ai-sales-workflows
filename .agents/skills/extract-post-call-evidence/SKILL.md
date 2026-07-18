---
name: extract-post-call-evidence
description: Analyse B2B sales call transcripts or notes to extract confirmed facts, estimates, commitments, stakeholders, concerns, unknowns and suggested next actions while separating evidence from inference. Use when reviewing a sales call, preparing CRM ready findings, identifying actions or qualification gaps, or creating reliable inputs for follow up. Do not use merely to write a finished follow up email.
---

# Extract Post Call Evidence

> Landed here directly rather than clicking through from a guide? This file is the instruction sheet an AI assistant follows, not written for a first read start to finish. [What is a sales AI skill?](../../../guides/what-is-a-sales-ai-skill.md) has the plain-English version.

Turn a sales transcript or clear notes into a reliable evidence pack for human review. Preserve uncertainty and avoid turning plausible interpretations into facts.

## Gather the Inputs

List the material supplied before analysing it. Inputs may include:

- Current call transcript or notes
- Current email correspondence
- Existing CRM record
- Earlier meeting notes
- Relevant public company information

Use only information needed for the sales task. Exclude unrelated personal information and material the user is not permitted to process.

## Follow the Source Order

Use this order when sources differ:

1. Direct statements from the current call
2. Written commitments in current email correspondence
3. Existing CRM records, treated as potentially stale
4. Earlier notes
5. Public information, treated as context rather than proof of an internal problem

Surface conflicts instead of silently choosing the most convenient version.

## Classify the Evidence

Use these labels consistently:

- `confirmed`: directly supported by a supplied source
- `estimate`: a number or view explicitly presented as approximate
- `second_hand`: reported by someone who is not the original source
- `inference`: a reasonable interpretation that still needs testing
- `unknown`: important information not established by the sources
- `conflict`: two supplied sources disagree

Do not upgrade an estimate, second hand comment or inference into a confirmed fact.

## Extract the Findings

1. Identify confirmed facts and estimates.
2. Capture customer problems and desired outcomes in the customer's language.
3. Record stakeholders and distinguish confirmed roles from assumed influence.
4. Separate buying signals from polite interest.
5. Capture concerns and objections without guessing what sits behind them.
6. Record each commitment with owner, action, timing, conditions and evidence.
7. Identify missing qualification and contradictions.
8. Propose one sensible next action based on the evidence available.
9. Prepare a concise CRM summary for review.

Read [the output schema](references/output-schema.md) before producing the final answer.

## Apply the Guardrails

- Never invent a meeting, deadline, budget, authority, urgency or commitment.
- Preserve conditional language such as "should", "subject to approval" and "I need to check".
- Do not treat a discussed next step as agreed unless the evidence shows agreement.
- Do not use a public company initiative as proof of an internal need.
- Mark CRM information as potentially stale when current evidence differs.
- State when the available evidence is insufficient.
- Recommend actions, but do not send messages or alter CRM data.

## Stop When the Task Is Unsafe

Do not manufacture a complete analysis when:

- No usable call evidence is supplied
- The transcript is too incomplete for the requested conclusion
- The user asks to fabricate evidence
- The output would expose unnecessary confidential or personal information
- The user asks to present an unsupported interpretation as confirmed

Explain the limitation and request only the minimum additional information needed.

## Require Human Review

End with the points a salesperson must check before using the output. Keep emails, CRM changes, meeting bookings and other external actions subject to explicit human approval.

For a fictional test, read [the Northstar example](references/northstar-example.md).
