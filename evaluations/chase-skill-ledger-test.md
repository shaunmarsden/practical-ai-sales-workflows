# The Ledger Step on the Skill: A Twelve-Run Test

The [prompt test](chase-dated-commitment-ledger-test.md) adopted a dated commitment ledger step, at five of six against two of six, and named one limit: the step was only in the prompt. This page tests it in the skill, which has longer instructions.

**It's the clearest result on this thread, and it shows a prediction I wrote down and got wrong.**

## The Prediction, Written Down Before Running

I expected the skill without the step to beat the prompt without it, since the [repeat run findings](repeat-run-findings.md) record two skill runs spotting this clash. **I was wrong, in the direction that would have flattered the skill.** It scored zero of six where the prompt scored two of six.

## The Change

I added one section before "Decide the Next Move", worded like the prompt's paragraph:

> ## Build a Dated Commitment Ledger Before Deciding
>
> Before choosing a move, list every date, deadline or commitment in the supplied material, including any the prospect set for themselves, and separately list every period anyone is stated to be away, unavailable or not monitoring messages. Then check each date in the first list against each period in the second and note which of them fall inside one. Carry that result into the output in words, including when nothing collides. The ledger is a working step, not part of the finished output.

## The Pass Mark and Two Ways to Fail

The pass mark matches the prompt test and the [weekday re-run](chase-weekday-rerun.md). Does the output say, as a fact taken from the dates, that the promised Thursday afternoon falls inside Alex's leave? Naming it as an unknown to confirm doesn't count.

Before any run I set two ways to fail:

- **The step doesn't carry over**, if the version with the ledger states the clash in two or fewer of six.
- **The step isn't needed**, if the skill without it states the clash in four or more of six. The [check requirement test](business-case-check-requirement-test.md) rejected that.

## Method

Twelve runs on the current chase scenario, with the answer key removed at the line its own warning names. Same model, a fresh context each time, no rubric, no access to this repository. Six used the skill before the step and six had the new section. I scored them without knowing which was which.

## Result

| | Runs | Stated that the promised date falls inside the leave |
| --- | ---: | ---: |
| Skill without the step | 6 | **0** |
| Skill with the step | 6 | **6** |

**The two sets didn't overlap at all.** A one-tailed Fisher's exact test gives p = 0.0011. Neither way to fail happened, so the skill now has the step. That's a bigger gap than the prompt's five of six against two of six, but only because the skill started worse.

## Why the Earlier Record Looked Like the Opposite

The repeat run findings say the skill "showed the conflict between the promised Thursday transcript and the leave dates rather than calling the transcript overdue". That seems to contradict zero of six, so I checked [the published output](../examples/hartwell-chase-output.md). It says the leave dates "suggest it does not, but Alex has not confirmed that directly", under things to confirm. This pass mark counts that hedge as a no.

**So the earlier scoring was looser than this pass mark, not a different result.** The repeat run findings now say so.

## Half the Instruction Did Not Work

**Five of the six ledger runs printed the ledger**, as a numbered list of dates and a "Collisions" section, though the instruction says it's a working step and not part of the output. None of the six did in the prompt test.

The difference is where the step sits. In the prompt it's a paragraph above the output sections. In the skill it's a `##` section among other `##` sections that describe output. **The same words in a different place produced the opposite result on that half of the instruction.** Whether printing matters is a judgement.

## What Did Not Move

**All 12 runs decided to wait rather than chase**, which makes 48 out of 48 across the four tests on this thread. Each test has been about one supporting fact inside a correct decision.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the pass mark myself.
- None of these runs had a scenario without a date clash, so p = 0.0011 says nothing about that case.
- A perfect split on six a side is easy to over-read. On the prompt, the same measurement moved from one of six to two of six between sessions.

## The Change to Test Next

I've since done both things this page named. On a [scenario with no clashing dates](chase-no-collision-test.md), neither version invented a clash, and the clause about saying when nothing clashes was followed five times in six. The same five of six printed the ledger, so the printing came from the section format, not chance. With no stated reason for the silence, all 12 runs chose to chase now, which broke the 48-run streak.

A [third test](chase-ledger-printing-test.md) found that saying outright that the ledger isn't output stops the printing, at zero of six against six of six, without losing the date clash. The skill now uses that wording. The printed ledger is about 139 words, roughly a quarter of the output.
