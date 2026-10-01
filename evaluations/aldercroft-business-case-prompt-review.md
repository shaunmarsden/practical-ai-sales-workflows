# Aldercroft Business Case Prompt Review

> **Correction.** This review argued that the prompt's required human-check section was the most likely reason it caught a gap the skill missed. I [tested that over six runs](business-case-check-requirement-test.md) and it was wrong. Two of three fresh runs of the unchanged skill caught the same gap, so the skill's published miss was normal variation. All three also produced a check section without being told to. The section below headed "Why This Scored Higher Than the Skill" is wrong on that point and says so.

This review scores the [worked business case](../examples/aldercroft-business-case-prompt-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests the [business case prompt](../templates/business-case-prompt.md). That's a different thing from the [Build a Business Case skill](../.agents/skills/build-business-case/SKILL.md), which the [Aldercroft business case review](aldercroft-business-case-review.md) scores. I cut the prompt down from the skill, so neither score is evidence for the other.

I wrote the prompt because the [Build a Business Case recipe card](../recipes/build-a-business-case.md) had nothing to paste. It was the last of the seventeen cards in that position.

I chose Aldercroft because it's the hardest of the three business case scenarios here. The whole case has to rest on forecasts made before any pilot. It has an unmeasured time estimate, a rough average hourly rate, a future headcount nobody has confirmed that the champion asked to leave out, and a side remark that's out of scope.

## Method Note

I pasted the prompt into a fresh context with only the [transcript](../examples/aldercroft-business-case-transcript.md) below it. I removed the transcript's answer key first, as its own warning says to. The run didn't know it was a test, didn't see the rubric and had no access to this repository.

**The order I worked in matters for how much the total is worth.** I wrote the prompt from the skill file, ran the test, and only then read the skill's own Aldercroft review so I could score the same way. I didn't write the prompt to avoid the weaknesses that review names. But one difference between the two is my doing, and it matters. See the section on it below.

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

The skill scored 46 on this scenario. Three of its four lost marks are ones this run kept:

| Area | Skill's run | This run |
| --- | --- | --- |
| Fact separation | 4, the six-hour estimate became a firm base for the maths without being flagged again there | 5, flagged again at the arithmetic |
| Missing information | 4, no pilot cost figure exists and the document didn't say so | 5, flagged with a marked gap and a check item |
| Hallucination risk | 4, two unmeasured inputs stacked into a confident-looking yearly figure | 5, no combined figure at all |
| Next step clarity | 4, nobody named to own the pilot scope decision | 4, the same gap |

**A three-point gap doesn't show the prompt is better than the skill.** I've seen identical prompts on identical inputs move by one to three points between runs, and a [nine-run test](hartwell-objection-ambiguous-test.md) where the same model reached a different main diagnosis each time. One run of each on one scenario can't tell a real difference from that.

**I thought one of the three points came from my design choice, not the model's judgement.** The skill lists eight things a document must contain, and a human-review section wasn't one of them. My prompt makes it a numbered, required section. I wrote that this was the most likely reason the pilot-cost gap got caught here and not there, and that I could test it by adding the same requirement to the skill.

**I tested it [over six runs](business-case-check-requirement-test.md), and I was wrong.** Two of three fresh runs of the unchanged skill named the missing pilot cost. So the published miss was normal variation in the skill, not the result of a missing instruction. All three unchanged runs also produced a human-check section unprompted. The section was always there. What changes is what goes in it.

That leaves the duller reading. **Three points between one run of each, on one scenario, can't be told apart from noise, and none of my explanations for it survived testing.**

## What Worked

- It kept the forecast honest both ways. The cautious "half" stayed the anchor, the more flattering "maybe more" never became the headline, and the whole document argues for running a pilot rather than promising a result.
- It didn't pad. Asked for three applied examples, it wrote one, based on the only manual task the call covers in depth. It said why the other two were missing and flagged the missing detail, rather than writing two paragraphs that would read the same in any other prospect's document. That's what the prompt's instruction about generic examples is for. It's also where a second scorer would most likely disagree with me: marking it down for not delivering a requested section would be fair.
- It caught something the answer key doesn't list. Nobody named a solution or product on the call, and the document says so rather than quietly naming one.
- The commercial section is an empty, marked gap, with an instruction not to fill it from internal pricing. On a document going to a CFO, that's the right kind of blank.

## What Needed Checking

- Nobody owns agreeing the pilot's length and measures. The document says it must happen before the pilot starts and leaves it there.
- Neither this run nor the skill's run produced three applied examples. The prompt asks for three. The skill only says three is a good number, so this is a gap against the prompt, not both. The skill's review didn't flag it either way, and it should have. [Twelve later runs](business-case-applied-examples-test.md) found the skill producing the one grounded example this scenario supports every time.
- The out-of-scope accounts payable remark appears in the check list, to confirm it's been kept out. The case itself is clean, and the skill's run did the same and scored 5, so this is consistent, not lenient. But a document sent on without its check list removed would carry that line.

## What This Test Cannot Prove

- One run, one scenario, scored by me, the person who wrote the prompt. Nobody outside this project has scored anything, for any job.
- It says nothing about the other two business case scenarios. Hartwell and Bramfield have a different commercial shape and a measured pilot behind them. There the pressure is on the reader and voice rules, not on labelling forecasts.
- It says nothing about reviewing an existing draft, since the prompt got a transcript. The skill does both, and this test covered one.

## The Change to Test Next

**I tested this one and rejected it.** The change was to add the human-check requirement to the skill and run it again on this scenario. If that caught the pilot-cost gap, the difference would be the instruction, not the skill versus the prompt. [Six runs](business-case-check-requirement-test.md) said no: two of three unchanged runs already caught the gap, and all three produced a check section without being told to. I kept the line as a clarification with weak evidence behind it, not as a proven fix.

The other open question about this skill, whether it drops its applied examples, is [also closed](business-case-applied-examples-test.md). The worry about this prompt was that its firm requirement for three applied examples might cause padding when the source supports only one. I [tested that over twelve runs](business-case-padding-test.md), and it didn't happen here. This run wasn't luck: twelve of twelve produce one grounded example and say why there aren't three.

That test found a different fault in this prompt. **Nine of twelve runs produced a pound figure built from two unmeasured inputs**, because the guardrail against that is in the skill and not here.
