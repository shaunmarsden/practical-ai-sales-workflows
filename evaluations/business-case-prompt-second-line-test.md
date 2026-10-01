# The Business Case Prompt's Second Line: A Twelve-Run Test

The [stacked-figure guardrail](business-case-prompt-guardrail-test.md) stopped the business case prompt building a pound figure from two guesses. That test also measured the cost: the prompt stopped giving the hours total too, which that test's own pass mark says isn't the fault. I adopted the guardrail anyway, and the page says plainly that I'd drawn the line too bluntly.

This tests a second line meant to redraw it. **It works. The hours total comes back in five of six runs, and the pound figure doesn't come back at all.**

## The Change

I added one line straight after the existing guardrail in the prompt's Rules list:

> The one exception: an estimate may be multiplied by a confirmed count, such as an estimated time per person by a confirmed number of people, to give a total in the estimate's own unit, labelled as resting on that estimate. Do not then multiply that total by anything else unmeasured, whether an approximate rate or a hoped-for reduction: that is two unmeasured figures again, one step removed.

The second sentence matters as much as the first. On this scenario there are two ways back to the fault from an allowed total. Multiplying 72 hours by the rough £35 rate rebuilds the pound figure one step later. Multiplying it by Tomasz's untested "half, maybe more" gives an hours-saved figure from two unmeasured inputs. The line has to close both, or allowing the total just moves the fault.

## The Criterion and the Conditions

I wrote these before either version ran.

- **Main measure, the hours total:** a total built from the six-hour estimate and the confirmed 12 analysts, such as 72 analyst-hours a week.
- **First guard, the fault**, copied unchanged from the [stacked figure test](business-case-stacked-figure-test.md) and the guardrail test: a currency figure built from both the six-hour estimate and the £35 rate, anywhere, however caveated.
- **Second guard, the reduction route:** anything multiplied by the untested reduction to give hours or money saved. I added it because a line allowing one multiplication could loosen another.

**Adopt** if the second line gives the hours total in four or more of six, the pound figure in one or fewer, and the reduction route no more often than the control. **Void** if the control gives the hours total in three or more. That would mean the guardrail alone no longer suppressed it, so there'd be nothing to restore.

## Method

Twelve runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with its answer key removed at the line its own warning names. Same scenario and model as both earlier tests, a fresh context each time and no access to this repository.

I ran both versions fresh on the same day. The earlier test had already measured the guardrail alone. But relying on runs from another session is how this repository once published a test with three reused runs it didn't disclose. So I ran the published prompt again as a same-day control. I scored all 12 without knowing which version produced which, and didn't open the key until I'd finished.

## Result

| | Runs | Hours total | Pound figure | Reduction route |
| --- | ---: | ---: | ---: | ---: |
| Published prompt, guardrail only | 6 | **0** | 0 | 0 |
| With the second line | 6 | **5** | 0 | 0 |

**Adopted.** It met every condition I'd set, and neither void condition happened. A one-tailed Fisher's exact test on five of six against none of six gives p = 0.0076.

The control matched the earlier test exactly: no hours total and no pound figure in six runs. So the same-day comparison and the one across sessions agree, and the result doesn't rest on either alone.

For comparison, the earlier test measured the prompt before any guardrail. Four of six gave some overall scale, and five of six produced the pound figure. The second line brings the hours total back to at least that level, while keeping the pound figure at none.

## What the Runs Actually Did

The five that gave the total all kept it in hours and said it rested on the estimate. Several said why they'd go no further. One wrote that it "does not combine that reduction estimate with the seventy-two hours a week figure to produce a projected hours-saved or pounds-saved number". Another said the total "is not to be combined" with the rate. That's the line's second sentence working, not just its first.

The sixth run with the line didn't give the total. The line allows it but doesn't require it, and one of six choosing not to isn't a failure of the line.

## How It Was Scored

I started each figure above with a search for candidates, then read every hit in context. You can't read a zero, because a search that finds nothing leaves nothing to read. So I checked each zero from more than one direction before trusting it. I searched for the pound figure as a £ amount, then in words, in thousands and without a symbol, before accepting that none of the 12 had one. For the seven runs without an hours total, I listed every hour figure each one states, and each states only the six hours per analyst. I later recounted in Python, which can't fail silently the way one search did in the [skill test](business-case-skill-second-line-test.md), and the counts match. The one hit on "hours saved" turned out, in context, to describe what the pilot would measure, not a forecast.

An earlier version of this page said every figure came from reading the runs. That claimed more than I'd done.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the pass mark myself.
- It says nothing about the skill. The line went into the prompt, where I'd measured the cost. The skill has the same guardrail and may suppress the same total on this scenario, but that's untested, so I haven't changed the skill.
- It says nothing about the Hartwell or Bramfield scenarios, where confirmed prices exist and the guardrail had already been shown not to block sound arithmetic.
- It says nothing about whether a reader would rather have the hours total. It measures whether one appears, not whether it helps.
- It isn't an independent test.

## The Change to Test Next

Whether the skill needs the same line. It has the same guardrail, and this scenario, where nothing is measured, is where the guardrail proved too blunt on the prompt. The pass mark and both guards carry over unchanged.

Now tested: [it does](business-case-skill-second-line-test.md), and I added the line to the skill.
