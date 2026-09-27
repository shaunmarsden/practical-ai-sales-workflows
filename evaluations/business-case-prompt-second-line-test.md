# The Business Case Prompt's Second Line: A Twelve-Run Test

The [stacked-figure guardrail](business-case-prompt-guardrail-test.md) stopped the business case prompt producing a pound figure from two guesses, and measured what that cost: it also stopped the prompt giving the hours total, which that test's own criterion says is not the defect. The guardrail was adopted anyway, with the page saying plainly that the line was drawn too bluntly.

This tests a second line meant to redraw it. **It works: the hours total comes back in five of six runs, and the pound figure does not come back at all.**

## The Change

One line added directly after the existing guardrail in the prompt's Rules list:

> The one exception: an estimate may be multiplied by a confirmed count, such as an estimated time per person by a confirmed number of people, to give a total in the estimate's own unit, labelled as resting on that estimate. Do not then multiply that total by anything else unmeasured, whether an approximate rate or a hoped-for reduction: that is two unmeasured figures again, one step removed.

The second sentence matters as much as the first. On this scenario there are two routes back to the defect from a permitted total. Multiplying 72 hours by the approximate £35 rate rebuilds the pound figure one step later. Multiplying it by Tomasz's untested "half, maybe more" produces an hours-saved figure from two unmeasured inputs. The line has to close both, or permitting the total simply moves the defect.

## The Criterion and the Conditions

Written before either arm ran.

- **Primary, the hours total:** a total built from the six-hour estimate and the confirmed twelve analysts, such as 72 analyst-hours a week.
- **Guard one, the defect**, copied unchanged from the [stacked figure test](business-case-stacked-figure-test.md) and the guardrail test: a currency figure derived from both the six-hour estimate and the £35 rate, anywhere, however caveated.
- **Guard two, the reduction route:** anything multiplied by the untested reduction to give hours or money saved. Registered because a line permitting one multiplication could loosen another.

**Adopt** if the second line gives the hours total in four or more of six, the pound figure in one or fewer, and the reduction route no more often than the control. **Void** if the control gives the hours total in three or more, which would mean the guardrail alone had stopped suppressing it and there was nothing to restore.

## Method

Twelve blind runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md) with its answer key removed at the line its own warning names, the same scenario and model as both earlier tests, a fresh isolated context each time and no access to this repository.

Both arms were run fresh on the same day. The earlier test had already measured the guardrail on its own, but relying on runs from another session is how this repository once published a test with three reused runs undisclosed, so the published prompt was run again as a same-day control. Scored blind, under a mapping not opened until all twelve were scored.

## Result

| | Runs | Hours total | Pound figure | Reduction route |
| --- | ---: | ---: | ---: | ---: |
| Published prompt, guardrail only | 6 | **0** | 0 | 0 |
| With the second line | 6 | **5** | 0 | 0 |

**Adopted.** Every registered condition was met, and neither void condition fired. Fisher's exact, one-tailed, on five of six against none of six: p = 0.0076.

The control reproduced the earlier test exactly: no hours total and no pound figure in six runs, as before. So the same-day comparison and the cross-session one agree, and the result does not rest on either alone.

For comparison with the prompt before any guardrail, measured in the earlier test: four of six gave some aggregate scale and five of six produced the pound figure. The second line restores the hours total to at least that level while keeping the pound figure at none.

## What the Runs Actually Did

The five that gave the total all kept it in hours, labelled it as resting on the estimate, and several said explicitly why they would go no further. One wrote that it "does not combine that reduction estimate with the seventy-two hours a week figure to produce a projected hours-saved or pounds-saved number". Another said the total "is not to be combined" with the rate. Those are the second sentence of the line doing its job, not just the first.

The sixth run with the line did not give the total. The line permits it rather than requiring it, and one of six choosing not to is not a failure of the line.

## How It Was Scored

Every figure above comes from reading the runs, and the zeros were checked from more than one direction before being trusted. The pound figure was searched as a £ amount, then as amounts written in words, in thousands and without a symbol, before accepting that none of twelve contained one. The seven runs without an hours total were each read for a total written some other way, and each states only the per-analyst six hours. The one hit on "hours saved" was read in context and turned out to describe what the pilot would measure, not a projection.

## What This Test Cannot Prove

- Six runs an arm, one scenario, one model, a criterion written and applied by the same person.
- It says nothing about the skill. The line went into the prompt, where the cost was measured. The skill carries the same guardrail and may suppress the same total on this scenario, but that is untested, so the skill is unchanged.
- It says nothing about the Hartwell or Bramfield scenarios, where confirmed prices exist and the guardrail was already shown not to suppress sound arithmetic.
- It says nothing about whether a reader would rather have the hours total than not. It measures whether one appears, not whether it helps.
- It is not an independent external test.

## The Change to Test Next

Whether the skill needs the same line. It carries the same guardrail, and this scenario, where nothing is measured, is the one where the guardrail was shown to be too blunt on the prompt. The criterion and both guards transfer unchanged.
