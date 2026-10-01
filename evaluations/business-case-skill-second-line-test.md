# The Business Case Skill's Second Line: A Twelve-Run Test

The [prompt's second line](business-case-prompt-second-line-test.md) brought back the hours total that the stacked-figure guardrail had blocked, without bringing back the pound figure. The skill has the same guardrail, so I tested whether it needs the same line.

**It does. The published skill gave the hours total in none of six runs. With the line, all six gave it, and neither version gave the pound figure.**

## Why This Was an Open Question

On the prompt, I'd measured the guardrail blocking the total before trying the line. On the skill I hadn't. Its own footer said at the time that a follow-up "confirmed it is not too blunt". If the skill gave the total unprompted, there'd be nothing for the line to bring back.

## The Change

The same line I added to the prompt, in the same place, straight after the guardrail:

> The one exception: an estimate may be multiplied by a confirmed count, such as an estimated time per person by a confirmed number of people, to give a total in the estimate's own unit, labelled as resting on that estimate. Do not then multiply that total by anything else unmeasured, whether an approximate rate or a hoped-for reduction: that is two unmeasured figures again, one step removed.

## What I Decided in Advance

I copied the three measures unchanged from the prompt test:

1. The hours total, from the six-hour estimate and the confirmed twelve.
2. The cost figure in pounds, from the six-hour estimate and the £35 rate, anywhere, however caveated.
3. Any hours or money saved from the untested "half, maybe more".

If the published skill gave the hours total in three or more of six, the skill doesn't need the line. I'd adopt the line if the published skill gave the total in two or fewer, the line gave it in four or more, the pound figure appeared in one or fewer, and savings didn't rise.

## A Known Leak, Noted Before Any Run

The skill's footer described this scenario's defect: four of six earlier runs had multiplied an untimed estimate by a rough rate into a pound figure. Every run read that footer, because the skill tells a reader to paste the whole file.

It doesn't bias the comparison, because both versions had it. It does weaken the pound-figure measure: a zero here says less than the same zero on the prompt did. It also breaks this repository's rule that a skill's pointer to a test scenario mustn't say what the test hinges on. I [fixed it afterwards](#one-difference-from-what-was-tested), because changing it mid-test would have changed the file under test.

## Method

Twelve runs of the skill on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with the answer key removed. Same scenario and model as the three earlier tests. Each run had a fresh context, no access to this repository and an instruction not to follow links. I scored all 12 without knowing which version produced which.

## Result

| | Runs | Hours total | Pound figure | Reduction route |
| --- | ---: | ---: | ---: | ---: |
| Published skill, guardrail only | 6 | **0** | 0 | 0 |
| With the second line | 6 | **6** | 0 | 0 |

**I adopted the line.** It met every condition I'd set. Fisher's exact test, one-tailed, on six of six against none of six: p = 0.0011.

The plain skill blocks the total just as the prompt did. The footer's "not too blunt" claim holds for the two scenarios it names, which have confirmed prices. It was never true of this one, where nothing is measured.

All six runs with the line kept the total in hours and labelled it as resting on the estimate. One said the reduction "is not combined with the hours estimate above into any single 'hours saved' figure", because that combination "would rest on two unmeasured inputs at once".

## A Counting Error That Nearly Reversed the Result

My first count of the hours total used a search pattern too complex for the tool. It failed on all 12 files, and the script printed "no 72 / seventy-two / 3,744" for each, because a failed search returns nothing and nothing looks like a zero. At face value that scored the total at none of 12 and would have concluded the skill needed no change, the opposite of what the runs show.

The error messages gave it away. I redid the count in a way that can't fail silently and read every hit and every miss. The six runs without a total each state only the six hours per analyst.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the test myself. Nobody outside this project ran or scored it.
- The pound-figure zero holds only with the footer's warning present.
- It says nothing about the Hartwell or Bramfield scenarios, where confirmed prices exist and the guardrail already allows sound arithmetic.
- It measures whether the total appears, not whether a reader is better off.

## One Difference From What Was Tested

The published skill now differs from the file the runs read in two ways.

First, a single full stop. Adding the line moved the guardrail's closing full stop onto the end of the new line, so I put it back after the runs. The words of both bullets are unchanged.

Second, the footer. I rewrote it to remove the leak. It no longer describes this scenario's defect or the earlier results. The rules the runs followed are unchanged.

## Corrections

An earlier version of this page dropped the run's own quotation marks around hours saved.

An earlier version also described the failed search's output as "no total", which was a paraphrase in quotation marks.
