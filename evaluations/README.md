# How Evaluations Work Here

Every worked example in this repo is scored, not just shown. This folder explains the standard so a new evaluation is comparable to an old one instead of judged by whoever wrote it that day.

## The Rubric

All scoring uses the same [Sales AI Output Rubric](sales-ai-output-rubric.md): ten areas, 1 to 5 each, with automatic-failure conditions that override the total. If you are adding a new worked example, score it against this rubric and nothing else. Do not invent a one-off scoring scheme for a single skill.

## Two Kinds of Evaluation

**Single run** — one model, one scenario, scored once. This is what most of the reviews in this folder are today (for example [northstar-lost-opportunity-review.md](northstar-lost-opportunity-review.md)). Good enough to check a workflow produces sane output on a realistic case.

**Repeated or cross-model run** — the same scenario run more than once, either across models (see [cross-model-post-call-comparison.md](cross-model-post-call-comparison.md)) or multiple times against the same model, to see whether the result is stable or whether it was a lucky single pass. Use the [test-run-template.md](test-run-template.md) for this, and record each run's setup with [model-run-metadata-template.md](model-run-metadata-template.md).

A single scored run tells you a workflow can produce a good result. It does not tell you a workflow reliably produces a good result. Treat single-run scores as "this worked once, under these conditions," not as a guarantee.

## Adding a New Evaluation

1. Run the workflow against a realistic fictional scenario (Northstar Analytics / Alex Morgan / Priya Chen, or Cedarwell Group for outbound).
2. Score it against the rubric, area by area, with a one-line reason for each score, not just a number.
3. Record what worked, what needed checking, and what you would change next time. Be honest about weak scores rather than rounding up.
4. If this is a repeated or cross-model run, use the templates in this folder so the metadata is comparable across runs.
