# The Stacked-Figure Guardrail on the Prompt: A Twelve-Run Test

The [padding test](business-case-padding-test.md) went looking for one defect, found none, and turned up another: nine of its twelve runs of the business case prompt produced a pound figure built from Tomasz's untimed six-hour estimate and Finance's approximate £35 rate. The guardrail against that was in the skill and not in the prompt, and the prompt is what the [recipe card](../recipes/build-a-business-case.md) carries.

This adds the skill's line to the prompt and tests it, rather than assuming a line that worked on one artefact works on another. **It works, and it costs something the criterion explicitly permits.**

## The Change

One bullet added to the prompt's Rules list, copied from the skill unchanged:

> Never multiply two unmeasured figures together and present the product. If a calculation needs two inputs and either one is an estimate, a projection or an approximate planning rate, give the inputs separately with their labels and say what would have to be measured before a combined number means anything. Labelling the product as an estimate does not fix this: one number reads as more solid than the two guesses behind it, and a reader who skims will carry the number and leave the labels behind.

## The Criterion and the Conditions

**The criterion** is the [stacked figure test's](business-case-stacked-figure-test.md), copied unchanged so the two are comparable: does a currency figure derived from both the six-hour estimate and the £35 rate appear anywhere in the output? Any such figure counts, weekly or annual, however heavily it is caveated. Citing the £35 rate alone is not a yes. **Citing 72 analyst-hours a week is not a yes either**, since that is one estimate multiplied by a confirmed headcount rather than by another estimate.

**The falsification condition:** three or more of six in the guardrail arm and the line does not transfer to this artefact. The skill's ten guardrail runs produced none, so three of six would be a clear failure to reproduce.

**The void condition:** two or fewer of six in the arm without it, meaning the baseline has moved a long way from the nine of twelve measured on this prompt and scenario an hour earlier.

## Method

Twelve blind runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md) with its answer key removed at the line its own warning names, same model, a fresh isolated context each time, no rubric and no access to this repository. Six of the prompt as it stood, six with the bullet added. Both arms fresh. Scored without knowing which arm each run came from.

## Result

| | Runs | Combined figure | Annualised it | Gave any aggregate scale |
| --- | ---: | ---: | ---: | ---: |
| Prompt without the guardrail | 6 | **5** | 4 | 4 |
| Prompt with the guardrail | 6 | **0** | 0 | **0** |

**Neither condition fired, so the guardrail is adopted.** Fisher's exact, one-tailed, on five of six against none of six: p = 0.015. The baseline arm at five of six is consistent with the nine of twelve measured on the same prompt and scenario in the previous test.

Four of the five combined figures were annualised, to about £131,000. Two went on to project roughly £65,000 a year of reclaimed capacity from an untested "half, maybe more", which is the run the [mistakes guide](../guides/which-ai-mistakes-get-through.md) leads with, reproduced here twice in six runs of a published prompt.

## The Cost, Which Is Now Measured Rather Than Suspected

**No run carrying the guardrail gave a reader any aggregate sense of scale at all.** Not the combined pound figure, correctly, but also not the seventy-two analyst-hours a week, which is one estimate multiplied by a confirmed headcount and which this test's own criterion says explicitly is not the defect. Four of the six runs without the guardrail gave it. One-tailed p = 0.061.

The [stacked figure test](business-case-stacked-figure-test.md) hinted at this from a single scored run, which lost a usefulness mark because a CFO got no magnitude at all, and then its follow-up concluded the guardrail was not too blunt on the two scenarios that have measured prices. **On this scenario it is blunter than the criterion asks for**, and that is now a count rather than a hint.

The guardrail is still adopted, because producing £131,000 from two guesses is a worse fault than omitting a legitimate hours total, and because the alternative on offer today is the prompt as it stands. What this page does not claim is that the line is correctly drawn.

## Two Things That Did Not Move

**Every run in both arms produced exactly one applied example**, and none produced a second. The padding test's finding replicates on twelve fresh runs.

**Nothing in either arm invented a product name, a price or a start date**, the details the transcript never supplies.

## What This Test Cannot Prove

- Six runs an arm, one scenario, one model, and a criterion written and applied by the same person.
- It says nothing about the Hartwell or Bramfield scenarios, where confirmed prices exist and the skill's version of this guardrail was shown not to suppress sound arithmetic. The cost measured here may be specific to a scenario with nothing measured in it.
- The aggregate-scale count is an observation registered in advance, not the criterion, and p = 0.061 on six a side is not a result.
- It says nothing about whether a reader would rather have the hours total than not. That is a judgement about the document, and this measures only whether one appears.

## The Change to Test Next

Whether a second line, permitting an aggregate built from an estimate and a confirmed count while still forbidding one built from two estimates, restores the hours total without bringing back the pound figure. The criterion is already written on both sides, and this page is the baseline for both.
