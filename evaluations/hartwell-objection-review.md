# Hartwell Objection Review

This review scores the [worked response](../examples/hartwell-objection-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The pilot figures and Priya's role and authority match the scenario exactly, and nothing is added |
| Evidence fidelity | 5 | It treats "Putting in front of the room" as the key signal rather than flattening it into a generic price objection |
| Fact separation | 5 | It clearly labels the diagnosis as reasoning from context, and keeps the secondary information point apart from the main driver |
| Missing information | 4 | It rightly flags that the QBR date is unknown and mustn't be invented, though it could also note that finance's specific grounds for objecting are unknown |
| Commercial usefulness | 5 | It gives Priya what she needs, ammunition to defend the number, rather than a discount or the pitch again |
| Next step clarity | 5 | Ends with a concrete either/or ask and a dated follow-up tied to the QBR |
| Tone | 5 | Measured and collaborative, neither defensive about the price nor pushy |
| Privacy | 5 | It brings in nothing beyond what's relevant to the objection |
| Approval discipline | 5 | The reply is drafted, not sent, and the discount question and follow-up date are left to me |
| Hallucination risk | 3 | The diagnosis that the real driver is "other people" rather than price is a fair reading of the context, but it's still an inference. A reasonable person could read this as a real price objection, and the response commits fairly hard to its reading |

## What Worked

- The wording was a price objection, and the response didn't take the bait, discount or defend the total. It read the objection again through Priya's role and the QBR context.
- The isolate step does real work. It asks Priya to confirm the driver rather than assume it, which protects against a wrong diagnosis.
- It used the pilot's own measured result as evidence the prospect produced, not a vendor's claim about value.
- It offered no discount, because none was asked for or authorised, and it says so for human review.

## What Needed Checking

- The core diagnosis is an inference, not a certainty. Its strength is that the isolate question ("is it the total, or defending it to the room?") lets Priya correct it easily if it's wrong. That design is what keeps the hallucination-risk score from being lower.
- The response assumes the pilot numbers turn cleanly into a payback per head. Nobody knows yet whether finance accepts that framing, and it's worth confirming.
- The follow-up must be dated against the real QBR date, which the draft rightly won't invent.

## What I Changed in the Prompt

Nothing needed changing for this run. The isolate step already guards against the main risk, committing to the wrong driver. The thing to test next is the opposite case: an objection where the price wording really is the whole story. That would confirm the workflow doesn't invent a hidden "other people" driver where there isn't one.

## Next Test

Run an ambiguous objection, one with real mixed signals where you can't clearly work out the driver from context, several times on the same model using the [test run template](test-run-template.md). Check whether the diagnosis stays the same across runs or swings between buckets. A single clean pass like this one shows the workflow can diagnose well. It doesn't yet show it diagnoses consistently when the signals are mixed. I've since run that test: see the [ambiguous objection stability test](hartwell-objection-ambiguous-test.md).
