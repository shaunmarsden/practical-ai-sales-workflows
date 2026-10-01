# CRM Hygiene: The Record That Should Have Existed

## Status

**A real gap, and a tested change to the method.** A real opportunity had no CRM record at all, because an automation that should have created it didn't. I never ran the published CRM hygiene method on that case, and couldn't have, so this isn't a real-use test and the evidence matrix doesn't log it as one. What it is: a real case that showed a gap, a fair test of the method against that gap, and one small change the test supported.

## What Was Reviewed Privately

A real enquiry came in through a paid social lead form. Within two minutes the person had booked a qualification meeting through the automated booking link. Five days later they attended the meeting. A short outbound call went out two minutes into it, and a follow-up email 45 minutes after it ended. None of it had an opportunity record.

The intake automation had started. Its first action runs before anything else, and the value it wrote to the contact record was still there. The step that creates the opportunity sits further down the same flow, behind a delay. Ninety seconds after the contact was created, inside that delay, two duplicate contact records were merged into the one that survived. The opportunity was never created. The only opportunity the contact ever had was made by hand five days later.

I checked every step above against the individual system records, not the note written at the time. I've left out the employer, the people, the record identifiers, the flow, the form, the campaign, the booking link, the pipeline, the value and the internal stage names.

### What is verified and what is inferred

The lesson only holds if these stay apart.

| Claim | Status |
|---|---|
| The enquiry came in at a recorded time through a lead form | Verified from the contact's creation date and source fields |
| The intake automation ran | Verified: the value its first action wrote is still on the contact record |
| The meeting was booked 90 seconds later from the automated link | Verified from the meeting's creation date and the recorded conversion event |
| Two records were merged into the survivor at a recorded time inside the delay | Verified from the merge fields, which carry the timestamp |
| The step that creates the opportunity sits behind a delay | Verified from the current flow definition |
| The eligibility rules wouldn't have held the opportunity back | Verified: every answer leads to the branch that creates one |
| No opportunity existed until someone made one by hand five days later | Verified: the contact has exactly one, and it was created on the later date |
| The meeting was attended, for about 35 minutes | Verified from a separate call record on the meeting platform |
| A call and a follow-up email followed | Verified from the call and email records |
| **The merge is what took the contact out of the automation** | **Inferred.** Nothing I can retrieve logs the removal. The merge is logged, the missing opportunity is verified, and the timing fits. That's a strong reading, not a recorded fact |
| **Which of the three records the automation had started on** | **Can't be known.** The survivor kept the earliest creation date, so the evidence that would settle it is gone |
| The flow in April was the same as it is now | **Not verified.** The flow has changed since, and it has no revision history I can see |

The rebuilt opportunity then ran for 10 weeks across five people on the employer side, and was lost in the end. That matters. Getting the record back didn't get the sale back. The value was in the pipeline being true, not in a different outcome.

## Why This Is Not Covered by the Existing Real-Use Finding

That job already has a logged real-use finding, about records in a live pipeline that were neither prospects nor ordinary missing-data cases. This is different. A test record is a row that shouldn't be there. This is a row that should be there and isn't, and no export can contain it.

## The Test

The obvious test would be to give the method an export with a row missing and ask what's wrong. That test is unfair. The method works through an export field by field, so a gap that leaves no trace in the export is bound to be missed, and proves nothing.

In the real case, the sign wasn't in the deal export at all. It was a contact with a booked and attended meeting, logged calls, recent emails, and no opportunity. The method's own list of inputs includes contact and last activity, and it's told to look for what's missing. So whether it spots this as missing is a fair question about the published text.

I built the [fictional contact-level export](../examples/fictional-crm-contact-export.md) to ask it. It carries eight problems, so this isn't the only thing in it: a clear duplicate, a near-duplicate that mustn't be merged on name alone, a blank owner, a complete-looking record four months stale, an early-stage record closing in four days, an obvious demo row, and two rows with no opportunity. Those last two are the point. One has the full trail an opportunity would normally follow. The other has nothing logged since the enquiry, so nothing was ever missed. A method that flags both the same way is reacting to a blank column, not weighing evidence.

I ran the published skill six times, then the changed skill six times. Each run saw only the skill, frozen as it stood, and the export, and was told to read nothing else. Before I built the input, I wrote down what would count as a pass, what would count against the method, and what would void a run.

## What the Method Got Right

| Check | Result |
|---|---|
| Flagged the missing opportunity, unprompted, as one of eight problems | 6 of 6 |
| Described the second row's thin trail correctly | 6 of 6 |
| Made up no stage, value or close date for the missing record | 6 of 6 |
| Kept the review read-only and left every action to a person | 6 of 6 |
| Also caught all six ordinary hygiene problems | 6 of 6 |

The first row proved me wrong. I'd assumed the method couldn't reach a record that doesn't exist, because it's written entirely around an export of records that do. I was wrong about finding it. Every run found it without being pointed at it.

