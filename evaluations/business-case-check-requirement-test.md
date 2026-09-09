# Business Case Check Requirement: A Six-Run Test

This page reports a test that failed to support the change it was written for, and corrects something this repository published two days of work ago.

## What Was Being Tested

The [business case prompt review](aldercroft-business-case-prompt-review.md) said that the prompt scoring three points above the skill on the Aldercroft scenario was probably my own design choice rather than the model's judgement. The prompt makes a human-check section a required numbered part; the skill did not list one. The skill's single published run did not flag that no pilot cost figure was ever established, and the prompt's run did.

So one line was added to the skill's list of required document parts:

> **Human check section**: present, and it must list every figure, claim and section a person has to confirm before the document is sent, plus anything left as an `unknown`. A figure the sources never established counts as something to confirm even when no section of the document is currently claiming it, so an absent price, rate or date belongs on this list rather than being left silent.

And then it was tested, rather than assumed to work.

## Method

Six blind runs on the same [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), same model, a fresh isolated context each time, no rubric, no access to this repository, and the transcript's answer key removed first as its own warning instructs.

- Three runs given the skill exactly as published before the change
- Three runs given the skill with that one line added, and nothing else altered

Three each rather than one each, because a one against one comparison could not separate the instruction from run to run variance. This repository has already measured identical prompts on identical input [moving by one to three points](repeat-run-findings.md), and a [nine-run test](hartwell-objection-ambiguous-test.md) in which the same model reached a different primary diagnosis every time.

**The criterion was written down before any run and is reproduced here unchanged:** does the output state anywhere that no pilot cost, price or commercial figure was established, or otherwise name the absent pilot cost as something a person must confirm? A document that simply leaves a commercial section out silently counts as a no.

**The falsification condition was also fixed in advance:** if the unmodified skill flags the absent pilot cost in two or three of its runs, the original miss was a one-run event and the added line is not what changed it.

## Result

| Run | Skill | Named the absent pilot cost |
| --- | --- | --- |
| 1 | As published | Yes |
| 2 | As published | Yes |
| 3 | As published | **No** |
| 1 | With the line | Yes |
| 2 | With the line | Yes |
| 3 | With the line | Yes |

**Two of three unmodified runs already flagged it. The falsification condition was met, so the hypothesis is rejected.**

The published Aldercroft record's miss was inside the skill's own variation. It was not caused by the absence of an instruction, and the added line is not what fixed it.

## The Claim This Corrects

The business case prompt review said the required check section was "the most likely reason the pilot-cost gap got caught here and not there". That was wrong, and it was wrong in the direction that made my own new prompt look better than the older skill.

It was also wrong about the mechanism. The review said the skill "leaves that to be produced voluntarily", implying the section itself was sometimes missing. **All three unmodified runs produced a human-check section without being told to**, headed "Figures to Confirm Before This Goes to Priya", "For Confirmation Before This Goes to Priya" and "Before This Is Sent, Internal Confirmation Checklist". The section was never the variable. What varies is what gets into it.

## What the Six Runs Did Show

**A worse failure than the one being chased, in the published skill.** Run 3 of the unmodified skill missed the pilot cost and also produced an annualised figure of £131,000 built from two unmeasured inputs, Tomasz's untimed six-hour estimate multiplied by Finance's approximate planning rate. That is the largest invented-looking number in any of the six, and it came from the version of the skill that is published.

**The stacked figure is not variance, it is the norm.** Four of the six runs multiplied the two unmeasured inputs into a pound figure: two of three before the change and two of three after it. The added line does not address that and did not change it. The published Aldercroft review lost a hallucination-risk mark for exactly this, on a £65,520 figure, and the defect has now been reproduced four times in six runs.

**Every one of the six runs used em dashes, and that has a consequence for every published output here.** The counts were thirteen, fourteen, fifteen, seventeen, twenty and twenty-three. This skill did not tell the model to avoid them, and at the time only four of the seventeen skills and four of the twenty-one prompt templates did. The [chase sequence prompt](../templates/chase-sequence-prompt.md), which carries the rule, produced none in its own run.

