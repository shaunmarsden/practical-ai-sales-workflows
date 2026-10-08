# Applied Examples: A Twelve-Run Test That Corrects Its Own Premise

The [stacked figure test](business-case-stacked-figure-test.md) named this as the next question about the Build a Business Case skill. Reading the wording before running anything showed that half the question was my own reporting error. Twelve runs, scored without knowing which version was which, showed the other half isn't there either.

## What This Repository Said, and What the Files Say

Two pages here said the skill and the prompt both ask for three applied examples, and that across six runs the instruction was never followed.

Only the prompt asks for three. The skill's bullet says "**Applied examples**: three is a good number", in a list where other items say "always present" and "present, with a real figure". The softer wording is deliberate.

All six of those runs were runs of the skill, so the claim measured whether the skill obeyed an instruction it doesn't contain. The prompt's one run produced a single grounded example and said why the other two were missing. [Its own review](aldercroft-business-case-prompt-review.md) recorded that as a strength. I've corrected the four pages that carried the wrong claim.

The earlier counts were one, zero, zero, one, zero and one. **Three of those six runs produced no applied example at all**, on a scenario that sets out one manual task in depth. A business case with no worked example drops the part that links a cost to the work, so I tested that.

## The Change and the Criterion

I replaced one line and changed nothing else:

> **Applied examples**: at least one is required, and one for each distinct manual task the sources establish in enough detail to describe. Three is a good number when the source material supports three. If it supports fewer, produce the ones it supports and say plainly which detail is missing, rather than padding to a number or leaving the section out.

The pass mark, decided before any run: at least one applied example that names the specific manual task the transcript sets out, its cost, what the proposed solution addresses, and what changes as a result. It needs all four. A cost section giving the six-hour estimate isn't an applied example.

Also decided in advance:

- If the published skill produces such an example in five or six of its six runs, the earlier three in six was normal variation. The change isn't needed and I don't adopt it.
- If both versions score six of six, the pass mark was too easy, and I add no runs to rescue a result.
- Any example that would read the same in another prospect's document counts as padding.

## Method

Twelve runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with its answer key removed at the line its own warning names. Same model, a fresh isolated context each time, no rubric, no access to this repository. Six used the skill as published and six had that one line changed.

I scored without knowing which version each output came from. I copied the outputs to neutrally named files under a mapping that was generated but never displayed, and opened it only after scoring all twelve. I scored every earlier comparison here knowing which version I was reading.

## Result

| | Runs | At least one grounded applied example |
| --- | ---: | ---: |
| Skill as published | 6 | **6** |
| Skill with the line | 6 | **6** |

**12 of 12. The published skill passed often enough that the change isn't needed, so I'm not adopting it.** No run produced a second or third example, so none padded.

Every run built one example around reconciliation matching, with the six-hour estimate labelled as Tomasz's own untimed observation. Seven gave it an "Applied example" heading and five put the same four things under a heading about the manual task. The weakest of the twelve never says what the proposed solution addresses. A second scorer would most likely mark it differently. It used the changed line.

## Something I Noticed Afterwards

Six of the 12 said why there's only one example. Four of six had the changed line and two of six didn't, a one-tailed p of 0.28. **This wasn't the pass mark, and six runs a side can't tell it from chance.** I haven't acted on it, because the last test on this skill turned this kind of cell into a claim that later needed correcting.

## Why the Earlier Count Cannot Be Rechecked

On this pass mark the earlier count is three of six, against six of six here. **That isn't a before-and-after comparison, and I offer no p value for one.** Five of those six outputs were never published, and the skill has since gained the stacked figure guardrail, the em dash rule and the human check line.

All three published Aldercroft outputs do contain an applied example: the [prompt output](../examples/aldercroft-business-case-prompt-output.md), the [check requirement output](../examples/aldercroft-business-case-check-requirement-output.md) and the [guardrail output](../examples/aldercroft-business-case-guardrail-output.md).

## Two Things the Input Carried

Both versions carried them equally, so neither explains a difference between them.

- The skill's evidence footer named the scenario's two traps, an unmeasured time estimate and an unconfirmed future headcount.
- The fictional-disclosure blockquote in the transcript names the same two traps and sits above the re-run line, so anyone who copies everything above it hands the model part of the answer key. That affects every earlier test on this transcript. I found the same fault in 15 published inputs and six skill footers. All are now fixed.

## What This Test Cannot Prove

- One scenario, one model. Aldercroft sets out one manual task in depth, so this says nothing about a source that supports three examples.
- Both versions passed completely. That shows the change isn't needed here, not that the wording is best.
- I wrote the pass mark and the change, and scored every run.
- It says nothing about the prompt, which is the file that asks for three.

## What Changed

**Nothing in the skill.** "Three is a good number" stays. The case for changing it rested on a fault that six fresh runs didn't reproduce once.

## The Change to Test Next

I [tested whether the prompt's firm "Three applied examples" causes padding](business-case-padding-test.md) on a source that supports only one. It doesn't. All 12 runs produced exactly one example and said why there weren't three.

That test found something else. **Nine of its 12 runs produced the stacked figure**, because the guardrail is in the skill but not the prompt. Adding it to the prompt was the next change to test, starting from nine of 12. I [did that](business-case-prompt-guardrail-test.md).
