# Fictional Weekly Operating Review Evaluation

This review scores the [worked weekly report](../examples/fictional-weekly-operating-review-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 4 | Accurate once corrected; the first draft miscounted Shaun's owned records as five instead of seven, caught by recounting the export directly rather than trusting the earlier claim |
| Evidence fidelity | 5 | Pulls the pipeline evidence review and CRM hygiene review findings through without softening or overstating them |
| Fact separation | 5 | Keeps "no baseline exists" and "outreach is missing, not zero" as explicit, separate statements rather than blending them into vaguer hedging |
| Missing information | 5 | Outreach activity is correctly reported as unavailable rather than assumed to be zero, and the report says plainly that only one meeting was actually supplied |
| Commercial usefulness | 5 | The three priorities are specific and drawn from real findings (the Hartwell duplicate, the two stale records, the Cedarwell message), not generic advice that could apply to any week |
| Next step clarity | 5 | Each priority names who or what needs to happen, not just that something should be reviewed |
| Tone | 5 | Plain and direct, no invented energy or urgency around a first, necessarily thin report |
| Privacy | 5 | Uses only what was actually supplied; no invented names or figures |
| Approval discipline | 5 | Nothing is presented as sent, merged or booked; every action is explicitly left for a person |
| Hallucination risk | 4 | No invented metric or comparison, and the "no baseline yet" discipline holds throughout, but see below |

## What Worked

- The report refuses to invent a pipeline movement narrative on a single snapshot, stating plainly that no comparison is possible yet rather than manufacturing a "since last week" line.
- Outreach activity is reported as missing, not as zero, which is the exact distinction the workflow exists to protect.
- The three priorities are pulled from real findings already produced by other workflows (the pipeline evidence review, the CRM hygiene review) rather than re-derived or invented for the report, showing this workflow genuinely composing rather than duplicating.
- The report is honest that only one meeting was supplied, rather than implying a fuller calendar.

## What Needed Checking

- This worked example needed a real correction before scoring: the first draft claimed five of Shaun's records were his own open deals, when the export shows seven. Caught by recounting directly against the export rather than trusting the earlier draft's arithmetic.
- Building this report also surfaced a second error, in the already-shipped CRM hygiene review it draws on: Harbourview's close date had been wrongly listed there as already passed, when it is five days in the future. That correction was made in the source review, not just worked around here, since the report should not quietly inherit a wrong finding from something it cites.
- The stale-record priority ("decide Thornfield's and Bellcross's fate") is directionally right but, like the source review it draws from, could commit to a sharper single action.

## What I Changed in the Prompt

Nothing needed changing in the prompt for this run. Both errors found while building this example were in the worked content, not the underlying instructions, which reinforces a pattern from the CRM hygiene review: composing one workflow's output into another is a genuinely effective way to catch mistakes the original review missed, not just a demonstration of reuse.

## Next Test

Run this workflow for a second week, once a genuine first report exists to compare against, to check whether it correctly reports real movement when a baseline does exist, rather than only being tested on the "no baseline yet" case shown here.
