# Cedarwell Outbound Review

This page scores the [worked outbound output](../examples/cedarwell-outbound-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 48 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The job advert wording, contact role and CRM check all match the scenario exactly |
| Evidence fidelity | 5 | Uses the advert's own phrasing as the hook rather than paraphrasing it into something vaguer |
| Fact separation | 5 | Holds the depot expansion as context, not evidence, and leaves it out of the message on purpose |
| Missing information | 4 | Flags the unverified email address and unconfirmed product claims. Could also note that Marcus Webb's authority over budget, not just process, is assumed from his title and not confirmed |
| Commercial usefulness | 5 | Gives a usable, specific first message rather than a template with brackets to fill in |
| Next step clarity | 5 | Ends with one easy ask, a reply, and says plainly what happens if one arrives |
| Tone | 5 | Short, specific, reads as a real message rather than a pitch |
| Privacy | 5 | Uses nothing beyond the public signal and named role |
| Approval discipline | 5 | Says that sending and any CRM entry need approval |
| Hallucination risk | 4 | No invented claim or statistic, and the value line stays in the reader's own terms rather than a vendor productivity claim. But the point about coordinator time is a fair inference from the advert, not something the advert says outright |

## What Worked

The hook comes entirely from the job advert's own wording. That's what the skill's guardrail against a general industry observation exists to enforce.

The depot expansion was real and available, but it stayed out of the message rather than being used to sound better informed than the evidence supports.

The offer is easy to accept, a short first look rather than a meeting. It puts the value in coordinator time, not a general productivity claim.

It treats Marcus Webb as the likely buyer without assuming interest or priorities beyond what his title and the advert support.

## What Needed Checking

Marcus Webb's authority is inferred from his title (Operations Director) and the advert. Nobody has confirmed he holds the budget for this kind of purchase. A careful reviewer should treat that as a fair but unconfirmed assumption, not settled fact.

The email address isn't verified. The output flags this, but it should be resolved by a safe method before sending, not guessed.

The "disproportionate amount of a coordinator's week" line is a fair inference from the advert's wording, not a figure the advert states. It's worth a second look to make sure it doesn't read as more certain than it is.

## What I Changed in the Prompt

Nothing in the skill needed changing for this run. The existing guardrails (never make up a signal, never open by asking for a meeting, never claim a capability nobody has confirmed) were enough without a new rule.

I later added a subject-line rule to the skill after reviewing real cold-email technique: short, lowercase, never naming the offer or how it works. I changed the subject line in the worked output above from "Manual reporting across three depot systems" to "quick question", so it shows the rule rather than leaving it untested on this scenario. Nothing else in the message changed. None of the scores above depended on the subject line, so the score stands.

## Next Test

Run a target with a weaker signal: a company with only a general industry-fit reason and no specific public signal anyone can check. That confirms whether the skill says so and declines to write a confident message anyway, rather than reaching for a softer version of the same hook.
