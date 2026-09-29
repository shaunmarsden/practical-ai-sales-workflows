# Hartwell Ambiguous Objection: Repeated Run Test

This is a stability test, not a single scored example. I ran the same [ambiguous objection](../examples/hartwell-objection-ambiguous-input.md) cold, three times each in Claude, ChatGPT and Gemini. I wanted to see whether the objection-handling workflow picks the *same* driver each time, or swings between readings when the answer isn't clear. It uses the [test run template](test-run-template.md) and scores against the [sales AI output rubric](sales-ai-output-rubric.md).

## Method Note

Claude ran the three Claude runs, each in a fresh conversation. I ran the ChatGPT and Gemini runs by hand with the same input and pasted them back for scoring, because Claude can't reach chatgpt.com or gemini.google.com. The [cross-model post-call comparison](cross-model-post-call-comparison.md) used the same split. Copilot is missing again because I couldn't test it, and that comparison's caveat applies here too.

**One thing this page can't settle.** The input file's description used to say the scenario is ambiguous on purpose, and that you can't cleanly work out the real driver from the context. That point belongs here, and it's in the section below. I've taken it out of the input. This page never recorded where the pasted input started and stopped, so I can't now tell whether the nine runs saw that sentence. If they did, the models were told the driver couldn't be worked out before being asked to work it out, which is exactly what this test was measuring.

## Scenario

Priya Chen's reply after the QBR is unclear. It mixes timing, a sign the reason to buy may be shrinking (AE roles "up in the air"), resistance to change ("a new tool they have to learn"), and a possible soft no ("let me sit with it"), with no date and no clear blocker. The full input, including what the seller does and doesn't know, is in the [scenario file](../examples/hartwell-objection-ambiguous-input.md). You can't work out the driver from the context, so there's no single "correct" primary driver, only better and worse ways of handling not knowing.

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

What I didn't expect: **ChatGPT and Gemini were more stable than Claude.** All six of their runs picked circumstances (timing) as the main driver, and stayed within a point or two of each other. Claude, run the same way, put a different driver first in each of its three runs. Higher top scores, less consistency.

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

Where they differed, in their own words:

- Run 1 led with timing: *"The reorg reads as the primary driver: this is most likely a genuine 'not now' rather than a 'no', with the headcount uncertainty as a secondary risk to check."*
- Run 2 led with the shrinking case: *"If the team is contracting, this is not a timing objection, it is a question about whether the case still sizes up. That needs clarifying before anything else."*
- Run 3 led with getting back in touch: *"'Let me sit with it' with no date is the signal I would weight most. The priority is a low-friction reason to re-engage."*

## ChatGPT, Per Model

All three runs scored 47/50. They were the most disciplined and neutral of the three models. Each one:

- Picked circumstances (timing) as the main driver, and ruled out an "other people" objection because Priya holds the budget, as the workflow intends.
- Isolated the objection well. ChatGPT 2 came closest of any ChatGPT or Gemini run to the sharpest reading, with a two-way question: *"the business case still stands but the timing is wrong; or something emerged in the QBR that has weakened the case."* It pointed at the case itself weakening, but put the cause on the QBR rather than on the "AE roles up in the air" signal.
- Lost one point on commercial usefulness, for treating "roles up in the air" as team disruption rather than a possible threat to the size of the case. Lost one on next-step clarity, for asking Priya to pick a revisit point, which is right, but leaving the cadence a little open.

They made up nothing, offered no discount, and didn't disqualify. On this case, ChatGPT was the safest.

## Gemini, Per Model

Runs scored 45, 45 and 46. Gemini was just as stable on timing, and good at naming the unknowns. Gemini 1 listed *"whether the AE team is growing or shrinking"* as unknown, and Gemini 3 flagged *"what 'up in the air' means for her headcount."* So Gemini noticed the headcount question more openly than ChatGPT did. But like ChatGPT, it didn't carry it into the reply as a commercial risk.

It lost points for the same two things every time:

- The reframe leaned persuasive. Every Gemini run pushed a version of "adopting now would actually relieve pressure during the reorg," for example *"giving them back that time on every single account could actually relieve operational pressure right now, rather than adding a heavy burden."* That gently argues *against* the timing concern Priya had just raised, rather than respecting it. It isn't a hard failure, because a reframe is allowed to offer another view. But it's the one place any model edged towards arguing with the stated driver. It cost a point on hallucination risk (a slightly overclaimed benefit) and tone.
- It chose its own cadence. Each run set an internal "2 to 3 week" follow-up. That's acceptable: it's an internal task, not a promise to Priya, and the reply still asks her for timing. But Gemini chose the number itself, where Claude and ChatGPT left the cadence to be agreed. Worth noting rather than marking down heavily.

Gemini 3 also had a visible typo in its analysis ("Circstances"). It didn't reach the draft for the customer.

## Where All Nine Runs Agreed

This is the reassuring part, and it held for every model:

- No run made up a fact. None decided the reorg outcome, the headcount direction or the QBR result. All nine treated those as unknown, as the scenario requires.
- No run offered a discount. Nothing in the objection asked for one.
- No run disqualified the deal, and none pushed to close straight away. All read "I think there's something here" as live and "let me sit with it" as a pause.
- All nine isolated the objection rather than assume. Every run ended by asking Priya to confirm the real blocker. This is the most important result, because it's what makes the differences below safe.
- All nine settled on a dated follow-up as the pipeline decision.

## Where Runs Disagreed

- Which driver led. Claude swung across all three: timing, the shrinking case and the soft no. ChatGPT and Gemini stayed on timing. A prospect would get a clearly different opening from Claude depending on the run, and the same one from the other two.
- The sharpest commercial reading was rare, and no model did it reliably. The strongest single move across all nine runs was treating "AE roles up in the air" as a possible threat to the *size* of the case, not just its timing. It led only once, in Claude Run 2. Several ChatGPT and Gemini runs *noticed* the headcount question but didn't act on it. So noticing the signal was common. Leading with it happened once in nine.
- Respecting the stated concern or nudging it. ChatGPT respected the timing concern most cleanly. Gemini kept nudging towards adopting now. Claude sat in between.

## Conclusion

When the answer isn't clear, the workflow is **stable where it matters and varies where that's acceptable, across all three models.** The guardrails held on every run: no made-up facts, no discount, no false disqualification, always an isolate step, always a dated follow-up. That's the main result, and it isn't specific to one model.

Judgement moved. Safety didn't. Claude produced the two highest-scoring runs but was the least consistent about which driver it put first. ChatGPT was the most consistent and disciplined, but never raised the sharpest commercial angle. Gemini was consistent too, but leaned harder on persuasion in the reframe, which is the thing to watch on a real timing objection.

Two practical lessons:

1. For an unclear objection, the isolate step and human review aren't optional. They turn "the model picked a different primary driver this time" from a risk into nothing, because every version still asks the prospect to confirm the driver rather than betting the reply on a guess. Never trust a single run of an unclear case unchecked, from any of these models.
2. Put the sharpest reading into the skill guidance. When an objection holds a signal that could shrink the *reason to buy* (here, fewer account executives to serve), not just delay the decision, the reply should clarify that first. Only one run in nine did this unprompted, so it's worth writing into the [objection-response skill](../.agents/skills/objection-response/SKILL.md) rather than hoping the model finds it.
