# Northstar Ambiguous Objection: Repeated Run Test

A stability test, not a single scored example. The same deliberately [ambiguous objection](../examples/northstar-objection-ambiguous-input.md) was run cold, three times, to see whether the objection-handling workflow diagnoses the *same* driver each time or swings between readings under genuine uncertainty. It uses the [test run template](test-run-template.md) and scores against the [sales AI output rubric](sales-ai-output-rubric.md).

> **Status: partial.** The three Claude runs below are complete. The ChatGPT and Gemini columns are still to be run by Shaun, using the identical input, before any cross-model conclusion can be drawn. Because I cannot access chatgpt.com or gemini.google.com, those runs have to be done by hand and pasted back for scoring, the same method as the [cross-model post-call comparison](cross-model-post-call-comparison.md).

## Scenario

An ambiguous post-QBR reply from Priya Chen that mixes timing, a possible shrinking rationale (AE roles "up in the air"), change-resistance ("a new tool they have to learn"), and a possible soft no ("let me sit with it"), with no date and no clear blocker. Full input, including what Shaun does and does not know, is in the [scenario file](../examples/northstar-objection-ambiguous-input.md). The point of the scenario is that the driver is genuinely not resolvable from context.

## Runs

| Field | Run 1 | Run 2 | Run 3 |
| --- | --- | --- | --- |
| Model | Claude | Claude | Claude |
| Version | Opus 4.8 | Opus 4.8 | Opus 4.8 |
| Date run | 2026-07-19 | 2026-07-19 | 2026-07-19 |
| Conversation state | Fresh, cold | Fresh, cold | Fresh, cold |
| Input | The scenario file, applied through the [objection-handling prompt](../templates/objection-handling-prompt.md) | Same | Same |

## What Each Run Diagnosed as the Primary Driver

- **Run 1** — foregrounded **circumstances (timing)**: *"The reorg reads as the primary driver: this is most likely a genuine 'not now' rather than a 'no', with the headcount uncertainty as a secondary risk to check."*
- **Run 2** — foregrounded a **shrinking rationale**: *"The signal that actually threatens the case is 'a couple of the AE roles are up in the air'. If the team is contracting, this is not a timing objection, it is a question about whether the case still sizes up. That needs clarifying before anything else."*
- **Run 3** — foregrounded **soft-no risk**: *"'Let me sit with it' with no date is the signal I would weight most. The priority is a low-friction reason to re-engage, not winning an argument about any single driver."*

All three explicitly stated the objection was mixed and could not be cleanly resolved. Where they differed was in **which driver they promoted to primary**, and therefore what the response led with.

## Scores

| Area | Run 1 | Run 2 | Run 3 | ChatGPT | Gemini |
| --- | ---: | ---: | ---: | ---: | ---: |
| Factual accuracy | 5 | 5 | 5 | | |
| Evidence fidelity | 5 | 5 | 4 | | |
| Fact separation | 5 | 5 | 5 | | |
| Missing information | 5 | 5 | 4 | | |
| Commercial usefulness | 4 | 5 | 4 | | |
| Next step clarity | 4 | 4 | 5 | | |
| Tone | 5 | 5 | 5 | | |
| Privacy | 5 | 5 | 5 | | |
| Approval discipline | 5 | 5 | 5 | | |
| Hallucination risk | 5 | 5 | 4 | | |
| **Total** | **48** | **49** | **46** | | |

## Where Runs Agreed

This is the reassuring part, and it maps onto the workflow's guardrails rather than its judgement:

- **No run invented a fact.** None of them decided the reorg outcome, the headcount direction, or the QBR result. All three explicitly held those as unknowns, exactly as the scenario requires.
- **No run offered a discount.** Nothing in the objection asked for one, and none appeared.
- **No run disqualified the deal, and none pushed for a close.** All three read "I think there's something here" as a live signal and "let me sit with it" as a pause, not a firm no.
- **All three isolated rather than assuming.** Every run ended by asking Priya to confirm the real blocker rather than answering only its own guess. This is what stops the divergence below from being dangerous.

## Where Runs Disagreed

- **Which driver led the response.** Run 1 led with timing, Run 2 with the headcount risk, Run 3 with re-engagement. A prospect reading the three replies would get three noticeably different opening moves, even though all three then isolate.
- **Commercial sharpness varied.** Run 2 scored highest on commercial usefulness because it caught that "AE roles up in the air" could undermine the *size* of the case, not just its timing, the most commercially consequential reading, and led with clarifying it. Run 1 and Run 3 treated headcount as a secondary check rather than the headline.
- **Run 3 traded a little rigour for warmth.** It weighted "keep it alive" highly and, in doing so, said slightly less about the headcount risk (hence the 4s on evidence fidelity and missing information). It is the friendliest reply and the one that does least to protect Shaun from a case that may have quietly weakened.

## Interim Conclusion (Claude only)

Under genuine ambiguity, the workflow is **stable where it matters and variable where variation is acceptable.** The guardrails held every time: no invented facts, no discount, no false disqualification, and always an isolate step. What moved between runs was which plausible driver got promoted to primary, which is a judgement call a competent human would also make differently on different days.

The practical implication: for a clean objection like the [price example](../examples/northstar-objection-response.md), a single run is trustworthy. For a genuinely ambiguous one, the isolate step and human review are not optional niceties, they are what makes the variation safe. The workflow does not remove the judgement here; it structures it and stops it going off the rails.

Run 2's instinct, to treat "AE roles up in the air" as a possible threat to the size of the case rather than just its timing, is the strongest single move across the three and worth folding into the skill guidance: when an objection contains a signal that could shrink the *rationale*, not just delay the decision, prioritise clarifying that.

**This conclusion is provisional.** It describes how one model behaves across three runs. Whether ChatGPT and Gemini stay as stable on the guardrails, or swing more on the primary driver, is exactly what the empty columns above are for.
