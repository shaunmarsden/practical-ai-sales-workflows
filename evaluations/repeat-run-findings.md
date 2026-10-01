# Repeat-Run Findings

I ran three of the scored tests here a second time, in fresh runs that saw only the input, and scored them against the same rubric. None of the three went down.

> A later, larger test shows better what repeat runs are for: [the business case check requirement test](business-case-check-requirement-test.md) used six runs to reject a claim I'd already published.

This page also corrects something. [Comparison With Similar Projects](../COMPARISON.md) said that no fictional test here had ever been run twice. That was wrong. The [ambiguous objection stability test](hartwell-objection-ambiguous-test.md) had already run the same input nine times, and neither the evidence matrix nor the comparison linked it.

## Result

| Test | Published | Repeat | Change |
| --- | ---: | ---: | --- |
| [Chase decision](hartwell-chase-review.md) | 48/50 | 48/50 | Held exactly |
| [CRM hygiene review](fictional-crm-hygiene-review-eval.md) | 46/50 | 49/50 | Up 3 |
| [Post-call evidence](hartwell-post-call-review.md) | 48/50 | 50/50 | Up 2 |

## The Nine-Run Test That Already Existed

The nine-run test ran one deliberately ambiguous objection three times on each of three models:

| Model | Scores | Primary driver diagnosed |
| --- | --- | --- |
| Claude | 48, 49, 46 | A different one in each of the three runs |
| ChatGPT | 47, 47, 47 | The same one all three times |
| Gemini | 45, 45, 46 | The same one all three times |

**Claude's scores on this rubric vary by about three points** on the same input with nothing changed, so the three-point rise I found sits inside a range already measured.

**The score is the less interesting half.** Claude put a different primary driver first in each run while scoring within three points every time. A steady total can hide a shifting judgement.

## Why Two Scores Went Up

The two that went up lost marks for mistakes I made while writing the worked example, not for weak methods.

The [CRM hygiene review](fictional-crm-hygiene-review-eval.md) records that its first draft found only two of the four rows with a blank contact, and counted a departed contact as a missing one. It also carried a wrong close date I caught later. The published 46 keeps those as a permanent deduction. The fresh run listed all four blank-contact rows first time, kept the departed contact apart, and got all eight day counts right.

So **a published score can measure how I wrote the example rather than the method.** A hand-written example, corrected twice, then scored, differs from a clean run of the same instruction, which is closer to what a reader gets.

But a three-point rise is inside Claude's normal range, so my drafting history and ordinary variation predict the same result, and this test can't tell them apart. The two that rose are the two whose reviews record my errors.

## What the Repeat Runs Got Right

The three fresh runs caught every trap in their inputs.

**Chase decision.** It declined to chase, treated the out of office as the reason for the silence, refused to switch to Priya, and showed the clash between the promised Thursday transcript and the leave dates.

I've since changed that scenario to name its weekdays. Both runs above were scored against the version without them. **I read "showed the conflict" more loosely here than a later test did.** The published output says the later leave dates "suggest" the Thursday timing doesn't stand, under a heading of things to confirm. A [twelve-run test](chase-skill-ledger-test.md) that counted only stated facts scored the published skill zero of six. Both records are accurate about what they measured.

**CRM hygiene review.** It rated the Hartwell duplicate confident and the Fenmoor/Fenmore pair uncertain, refused to merge on a name, and dismissed a false duplicate based on the word "Analytics" alone.

**Post-call evidence.** It labelled the fifteen-to-thirty-minute admin figure as the customer's own unmeasured estimate, and flagged it as the number most likely to harden quietly into a fact. It recorded the proposed Tuesday meeting as not agreed.

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

## Repeating These Tests

Two of the three published inputs have a section headed "Deliberate Test Points" that names every trap in the scenario. Anyone who pastes the published input is sitting an open-book exam.

For these three runs I removed that section, and any line saying the file exists to test a skill. All twenty-four inputs with an answer key now have a line above it telling you to stop copying there, and a check makes sure that warning stays.

## Method

Three runs, each in a fresh context, each given the skill file as a reader would paste it plus the stripped scenario. No run saw the rubric, the published score, the test points, or any sign that this was a test. All three used Claude Opus 5. The published examples I compared them with were made earlier, by hand, and I corrected them while writing.

I designed the scenarios, wrote the rubric, ran the repeats and scored them. One repeat of each of three tests doesn't measure variation, and the nine-run test is better evidence on that. This rules out only the chance that the three published scores were wild.

## What Would Make This Worth More

Repeating a test the same way again adds very little now. Two things would add a lot:

- Somebody else scoring these three fresh outputs against the same rubric, without seeing my scores. That's the gap named in [Evidence Status](../EVIDENCE-STATUS.md). It's the only way to tell whether a 49 and a 46 differ because the outputs differ or because I scored them on different days.
- Rescoring the published worked examples as they stand now. If the CRM example scores 46 because of two drafting errors I later fixed, the current file may deserve a different number.
