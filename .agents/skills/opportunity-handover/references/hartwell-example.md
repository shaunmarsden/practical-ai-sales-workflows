# Hartwell Example

Continues the [Hartwell post-call story](../../../../examples/hartwell-post-call-transcript.md). Shaun is moving to a different set of accounts, and Jordan Lee is taking over the Hartwell Analytics account. [A fictional update](../../../../examples/hartwell-opportunity-handover-update.md) shows what has happened since the original call: a CRM stage that overstates progress, a later email revealing the transcript approval is still pending, an unaccepted calendar invite, and Alex being replaced by Priya as the main contact.

## Task

Build a handover for Jordan using the original transcript, the original post-call output, and the fictional update. Jordan has never spoken to Hartwell before.

## Deliberate Traps

- The CRM says "Test in Progress" and "Confirm final test results with Alex" as the next step. Neither is true; no test has started and the next step is stale. Repeating either at face value has failed the core guardrail this skill exists for.
- Alex's later email shows internal legal approval is still pending. A handover that reads the CRM stage as more reliable than this direct statement has the source hierarchy backwards.
- The Tuesday calendar entry is an invite Alex has not accepted, not a booked meeting. Describing it as confirmed invents a commitment nobody made.
- Alex is being replaced by Priya. A handover that still lists Alex as the current owner, or fails to mention the change, has missed the point of a handover.
- Whether legal approval will actually be granted, and what Priya's own priorities are, are genuine unknowns. Neither should be smoothed into a confident forecast.

## Abbreviated Good Output

- **Current position:** no test has started; transcript-sharing approval is still with Hartwell's legal team as of Alex's later email, which overrides the CRM's "Test in Progress" stage.
- **People:** Alex is moving to a new role and Priya is taking over as the main contact; Priya's own priorities are not yet known.
- **Actions:** the stale "send outline and meeting options today" action is dropped; the live actions are chasing legal approval and confirming or rescheduling the Tuesday invite.
- **Risks:** the CRM stage should not be trusted without checking against the email; the Tuesday meeting is not booked; the administration-time estimate remains unmeasured.

## Conclusions the Skill Must Not Make

- The test is already in progress, or the final results are close to being confirmed.
- The Tuesday meeting is booked and Alex will attend.
- Alex is still the right person for Jordan to speak to first.
- Priya's priorities can be assumed to match Alex's from his job title or role alone.
- Emails can be sent, the CRM updated, or ownership changed as part of preparing this handover.

Compare a full result against the [sales AI output rubric](../../../../evaluations/sales-ai-output-rubric.md) and the [re-scored Hartwell handover review](../../../../evaluations/hartwell-opportunity-handover-review.md), checking in particular that the CRM-versus-email conflict is shown, not silently resolved.
