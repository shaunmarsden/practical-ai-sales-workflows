# Test Run Template (Repeated or Cross-Model)

Use this when scoring the same scenario more than once, either across models or multiple times against one model, instead of the single-run review format.

## Scenario

What fictional situation was tested, and a link to the input (transcript, scenario doc, etc).

## Runs

One [model-run-metadata-template.md](model-run-metadata-template.md) block per run, listed here.

## Scores

| Area | Run 1 | Run 2 | Run 3 |
| --- | ---: | ---: | ---: |
| Factual accuracy | | | |
| Evidence fidelity | | | |
| Fact separation | | | |
| Missing information | | | |
| Commercial usefulness | | | |
| Next step clarity | | | |
| Tone | | | |
| Privacy | | | |
| Approval discipline | | | |
| Hallucination risk | | | |
| **Total** | | | |

## Where Runs Agreed

What stayed consistent across every run, regardless of model or attempt. This is the part of the workflow you can trust.

## Where Runs Disagreed

What changed between runs, and whether that disagreement matters commercially (a different phrasing is fine, a different classification of the same evidence is not). Quote the actual differing text rather than summarising it away.

## Conclusion

Whether the workflow is stable enough to rely on, or whether it needs a tighter prompt, a stricter output schema, or a human check on this particular judgement call before it can be trusted unattended.
