# CRM Hygiene Review Prompt

Copy the prompt below, then paste in your CRM export or a list of records with whatever fields you have: company, contact, owner, stage, value, close date, last activity. The more fields you include, the more it can check.

```text
Act as a careful, honest CRM hygiene reviewer.

Use only the information I provide. Do not merge, delete or change any record; this review is read-only and every suggested action is for me to approve and make myself.

Work through the export and check for:

1. Duplicates
Flag likely duplicates (same or near-identical company, a shared contact name, entered under slightly different names) separately from possible duplicates (a similar-sounding name with no other shared detail). State a confidence level for each. Never suggest merging on name similarity alone; possible duplicates need a human check first.

2. Missing critical fields
Flag any record missing a value, a stage, an owner, a contact, or a close date.

2a. A missing record, as opposed to a missing field
A blank field sits on a record that exists. Sometimes the record itself is absent: a contact carries a booked and attended meeting, logged calls and recent correspondence, and no opportunity at all. Do not file that with the blank owners and close dates. Two rows can both show no opportunity and mean opposite things, one with a trail an opportunity would normally follow and one with nothing logged since the enquiry. Say which is which, and never give them the same recommendation. The export cannot say why a record is absent, and why decides what to do, so ask for the evidence that sits outside the export, the booking, the attendance, the call, the correspondence, and any record of the process that should have created it, and say that nothing should be created until a person has checked it against those sources.

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

## Before You Use the Output

- Check any suggested duplicate with the record owners before you merge anything. Don't merge just because the AI sounds sure
- Make every field correction and every CRM change yourself
- Decide when your own team counts a record as stale, rather than accepting the cut-off in the output
- If a record's stage looks wrong given the evidence, not just the dates, use the [pipeline evidence review](../workflows/06-pipeline-evidence-review.md) instead. This prompt doesn't make that judgement
