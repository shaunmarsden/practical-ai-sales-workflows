# CRM Hygiene Review Prompt

Copy the prompt below, then paste in your CRM export or a list of records with whatever fields you have: company, contact, owner, stage, value, close date, last activity. The more fields you include, the more this can actually check.

```text
Act as a careful, honest CRM hygiene reviewer.

Use only the information I provide. Do not merge, delete or change any record; this review is read-only and every suggested action is for me to approve and make myself.

Work through the export and check for:

1. Duplicates
Flag likely duplicates (same or near-identical company, a shared contact name, entered under slightly different names) separately from possible duplicates (a similar-sounding name with no other shared detail). State a confidence level for each. Never suggest merging on name similarity alone; possible duplicates need a human check first.

2. Missing critical fields
Flag any record missing a value, a stage, an owner, a contact, or a close date.

3. Stale records
Flag records with no recent activity relative to today's date, including ones where every field looks complete but the close date has passed and nothing has moved in a long time. State the threshold you used to call something stale, and note that it is illustrative, not a fixed rule.

4. Close dates that do not fit the stage
Flag a close date that is unrealistic for how early or late the recorded stage is, such as an imminent date on a deal still in early discovery.

5. What has no issue
Say plainly which records have every field present, a realistic close date for their stage, and recent activity, so this does not read as a list of only problems.

Finish with a short summary table of issue types and how many records carry each one.

Rules:
- Do not merge, delete or update any CRM record
- Do not diagnose why a specific deal has stalled or whether it is still alive; only flag that a date or field is structurally unsupported. Point to a pipeline evidence review for that judgement instead.
- Keep confident and uncertain duplicate findings visibly separate
- State any threshold used (such as what counts as stale) as illustrative, not universal
- Call out genuinely clean records, not only problems
```

## Before You Use the Output

- Confirm any suggested duplicate with the actual record owners before merging anything; do not merge on the AI's confidence alone
- Make every field correction and every CRM change yourself
- Decide your own team's actual staleness threshold rather than accepting the one used in the output
- If a record's stage looks wrong given the evidence, not just the dates, use the [pipeline evidence review](../workflows/06-pipeline-evidence-review.md) instead; this prompt does not do that judgement
