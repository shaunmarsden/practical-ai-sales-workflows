# Bramfield Business Case Review

This review scores the [worked business case](../examples/bramfield-business-case-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Names, roles, seat count and both pricing paths match the transcript exactly |
| Evidence fidelity | 5 | The timed eighteen-to-seven-minute figure and the two qualitative pilot observations are each represented as what they are, not inflated into equivalent measured claims |
| Fact separation | 4 | The conditional pricing is stated correctly, though the document could be even more explicit that the two totals are mutually exclusive, not additive options |
| Missing information | 5 | The compliance confirmation and the rollout timing are both flagged as outstanding, and Meera's specific priorities are correctly left unstated |
| Commercial usefulness | 5 | Both pricing paths are shown with totals calculated correctly, giving Meera exactly what she needs to compare them |
| Next step clarity | 4 | The next step is clear, but, as with the Hartwell case, timing depends on people who have not yet confirmed a date |
| Tone | 5 | Reads as a proposal for Meera, third person throughout, appropriately more formal given the regulatory content |
| Privacy | 5 | No claims handler is named individually, as instructed |
| Approval discipline | 5 | Explicitly a draft; nothing is presented as sent, approved or confirmed |
| Hallucination risk | 3 | No invented figures or dates, but the commercial section is the hardest part of this scenario to get exactly right, and a careful reader should still double-check the conditional wording before this goes to Finance |

## What Worked

- The two-year conditional pricing is stated correctly and the document explicitly says the discounted year-two rate is not available on its own, which is the main trap this scenario was built to test.
- The £34,920 and £37,440 totals are both calculated correctly from the confirmed per-seat figures, and both are shown rather than only the cheaper one.
- Meera's own priorities are not invented from her job title. The document sticks to what Ravi actually said, that she needs to approve spend above his sign-off limit, and nothing more specific.
- The compliance answer given on the call (outputs inherit Bramfield's existing FCA retention and access policy because they stay in-environment) is stated as Shaun's real answer, while written confirmation is correctly flagged as still outstanding, mirroring the same discipline as the Hartwell case's compliance trap.
- The Q1 rollout target is correctly attributed to Ravi as his own hope, not converted into a date Meera or Finance have agreed.
- The underwriting team aside is left out of the document entirely, as instructed.

## What Needed Checking

- The commercial section is genuinely harder to misread here than in the Hartwell case, since two totals sit next to each other. A human should re-read the conditional wording once more before this goes to Meera, since a Finance reader skimming quickly is the person most likely to take the cheaper total as guaranteed.
- Shaun should confirm the rollout timing with Ravi and update the document once Meera's own budget cycle is known.
- The compliance confirmation should be chased and the document updated once it arrives.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The scenario was deliberately built to test a genuinely different trap from the Hartwell case, conditional multi-year pricing rather than a flat figure, and the skill's existing "never invent a figure" and "figures the prospect has actually seen or agreed" guardrails were sufficient to handle it correctly without a new rule.

## Next Test

Run this same transcript through ChatGPT, Claude and Gemini and score each output, paying particular attention to whether every model keeps the two pricing paths visibly separate rather than collapsing them into a single headline number, since that is the trap most likely to be missed under time pressure.
