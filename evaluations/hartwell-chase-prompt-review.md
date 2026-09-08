# Hartwell Chase Prompt Review

This review scores the [worked decision](../examples/hartwell-chase-prompt-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests the [chase sequence prompt](../templates/chase-sequence-prompt.md), which is a different artefact from the [Plan a Chase Sequence skill](../.agents/skills/plan-chase-sequence/SKILL.md) scored in the [chase decision review](hartwell-chase-review.md). The prompt is condensed from the skill, so the two are related, but neither score is evidence for the other.

The prompt exists because the [Chase a Quiet Prospect recipe card](../recipes/chase-a-quiet-prospect.md) had nothing to paste. It said everything a reader needed was on the card and then sent them to a skill file that opens by saying it is not written to be read start to finish.

## Method Note

The prompt was pasted into a fresh, isolated context with only the [scenario](../examples/hartwell-chase-input.md) below it, and the scenario's answer key was removed first, as its own warning instructs. The run did not know it was a test, did not see the rubric, and had no access to this repository. The output is reproduced unedited.

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every date, the automatic reply, the CRM task and the conditional transcript approval are represented exactly as supplied, with nothing misstated |
| Evidence fidelity | 4 | The newer automatic reply correctly outweighs the older CRM task, and the transcript stays conditional throughout, but Alex's own Thursday commitment is never mentioned and the case plants a conflict between it and his leave dates |
| Fact separation | 5 | It labels its own sections "Evidenced", "Not evidence of lost interest" and "Unconfirmed", and separates what is known from what is inferred without being asked to use those words |
| Missing information | 4 | Three unknowns are named plus three things to watch for, but the Thursday timing is not among them |
| Commercial usefulness | 5 | It reaches the right decision, gives the reasoning a person can check, and leaves a clear route back into the opportunity |
| Next step clarity | 4 | It gives a revisit window and three concrete preparation items, though the owner is implied rather than stated |
| Tone | 5 | Plain and direct, with no filler and no hedging that obscures the decision |
| Privacy | 5 | Uses only the fictional information supplied and adds no unnecessary personal detail |
| Approval discipline | 4 | Nothing is treated as sent or changed and it writes "No message yet", but it proposes moving the CRM due date without saying in that line that a person must approve it |
| Hallucination risk | 5 | Invents nothing. It refuses to promote Priya from a name mentioned once to a viable route, and labels the revisit date as a plan rather than an agreement |

## What Worked

- It did not obey the stale CRM task. It noticed the task was created before the automatic reply arrived and said the later information supersedes it.
- It separated an out of office notice from a reply awaiting an answer, which is the distinction the prompt's own stop condition depends on.
- It refused to treat Priya as an alternative stakeholder, and said why: she was mentioned but never identified as a route.
- It declined to draft a message at all, which is the harder answer on this scenario, and still produced something useful for later.

## What It Missed

**The Thursday conflict.** Alex said on 7th July that he should be able to share the transcript by Thursday afternoon, subject to internal approval. He then went away from 8th July. The case is built so that the promised Thursday falls inside the leave, and it asks for that conflict to be shown rather than for the transcript to be described as overdue or as unconditionally promised. This run handled the conditionality well and repeatedly, and never mentioned Thursday.

The skill's run on the same scenario did surface it, and its review scored evidence fidelity 5 partly for that. So on this one point the shorter artefact came out worse.

**What I cannot tell you is why.** The prompt does say "If a task, reminder or date was set before something later changed the picture, say so rather than treating it as current", which covers Alex's Thursday commitment as much as it covers the CRM task. The run applied it to one and not the other. Whether the wording is too easily read as being about reminders only, or whether one run simply missed it, needs another run to separate, and this test has been run once.

## What This Test Cannot Prove

- One run, one fictional scenario, scored by the person who wrote the prompt. There is no second scorer, and [nobody outside this project has scored anything](../EVIDENCE-STATUS.md).
- It says nothing about whether a second run of the same prompt would miss the same thing, catch it, or miss something else. This repository has already measured identical prompts on identical inputs moving by [one to three points between runs](repeat-run-findings.md), and a [nine-run test](hartwell-objection-ambiguous-test.md) where the same model named a different primary driver each time.
- **The two point gap against the skill's 48 is not evidence the prompt is worse.** It is inside the run-to-run movement this repository has already measured on its own tests. The named omission above is worth more than the difference in the totals.
- The scenario rewards not sending anything. A scenario where chasing is the right call would test the drafting rules, the stage shapes and the anchor rule, none of which this run had to exercise.

## The Change to Test Next

Widen the stale-date instruction so it names a commitment the prospect made themselves, not only a task or reminder that was set. Then run this scenario again and see whether Thursday appears.
