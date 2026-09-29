# The Stacked-Figure Guardrail on the Prompt: A Twelve-Run Test

The [padding test](business-case-padding-test.md) looked for one defect, found none, and turned up another. Nine of its 12 runs of the business case prompt produced a pound figure built from Tomasz's untimed six-hour estimate and Finance's rough £35 rate. The skill had a guardrail against that, but the prompt didn't, and the prompt is what the [recipe card](../recipes/build-a-business-case.md) carries.

So I added the skill's line to the prompt and tested it, rather than assuming a line that worked in one place works in another. **It works, and it has a cost that my test allows.**

## The Change

I added one bullet to the prompt's Rules list, copied from the skill unchanged:

> Never multiply two unmeasured figures together and present the product. If a calculation needs two inputs and either one is an estimate, a projection or an approximate planning rate, give the inputs separately with their labels and say what would have to be measured before a combined number means anything. Labelling the product as an estimate does not fix this: one number reads as more solid than the two guesses behind it, and a reader who skims will carry the number and leave the labels behind.

## What I Decided in Advance

I copied the test from the [stacked figure test](business-case-stacked-figure-test.md) unchanged, so the two can be compared. Does a pound figure worked out from both the six-hour estimate and the £35 rate appear anywhere in the output? Any such figure counts, weekly or yearly, however many caveats surround it. Quoting the £35 rate alone doesn't count. **Nor does quoting 72 analyst-hours a week**, since that's one estimate multiplied by a confirmed headcount, not by another estimate.

If three or more of the six guardrail runs produced the figure, the line doesn't carry over to the prompt. The skill's ten guardrail runs produced none, so three of six would be a clear failure.

If two or fewer of the six runs without it produced the figure, the plain prompt would have moved a long way from the nine of 12 I'd measured on this prompt and scenario an hour earlier, and the test wouldn't count.

## Method

I made 12 runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with the answer key removed at the line its own warning names. I used the same model and a fresh context each time, with no rubric and no access to this repository. Six used the prompt as it stood, and six had the bullet added. I ran both fresh, and scored them without knowing which version each came from.

## Result

| | Runs | Combined figure | Annualised it | Gave any aggregate scale |
| --- | ---: | ---: | ---: | ---: |
| Prompt without the guardrail | 6 | **5** | 4 | 4 |
| Prompt with the guardrail | 6 | **0** | 0 | **0** |

**Neither rule was triggered, so I adopted the guardrail.** Fisher's exact test, one-tailed, on five of six against none of six: p = 0.015. The plain prompt's five of six fits the nine of 12 from the previous test on the same prompt and scenario.

Four of the five combined figures were turned into a yearly figure of about £131,000. Two went on to project roughly £65,000 a year of freed-up time from an untested "half, maybe more". That's the run the [mistakes guide](../guides/which-ai-mistakes-get-through.md) opens with, repeated here twice in six runs of a published prompt.

## The Cost, Now Measured

**No guardrail run gave a reader any overall sense of scale.** It rightly left out the combined pound figure. But it also left out the 72 analyst-hours a week, which is one estimate multiplied by a confirmed headcount, and which my own test says isn't the defect. Four of the six runs without the guardrail gave it. One-tailed p = 0.061.

The [stacked figure test](business-case-stacked-figure-test.md) hinted at this from one scored run, which lost a usefulness mark because a CFO got no sense of size. Its follow-up then found the guardrail wasn't too blunt on the two scenarios with measured prices. **On this scenario it's blunter than my test asks for**, and that's now a count, not a hint.

I still adopted the guardrail. Producing £131,000 from two guesses is worse than leaving out a fair hours total, and the only other option today is the prompt as it stands. I don't claim the line is drawn in the right place.

## Two Things That Didn't Move

**Every run in both versions produced exactly one applied example**, and none produced a second. The padding test's finding held on 12 fresh runs.

**No run in either version invented a product name, a price or a start date**, the details the transcript never gives.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the test myself.
- It says nothing about the Hartwell or Bramfield scenarios, where confirmed prices exist and the skill's version of this guardrail didn't block sound arithmetic. The cost here may be specific to a scenario with nothing measured.
- I planned to count the overall scale in advance, but it wasn't the test, and p = 0.061 on six a side isn't a result.
- It says nothing about whether a reader would rather have the hours total. That's a judgement about the document. This measures only whether one appears.

## The Change to Test Next

Whether a second line brings back the hours total without bringing back the pound figure. It would allow a total built from an estimate and a confirmed count, while still forbidding one built from two estimates. The test is already written for both versions, and this page gives the starting point for both.
