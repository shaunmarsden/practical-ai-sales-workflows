# Hartwell Post Call Review

This review scores the [worked output](../examples/hartwell-post-call-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

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
