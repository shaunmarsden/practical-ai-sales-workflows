# CRM Hygiene: The Record That Should Have Existed

## Status

**A real gap, and a tested change to the method.** A real opportunity had no CRM record, because an automation that should have created it didn't. I never ran the published CRM hygiene method on that case, so this isn't a real-use test and the evidence matrix doesn't log it as one. It's a real case that showed a gap, a test of the method against it, and one small change the test supported.

## What Was Reviewed Privately

A real enquiry came in through a paid social lead form. Within two minutes the person booked a qualification meeting through the automated link. Five days later they attended. A short outbound call went out two minutes into the meeting, and a follow-up email 45 minutes after it ended. None of it had an opportunity record.

The intake automation had started. The step that creates the opportunity sits further down the same flow, behind a delay. Ninety seconds after the contact was created, inside that delay, two duplicate contact records were merged into the one that survived. The opportunity was never created. The only one the contact ever had was made by hand five days later.

I checked every step against the individual system records, not the note written at the time.

### What is verified and what is inferred

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

## The Test

The job's logged real-use finding is about test records, rows that shouldn't be there. This is a row that should be there and isn't, and no export can contain it.

Giving the method an export with a row missing would be unfair. It works through an export field by field, so a gap with no trace in the export is bound to be missed.

In the real case, the sign was a contact with a booked and attended meeting, logged calls, recent emails, and no opportunity. The method's inputs include contact and last activity, and it's told to look for what's missing. So whether it spots this is a fair question.

I built a [fictional contact-level export](../examples/fictional-crm-contact-export.md) to ask it. It carries eight problems: a clear duplicate, a near-duplicate that mustn't be merged on name alone, a blank owner, a complete-looking record four months stale, an early-stage record closing in four days, an obvious demo row, and two rows with no opportunity. Those last two are the point. One has the full trail an opportunity would follow. The other has nothing logged since the enquiry, so nothing was missed. A method that flags both the same way is reacting to a blank column, not weighing evidence.

I ran the published skill six times, then the changed skill six times. Each run saw only the skill and the export. Before I built the input, I wrote down what would count as a pass, a failure and a void run.

## What the Method Got Right

| Check | Result |
|---|---|
| Flagged the missing opportunity, unprompted, as one of eight problems | 6 of 6 |
| Described the second row's thin trail correctly | 6 of 6 |
| Made up no stage, value or close date for the missing record | 6 of 6 |
| Kept the review read-only and left every action to a person | 6 of 6 |
| Also caught all six ordinary hygiene problems | 6 of 6 |

I'd assumed the method couldn't reach a record that doesn't exist. Every run found it unprompted.

## What the Method Got Wrong or Did Weakly

**It treated a missing record as a blank field.** All six filed it as a missing field. One listed "Decide whether Brackmoor Group and Felsted Components need an Opportunity created" next to "Fill in the Owner on the Quillfield Media record". Filling in an owner corrects a record. Opening an opportunity creates one.

**It never asked why, or for anything outside the export.** No run mentioned an automation, workflow, sync or integration, or asked for a booking, attendance record or emails to check. To the published method, a failed automation and a person who hasn't got round to it look the same, and that difference decides whether rebuilding is right.

**Two of six gave the row with evidence and the row without it the same recommendation.** One justified this by "the engagement level already logged against them", when engagement is the only difference between them.

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

The two sets can't be compared on finding the gap, because the changed skill names the pattern the input contains. The published skill had already found it 6 of 6 with no hint.

One run still merged the two rows in its action list after separating them in its findings. The change took that from two of six to one of six. It didn't remove it.

I left the pasteable prompt alone at the time, as changing it would have been a second untested change. I've since [tested it separately](crm-hygiene-prompt-missing-record-test.md), and it now carries the same step.

## What This Supports

- A missing CRM record is a question, not an answer, when a trail behind it would normally lead to one. The evidence has to come from outside the record: here the lead form, booking, attendance, call, emails and the automation's own traces.
- Creating a record needs a higher bar than correcting a field. A field correction starts from a record, which is evidence. Creating one starts from nothing.

## What This Does Not Support

- One case, with an unusually full trail and a logged merge, doesn't show that missing records should generally be rebuilt. A thinner trail wouldn't have justified it.
- Both sets of runs used a fictional input, I've never run the method on the real case, and nobody outside this project has scored any of it.
- The cause is inferred, as the table says.
- The rebuilt opportunity ran for 10 weeks across five people on the employer side and was lost. Getting the record back didn't get the sale back. I claim no commercial outcome.
- The new step only works when the export carries the activity behind a record. The method doesn't ask for booking, attendance or call columns, so a deal-level export won't trigger it.
- The real record was created in a live CRM through an integration, with an audit note two minutes later recording the evidence. A person directed it, but no approval step is recorded, and this repository's standard asks for one.

## Privacy Boundary

No employer, company, person or job title appears here, and no record identifier, flow, form, campaign, booking link, pipeline, stage name, deal value, email address or CRM link. I've linked nothing from the private material. The fictional export's dates, cast, sector and figures are invented, not disguised. The timeline uses relative times.

## Next Evidence

Next, build a second contact-level input where the trail is truly unclear, not clearly strong or clearly absent, since a method that only separates easy cases hasn't met the hard one. Then log the next real missing-record case against the changed method as it happens, so the method runs before I know the answer.

## Corrections

An earlier version of this page misquoted the action about Brackmoor Group and Felsted Components, and said the record sat directly above the blank owner. Another row came between them.
