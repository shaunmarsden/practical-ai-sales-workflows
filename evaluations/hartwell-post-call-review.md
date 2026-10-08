# Hartwell Post Call Review

This review scores the [worked output](../examples/hartwell-post-call-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

> I've since [run this test again, scored without knowing which run was which](repeat-run-findings.md), and the repeat scored 50 out of 50, two higher than this one. That page explains why two of the three repeats came out higher than their published scores.

## What the Transcript Was Deliberately Built to Test

This section used to live inside [the transcript itself](../examples/hartwell-post-call-transcript.md), as a "Deliberate Test Points" list. I moved it here because it tells a reader, or a model being tested on this transcript, what the right handling of the evidence looks like. That spoils the transcript as a test input for any skill, including ones built after this workflow. The design is worth keeping on record. It just doesn't belong in the raw material a model reads as evidence.

I built the fictional transcript to include information a workflow should handle with care:

- The team has eight account executives.
- HubSpot is the confirmed CRM.
- The current admin time is an estimate, not a measured fact.
- Alex intends to send an anonymised transcript by Thursday afternoon, subject to internal approval.
- I promised to send a test outline and meeting options today.
- A meeting next Tuesday morning was discussed, but no time was confirmed.
- I need to check my diary.
- Alex needs to check the recording package and whether Priya wants anything included.
- No automated email sending was agreed.
- No pricing, purchase or implementation commitment was made.

## Result

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Names, roles, systems and numbers match the transcript |
| Evidence fidelity | 5 | Conditional approval and relative timings are kept |
| Fact separation | 5 | The unmeasured time estimate is clearly kept apart |
| Missing information | 5 | The call date, diary check, approval and meeting time are all flagged |
| Commercial usefulness | 5 | The output can support the real follow-up work |
| Next step clarity | 5 | Actions have owners, timing and evidence |
| Tone | 4 | The email is natural, but I'd still make a final pass on the wording |
| Privacy | 5 | Only information the sales task needs is included |
| Approval discipline | 5 | The email and CRM changes are clearly drafts |
| Hallucination risk | 4 | The output is careful, but relative words such as today and Thursday still need the original call context |

## What Worked

- The output kept a conditional deadline conditional.
- It didn't invent a meeting for next Tuesday.
- It kept the admin estimate apart from confirmed facts.
- It kept Priya's involvement tentative.
- It produced an email and CRM note that need only a short human review.

## What Needed Checking

- The transcript doesn't include the call date, so relative timings can't be safely turned into dates.
- The email needs real meeting options before it can be sent.
- I should make a final pass on tone so the email sounds exactly like me.
- The actions table says Alex "should be able to send it" and "said he would check". The transcript never gives Alex's gender. I missed that when I scored it, and the [handover review](hartwell-opportunity-handover-review.md) treats the same slip as an automatic failure.

## What I Changed in the Prompt

The prompt now tells the AI to keep relative timing as it is when the call date is missing. It also asks for placeholders where the salesperson still needs to check something.

## Next Test

Run the same transcript and prompt in ChatGPT, Claude and Gemini. Score each output on the same rubric, and compare the corrections each needs rather than just picking the most polished answer.
