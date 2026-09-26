# Pick the Right Proof Point: A Workflow That Did Not Earn Its Place

## Status

**Negative result. No workflow, skill or recipe card was added.** A candidate sales job was reviewed for overlap, judged genuinely distinct, given a drafted method, and tested against a plain instruction. The plain instruction did the job just as well on every measure registered in advance, so the method was not published. This page is the record of that, since a candidate rejected on evidence is worth more to a reader than a candidate quietly dropped.

## The Job, and Why It Looked Distinct

The sales job: you have several proof points, case studies or past results, and you need to decide which one, if any, to use with a particular buyer, and what you are actually entitled to claim from it.

The overlap review found nothing in this repository that does it. Four assets consume a proof point without choosing one: [Review a Lost Opportunity](../workflows/04-lost-opportunity-review.md) flags a proof point as reusable, the [chase skill](../.agents/skills/plan-chase-sequence/SKILL.md) names a case study as something to add before chasing, the [Sales Copilot guide](../guides/build-an-approval-gated-sales-copilot.md) has its fictional copilot use one correctly, and [Champion Enablement](../.agents/skills/champion-enablement/SKILL.md) routes this deal's evidence to the right stakeholder.

The nearest thing to a selection method is the [business case skill](../.agents/skills/build-business-case/SKILL.md), which classifies evidence as confirmed, inference or unknown. That is about the buyer's own situation, sourced from the current call. It has no concept of another customer's result, no permission-to-share axis and no similarity judgement, so it does not cover this.

The [workflow router](../.agents/skills/workflow-router/SKILL.md) has no route for it either, while the Sales Copilot's own fictional environment lists "Select an Approved Proof Point" as an available specialist route. The repository had already imagined the job without building it.

So the job is distinct. That turned out not to be the question that mattered.

## What Was Tested

A method was drafted to the eight factors the job seems to need: problem similarity, context similarity, whether a result was measured or estimated, whether causation is supported, whether the evidence may be shared, whether using it needs extrapolation, whether it answers the buyer's actual concern, and whether the honest answer is that nothing fits. The full text is in the appendix.

The baseline was not an empty prompt. It was the instruction a competent seller would actually type:

> You are helping a salesperson choose a proof point. Read the buyer brief and proof library below and answer the question at the end. Be careful not to overclaim.

Twelve runs, six a side, each in a fresh isolated context given only its instruction and the scenario, told to read nothing else. Criteria, the falsification condition and the void conditions were written before the method was drafted and before any run. Scoring was blind: all twelve outputs were copied to neutrally named files under a mapping that was not opened until every run had been scored.

## The Scenario

Fictional throughout. Dominic Achebe, Head of Field Operations at Vantry Water, a regional water utility with 140 field engineers. His engineers finish a job on a handheld app and re-key the completion notes into the asset management system afterwards, which he estimates at six hours a week each but has never measured. His director wants the integration cost justified, and separately wants to know whether the change reduces errors in the asset records, which Dominic says he cares about more than the hours. He was explicit on the call: "Every vendor shows me a number from someone else's business. My jobs vary more than a typical site. I want to know what actually transfers."

The library holds seven entries, each carrying a trap stated as a neutral fact rather than flagged:

| Entry | What makes it wrong, or right |
| --- | --- |
| Kelbrook Water | Same sector, measured, approved. Contact centre handling time after a billing consolidation, which is not the buyer's problem |
| Orrindale Energy | A projected 840,000 pounds, built by pre-sales from assumed headcount and salary, never measured in the nineteen months since go-live |
| Pennhallow Facilities | The identical re-keying task, measured, a large drop. The handheld devices were also replaced in the same twelve weeks |
| Danecourt Logistics | Measured and clean, but the people were depot-based planners at fixed desks on a wired network |
| Sallowfield Water | Same sector, same task, measured on 110 engineers, no other changes, and the only entry touching the error question. Shared under NDA, not approved for external use, not to be described even without the name |
| Braylock Gas | A warm quotation, approved, with no measurement behind it |
| Halewood Water | Same sector, same task, same role, measured by timesheet code, nothing else changed, approved. A pilot of 12 engineers, with the other 95 unmeasured |

The defensible answer is the least impressive one. Halewood on the hours question, scoped to twelve engineers and not multiplied up. On the error question there is no usable proof at all, because the one entry that measured it cannot be shared.

## The Result

Every figure below was scored by reading all twelve outputs, not by pattern matching.

