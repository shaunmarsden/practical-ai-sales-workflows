# Hartwell Ambiguous Objection: Repeated Run Test

A stability test, not a single scored example. The same deliberately [ambiguous objection](../examples/hartwell-objection-ambiguous-input.md) was run cold, three times each in Claude, ChatGPT and Gemini, to see whether the objection-handling workflow diagnoses the *same* driver each time or swings between readings under genuine uncertainty. It uses the [test run template](test-run-template.md) and scores against the [sales AI output rubric](sales-ai-output-rubric.md).

## Method Note

The three Claude runs were run by Claude in fresh, cold conversations. The ChatGPT and Gemini runs were run by hand by Shaun, using the identical input, and pasted back for scoring, because Claude cannot access chatgpt.com or gemini.google.com. This is the same split used in the [cross-model post-call comparison](cross-model-post-call-comparison.md). Copilot is again absent, since it was not available to test; see that comparison's caveat, which applies here too.

## Scenario

An ambiguous post-QBR reply from Priya Chen that mixes timing, a possible shrinking rationale (AE roles "up in the air"), change-resistance ("a new tool they have to learn"), and a possible soft no ("let me sit with it"), with no date and no clear blocker. Full input, including what Shaun does and does not know, is in the [scenario file](../examples/hartwell-objection-ambiguous-input.md). The point of the scenario is that the driver is genuinely not resolvable from context, so there is no single "correct" primary driver, only better and worse ways of handling not knowing.

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

The finding that was not expected: **ChatGPT and Gemini were more stable than Claude.** All six of their runs picked circumstances (timing) as the primary driver and stayed within a point or two of each other. Claude, run the same way, promoted a different driver to primary in each of its three runs. Higher peak scores, lower consistency.

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

Where they differed, quoted directly:

- **Run 1** led with timing: *"The reorg reads as the primary driver: this is most likely a genuine 'not now' rather than a 'no', with the headcount uncertainty as a secondary risk to check."*
- **Run 2** led with the shrinking rationale: *"If the team is contracting, this is not a timing objection, it is a question about whether the case still sizes up. That needs clarifying before anything else."*
- **Run 3** led with re-engagement: *"'Let me sit with it' with no date is the signal I would weight most. The priority is a low-friction reason to re-engage."*

## ChatGPT, Per Model

All three runs scored 47/50. They were the most disciplined and neutral of the three models. Each one:

- Diagnosed circumstances (timing) as primary, and explicitly ruled out an "other people" objection using Priya's budget authority, exactly as the workflow intends.
- Isolated well. ChatGPT 2 came closest of any external run to the sharpest reading, offering a two-way isolate: *"the business case still stands but the timing is wrong; or something emerged in the QBR that has weakened the case."* It gestured at the case itself weakening, though it pinned the cause on the QBR rather than on the "AE roles up in the air" signal.
- Lost one point on commercial usefulness (treating "roles up in the air" as team disruption rather than a possible threat to the size of the case) and one on next-step clarity (asking Priya to pick a revisit point, which is correct, but leaving the cadence slightly open).

They invented nothing, offered no discount, and did not disqualify. On this case, ChatGPT was the safest pair of hands.

## Gemini, Per Model

Runs scored 45, 45 and 46. Also fully stable on the timing diagnosis, and good at naming the unknowns: Gemini 1 explicitly listed *"whether the AE team is growing or shrinking"* as unknown, and Gemini 3 flagged *"what 'up in the air' means for her headcount."* So Gemini noticed the headcount ambiguity more openly than ChatGPT did, but, like ChatGPT, did not carry it into the response as a commercial risk.

Two consistent deductions:

- **The reframe leaned persuasive.** Every Gemini run pushed a version of "adopting now would actually relieve pressure during the reorg," for example *"giving them back that time on every single account could actually relieve operational pressure right now, rather than adding a heavy burden."* That is a reframe that mildly argues *against* the timing concern Priya just raised, rather than respecting it. It is not a hard failure, reframing is allowed to offer perspective, but it is the one place any model edged toward arguing with the stated driver. Costs a point on hallucination risk (a lightly overclaimed benefit) and tone.
- **Self-prescribed cadence.** Each run set an internal "2 to 3 week" follow-up. This is acceptable, it is an internal task, not a commitment promised to Priya, and the reply still asks her for timing, but it is a self-generated number where Claude and ChatGPT left the cadence to be agreed. Worth noting rather than penalising heavily.

Gemini 3 also contained a visible typo in its analysis ("Circstances"), a polish issue that did not reach the customer-facing draft.

## Where All Nine Runs Agreed

This is the reassuring part, and it is model-robust:

- **No run invented a fact.** Not one decided the reorg outcome, the headcount direction, or the QBR result. All nine held those as unknowns, as the scenario requires.
- **No run offered a discount.** Nothing in the objection asked for one, and none appeared.
- **No run disqualified the deal, and none pushed for an immediate close.** All read "I think there's something here" as live and "let me sit with it" as a pause.
- **All nine isolated rather than assuming.** Every run ended by asking Priya to confirm the real blocker. This is the single most important result: it is what makes the divergence below safe.
- **All nine landed on a dated follow-up** as the pipeline decision.

## Where Runs Disagreed

- **Which driver led the response.** Claude swung across all three of timing, shrinking-rationale, and soft-no. ChatGPT and Gemini stayed locked on timing. A prospect would get a noticeably different opening move from Claude depending on the run, and a consistent one from the other two.
- **The sharpest commercial read is rare, and not flattering to any one model.** The strongest single move across all nine runs, treating "AE roles up in the air" as a possible threat to the *size* of the case rather than just its timing, appeared as the lead only once, in Claude Run 2. Several external runs *noticed* the headcount ambiguity but did not act on it. So noticing the signal was common; leading with it happened once in nine.
- **Respecting versus nudging the stated concern.** ChatGPT respected the timing concern most cleanly. Gemini consistently nudged toward adopting now. Claude sat in between.

## Conclusion

Under genuine ambiguity, the workflow is **stable where it matters and variable where variation is acceptable, across all three models.** The guardrails held on every single run: no invented facts, no discount, no false disqualification, always an isolate step, always a dated follow-up. That robustness is the main result and it is not model-specific.

What moved was judgement, not safety. Claude produced the two highest-scoring individual runs but was the least consistent about which driver it foregrounded. ChatGPT was the most consistent and the most disciplined, at the cost of never surfacing the sharpest commercial angle. Gemini was consistent too but leaned harder on persuasion in the reframe, which is the behaviour to watch on a genuine timing objection.

Two practical takeaways:

1. **For an ambiguous objection, the isolate step and human review are not optional.** They are what turns "the model picked a different primary driver this time" from a risk into a non-event, because every version still asks the prospect to confirm the driver rather than betting the response on a guess. A single run of an ambiguous case should never be trusted unattended, from any of these models.
2. **Fold the sharpest read into the skill guidance.** When an objection contains a signal that could shrink the *rationale* (here, fewer account executives to serve), not just delay the decision, the response should prioritise clarifying that. Only one run in nine did this unprompted, which means it is worth making explicit in the [objection-response skill](../.agents/skills/objection-response/SKILL.md) rather than hoping the model finds it.
