# The Ledger Step on the Skill: A Twelve-Run Test

The [prompt test](chase-dated-commitment-ledger-test.md) adopted a dated commitment ledger step at five of six against two of six, and named the obvious limit: the step was in the prompt only, and the skill is a different artefact with a longer instruction sheet. This tests it there.

**It is the clearest result on this thread, and it also shows a prediction I wrote down and got wrong.**

## The Prediction, Written Down Before Running

I expected the published skill to do better at this than the published prompt did, because the [repeat run findings](repeat-run-findings.md) record two runs of the skill showing this clash on the harder version of the scenario, where it could only be inferred.

**That was wrong in the direction that would have flattered the skill.** It scored zero of six where the prompt scored two of six.

## The Change

One section inserted before "Decide the Next Move", worded as the prompt's paragraph is:

> ## Build a Dated Commitment Ledger Before Deciding
>
> Before choosing a move, list every date, deadline or commitment in the supplied material, including any the prospect set for themselves, and separately list every period anyone is stated to be away, unavailable or not monitoring messages. Then check each date in the first list against each period in the second and note which of them fall inside one. Carry that result into the output in words, including when nothing collides. The ledger is a working step, not part of the finished output.

## The Criterion and Two Ways to Fail

**The criterion** is the one used for the prompt test and the weekday re-run, so all three are comparable: does the output state that the promised Thursday afternoon falls inside Alex's leave, or that the leave began before the promised date, as a fact drawn from the dates? Naming it as an unknown to confirm is not a yes.

Both failure conditions were fixed before any run:

- **The step does not transfer**, if the ledger arm states the clash in two or fewer of six.
- **The step is unnecessary**, if the published skill states it in four or more of six. Adding an instruction for behaviour that is already happening is what the [check requirement test](business-case-check-requirement-test.md) rejected.

## Method

Twelve blind runs on the current chase scenario, answer key removed at the line its own warning names, same model, a fresh isolated context each time, no rubric and no access to this repository. Six of the published skill, six with the section inserted. Both arms fresh: neither the prompt test's runs nor the two older skill runs were reused. Scored without knowing which arm each run came from.

## Result

| | Runs | Stated that the promised date falls inside the leave |
| --- | ---: | ---: |
| Skill as published | 6 | **0** |
| Skill with the ledger section | 6 | **6** |

**Complete separation.** Fisher's exact, one-tailed, gives p = 0.0011. Neither failure condition fired, so the step is adopted into the skill.

This is a stronger result than the prompt's five of six against two of six, and the reason is not that the skill responds better to the step. It is that **the published skill was worse at this to begin with**, so there was more room.

## Why the Earlier Record Looked Like the Opposite

The repeat run findings say the skill "showed the conflict between the promised Thursday transcript and the leave dates rather than calling the transcript overdue". That reads like a contradiction of zero of six, so the published output was checked directly rather than reasoned about.

[It says](../examples/hartwell-chase-output.md): "Whether the earlier Thursday timing still stands. The later leave dates suggest it does not, but Alex has not confirmed that directly." That is under a heading of things to confirm, and it is exactly the hedged form this criterion counts as a no.

**So the earlier scoring was looser than this criterion, not a different result.** Both records are accurate about what they measured, and the [repeat run findings](repeat-run-findings.md) now says so.

## The Step Worked and Half Its Instruction Did Not

**Five of the six ledger runs printed the ledger**, as a numbered list of dates followed by a "Collisions" section, despite the instruction saying it is a working step and not part of the finished output.

In the prompt test, none of the six did that. The difference is placement: in the prompt the step is a paragraph above the list of output sections, and in the skill it is a `##` section among other `##` sections that do describe output. **The same words in a different position produced the opposite behaviour on that half of the instruction.**

Whether that matters is a judgement rather than a finding. A collision table is arguably useful to a reader, and the instruction not to print it was written to keep the output clean. It is named at the bottom of this page rather than quietly reworded, since no test here supports either choice.

**This has since replicated.** The [no-collision test](chase-no-collision-test.md) found the same five of six printing it, on a different scenario, so it is a property of the section form of the instruction rather than a one-off.

## What Did Not Move

**All twelve runs decided to wait rather than chase**, which makes it forty-eight for forty-eight across the four tests on this thread. Every one of these tests has been about one supporting fact inside a correct decision.

## What This Test Cannot Prove

- Six runs an arm, one scenario, one model, and a criterion written and applied by the same person. Blind scoring removes knowing the arm and nothing else.
- p = 0.0011 on this criterion, this scenario, this model. It says nothing about a chase scenario with no date clash in it, where the instruction asks for a line saying nothing collides. None of these twelve runs was that case, and it is the same gap the prompt test left open.
- Perfect separation on six a side is easy to over-read. The published arm's zero of six is a single measurement of a cell that moved from one of six to two of six between sessions on the prompt.

## The Change to Test Next

The first of the two things this page named has been done: on a [scenario with no colliding dates](chase-no-collision-test.md), neither arm invented one and the step's own clause about saying nothing collides was followed five times in six.

What is left is whether the ledger should be printed. Two tests now show five of six runs printing it against an instruction saying not to, which needs a criterion about the output a person has to read rather than about a fact appearing at all.
