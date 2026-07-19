# Northstar Objection Review

This review scores the [worked response](../examples/northstar-objection-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The pilot figures and Priya's role and authority match the scenario exactly; nothing is added |
| Evidence fidelity | 5 | "Putting in front of the room" is treated as the key signal rather than being flattened into a generic price objection |
| Fact separation | 5 | The diagnosis is clearly labelled as reasoning from context, and the secondary information element is kept separate from the primary driver |
| Missing information | 4 | Correctly flags that the QBR date is unknown and not to be invented, though it could also note that finance's specific objection criteria are unknown |
| Commercial usefulness | 5 | Gives Priya what she actually needs, ammunition to defend the number, rather than a discount or a restated pitch |
| Next step clarity | 5 | Ends with a concrete either/or ask and a dated follow-up tied to the QBR |
| Tone | 5 | Measured and collaborative, neither defensive about the price nor pushy |
| Privacy | 5 | Nothing beyond what is relevant to the objection is introduced |
| Approval discipline | 5 | The reply is drafted, not sent; the discount question and the follow-up date are explicitly left to Shaun |
| Hallucination risk | 3 | The diagnosis that the real driver is "other people" rather than price is a defensible read of the context, but it is still an inference; a reasonable person could read this as a genuine price objection, and the response commits fairly hard to its reading |

## What Worked

- The surface wording was a price objection and the response did not take the bait, discount, or defend the total; it re-read the objection through Priya's role and the QBR context.
- The isolate step is doing real work: it asks Priya to confirm the driver rather than assuming it, which protects against the diagnosis being wrong.
- The pilot's own measured result was used as defensible, prospect-generated evidence, not a vendor value claim.
- No discount was offered, because none was asked for or authorised, and this is called out explicitly for human review.

## What Needed Checking

- The core diagnosis is an inference, not a certainty. Its strength is that the isolate question ("is it the total, or defending it to the room?") lets Priya correct it cheaply if it is wrong. That design is what keeps the hallucination-risk score from being lower.
- The response assumes the pilot numbers translate cleanly into a per-head payback. Whether finance accepts that framing is unknown and worth confirming.
- The follow-up must be dated against the real QBR date, which the draft correctly declines to invent.

## What I Changed in the Prompt

Nothing needed changing for this run. The isolate step already guards against the main risk, which is committing to the wrong driver. The thing worth testing next is the opposite case, an objection where the surface price wording really is the whole story, to confirm the workflow does not manufacture a hidden "other people" driver where none exists.

## Next Test

Run a genuinely ambiguous objection, one with real mixed signals where the driver is not clearly resolvable from context, several times against the same model using the [test run template](test-run-template.md), and check whether the diagnosis stays stable across runs or swings between buckets. A single clean pass like this one shows the workflow can diagnose well; it does not yet show it diagnoses consistently under ambiguity.
