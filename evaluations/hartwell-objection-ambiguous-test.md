# Hartwell Ambiguous Objection: Repeated Run Test

This is a stability test, not a single scored example. I ran the same [ambiguous objection](../examples/hartwell-objection-ambiguous-input.md) cold, three times each in Claude, ChatGPT and Gemini. I wanted to see whether the objection-handling workflow picks the *same* driver each time, or swings between readings when the answer isn't clear. It uses the [test run template](test-run-template.md) and scores against the [sales AI output rubric](sales-ai-output-rubric.md).

## Method Note

Claude ran the three Claude runs, each in a fresh conversation. I ran the ChatGPT and Gemini runs by hand with the same input and pasted them back for scoring, because Claude can't reach those sites. The [cross-model post-call comparison](cross-model-post-call-comparison.md) used the same split, and its Copilot caveat applies here too: I couldn't test Copilot.

**One thing this page can't settle.** The input file's description used to say the scenario is ambiguous on purpose, and that you can't cleanly work out the real driver from the context. I've taken that out of the input. This page never recorded where the pasted input started and stopped, so I can't tell whether the nine runs saw that sentence. If they did, the models were told the driver couldn't be worked out before being asked to work it out, which is what this test was measuring.

## Scenario

Priya Chen's reply after the QBR is unclear. It mixes timing, a sign the reason to buy may be shrinking (AE roles "up in the air"), resistance to change ("a new tool they have to learn"), and a possible soft no ("let me sit with it"), with no date and no clear blocker. The full input is in the [scenario file](../examples/hartwell-objection-ambiguous-input.md). There's no single "correct" primary driver, only better and worse ways of handling not knowing.

## The Headline: Primary Driver Diagnosed, Per Run

| Run | Primary driver diagnosed | Total / 50 |
| --- | --- | ---: |
| Claude 1 | Circumstances (timing) | 48 |
| Claude 2 | Shrinking rationale (case may not size up) | 49 |
| Claude 3 | Soft-no risk (keep it alive) | 46 |
| ChatGPT 1 | Circumstances (timing) | 47 |
| ChatGPT 2 | Circumstances (timing) | 47 |
| ChatGPT 3 | Circumstances (timing) | 47 |
| Gemini 1 | Circumstances (timing) | 45 |
| Gemini 2 | Circumstances (timing) | 45 |
| Gemini 3 | Circumstances (timing) | 46 |

What I didn't expect: **ChatGPT and Gemini were more stable than Claude.** All six of their runs picked circumstances (timing) as the main driver and stayed within a point or two of each other. Claude put a different driver first in each of its three runs. Higher top scores, less consistency.

## Claude, Per Area

| Area | Run 1 | Run 2 | Run 3 |
| --- | ---: | ---: | ---: |
| Factual accuracy | 5 | 5 | 5 |
| Evidence fidelity | 5 | 5 | 4 |
| Fact separation | 5 | 5 | 5 |
| Missing information | 5 | 5 | 4 |
| Commercial usefulness | 4 | 5 | 4 |
| Next step clarity | 4 | 4 | 5 |
| Tone | 5 | 5 | 5 |
| Privacy | 5 | 5 | 5 |
| Approval discipline | 5 | 5 | 5 |
| Hallucination risk | 5 | 5 | 4 |
| **Total** | **48** | **49** | **46** |

Run 2 led with the shrinking case: *"If the team is contracting, this is not a timing objection, it is a question about whether the case still sizes up. That needs clarifying before anything else."*

## ChatGPT, Per Model

All three runs scored 47/50, the most disciplined and neutral of the three models. Each picked circumstances (timing) as the main driver, and ruled out an "other people" objection because Priya holds the budget, as the workflow intends.

ChatGPT 2 came closest of any ChatGPT or Gemini run to the sharpest reading, with a two-way question: *"the business case still stands but the timing is wrong; or something emerged in the QBR that has weakened the case."* It put the cause on the QBR, not on the "AE roles up in the air" signal.

Each run lost one point on commercial usefulness, for treating "roles up in the air" as team disruption rather than a possible threat to the size of the case, and one on next-step clarity, for leaving the cadence a little open.

## Gemini, Per Model

Runs scored 45, 45 and 46. Gemini was as stable on timing, and good at naming unknowns. Gemini 1 listed *"whether the AE team is growing or shrinking"* as unknown. It noticed the headcount question more openly than ChatGPT, but didn't carry it into the reply as a commercial risk either.

It lost points for the same two things every time:

- The reframe leaned persuasive. Every Gemini run pushed a version of "adopting now would actually relieve pressure during the reorg," which gently argues *against* the timing concern Priya had just raised. It isn't a hard failure, since a reframe may offer another view, but it's the one place any model edged towards arguing with the stated driver. It cost a point on hallucination risk (a slightly overclaimed benefit) and on tone.
- It chose its own cadence. Each run set an internal "2 to 3 week" follow-up. That's acceptable, as it isn't a promise to Priya and the reply still asks her for timing, but Claude and ChatGPT left the cadence to be agreed.

## Where All Nine Runs Agreed

- No run made up a fact. None decided the reorg outcome, the headcount direction or the QBR result. All nine treated those as unknown.
- No run offered a discount or disqualified the deal, and none pushed to close straight away.
- All nine isolated the objection rather than assume. Every run ended by asking Priya to confirm the real blocker. This is the most important result, because it's what makes the differences below safe.
- All nine settled on a dated follow-up.

## Where Runs Disagreed

The sharpest commercial reading was rare. Treating "AE roles up in the air" as a possible threat to the *size* of the case, not just its timing, led only once in nine, in Claude Run 2. Several ChatGPT and Gemini runs noticed the headcount question but didn't act on it.

## Conclusion

When the answer isn't clear, the workflow is **stable where it matters and varies where that's acceptable, across all three models.** The guardrails held on every run. Judgement moved. Safety didn't.

Claude produced the two highest-scoring runs but was the least consistent about its first driver. ChatGPT was the most consistent and disciplined, but never raised the sharpest commercial angle. Gemini was consistent too, but leaned harder on persuasion in the reframe, which is the thing to watch on a real timing objection.

Two practical lessons:

1. For an unclear objection, the isolate step and human review aren't optional. Every version asks the prospect to confirm the driver rather than betting the reply on a guess, so a different primary driver each run does no harm. Never trust a single run of an unclear case unchecked.
2. Put the sharpest reading into the skill guidance. When an objection holds a signal that could shrink the *reason to buy* (here, fewer account executives to serve), not just delay the decision, the reply should clarify that first. Only one run in nine did this unprompted, so it's worth writing into the [objection-response skill](../.agents/skills/objection-response/SKILL.md).
