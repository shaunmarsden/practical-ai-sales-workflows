---
name: crm-hygiene-review
description: Audit a CRM export for duplicates, missing fields, records that are not real prospects at all, stale records, and close dates that do not fit their stage, without judging why any specific deal has stalled. Use when you want to trust a CRM export before using it for a total, a review, or a report, or when duplicates, gaps or stale records are suspected. Do not use this to judge whether a deal is still alive or genuinely stalled; use the pipeline-evidence-review skill for that.
---

# CRM Hygiene Review

> Landed here directly rather than clicking through from a guide? This file is the instruction sheet an AI assistant follows, not written for a first read start to finish. [What is a sales AI skill?](../../../guides/what-is-a-sales-ai-skill.md) has the plain-English version.

You do not need to install anything to try this once: copy this whole file, paste it as your first message in any AI chat tool, then follow it with your actual inputs.

This audits the structural problems that quietly make a CRM export unreliable, duplicates, missing fields, stale records, and dates that do not fit the stage, without touching anything or judging why a specific deal has stalled.

## Gather the Inputs

A CRM export or list covering the records to check: company, contact, owner, stage, value, close date, last activity. The more fields provided, the more this can actually check.

## Scan Every Record for Structural Gaps

Work through the export field by field, not deal by deal. Look for what is missing (a blank owner, contact, value, stage or close date) and what is inconsistent (a close date far too soon for an early stage, a company appearing more than once).

## Flag Records That Are Not Real Prospects At All

Some records are not an incomplete prospect; they are not a prospect at all, a test entry, a practice run, an internal course or demo left behind in the live pipeline. This is different from a missing field (a real prospect with a gap) and from a duplicate (the same real prospect twice). A deal name that reads like a course title, a project name, or an obvious placeholder, especially paired with no stage and no pipeline, is the signal to look for. Flag it separately, and suggest archiving or deleting it rather than treating it as a prospect that merely needs its fields filled in.

## Separate Confident Findings From Uncertain Ones

A duplicate with a shared contact name at what reads as the same company, entered under two slightly different names, is a confident finding. A similar-sounding company name with no other shared detail is not; it needs a human to confirm before anything is merged. Keep these visibly separate, and never merge on name similarity alone.

## Identify Staleness Properly

A record can look unhealthy because every field is blank, or it can look healthy because every field is filled in while quietly being months overdue with no recent activity. Check both. Do not assume a complete-looking record is a current one. State any threshold used to call something stale as illustrative, not a universal rule.

## Stay Out of the Stage-Accuracy Question

Flag a close date that has passed, or that does not fit the stage, as a structural fact. Do not judge whether the underlying deal is paused, blocked or genuinely dead; that requires more evidence than a CRM export alone provides. Point to the pipeline-evidence-review skill for that judgement once enough evidence exists.

## Apply the Guardrails

- Every finding is a suggestion. Merging duplicates, filling in a missing field, archiving a non-prospect record, or reassigning an owner all stay with a person; nothing is merged, deleted or changed here.
- Keep confident and uncertain duplicate findings visibly separate at all times.
- Never diagnose why a specific deal has stalled or whether it is still alive; only flag that a date or field is structurally unsupported.
- Where a record has every field present, a realistic close date for its stage, and recent activity, say so. A review that finds a problem on every record will not be trusted on the ones that genuinely have one.

## Stop When the Task Is Unsafe

Do not produce a review when:

- The export is missing enough fields (stage, close date, last activity) that duplicates or staleness cannot actually be judged
- The request is to merge, delete, or update records directly rather than flag them for a person to action
- The request is to use this review's output to diagnose why a specific deal has stalled, rather than only its structural hygiene

## Require Human Review

This flags issues; it does not act on them. Confirm any suggested duplicate with the actual record owners before merging anything, and make every field correction and CRM change directly.

Read the [fictional CRM export](../../../examples/fictional-crm-export.md) and [completed review](../../../examples/fictional-crm-hygiene-review.md) for a worked test, and the [honest evaluation](../../../evaluations/fictional-crm-hygiene-review-eval.md) for how it scored.
