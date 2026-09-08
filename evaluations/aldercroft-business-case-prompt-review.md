# Aldercroft Business Case Prompt Review

> **Correction.** This review argued that the prompt's required human-check section was the most likely reason it caught a gap the skill missed. That was [tested over six runs](business-case-check-requirement-test.md) and rejected. Two of three fresh runs of the unmodified skill caught the same gap, so the published skill record's miss was inside its own variation, and all three produced a check section without being told to. The section was never the variable. The section below headed "Why This Scored Higher Than the Skill" is wrong on that point and is corrected there.

This review scores the [worked business case](../examples/aldercroft-business-case-prompt-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests the [business case prompt](../templates/business-case-prompt.md), which is a different artefact from the [Build a Business Case skill](../.agents/skills/build-business-case/SKILL.md) scored in the [Aldercroft business case review](aldercroft-business-case-review.md). The prompt is condensed from the skill, so neither score is evidence for the other.

The prompt exists because the [Build a Business Case recipe card](../recipes/build-a-business-case.md) had nothing to paste. It was the last of the seventeen cards in that position.

Aldercroft was chosen because it is the hardest of the three business case scenarios here: the case has to be built entirely from pre-pilot projections, with an unmeasured time estimate, an approximate blended hourly rate, an unconfirmed future headcount the champion explicitly asked to be excluded, and an out-of-scope aside.

## Method Note

The prompt was pasted into a fresh, isolated context with only the [transcript](../examples/aldercroft-business-case-transcript.md) below it, and the transcript's answer key was removed first, as its own warning instructs. The run did not know it was a test, did not see the rubric, and had no access to this repository.

**Order of work, because it affects how much weight the total carries.** I wrote the prompt from the skill file, ran the test, and only then read the skill's own Aldercroft review to score consistently against it. The prompt was not written to dodge the weaknesses that review names. One difference between the two artefacts is mine, though, and it matters: see the section on it below.

## Result

**Score: 49 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The six-hour estimate, the thirty-five-pound blended rate, the twelve-person headcount, the audit-trail requirement and the pilot-not-rollout ask all match the transcript exactly |
| Evidence fidelity | 5 | Every one of the transcript's conditions survives, including the two most likely to be flattened: the rate stays an approximate planning average and the five unconfirmed analysts stay out of every figure |
| Fact separation | 5 | A status column labels each summary item, and the six-hour estimate is re-flagged as unmeasured at the point the arithmetic uses it, not only where it is introduced |
| Missing information | 5 | Names the absent pilot cost, the undefined measurement period, the missing resourcing figure and the fact that no solution name was ever established, which the transcript does not prompt for |
| Commercial usefulness | 5 | Correctly sizes the ask to a paid pilot with a measurement period, exactly what the champion asked for, and gives the reader the two component figures without welding them into one |
| Next step clarity | 4 | Names Priya as the approver and is explicit that sending does not finish the process, but nobody is named as owning the job of agreeing the pilot's length and measures |
| Tone | 5 | Third person throughout, correctly, because the reader is the CFO rather than the person on the call. Hedged in proportion to genuinely low-confidence material without reading as evasive |
| Privacy | 5 | No individual analyst named, no customer personal data, and the out-of-scope accounts payable aside is kept out of the case itself |
| Approval discipline | 5 | States plainly that this remains a draft for the champion's review, leaves the commercial section as a marked placeholder rather than filling it, and treats nothing as sent or agreed |
| Hallucination risk | 5 | Invents nothing, including a product name it correctly reports was never established, and declines to multiply two unmeasured inputs into a single headline saving |

## Why This Scored Higher Than the Skill, and Why That Is Not a Result

The skill scored 46 on this same scenario. Three of its four lost marks are the three this run did not lose:

| Area | Skill's run | This run |
| --- | --- | --- |
| Fact separation | 4, the six-hour estimate was a stable base for the maths without being re-flagged there | 5, re-flagged at the arithmetic |
| Missing information | 4, no pilot cost figure exists and the document did not say so | 5, flagged with a marked placeholder and a check item |
| Hallucination risk | 4, two unmeasured inputs stacked into a confident-looking annual figure | 5, no combined figure produced at all |
| Next step clarity | 4, nobody named as owning the pilot scope decision | 4, the same gap |

**A three point gap is not evidence the prompt is better than the skill.** This repository has measured identical prompts on identical inputs moving by one to three points between runs, and a [nine-run test](hartwell-objection-ambiguous-test.md) in which the same model reached a different primary diagnosis each time. One run of each artefact on one scenario cannot separate a real difference from that.

**I thought one of the three was my own design choice rather than the model's judgement,** because the skill lists eight things a document must contain and a human-review section was not among them, while my prompt makes it a numbered, required section. I wrote that this was the most likely reason the pilot-cost gap got caught here and not there, and that it was testable by adding the same requirement to the skill.

**It was tested, over [six blind runs](business-case-check-requirement-test.md), and it was wrong.** Two of three fresh runs of the unmodified skill named the absent pilot cost, so the published record's miss was inside the skill's own variation rather than caused by a missing instruction. All three unmodified runs also produced a human-check section unprompted, so the section was never the variable; what varies is what goes into it.

What that leaves is the honest and duller reading: **three points between one run of each artefact, on one scenario, is not separable from noise, and I do not have an explanation for it that survived testing.**

## What Worked

- It kept the projection honest in both directions. The conservative "half" stayed the anchor, the more flattering "maybe more" never became the headline, and the whole document is framed as the reason to run a pilot rather than a promise of a result.
- It refused to pad. Asked for three applied examples, it produced one grounded in the only manual task the call establishes in depth, said plainly why the other two are absent, and flagged the missing detail rather than writing two paragraphs that would read the same in any other prospect's document. That is what the prompt's own instruction about generic examples is for, and it is also the place a second scorer is most likely to disagree with me: marking it down as failing to deliver a requested section would be defensible.
- It caught something the answer key does not list. No solution or product name was ever established on the call, and the document says so rather than quietly naming one.
- The commercial section is an empty marked placeholder with an instruction not to fill it from internal pricing. On a document heading for a CFO that is the right kind of blank.

## What Needed Checking

- Nobody owns agreeing the pilot's length and measures. The document says it must happen before the pilot starts and leaves it there.
- Neither this run nor the skill's run produced the three applied examples both artefacts ask for. The skill's review did not flag that, and it should have. That is a gap in my earlier scoring rather than in either output.
- The out-of-scope accounts payable aside appears in the check list, as a confirmation that it has been kept out. The case itself is clean, and the skill's run did the same thing and scored 5, so this is consistent rather than lenient, but a document forwarded without its check list stripped would carry that line.

## What This Test Cannot Prove

- One run, one scenario, scored by the person who wrote the prompt. Nobody outside this project has scored anything, for any job.
- It says nothing about the other two business case scenarios. Hartwell and Bramfield have a different commercial shape and a measured pilot behind them, where the pressure is on the reader and voice rules rather than on labelling projections.
- It says nothing about the audit path, since the prompt was given a transcript rather than an existing draft to review. The skill covers both; this test exercised one.

## The Change to Test Next

Add the explicit human-check requirement to the skill and re-run the skill on this scenario. If the pilot-cost gap gets caught, the difference was the instruction rather than the artefact, and the skill should keep it.
