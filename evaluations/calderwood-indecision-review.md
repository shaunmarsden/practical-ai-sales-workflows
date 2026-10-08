# Calderwood Buyer Indecision Review

This page scores the [worked response](../examples/calderwood-indecision-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Gets Tom's authority, the pilot feedback and the three delays exactly as given |
| Evidence fidelity | 5 | Keeps the pattern of soft delays Tom created himself as the key signal, not flattened into one objection |
| Fact separation | 5 | The diagnosis clearly reasons from behaviour, and it flags the "shorter term / phased start" options as depending on whether they're really available |
| Missing information | 4 | Rightly notes the terms must be confirmed as available, though it could also flag that nobody fully tested whether "run it past the team" was a real gate |
| Commercial usefulness | 5 | Gives a different play from "follow up again", one that fits how indecision behaves |
| Next step clarity | 5 | Ends with a concrete, low-stakes offer and a direct question about what would make deciding safe |
| Tone | 5 | Warm and direct, takes pressure off rather than adding it |
| Privacy | 5 | Uses only what's on record, and brings in nothing from outside |
| Approval discipline | 5 | Drafts only, and leaves the conditional terms for me to confirm and offer |
| Hallucination risk | 3 | The "indecision, not objection" diagnosis is a defensible read, but still an inference. And the smaller-first-step offer only holds if that term really exists, which the reply depends on |

## What Worked

The response avoids the obvious move. It doesn't push harder, add urgency or reach for a discount, which is the trap with a fearful buyer, and it says plainly why those would backfire.

It builds the diagnosis from behaviour, a willing buyer who keeps creating soft delays, not from Tom's words alone. It rules out an objection, an approval gate, going quiet and disqualification.

The strongest lever is feedback from Tom's own team, which is on record, not a claim the vendor made up.

It handles the conditional terms honestly. The reply offers a smaller first step, but the notes say to send it only if that term really exists.

## What Needed Checking

The core diagnosis is an inference. The six-week pattern supports it well, but a person should confirm nothing unspoken sits behind the delays. That's why I gave hallucination risk a 3.

The "shorter initial term / phased start" is the move everything rests on, and it only works if I can offer it. If I can't, the reply needs reworking around a different safe first step.

The response treated "Run it past the team" as Tom seeking comfort, not a real approval gate. That's the likely read, but it's worth confirming it isn't a real dependency.

## What I Changed in the Prompt

Nothing needed changing for this run. The instruction to stop and say so if the situation isn't indecision does important work. The whole workflow fails if it forces the indecision playbook onto a real objection or approval gate. One refinement is worth testing: asking the model for two or three first steps that can be undone, so I can pick one that's available, rather than one suggested term.

## Next Test

Run a case that looks like indecision on the surface but is really a hidden approval gate or an unspoken objection. That confirms whether the workflow diagnoses it as *not* indecision and sends it elsewhere, rather than applying the risk-reduction playbook to a problem it can't solve.
