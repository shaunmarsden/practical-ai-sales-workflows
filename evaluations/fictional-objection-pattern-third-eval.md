# Fictional Objection Pattern Third Evaluation

This review scores the [third worked analysis](../examples/fictional-objection-pattern-review-three.md) against the [sales AI output rubric](sales-ai-output-rubric.md). The [first](fictional-objection-pattern-review-eval.md) and [second](fictional-objection-pattern-second-eval.md) evaluations are still available.

I built this test around two decoy entries. On the surface they look like the real pattern, one because someone else's input is needed and the other because the stage and outcome match, but the cause is different in both.

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Counts eight occurrences across seven separate deals correctly, including the Bellhaven duplicate |
| Evidence fidelity | 5 | Groups the five differently worded entries about the attestation surprise by their shared cause, and keeps both decoys out even though they look alike |
| Fact separation | 5 | Keeps the applicants' own stated reasons, Corvane's household budget and Priya's new job, as stated facts rather than inferred causes |
| Missing information | 4 | Rightly flags that the sample is only self-funded applicants, but doesn't ask whether the five affected deals share a lead source or piece of marketing that might explain the cluster before discovery even starts |
| Commercial usefulness | 5 | The suggested action, explaining the attestation requirement earlier, aims at when the gap in expectations opens, not at a generic messaging fix |
| Next step clarity | 4 | The suggested actions are concrete, but none names who owns checking back with the five applicants, or by when |
| Tone | 5 | Measured and specific, and doesn't overstate what five deals support |
| Privacy | 5 | Uses only fictional applicants and companies |
| Approval discipline | 5 | Leaves every suggested action for a person to approve, and presents nothing as already changed |
| Hallucination risk | 4 | The medium-high confidence is fair. But grouping Marrow Fields, who withdrew before ever applying, with four stalls mid-conversation is a slightly bigger leap than the other four. A person should confirm it belongs in the same group |

## What Worked

- It left out Corvane Digital. It saw that "checking with someone else" looks like the real pattern on the surface, but involves a different person (a partner, not an employer) and a different reason (household budget).
- It left out Priya Anand by taking her stated reason at face value, rather than inferring the attestation cause just because the stage and outcome matched.
- It didn't let the Bellhaven duplicate inflate the count of separate deals, as in the second test.
- It recommended a specific action aimed at timing, explaining the requirement earlier, rather than a generic "improve messaging" suggestion.

## What Needed Checking

- Marrow Fields withdrew before any live conversation about the requirement. That's a different kind of evidence from a stall in the middle of one. A person should confirm it belongs with the same cause, rather than being a related signal worth tracking separately.
- The review doesn't ask whether the five affected applicants came through the same channel or piece of marketing. That could point to fixing the messaging further back, instead of or as well as fixing the discovery conversation.
- There's no owner or timeframe for following up with the five applicants who may still be reachable.

## What I Changed in the Prompt

Nothing, for this run. The instruction to check the cause, not just the words, and the rule to group entries only with real evidence of a shared cause, were enough to separate both decoys from the real pattern. It didn't need a new rule aimed at "someone else's input" as a surface shape.

## Next Test

Run a case where a decoy entry doesn't state its own different reason, unlike Corvane and Priya here. The skill would then have to infer a different cause from thinner evidence. Check whether it still resists merging them, or reports the cause as unclear rather than guessing either way.
