# Cedarwell Outbound Review

This review scores the [worked outbound output](../examples/cedarwell-outbound-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The job advert wording, contact role and CRM check all match the scenario exactly |
| Evidence fidelity | 5 | The advert's own phrasing is used as the hook rather than paraphrased into something vaguer or more generic |
| Fact separation | 5 | The depot expansion is correctly held as context, not evidence, and is deliberately left out of the message itself |
| Missing information | 4 | Correctly flags the unverified email address and unconfirmed product claims; could also note that Marcus Webb's actual authority over budget, not just process, is assumed from title and not independently confirmed |
| Commercial usefulness | 5 | Gives a genuinely usable, specific first-touch message rather than a generic template with brackets to fill in |
| Next step clarity | 5 | Ends with a single, low-friction ask, a reply, and states plainly what happens if one arrives |
| Tone | 5 | Short, specific, reads as a real message rather than a pitch |
| Privacy | 5 | Nothing beyond the public signal and named role is used |
| Approval discipline | 5 | Explicitly states that sending and any CRM entry require approval |
| Hallucination risk | 4 | No invented claim or statistic, and the value line stays in the reader's own terms rather than a vendor productivity claim, though the coordinator-time framing is a reasonable inference from the advert, not something the advert states outright |

## What Worked

- The hook is built entirely from the job advert's own wording, which is the exact discipline the skill's guardrail against a generic industry observation exists to enforce.
- The depot expansion, real and available, was correctly excluded from the message itself rather than used to sound more informed than the evidence actually supports.
- The offer is genuinely low-friction, a short first look, not a meeting ask, and the value is stated in coordinator time, not a generic productivity claim.
- Marcus Webb's role is treated as the plausible buyer without assuming interest or specific priorities beyond what his title and the advert support.

## What Needed Checking

- Marcus Webb's authority is inferred from his title (Operations Director) and the advert; his specific budget authority for this kind of purchase is not independently confirmed, and a careful reviewer should treat that as a reasonable but unconfirmed assumption rather than settled fact.
- The email address has not been verified; this is correctly flagged, but should be resolved through a safe method before sending, not guessed.
- The "disproportionate amount of a coordinator's week" framing is a reasonable inference from the advert's own wording, not a figure the advert states; worth a second look to confirm it does not read as more certain than it is.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The existing guardrails (never fabricate a signal, never lead with a meeting ask, never claim an unconfirmed capability) were sufficient without a new rule.

## Next Test

Run a weaker-signal target, a company that only has a generic industry-fit reason and no specific, verifiable public signal, to confirm the skill correctly says so and declines to write a confident-sounding message anyway, rather than reaching for a softer version of the same hook.