This repository's style rule forbids em dashes and a CI check enforces it across every tracked Markdown and HTML file, including published outputs. The published Aldercroft output from this same skill contains none. Six of six fresh runs producing between thirteen and twenty-three makes it unlikely that run genuinely produced zero, and **no example file here discloses a punctuation conversion.** I cannot prove any published output was edited, and I am not asserting it. What I can state is the arithmetic: the character cannot survive CI, the model produces it reliably, and nothing in `examples/` says it was removed. The sibling repository's equivalent page does disclose exactly that, in one sentence.

The [output published alongside this test](../examples/aldercroft-business-case-check-requirement-output.md) discloses it, and says which replacements were my judgement rather than a mechanical swap.

This was acted on. All seventeen skills now carry the rule, [tested over thirty-three runs](em-dash-rule-test.md), and a check stops a new skill shipping without it.

**Nothing produces three applied examples.** Across six runs the count was one, zero, zero, one, zero and one. The published Aldercroft review never flagged this, which the prompt review already recorded as a gap in my scoring rather than in any output.

> **Correction.** This section originally said that both the skill and the prompt ask for three, and treated the counts as an instruction being ignored. Only the prompt asks for three. The skill says "three is a good number", and all six of these runs were runs of the skill. Six fresh runs of the published skill later produced at least one grounded example every time, so the gap the counts pointed at did not reproduce. See the [applied examples test](business-case-applied-examples-test.md).

## What Happened to the Change

**The line was kept, and it is labelled as weakly evidenced rather than as a fix.**

Keeping it is a judgement call and worth stating plainly. Against it: the hypothesis that motivated it was rejected, and three runs each cannot distinguish three from three against two from three. For it: run 3 of the unmodified skill is a real instance of exactly the failure the line describes, an absent price left silent, and the modified runs did not reproduce it.

So it stays as a clarification of something the skill's evidence labels already imply, not as a demonstrated improvement. If you would rather this repository carried no unevidenced changes at all, reverting one line is the whole cost of that.

## One Modified Run, Scored in Full

Scored for the record, on the run named in advance rather than the best of the three: [the first modified run](../examples/aldercroft-business-case-check-requirement-output.md).

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Headcount, rate, six-hour estimate, audit-trail requirement and the pilot-not-rollout ask all match the transcript |
| Evidence fidelity | 5 | Every condition survives, including the excluded future headcount and the out-of-scope accounts payable aside |
| Fact separation | 5 | The derived figures are labelled as built on two unverified inputs at the point they appear, not only where the inputs were introduced |
| Missing information | 5 | Pilot investment, start date, measurement period length and wider resourcing all named as unknown |
| Commercial usefulness | 5 | Correctly sized ask, and it gives the pilot four measurable success indicators to be judged against later |
| Next step clarity | 4 | Explicit that sending is not approval, but nobody is named as owning the job of agreeing the measurement period |
| Tone | 5 | Third person for a CFO reader who was not on the call, hedged in proportion to the material |
| Privacy | 5 | No personal data, and the out-of-scope aside stays out of the case itself |
| Approval discipline | 5 | Checkboxes rather than assertions, and it states that the document being sent is not approval |
| Hallucination risk | 4 | Labels the stacked £2,520 and £1,260 figures heavily and offers to cut them, but still produces them, which is the same defect the published run lost this mark for |

## What This Test Cannot Prove

- Three runs per arm. It can reject a strong claim, which it did, but it cannot establish a small effect. Three from three against two from three is not a result.
- One scenario, one model, and every run scored by the same person, who also wrote the change being tested. Nobody outside this project has scored anything.
- It says nothing about the other two business case scenarios, or about the audit path, since all six runs were given a transcript rather than an existing draft to review.

## The Change to Test Next, With Evidence Behind It

Four of six runs multiplied an untimed estimate by an approximate planning rate to produce a pound figure, and one annualised it to £131,000. That is a replicated defect rather than a hypothesis. Add a guardrail against combining two unmeasured inputs into a single headline figure, and re-run this scenario. The criterion is already obvious and should be written down before running: does a pound figure derived from both estimates appear at all.
