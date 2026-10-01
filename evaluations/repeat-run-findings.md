# Repeat-Run Findings

I ran three of the scored tests here a second time, in fresh runs that saw only the input, and scored them against the same rubric. This page records what happened.

> A later, larger test sits alongside this one: [the business case check requirement test](business-case-check-requirement-test.md) ran the same scenario six times, three on each side of a one-line change, and used the result to reject a claim I'd already published. It's a better example of what repeat runs are for.

This page also corrects something. [Comparison With Similar Projects](../COMPARISON.md) said that no fictional test here had ever been run twice. That was wrong when I published it. The [ambiguous objection stability test](hartwell-objection-ambiguous-test.md) had already run the same input nine times, three on each of three models. Neither the evidence matrix nor the comparison page linked it, so I claimed something was missing that was sitting in this folder. Its results matter for reading mine, so I set them out first.

## Result

| Test | Published | Repeat | Change |
| --- | ---: | ---: | --- |
| [Chase decision](hartwell-chase-review.md) | 48/50 | 48/50 | Held exactly |
| [CRM hygiene review](fictional-crm-hygiene-review-eval.md) | 46/50 | 49/50 | Up 3 |
| [Post-call evidence](hartwell-post-call-review.md) | 48/50 | 50/50 | Up 2 |

None of the three went down. That means less than it sounds, and the next section says why.

## The Nine-Run Test That Already Existed

The [ambiguous objection stability test](hartwell-objection-ambiguous-test.md) tells you more about variation than this page does. It ran one deliberately ambiguous objection from scratch, three times on each of three models:

| Model | Scores | Primary driver diagnosed |
| --- | --- | --- |
| Claude | 48, 49, 46 | A different one in each of the three runs |
| ChatGPT | 47, 47, 47 | The same one all three times |
| Gemini | 45, 45, 46 | The same one all three times |

Two things follow for my three repeats.

**Claude's scores on this rubric vary by about three points.** Forty-six to forty-nine, on the same input, with nothing changed. So the three-point rise I found sits inside a range already measured. I shouldn't call it a finding without saying so.

**The score is the less interesting half.** Claude put a different primary driver first in each run, while scoring within three points every time. A steady total can hide a shifting judgement. That's what a repeat run is for, and a single score never shows it.

## Why Two Scores Went Up, and What That Might Mean

The two that went up weren't marked down for weak methods. They were marked down for mistakes I made while writing the worked example, and the reviews say so.

The [CRM hygiene review](fictional-crm-hygiene-review-eval.md) records that its first draft found only two of the four rows with a blank contact, and counted a departed contact as a missing one. It also carried a wrong close date that I only caught later, while building the weekly operating review. The published 46 keeps those corrections as a permanent deduction.

The fresh run made none of those mistakes. It listed all four blank-contact rows first time, kept the departed contact apart from the blank ones, and got all eight of its day counts right. I checked them.

That suggests **a published score can measure how I wrote the example rather than the method.** A worked example written by hand, corrected twice, then scored, is different from a clean run of the same instruction on the same input. The first records how I built the example. The second is closer to what a reader would get.

I believe that explanation because the review's own text records the corrections. But the nine-run test means these numbers can't prove it. A three-point rise is inside Claude's normal range on this rubric, so my drafting history and ordinary variation predict the same result, and this test can't tell them apart. Both readings stand.

The direction isn't in doubt. None of the three went down, and the two that rose are the two whose reviews record errors I made while writing.

## What the Repeat Runs Got Right

The three fresh runs caught every trap in their inputs.

**Chase decision.** It declined to chase on a CRM task set before the automatic reply. It treated the out of office as the reason for the silence, not as lost interest. It refused to switch to Priya, because an out of office doesn't say a contact is the wrong route. And it showed the clash between the promised Thursday transcript and the leave dates, rather than calling the transcript overdue.

I've since changed that scenario to name its weekdays, so the Thursday clash can now be checked rather than inferred. Both runs above were scored against the version without them. **I read "showed the conflict" more loosely here than a later test did.** The published output says the later leave dates "suggest" the Thursday timing doesn't stand, under a heading of things to confirm. A [twelve-run test](chase-skill-ledger-test.md) that counted only stated facts scored the published skill zero of six. Both records are accurate about what they measured.

**CRM hygiene review.** It rated the Hartwell duplicate as confident, because of a shared contact, and the Fenmoor/Fenmore pair as uncertain, with nothing to confirm it. It refused to merge on a name. It kept the departed contact apart from the blanks and named the records with nothing wrong in their structure. It raised, then dismissed, a false duplicate based on the word "Analytics" alone. It also stayed out of judging whether stages were accurate and pointed to the pipeline evidence review for that, which is the line the skill should hold.

**Post-call evidence.** It labelled the fifteen-to-thirty-minute admin figure as the customer's own unmeasured estimate. Then it flagged it in its human-check list as the number most likely to harden quietly into a fact. It recorded the proposed Tuesday meeting as not agreed and kept the transcript commitment conditional. It marked one stakeholder's involvement as an inference. It refused to guess why sharing the transcript needed an internal check, saying not to assume it is a data protection, legal or consent question.

