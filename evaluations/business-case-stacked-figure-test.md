# Business Case Stacked Figure: A Nineteen-Run Test

The [previous test](business-case-check-requirement-test.md) found a defect worth fixing rather than the one it went looking for: four of six runs of the Build a Business Case skill multiplied Tomasz's untimed six-hour-a-week estimate by Finance's approximate £35 planning rate to produce a single pound figure. One annualised it to £131,000. This tests a guardrail against that, and it is the first change to this repository that a test has actually supported.

## The Guardrail

One line added to the skill's guardrails:

> Never multiply two unmeasured figures together and present the product. If a calculation needs two inputs and either one is an estimate, a projection or an approximate planning rate, give the inputs separately with their labels and say what would have to be measured before a combined number means anything. Labelling the product as an estimate does not fix this: one number reads as more solid than the two guesses behind it, and a reader who skims will carry the number and leave the labels behind.

## Method

Nineteen blind runs on the same [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), same model, a fresh isolated context each time, no rubric, no access to this repository, and the transcript's answer key removed first as its own warning instructs.

**Sixteen of the nineteen were made for this test.** The other three are the previous test's three unmodified runs, reused because they carried neither the guardrail nor the warning note and so belong in the plain baseline cell. Two of those three produced the defect. Every count on this page includes them.

**The criterion was written down before any run:** does a currency figure derived from both the six-hour estimate and the £35 rate appear anywhere in the output? Any such figure counts, weekly or annual, however heavily it is caveated, because producing the number at all is the defect. Citing the £35 rate alone is not a yes. Citing 72 analyst-hours a week is not a yes either, since that is one estimate multiplied by a confirmed headcount rather than by another estimate.

**The design had to change mid-test, and the reason is worth recording.** The first nine runs compared the skill as published against the skill plus the guardrail. Both included a note added in the previous test warning a human reader that this defect exists. These files are pasted into a model as instructions, so a paragraph written for a reader also lands in the model's context, and that made the published version an impure control. Seven further runs were added to separate the two: five of a version with the guardrail and no warning, and two more of the version with neither, which is what took the plain baseline cell from three runs to five.

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

Five of the ten guardrail runs were read in full rather than only checked against the criterion, and all five engaged with both figures rather than dodging them. Each cited the six-hour estimate and the £35 rate, kept them apart with their own labels, and four said explicitly why they were not combining them. The fifth listed them as separate labelled inputs and simply never multiplied, which is the same behaviour without the commentary.

## A Mistake I Made Inside This Test

After the first nine runs I reported that the warning note "appears to have suppressed the defect on its own", and that it had possibly done more than the guardrail. That was wrong.

It rested on comparing the warning arm's 1 of 4 against the previous test's three unmodified runs, 2 of 3. Two more baseline runs moved that cell to 3 of 5, and 1 of 4 against 3 of 5 is nothing at all. **I over-read a three-run baseline, which is the exact error this whole line of testing exists to avoid, made while running the test designed to avoid it.**

The general point about these files being dual-purpose still holds, because it is true by construction: documentation written into a skill file does reach the model. What does not hold is the claim that it changed the result here.

## The Worst Run of the Nineteen

One baseline run produced £2,520 a week, annualised it to £131,000, and then projected £65,000 a year of reclaimed capacity from Tomasz's untested "half, maybe more". Three derived figures from two unmeasured inputs and one gut feel, labelled as illustrative and put in front of a CFO.

That run came from the skill as it stood before the guardrail. It is the clearest single reason the change is worth having.

## One Guardrail Run, Scored in Full

