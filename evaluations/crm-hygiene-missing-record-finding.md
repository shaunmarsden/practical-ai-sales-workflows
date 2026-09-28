# CRM Hygiene: The Record That Should Have Existed

## Status

**Internal scope finding, plus a tested change to the method.** A real opportunity was found to have no CRM record at all, because an automation that should have created it did not. The published CRM hygiene method was never run against that case and could not have been, so this is not a real-use test of the method and is not logged as one in the evidence matrix. What it is: a real case that exposed a gap, a fair test of the published method against that gap, and one bounded change that the test justified.

## What Was Reviewed Privately

A real enquiry arrived through a paid social lead form. Within two minutes the person had booked a qualification meeting from the automated booking link. Five days later the meeting was held and attended, a short outbound call was placed two minutes into it, and a follow-up email went out forty-five minutes after it finished. There was no opportunity record for any of it.

The intake automation had started. Its first action, which runs before anything else, had written its value to the contact record and that value was still there. The action that creates the opportunity sits behind a delay, further down the same flow. Ninety seconds after the contact was created, and inside that delay, two duplicate contact records were merged into the one that survived. The opportunity was never created. The record that existed five days later, when the reconstruction was made, was the only one the contact had ever had, and it was made by hand.

Every step above was checked against the individual system records rather than taken from the note written at the time. The employer, the people, the record identifiers, the flow, the form, the campaign, the booking link, the pipeline, the value and the internal stage names are not reproduced here.

### What is verified and what is inferred

The published lesson only holds if these are kept apart.

| Claim | Status |
|---|---|
| The enquiry arrived at a recorded time through a lead form | Verified from the contact's creation date and source fields |
| The intake automation ran | Verified: its first action's value is still on the contact record |
| The meeting was booked ninety seconds later from the automated link | Verified from the meeting's creation date and the recorded conversion event |
| Two records were merged into the survivor, at a recorded time inside the delay | Verified from the merge fields, which carry the timestamp |
| The automation's opportunity-creation step sits behind a delay | Verified from the current flow definition |
| The eligibility rules would not have withheld the opportunity | Verified: every answer routes to the branch that creates one |
| No opportunity existed until it was made by hand five days later | Verified: the contact has exactly one, and its creation date is the later one |
| The meeting was attended, for about thirty-five minutes | Verified from a separate meeting-platform call record |
| A call and a follow-up email followed | Verified from the call and email records |
| **The merge is what unenrolled the automation** | **Inferred.** The unenrolment is not logged anywhere retrievable. The merge is logged, the absent opportunity is verified, and the timing fits. That is a strong reading, not a recorded fact |
| **Which of the three records the automation had enrolled** | **Not determinable.** The survivor kept the earliest creation date, so the evidence that would settle it is gone |
| The flow definition in April was the same as it is now | **Not verified.** The flow has been revised since, and no revision history is available for it |

The reconstructed opportunity then ran for ten weeks across five people on the employer side and was eventually lost. That matters for an honest reading: recovering the record did not recover a sale. The value was in the pipeline being true, not in the outcome changing.

## Why This Is Not Covered by the Existing Real-Use Finding

That job already has a logged real-use finding, about records in a live pipeline that were neither prospects nor ordinary missing-data cases. This is a different thing. A test record is a row that should not be there. This is a row that should be there and is not, and no export can contain it.

## The Test

The obvious test would be to hand the method an export with a row missing and ask what is wrong. That is a category error: the method is told to work through an export field by field, so an absence with no in-band signal fails by construction and proves nothing.

The real case's signal was not in the deal export at all. It was a contact with a booked and attended meeting, logged calls, recent correspondence, and no opportunity. The method's own stated inputs include contact and last activity, and it is told to look for what is missing, so whether that registers as missing is a genuine question about the published text.

The [fictional contact-level export](../examples/fictional-crm-contact-export.md) was built to ask it. It carries eight anomalies so the question is not the only thing in it: a confident duplicate, a near-duplicate that must not be merged on name alone, a blank owner, a complete-looking record four months stale, an early-stage record closing in four days, an obvious demo row, and two rows with no opportunity. Those last two are the point. One has the full trail an opportunity would normally follow. The other has nothing logged since the enquiry, so nothing was ever missed. A method that flags both identically is pattern-matching a blank column, not reasoning about evidence.

Six blind runs, each given only the frozen skill and the export and told to read nothing else, then six more against the changed skill. Criteria, the falsification condition and the void conditions were written before the input was built.

## What the Method Got Right

| Check | Result |
|---|---|
| Flagged the missing opportunity, unprompted, as one of eight anomalies | 6 of 6 |
| Described the second row's thin trail accurately | 6 of 6 |
| Invented no stage, value or close date for the record that was absent | 6 of 6 |
| Kept the review read-only and routed every action to a person | 6 of 6 |
| Caught all six ordinary hygiene problems as well | 6 of 6 |

The first row falsified what I expected. I had read the method as having no reach into a record that does not exist, because it is written entirely around an export of records that do. That reading was wrong about detection. Every run found it without being pointed at it.

