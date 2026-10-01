# Wrenford Objection Review

This review scores the [worked response](../examples/wrenford-objection-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests the workflow's own stop condition, not another diagnosis. In the [scenario](../examples/wrenford-objection-input.md), the question is a real contract question that nobody on the call has confirmed.

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The clause, the account split and the second-hand nature of the summary all match the scenario exactly |
| Evidence fidelity | 5 | Describes the clause as a second-hand summary throughout, and never upgrades it to confirmed fact |
| Fact separation | 5 | Separates what's known (a clause exists, tied to one client) from what isn't (its exact wording, and whether anyone has tested it internally) |
| Missing information | 4 | Rightly flags that the clause's wording is unconfirmed, but doesn't flag separately that nobody knows whether anyone at Wrenford has tested or interpreted it. The source notes list that as its own open question |
| Commercial usefulness | 5 | Keeps Aisha as a live, keen candidate with a real next step, rather than losing her or overpromising to keep her |
| Next step clarity | 4 | Asks for the clause's wording or a compliance confirmation, but doesn't say who at Wrenford to ask, since the source notes don't show anyone has been identified |
| Tone | 5 | Warm and honest about the limits of what's known, not defensive or evasive |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | Says plainly that nothing has been sent and no reading of the clause has been treated as settled |
| Hallucination risk | 4 | Mostly careful. But "what's been described sounds like it's tied specifically to one client's data" repeats the second-hand summary's framing quite confidently, even while hedging. It leans slightly towards the reassuring reading of an unconfirmed clause instead of staying neutral |

## What Worked

- It saw this as a stop condition, rather than forcing it into a diagnosis and answering with false confidence.
- It never settled the contract question either way. The draft says "I haven't seen the actual clause" and "I don't think it's fair to either of us for me to guess."
- It restated the open question precisely (does the clause cover general training, or only work touching that one client's data?) rather than steering towards a comforting answer.
- It kept Aisha engaged with a concrete next step she can answer, instead of dismissing the objection or letting it stall the conversation with no way forward.

## What Needed Checking

- The line calling the clause "tied specifically to one client's data" matches what Aisha was told. But repeating it quite confidently, even with a hedge, leans towards the reassuring reading this test exists to catch. Worth watching for in other runs.
- Whether anyone at Wrenford has ever tested or interpreted the clause is a separate unknown the source notes raise, and the response doesn't list it as its own open question.
- It names nobody at Wrenford to ask. That's right, since nobody was identified, but the next step would be stronger with a named role to send it to once one exists.

## What I Changed in the Prompt

Nothing, for this run. This run tested the stop-condition guardrail directly ("do not produce a confident response when the objection involves a legal, compliance or contractual question beyond what has already been confirmed"), and it held. The hedged restatement above is still worth watching.

## Next Test

Run a case where the contract question is the only thing raised, with no general-skills angle to turn towards. That would check the workflow still stops cleanly, rather than finding a narrower question to answer confidently when the source material has none.
