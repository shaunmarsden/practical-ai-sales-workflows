# Hartwell Chase Prompt Review

This review scores the [worked decision](../examples/hartwell-chase-prompt-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests the [chase sequence prompt](../templates/chase-sequence-prompt.md), which is a different file from the [Plan a Chase Sequence skill](../.agents/skills/plan-chase-sequence/SKILL.md) scored in the [chase decision review](hartwell-chase-review.md). The prompt is a shortened version of the skill, so they're related, but neither score is evidence for the other.

The prompt exists because the [Chase a Quiet Prospect recipe card](../recipes/chase-a-quiet-prospect.md) had nothing to paste. It said everything a reader needed was on the card, then sent them to a skill file that opens by saying it isn't written to be read start to finish.

> **The scenario has changed since I scored this.** It now names the weekdays, so the promised Thursday is 9th July, and its clash with the leave can be checked rather than inferred. I scored this record against the version without them. The [stale-date test](chase-stale-date-test.md) says why I added them.

## Method Note

I pasted the prompt into a fresh, isolated context with only the [scenario](../examples/hartwell-chase-input.md) below it, after removing the scenario's answer key as its own warning says. The run didn't know it was a test, didn't see the rubric, and had no access to this repository. The output is reproduced unedited.

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every date, the automatic reply, the CRM task and the conditional transcript approval appear exactly as supplied, with nothing misstated |
| Evidence fidelity | 4 | The newer automatic reply rightly outweighs the older CRM task, and the transcript stays conditional throughout. But it never mentions Alex's own Thursday commitment, and the case plants a conflict between that and his leave dates |
| Fact separation | 5 | It labels its own sections "Evidenced", "Not evidence of lost interest" and "Unconfirmed", and separates the known from the inferred without being asked to use those words |
| Missing information | 4 | It names three unknowns and three things to watch for, but the Thursday timing isn't among them |
| Commercial usefulness | 5 | It reaches the right decision, gives reasoning a person can check, and leaves a clear way back into the opportunity |
| Next step clarity | 4 | It gives a revisit window and three concrete things to prepare, though the owner is implied, not stated |
| Tone | 5 | Plain and direct, with no filler and no hedging that hides the decision |
| Privacy | 5 | Uses only the fictional information supplied and adds no unneeded personal detail |
| Approval discipline | 4 | Nothing is treated as sent or changed, and it writes "No message yet". But it proposes moving the CRM due date without saying in that line that a person must approve it |
| Hallucination risk | 5 | Invents nothing. It won't promote Priya from a name mentioned once to a real route, and labels the revisit date as a plan, not an agreement |

## What Worked

- It didn't obey the stale CRM task. It noticed the task was created before the automatic reply arrived, and said the later information replaces it.
- It told an out-of-office notice apart from a reply waiting for an answer. The prompt's own stop condition depends on that difference.
- It refused to treat Priya as another stakeholder to try, and said why: she was mentioned but never named as a route.
- It chose not to draft a message at all, which is the harder answer on this scenario, and still produced something useful for later.

## What It Missed

**The Thursday conflict.** On 7th July Alex said he should be able to share the transcript by Thursday afternoon, subject to internal approval. He then went away from 8th July. The case is built so the promised Thursday falls inside the leave. It asks for that conflict to be shown, rather than for the transcript to be called overdue or promised without conditions. This run handled the conditions well, and more than once, but never mentioned Thursday.

The skill's run on the same scenario did raise it, and its review scored evidence fidelity 5 partly for that. So on this one point the shorter file did worse.

**A smaller slip.** The output paraphrases Alex's automatic reply as responding "only if something is urgent". The notice says he'll answer non-urgent messages when he's back. It doesn't change the decision, but it's a misstatement against the "nothing misstated" note above.

**What I can't tell you is why.** The prompt does say "If a task, reminder or date was set before something later changed the picture, say so rather than treating it as current", which covers Alex's Thursday commitment as much as the CRM task. The run applied it to one and not the other. It could be that the wording reads too easily as being about reminders only, or that one run simply missed it. Telling those apart needs another run, and I've run this test once.

## What This Test Cannot Prove

- One run, one fictional scenario, scored by me, and I wrote the prompt. There's no second scorer, and [nobody outside this project has scored anything](../EVIDENCE-STATUS.md).
- It says nothing about whether a second run of the same prompt would miss the same thing, catch it, or miss something else. I've already measured identical prompts on identical inputs moving by [up to three points between runs](repeat-run-findings.md), and a [nine-run test](hartwell-objection-ambiguous-test.md) where the same model named a different primary driver each time.
- **The two-point gap against the skill's 48 isn't evidence the prompt is worse.** It's within the run-to-run movement I've already measured. The named miss above is worth more than the difference in totals.
- The scenario rewards sending nothing. A scenario where chasing is the right call would test the drafting rules, the stage shapes and the anchor rule. This run didn't have to use any of them.

## The Change to Test Next

**I tested the obvious change, and rejected it.** I widened the instruction to name a commitment the prospect made themselves, and [ran the scenario twelve times](chase-stale-date-test.md), six a side, scored without knowing which version each run came from. Four of six runs of the prompt as published named Alex's Thursday commitment. That met the condition I'd set in advance for rejecting the change, and puts the miss above within the prompt's normal variation. I haven't adopted the wider wording.

That test also found something this review got slightly wrong. It says the case is built so the promised Thursday falls inside the leave. The scenario didn't state which weekday 7th July was, so the conflict followed from the dates rather than being stated by them, and three of the twelve runs said so.
