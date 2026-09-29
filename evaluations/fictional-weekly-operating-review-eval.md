# Fictional Weekly Operating Review Evaluation

This review scores the [worked weekly report](../examples/fictional-weekly-operating-review-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 4 | Accurate once corrected. The first draft counted Shaun's records as five instead of seven. I caught it by recounting the export rather than trusting the earlier claim |
| Evidence fidelity | 5 | Carries the findings from the pipeline evidence review and the CRM hygiene review through without softening or overstating them |
| Fact separation | 5 | Keeps "no baseline exists" and "outreach is missing, not zero" as clear, separate statements rather than blurring them into vaguer hedging |
| Missing information | 5 | Reports outreach activity as unavailable rather than assuming zero, and says plainly that only one meeting was supplied |
| Commercial usefulness | 5 | The three priorities are specific and come from real findings (the Hartwell duplicate, the two stale records, the Cedarwell message), not generic advice that could fit any week |
| Next step clarity | 5 | Each priority says who or what needs to happen, not just that something should be reviewed |
| Tone | 5 | Plain and direct, with no made-up energy or urgency around a first report that's bound to be thin |
| Privacy | 5 | Uses only what was supplied, with no invented names or figures |
| Approval discipline | 5 | Presents nothing as sent, merged or booked, and leaves every action for a person |
| Hallucination risk | 4 | No invented metric or comparison, and it keeps to "no baseline yet" throughout. I docked a mark for the record-count error also scored under factual accuracy: a confidently stated figure the export contradicted, which is exactly what this row is there to catch |

## What Worked

- The report won't invent a story of pipeline movement from a single snapshot. It says plainly that no comparison is possible yet, rather than making up a "since last week" line.
- It reports outreach activity as missing, not zero, which is exactly the distinction the workflow exists to protect.
- The three priorities come from findings other workflows had already produced (the pipeline evidence review, the CRM hygiene review), not worked out again or invented for the report. So this workflow builds on the others rather than repeating them.
- It says plainly that only one meeting was supplied, rather than implying a fuller calendar.

## What Needed Checking

- This worked example needed a real correction before scoring. The first draft said five of Shaun's records were his own open deals, when the export shows seven. I caught it by recounting against the export rather than trusting the earlier draft's arithmetic.
- Building this report also turned up a second error, in the CRM hygiene review it draws on, which I'd already published. That review listed Harbourview's close date as already passed, when it's five days away. I corrected the source review, not just worked around it here, since the report shouldn't quietly inherit a wrong finding from something it cites.
- The stale-record priority ("decide Thornfield's and Bellcross's fate") points the right way but, like the review it draws from, could commit to one sharper action.

## What I Changed in the Prompt

Nothing, for this run. Both errors I found while building this example were in the worked content, not the instructions. That backs up a pattern from the CRM hygiene review: feeding one workflow's output into another is a good way to catch mistakes the first review missed, not just a show of reuse.

## Next Test

Run this workflow for a second week, once a real first report exists to compare against. That would check it reports real movement correctly when there is a baseline, rather than only testing the "no baseline yet" case shown here.
