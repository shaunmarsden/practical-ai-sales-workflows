# Repeat-Run Findings

Three of the scored tests in this repository were run again, blind, and scored against the same rubric. This page records what happened.

It also corrects something. [Comparison With Similar Projects](../COMPARISON.md) said, in my name, that no fictional test here had ever been run twice. That was wrong when I published it. The [ambiguous objection stability test](hartwell-objection-ambiguous-test.md) had already run the same input nine times, three each across three models, and neither the evidence matrix nor the comparison page linked it, which is how I came to assert an absence that was sitting in this folder. Its results matter for reading mine, so they are set out below before my own.

## Result

| Test | Published | Repeat | Change |
| --- | ---: | ---: | --- |
| [Chase decision](hartwell-chase-review.md) | 48/50 | 48/50 | Held exactly |
| [CRM hygiene review](fictional-crm-hygiene-review-eval.md) | 46/50 | 49/50 | Up 3 |
| [Post-call evidence](hartwell-post-call-review.md) | 48/50 | 50/50 | Up 2 |

None of the three went down. That is a weaker claim than it sounds, and the next section explains why.

## The Nine-Run Test That Already Existed

The [ambiguous objection stability test](hartwell-objection-ambiguous-test.md) is a better variance study than this page is. It ran one deliberately ambiguous objection cold, three times each on three models:

| Model | Scores | Primary driver diagnosed |
| --- | --- | --- |
| Claude | 48, 49, 46 | A different one in each of the three runs |
| ChatGPT | 47, 47, 47 | The same one all three times |
| Gemini | 45, 45, 46 | The same one all three times |

Two things follow from it that bear directly on my three repeats.

**Claude's spread on this rubric is about three points.** Forty-six to forty-nine, on identical input, with nothing changed. So the three-point rise I found below sits inside a band that was already measured. I should not read it as a finding without saying that.

**The score is the less interesting half.** Claude promoted a different primary driver to first place in each run while scoring within three points every time. A stable total can hide an unstable judgement, which is the sort of thing a repeat run is actually for and a single score never shows.

## Why Two Scores Went Up, and What That Might Mean

The two that improved were not docked for weaknesses in the method. They were docked for mistakes made while writing the worked example, and the reviews say so in their own words.

The [CRM hygiene review](fictional-crm-hygiene-review-eval.md) records that its first draft undercounted the blank-contact rows, missing two of four, and miscounted a departed contact as a missing one. It also inherited a wrong close date that was only caught later, while building the weekly operating review. The published 46 carries those corrections as a permanent deduction.

The fresh run made none of those mistakes. It listed all four blank-contact rows first time, kept the departed contact separate from the blank ones, and got all eight of its day-count calculations right, which I checked.

That suggests **a published score can be measuring the authoring process rather than the method.** A worked example written by hand, corrected twice, then scored, is a different object from a clean run of the same instruction on the same input. The first records how the example was built. The second is closer to what a reader would actually get.

I believe that explanation because the corrections are documented in the review's own text rather than inferred. But the nine-run test above means I cannot claim it from these numbers alone: a three-point rise is inside Claude's measured spread on this rubric, so drafting history and ordinary run-to-run variation predict the same result and this test cannot separate them. Both readings stay on the table.

What is not in doubt is the direction. None of the three went down, and the two that rose are the two whose published reviews record errors made during writing.

## What the Repeat Runs Got Right

The three fresh runs caught every deliberate trap in their inputs.

**Chase decision.** Declined to chase on a CRM task that predated the automatic reply, treated the out of office as a reason for silence rather than lost interest, refused to switch to Priya on the grounds that an out of office does not say a contact is the wrong route, and showed the conflict between the promised Thursday transcript and the leave dates rather than calling the transcript overdue.

**CRM hygiene review.** Graded the Hartwell duplicate as confident on a shared contact and the Fenmoor/Fenmore pair as uncertain with nothing to verify it, refused to merge on a name, kept the departed contact separate from the blanks, named the records that are structurally clean, and raised then dismissed a false duplicate on the word "Analytics" alone. It also stayed out of the stage-accuracy judgement and pointed at the pipeline evidence review for it, which is the boundary that skill is supposed to hold.

**Post-call evidence.** Labelled the fifteen-to-thirty-minute admin figure as the customer's own unmeasured estimate, then flagged it in its human-check list as the number most likely to get quietly hardened into a fact. Recorded the proposed Tuesday meeting as not agreed. Kept the transcript commitment conditional. Marked one stakeholder's involvement as an inference. Refused to guess why an internal check on sharing the transcript was needed, saying not to assume it is a data protection, legal or consent question.

## Where Each Repeat Run Lost Marks

### Chase decision

