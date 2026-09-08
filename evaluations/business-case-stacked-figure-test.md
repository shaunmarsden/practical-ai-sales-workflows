# Business Case Stacked Figure: A Nineteen-Run Test

The [previous test](business-case-check-requirement-test.md) found a defect worth fixing rather than the one it went looking for: four of six runs of the Build a Business Case skill multiplied Tomasz's untimed six-hour-a-week estimate by Finance's approximate £35 planning rate to produce a single pound figure. One annualised it to £131,000. This tests a guardrail against that, and it is the first change to this repository that a test has actually supported.

## The Guardrail

One line added to the skill's guardrails:

> Never multiply two unmeasured figures together and present the product. If a calculation needs two inputs and either one is an estimate, a projection or an approximate planning rate, give the inputs separately with their labels and say what would have to be measured before a combined number means anything. Labelling the product as an estimate does not fix this: one number reads as more solid than the two guesses behind it, and a reader who skims will carry the number and leave the labels behind.

## Method

Nineteen blind runs on the same [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), same model, a fresh isolated context each time, no rubric, no access to this repository, and the transcript's answer key removed first as its own warning instructs.

**The criterion was written down before any run:** does a currency figure derived from both the six-hour estimate and the £35 rate appear anywhere in the output? Any such figure counts, weekly or annual, however heavily it is caveated, because producing the number at all is the defect. Citing the £35 rate alone is not a yes. Citing 72 analyst-hours a week is not a yes either, since that is one estimate multiplied by a confirmed headcount rather than by another estimate.

**The design had to change mid-test, and the reason is worth recording.** The first nine runs compared the skill as published against the skill plus the guardrail. Both included a note added in the previous test warning a human reader that this defect exists. These files are pasted into a model as instructions, so a paragraph written for a reader also lands in the model's context, and that made the published version an impure control. Ten further runs were added to separate the two: a version with the guardrail and no warning, and more runs of the version with neither.

## Result

| | No guardrail | Guardrail |
| --- | ---: | ---: |
| **No defect warning** | 3 of 5 | **0 of 5** |
| **Defect warning present** | 1 of 4 | 0 of 5 |

Nineteen runs. Fisher's exact, one-tailed:

- **The guardrail on its own, against the plain baseline: 0 of 5 against 3 of 5.** p = 0.083.
- **The guardrail present against absent, collapsing over the warning: 0 of 10 against 4 of 9.** p = 0.033.
- The warning on its own, against the plain baseline: 1 of 4 against 3 of 5. p = 0.357.

**The guardrail is supported and is kept.** Ten runs carried it and none produced a combined figure. Nine did not and four did.

**The warning note's effect cannot be distinguished from noise** and no claim is made for it. It stays in the skill because it is honest documentation for a reader, not because it was shown to do anything.

All five guardrail runs engaged with both figures rather than dodging them. Each cited the six-hour estimate and the £35 rate, kept them apart with their own labels, and four said explicitly why they were not combining them. The fifth listed them as separate labelled inputs and simply never multiplied, which is the same behaviour without the commentary.

## A Mistake I Made Inside This Test

After the first nine runs I reported that the warning note "appears to have suppressed the defect on its own", and that it had possibly done more than the guardrail. That was wrong.

It rested on comparing the warning arm's 1 of 4 against a three-run baseline of 2 of 3. Two more baseline runs moved that cell to 3 of 5, and 1 of 4 against 3 of 5 is nothing at all. **I over-read a three-run baseline, which is the exact error this whole line of testing exists to avoid, made while running the test designed to avoid it.**

The general point about these files being dual-purpose still holds, because it is true by construction: documentation written into a skill file does reach the model. What does not hold is the claim that it changed the result here.

## The Worst Run of the Nineteen

One baseline run produced £2,520 a week, annualised it to £131,000, and then projected £65,000 a year of reclaimed capacity from Tomasz's untested "half, maybe more". Three derived figures from two unmeasured inputs and one gut feel, labelled as illustrative and put in front of a CFO.

That run came from the skill as it stood before the guardrail. It is the clearest single reason the change is worth having.

## One Guardrail Run, Scored in Full

[The first of the five](../examples/aldercroft-business-case-guardrail-output.md), chosen by the same rule as last time: the first run rather than the best.

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Headcount, rate, six-hour estimate, audit-trail requirement and the pilot ask all match the transcript |
| Evidence fidelity | 5 | Keeps the rate an approximate planning average, keeps the five unconfirmed analysts out of every figure, and keeps the reduction as a gut feel |
| Fact separation | 5 | Marks unknowns with a literal `unknown` label in a table, and heads its cost section "kept separate, not combined into a headline" |
| Missing information | 5 | Product name, start date, pricing, resourcing and the audit-trail mechanics all named as unknown |
| Commercial usefulness | 4 | Correctly sized ask and honest about what the pilot is for, but a CFO gets no cost magnitude at all, not even the two inputs left adjacent for her to combine herself |
| Next step clarity | 4 | Explicit that the document does not replace Priya's decision, but nobody is named as owning the measurement period |
| Tone | 5 | Third person, headed DRAFT, hedged in proportion to material that is almost entirely unmeasured |
| Privacy | 5 | No personal data, no individual analyst named, out-of-scope aside kept out of the case |
| Approval discipline | 5 | Titled as a draft requiring human review, with a checkbox list rather than assertions |
| Hallucination risk | 5 | Produces no combined figure, invents no product name, and says plainly there is nothing in the sources to draw one from |

The usefulness mark is where a second scorer is most likely to disagree with me. Refusing to combine the figures is what the guardrail asks for, and this run went further than the guardrail requires by not putting the two inputs anywhere near each other, which arguably costs the reader something the guardrail never intended to take away.

## What This Test Cannot Prove

- One scenario, one model, and every run scored by the person who wrote the guardrail. Nobody outside this project has scored anything.
- Nineteen runs is enough to support a change and nowhere near enough to size the effect. The guardrail arm is zero of ten, which is consistent with the defect being rare rather than eliminated.
- It says nothing about the other two business case scenarios, where the pilot has actually run and measured figures exist, so there may be nothing unmeasured to combine.
- It says nothing about whether the guardrail costs anything elsewhere. The usefulness mark above is one run's worth of a hint that it might.

## The Change to Test Next

Whether the guardrail is too blunt. The scored run above kept the two inputs in separate sections rather than adjacent with their labels, which is more than the instruction asks for and leaves a CFO with no sense of scale. Run the other two business case scenarios, where measured figures exist, and check the guardrail does not suppress arithmetic that is perfectly sound.
