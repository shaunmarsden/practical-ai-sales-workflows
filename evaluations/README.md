# How Evaluations Work Here

I score the worked examples in this repo, not just show them. This folder sets out the standard, so a new evaluation compares with an old one instead of depending on whoever wrote it that day.

## The Rubric

All scoring uses the same [Sales AI Output Rubric](sales-ai-output-rubric.md): ten areas, 1 to 5 each, with automatic-failure conditions that override the total. If you're adding a new worked example, score it against this rubric and nothing else. Don't invent a one-off scoring scheme for a single skill.

## Two Kinds of Evaluation

**Single run**: one model, one scenario, scored once. Most of the reviews in this folder are this kind today (for example [hartwell-lost-opportunity-review.md](hartwell-lost-opportunity-review.md)). It's enough to check a workflow gives sensible output on a realistic case.

**Repeated or cross-model run**: the same scenario run more than once, either on different models (see [cross-model-post-call-comparison.md](cross-model-post-call-comparison.md)) or several times on the same model, to see whether the result holds or was a lucky one-off. Use the [test-run-template.md](test-run-template.md) for this, and record each run's setup with [model-run-metadata-template.md](model-run-metadata-template.md).

A single scored run tells you a workflow can produce a good result. It doesn't tell you it does so reliably. Treat single-run scores as "this worked once, under these conditions," not as a guarantee.

An example that combines workflows is still a single run, but the review must also check whether the agent chose the right workflow, used only the sources it needed, kept conflicts visible and held every outside action for approval. See the [fictional sales-copilot review](fictional-sales-copilot-review.md) for that shape.

## Changing a Skill's Instructions

When a test finds a real failure and the fix changes a skill's instructions, use the [instruction change and regression history template](../templates/instruction-change-history-template.md) rather than just editing the skill and moving on. It records the original wording, the failure, the exact change and the rerun result. It also has a standing regression checklist, so fixing one failure doesn't quietly reopen a guardrail that already worked.

## Adding a New Evaluation

1. Run the workflow against a realistic fictional scenario (Hartwell Analytics / Alex Morgan / Priya Chen, or Cedarwell Group for outbound).
2. Score it against the rubric, area by area, with a one-line reason for each score, not just a number.
3. Record what worked, what needed checking, and what you'd change next time. Give weak scores as they are, rather than rounding up.
4. If this is a repeated or cross-model run, use the templates in this folder so the metadata is comparable across runs.
