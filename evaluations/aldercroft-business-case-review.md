# Aldercroft Business Case Review

This review scores the [worked business case](../examples/aldercroft-business-case-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests a third trap, different from the [Hartwell](hartwell-business-case-review.md) and [Bramfield](bramfield-business-case-review.md) cases. The whole business case rests on forecasts made before any pilot. Two separate unmeasured estimates combine into one headline figure, and an unconfirmed future headcount sits right next to the confirmed current one.

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The six-hour estimate, the £35 blended rate, the headcount of 12 and the ask for a pilot, not a rollout, all match the transcript exactly |
| Evidence fidelity | 5 | Keeps the "projection, not a measured result" framing throughout, including in the section whose heading says exactly that |
| Fact separation | 4 | Rightly separates the pilot ask from the rollout ask. But the projected-saving section treats the six-hour estimate as a stable base for the sum, without flagging again, at the point of the maths, that it's unmeasured too, not just the reduction percentage applied to it |
| Missing information | 4 | Rightly leaves the pilot length and measurement method unconfirmed, but doesn't flag that there's no pilot cost yet either. Priya would need that next to the projected saving to weigh the ask |
| Commercial usefulness | 5 | Sizes the ask to a pilot, exactly what Tomasz asked for, rather than reaching for a rollout case the evidence can't support |
| Next step clarity | 4 | Names Priya as the approver, but doesn't say who agrees the pilot's length and measurement method, or by when |
| Tone | 5 | Hedged throughout, to match how uncertain a forecast made before a pilot really is, without sounding falsely unsure or falsely confident |
| Privacy | 5 | No analyst named and no customer personal data mentioned, matching what was discussed |
| Approval discipline | 5 | Says plainly that nothing has been sent or approved, and scales the ask to a pilot, not a rollout |
| Hallucination risk | 4 | It invents no fact. But stacking two unmeasured inputs, the time estimate and the reduction estimate, into one confident-looking annual figure carries a real risk that a reader treats £65,520 as reliable, even with the labels around it |

## What Worked

- It asked for approval of a pilot, not a rollout, exactly as Tomasz said he wanted from this document. It didn't fall back on the more common rollout framing used in the Hartwell and Bramfield cases.
- It used 12 analysts throughout, and left out the five more Aldercroft hopes to hire by Q2, which aren't confirmed. Using 17 would have given a bigger headline number.
- It treated "half, maybe more" as a range, with half as the cautious headline figure. It named the better reading as upside it hadn't estimated, rather than folding it into the number.
- It answered the audit-trail question Tomasz said Priya would ask, rather than giving a generic security reassurance.
- It left the accounts payable aside out of the document entirely, as instructed.

## What Needed Checking

- The projected saving combines two unmeasured numbers into one figure: six hours a week, observed but not timed, and a guessed reduction percentage. Each is labelled as an estimate, but a person should check that the combined £65,520 doesn't read as more solid than either input once it reaches Priya.
- The call didn't establish a pilot cost, and the document doesn't flag this as a gap. Priya would reasonably want a rough pilot cost next to the projected saving before approving it, even as a line marked to be confirmed.
- Nobody is named as owning the follow-up to agree the pilot's length and how it will be measured before it starts.
- The output's Time Commitment section says each analyst would get a short onboarding session before the measurement period. Nothing on the call says that, so my "invents no fact" note above is too strong. A person should cut the line or confirm it with Tomasz.

## What I Changed in the Prompt

Nothing in the skill needed changing for this run. Two existing rules were enough: the `confirmed`, `inference` and `unknown` evidence labels, and the instruction never to replace a confirmed detail with a generic placeholder. They kept the projection honestly labelled and the unconfirmed headcount out, with no new rule for the pre-pilot case.

## Next Test

Run a case where the champion sees the projection, pushes back, and asks for the more hopeful reduction percentage as the headline figure instead of the cautious one. That checks whether the skill keeps the cautious framing, or clearly labels the change as a request, rather than quietly swapping the number.