[The first guardrail run](../examples/aldercroft-business-case-guardrail-output.md), chosen by the same rule as last time: the first run rather than the best.

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
- **The input was not as clean as the method above claims.** Removing the answer key at the line the transcript's own warning names left its fictional-disclosure blockquote in place, and that blockquote said the champion's time estimate was a live trap. The time estimate is one of the two figures this test is about. It was constant across all four cells, so the comparison holds, but the absolute rates may not be what a genuinely blind input would give. This page never recorded where the pasted input started and stopped, so whether these nineteen runs carried that sentence cannot be confirmed now, only inferred from the procedure they followed. The [blockquote has since been fixed](../examples/aldercroft-business-case-transcript.md).
- Three of the nineteen were not made for this test. They fit the plain baseline cell because they carried neither variable, but they were produced against a different question, and the first version of this page did not say so.
- Nineteen runs is enough to support a change and nowhere near enough to size the effect. The guardrail arm is zero of ten, which is consistent with the defect being rare rather than eliminated.
- It says nothing about the other two business case scenarios, where the pilot has actually run and measured figures exist, so there may be nothing unmeasured to combine.
- It says nothing about whether the guardrail costs anything elsewhere. The usefulness mark above is one run's worth of a hint that it might.

## Follow-Up: Is the Guardrail Too Blunt?

The section above named this as the next thing to test, and it has been tested.

**The worry.** The scored Aldercroft run refused so thoroughly that it kept the two inputs in separate sections and left a CFO with no sense of scale. If the guardrail also suppresses arithmetic that is perfectly sound, it costs more than it saves.

**Why Hartwell and Bramfield test it.** Aldercroft had nothing measured. These two both carry a confirmed seat count and a confirmed per-seat price, and the skill's own reference file for Hartwell says outright that "the annual total can be calculated from it", so the arithmetic is expected by this repository rather than by me.

**The criterion, fixed before any run:** does the output state a total cost derived from the confirmed seat count and the confirmed per-seat price? A run that gives both numbers and never combines them is a no. The contingency was fixed in advance too: if any run omitted the arithmetic, control runs without the guardrail would be added, because otherwise an omission cannot be pinned on the guardrail.

**Six blind runs of the published skill, guardrail included, three on each scenario.**

| Scenario | Confirmed arithmetic produced | Figures given |
| --- | ---: | --- |
| Hartwell | 3 of 3 | £4,320 a year in all three, £360 a month in one |
| Bramfield | 3 of 3 | £18,720 year one in all three, £16,200 year two in two, £1,560 a month in two, £34,920 across both years in two |

**The guardrail is not too blunt.** Every one of the six produced the combined total, and every figure is arithmetically correct: eight at forty five is £360 a month and £4,320 a year; thirty at fifty two is £1,560 and £18,720; thirty at forty five is £1,350 and £16,200; the two years together are £34,920.

No control arm was needed, and by the contingency set beforehand none was run.

**Two things checked while the outputs were open, neither of them the criterion.** All three Bramfield runs attached the two-year condition to the year-two rate, which is that scenario's headline trap and the thing its reference file warns misrepresents the commercial terms if dropped. And none of the six combined an unmeasured figure with money, so the guardrail still bites where it should.

**What this says about the earlier usefulness mark.** The Aldercroft run scored 4 for commercial usefulness because a CFO got no sense of scale. On this evidence that was the scenario, not the guardrail. Aldercroft has nothing measured to combine, so refusing was correct and the missing scale is the source material's fault. I attributed it to the instruction and that looks wrong.

**Limits.** Six runs, one model, scored by me against a criterion I wrote, though the Hartwell arithmetic expectation is the repository's own rather than mine. The six outputs are not published: the finding is the counts, and five more business case documents in `examples/` would be clutter rather than evidence. Raw outputs were retained while scoring.

## The Change to Test Next

Nothing on this thread. The guardrail blocks what it was written to block and permits what it should permit, over twenty-five runs in total.

The one question left open about this skill was the applied examples count, and it was [tested over twelve runs](business-case-applied-examples-test.md) and came to nothing. The skill only ever said three was a good number, the prompt is the artefact that asks for three, and six fresh runs of the published skill each produced the one grounded example the scenario supports.

**The next change to test is on the prompt rather than the skill:** whether its hard requirement for three applied examples causes padding on a source that supports one. Its single run did not pad, and one run is not evidence either way.