**Score: 48 out of 50**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every date, the leave window, the team size and the task timing are used correctly |
| Evidence fidelity | 5 | The transcript's conditionality and the automatic reply's wording are both preserved |
| Fact separation | 5 | The reason for the silence is offered as the most likely explanation, not as fact |
| Missing information | 4 | Does not note that no review time was ever confirmed, though two were offered on the 7th |
| Commercial usefulness | 5 | A decision, the reasoning, a held draft and the conditions that would change it |
| Next step clarity | 5 | Owner and timing explicit throughout, including landing the message on the 21st rather than the 20th |
| Tone | 5 | Plain, no opening pleasantry, no reference to the unanswered message |
| Privacy | 5 | Nothing sensitive or irrelevant |
| Approval discipline | 5 | The draft is held, and the CRM date change is left for a person |
| Hallucination risk | 4 | Offers a version of the test that runs on a transcript the prospect redacts themselves, which is not an established capability |

### CRM hygiene review

**Score: 49 out of 50**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | All eight day-count calculations are correct, checked against the snapshot date |
| Evidence fidelity | 5 | Confident and uncertain duplicates stay graded differently, and the departed contact keeps its distinction |
| Fact separation | 4 | Declares a sixty-day staleness threshold, then lists two records at 43 and 33 days inside the stale table. The reason given is sound, an already-passed close date, but they are not stale by its own definition |
| Missing information | 5 | Every blank field found, including the record with no owner and the one that cannot be assessed at all |
| Commercial usefulness | 5 | Names the three specific ways a total taken from this export would be wrong |
| Next step clarity | 5 | Numbered actions, each with the named owner who has to do it |
| Tone | 5 | Matter-of-fact, no accusation about whose records these are |
| Privacy | 5 | Fictional throughout, nothing sensitive |
| Approval discipline | 5 | States plainly that nothing has been merged, deleted, archived, reassigned or edited |
| Hallucination risk | 5 | The staleness threshold it introduces is explicitly labelled illustrative rather than a rule |

### Post-call evidence

**Score: 50 out of 50**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Call length, team size, CRM, roles and the admin estimate all match the transcript |
| Evidence fidelity | 5 | The customer's "usually" hedge is carried through with the hedge intact |
| Fact separation | 5 | Uses explicit confirmed, estimate, inference and unknown labels on every finding |
| Missing information | 5 | Names the test's own success criteria as an unknown and the largest gap, which the transcript does leave open |
| Commercial usefulness | 5 | Suggests asking what result would count as success, which costs one sentence and closes that gap |
| Next step clarity | 5 | A commitments table with owner, timing and condition for each |
| Tone | 5 | Clinical, which suits an evidence pack |
| Privacy | 5 | Nothing beyond what the call supplied |
| Approval discipline | 5 | The CRM summary is marked as a draft not to be written automatically |
| Hallucination risk | 5 | Refuses to guess the reason for the internal sharing check rather than assuming one |

A clean fifty is not a claim that the output is perfect. It is a claim that I found nothing in it that the rubric's ten areas ask about, scored by the same person who wrote the rubric.

## A Problem With Repeating These Tests At All

The published inputs are not clean test material. Two of the three carry a section headed "Deliberate Test Points" that names, in order, every trap the scenario contains.

That is useful for a reader trying to understand what the example is for. It also means anybody who repeats one of these tests by pasting the published input is running an open-book exam, and will get a better result than the original run did for reasons that have nothing to do with the method.

For these three runs I removed that section, and any line stating that the file exists to test a skill, before the input went anywhere. The runner received the skill instruction and the scenario only.

All twenty-four inputs that carry an answer key now say so directly, in a line above it telling you to stop copying there. A check keeps that warning present and keeps it above the key, so a file cannot quietly lose it. That is the fix for the next person; it does not change the three runs recorded here, which were stripped by hand.

## Method

Three runs, each in a fresh isolated context, each given the skill file exactly as a reader would paste it plus the stripped scenario. No runner received the rubric, the published score, the deliberate test points, or any indication that this was a test or a comparison.

All three used Claude Opus 5. The published examples they are compared against were produced earlier, by hand, with the author correcting them during writing, which is the difference this page is mostly about.

The outputs contained em dashes, en dashes and currency symbols that this repository's own style rules exclude. That is a formatting matter rather than a scoring one, and the rubric does not ask about it, but it is worth knowing that a raw run needs cleaning before it could be published here.

Same limitation as everywhere else: one person designed the scenarios, wrote the rubric, ran the repeats and scored them. One repeat of each of three tests is not a variance study, and the nine-run test above is the better piece of evidence on that question. This rules out nothing except the possibility that these three published scores were wild.

## What Would Make This Worth More

Repeating a test the same way again adds very little now. Two things would add a lot:

- **Somebody else scoring these three fresh outputs** against the same rubric, without seeing my scores. That is the gap named in [Evidence Status](../EVIDENCE-STATUS.md) and it is the only thing that would tell me whether a 49 and a 46 differ because the outputs differ or because I scored them on different days.
- **Rescoring the published worked examples as they now stand**, separately from the authoring history. If the CRM example scores 46 because of two drafting errors that were then fixed, the current file may deserve a different number than the one on it.
