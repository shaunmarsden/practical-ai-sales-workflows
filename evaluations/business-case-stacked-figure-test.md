# Business Case Stacked Figure: A Nineteen-Run Test

The [previous test](business-case-check-requirement-test.md) found a different defect from the one it was looking for. In four of six runs, the Build a Business Case skill multiplied Tomasz's untimed estimate of six hours a week by Finance's rough £35 planning rate to get a single figure in pounds. One run turned that into £131,000 a year. This page tests a guardrail against that. It's the first change to this repository that a test has supported.

## The Guardrail

I added one line to the skill's guardrails:

> Never multiply two unmeasured figures together and present the product. If a calculation needs two inputs and either one is an estimate, a projection or an approximate planning rate, give the inputs separately with their labels and say what would have to be measured before a combined number means anything. Labelling the product as an estimate does not fix this: one number reads as more solid than the two guesses behind it, and a reader who skims will carry the number and leave the labels behind.

## Method

I ran the skill 19 times on the same [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with the same model and a fresh context each time. Each run had no rubric and no access to this repository. I removed the transcript's answer key first, as its own warning says to.

I made 16 of the 19 runs for this test. The other three are the previous test's three unchanged runs. I reused them because they had neither the guardrail nor the warning note, so they belong with the plain skill. Two of those three had the defect. Every count on this page includes them.

Before any run, I wrote down the test: does the output contain a pound figure worked out from both the six-hour estimate and the £35 rate? Any such figure counts, weekly or yearly, however many caveats surround it, because producing the number at all is the defect. Quoting the £35 rate alone doesn't count. Nor does quoting 72 analyst-hours a week, since that's one estimate multiplied by a confirmed headcount, not by another estimate.

I had to change the design partway through. The first nine runs compared the published skill with the skill plus the guardrail. Both had a note, added in the previous test, warning a human reader about this defect. People paste these files into a model as instructions, so a note for a reader reaches the model too. The published version wasn't a clean comparison.

So I added seven runs: five with the guardrail and no warning, and two more with neither. That took the plain skill from three runs to five.

## Result

| | No guardrail | Guardrail |
| --- | ---: | ---: |
| **No defect warning** | 3 of 5 | **0 of 5** |
| **Defect warning present** | 1 of 4 | 0 of 5 |

Nineteen runs. Fisher's exact test, one-tailed:

- The guardrail alone, against the plain skill: 0 of 5 against 3 of 5. p = 0.083.
- Guardrail against no guardrail, with or without the warning: 0 of 10 against 4 of 9. p = 0.033.
- The warning alone, against the plain skill: 1 of 4 against 3 of 5. p = 0.357.

**I'm keeping the guardrail.** Ten runs had it and none produced a combined figure. Nine didn't and four did.

I can't tell the warning note's effect from chance, so I make no claim for it. It stays in the skill because it's useful documentation for a reader, not because it did anything.

I read five of the ten guardrail runs in full. None avoided the figures. Each quoted the six-hour estimate and the £35 rate and kept them apart with their own labels. Four said why they weren't combining them. The fifth listed them as separate inputs and never multiplied them, which is the same thing without the comment.

## A Mistake I Made Inside This Test

After the first nine runs I reported that the warning note "appears to have suppressed the defect on its own", and that it might have done more than the guardrail. That was wrong.

I'd compared the warning version's 1 of 4 with the previous test's three unchanged runs, 2 of 3. Two more plain runs moved that to 3 of 5, and 1 of 4 against 3 of 5 means nothing. I read too much into three runs, the error this line of testing exists to avoid, while running the test designed to avoid it.

It's still true that documentation in a skill file reaches the model. It isn't true that it changed the result here.

## The Worst Run of the Nineteen

One plain run produced £2,520 a week, turned it into £131,000 a year, then projected £65,000 a year of freed-up time from Tomasz's untested "half, maybe more". That's three figures from two unmeasured inputs and a hunch, labelled as illustrative and put in front of a CFO.

That run used the skill as it was before the guardrail. It's the clearest reason the change is worth having.

## One Guardrail Run, Scored in Full

[The first guardrail run](../examples/aldercroft-business-case-guardrail-output.md), picked by the same rule as last time: the first run, not the best.

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Headcount, rate, six-hour estimate, audit-trail requirement and the pilot ask all match the transcript |
| Evidence fidelity | 5 | Keeps the rate a rough planning average, keeps the five unconfirmed analysts out of every figure, and keeps the reduction as a hunch |
| Fact separation | 5 | Marks unknowns with a literal `unknown` label in a table, and heads its cost section "kept separate, not combined into a headline" |
| Missing information | 5 | Names product name, start date, pricing, resourcing and how the audit trail works as unknown |
| Commercial usefulness | 4 | Asks for the right size of pilot and is honest about what it's for, but a CFO gets no sense of cost at all, not even the two inputs side by side to combine herself |
| Next step clarity | 4 | Says the document doesn't replace Priya's decision, but names nobody as owning the measurement period |
| Tone | 5 | Third person, headed DRAFT, hedged in line with material that is almost entirely unmeasured |
| Privacy | 5 | No personal data, no analyst named, out-of-scope aside kept out of the case |
| Approval discipline | 5 | Titled as a draft needing human review, with a checkbox list rather than assertions |
| Hallucination risk | 5 | Produces no combined figure, invents no product name, and says there is nothing in the sources to draw one from |

The usefulness mark is where a second scorer would most likely disagree with me. Refusing to combine the figures is what the guardrail asks for. This run went further and kept the two inputs well apart, which arguably costs the reader something the guardrail never meant to take away.

## What This Test Cannot Prove

- One scenario, one model, and I scored every run after writing the guardrail. Nobody outside this project has scored anything.
- **The input wasn't as clean as the method above says.** I cut the answer key where the transcript's warning says to, but that left in a blockquote saying the example was fictional. It called the champion's time estimate a live trap, and that estimate is one of the two figures under test. It was the same in all four groups, so the comparison holds, but the overall rates may differ from a clean input. I never recorded where the pasted input started and stopped, so I can only infer that these 19 runs carried that sentence. I've since [fixed the blockquote](../examples/aldercroft-business-case-transcript.md).
- Three of the 19 weren't made for this test. They fit the plain group because they had neither change, but they were made for a different question, and the first version of this page didn't say so.
- Nineteen runs is enough to support a change and nowhere near enough to measure the size of the effect. The guardrail version scored zero of ten, which fits a defect that is rare rather than gone.
- It says nothing about the other two business case scenarios. There the pilot has run and measured figures exist, so there may be nothing unmeasured to combine.
- It says nothing about whether the guardrail costs anything elsewhere. The usefulness mark above is one run's hint that it might.

## Follow-Up: Is the Guardrail Too Blunt?

I named this above as the next thing to test, and I've tested it.

The scored Aldercroft run kept the two inputs in separate sections and left a CFO with no sense of scale. If the guardrail also blocks sound arithmetic, it costs more than it saves.

Aldercroft had nothing measured, so I used Hartwell and Bramfield. Both have a confirmed seat count and a confirmed price per seat. The skill's own reference file for Hartwell says "the annual total can be calculated from it", so the repository expects the sum, not just me.

Before any run I fixed the test: does the output state a total cost worked out from the confirmed seat count and price per seat? A run that gives both numbers and never combines them fails. I also decided in advance that if any run left out the sum, I'd add runs without the guardrail, because otherwise I couldn't blame the guardrail for the gap.

I ran the published skill, guardrail included, six times: three on each scenario.

| Scenario | Confirmed arithmetic produced | Figures given |
| --- | ---: | --- |
| Hartwell | 3 of 3 | £4,320 a year in all three, £360 a month in one |
| Bramfield | 3 of 3 | £18,720 year one in all three, £16,200 year two in two, £1,560 a month in two, £34,920 across both years in two |

**The guardrail isn't too blunt.** All six produced the combined total, and every figure is correct: eight at forty five is £360 a month and £4,320 a year; thirty at fifty two is £1,560 and £18,720; thirty at forty five is £1,350 and £16,200; the two years together are £34,920.

No runs without the guardrail were needed, so by the rule I set beforehand I ran none.

I checked two other things while the outputs were open. All three Bramfield runs tied the two-year condition to the year-two rate. That's the scenario's main trap, and its reference file warns that dropping it misstates the commercial terms. And none of the six combined an unmeasured figure with money, so the guardrail still blocks what it should.

This changes how I read the earlier usefulness mark. The Aldercroft run scored 4 for commercial usefulness because a CFO got no sense of scale. On this evidence the scenario caused that, not the guardrail. Aldercroft has nothing measured to combine, so refusing was right. I blamed the instruction, and that looks wrong.

The limits: six runs, one model, scored by me against a test I wrote, though the Hartwell sum is the repository's expectation, not mine. I haven't published the six outputs. The finding is the counts, and five more business case documents in `examples/` would be clutter, not evidence. I kept the raw outputs while scoring.

## The Change to Test Next

Nothing more on this for the skill. Over 25 runs in total, the guardrail blocks what it was written to block and allows what it should.

**The prompt was different.** It never had this line, and [12 runs](business-case-prompt-guardrail-test.md) later found it producing the combined figure in five of six. The prompt now has the guardrail too. That test measured a cost this one only hinted at: on this scenario the line also blocks the total hours figure it's meant to allow.

The one open question about this skill was the number of applied examples. I [tested it over 12 runs](business-case-applied-examples-test.md) and found nothing. The skill only ever said three was a good number, the prompt is what asks for three, and six fresh runs of the published skill each produced the one grounded example the scenario supports.

**The next change to test is on the prompt, not the skill:** whether its strict demand for three applied examples leads to padding on a source that supports one. Its single run didn't pad, and one run proves nothing either way.
