# Thornbury Objection Review

This review scores the [worked response](../examples/thornbury-objection-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests a harder pattern than the [Hartwell](hartwell-objection-review.md) or [Wrenford](wrenford-objection-review.md) tests. The objection reads exactly like an ordinary circumstances or budget objection. But the standard, factually correct playbook answer is the wrong move, because it answers a question the prospect never asked.

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Correctly reflects that Grace accepted the funding mechanism on the first call and hasn't disputed it here |
| Evidence fidelity | 5 | Keeps the funding question, already settled, apart from the optics question, the one that's live |
| Fact separation | 5 | Clearly separates what Grace already accepted from what she's raising now, without mixing the two |
| Missing information | 4 | Rightly focuses on Grace's concern, but doesn't say what, if anything, Rosalind should be told in the meantime. She's still keen and waiting to hear something |
| Commercial usefulness | 5 | Offers two different, workable options rather than one generic "let's talk timing" response |
| Next step clarity | 4 | Asks Grace to choose between two options, but proposes no deadline for her reply. That leaves the follow-up as open-ended as the objection, with no way out unless a date is set |
| Tone | 5 | Warm and direct, and takes care not to sound like it's arguing with a settled question |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | Says plainly that nothing has been sent and no commitment has been offered or authorised |
| Hallucination risk | 4 | It offers the "start without any internal announcement" option as fully available. But it doesn't flag that ordinary HR or payroll admin for a new apprenticeship might itself be visible internally, which would make that option less quiet than it's presented |

## What Worked

- It saw that the wording matches a standard circumstances or budget objection, and that answering it as one would miss the point, since Grace never disputed the funding.
- It didn't explain or argue the levy funding again. Grace had already accepted it, and repeating a settled point to someone who didn't ask about it is the trap here.
- It didn't treat this as a disqualification. It saw a specific reason to wait, not a sign that the fit or value was never there.
- It offered two different options rather than pushing towards one, and didn't invent urgency during a period the response itself calls sensitive.

## What Needed Checking

- It doesn't address Rosalind's position at all. The source material describes her as "still keen" and waiting to hear something, and the response says nothing about what, if anything, I or Grace should tell her while this gets worked out.
- The "no internal announcement" option should be checked against Thornbury's real HR and payroll process before it's offered as fully quiet. Ordinary admin for a new apprenticeship may be visible internally, whatever anyone announces.
- It proposes no deadline for Grace's reply, so the open-ended "a few months" pattern in the objection could repeat in the follow-up.

## What I Changed in the Prompt

Nothing in the skill needed changing for this run. This run tested the instruction to find what's driving an objection, not just its wording, because the wording and the standard answer to it pointed the wrong way. The bucket system's `circumstances` category held up, but only because the response looked past the wording to what Grace had and hadn't disputed.

## Next Test

Run a case where the wording points to one bucket and the right answer at first seems to belong to a second, but solving it means spotting a third driver the conversation never names. That would check whether the skill can keep more than two readings open at once, rather than settling for the first plausible reframe of the wording.
