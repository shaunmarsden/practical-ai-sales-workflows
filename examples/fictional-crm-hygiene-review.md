# Fictional CRM Hygiene Review

> This is a worked review created from the [fictional CRM export](fictional-crm-export.md). It is read-only. Nothing has been merged, deleted or changed in any CRM. Every suggested action is left for a person to approve and make.

## Summary

| Issue type | Records | Count |
| --- | --- | --- |
| Likely exact duplicate | Rows 1, 2 (Hartwell Analytics) | 2 |
| Possible duplicate, needs a human check | Rows 10, 11 (Fenmoor / Fenmore Retail Solutions) | 2 |
| Missing value, stage, close date or last activity | Rows 8, 14 | 2 |
| Blank contact field | Rows 3, 9, 10, 11 | 4 |
| Missing owner | Row 9 | 1 |
| Stale, no recent activity | Rows 9, 15 | 2 |
| Contact recorded as departed, not blank | Row 5 | 1 |
| Close date unsupported by stage | Row 13 | 1 |
| Close date already passed | Rows 1, 4, 7 | 3 |
| No issue found | Rows 6, 12 | 2 |

Some records appear in more than one row above; Row 9, for example, is both stale and missing a contact and an owner.

## Likely Exact Duplicate

**Rows 1 and 2, Hartwell Analytics / Hartwell Analytics Ltd.** Same contact, Priya Chen, at what reads as the same company with a suffix added. Different owners, stages and values suggest this was entered twice rather than updated once, most likely a marketing-sourced lead re-entered without checking for an existing record.

- **Confidence:** high. Same named contact at what is very likely the same company is a strong signal.
- **Suggested action:** merge, with Shaun's row kept as the primary since it is the more advanced of the two (Negotiation versus Qualification), though Marcus Webb's row is the more recently active and should be checked for anything worth carrying over, such as a newer contact detail, before it is archived. A person should confirm this is genuinely one company before merging.

## Possible Duplicate, Needs a Human Check

**Rows 10 and 11, Fenmoor Retail Solutions / Fenmore Retail Solutions.** Similar but not identical names, no contact name recorded on either row, different owners, different stages and values. This could be the same company entered twice with a typo, or two separate companies that happen to sound alike.

- **Confidence:** low. There is not enough here, no shared contact, no shared detail beyond a similar name, to call this a duplicate with any certainty.
- **Suggested action:** ask Priti Shah and Marcus Webb directly whether these are the same account before touching either record. Do not merge on name similarity alone.

## Missing Critical Fields

- **Row 8, Bramfield Insurance Group.** Stage, close date and last activity are all blank. The value is present, which suggests this record was set up but never properly worked, or handed off incompletely.
- **Row 14, Westgate Analytics.** No value recorded, which means any pipeline total calculated from this export understates the true figure by at least this deal's size.
- **Rows 3, 9, 10 and 11 have a blank contact field.** Cedarwell Group, Thornfield Manufacturing, Fenmoor Retail Solutions and Fenmore Retail Solutions all carry no named contact at all. Row 9 is also missing an owner, the only record in this export with no one assigned to it.
- **Row 5, Harbourview Media, is a different case worth keeping separate.** The contact field is not blank; it notes the previous contact has left. That is a data-freshness problem, not a missing field, and should not be counted alongside the genuinely blank ones above.
- **Suggested action:** Ravi Patel's owner, Marcus Webb, should confirm the current stage and next step for Bramfield. Westgate's owner should add the missing value. The four blank-contact records need a named contact added by their owners, and Thornfield specifically needs an owner assigned before anyone is accountable for it.

## Stale Records

- **Row 9, Thornfield Manufacturing.** No owner, no contact, last activity eight months ago, close date passed over six months ago. This reads as abandoned, not merely slow.
- **Row 15, Bellcross Insurance.** Every field is present, which makes this easy to miss, but the close date passed nearly four months ago and there has been no activity in over six months.
- **Suggested action:** both should be reassigned an owner (Thornfield currently has none) and either genuinely re-engaged with a dated reason, or closed and reclassified, rather than left open indefinitely. This review does not judge whether either deal is recoverable; that judgement needs a person, or the [pipeline evidence review](../workflows/06-pipeline-evidence-review.md) if there is enough evidence to work with.

## Close Date Unsupported by Stage

**Row 13, Aldermoor Facilities.** Discovery stage, five days from this snapshot's date. A close date this close for a deal this early is very unlikely to reflect reality.

- **Suggested action:** the owner should correct the close date to something realistic for a Discovery-stage deal, or explain what makes this one genuinely fast-moving.

## Close Dates Already Passed

Rows 1 (Hartwell) and 4 (Meridian) carry a close date that has already passed. Row 7 (Calderwood)'s close date, 15 August, has also passed. This review flags the date itself as unsupported. It does not attempt to diagnose why each deal has not closed, whether it is paused, blocked, or simply overdue for an update; that is what the [pipeline evidence review](../workflows/06-pipeline-evidence-review.md) is for, and two of these three deals are examined there in detail.

Row 5 (Harbourview)'s recorded close date, 20 October, has not actually passed yet. Its issue is different: the only known contact appears to have left the company, which the recorded stage and next step both still depend on. See the "Missing Critical Fields" section above and the [pipeline evidence review](../workflows/06-pipeline-evidence-review.md) for that finding.

## No Issue Found

Row 6 (Oakline Dental Group) and Row 12 (Riverside Logistics Partners) have every field present, a close date consistent with their stage, and recent activity. No hygiene issue is flagged on either, deliberately, so this review does not read as a list of problems on every record.

## What Not to Do

- Do not merge, delete or update any record automatically. Every action above is a suggestion for a person to approve.
- Do not merge the possible Fenmoor/Fenmore duplicate on name similarity alone; confirm with the owners first.
- Do not treat a stale or overdue record as evidence the deal is dead; that is a separate judgement, covered by the pipeline evidence review where enough evidence exists.
- Do not present any scoring threshold used here (such as what counts as "stale") as a universal rule; these should be configurable to the team's own definition.

## Notes for Human Review

- The eight-month and six-month staleness figures used above are illustrative, not a fixed threshold. Confirm what counts as stale for this team before relying on this review's judgement calls.
- Confirming the two duplicate candidates with the actual owners should happen before this export is used for any pipeline total, since a confirmed duplicate changes the real number.
