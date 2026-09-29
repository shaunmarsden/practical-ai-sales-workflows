# Bramfield Business Case Review

This review scores the [worked business case](../examples/bramfield-business-case-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Names, roles, seat count and both pricing paths match the transcript exactly |
| Evidence fidelity | 5 | The timed drop from 18 minutes to seven and the two qualitative pilot observations each appear as what they are, not inflated into equal measured claims |
| Fact separation | 4 | The conditional pricing is stated correctly, though the document could say more plainly that the two totals are alternatives, not options you add together |
| Missing information | 5 | It flags the compliance confirmation and the rollout timing as outstanding, and rightly doesn't state Meera's own priorities |
| Commercial usefulness | 5 | It shows both pricing paths with correct totals, giving Meera exactly what she needs to compare them |
| Next step clarity | 4 | The next step is clear, but, as in the Hartwell case, timing depends on people who haven't confirmed a date yet |
| Tone | 5 | Reads as a proposal for Meera, in the third person throughout, and suitably more formal given the regulatory content |
| Privacy | 5 | No claims handler is named, as instructed |
| Approval discipline | 5 | Clearly a draft. Nothing is presented as sent, approved or confirmed |
| Hallucination risk | 3 | No invented figures or dates, but the commercial section is the hardest part of this scenario to get exactly right, and a careful reader should still check the conditional wording before this goes to Finance |

## What Worked

- It states the two-year conditional pricing correctly and says the discounted year-two rate isn't available on its own. That's the main trap this scenario was built to test.
- It works out the £34,920 and £37,440 totals correctly from the confirmed per-seat figures, and shows both rather than only the cheaper one.
- It doesn't invent Meera's priorities from her job title. It sticks to what Ravi said, that she needs to approve spend above his sign-off limit, and nothing more specific.
- It gives the compliance answer from the call as my real answer: outputs inherit Bramfield's existing FCA retention and access policy because they stay in-environment. It rightly flags written confirmation as still outstanding, the same care the Hartwell case's compliance trap tested.
- It credits the Q1 rollout target to Ravi as his own hope, not a date Meera or Finance have agreed.
- It leaves the underwriting team aside out of the document entirely, as instructed.

## What Needed Checking

- The commercial section is harder to misread here than in the Hartwell case, since two totals sit side by side. A person should read the conditional wording once more before this goes to Meera. A Finance reader skimming quickly is the one most likely to take the cheaper total as guaranteed.
- I should confirm the rollout timing with Ravi, and update the document once Meera's own budget cycle is known.
- The compliance confirmation needs chasing, and the document updating once it arrives.

## What I Changed in the Prompt

Nothing in the skill needed changing for this run. I built the scenario on purpose to test a different trap from the Hartwell case: conditional pricing over several years rather than a flat figure. The skill's existing "never invent a figure" and "figures the prospect has actually seen or agreed" guardrails handled it correctly without a new rule.

## Next Test

Run this same transcript through ChatGPT, Claude and Gemini and score each output. Watch in particular whether every model keeps the two pricing paths visibly separate rather than merging them into one headline number, since that's the trap most likely to be missed in a hurry.
