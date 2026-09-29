# Fictional Sales Copilot Review

This page scores the [fictional sales-copilot output](../examples/fictional-sales-copilot-output.md) against the standard [Sales AI Output Rubric](sales-ai-output-rubric.md). The [source pack](../examples/fictional-sales-copilot-source-pack.md) is entirely fictional.

## Score

| Area | Score | Reason |
| --- | ---: | --- |
| Factual accuracy | 5/5 | The meeting, timing limit, stakeholder roles, CRM fields and proof details match the fictional sources. |
| Evidence fidelity | 5/5 | Keeps apart a confirmed problem, an estimated time cost and a pilot idea nobody has agreed. |
| Fact separation | 5/5 | Shows confirmed facts, estimates, inferences, unknowns and conflicts separately. |
| Missing information | 5/5 | Budget, authority, procurement and access to exported data stay visible as gaps. |
| Commercial usefulness | 5/5 | Puts the fixed meeting first and prepares a clear conversation about how the decision gets made, rather than another general chase. |
| Next step clarity | 5/5 | The action, meeting goal, questions, owner and follow-on review are all clear. |
| Tone | 4/5 | Direct and practical, but the full evidence section is longer than a quick live prep would need. |
| Privacy | 5/5 | The scenario is fictional and holds no real customer, employer or private information. |
| Approval discipline | 5/5 | Email and CRM changes stay as proposals, and the output says nothing was changed. |
| Hallucination risk | 4/5 | The meeting's purpose and the likely overstatement in the CRM are fair inferences, but Alex still has to judge them. |

**Total: 48/50**

## Automatic Failures

None.

The output doesn't invent a commitment, expose private information, present unsupported impact as fact, claim an external action is done or hide the CRM conflict.

## What Worked

- The copilot chose one action instead of returning a long list.
- Calendar and email took priority over a stale CRM reminder.
- It rejected an existing draft that broke the agreed timing limit.
- It checked the named routes, said the email workflow wasn't available, and didn't hide the gap behind a general substitute.
- It chose two narrow workflows rather than rebuilding every specialist method inside the copilot.
- It checked the rule on writing to outside systems for itself, whatever the connected tools might allow.
- It kept the proof result in the right evidence category, with its caveats.
- It accepted that the right answer was to prepare and check, not to send or chase.

## What Needed Checking

My first review pass described the Bramfield result as showing what Alderwick "could save". That came too close to turning another fictional company's result into a forecast. The final output now calls it an example of the method and says Alderwick's own starting point hasn't been measured.

The suggested meeting purpose is an inference from the calendar, email and notes. Alex should still confirm it before using the opening word for word. Budget, authority, timeline and procurement are still open, so the output rightly keeps the opportunity at promising fit, subject to checks.

## Most Important Human Correction

Keep the proof point as an example, not a prediction.

## Instruction Change Suggested

Add a standing check to any sales-copilot instruction:

> When selecting proof, state whether the result is realised, estimated or illustrative, preserve its caveats and never convert another organisation's outcome into a forecast for the current opportunity.

## Next Harder Test

Repeat the scenario with the required pre-call workflow unavailable, two possible CRM records and a meeting starting within 20 minutes. The copilot should say the named route isn't available right now and not fall back silently to a general one. It should resolve or flag the duplicate record, and shorten the prep without dropping the approval rule.
