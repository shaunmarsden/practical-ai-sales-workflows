# Fictional Objection Pattern Review Evaluation

This review scores the [worked pattern analysis](../examples/fictional-objection-pattern-review.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every quote, stage, role and outcome matches the log exactly, including the two objections reused from existing Hartwell and Bramfield material |
| Evidence fidelity | 5 | Keeps each Copilot mention's actual underlying driver distinct rather than treating "Copilot" as one label |
| Fact separation | 5 | Explicitly separates the observed fact (three mentions) from the assumed root cause (one competitive problem), which is the entire point of the workflow |
| Missing information | 4 | Correctly flags the sample is too small to rule out a real Copilot pattern at volume; could also note that all three Copilot-adjacent entries came from only two sectors, which limits how far the "no single pattern" conclusion can be generalised |
| Commercial usefulness | 5 | The compliance one-pager recommendation is concrete and actionable; the refusal to build a "beat Copilot" playbook item is equally useful as a negative finding |
| Next step clarity | 4 | The compliance action is specific; the Copilot finding's next step is more of a caution than an action, which is appropriate here but softer than the other recommendation |
| Tone | 5 | Matter-of-fact throughout, does not oversell either finding |
| Privacy | 5 | All fictional; no real company, person or figure |
| Approval discipline | 5 | Nothing is presented as already built or sent; the one-pager and its ownership are both left for a person to decide |
| Hallucination risk | 4 | The compliance pattern's high confidence is well earned from two essentially identical needs; the "no single Copilot pattern" conclusion is a defensible read of six data points, but six is a small sample, and the review says so rather than overstating certainty |

## What Worked

- The core discipline of the workflow, keeping an observed count separate from an assumed cause, is demonstrated correctly on the one finding built specifically to test it, and the review does not fall into the trap of averaging outcomes across dissimilar situations.
- Reusing two objections already on record (Hartwell's Copilot and price objections) rather than inventing new ones for this test keeps the fictional universe consistent and shows the same data being read a second, different way for a new purpose.
- The compliance pattern is correctly identified as high confidence precisely because the underlying need is the same each time, not because the wording is similar, which is the right basis for that judgement.
- The review declines to produce a loss rate or win rate from a six-entry sample, which is the correct call given how easily a small number can be misread as a statistic.

## What Needed Checking

- The three Copilot-adjacent entries all come from only two industries (professional services, underwriting) plus the original SaaS-adjacent Hartwell case; a genuinely broader review should note that limits how confidently "no single pattern" can be said to generalise across sectors not represented here.
- The Copilot finding's recommendation, "have a ready, honest answer available," is directionally right but softer than the compliance recommendation; a sharper version might specify what that answer should actually contain.
- This log is deliberately small (six entries) to make the test traceable by hand. A real pattern review would need a genuinely larger sample before either finding should be treated as settled.

## What I Changed in the Prompt

Nothing needed changing in the prompt for this run. The instruction to keep observed patterns and assumed causes separate was sufficient on its own to produce the correct read of both the real and the misleading pattern, without needing an additional rule specific to competitor mentions.

## Next Test

Run this workflow against a larger, messier log, twenty to thirty entries across more sectors and objection types, including at least one pattern that looks weak at six entries but becomes genuinely strong at volume, to check whether the workflow correctly revises its confidence upward when the evidence actually improves, not just downward when it is thin.
