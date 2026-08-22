# Wrenmoor Buyer Indecision Review

This review scores the [worked response](../examples/wrenmoor-indecision-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests a harder pattern than the [Calderwood test](calderwood-indecision-review.md): each stated reason here is individually legitimate and gets genuinely resolved, with a new reason appearing immediately after, rather than the same unresolved reason recurring.

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The three reasons, their resolution order, and the exact wording of Farrah's messages are all represented correctly |
| Evidence fidelity | 5 | Preserves the sequential-resolution pattern as the actual signal, rather than flattening it into a single soft delay |
| Fact separation | 4 | Generally careful, but "the chain has no visible end" is stated as settled fact when it is really the diagnosis's own inference from three data points, not yet a fourth confirmed instance |
| Missing information | 4 | Flags that a phased rollout option is only conditional, but does not flag that the 34-seat count was confirmed without reconfirming price against that number, a distinct open commercial detail |
| Commercial usefulness | 5 | Gives a genuinely different play from either pushing on the offsite or passively waiting for it, and treats the offsite itself as legitimate throughout |
| Next step clarity | 4 | Asks Farrah to name a specific week, which is concrete, but does not say what happens if she does not, or replies with another open-ended reason instead |
| Tone | 5 | Names the pattern without accusation, explicitly frames it as not a criticism |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | States plainly that nothing has been sent, and explicitly leaves the phased-rollout option out of the draft since it is not confirmed available |
| Hallucination risk | 4 | The pattern read is well evidenced by three concrete data points, stronger than a single ambiguous request, but it is still an inference about an unstated internal reason, and the response's self-correction condition (re-diagnose if a specific concern surfaces) is doing real work to keep it honest |

## What Worked

- Correctly refused to diagnose reason one or two as indecision in isolation, recognising that a real, still-open budget or headcount dependency would be a legitimate reason to wait. The diagnosis only firms up once the pattern across all three is visible.
- Treated the team offsite as a legitimate reason on its own terms rather than contesting it, while still naming the sequence around it, which avoids the obvious trap of arguing with a dated, plausible-sounding constraint.
- Did not invent a date for "right after" the offsite, and instead built the next step around getting Farrah to name one.
- Left the phased-rollout option out of the actual draft reply, keeping it explicitly conditional in the method section rather than sending an unconfirmed term.

## What Needed Checking

- "The chain has no visible end" is a strong claim built from three data points. It is a reasonable read, but a human should confirm nothing legitimate is actually still open, for instance whether the 34-seat price was ever explicitly reconfirmed, before treating the diagnosis as settled.
- The draft does not set an expectation for what happens if Farrah's next reply produces a fourth soft reason rather than a firm week. The pipeline decision section covers this at the diagnosis level, but the draft reply itself does not.
- The seat-count-to-price link is the one commercial detail this test surfaced that the response does not raise as an open question, worth checking directly rather than assuming it was implicitly settled alongside the headcount number.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The requirement to rule out a real sequential dependency before diagnosing indecision, and to treat each stated reason as legitimate while it is still open, held even against a pattern designed to look like due diligence at every individual step. The offsite, the hardest single test point in this scenario, was not treated as a clean external blocker just because it had a date attached.

## Next Test

Run a case where the pattern looks identical, three resolved reasons in sequence, but the third one turns out to be a genuine, confirmed external blocker rather than another soft reason, to check the skill correctly stops treating the sequence as proof of indecision once a real block is actually confirmed, rather than applying the pattern read mechanically regardless of what the evidence later shows.
