# Kellow Fit and Limitations Review Review

This review scores the [worked fit and limitations review](../examples/kellow-fit-review-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every detail matches what the discovery call established |
| Evidence fidelity | 5 | Each verdict rests on the evidence for that team, not one generic argument for all |
| Fact separation | 5 | Keeps uncertain apart from poor fit, and the unconfirmed system integration stays unconfirmed throughout |
| Missing information | 4 | Rightly flags what needs confirming for two of the three teams, but gives no specific next question about Field Service Engineers beyond "a short conversation," which is vaguer than it could be |
| Commercial usefulness | 5 | Gives Priya's contact a recommendation they can use: build here, don't build there yet, and here's exactly why |
| Next step clarity | 4 | The next steps for the poor-fit and uncertain teams point the right way but name no owner or timing, unlike the clear pilot recommendation for the good-fit team |
| Tone | 5 | Plain and direct, with no made-up confidence and no false balance |
| Privacy | 5 | Entirely fictional, with no real company or person data |
| Approval discipline | 5 | Says nothing has gone to the prospect, and that this is input to a decision, not a finished document |
| Hallucination risk | 4 | The rejected "one rollout reaches the whole team" framing is there on purpose, as the spin the skill exists to catch, not a claim the output backs. But a careful reviewer should check it reads clearly as rejected reasoning, not an argument included by mistake |

## What Worked

- It calls Regional Account Managers a clean good fit, without inventing a caveat to look more balanced. That's what a confirmed match should get.
- It describes Central Order Support's shared queue as the real mismatch it is, rather than recasting it as a rollout advantage. That's the exact failure this skill exists to catch.
- It leaves Field Service Engineers as uncertain, rather than pushing to an early yes or no just to have an answer for every team raised on the call.

## What Needed Checking

- The next steps for Central Order Support and Field Service Engineers point the right way but could be sharper: a named person to ask, or a specific question for Priya's IT team, rather than a general instruction to go and confirm.
- A reviewer should check that the rejected "advantage" framing for Central Order Support clearly reads as an example of what not to do. Someone skimming could mistake it for a real claim if the sentence around it were shortened.

## What I Changed in the Prompt

Nothing, for this run. The main guardrail, against recasting a poor fit as a hidden strength, held on the first test built to catch it.

## Next Test

Run a scenario where the good-fit case itself has a real, if smaller, limit. That would confirm the skill can give a mixed verdict within one category, rather than always sorting each team cleanly into one of the three.
