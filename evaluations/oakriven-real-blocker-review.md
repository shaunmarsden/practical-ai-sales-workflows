# Oakriven Real Blocker Diagnosis Review

This review scores the [worked diagnosis](../examples/oakriven-real-blocker-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). The pattern is harder than in the [Rowcastle test](rowcastle-real-blocker-review.md). There's no unplanned attendee. Instead, the keen contact himself suggests a plan that would push an enrolment so far along that the real decision-maker would face something already done, not a real choice made up front.

## Result

| | Score |
| --- | ---: |
| Score | 47 / 50 |
| Automatic failure | No |

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every detail, the hallway conversation, the cohort date, the proposed process, matches the scenario notes exactly |
| Evidence fidelity | 5 | Keeps a vague reaction given before any specifics apart from a confirmed sign-off, rather than treating Dev's account as settled |
| Fact separation | 5 | States exactly what Dev said, then separates it from what would settle the authority question, without guessing Rina's answer either way |
| Missing information | 4 | Rightly treats Rina's authority as unconfirmed, but doesn't consider that Rina may not be the final approver either. Nothing in the scenario rules out a further approval step above her |
| Commercial usefulness | 5 | Gives a clear recommendation you can act on, ask Rina directly and promptly, rather than a vague warning to "be careful" |
| Next step clarity | 4 | Rightly says to ask Rina promptly given the deadline, but suggests no day or timeframe. That leaves "promptly" as open to reading as the deadline pressure it's meant to answer |
| Tone | 5 | Plain and doesn't accuse anyone. It declines to treat Dev's optimism as bad faith |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | Says plainly that nobody has been contacted, and declines to have this diagnosis contact anyone itself |
| Hallucination risk | 4 | Careful throughout, but "neither, on current evidence, is anyone else yet" the confirmed decision-maker moves from "not yet confirmed" towards doubting Rina's authority in particular. The fair position is that nobody has tested it either way |

## What Worked

- It saw that Dev's enthusiasm and urgency aren't evidence of his own authority, and it didn't rule his authority in or out on job title alone.
- It kept a vague hallway reaction, given before any specifics, apart from a confirmed approval of this enrolment, cohort date and commitment.
- It named the proposed process itself, telling Rina after the paperwork is done, as the thing to avoid. It didn't just flag in general terms that her authority was unconfirmed.
- It declined to treat Dev as acting in bad faith, and declined to guess whether Rina would say yes or no.
- It treated the real deadline as a reason to ask soon, not a reason to skip asking. That's the right response to real urgency: neither ignoring it nor letting it excuse skipping the check.

## What Needed Checking

- Rina may not be the final approver either. Nothing in the scenario says whether another sign-off sits above her, and the diagnosis doesn't raise this as an open question the way the Rowcastle test raised "Group Ops."
- "Ask Rina promptly" would be stronger with a day or short window attached, given the deadline the scenario describes.
- I think the Hallucination risk note above overstates this. Section 4 of the output says plainly that nobody has confirmed Rina's authority and nobody has confirmed she lacks it, and that it hasn't been tested. Only the closing line, "neither, on current evidence, is anyone else yet", could be read as doubting her.

## What I Changed in the Prompt

Nothing, for this run. This run tested most directly the guardrail against treating enthusiasm, or being the main contact, as proof of authority. It held, even against a plan built to make the authority question harder to ask in advance.

## Next Test

Run a scenario where the keen contact's account of a stakeholder's position turns out, once checked, to be right. That would confirm the skill doesn't treat every unconfirmed authority claim as suspect by default, only as unconfirmed until someone checks it.
