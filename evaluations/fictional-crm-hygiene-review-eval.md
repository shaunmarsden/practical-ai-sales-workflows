# Fictional CRM Hygiene Review Evaluation

This review scores the [worked CRM hygiene review](../examples/fictional-crm-hygiene-review.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 45 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 4 | Accurate against the export once corrected. Two errors were found and fixed in this worked example: the first draft wrongly claimed Shaun's Hartwell row was the more recently active one, when the export shows Marcus Webb's row is; a later correction found Harbourview's close date, 20 October, had been wrongly listed as already passed relative to the scenario's 15 October date, when it is five days in the future. Both are fixed, neither silently left. |
| Evidence fidelity | 5 | The Hartwell duplicate's shared contact name is treated as strong evidence; the Fenmoor/Fenmore possible duplicate is correctly treated as weak, since it shares no contact and only a similar name |
| Fact separation | 5 | Cleanly separates a blank contact field (rows 3, 9, 10, 11) from a departed-but-recorded contact (row 5), rather than lumping both under "missing" |
| Missing information | 4 | Good coverage of blank fields, though the first draft undercounted the blank-contact rows and miscounted row 5 as missing when it is stale, not blank; also fixed |
| Commercial usefulness | 5 | Gives concrete, named actions (ask Priti Shah and Marcus Webb directly, correct Aldermoor's close date) rather than a generic "review your data" |
| Next step clarity | 4 | Actions are specific for most findings; the stale-record suggestion ("re-engage or close") is the softest of the set |
| Tone | 5 | Matter-of-fact, no accusation, consistent with the rest of the repository |
| Privacy | 5 | All fictional; no real company or person |
| Approval discipline | 5 | Explicitly read-only throughout; every merge, correction and reassignment is left for a person |
| Hallucination risk | 4 | No invented figures or dates, and the duplicate confidence levels are honestly graded (high versus low), but see below |

## What Worked

- The two duplicate candidates are handled with genuinely different confidence, high for Hartwell's shared contact name, low for Fenmoor/Fenmore's similar name alone, and the review explicitly refuses to suggest merging the second pair without a human check.
- Row 5's departed contact is correctly kept separate from a truly blank contact field, a distinction the first draft did not make cleanly enough and that was worth tightening.
- The review stays out of the stage-accuracy question on purpose, flagging overdue close dates as a structural fact and pointing to the pipeline evidence review for the deeper judgement, rather than re-doing that analysis.
- A genuinely stale-but-complete record (row 15) is called out separately from an obviously incomplete one (row 9), which is the harder and more useful catch of the two.
- Two records are explicitly named as clean, so the review does not read as a list of only problems.

## What Needed Checking

- This worked example needed two real corrections before it was honest: the first draft claimed Shaun's Hartwell row was more recently active, which the export contradicts; a second error, found only later while building the weekly operating review that pulls this review's findings into a report, wrongly listed Harbourview's close date as already passed when it is still five days away. Neither was caught by re-reading the review for plausibility; both were caught by checking it, and later reusing it, against the source data directly. Composing a workflow's output into another workflow, as the weekly operating review does here, turned out to be a genuinely effective second check, not just a reuse of existing content.
- The summary table originally undercounted the blank-contact rows (missed two of four) and conflated a stale contact with a missing one; both are fixed, but a first pass at a larger real export should expect to make the same kind of counting error and check it.
- The suggested actions for stale records could be sharper; "re-engage or close" is directionally right but does not commit to a specific next step the way the duplicate and missing-field actions do.

## What I Changed in the Prompt

Nothing needed changing in the prompt for this run. The error that surfaced was in how the worked example was written, not in the underlying instructions, which is itself a useful finding: a self-authored worked example needs the same line-by-line check against its own source data as any real output would, not just a read for plausibility.

## Next Test

Run a larger, real-shaped export, fifty to a hundred records, to see whether the same checks (duplicate confidence, blank-field detection, staleness, close-date-versus-stage) hold up at volume, and whether a genuinely large duplicate cluster (three or more near-identical records, not just a pair) gets handled as cleanly as the two-record case here.
