# Fictional CRM Hygiene Review Evaluation

This page scores the [worked CRM hygiene review](../examples/fictional-crm-hygiene-review.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

> I've since [run this test again, blind](repeat-run-findings.md), and the repeat scored 49 out of 50, three higher than this one. That page explains why two of the three repeats scored higher than their published scores.

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 4 | Accurate against the export once corrected. I found and fixed two errors. The first draft said my own Hartwell row was the more recently active one, when the export shows Marcus Webb's row is. A later check found Harbourview's close date, 20 October, wrongly listed as already passed against the scenario's 15 October date, when it's five days away. Both are fixed and neither was left silently. |
| Evidence fidelity | 5 | Treats the Hartwell duplicate's shared contact name as strong evidence, and the Fenmoor/Fenmore possible duplicate as weak, since it shares no contact and only a similar name |
| Fact separation | 5 | Keeps a blank contact field (rows 3, 9, 10, 11) apart from a contact who left but is still recorded (row 5), rather than putting both under "missing" |
| Missing information | 4 | Good coverage of blank fields, though the first draft undercounted the blank-contact rows and counted row 5 as missing when it's out of date, not blank. Also fixed |
| Commercial usefulness | 5 | Gives specific, named actions (ask Priti Shah and Marcus Webb directly, correct Aldermoor's close date) rather than a general "review your data" |
| Next step clarity | 4 | Actions are specific for most findings. The stale-record suggestion ("re-engage or close") is the weakest of the set |
| Tone | 5 | Matter-of-fact, no blame, in line with the rest of the repository |
| Privacy | 5 | All fictional, no real company or person |
| Approval discipline | 5 | Read-only throughout, and leaves every merge, correction and reassignment for a person |
| Hallucination risk | 4 | No invented figures or dates, and the duplicate confidence levels are fairly rated (high against low). Marked down for the two errors also scored under factual accuracy: which Hartwell row was more recently active, and whether Harbourview's close date had passed. Both were stated confidently and both contradicted by the export |

## What Worked

The two possible duplicates get different levels of confidence: high for Hartwell's shared contact name, low for Fenmoor/Fenmore's similar name alone. The review refuses to suggest merging the second pair without a person checking.

Row 5's departed contact stays apart from a truly blank contact field. The first draft didn't make that distinction clearly enough, and it was worth tightening.

The review stays out of whether stages are accurate, on purpose. It flags overdue close dates as a fact about the record and points to the pipeline evidence review for the deeper judgement, rather than redoing that analysis.

It calls out a stale but complete record (row 15) separately from a plainly incomplete one (row 9). That's the harder and more useful catch of the two.

It names two records as clean, so the review doesn't read as a list of problems only.

## What Needed Checking

This worked example needed two real corrections before it was right. The first draft said my own Hartwell row was more recently active, which the export contradicts. I found the second error only later, while building the weekly operating review that pulls this review's findings into a report: it listed Harbourview's close date as already passed when it's still five days away.

Re-reading the review for whether it sounded right caught neither. Checking it, and later reusing it, against the source data caught both. Feeding one workflow's output into another, as the weekly operating review does here, turned out to be a good second check, not just a reuse of existing content.

The summary table at first undercounted the blank-contact rows, missing two of four, and mixed up an out-of-date contact with a missing one. Both are fixed. A first pass at a larger real export should expect the same kind of counting error and check for it.

The suggested actions for stale records could be sharper. Saying "re-engage or close" points the right way but doesn't commit to a specific next step, as the duplicate and missing-field actions do.

## What I Changed in the Prompt

Nothing in the prompt needed changing for this run. The error was in how I wrote the worked example, not in the instructions. That's a useful finding in itself: a worked example I write needs the same line-by-line check against its source data as any real output, not just a read for whether it sounds right.

## Next Test

Run a larger export shaped like real data, fifty to a hundred records. See whether the same checks (duplicate confidence, blank fields, staleness, close date against stage) hold up at volume. And see whether a large cluster of duplicates (three or more near-identical records, not just a pair) is handled as cleanly as the two-record case here.
