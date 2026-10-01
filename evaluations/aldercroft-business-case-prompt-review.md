# Aldercroft Business Case Prompt Review

> **Correction.** This review argued that the prompt's required human-check section was the most likely reason it caught a gap the skill missed. I [tested that over six runs](business-case-check-requirement-test.md) and it was wrong. Two of three fresh runs of the unchanged skill caught the same gap. The section headed "Why This Scored Higher Than the Skill" says so too.

This review scores the [worked business case](../examples/aldercroft-business-case-prompt-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests the [business case prompt](../templates/business-case-prompt.md), which I cut down from the [Build a Business Case skill](../.agents/skills/build-business-case/SKILL.md). The [Aldercroft business case review](aldercroft-business-case-review.md) scores the skill, so neither score is evidence for the other.

I wrote the prompt because the [Build a Business Case recipe card](../recipes/build-a-business-case.md) had nothing to paste. I chose Aldercroft because it's the hardest of the three business case scenarios here. The whole case rests on forecasts made before any pilot, with an unmeasured time estimate, a rough hourly rate, a future headcount nobody has confirmed, and an out-of-scope side remark.

## Method Note

I pasted the prompt into a fresh context with only the [transcript](../examples/aldercroft-business-case-transcript.md) below it, with its answer key removed. The run didn't see the rubric and had no access to this repository. I wrote the prompt from the skill file, ran the test, and only then read the skill's own Aldercroft review. I didn't write the prompt to avoid that review's weaknesses, but one difference between the two is my doing. See the next section.

## Result

**Score: 49 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The six-hour estimate, the £35 average rate, the 12-person headcount, the audit-trail requirement and the pilot-not-rollout ask all match the transcript exactly |
| Evidence fidelity | 5 | Every condition in the transcript survives, including the two most likely to get flattened: the rate stays a rough planning average, and the five unconfirmed analysts stay out of every figure |
| Fact separation | 5 | A status column labels each summary item, and the six-hour estimate is flagged again as unmeasured where the arithmetic uses it, not only where it first appears |
| Missing information | 5 | Names the missing pilot cost, the undefined measurement period, the missing resourcing figure and the fact that nobody named a solution, which the transcript doesn't prompt for |
| Commercial usefulness | 5 | Sizes the ask correctly as a paid pilot with a measurement period, which is what the champion asked for, and gives the reader the two figures without welding them into one |
| Next step clarity | 4 | Names Priya as the approver and says clearly that sending doesn't finish the process, but names nobody to own agreeing the pilot's length and measures |
| Tone | 5 | Third person throughout, which is right, because the reader is the CFO, not the person on the call. Hedged in line with how weak the material is, without sounding evasive |
| Privacy | 5 | Names no analyst, has no customer personal data, and keeps the out-of-scope accounts payable remark out of the case |
| Approval discipline | 5 | Says plainly that it's still a draft for the champion to review, leaves the commercial section as a marked gap rather than filling it, and treats nothing as sent or agreed |
| Hallucination risk | 5 | Invents nothing, including a product name, which it says was never set, and declines to multiply two unmeasured inputs into one headline saving |

## Why This Scored Higher Than the Skill, and Why That Is Not a Result

The skill scored 46 on this scenario and lost four marks. This run didn't lose three of them:

| Area | Skill's run | This run |
| --- | --- | --- |
| Fact separation | 4, the six-hour estimate became a firm base for the maths without being flagged again there | 5, flagged again at the arithmetic |
| Missing information | 4, no pilot cost figure exists and the document didn't say so | 5, flagged with a marked gap and a check item |
| Hallucination risk | 4, two unmeasured inputs stacked into a confident-looking yearly figure | 5, no combined figure at all |
| Next step clarity | 4, nobody named to own the pilot scope decision | 4, the same gap |

**A three-point gap doesn't show the prompt is better than the skill.** Identical prompts on identical inputs have moved by one to three points between runs, and in a [nine-run test](hartwell-objection-ambiguous-test.md) the same model reached a different main diagnosis each time.

**I thought one of the three points came from my design choice.** The skill lists eight things a document must contain, and a human-review section wasn't one of them. My prompt requires one. I wrote that this was the most likely reason the pilot-cost gap got caught here and not there.

**I tested it [over six runs](business-case-check-requirement-test.md), and I was wrong.** Two of three fresh runs of the unchanged skill named the missing pilot cost, and all three produced a human-check section unprompted. So the published miss was normal variation, and none of my explanations for the gap survived testing.

## What Worked

- It kept the forecast honest both ways. The cautious "half" stayed the anchor, and "maybe more" never became the headline.
- It didn't pad. Asked for three applied examples, it wrote one, based on the only manual task the call covers in depth, and said why the other two were missing. A second scorer would most likely disagree with me here, since marking it down for not delivering a requested section would be fair.
- It caught something the answer key doesn't list. Nobody named a solution or product on the call, and the document says so rather than quietly naming one.
- The commercial section is an empty, marked gap, with an instruction not to fill it from internal pricing. For a CFO, that's the right kind of blank.

## What Needed Checking

- Nobody owns agreeing the pilot's length and measures.
- Neither this run nor the skill's run produced three applied examples. The prompt asks for three and the skill only says three is a good number, so this is a gap against the prompt alone. [Twelve later runs](business-case-applied-examples-test.md) found the skill producing the one grounded example this scenario supports every time.
- The out-of-scope accounts payable remark appears in the check list, to confirm it's been kept out. The case itself is clean, and the skill's run did the same and scored 5, but a document sent on without its check list removed would carry that line.

## What This Test Cannot Prove

- One run, one scenario, scored by me, the person who wrote the prompt. Nobody outside this project has scored anything.
- It says nothing about the other two scenarios, which have a measured pilot behind them, or about reviewing an existing draft, since the prompt got a transcript.

## The Change to Test Next

The human-check change is tested and rejected. I kept the line in the skill as a clarification with weak evidence behind it, not as a proven fix.

The worry about this prompt was that its firm requirement for three applied examples might cause padding when the source supports only one. I [tested that over twelve runs](business-case-padding-test.md), and it didn't happen: all twelve produce one grounded example and say why there aren't three.

That test found a different fault. **Nine of twelve runs produced a pound figure built from two unmeasured inputs**, because the guardrail against that is in the skill and not here.
