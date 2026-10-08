# Fictional Objection Pattern Review Evaluation

This review scores the [worked pattern analysis](../examples/fictional-objection-pattern-review.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every quote, stage, role and outcome matches the log exactly, including the two objections reused from the Hartwell and Bramfield material |
| Evidence fidelity | 5 | Keeps the real driver behind each Copilot mention separate, rather than treating "Copilot" as one label |
| Fact separation | 5 | Separates the observed fact (three mentions) from the assumed root cause (one competitive problem), which is the whole point of the workflow |
| Missing information | 4 | Rightly flags that the sample is too small to rule out a real Copilot pattern at volume. It could also note that all three entries near Copilot came from only two sectors, which limits how far the "no single pattern" conclusion reaches |
| Commercial usefulness | 5 | The compliance one-pager recommendation is concrete and usable. Refusing to build a "beat Copilot" playbook item is just as useful, as a negative finding |
| Next step clarity | 4 | The compliance action is specific. The Copilot finding's next step is more a caution than an action, which suits the case but is softer than the other recommendation |
| Tone | 5 | Matter-of-fact throughout, and doesn't oversell either finding |
| Privacy | 5 | All fictional, with no real company, person or figure |
| Approval discipline | 5 | Nothing is presented as already built or sent. The one-pager and who owns it are both left for a person to decide |
| Hallucination risk | 4 | The compliance pattern earns its high confidence from two almost identical needs. The "no single Copilot pattern" conclusion is a fair reading of six data points, but six is a small sample, and the review says so rather than overstating how sure it is |

## What Worked

- The workflow's core rule, keeping an observed count apart from an assumed cause, works correctly on the one finding built to test it. The review doesn't fall into averaging outcomes across unlike situations.
- Reusing three objections already on record (Hartwell's Copilot and price objections, and Bramfield's compliance question), rather than inventing new ones, keeps the fictional world consistent. It also shows the same data read a second way for a new purpose.
- It rates the compliance pattern high confidence because the need underneath is the same each time, not because the wording is similar. That's the right basis for the judgement.
- It won't give a loss rate or win rate from six entries, which is right given how easily a small number gets misread as a statistic.

## What Needed Checking

- The three entries near Copilot come from only two industries (professional services, underwriting), plus the original Hartwell case, which is close to SaaS. A broader review should note that this limits how confidently "no single pattern" can be said to hold in sectors not represented here.
- The Copilot finding's recommendation, "have a ready, honest answer available," points the right way but is softer than the compliance recommendation. A sharper version might say what that answer should contain.
- The output never mentions entry 2, Hartwell's price-looking objection, though it counts six data points.
- This log is small on purpose (six entries) so the test can be traced by hand. A real pattern review would need a much larger sample before either finding counts as settled.

## What I Changed in the Prompt

Nothing in the prompt needed changing for this run. The instruction to keep observed patterns and assumed causes apart was enough on its own to read both the real and the misleading pattern correctly, with no extra rule for competitor mentions.

## Next Test

Run this workflow on a larger, messier log: 20 to 30 entries across more sectors and objection types. Include at least one pattern that looks weak at six entries but becomes strong at volume. That checks whether the workflow raises its confidence when the evidence improves, not just lowers it when the evidence is thin.
