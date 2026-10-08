# Business Case Check Requirement: A Six-Run Test

This test didn't support the change I wrote it for, and it corrects something I published earlier.

## What Was Being Tested

The [business case prompt review](aldercroft-business-case-prompt-review.md) said the prompt probably beat the skill by three points on the Aldercroft scenario because of my design choice, not the model's judgement. The prompt makes a human-check section a required part. The skill didn't list one, and its one published run didn't flag that nobody had set a pilot cost.

So I added one line to the skill's list of required document parts:

> **Human check section**: present, and it must list every figure, claim and section a person has to confirm before the document is sent, plus anything left as an `unknown`. A figure the sources never established counts as something to confirm even when no section of the document is currently claiming it, so an absent price, rate or date belongs on this list rather than being left silent.

## Method

Six runs on the same [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with its answer key removed: same model, a fresh context each time, no rubric, no access to this repository.

- Three runs with the skill exactly as published before the change
- Three runs with the skill plus that one line, and nothing else changed

I ran three of each because identical prompts on identical input have already [moved by one to three points](repeat-run-findings.md), and one against one can't separate the instruction from that.

**The pass mark, written down before any run:** does the output say anywhere that no pilot cost, price or commercial figure was set, or otherwise name the missing pilot cost as something a person must confirm? Leaving out a commercial section without comment counts as a no. **What would prove me wrong:** if the unchanged skill flags it in two or three of its runs, the original miss was a one-off and the new line isn't what changed it.

## Result

| Run | Skill | Named the absent pilot cost |
| --- | --- | --- |
| 1 | As published | Yes |
| 2 | As published | Yes |
| 3 | As published | **No** |
| 1 | With the line | Yes |
| 2 | With the line | Yes |
| 3 | With the line | Yes |

**Two of three unchanged runs already flagged it. That's what I'd said would prove me wrong, so I rejected the idea.** The published miss was normal variation. A missing instruction didn't cause it.

## The Claim This Corrects

The prompt review said the required check section was "the most likely reason the pilot-cost gap got caught here and not there". That was wrong, in the direction that flattered my new prompt. It also implied the skill's section was sometimes missing. **All three unchanged runs produced a human-check section without being told to.**

## What the Six Runs Did Show

**A worse failure than the one I was chasing.** Unchanged run 3 missed the pilot cost. It also produced a yearly figure of £131,000 from two unmeasured inputs: Tomasz's untimed six-hour estimate multiplied by Finance's rough planning rate. It came from the published skill.

**The stacked figure isn't variation. It's the norm.** Four of the six runs multiplied the two unmeasured inputs into a pound figure, two of three before the change and two of three after. The published Aldercroft review lost a hallucination-risk mark for exactly this, on a £65,520 figure.

**All six runs used em dashes**, thirteen to twenty-three each. The skill didn't tell the model to avoid them, and at the time only four of the seventeen skills did. A CI check bans them from every tracked file, and the published Aldercroft output from this skill has none. Nothing in `examples/` says a punctuation change was made. I can't prove anyone edited a published output, and I'm not saying they did. The model produces the character reliably and CI can't let it through.

The [output published alongside this test](../examples/aldercroft-business-case-check-requirement-output.md) says which replacements were my judgement. All seventeen skills now carry the rule, [tested over thirty-three runs](em-dash-rule-test.md), and a check stops a new skill shipping without it.

## What Happened to the Change

**I kept the line, and I label it as weakly evidenced, not as a fix.** Against it: I rejected the idea that led to it, and three runs each can't tell three from three apart from two from three. For it: unchanged run 3 is a real case of the failure the line describes, and the changed runs didn't repeat it. Reverting it is one line.

## One Modified Run, Scored in Full

I scored the run I'd named in advance, not the best: [the first modified run](../examples/aldercroft-business-case-check-requirement-output.md).

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Headcount, rate, six-hour estimate, audit-trail requirement and the pilot-not-rollout ask all match the transcript |
| Evidence fidelity | 5 | Every condition survives, including the excluded future headcount and the out-of-scope accounts payable aside |
| Fact separation | 5 | The derived figures say they rest on two unchecked inputs where they appear, not only where the inputs came in |
| Missing information | 5 | Names pilot investment, start date, length of the measurement period and wider resourcing as unknown |
| Commercial usefulness | 5 | The ask is the right size, and it gives the pilot four measurable success markers to judge it by later |
| Next step clarity | 4 | Says clearly that sending isn't approval, but names nobody to own agreeing the measurement period |
| Tone | 5 | Third person for a CFO who wasn't on the call, hedged in line with the material |
| Privacy | 5 | No personal data, and the out-of-scope aside stays out of the case |
| Approval discipline | 5 | Checkboxes rather than assertions, and it says sending the document isn't approval |
| Hallucination risk | 4 | Labels the stacked £2,520 and £1,260 figures heavily and offers to cut them, but still produces them, the same fault the published run lost this mark for |

## What This Test Cannot Prove

- Three runs per version can reject a strong claim, which it did, but can't show a small effect.
- One scenario, one model, and I scored every run and wrote the change.
- It says nothing about the other two business case scenarios, or about reviewing an existing draft, since all six runs got a transcript.

## The Change to Test Next

The next change was a guardrail against combining two unmeasured inputs into one headline figure, with the pass mark written down first: does a pound figure built from both estimates appear at all? **I did that.** [Nineteen runs](business-case-stacked-figure-test.md), with the pass mark decided in advance. None of the ten with the guardrail produced a combined figure, against four of the nine without. A six-run follow-up confirmed it doesn't block sound arithmetic. It was the first change to this skill that a test supported.

## Corrections

An earlier version of this page said that both the skill and the prompt ask for three applied examples, and that across six runs the counts (one, zero, zero, one, zero, one) showed the model ignoring an instruction. Only the prompt asks for three. The skill says "three is a good number", and all six of these runs used the skill. Six later fresh runs of the published skill each produced at least one grounded example. See the [applied examples test](business-case-applied-examples-test.md).
