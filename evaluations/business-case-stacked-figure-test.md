# Business Case Stacked Figure: A Nineteen-Run Test

The [previous test](business-case-check-requirement-test.md) found a defect it wasn't looking for. In four of six runs, the Build a Business Case skill multiplied Tomasz's untimed estimate of six hours a week by Finance's rough £35 planning rate to get a single figure in pounds. One run turned that into £131,000 a year. This page tests a guardrail against that, the first change to this repository that a test has supported.

## The Guardrail

I added one line to the skill's guardrails:

> Never multiply two unmeasured figures together and present the product. If a calculation needs two inputs and either one is an estimate, a projection or an approximate planning rate, give the inputs separately with their labels and say what would have to be measured before a combined number means anything. Labelling the product as an estimate does not fix this: one number reads as more solid than the two guesses behind it, and a reader who skims will carry the number and leave the labels behind.

## Method

I ran the skill 19 times on the same [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with the same model, a fresh context each time, no rubric and no access to this repository. I removed the transcript's answer key first.

I made 16 of the runs for this test. The other three are the previous test's unchanged runs, which had neither the guardrail nor the warning note. Two had the defect. Every count here includes them.

The test, written down before any run: does the output contain a pound figure worked out from both the six-hour estimate and the £35 rate? Any such figure counts, weekly or yearly, whatever the caveats. The £35 rate alone doesn't. Nor do 72 analyst-hours a week, which is one estimate times a confirmed headcount.

I changed the design partway through. The first nine runs compared the published skill with the skill plus the guardrail, but both carried a note, added in the previous test, warning a human reader about this defect. A model reads that note too, so the comparison wasn't clean. I added seven runs: five with the guardrail and no warning, and two with neither.

## Result

| | No guardrail | Guardrail |
| --- | ---: | ---: |
| **No defect warning** | 3 of 5 | **0 of 5** |
| **Defect warning present** | 1 of 4 | 0 of 5 |

Nineteen runs. Fisher's exact test, one-tailed:

- The guardrail alone, against the plain skill: 0 of 5 against 3 of 5. p = 0.083.
- Guardrail against no guardrail, with or without the warning: 0 of 10 against 4 of 9. p = 0.033.
- The warning alone, against the plain skill: 1 of 4 against 3 of 5. p = 0.357.

**I'm keeping the guardrail.** None of the ten runs with it produced a combined figure. Four of the nine without it did.

I can't tell the warning note's effect from chance, so I make no claim for it. It stays as documentation for a reader.

I read five of the ten guardrail runs in full. Each quoted the six-hour estimate and the £35 rate under separate labels. Four said why they weren't combining them.

## A Mistake I Made Inside This Test

After the first nine runs I reported that the warning note "appears to have suppressed the defect on its own". That was wrong. I'd compared its 1 of 4 with the previous test's three plain runs, 2 of 3. Two more plain runs made that 3 of 5, and 1 of 4 against 3 of 5 means nothing. I'd read too much into three runs.

## The Worst Run of the Nineteen

One plain run produced £2,520 a week, turned it into £131,000 a year, then projected £65,000 a year of freed-up time from Tomasz's untested "half, maybe more". That's three figures from two unmeasured inputs and a hunch, in front of a CFO.

## One Guardrail Run, Scored in Full

[The first guardrail run](../examples/aldercroft-business-case-guardrail-output.md), picked as last time: the first run, not the best.

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

A second scorer would most likely disagree with me on the usefulness mark. The guardrail asks for refusing to combine the figures, not for keeping them well apart, which arguably costs the reader.

Two of my notes don't match the output. I said the out-of-scope aside stayed out of the case, but its Scope section names the accounts payable team and its matching problem. And the usefulness note says a CFO gets not even the inputs side by side, when the cost inputs list gives the six hours, the reduction and the £35 rate together. What's missing is any total.

## What This Test Cannot Prove

- One scenario, one model, and I scored every run after writing the guardrail. Nobody outside this project has scored anything.
- **The input wasn't as clean as the method says.** After I cut the answer key, a blockquote remained that called the champion's time estimate, one of the two figures under test, a live trap. It was the same in all four groups, so the comparison holds, but the overall rates may differ on a clean input. I never recorded where the pasted input started and stopped, so I can only infer these runs carried that sentence. I've since [fixed the blockquote](../examples/aldercroft-business-case-transcript.md).
- Nineteen runs is enough to support a change, not to measure its size. Zero of ten fits a defect that is rare rather than gone.
- It says nothing about the other two business case scenarios, where measured figures exist, so there may be nothing unmeasured to combine.

## Follow-Up: Is the Guardrail Too Blunt?

The scored Aldercroft run left a CFO with no sense of scale. If the guardrail also blocks sound arithmetic, it costs more than it saves. Aldercroft had nothing measured, so I used Hartwell and Bramfield, which both have a confirmed seat count and price per seat. The skill's Hartwell reference file says "the annual total can be calculated from it", so the repository expects the sum.

The test, fixed beforehand: does the output state a total cost worked out from the confirmed seat count and price? A run that gives both numbers and never combines them fails. If any did, I'd add runs without the guardrail. I ran the published skill, guardrail included, six times: three on each scenario.

| Scenario | Confirmed arithmetic produced | Figures given |
| --- | ---: | --- |
| Hartwell | 3 of 3 | £4,320 a year in all three, £360 a month in one |
| Bramfield | 3 of 3 | £18,720 year one in all three, £16,200 year two in two, £1,560 a month in two, £34,920 across both years in two |

**The guardrail isn't too blunt.** All six produced the combined total, and every figure is correct: eight at forty five is £360 a month and £4,320 a year; thirty at fifty two is £1,560 and £18,720; thirty at forty five is £1,350 and £16,200; the two years together are £34,920. None left out the sum, so by my rule I ran none without the guardrail.

All three Bramfield runs also tied the two-year condition to the year-two rate, the scenario's main trap. None of the six combined an unmeasured figure with money, so the guardrail still blocks what it should. The Aldercroft run's 4 for commercial usefulness was the scenario's doing, not the guardrail's. I blamed the instruction, and that looks wrong.

The limits: six runs, one model, scored by me against a test I wrote, though the Hartwell sum is the repository's expectation, not mine. I haven't published the six outputs, since they'd be clutter in `examples/`.

## The Change to Test Next

Nothing more for the skill at the time. Across 25 runs in total, the guardrail blocks what it was written to block and allows what it should.

The prompt never had this line, and [12 runs](business-case-prompt-guardrail-test.md) later found it producing the combined figure in five of six. The prompt now has the guardrail too. That test also found a cost this one only hinted at: on that scenario the line blocks the total hours figure it's meant to allow. The skill turned out to do the same, and a [second line](business-case-skill-second-line-test.md) fixed it there too.

I [tested the number of applied examples over 12 runs](business-case-applied-examples-test.md) and found nothing. Only the prompt asks for three, and six fresh runs of the skill each produced the one grounded example the scenario supports. The next change to test is on the prompt: whether its demand for three leads to padding on a source that supports one. Its single run didn't pad, and one run proves nothing. I [tested that over 12 runs](business-case-padding-test.md) and it doesn't pad.

## Corrections

The first version of this page didn't say that three of the 19 runs came from the previous test.