## What the Method Got Wrong or Did Weakly

Past that point, my assumption held.

**It treated a missing record as a blank field.** All six filed it under a missing-fields heading. One put it in the same list as "Owner field is blank". Then, in its numbered actions, it listed "Decide whether Brackmoor Group and Felsted Components need an Opportunity created" next to "Fill in the Owner on the Quillfield Media record". Those aren't the same kind of act. Filling in an owner corrects a record. Opening an opportunity creates one. (An earlier version of this page misquoted the first of those and said the record sat directly above the blank owner. Another row came between them.)

**It never asked why, and never asked for anything outside the export.** No run mentioned an automation, a workflow, a sync or an integration. None asked for a booking, an attendance record or emails to check against. To the published method, a failed automation and a person who hasn't got round to it look the same. That difference is exactly what decides whether rebuilding the record is right.

**Two of six gave the row with evidence and the row without it the same recommendation.** One justified this by "the engagement level already logged against them", when the engagement level is the only difference between them.

## The Change, and What It Cost

I added one step to the skill and the workflow, and one guardrail line: tell a missing field from a missing record, never give the two rows the same recommendation, name the evidence outside the export, and create nothing until a person has checked it.

| Check | Published | Changed |
|---|---|---|
| Filed the missing record as an ordinary missing field | 6 of 6 | 0 of 6 |
| Told the row with evidence from the row without | 6 described it, 4 drew the conclusion | 6 of 6 |
| Gave both rows the same recommendation | 2 of 6 | 1 of 6 |
| Named evidence outside the export to check first | 0 of 6 | 6 of 6 |
| Wrongly treated the row without evidence as a missing record | 0 of 6 | 0 of 6 |
| Still caught all six ordinary problems, duplicates still split | 6 of 6 | 6 of 6 |

You can't compare how often the two sets found the gap, because the changed skill names the pattern the input contains. So I make no claim about finding it from the second set. The published skill had already found it 6 of 6 with no hint.

One run still merged the two rows back together in its action list after separating them in its findings. The change took that from two of six to one of six. It didn't remove it.

The published skill is exactly the file those six runs read. At the time I left the pasteable prompt alone on purpose, because changing it would have been a second, untested change. I've since [tested it separately](crm-hygiene-prompt-missing-record-test.md), and it now carries the same step, so the recipe card and the skill match.

## What This Supports

- A missing CRM record is worth treating as a question, not an answer, when there's a trail behind it that a record would normally follow.
- The evidence has to come from outside the record, because there's no record to read. In the real case that meant the lead form, the booking, the attendance, the call, the emails and the automation's own traces.
- The burden of proof runs the other way from ordinary hygiene. Correcting a field starts from a record, which is itself evidence. Creating one starts from nothing, so the bar has to be higher, not lower.
- A method can find a problem and still file it wrongly. Every run found it here and every run filed it wrongly. A pass mark wouldn't have shown that.
- Two gaps can look the same in an export and mean opposite things. Telling them apart is the difference between correcting a pipeline and inflating one.

## What This Does Not Support

- It doesn't show that missing records should generally be rebuilt. One case, with an unusually full trail and a logged merge, doesn't make a rule. A thinner trail wouldn't have justified it.
- It doesn't show the method now handles this well in real use. Both sets of runs used a fictional input. I've still never run the method on the real case.
- The cause is inferred, not logged. The merge is recorded and the missing opportunity is verified. The removal from the automation isn't, and the merge destroyed the evidence that would settle it.
- I claim no commercial outcome. The rebuilt opportunity was lost in the end.
- It isn't an independent test. Nobody outside this project has scored any of it.
- The new step only works when the export carries the activity behind a record. The method's list of inputs doesn't ask for booking, attendance or call columns, so a deal-level export won't trigger it at all. That's a limit of the change, not a hidden success.
- The real record was created in a live CRM through an integration, with an audit note two minutes later recording the evidence. A person directed it, but no approval step is recorded, and this repository's own standard asks for one. If this became a routine, that approval point would need writing down, not assuming.

## Privacy Boundary

No employer, company, person or job title appears here. I haven't reproduced any record identifier, flow identifier, form name, campaign name, booking link, pipeline, internal stage name, deal value, email address or CRM link, or linked any document from the private material. The dates in the fictional export aren't the real ones, and its cast, sector and figures are invented, not disguised. The timeline above uses relative times, not the original timestamps.

## Next Evidence

The change has worked on one fictional input. The first next step this page named, running the same input against the pasteable prompt, is [now done](crm-hygiene-prompt-missing-record-test.md), and the prompt carries the step.

Two useful next steps, in order. First, build a second contact-level input where the trail is truly unclear, not clearly strong or clearly absent. A method that only separates the easy cases hasn't been tested on the one that matters. Second, log the next real missing-record case against the changed method as it happens, so that for once the method runs before I know the answer.
