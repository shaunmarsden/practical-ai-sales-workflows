# The Ledger Step on the Skill: A Twelve-Run Test

The [prompt test](chase-dated-commitment-ledger-test.md) adopted a dated commitment ledger step, at five of six against two of six. It also named the obvious limit: the step was only in the prompt, and the skill is a different thing with longer instructions. This page tests it in the skill.

**It's the clearest result on this thread, and it shows a prediction I wrote down and got wrong.**

## The Prediction, Written Down Before Running

I expected the skill without the step to beat the prompt without it. The [repeat run findings](repeat-run-findings.md) record two runs of the skill spotting this clash on the harder version of the scenario, where it could only be inferred.

**I was wrong, in the direction that would have flattered the skill.** It scored zero of six where the prompt scored two of six.

## The Change

I added one section before "Decide the Next Move", worded like the prompt's paragraph:

> ## Build a Dated Commitment Ledger Before Deciding
>
> Before choosing a move, list every date, deadline or commitment in the supplied material, including any the prospect set for themselves, and separately list every period anyone is stated to be away, unavailable or not monitoring messages. Then check each date in the first list against each period in the second and note which of them fall inside one. Carry that result into the output in words, including when nothing collides. The ledger is a working step, not part of the finished output.

## The Criterion and Two Ways to Fail

**The pass mark** is the same as in the prompt test and the weekday re-run, so all three compare. Does the output say that the promised Thursday afternoon falls inside Alex's leave, or that the leave began before the promised date, as a fact taken from the dates? Naming it as an unknown to confirm doesn't count.

I set both ways to fail before any run:

- **The step doesn't carry over**, if the version with the ledger states the clash in two or fewer of six.
- **The step isn't needed**, if the skill without it states the clash in four or more of six. Adding an instruction for something already happening is what the [check requirement test](business-case-check-requirement-test.md) rejected.

## Method

Twelve runs on the current chase scenario, with the answer key removed at the line its own warning names. Same model, a fresh context each time, no rubric and no access to this repository. Six used the skill as it stood before the step, and six had the new section. **The skill now has the step**, so "published" today means the second of those. I've named the versions below for what they contain, not for what was published at the time. Both sets were fresh: I didn't reuse the prompt test's runs or the two older skill runs. I scored them without knowing which version each came from.

## Result

| | Runs | Stated that the promised date falls inside the leave |
| --- | ---: | ---: |
| Skill without the step | 6 | **0** |
| Skill with the step | 6 | **6** |

**The two sets didn't overlap at all.** A one-tailed Fisher's exact test gives p = 0.0011. Neither way to fail happened, so the skill now has the step.

This beats the prompt's five of six against two of six. That's not because the skill responds better to the step. **The skill was worse at this to start with**, so it had more room to improve.

## Why the Earlier Record Looked Like the Opposite

The repeat run findings say the skill "showed the conflict between the promised Thursday transcript and the leave dates rather than calling the transcript overdue". That seems to contradict zero of six, so I checked the published output itself rather than reasoning about it.

[It says](../examples/hartwell-chase-output.md): "Whether the earlier Thursday timing still stands. The later leave dates suggest it does not, but Alex has not confirmed that directly." That sits under a heading of things to confirm. It's exactly the hedged form this pass mark counts as a no.

**So the earlier scoring was looser than this pass mark. It wasn't a different result.** Both records are accurate about what they measured, and the [repeat run findings](repeat-run-findings.md) now say so.

## The Step Worked and Half Its Instruction Did Not

**Five of the six ledger runs printed the ledger**, as a numbered list of dates followed by a "Collisions" section. The instruction says it's a working step and not part of the finished output.

In the prompt test, none of the six did that. The difference is where the step sits. In the prompt it's a paragraph above the list of output sections. In the skill it's a `##` section among other `##` sections that do describe output. **The same words in a different place produced the opposite result on that half of the instruction.**

Whether that matters is a judgement, not a finding. A table of clashes may help a reader, and I wrote the instruction not to print it to keep the output clean. I've named it at the bottom of this page rather than quietly rewording it, since no test here backs either choice.

**This has since happened again, and been settled.** The [no-collision test](chase-no-collision-test.md) found the same five of six printing it on a different scenario, so it came from the section format, not chance. A [third test](chase-ledger-printing-test.md) found that saying so outright stops the printing, at zero of six against six of six, without losing the date clash the step is there to catch. The skill now uses the stronger wording.

## What Did Not Move

**All 12 runs decided to wait rather than chase.** That makes it 48 out of 48 across the four tests on this thread. Every one of these tests has been about one supporting fact inside a correct decision.

A [fifth test](chase-no-collision-test.md) later broke that streak on purpose. On a scenario with no stated reason for the silence, all 12 of its runs chose to chase now instead, in both versions.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the pass mark myself. Scoring without knowing the version removes that one bias and nothing else.
- p = 0.0011 holds for this pass mark, this scenario and this model. It says nothing about a chase scenario with no date clash, and none of these 12 runs had one. I've since [tested that separately](chase-no-collision-test.md), and neither version invented a clash there.
- A perfect split on six a side is easy to over-read. The zero of six without the step is one measurement of a result that moved from one of six to two of six between sessions on the prompt.

## The Change to Test Next

I've done the first of the two things this page named. On a [scenario with no clashing dates](chase-no-collision-test.md), neither version invented one, and the step's clause about saying when nothing clashes was followed five times in six.

The second, whether the ledger should be printed, I [tested too](chase-ledger-printing-test.md), by first asking whether the instruction could be made to hold at all. It can, and now does. That doesn't settle whether the shorter output is better, but it puts a number on the trade: the printed ledger is about 139 words, roughly a quarter of the output.
