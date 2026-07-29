# Hartwell Pre Call Review

This review compares the original [Hartwell pre call example](../examples/hartwell-pre-call.md) with a [rerun using the new skill](../examples/hartwell-pre-call-skill-output.md). Both are scored against the [sales AI output rubric](sales-ai-output-rubric.md) using the same fictional [source pack](../examples/hartwell-pre-call-input.md).

## Baseline Result

**Original example: 42 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The contact, role, company and meeting purpose all match the source pack |
| Evidence fidelity | 3 | The output does not show what each source supports and drops Alex's direct statement that the current process has not been mapped; the public signal is safely omitted but not visibly assessed |
| Fact separation | 4 | Confirmed context and assumptions are separated, though the seller's good outcome is not labelled as a seller objective |
| Missing information | 3 | Team size, CRM and platform are flagged, but authority, budget, timescale, the reason for reviewing now and the relevance of the vacancies are not |
| Commercial usefulness | 4 | The questions and conversation paths are practical, although some alternative topics are introduced without evidence |
| Next step clarity | 4 | A deeper mapping session is framed as conditional, but its status as a seller objective could be clearer |
| Tone | 5 | The opening and questions are natural, concise and suitable for a live call |
| Privacy | 5 | Only the fictional information needed for preparation is used |
| Approval discipline | 5 | No message, meeting or CRM action is treated as completed |
| Hallucination risk | 4 | The administration hypothesis is labelled, but the alternative preparation, research and pipeline-review angles are not grounded in the supplied sources |

## What the Baseline Showed

The existing example is useful and safe. Its weakness is traceability, not bad sales advice. A visitor cannot inspect the underlying sources, and the card does not make it obvious which source supports each claim. It also misses several unknowns that matter before interpreting Alex's title or the public vacancies.

## Why a Skill Is Justified

Pre-call preparation happens repeatedly, uses several source types and has a stable output shape. The same safeguards matter every time: public information must not become proof of private pain, a title must not become authority and a seller's desired next step must not become a customer commitment. That makes a bounded reusable instruction more useful than relying on the short prompt alone.

## Skill Rerun Result

**Skill output: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every named fact, date and source matches the source pack |
| Evidence fidelity | 5 | The source ledger shows what each source supports and keeps the public vacancies in their proper context |
| Fact separation | 5 | Confirmed context, public background, assumptions, unknowns and the relevance hypothesis remain distinct |
| Missing information | 5 | The card flags the current process, CRM, team size, authority, budget, timescale and relevance of the public signal |
| Commercial usefulness | 4 | The card supports a sensible exploratory call, but the thin source pack limits how tailored the conversation can become |
| Next step clarity | 4 | The possible workflow mapping session is clearly conditional, although the real next step can only emerge during the call |
| Tone | 5 | The opening, questions and voicemail are direct and natural |
| Privacy | 5 | Only the fictional information required for the task is included |
| Approval discipline | 5 | Nothing is treated as sent, booked, agreed or changed |
| Hallucination risk | 4 | The hypotheses are well labelled, but they remain interpretations that a salesperson must test live |

## What Improved

- The raw fictional sources are now inspectable.
- Each source has a date and a stated purpose.
- Public hiring information stays background rather than becoming evidence of an internal problem.
- Alex's role stays separate from authority or budget.
- The seller's desired outcome stays separate from an agreed customer next step.
- The final card is still short enough to use during the call.

## What Still Needs Checking

- The relevance hypothesis is plausible, not confirmed.
- The public vacancies may have nothing to do with the workflow review.
- The source pack is deliberately thin, so a real card should use any approved recent CRM notes or interactions that exist.
- A strong card can prepare the conversation, but it cannot decide which question or path fits once Alex starts answering.

## Independent Forward Test

A fresh agent first ran the skill against the Hartwell source pack. The evidence handling was correct, but the output introduced a hyphenated reader-facing title, bold labels inside bullets and a second risks section after the unknowns. The skill and card template were tightened to make the repository's formatting and section order explicit.

A second fresh agent then ran the revised skill against a different fictional company, Northbridge Systems. It:

- kept public hiring and expansion signals separate from evidence of an internal problem;
- left the contact's authority, budget and timescale unknown;
- produced one source ledger and one human check without duplicating sections;
- avoided hyphenated titles, em dashes and bold labels inside bullets; and
- kept the suggested mapping exercise conditional rather than customer-agreed.

This shows the instruction generalised beyond the Hartwell wording. It does not prove reliable performance across models or real users.

## Next Test

Use a harder pre-call case where a current CRM note conflicts with an older email, and a public announcement suggests a plausible but unconfirmed priority. The skill should show both conflicts, ask for the minimum clarification and avoid producing a confident call angle until the evidence is safe enough.