## Where Each Repeat Run Lost Marks

### Chase decision

**Score: 48 out of 50**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every date, the leave window, the team size and the task timing are used correctly |
| Evidence fidelity | 5 | Keeps the transcript's conditions and the automatic reply's wording |
| Fact separation | 5 | Offers the reason for the silence as the most likely explanation, not as fact |
| Missing information | 4 | Doesn't note that no review time was ever confirmed, though two were offered on the 7th |
| Commercial usefulness | 5 | A decision, the reasoning, a held draft and the conditions that would change it |
| Next step clarity | 5 | Owner and timing clear throughout, including landing the message on the 21st rather than the 20th |
| Tone | 5 | Plain, no opening pleasantry, no reference to the unanswered message |
| Privacy | 5 | Nothing sensitive or irrelevant |
| Approval discipline | 5 | Holds the draft, and leaves the CRM date change for a person |
| Hallucination risk | 4 | Offers a version of the test that runs on a transcript the prospect redacts themselves, which isn't an established capability |

### CRM hygiene review

**Score: 49 out of 50**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | All eight day counts are correct, checked against the snapshot date |
| Evidence fidelity | 5 | Keeps confident and uncertain duplicates rated differently, and keeps the departed contact distinct |
| Fact separation | 4 | Sets a sixty-day staleness threshold, then lists two records at 43 and 33 days in the stale table. The reason is sound, a close date already passed, but they aren't stale by its own definition |
| Missing information | 5 | Finds every blank field, including the record with no owner and the one that can't be assessed at all |
| Commercial usefulness | 5 | Names the three ways a total taken from this export would be wrong |
| Next step clarity | 5 | Numbered actions, each with the named owner who has to do it |
| Tone | 5 | Matter-of-fact, no blame about whose records these are |
| Privacy | 5 | Fictional throughout, nothing sensitive |
| Approval discipline | 5 | Says plainly that nothing has been merged, deleted, archived, reassigned or edited |
| Hallucination risk | 5 | Labels the staleness threshold it sets as illustrative, not a rule |

### Post-call evidence

**Score: 50 out of 50**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Call length, team size, CRM, roles and the admin estimate all match the transcript |
| Evidence fidelity | 5 | Keeps the customer's "usually" hedge intact |
| Fact separation | 5 | Labels every finding confirmed, estimate, inference or unknown |
| Missing information | 5 | Names the test's own success criteria as unknown and the largest gap, which the transcript does leave open |
| Commercial usefulness | 5 | Suggests asking what result would count as success, which costs one sentence and closes that gap |
| Next step clarity | 5 | A commitments table with owner, timing and condition for each |
| Tone | 5 | Clinical, which suits an evidence pack |
| Privacy | 5 | Nothing beyond what the call supplied |
| Approval discipline | 5 | Marks the CRM summary as a draft not to be written automatically |
| Hallucination risk | 5 | Refuses to guess the reason for the internal sharing check |

A clean fifty doesn't mean the output is perfect. It means I found nothing in it that the rubric's ten areas ask about, and I wrote the rubric.

## A Problem With Repeating These Tests At All

The published inputs aren't clean test material. Two of the three have a section headed "Deliberate Test Points" that names, in order, every trap in the scenario.

That helps a reader see what the example is for. It also means anyone who repeats one of these tests by pasting the published input is sitting an open-book exam. They'll get a better result than the original run for reasons that have nothing to do with the method.

For these three runs I removed that section, and any line saying the file exists to test a skill, before the input went anywhere. Each run got the skill instruction and the scenario only.

All twenty-four inputs with an answer key now have a line above it telling you to stop copying there. A check makes sure that warning stays, above the key, so a file can't quietly lose it. That fixes it for the next person. It doesn't change the three runs here, which I stripped by hand.

## Method

Three runs, each in a fresh context, each given the skill file as a reader would paste it plus the stripped scenario. No run saw the rubric, the published score, the test points, or any sign that this was a test or a comparison.

All three used Claude Opus 5. The published examples I compared them with were made earlier, by hand, and I corrected them while writing. That difference is what this page is mostly about.

The outputs had em dashes, en dashes and currency symbols that this repository's style rules exclude. That's formatting, not scoring, and the rubric doesn't ask about it. But a raw run needs cleaning before it can be published here.

The usual limit applies: I designed the scenarios, wrote the rubric, ran the repeats and scored them. One repeat of each of three tests doesn't measure variation, and the nine-run test above is better evidence on that. This rules out only the chance that these three published scores were wild.

## What Would Make This Worth More

Repeating a test the same way again adds very little now. Two things would add a lot:

- Somebody else scoring these three fresh outputs against the same rubric, without seeing my scores. That's the gap named in [Evidence Status](../EVIDENCE-STATUS.md). It's the only way to tell whether a 49 and a 46 differ because the outputs differ or because I scored them on different days.
- Rescoring the published worked examples as they stand now, apart from how they were written. If the CRM example scores 46 because of two drafting errors I later fixed, the current file may deserve a different number.