## What the Method Got Wrong or Did Weakly

The reading survived everywhere after detection.

**It classified a record that does not exist as a field that is blank.** All six filed it under a missing-fields heading. One filed it in the same list as "Owner field is blank" and then, in its numbered actions, listed "Decide whether Brackmoor Group and Felsted Components need an Opportunity created" alongside "Fill in the Owner on the Quillfield Media record". An earlier version of this page misquoted the first of those and said the record sat directly above the blank owner; another row came between them. Those are not the same kind of act. Filling in an owner corrects a record; opening an opportunity brings one into existence.

**It never asked why, and never asked for anything outside the export.** No run mentioned an automation, a workflow, a sync or an integration, and none asked for a booking, an attendance record or correspondence to check against. An automation that failed and a person who has not got round to it are indistinguishable to the published method, and that distinction is exactly what decides whether reconstructing is right.

**Two of six gave the evidenced row and the unevidenced row the same recommendation**, in one case justified by "the engagement level already logged against them" when the engagement level is the only difference between them.

## The Change, and What It Cost

One new step in the skill and the workflow, and one guardrail line: separate a missing field from a missing record, never give the two rows the same recommendation, name the evidence outside the export, and create nothing until a person has checked it.

| Check | Published | Changed |
|---|---|---|
| Filed the absent record as an ordinary missing field | 6 of 6 | 0 of 6 |
| Distinguished the evidenced row from the unevidenced one | 6 described, 4 drew the inference | 6 of 6 |
| Gave both rows the same recommendation | 2 of 6 | 1 of 6 |
| Named evidence outside the export to check first | 0 of 6 | 6 of 6 |
| Wrongly treated the unevidenced row as a missing record | 0 of 6 | 0 of 6 |
| Still caught all six ordinary problems, duplicates still split | 6 of 6 | 6 of 6 |

Detection is not comparable between the two sets, because the changed skill names the pattern the input contains. That is why no detection claim rests on the second set; detection was already 6 of 6 with no hint at all.

One run still re-merged the two rows in its action list after separating them in its findings. The change took that from two of six to one of six. It did not remove it.

The published skill is byte-identical to the file those six runs read. The pasteable prompt was deliberately left unchanged at the time, because changing it would have been a second untested change. It has since been [tested separately](crm-hygiene-prompt-missing-record-test.md) and now carries the same step, so the recipe card and the skill no longer differ.

## What This Supports

- An absent CRM record is worth treating as a question rather than an answer, when there is a trail behind it that a record would normally follow.
- The evidence has to come from outside the record, because there is no record to read. In the real case that meant the lead form, the booking, the attendance, the call, the correspondence, and the automation's own traces.
- The burden of proof runs the other way from ordinary hygiene. Correcting a field starts from a record that is itself evidence. Creating one starts from nothing, so the standard has to be higher, not lower.
- A method can find a defect and still classify it wrongly. Detection was unanimous here and the classification was unanimously wrong, which is not a distinction a pass mark would have shown.
- Two absences can look identical in an export and mean opposite things. Separating them is the difference between correcting a pipeline and inflating one.

## What This Does Not Support

- It does not show that missing records should generally be reconstructed. One case, with an unusually rich trail and a logged merge event, does not establish a rule. A thinner trail would not have justified it.
- It does not show the method now handles this well in real use. Both sets of runs are against a fictional input. The method has still never been run against the real case.
- The causal claim is inferred, not logged. The merge is recorded and the absent opportunity is verified; the unenrolment itself is not, and the definitive evidence was destroyed by the merge.
- No commercial outcome is claimed. The recovered opportunity was eventually lost.
- It is not an independent external user test. Nobody outside this project has scored any of it.
- The new step only bites when the export carries the activity that sits behind a record. The method's stated inputs do not ask for booking, attendance or call columns, so a deal-level export will not trigger it at all. That is a limit of the change, not a quiet success.
- The real write was made in a live CRM through an integration, with an audit note recording the evidence two minutes later. A person directed it, but no explicit approval step is recorded, and the repository's own standard asks for one. If this became a routine, that approval point would have to be written down rather than assumed.

## Privacy Boundary

No employer, company, person or job title appears here. No record identifier, flow identifier, form name, campaign name, booking link, pipeline, internal stage name, deal value, email address or CRM link is reproduced, and no document referenced in the private material is linked. The dates in the fictional export are not the real ones, and its cast, sector and figures are invented rather than disguised. The verified timeline above is described in relative terms, not with the original timestamps.

## Next Evidence

The change is proved on one fictional input. Running the same input against the pasteable prompt, the first next step this page named, has [since been done](crm-hygiene-prompt-missing-record-test.md), and the prompt now carries the step. The useful next steps, in order: build a second contact-level input where the trail is genuinely ambiguous rather than clearly strong or clearly absent, since a method that only separates the easy cases has not been tested on the one that matters; and log the next real missing-record case against the changed method, prospectively, so that for once the method is run before the answer is known.
