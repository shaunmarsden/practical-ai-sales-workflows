# Chase Stale-Date Wording: A Twelve-Run Test

The [chase prompt review](hartwell-chase-prompt-review.md) named a change and never made it. This makes it, tests it, and rejects it.

## What Was Being Tested

That review found the run never mentioned Alex's own commitment to share the transcript by Thursday afternoon, a commitment the scenario places against his later leave. The prompt's stale-date line said:

> If a task, reminder or date was set before something later changed the picture, say so rather than treating it as current.

The run applied that to the CRM task and not to Alex's commitment. **The review was explicit that it could not say why:** either the wording reads as being about internally set reminders only, or that one run simply missed it. It named the fix and the re-run, and neither happened until now.

## The Change

One sentence widened, nothing else altered:

> If a task, reminder, date or commitment was set before something later changed the picture, say so rather than treating it as current. That includes a commitment the prospect made themselves, such as a date they offered to send something by, not only a task or reminder set internally.

## The Criterion and the Conditions

**The criterion, written down before any run:** does the output mention Alex's own commitment to share the transcript by Thursday afternoon? It has to refer to that commitment. The word Thursday appearing as a proposed send date for a new message does not count.

**The falsification condition, also fixed in advance:** if the prompt as published mentions the commitment in four or more of its six runs, the wording was not the cause, the original miss was a one-run event, and the change is not adopted.

**Contingencies, fixed in advance:** if both arms came out six of six or zero of six, the criterion could not separate them and no runs would be added to rescue a result. Whether a run also states that the promised Thursday conflicts with the leave was recorded as an observation, not as the criterion.

## Method

Twelve blind runs on the [Hartwell chase scenario](../examples/hartwell-chase-input.md) with its answer key removed at the line its own warning names, same model, a fresh isolated context each time, no rubric and no access to this repository. Six of the prompt as published, six with that one sentence widened. Every run made for this test.

Scored without knowing which arm each run came from, as in the [applied examples test](business-case-applied-examples-test.md): the twelve inputs were copied to neutrally named files under a mapping generated and never displayed, opened only after all twelve had been scored.

## Result

| | Runs | Named Alex's Thursday commitment |
| --- | ---: | ---: |
| Prompt as published | 6 | **4** |
| Prompt with the sentence widened | 6 | **6** |

**The falsification condition was met exactly at its threshold, so the change is not adopted.** Four of six runs of the published prompt named the commitment, which puts the original miss inside the prompt's own variation rather than making it a consequence of the wording.

Fisher's exact on the misses, zero of six against two of six, one-tailed: p = 0.45. There is nothing there, and the falsification condition was written to fire regardless of what the arithmetic said.

**This is the second time a "the wording caused it" hypothesis here has been rejected by running the baseline properly rather than reasoning about the instruction.** The [check requirement test](business-case-check-requirement-test.md) was the first.

## What the Ten Runs Did With It

Every one of the ten treated the commitment as overtaken by the leave rather than as broken or overdue, which is what the scenario's answer key asks for. Two of them made the point sharply: one wrote that treating "he said Thursday" as a missed deadline worth raising would be wrong, and another that the commitment "cannot currently be read as met, broken, or lapsed".

The two runs that missed it, both of the published prompt, did not ignore the transcript. Both raised whether internal approval was ever granted, and both named the CRM task as predating the auto-reply. What neither did was connect Alex's own date to anything.

## The More Interesting Finding, Which Was Not the Criterion

**Three of the twelve runs noticed that the scenario never says which weekday 7th July was**, so they declined to state whether the promised Thursday actually fell inside the leave. One put it as an unknown to confirm rather than assume. A fourth run asserted flatly that the commitment "falls inside that away period".

They are right that it is not stated. The conflict follows from the dates on every reading except 7th July having been a Thursday itself, which the scenario never rules out, so the inference is strong rather than certain. **The answer key claims more than the input establishes**, and it now carries that qualification.

Whether to fix the input instead, by naming the weekday and making the conflict checkable, is a judgement about cost rather than accuracy. It would change published test material that three existing records were scored against, and that would need disclosing on each. It is named at the bottom of this page rather than done here.

## What This Test Cannot Prove

- Six runs an arm. It can reject the hypothesis it was built for, which it did at exactly the threshold set in advance, and it cannot establish a small effect. Four of six against six of six is not a result in the other direction either.
- One scenario, one model, and the criterion written and applied by the same person. Blind scoring removes knowing which arm a run came from; it does not remove that.
- The criterion is about naming the commitment, not about handling it well. All ten that named it handled it the way the answer key asks, but that was an observation made afterwards, not a scored measure.
- One judgement call inside the scoring, recorded because a second scorer could go the other way: one of the two misses does refer to Alex's stated intention to send the transcript, "he said should be able to, subject to internal approval", without ever mentioning the date. Under a criterion about naming the commitment rather than its timing, that run would count as a yes and the published arm would be five of six. The falsification condition fires either way.

## What Changed

**Nothing in the prompt.** The widened sentence is not adopted, and the published wording stays.

The chase input's answer key now says the Thursday conflict follows from the dates rather than being stated outright. The [chase prompt review's](hartwell-chase-prompt-review.md) closing section records that its proposed change was made, tested and rejected.

## The Change to Test Next

Nothing on this thread. The one thing left to decide is not a test: whether to name the weekday in the chase scenario so the conflict is checkable rather than inferable, accepting that three published records were scored against the version without it.