| Failure condition, registered in advance | Plain instruction | The method |
| --- | ---: | ---: |
| Presented an estimate as a measured result | 0 of 6 | 0 of 6 |
| Used the confidential entry externally | 0 of 6 | 0 of 6 |
| Claimed causation the source does not support | 0 of 6 | 0 of 6 |
| Extrapolated the pilot group to the organisation | 0 of 6 | 0 of 6 |
| Invented a similarity | 0 of 6 | 0 of 6 |
| Fabricated a figure, quotation or customer | 0 of 6 | 0 of 6 |
| Forced a proof point where none was suitable | 0 of 6 | 0 of 6 |

| Positive criterion, registered in advance | Plain instruction | The method |
| --- | ---: | ---: |
| Selected the defensible entry as the primary proof | 6 of 6 | 6 of 6 |
| Said the error question has no usable proof | 6 of 6 | 6 of 6 |
| Named the permission problem rather than going quiet on it | 6 of 6 | 6 of 6 |

**The falsification condition fired.** It was registered as: the plain instruction scoring zero or one failures across its six runs falsifies the case for the workflow. It scored zero. Every plain-instruction run reached the same answer, refused the confidential entry even unnamed, rejected the confounded entry on the device replacement, declined to scale twelve engineers to a hundred and forty, and named the gap on the error question.

## The One Difference, Reported Honestly

Every run of the method told the seller to confirm the sharing permission was still current before sending, and to stand behind the claim in its final written form. No plain-instruction run did. That is six of six against none of six, on a real point: a proof library goes stale, and permission granted last year may not hold today.

It was not a registered criterion. It is an observation from reading, not a measured claim, and it arrived after the registered criteria came out level, which is precisely when the person who wrote the method is most motivated to find something. It is worth one sentence in a guide. It is not worth a workflow, a skill, a recipe card, a prompt, two example files, an evaluation, a matrix row and the nine prose counts elsewhere in the repository that adding a job would make stale.

## Two Defects Seen in Passing

Neither is a registered failure, and both are recorded because they happened.

One run of the method gave the wrong denominator twice, writing "12 of 95 engineers" and "Halewood's full 95-engineer workforce". The scenario says twelve in the pilot and ninety-five not included, so the total is a hundred and seven, which three other runs derived correctly. That is a misreading of the source rather than an invented number.

One plain-instruction run offered a hypothesis line for the error question, framed explicitly as a hypothesis with no measured evidence behind it. That is not forcing a proof point, but it is the closest any run came to softening a gap it had correctly identified.

## What This Does Not Show

- It does not show the job is not real. It shows this method did not beat a plain instruction on this scenario.
- **The scenario may be too easy.** Every trap is visible in the library text, and a careful reader can see each one without any method at all. A harder version would bury the permission line in a longer entry, or make two candidates genuinely close so the choice is a judgement rather than an elimination.
- One scenario, one model, six runs a side, built and scored by the same person who wrote the method.
- It does not show that a proof-selection method could never help. It shows that this one, on this test, added nothing a plain instruction did not already produce.

## What Would Change the Answer

A scenario where the traps are not all visible on the surface. Two candidates that are genuinely close on problem and context, so the answer turns on a judgement rather than on eliminating six obvious misfits. A library long enough that a reader cannot hold every entry in mind at once, which is where a method usually starts to pay. If a harder scenario separated the two arms, the method would deserve another look. On this evidence it does not.

## Appendix: The Method That Was Tested

Not published as a skill. Reproduced so a reader can judge the comparison rather than take it on trust.

```text
Gather the inputs: what the buyer said they are concerned about, in their own
words where possible, and the candidate proof points with whatever the record
holds about each.

Start from the buyer's concern. Write down what the buyer is worried about
before looking at the library. If they raised more than one concern, take each
separately. Choosing first and justifying afterwards is the failure this step
exists to prevent.

Separate what was measured from what was estimated. For each candidate say
plainly which it is: measured before and after by a stated method, estimated or
modelled from assumptions, reported without measurement, or qualitative only. A
modelled figure is not a result, whatever its size.

Check whether the result is attributable. A measured change is evidence for your
product only if nothing else plausible changed at the same time.

Check what you are allowed to share. Confidential or unapproved material stays
internal, and that covers describing the result without naming the customer.

Judge the problem and the context separately. Same industry is not the same
problem. Ask separately whether the people are comparable: role, working
conditions, and anything about the setting that plausibly drove the result.

Say what the proof entitles you to claim, in the narrowest form the source
supports. Do not scale a result measured on a small group into a figure for the
buyer's whole organisation.

Be willing to return nothing. Where no candidate is close enough on problem,
context, evidence and permission, say so plainly and stop.

Guardrails: never present an estimate as measured; never use confidential
evidence externally, named or unnamed; never attribute a result where the record
shows another change in the same period; never scale beyond the group measured;
never invent a figure, quotation, customer or similarity; never choose the most
impressive candidate over the most defensible one.

Require human review: confirm the sharing permission is still current, and that
you will stand behind the claim in the form it is finally written.
```
