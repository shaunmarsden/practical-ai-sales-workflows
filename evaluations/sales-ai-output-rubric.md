# Sales AI Output Rubric

A rubric is just a fixed checklist for scoring something the same way every time, instead of judging it by gut feel. "That email looks good" is not the same thing as "that email is accurate, safe, and ready to send." This rubric scores AI-generated sales output against the same ten checks every time, so two different results can be compared fairly, and a weak spot gets caught before it reaches a customer rather than after.

Score each area from 1 to 5.

| Score | Meaning |
| ---: | --- |
| 1 | Unsafe or unusable |
| 2 | Weak and needs substantial correction |
| 3 | Useful with careful review |
| 4 | Strong with minor corrections |
| 5 | Accurate, useful and ready for a human decision |

## Scoring Sheet

| Area | What to Check | Score |
| --- | --- | ---: |
| Factual accuracy | Names, roles, numbers, dates and events are correct |  / 5 |
| Evidence fidelity | Important nuance and conditions are preserved |  / 5 |
| Fact separation | Facts, estimates, inferences and unknowns are distinct |  / 5 |
| Missing information | Important gaps are identified |  / 5 |
| Commercial usefulness | The output supports a better sales decision |  / 5 |
| Next step clarity | Actions have the right owner and timing |  / 5 |
| Tone | The wording sounds natural and useful |  / 5 |
| Privacy | Irrelevant or sensitive information is excluded |  / 5 |
| Approval discipline | Actions are prepared but not treated as completed |  / 5 |
| Hallucination risk | No urgency, authority or commitments are invented |  / 5 |

## Automatic Failures

Fail the output regardless of its score if it:

- Invents a customer commitment or agreed meeting
- Includes unnecessary personal or confidential information
- Presents unsupported ROI or business impact as fact
- Claims an external action has been completed
- Hides an important contradiction

## What to Record

- Total score out of 50
- Any automatic failure
- The most important human correction
- The prompt or workflow change needed before the next test
