# Fictional Pipeline Review Evaluation

This page scores the [worked pipeline review](../examples/fictional-pipeline-review.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Recorded fields and dated events match the snapshot exactly, and it spots both passed close dates |
| Evidence fidelity | 5 | Keeps Priya's "this cycle" pause and the six weeks of Meridian silence as stated, not rounded into something firmer |
| Fact separation | 5 | Labels the Harbourview departure an inference from LinkedIn, kept apart from the confirmed CRM fields |
| Missing information | 5 | Each deal names what to confirm, and the Harbourview "who owns this now" unknown stays open rather than filled |
| Commercial usefulness | 5 | Gives an honest, usable read on each deal and flags that overdue dates distort the pipeline total |
| Next step clarity | 4 | Most next steps are concrete. Meridian's is a little soft ("one clear either-or message") and isn't drafted |
| Tone | 5 | Describes drift without blaming the salesperson, as intended |
| Privacy | 5 | Uses only the supplied fields and notes, and brings in nothing from outside |
| Approval discipline | 5 | Read-only throughout, and leaves every suggested change for me to approve and make |
| Hallucination risk | 3 | The judgements on what the evidence supports are presented fairly, but "likely stalled" and "blocked" are readings a reasonable person could grade differently |

## What Worked

For every deal it puts the recorded position next to what the evidence supports, which is the whole point of the workflow, and it names the gap rather than implying it.

It calls Oakline healthy. A review that found a problem with the one sound deal wouldn't be trusted on the other four. Keeping it clean is what makes the rest believable.

It treats "Proposal Sent" for Meridian as a true record of something done, but not as evidence of a live deal. That's the exact trap the workflow is built to catch.

It handles the Harbourview departure as an inference to confirm, not a fact. It names plainly the recorded next step that can't happen ("Send contract" with no one to send it to).

It changes nothing in any system. The read-only rule holds on every deal.

## What Needed Checking

The judgements on what the evidence supports ("paused", "likely stalled", "blocked") are readings. They're defensible and kept apart from the recorded fields, but they're the part a person should sense-check. That's why I gave hallucination risk a 3 rather than a 5.

The Meridian next step could be sharper. Suggesting a message is right, but drafting the actual either-or line would be more useful.

The review sees only what was pasted in. A deal that looks stalled here may have context in my head that the notes didn't capture, and the output rightly defers to that.

## What I Changed in the Prompt

Nothing needed changing for this run. The read-only rule and the "call the healthy deals healthy" instruction both did real work here. One refinement is worth testing: asking the review to draft the next message for a stalled deal, not just say one is needed.

## Next Test

Run a larger, messier pipeline of fifteen to twenty deals, with at least one exact duplicate and one deal with no owner. See whether the review stays accurate at volume, and whether it leaves real CRM-hygiene issues (duplicates, ownership) to a separate hygiene pass rather than trying to fix everything at once.
