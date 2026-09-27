# The Business Case Skill's Second Line: A Twelve-Run Test

The [prompt's second line](business-case-prompt-second-line-test.md) restored the hours total that the stacked-figure guardrail had suppressed, without bringing back the pound figure. The skill carries the identical guardrail, so this asks whether it needs the same line.

**It does. The published skill gave the hours total in none of six runs; with the line, all six gave it, and the pound figure stayed at none in both.**

## Why This Was a Genuinely Open Question

On the prompt, the guardrail had already been measured suppressing the total before the line was tried. On the skill it had not. One scored run had hinted at it, but that is not a count, and the skill differs from the prompt in ways that could plausibly matter: it is a longer instruction sheet with its own source order, evidence classification and guidance on applied examples, and its own footer says a follow-up "confirmed it is not too blunt". If any of that made the skill give the total unprompted, there would have been nothing for the line to restore.

So the control arm had a real job: settle whether the skill suppresses the total at all, before asking whether the line fixes it.

## The Change

The same line adopted on the prompt, in the same words and the same position, directly after the guardrail:

> The one exception: an estimate may be multiplied by a confirmed count, such as an estimated time per person by a confirmed number of people, to give a total in the estimate's own unit, labelled as resting on that estimate. Do not then multiply that total by anything else unmeasured, whether an approximate rate or a hoped-for reduction: that is two unmeasured figures again, one step removed.

## The Criterion and the Conditions

Written before either arm ran, with the three measures copied unchanged from the prompt test: the hours total from the six-hour estimate and the confirmed twelve; the pound figure from the six-hour estimate and the £35 rate, anywhere, however caveated; and any hours or money saved from the untested "half, maybe more".

**Void, meaning the skill does not need the line**, if the published skill gave the hours total in three or more of six. **Adopt** if the published skill gave it in two or fewer, the line gave it in four or more, the pound figure stayed at one or fewer, and the reduction route did not rise.

## Contamination, Registered Before Any Run

The skill's own footer describes this scenario's defect in detail: four of six earlier runs multiplying an untimed estimate by an approximate rate into a pound figure, and the guardrail written against it. The skill tells a reader to paste the whole file, so every run in both arms read that.

- **It does not bias the comparison.** The footer is identical in both arms, and the line sits in the rules rather than the footer, so the difference between the arms is the line's.
- **It does weaken the pound-figure measure.** With the footer already warning against that figure, a zero here is weaker evidence that the line did not reopen the door than the same zero on the prompt was, where no such warning existed.
- **It is a leak by this repository's own rule**, which says a skill's pointer to a test scenario must not say what the test hinges on. It is recorded here and not changed, because changing it would have changed the file under test.

## Method

Twelve blind runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md) with its answer key removed at the line its own warning names, the same scenario and model as the three earlier tests, a fresh isolated context each time, no access to this repository and an instruction not to follow links. Both arms were run fresh on the same day. Scored blind, under a mapping not opened until all twelve were scored.

## Result

| | Runs | Hours total | Pound figure | Reduction route |
| --- | ---: | ---: | ---: | ---: |
| Published skill, guardrail only | 6 | **0** | 0 | 0 |
| With the second line | 6 | **6** | 0 | 0 |

**Adopted.** Every registered condition was met and the void condition did not fire. Fisher's exact, one-tailed, on six of six against none of six: p = 0.0011.

The control settled the open question. The skill suppresses the total exactly as the prompt did, with none of six giving it, despite its longer guidance and despite a footer that says the guardrail is not too blunt. That footer claim is true of the two scenarios it names, which have confirmed prices; it was never true of this one, where nothing is measured.

The six runs with the line all kept the total in hours and labelled it as resting on the estimate. One said in terms that the reduction "is not combined with the hours estimate above into any single hours saved figure", because that "would rest on two unmeasured inputs at once".

## A Scoring Failure That Nearly Reversed the Result

The first attempt to count the hours total used a search whose pattern was too complex for the tool. It errored on every one of the twelve files, and the script around it printed "no total" for each, because an error returns nothing and nothing looks like a zero. Taken at face value that would have scored the total at none of twelve, which is the void condition: the test would have concluded the skill needed no change, the opposite of what the runs show.

The error messages were in the output, which is how it was caught. The count was redone in a way that cannot fail silently, and every hit and every miss was then read. The six runs without a total each state only the per-analyst six hours. This repository has recorded counts from searches going wrong before; this is the first where the search did not return a wrong number but no number at all, dressed as a clean result.

## What This Test Cannot Prove

- Six runs an arm, one scenario, one model, a criterion written and applied by the same person.
- The pound-figure zero is weakened by the footer, as registered. It shows the line did not reopen the door in the presence of that warning, not that it would not without it.
- It says nothing about the Hartwell or Bramfield scenarios, where confirmed prices exist and the guardrail was already shown not to suppress sound arithmetic.
- It measures whether the total appears, not whether a reader is better off with it.
- It is not an independent external test.

## One Difference From What Was Tested

The published skill differs from the file the six runs read by a single full stop. Inserting the line after the guardrail moved the guardrail's closing full stop onto the end of the new line, so the guardrail became the only bullet in its list without one. It was restored after the runs. The words of both bullets are unchanged. The prompt was not affected, because none of its bullets end with a full stop.

## What It Leaves

The skill and the prompt now carry the same guardrail and the same exception, and behave the same way on this scenario. The footer leak described above is still there, and is the one thing this test found that it deliberately did not fix.
