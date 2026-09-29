# Aldermere Fit and Limitations Review Review

This page scores the [worked fit and limitations review](../examples/aldermere-fit-review-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests a harder pattern than the [Kellow test](kellow-fit-review-review.md). Two teams both raise something they call "compliance," and it means different things for each. For one it's a gap in what the product can do. For the other it's an admin step that has been done before.

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every detail traces to what the discovery call established |
| Evidence fidelity | 5 | Bases each classification on the evidence for that team, not a shared, general compliance argument |
| Fact separation | 5 | Separates the two meanings of "compliance" for Quality Assurance and the commercial field team, rather than treating either as evidence about the other |
| Missing information | 4 | Rightly leaves Regulatory Affairs uncertain, but doesn't flag that their work on regulator correspondence could raise a validation question like Quality Assurance's, not just an ordinary workflow question, once more is known |
| Commercial usefulness | 5 | Gives Daniel a usable recommendation for each team, and says why they differ |
| Next step clarity | 4 | The commercial field team's step names what's needed but not who starts the data processing agreement or by when. Regulatory Affairs' follow-up names "someone on this team" rather than a specific person |
| Tone | 5 | Plain and direct, no invented confidence and no spin on the poor-fit classification |
| Privacy | 5 | Entirely fictional, no real company or person data |
| Approval discipline | 5 | Says nothing has been presented to Daniel and this is input to a decision, not a finished document |
| Hallucination risk | 4 | Rightly refuses to recast the validation gap as an opportunity. But it repeats Daniel's claim, that no vendor of this type has completed GxP validation for Aldermere's systems, fairly confidently. That's Daniel's account of the market, not something anyone has checked |

## What Worked

It states Quality Assurance's poor fit as a specific, named gap, the lack of GxP validation, rather than a general "compliance said no," and it refuses to recast that gap as a hidden chance to become a validation case study.

It sees the commercial field team's data processing agreement as a real but admin step, one Aldermere has done before. It refuses to give it the same weight as Quality Assurance's gap in capability, even though both came up under the word "compliance."

It leaves Regulatory Affairs uncertain rather than forcing an early classification just to have an answer for every team raised on the call.

## What Needed Checking

Regulatory Affairs' uncertain classification doesn't consider one risk. If their work touches regulator-facing content the way batch records do, the same validation question that ruled out Quality Assurance may need asking again, not just an ordinary "what system do they use" question.

The commercial field team's recommendation would be stronger with a named owner and rough timeframe for starting the data processing agreement, rather than an action with no owner.

A reviewer should check Daniel's claim, rather than take it on trust, that no vendor of this type has completed GxP validation for any of Aldermere's manufacturing systems. It's his account of the market, and this call didn't verify it.

## What I Changed in the Prompt

Nothing in the skill needed changing for this run. The existing guardrail against dressing up a poor fit as a strength was enough. So was the instruction to classify each use case against confirmed capability rather than a shared impression. Together they split two uses of the same word into two classifications, without a new rule aimed at regulatory language.

## Next Test

Run a scenario where the good-fit case has a real, if smaller, limitation. That confirms the skill can hold a mixed verdict inside one classification, rather than sorting every team cleanly into one of the three categories. The Kellow test's own next-test note proposed this.
