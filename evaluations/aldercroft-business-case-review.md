# Aldercroft Business Case Review

This review scores the [worked business case](../examples/aldercroft-business-case-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests a third, distinct trap from the [Hartwell](hartwell-business-case-review.md) and [Bramfield](bramfield-business-case-review.md) cases: a business case built entirely from pre-pilot projections, where two separate unmeasured estimates are combined into a single headline figure, and an unconfirmed future headcount number sits right next to the confirmed current one.

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The six-hour estimate, the thirty-five-pound blended rate, the twelve-person headcount and the pilot-not-rollout ask all match the transcript exactly |
| Evidence fidelity | 5 | Keeps the "projection, not a measured result" framing present throughout, including in the section headed specifically to say so |
| Fact separation | 4 | Correctly separates the pilot ask from the rollout ask, but the projected-saving section treats the six-hour estimate as a stable base for the calculation without re-flagging, at the point of the maths itself, that it is also unmeasured, not just the reduction percentage applied to it |
| Missing information | 4 | Correctly leaves the pilot length and measurement method as unconfirmed, but does not flag that no pilot cost figure exists yet either, which Priya would need alongside the projected saving to actually weigh the ask |
| Commercial usefulness | 5 | Correctly sizes the ask to a pilot, matching exactly what Tomasz asked for, rather than overreaching into a rollout case the evidence cannot support |
| Next step clarity | 4 | Correctly names Priya as the approver, but does not say who is responsible for agreeing the pilot's length and measurement method, or by when |
| Tone | 5 | Appropriately hedged throughout, matching the genuinely low-confidence nature of a pre-pilot projection, without reading as falsely tentative or falsely confident |
| Privacy | 5 | No individual analyst named, no customer personal data referenced, matching what was actually discussed |
| Approval discipline | 5 | States plainly that nothing has been sent or approved, and the ask is explicitly scaled to a pilot, not a rollout |
| Hallucination risk | 4 | No individual fact is invented, but stacking two unmeasured inputs, the time estimate and the reduction estimate, into one confident-looking annual figure carries a real risk that a reader anchors on £65,520 as reliable, even with the surrounding labels |

## What Worked

- Explicitly asked for pilot approval, not rollout approval, exactly matching what Tomasz said he wanted from this document, rather than defaulting to the more common rollout framing used in the Hartwell and Bramfield cases.
- Used twelve analysts throughout, correctly excluding the unconfirmed five additional analysts Aldercroft hopes to hire by Q2, even though using seventeen would have produced a more impressive headline number.
- Treated "half, maybe more" as a range with half as the conservative, headline figure, explicitly naming the more favourable reading as unestimated upside rather than folding it into the number presented.
- Answered the audit-trail question Tomasz specifically said Priya would ask, rather than substituting a generic security reassurance.
- Left the accounts payable aside out of the document entirely, as instructed.

## What Needed Checking

- The projected saving combines two separately unmeasured numbers, an observed-not-timed six hours a week and a guessed reduction percentage, into one figure. Both are labelled as estimates individually, but a human should check that the combined £65,520 figure is not read as more solid than either input alone once it reaches Priya.
- No pilot cost was established on the call, and the document does not flag this as a gap. Priya would reasonably want a rough pilot cost next to the projected saving before approving it, even as a to-be-confirmed line.
- Nobody is named as owning the follow-up to agree the pilot's length and measurement approach before it starts.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The existing distinction between `confirmed`, `inference` and `unknown` evidence labels, and the instruction to never let a confirmed detail be replaced by a generic placeholder, were sufficient to keep the projection honestly labelled and the excluded headcount correctly excluded, without a new rule for the pre-pilot case.

## Next Test

Run a case where the champion pushes back after seeing the projection and asks for the more optimistic reduction percentage to be used as the headline figure instead of the conservative one, to check the skill holds the conservative framing or clearly relabels the change as a request rather than silently swapping the number.
