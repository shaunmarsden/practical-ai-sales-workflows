# Hartwell Pre Call Review

This review compares the original [Hartwell pre call example](../examples/hartwell-pre-call.md) with a [rerun using the new skill](../examples/hartwell-pre-call-skill-output.md). I scored both against the [sales AI output rubric](sales-ai-output-rubric.md), using the same fictional [source pack](../examples/hartwell-pre-call-input.md).

## Baseline Result

**Original example: 42 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The contact, role, company and meeting purpose all match the source pack |
| Evidence fidelity | 3 | The output doesn't show what each source supports, and drops Alex's direct statement that nobody has mapped the current process. It safely leaves out the public signal but doesn't visibly weigh it |
| Fact separation | 4 | Confirmed context and assumptions are kept apart, though the seller's good outcome isn't labelled as the seller's own aim |
| Missing information | 3 | It flags team size, CRM and platform, but not authority, budget, timescale, the reason for reviewing now, or whether the vacancies are relevant |
| Commercial usefulness | 4 | The questions and conversation paths are practical, though some other topics come in without evidence |
| Next step clarity | 4 | A deeper mapping session is framed as conditional, but it could be clearer that this is the seller's aim |
| Tone | 5 | The opening and questions are natural, short and suitable for a live call |
| Privacy | 5 | It uses only the fictional information needed to prepare |
| Approval discipline | 5 | No message, meeting or CRM action is treated as done |
| Hallucination risk | 4 | The admin hypothesis is labelled, but the other preparation, research and pipeline-review angles aren't grounded in the sources supplied |

## What the Baseline Showed

The existing example is useful and safe. Its weakness is that you can't trace its claims, not that its sales advice is bad. A visitor can't see the sources behind it, and the card doesn't make clear which source supports each claim. It also misses several unknowns that matter before reading anything into Alex's title or the public vacancies.

## Why a Skill Is Justified

Pre-call preparation comes up again and again, uses several kinds of source, and produces the same shape of output. The same safeguards matter every time. Public information mustn't become proof of private pain. A title mustn't become authority. A step the seller wants mustn't become a customer commitment. So a reusable instruction with clear limits is more useful than relying on the short prompt alone.

## Skill Rerun Result

**Skill output: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every named fact, date and source matches the source pack |
| Evidence fidelity | 5 | The source ledger shows what each source supports, and keeps the public vacancies in their proper place |
| Fact separation | 5 | Confirmed context, public background, assumptions, unknowns and the relevance hypothesis stay separate |
| Missing information | 5 | The card flags the current process, CRM, team size, authority, budget, timescale and whether the public signal is relevant |
| Commercial usefulness | 4 | The card supports a sensible exploratory call, but the thin source pack limits how tailored the conversation can be |
| Next step clarity | 4 | The possible workflow mapping session is clearly conditional, though the real next step can only come out of the call |
| Tone | 5 | The opening, questions and voicemail are direct and natural |
| Privacy | 5 | It includes only the fictional information the task needs |
| Approval discipline | 5 | Nothing is treated as sent, booked, agreed or changed |
| Hallucination risk | 4 | The hypotheses are well labelled, but they're still readings a salesperson has to test on the call |

## What Improved

- You can now see the raw fictional sources.
- Each source has a date and a stated purpose.
- Public hiring information stays as background rather than becoming evidence of an internal problem.
- Alex's role stays separate from authority or budget.
- The outcome the seller wants stays separate from a next step the customer has agreed.
- The final card is still short enough to use during the call.

## What Still Needs Checking

- The relevance hypothesis is plausible, not confirmed.
- The public vacancies may have nothing to do with the workflow review.
- The source pack is thin on purpose, so a real card should use any approved recent CRM notes or interactions that exist.
- A strong card can prepare the conversation, but it can't decide which question or path fits once Alex starts answering.

## Independent Forward Test

A fresh agent first ran the skill against the Hartwell source pack. It handled the evidence correctly, but the output added a hyphenated title for the reader, bold labels inside bullets, and a second risks section after the unknowns. I tightened the skill and card template to spell out the repository's formatting and section order.

A second fresh agent then ran the revised skill against a different fictional company, Northbridge Systems. It:

- kept public hiring and expansion signals separate from evidence of an internal problem;
- left the contact's authority, budget and timescale as unknown;
- produced one source ledger and one human check, with no repeated sections;
- avoided hyphenated titles, em dashes and bold labels inside bullets; and
- kept the suggested mapping exercise conditional rather than agreed with the customer.

This shows the instruction worked beyond the Hartwell wording. It doesn't prove it works reliably across models or real users.

## Next Test

Use a harder pre-call case, where a current CRM note conflicts with an older email and a public announcement suggests a plausible but unconfirmed priority. The skill should show both conflicts, ask for the least clarification it needs, and hold back from a confident call angle until the evidence is safe enough.
