# Fictional Pipeline Review Evaluation

This review scores the [worked pipeline review](../examples/fictional-pipeline-review.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Recorded fields and dated events match the snapshot exactly; the two passed close dates are identified correctly |
| Evidence fidelity | 5 | Priya's "this cycle" pause and the six weeks of Meridian silence are preserved as stated, not rounded into something firmer |
| Fact separation | 5 | The Harbourview departure is labelled an inference from LinkedIn, kept distinct from the confirmed CRM fields |
| Missing information | 5 | Each deal names what to confirm; the Harbourview "who owns this now" unknown is held open rather than filled |
| Commercial usefulness | 5 | Gives an honest, actionable read per deal and flags that overdue dates distort the pipeline total |
| Next step clarity | 4 | Most next steps are concrete; Meridian's is a little soft ("one clear either-or message") without drafting it |
| Tone | 5 | Describes drift without blaming the salesperson, exactly as intended |
| Privacy | 5 | Uses only the supplied fields and notes; nothing external is introduced |
| Approval discipline | 5 | Read-only throughout; every suggested change is explicitly left for Shaun to approve and make |
| Hallucination risk | 3 | The evidence-supported states are judgement calls presented fairly, but "likely stalled" and "blocked" are interpretations a reasonable person could grade differently |

## What Worked

- The recorded position and the evidence-supported position are held side by side for every deal, which is the whole point of the workflow, and the gap is named rather than implied.
- Oakline is called out as genuinely healthy. A review that flagged a problem on the one sound deal would not be trusted on the other four; keeping it clean is what makes the rest credible.
- "Proposal Sent" for Meridian is correctly treated as a true record of an action but not as evidence of a live deal, which is the exact trap the workflow is built to catch.
- The Harbourview departure is handled as an inference to confirm, not a fact, and the impossible recorded next step ("Send contract" with no one to send it to) is named plainly.
- Nothing is changed in any system; the read-only discipline holds on every deal.

## What Needed Checking

- The evidence-supported states ("paused", "likely stalled", "blocked") are interpretations. They are defensible and clearly separated from the recorded fields, but they are the part a human should sanity-check, which is why the hallucination-risk score is a deliberate 3 rather than a 5.
- The Meridian next step could be sharper. Suggesting a message is right; drafting the actual either-or line would be more useful.
- The review sees only what was pasted in. A deal that looks stalled here may have context in Shaun's head that the notes did not capture, which the output correctly defers to.

## What I Changed in the Prompt

Nothing needed changing for this run. The read-only rule and the "call the healthy deals healthy" instruction both did real work here. The one refinement worth testing: asking the review to draft the actual next-touch message for a stalled deal, rather than only naming that one is needed.

## Next Test

Run a larger, messier pipeline of fifteen to twenty deals, including at least one exact duplicate and one deal with a missing owner, to see whether the review stays accurate at volume and whether it correctly leaves genuine CRM-hygiene issues (duplicates, ownership) to a separate hygiene pass rather than trying to solve everything at once.
