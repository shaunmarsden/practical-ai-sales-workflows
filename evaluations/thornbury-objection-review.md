# Thornbury Objection Review

This review scores the [worked response](../examples/thornbury-objection-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests a harder pattern than either the [Hartwell](hartwell-objection-review.md) or [Wrenford](wrenford-objection-review.md) tests: an objection that reads exactly like an ordinary circumstances or budget objection, where the standard, factually correct playbook answer is precisely the wrong move because it answers a question the prospect never actually asked.

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Correctly reflects that Grace already accepted the funding mechanism on the first call and has not disputed it here |
| Evidence fidelity | 5 | Preserves the distinction between the funding question, already resolved, and the optics question, the one actually live |
| Fact separation | 5 | Clearly separates what Grace already accepted from what she is actually raising now, without conflating the two |
| Missing information | 4 | Correctly focuses on Grace's concern, but does not say what, if anything, should be told to Rosalind in the meantime, who is still keen and waiting to hear something |
| Commercial usefulness | 5 | Offers two genuinely distinct, workable options rather than one generic "let's talk timing" response |
| Next step clarity | 4 | Asks Grace to choose between two options, but does not propose a deadline for her reply, leaving the follow-up as open-ended as the objection itself, without a way to escape that unless a specific date is set |
| Tone | 5 | Warm and direct, explicitly avoids sounding like it is arguing with a settled question |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | States plainly nothing has been sent and no commitment has been offered or authorised |
| Hallucination risk | 4 | The "start without any internal announcement" option is offered as genuinely available, but the response does not flag that ordinary HR or payroll administration around a new apprenticeship might itself create some internal visibility, which would make that option less fully quiet than it is presented as being |

## What Worked

- Correctly recognised that the surface wording matches a standard circumstances or budget objection, and correctly recognised that answering it as one would miss the point entirely, since Grace never disputed the funding.
- Did not re-explain or re-argue the levy funding mechanism, which Grace had already accepted, avoiding the trap of repeating a settled point back to someone who did not ask about it.
- Correctly did not treat this as a disqualification, recognising a specific, describable reason to wait rather than a sign that fit or value were never there.
- Offered two genuinely different options rather than pressuring toward one, and explicitly did not manufacture urgency during a period the response itself acknowledges is sensitive.

## What Needed Checking

- Rosalind's own position is not addressed at all. She is described in the source material as "still keen" and waiting to hear something, and the response is silent on what, if anything, Shaun or Grace should tell her while this is being worked out.
- The "no internal announcement" option should be checked against Thornbury's actual HR and payroll process before being offered as fully quiet; ordinary administration around a new apprenticeship may itself be visible internally regardless of any deliberate announcement.
- No deadline is proposed for Grace's reply, which risks the same open-ended "a few months" pattern the objection itself contained, recurring in the follow-up.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The instruction to identify what is actually driving an objection, not just its surface wording, was the one directly tested here, since the surface wording and the standard correct answer to that surface wording pointed in exactly the wrong direction. The bucket system's `circumstances` category held up, but only because the response looked past the surface match to what Grace had and had not actually disputed.

## Next Test

Run a case where the objection's surface wording points to one bucket and the correct answer initially looks like it belongs to a second, but the actual resolution requires recognising a third driver that the conversation never explicitly names, to check whether the skill can hold open more than two candidate readings at once rather than settling for the first plausible reframe of the surface wording.
