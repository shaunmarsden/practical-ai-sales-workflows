# Calderwood Buyer Indecision Review

This review scores the [worked response](../examples/calderwood-indecision-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Tom's authority, the pilot feedback and the three delays are represented exactly as given |
| Evidence fidelity | 5 | The pattern of soft, self-generated delays is preserved as the key signal, not flattened into a single objection |
| Fact separation | 5 | The diagnosis is clearly reasoning from behaviour, and the "shorter term / phased start" options are explicitly flagged as conditional on being genuinely available |
| Missing information | 4 | Correctly notes the terms must be confirmed available, though it could also flag that "run it past the team" was never fully tested as a real gate |
| Commercial usefulness | 5 | Gives a genuinely different play from "follow up again", one that fits how indecision actually behaves |
| Next step clarity | 5 | Ends with a concrete low-stakes offer and a direct question about what would make deciding safe |
| Tone | 5 | Warm and direct, takes pressure off rather than adding it |
| Privacy | 5 | Uses only what is on record; nothing external introduced |
| Approval discipline | 5 | Drafts only; the conditional terms are explicitly left for Shaun to confirm and offer |
| Hallucination risk | 3 | The "indecision, not objection" diagnosis is a defensible read, but it is still an inference; and the smaller-first-step offer only holds if that term genuinely exists, which the reply depends on |

## What Worked

- The response resists the obvious move. It does not push harder, add urgency, or reach for a discount, which is exactly the trap with a fearful buyer, and it says plainly why those would backfire.
- The diagnosis is built from behaviour (a willing buyer repeatedly self-generating soft delays) rather than from Tom's words alone, and it actively rules out objection, approval gate, quiet and disqualification.
- The strongest lever is Tom's own team's feedback, which is on record, not a manufactured vendor claim.
- The conditional terms are handled honestly: the reply offers a smaller first step but the notes make clear it must only be sent if that term genuinely exists.

## What Needed Checking

- The core diagnosis is an inference. It is well supported by the six-week pattern, but a human should confirm there is genuinely nothing unspoken behind the delays, which is why the hallucination-risk score is a deliberate 3.
- The "shorter initial term / phased start" is the load-bearing move, and it only works if Shaun can actually offer it. If he cannot, the reply needs reworking around a different safe first step.
- "Run it past the team" was treated as comfort-seeking rather than a real approval gate. That is the likely read, but worth confirming it is not a genuine dependency.

## What I Changed in the Prompt

Nothing needed changing for this run. The instruction to stop and say so if the situation is not actually indecision is doing important work, since the whole vertical fails if it forces the indecision playbook onto a real objection or approval gate. The refinement worth testing: asking the model to propose two or three genuinely-reversible first-step options so Shaun can pick one that is actually available, rather than a single suggested term.

## Next Test

Run a case that looks like indecision on the surface but is actually a hidden approval gate or an unspoken objection, to confirm the workflow correctly diagnoses it as *not* indecision and routes elsewhere, rather than applying the risk-reduction playbook to a problem it cannot solve.
