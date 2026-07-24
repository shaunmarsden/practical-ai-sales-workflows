# Cedarwell Campaign Review Evaluation

This review scores the [worked campaign review output](../examples/cedarwell-campaign-review-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 45 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every number in the output matches the fictional campaign data exactly |
| Evidence fidelity | 5 | Correctly preserves that two variables changed at once, rather than simplifying to one clean comparison |
| Fact separation | 5 | Keeps the reply-rate figures separate from any conclusion about which change caused them |
| Missing information | 4 | Flags the small sample and the two simultaneous changes; could also note more explicitly that campaign two's follow-up window has not closed, so its meeting and opportunity figures may still move |
| Commercial usefulness | 4 | The recommended next test, a genuine like-for-like comparison, is useful and specific, though it does not estimate what sample size a like-for-like test would actually need to be conclusive |
| Next step clarity | 4 | States what to do next but leaves the decision of which variable to test first, message or list source, to the reader without a recommendation either way |
| Tone | 5 | Reads as a plain analytical read of numbers, not a pitch for either campaign |
| Privacy | 5 | Nothing beyond aggregate counts and the two changed variables is used |
| Approval discipline | 5 | States plainly that no next campaign's targeting is recommended, leaving that decision to a person |
| Hallucination risk | 4 | Correctly avoids treating the higher reply rate as proof of anything, though the phrase "roughly eight percentage points" is a strictly correct calculation, not something confirmed by any process beyond arithmetic, and should be read as exactly that |

## What Worked

- The output resists the most tempting reading of this data, that campaign two's higher reply rate shows the new approach works better, and names precisely why that reading does not hold: two changes at once, and too small a sample.
- Campaign two's zero qualified opportunities against campaign one's one is stated plainly, rather than left out because it complicates an otherwise flattering reply-rate story.
- The recommended next test is genuinely actionable: a real like-for-like comparison, not a vague "test more."

## What Needed Checking

- Campaign two's follow-up window has not closed; a reviewer should confirm whether its meeting and opportunity figures are still moving before treating this comparison as final, not just as a snapshot.
- The output does not suggest a sample size for a conclusive like-for-like test; a person deciding whether to run one should size it properly rather than repeating a 12-send campaign and hitting the same inconclusive problem again.

## What I Changed in the Prompt

Nothing changed in the prompt itself for this run. The existing rules, mark a small or mixed sample inconclusive, compare like with like, do not stop the review at the more flattering number, were sufficient to catch both deliberate test points in the fictional data without a new rule.

## Next Test

Run a case where only one variable actually changed between two comparable campaigns, with a large enough sample on both sides, to confirm the prompt correctly credits a real, isolated difference when one genuinely exists, rather than only being good at flagging when it does not.
