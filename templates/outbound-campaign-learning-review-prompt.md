# Outbound Campaign Learning Review Prompt

> This is the prompt behind the [outbound campaign learning review workflow](../workflows/14-outbound-campaign-learning-review.md), which now has its own fictional test and scored evaluation. Try it on a real campaign, then ask whether it led to a better next test or just a tidy report. That matters more than the fictional test.

Copy the prompt below, then add what you have: the audience, the signal or list source, the message and offer, what changed since the last campaign, and the raw numbers.

```text
Act as a careful reviewer of an outbound campaign's actual result, not its impression.

Use only the numbers and detail I give you. Do not treat reply rate alone as the result, and do not imply a conclusion my sample size cannot actually support.

Record the following, exactly as I have described it, not a tidied-up version:

1. The audience: who this went to, and why it was selected.
2. The signal or data source used to build the list or angle.
3. The front-end offer, the message itself, and the call to action.
4. The single variable actually being tested here, and what was deliberately kept the same as the last comparable campaign. If more than one thing changed at once, say so plainly rather than picking one to credit.
5. The raw numbers: messages delivered, total replies, positive replies, meetings booked, meetings attended, and qualified opportunities that came from them.
6. Anything that makes this comparison uncertain: a small sample, a mixed audience, a data source that changed partway through, a benchmark from somewhere else being used as if it were this campaign's own baseline.
7. What to keep, stop, or test next, based only on what these numbers actually support.

Rules:
- Never present one campaign, a small sample, or someone else's benchmark as proof of what should work everywhere.
- Compare like with like. A change in audience and a change in message at the same time cannot be credited to either one alone.
- Mark a small or mixed sample as inconclusive rather than reading a trend into it.
- If reply rate looks good but meetings or qualified opportunities do not follow, say so rather than stopping the review at the more flattering number.
```

## Before You Use the Output

- Check that only one real change gets the credit, not several changes bundled together
- Confirm a small or mixed sample has been marked inconclusive, not quietly treated as a result
- Decide yourself what to keep, stop or test next. This suggests a reading of the numbers, not the decision
- If it helped you plan a better next test, log that in the [time and quality log](time-and-quality-log.md). If it only produced a tidy report with nothing to act on, that's worth knowing too
