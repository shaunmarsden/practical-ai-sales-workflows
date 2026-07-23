# Kellow Fit and Limitations Review Review

This review scores the [worked fit and limitations review](../examples/kellow-fit-review-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every detail traces to what was actually established in the discovery call |
| Evidence fidelity | 5 | Each classification is grounded in the specific evidence for that team, not a shared generic argument |
| Fact separation | 5 | Uncertain is kept genuinely distinct from poor fit; the unconfirmed system integration stays unconfirmed throughout |
| Missing information | 4 | Correctly flags what needs confirming for two of the three teams, but does not name a specific next question to ask about Field Service Engineers beyond "a short conversation," which is a little vaguer than it could be |
| Commercial usefulness | 5 | Gives Priya's contact a genuinely usable recommendation: build here, do not build there yet, and here is exactly why |
| Next step clarity | 4 | The next steps for the poor-fit and uncertain teams are directionally right but do not name an owner or a timing, unlike the good-fit team's clear pilot recommendation |
| Tone | 5 | Plain and direct, no invented confidence and no false balance |
| Privacy | 5 | Entirely fictional, no real company or person data |
| Approval discipline | 5 | Explicitly states nothing has been presented to the prospect and this is input to a decision, not a finished document |
| Hallucination risk | 4 | The rejected "one rollout reaches the whole team" framing is deliberately included as the spin trap the skill exists to catch, not an actual claim the output endorses, but a careful reviewer should confirm it reads clearly as rejected reasoning rather than an accidentally-included argument |

## What Worked

- Regional Account Managers is called a clean good fit without inventing an unnecessary caveat to appear more balanced, exactly what a confirmed match should get.
- Central Order Support's shared-queue structure is described as the real mismatch it is, rather than being reframed as a rollout advantage, which is the specific failure mode this skill exists to catch.
- Field Service Engineers is left genuinely uncertain rather than being pushed toward a premature yes or no under pressure to have an answer for every team raised on the call.

## What Needed Checking

- The next steps for Central Order Support and Field Service Engineers are correct in direction but could be sharper: a named person to ask, or a specific question to put to Priya's IT team, rather than a general instruction to go and confirm.
- A reviewer should double check that the rejected "advantage" framing for Central Order Support reads unambiguously as an example of what not to do, since a skim read could mistake it for an actual claim if the surrounding sentence were shortened.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The core guardrail against reframing a poor fit as a hidden strength held up on the first test built specifically to catch it.

## Next Test

Run a scenario where the good fit case itself has a genuine, if smaller, limitation, to confirm the skill can hold a mixed verdict within a single classification rather than defaulting every team to one of the three categories cleanly.
