# Hartwell Post Call Review

This review scores the [worked output](../examples/hartwell-post-call-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

> This test has since been [run again, blind](repeat-run-findings.md), and the repeat scored 50 out of 50, two higher than this one. That page explains why two of the three repeats came out higher than their published scores.

## What the Transcript Was Deliberately Built to Test

This section used to live inside [the transcript itself](../examples/hartwell-post-call-transcript.md), as a "Deliberate Test Points" list. It has been moved here because it tells a reader, or a model being tested against this transcript, what the correct handling of the evidence looks like, which defeats the point of using the transcript as a blind test input for any skill, including ones built after this workflow. The design intent is worth keeping on record; it just does not belong inside the raw source material a model reads as evidence.

The fictional transcript was built to include information a workflow should handle carefully:

- The team has eight account executives.
- HubSpot is the confirmed CRM.
- The current administration time is an estimate, not a measured fact.
- Alex intends to send an anonymised transcript by Thursday afternoon, subject to internal approval.
- Shaun promised to send a test outline and meeting options today.
- A meeting next Tuesday morning was discussed but no time was confirmed.
- Shaun needs to check his diary.
- Alex needs to check the recording package and whether Priya wants anything included.
- No automated email sending was agreed.
- No pricing, purchase or implementation commitment was made.

## Result

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Names, roles, systems and numbers match the transcript |
| Evidence fidelity | 5 | Conditional approval and relative timings are preserved |
| Fact separation | 5 | The unmeasured time estimate is clearly separated |
| Missing information | 5 | The call date, diary check, approval and meeting time are all flagged |
| Commercial usefulness | 5 | The output can support the real follow up work |
| Next step clarity | 5 | Actions have owners, timing and evidence |
| Tone | 4 | The email is natural, but Shaun would still make a final wording pass |
| Privacy | 5 | Only information needed for the sales task is included |
| Approval discipline | 5 | The email and CRM changes are explicitly drafts |
| Hallucination risk | 4 | The output is careful, but relative words such as today and Thursday still require the original call context |

## What Worked

- The output kept a conditional deadline conditional.
- It did not invent a meeting for next Tuesday.
- It separated the administration estimate from confirmed facts.
- It kept Priya's involvement tentative.
- It produced an email and CRM note that need only a short human review.

## What Needed Checking

- The transcript does not include the call date, so relative timings cannot be converted safely.
- The email needs real meeting options before it can be sent.
- Shaun should make a final tone pass so the email sounds exactly like him.

## What I Changed in the Prompt

The prompt now tells the AI to preserve relative timing when the call date is missing. It also requires placeholders for information the salesperson still needs to check.

## Next Test

Run the same transcript and prompt in ChatGPT, Claude and Gemini. Score each output using the same rubric and compare the corrections required rather than simply choosing the most polished answer.
