# 🧹 Recipe: Keep Your CRM Honest

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Auditing a CRM export for the structural problems that quietly make it unreliable: duplicates, missing fields, stale records and dates that do not fit the stage, without touching anything or judging why a specific deal has stalled.

## You need

A CRM export or list covering the records you want checked: company, contact, owner, stage, value, close date, last activity.

## You'll get

Likely and possible duplicates kept clearly separate, records missing critical fields, stale records, and dates that do not fit their stage, all flagged for a person to act on.

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/crm-hygiene-review-prompt.md -->
```text
Act as a careful, honest CRM hygiene reviewer.

Use only the information I provide. Do not merge, delete or change any record; this review is read-only and every suggested action is for me to approve and make myself.

Work through the export and check for:

1. Duplicates
Flag likely duplicates (same or near-identical company, a shared contact name, entered under slightly different names) separately from possible duplicates (a similar-sounding name with no other shared detail). State a confidence level for each. Never suggest merging on name similarity alone; possible duplicates need a human check first.

2. Missing critical fields
Flag any record missing a value, a stage, an owner, a contact, or a close date.

3. Records that are not real prospects at all
Flag a record that reads like a test entry, a practice run, an internal course or demo, rather than a real prospect, such as a deal name that looks like a course title or an obvious placeholder, especially with no stage and no pipeline. Keep this separate from a real prospect that is merely missing a field, and suggest archiving or deleting it rather than filling it in.

4. Stale records
Flag records with no recent activity relative to today's date, including ones where every field looks complete but the close date has passed and nothing has moved in a long time. State the threshold you used to call something stale, and note that it is illustrative, not a fixed rule.

5. Close dates that do not fit the stage
Flag a close date that is unrealistic for how early or late the recorded stage is, such as an imminent date on a deal still in early discovery.

6. What has no issue
Say plainly which records have every field present, a realistic close date for their stage, and recent activity, so this does not read as a list of only problems.

Finish with a short summary table of issue types and how many records carry each one.

Rules:
- Do not merge, delete or update any CRM record
- Do not diagnose why a specific deal has stalled or whether it is still alive; only flag that a date or field is structurally unsupported. Point to a pipeline evidence review for that judgement instead.
- Keep confident and uncertain duplicate findings visibly separate
- State any threshold used (such as what counts as stale) as illustrative, not universal
- Call out genuinely clean records, not only problems
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/08-crm-hygiene-review.md)**  
Also: [Prompt](../templates/crm-hygiene-review-prompt.md) · [Worked example](../examples/fictional-crm-hygiene-review.md)

## The AI cannot decide

- Whether two similar-looking records are actually the same company
- Whether a record that looks complete is genuinely current rather than stale

## You must check

- Every likely duplicate is confident, based on more than a similar-sounding name
- Possible duplicates are kept separate and flagged for your check, not merged
- The review stops at flagging a date, not diagnosing why the deal stalled

## Then

Confirm any suggested duplicate yourself before merging, and make every field correction and CRM change directly; nothing here merges, deletes or changes a record on its own.

---

Want the fuller method or where this stops and the pipeline evidence review starts? Open the [workflow](../workflows/08-crm-hygiene-review.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
