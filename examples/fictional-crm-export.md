# Fictional CRM Export

> This is an entirely fictional CRM export, created to test the CRM Hygiene Review workflow. Every record, name and figure is invented. It reuses several companies from the [fictional pipeline snapshot](fictional-pipeline-snapshot.md) and [buyer indecision](calderwood-indecision-input.md) scenarios for continuity, and adds fresh records for the specific hygiene issues those scenarios did not need.

This export covers the whole fictional sales team, not just Shaun's own deals, since a hygiene review is normally run across a team's CRM rather than one person's pipeline. Today's date for this snapshot is 15 October.

## The Export

| # | Company | Contact | Owner | Stage | Value | Close date | Last activity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Northstar Analytics | Priya Chen | Shaun | Negotiation | £48,000 | 30 Sep | 12 Sep |
| 2 | Northstar Analytics Ltd | Priya Chen | Marcus Webb | Qualification | £45,000 | 31 Dec | 2 Oct |
| 3 | Cedarwell Group | (blank) | Shaun | Qualification | £30,000 | 31 Oct | 9 Oct |
| 4 | Meridian Freight | Ops Lead | Shaun | Proposal Sent | £72,000 | 30 Sep | 2 Sep |
| 5 | Harbourview Media | (departed) | Shaun | Verbal Commit | £55,000 | 20 Oct | 25 Sep |
| 6 | Oakline Dental Group | Office Manager | Shaun | Discovery | £18,000 | 30 Nov | 11 Oct |
| 7 | Calderwood Group | Tom Whitfield | Shaun | Negotiation | £40,000 | 15 Aug | 19 Jul |
| 8 | Bramfield Insurance Group | Ravi Patel | Marcus Webb | (blank) | £34,920 | (blank) | (blank) |
| 9 | Thornfield Manufacturing | (blank) | (blank) | Discovery | £22,000 | 31 Mar | 14 Feb |
| 10 | Fenmoor Retail Solutions | (blank) | Priti Shah | Proposal Sent | £26,000 | 30 Nov | 3 Oct |
| 11 | Fenmore Retail Solutions | (blank) | Marcus Webb | Discovery | £24,500 | 15 Dec | 28 Sep |
| 12 | Riverside Logistics Partners | Head of Ops | Priti Shah | Proposal Sent | £38,000 | 15 Nov | 14 Oct |
| 13 | Aldermoor Facilities | Facilities Lead | Shaun | Discovery | £15,000 | 20 Oct | 10 Oct |
| 14 | Westgate Analytics | Ops Director | Marcus Webb | Qualification | (blank) | 15 Dec | 8 Oct |
| 15 | Bellcross Insurance | Head of Claims | Priti Shah | Negotiation | £20,000 | 30 Jun | 2 Apr |

## Deliberate Test Points

- **Row 1 and 2: a likely exact duplicate.** Same company (one entered with "Ltd" appended), same named contact, two different owners, two different stages and values. Reads as the same account entered twice, most likely by a rep who did not check for an existing record before a marketing-sourced lead came in.
- **Row 10 and 11: a possible, not certain, duplicate.** Similar but not identical company names, no contact name given for either, different owners, different stages and values. This could be the same company mistyped twice, or two genuinely different companies that happen to sound alike. There is not enough here to call it confidently either way.
- **Row 8: missing critical fields.** Stage, close date and last activity are all blank, as if the record was created but never properly worked, or handed off incompletely between reps.
- **Row 9: stale and missing ownership.** No contact, no owner, and the last activity is exactly eight months old relative to this snapshot, with a close date that passed over six months ago. This reads as an abandoned record no one is accountable for.
- **Row 15: stale despite looking complete.** Every field is filled in, but the close date passed nearly four months ago and there has been no activity in over six months. A record can look healthy on the surface and still be stale.
- **Row 13: a close date that does not fit the stage.** Discovery stage, five days from this snapshot's date, with no evidence of anything close to a decision. A close date this close for a deal this early is very unlikely to be real.
- **Row 14: a missing value field**, which would understate any total pipeline value calculated from this export.
- **Rows 3, 4, 5, 7: close dates already covered elsewhere.** Cedarwell's close date has not yet passed and is not itself a hygiene issue. Meridian's and Harbourview's close dates have passed, and Calderwood's is also overdue; these are real, but this hygiene review should flag the date itself as unsupported without re-diagnosing why, since working out whether each of these deals is paused, blocked or genuinely stalled is what the [pipeline evidence review](../workflows/06-pipeline-evidence-review.md) already does in detail.
- **Row 12: included as a genuinely clean record.** Every field present, the close date is realistic for the stage, and the last activity is recent. A hygiene review that manufactures a problem here would not be trusted on the rest.
