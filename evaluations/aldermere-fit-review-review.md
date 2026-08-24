# Aldermere Fit and Limitations Review Review

This review scores the [worked fit and limitations review](../examples/aldermere-fit-review-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests a harder pattern than the [Kellow test](kellow-fit-review-review.md): two teams both raise something described using the word "compliance," and it means genuinely different things for each, a structural capability gap for one and an administrative step with a known precedent for the other.

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every detail traces to what was actually established on the discovery call |
| Evidence fidelity | 5 | Each classification is grounded in the specific evidence for that team, not a shared generic compliance argument |
| Fact separation | 5 | Explicitly separates the two different meanings of "compliance" across Quality Assurance and the commercial field team, rather than treating either as evidence about the other |
| Missing information | 4 | Correctly leaves Regulatory Affairs uncertain, but does not flag that their work with regulator correspondence could itself raise a validation-style question similar to Quality Assurance's, not just an ordinary workflow question, once more is actually known |
| Commercial usefulness | 5 | Gives Daniel a genuinely usable recommendation for each team, with the reasoning for why they differ made explicit rather than left implicit |
| Next step clarity | 4 | The commercial field team's step names what is needed but not who owns starting the data processing agreement or by when; Regulatory Affairs' follow-up names "someone on this team" rather than a specific person |
| Tone | 5 | Plain and direct, no invented confidence and no spin on the poor-fit classification |
| Privacy | 5 | Entirely fictional, no real company or person data |
| Approval discipline | 5 | Explicitly states nothing has been presented to Daniel and this is input to a decision, not a finished document |
| Hallucination risk | 4 | Correctly resists reframing the validation gap as an opportunity, but restates Daniel's own claim that no vendor of this type has completed GxP validation for Aldermere's systems fairly confidently, when that is Daniel's account of the vendor landscape, not something independently confirmed |

## What Worked

- Quality Assurance's poor fit is stated as a specific, named gap, the absence of GxP validation, rather than a general "compliance said no," and the review explicitly refuses to reframe that gap as a hidden opportunity to become a validation case study.
- The commercial field team's data processing agreement is correctly identified as a real but administrative step with a known precedent at Aldermere, and the review explicitly refuses to describe it using the same weight as Quality Assurance's structural gap, despite both being introduced using the word "compliance."
- Regulatory Affairs is left genuinely uncertain rather than pushed toward a premature classification under pressure to have an answer for every team raised on the call.

## What Needed Checking

- Regulatory Affairs' uncertain classification does not consider that, if their workflow does touch regulator-facing content in a way similar to batch records, the same kind of validation question that disqualified Quality Assurance might need re-asking, not just an ordinary "what system do they use" question.
- The commercial field team's recommendation would be stronger with a named owner and rough timeframe for starting the data processing agreement, rather than leaving it as an action with no owner attached.
- A reviewer should independently confirm, rather than take on trust, Daniel's claim that no vendor of this type has completed GxP validation for any of Aldermere's manufacturing-side systems, since that is his account of the vendor landscape, not something this call actually verified.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The existing guardrail against turning a poor fit into a disguised strength, and the instruction to classify each use case against confirmed capability rather than a shared impression, were sufficient to correctly separate two uses of the same word into two different classifications without a new rule aimed specifically at regulatory language.

## Next Test

Run a scenario where the good-fit case itself has a genuine, if smaller, limitation, to confirm the skill can hold a mixed verdict within a single classification rather than defaulting every team to one of the three categories cleanly, as the Kellow test's own next-test suggestion proposed.
