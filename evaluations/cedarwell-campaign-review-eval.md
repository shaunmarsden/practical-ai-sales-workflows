# Cedarwell Campaign Review Evaluation

This review scores the [worked campaign review output](../examples/cedarwell-campaign-review-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every number in the output matches the fictional campaign data exactly |
| Evidence fidelity | 5 | Keeps the fact that two variables changed at once, rather than simplifying to one clean comparison |
| Fact separation | 5 | Keeps the reply-rate figures apart from any conclusion about which change caused them |
| Missing information | 4 | Flags the small sample and the two changes made at once. It could also say more plainly that campaign two's follow-up window hasn't closed, so its meeting and opportunity figures may still move |
| Commercial usefulness | 4 | The recommended next test, a real like-for-like comparison, is useful and specific, though it doesn't estimate how big a like-for-like test would need to be to settle the question |
| Next step clarity | 4 | Says what to do next, but leaves the reader to choose which variable to test first, message or list source, with no recommendation either way |
| Tone | 5 | Reads as a plain reading of the numbers, not a pitch for either campaign |
| Privacy | 5 | Uses nothing beyond total counts and the two changed variables |
| Approval discipline | 5 | Says plainly that it recommends no targeting for the next campaign, and leaves that decision to a person |
| Hallucination risk | 4 | Rightly avoids treating the higher reply rate as proof of anything. The phrase "roughly eight percentage points" is correct arithmetic, not something any other process confirms, and should be read as exactly that |

## What Worked

- The output resists the most tempting reading of this data: that campaign two's higher reply rate shows the new approach works better. It names exactly why that reading doesn't hold: two changes at once, and too small a sample.
- It states plainly that campaign two had zero qualified opportunities against campaign one's one, rather than leaving that out because it spoils an otherwise flattering reply-rate story.
- The recommended next test is one you can act on: a real like-for-like comparison, not a vague "test more."

## What Needed Checking

- Campaign two's follow-up window hasn't closed. A reviewer should check whether its meeting and opportunity figures are still moving before treating this comparison as final rather than a snapshot.
- The output doesn't suggest a sample size for a like-for-like test that would settle it. Anyone deciding whether to run one should size it properly, rather than repeat a 12-send campaign and hit the same problem again.

## What I Changed in the Prompt

Nothing in the prompt changed for this run. The existing rules were enough to catch both test points planted in the fictional data, with no new rule: mark a small or mixed sample as inconclusive, compare like with like, and don't stop the review at the more flattering number.

## Next Test

Run a case where only one variable changed between two comparable campaigns, with a big enough sample on both sides. That would confirm the prompt credits a real, single difference when there is one, rather than only being good at flagging when there isn't.
