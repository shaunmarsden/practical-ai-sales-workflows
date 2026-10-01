# The Business Case Skill's Second Line: A Twelve-Run Test

The [prompt's second line](business-case-prompt-second-line-test.md) brought back the hours total that the stacked-figure guardrail had blocked, without bringing back the pound figure. The skill has the same guardrail, so I tested whether it needs the same line.

**It does. The published skill gave the hours total in none of six runs. With the line, all six gave it, and neither version gave the pound figure.**

## Why This Was an Open Question

On the prompt, I'd already measured the guardrail blocking the total before trying the line. On the skill I hadn't. One scored run had hinted at it, but that isn't a count.

The skill also differs from the prompt in ways that could matter. It's a longer instruction sheet, with its own source order, evidence labels and guidance on applied examples. Its own footer said at the time that a follow-up "confirmed it is not too blunt". If any of that made the skill give the total unprompted, there'd be nothing for the line to bring back.

So the plain skill had a real job: show whether it blocks the total at all, before I asked whether the line fixes it.

## The Change

The same line I added to the prompt, in the same words and the same place, straight after the guardrail:

> The one exception: an estimate may be multiplied by a confirmed count, such as an estimated time per person by a confirmed number of people, to give a total in the estimate's own unit, labelled as resting on that estimate. Do not then multiply that total by anything else unmeasured, whether an approximate rate or a hoped-for reduction: that is two unmeasured figures again, one step removed.

## What I Decided in Advance

I wrote these down before either version ran, and copied the three measures unchanged from the prompt test:

1. The hours total, from the six-hour estimate and the confirmed twelve.
2. The cost figure in pounds, from the six-hour estimate and the £35 rate, anywhere, however caveated.
3. Any hours or money saved from the untested "half, maybe more".

If the published skill gave the hours total in three or more of six, the skill doesn't need the line. I'd adopt the line if the published skill gave the total in two or fewer, the line gave it in four or more, the pound figure appeared in one or fewer, and the savings figure didn't rise.

## A Known Leak, Noted Before Any Run

At the time of the test, the skill's own footer described this scenario's defect in detail. It said four of six earlier runs had multiplied an untimed estimate by a rough rate into a pound figure, and that the guardrail was written against it. The skill tells a reader to paste the whole file, so every run in both versions read that.

It doesn't bias the comparison. The footer was the same in both versions, and the line sits in the rules, not the footer, so any difference comes from the line.

It does weaken the pound-figure measure. With the footer already warning against that figure, a zero here says less about whether the line let it back in than the same zero on the prompt did, where there was no such warning.

It breaks this repository's own rule that a skill's pointer to a test scenario mustn't say what the test hinges on. I noted it here and didn't change it, because that would have changed the file under test. I [fixed it afterwards](#one-difference-from-what-was-tested), in a separate change.

## Method

I ran the skill 12 times on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with the answer key removed at the line its own warning names. It was the same scenario and model as the three earlier tests. Each run had a fresh context, no access to this repository and an instruction not to follow links. I ran both versions fresh on the same day. I scored all 12 without knowing which version produced which.

## Result

| | Runs | Hours total | Pound figure | Reduction route |
| --- | ---: | ---: | ---: | ---: |
| Published skill, guardrail only | 6 | **0** | 0 | 0 |
| With the second line | 6 | **6** | 0 | 0 |

**I adopted the line.** It met every condition I'd set. Fisher's exact test, one-tailed, on six of six against none of six: p = 0.0011.

The plain skill answered the open question. It blocks the total just as the prompt did, with none of six giving it, despite its longer guidance and despite a footer saying the guardrail isn't too blunt. That footer claim is true of the two scenarios it names, which have confirmed prices. It was never true of this one, where nothing is measured.

All six runs with the line kept the total in hours and labelled it as resting on the estimate. One said the reduction "is not combined with the hours estimate above into any single 'hours saved' figure", because that combination "would rest on two unmeasured inputs at once".

## A Counting Error That Nearly Reversed the Result

My first count of the hours total used a search pattern too complex for the tool. It failed on all 12 files. The script around it then reported no total for each, printing "no 72 / seventy-two / 3,744", because a failed search returns nothing and nothing looks like a zero.

Taken at face value, that would have scored the total at none of 12. The test would then have concluded the skill needed no change, the opposite of what the runs show.

The error messages were in the output, which is how I caught it. I redid the count in a way that can't fail silently, then read every hit and every miss. The six runs without a total each state only the six hours per analyst.

Searches have given me wrong counts before. This is the first time a search returned no number at all and it looked like a clean result.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the test myself.
- The footer weakens the pound-figure zero, as noted above. It shows the line didn't let the figure back in when that warning was present, not that it wouldn't without it.
- It says nothing about the Hartwell or Bramfield scenarios, where confirmed prices exist and the guardrail already allows sound arithmetic.
- It measures whether the total appears, not whether a reader is better off with it.
- Nobody outside this project ran or scored it.

## One Difference From What Was Tested

The published skill now differs from the file the runs read in two ways.

The first is a single full stop. Adding the line after the guardrail moved the guardrail's closing full stop onto the end of the new line, so the guardrail was the only bullet in its list without one. I put it back after the runs. The words of both bullets are unchanged. The prompt wasn't affected, because none of its bullets end with a full stop.

The second is the footer. After this test I rewrote it to remove the leak. It no longer describes this scenario's defect or the earlier results. It now points to Bramfield and Aldercroft as further tests of the same job, without saying what each one turns on. The rules the runs followed are unchanged. The runs read the old footer, which warned them about the pound figure, and that's why the pound-figure zero here is weaker than on the prompt.

## What It Leaves

The skill and the prompt now have the same guardrail and the same exception, and behave the same way on this scenario. The footer leak was the one thing this test found and didn't fix at the time. I've since fixed it in a separate change.

## Corrections

An earlier version of this page dropped the run's own quotation marks around hours saved.

An earlier version also described the failed search's output as "no total", which was a paraphrase in quotation marks.
