# The Dated Commitment Ledger: A Twelve-Run Test

Three tests have now gone at the same defect. The [chase prompt review](hartwell-chase-prompt-review.md) found a run that never mentioned the transcript Alex promised by Thursday afternoon, a promise the scenario places inside his later leave. Widening the instruction was [rejected](chase-stale-date-test.md). Naming the weekday in the scenario, so the clash could be established at all, was [rejected too](chase-weekday-rerun.md).

**This is the first change on this thread that has not been rejected**, and it is the same shape as the one that worked on the invented-pronoun failure: a required step rather than a principle.

## The Change

One paragraph inserted before the prompt's section list, and nothing else altered:

> Before writing any of the sections below, build a dated commitment ledger. List every date, deadline or commitment in what I have given you, including any the prospect set for themselves, and separately list every period anyone is stated to be away, unavailable or not monitoring messages. Then check each date in the first list against each period in the second and note which of them fall inside one. Carry that result into section 1 in words, including when nothing collides. The ledger itself is a working step, not part of the output.

## The Criterion and the Conditions

**The criterion, written down before any run,** and the same one the weekday re-run used so the two are comparable: does the output state that the promised Thursday afternoon falls inside Alex's leave, or that the leave began before the promised date, as a fact drawn from the dates? Naming it as an unknown to confirm is not a yes. Saying the commitment was overtaken by events, without connecting the promised date to the leave dates, is not a yes either, since that is equally true of the CRM task.

**The falsification condition:** if the arm carrying the ledger states the clash in two or fewer of its six runs, the mechanism did not work either and it is not adopted.

**A void condition, which the earlier tests on this thread did not have:** if the arm without the ledger states the clash in four or more of six, the baseline has moved a long way from the one of six measured the day before on the same prompt and scenario, and the comparison cannot be read at all.

## Method

Twelve blind runs on the current chase scenario, answer key removed at the line its own warning names, same model, a fresh isolated context each time, no rubric and no access to this repository. Six of the published prompt, six with the paragraph inserted. Both arms run fresh rather than reusing the previous day's runs. Scored without knowing which arm each run came from.

## Result

| | Runs | Stated that the promised date falls inside the leave |
| --- | ---: | ---: |
| Prompt as published | 6 | **2** |
| Prompt with the ledger step | 6 | **5** |

**The falsification condition was not met and the void condition did not fire, so the step is adopted.**

**The evidence is weaker than the table looks.** Fisher's exact on five of six against two of six, one-tailed, gives p = 0.12. That does not reach the level this repository has treated as a result elsewhere, and the pre-registered condition was a threshold rather than a significance test. What can be said is that the mechanism was not falsified, on a thread where two previous changes were.

**A post-hoc calculation, offered as information rather than as the result.** Pooling the previous day's six runs of the published prompt, which produced one of six on the same scenario, gives three of twelve against five of six and p = 0.032. Pooling arms across sessions was not pre-registered, and it is the move criticised on the [stacked figure test](business-case-stacked-figure-test.md), so it is not what this test rests on.

## What the Mechanism Actually Did

Four of the six ledger runs visibly performed the comparison, opening section 1 with a line like "Checking the dates against that away period" or "Collision check". A fifth stated the clash without showing the working. **The sixth did neither**, never mentioning the promised date at all, so a required step can still be skipped entirely.

The two runs of the published prompt that met the criterion got there without any prompting to compare dates, which is worth remembering before treating the step as the only route to the behaviour.

**The pre-registered observation came back clean.** No run printed the ledger as a table or list. The instruction to treat it as a working step rather than output held in all six.

## What Did Not Move, in Any of the Thirty-Six Runs

**Every single run across all three tests on this thread decided to wait rather than chase.** Thirty-six for thirty-six. This whole line of work has been about one supporting fact inside a correct answer, not about a wrong decision, and that is worth keeping in proportion.

## The Baseline Moved Between Sessions

The published prompt produced one of six on this scenario yesterday and two of six today. Both are the same prompt on the same input. **That is the run-to-run movement this repository keeps measuring, showing up inside a six-run cell**, and it is the reason the void condition was written into the pre-registration before the numbers existed.

## What This Test Cannot Prove

- Six runs an arm, one scenario, one model, and a criterion written and applied by the same person. Blind scoring removes knowing the arm and nothing else.
- p = 0.12 supports adopting a change that costs one paragraph. It would not support a claim that the step reliably produces the behaviour.
- **The step is in the prompt only.** The [Plan a Chase Sequence skill](../.agents/skills/plan-chase-sequence/SKILL.md) does not carry it and has not been tested with it, and the em dash rule is the cautionary example of changing many artefacts on the strength of one.
- It says nothing about whether the ledger helps on an input with no date clash in it, where the instruction asks for a line saying nothing collides. None of these twelve runs was that case.

## The Change to Test Next

Whether the same step helps the skill, which is a different artefact and a longer instruction sheet, and whether it costs anything on a scenario where no dates collide at all.
