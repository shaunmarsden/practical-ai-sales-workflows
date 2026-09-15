# Does the Hard Count Cause Padding: A Twelve-Run Test

The [applied examples test](business-case-applied-examples-test.md) ended by naming this: the business case prompt makes "Three applied examples" a numbered required part, the skill only ever said three was a good number, and the Aldercroft transcript establishes one manual task in depth. A run producing three grounded examples from it would have to invent two.

**It does not happen, and the test found something worse while looking.**

## The Criterion and the Condition

**The criterion, fixed before any run.** Does the output contain an applied example that is not grounded in a task the transcript establishes? An example counts as ungrounded if it describes work, a saving or a process the transcript does not contain, or if it would read the same in a different prospect's document. That second test is the prompt's own wording and the skill's guardrail, not a standard invented here.

The accounts payable aside was ruled out in advance as a second grounded task: the transcript names it only to exclude it, so building an example on it is inventing detail the call does not supply.

**The falsification condition.** If the prompt as it stands produces no ungrounded example in six runs, the hard count does not cause padding on this scenario and no change is made.

## Method

Twelve blind runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md) with its answer key removed at the line its own warning names, same model, a fresh isolated context each time, no rubric and no access to this repository. Six of the prompt as it stands, six with the count removed and the skill's softer wording in its place. The two inputs differ by that item and nothing else. Scored without knowing which arm each run came from.

## Result

| | Runs | Ungrounded examples | Produced exactly one grounded example |
| --- | ---: | ---: | ---: |
| Prompt with the hard count | 6 | **0** | 6 |
| Prompt with the count removed | 6 | **0** | 6 |

**The falsification condition was met and no change is made.** The hard count does not cause padding on this scenario.

**All twelve went further than not padding.** Every run produced exactly one applied example and said in the document why there were not three, and every one of them correctly excluded the accounts payable aside as a candidate, usually naming Tomasz's request to keep it out. Several listed the minimum detail a second example would need.

So the worry the [prompt review](aldercroft-business-case-prompt-review.md) raised is unfounded here, and what its single run did was not luck: it is what twelve of twelve do.

## What the Runs Did Instead, Which Is Worse

**Nine of the twelve produced a pound figure built from Tomasz's untimed six-hour estimate and Finance's approximate £35 rate.** Seven annualised it, to about £131,000. Two went further and projected roughly £65,000 a year of reclaimed capacity from an untested "half, maybe more".

That is the stacked figure: the defect this repository [tested over nineteen runs](business-case-stacked-figure-test.md), wrote a guardrail for, and records as the lead example of a mistake that reads as sourced fact.

**The guardrail is in the skill and not in the prompt.** The skill produced no combined figure in ten runs carrying it. The prompt, which has no such line, produces one in nine of twelve.

It is balanced across the arms of this test, four of six against five of six, which is what you would expect from something the reworded item has nothing to do with. **This was not the pre-registered criterion. It is an observation made with the outputs open, and it is a count of a defect rather than a comparison, so it needs no arm to be read.**

The prompt is the artefact the [recipe card](../recipes/build-a-business-case.md) carries, so it is the one most likely to be used.

## The Fourth Incomplete Search in Two Days

Scoring the observation about whether runs say why there are not three examples, my first pass marked two of the twelve as not doing so. Both do. One writes "there is not yet enough confirmed detail to add a second or third example without inventing detail that was not established on the call", and my pattern looked for "not enough confirmed detail".

That follows a case-sensitive check that made a file look like it lacked a step, a rename sweep that missed one phrasing, and a clash-statement pattern that missed "fall inside the window". **Four wrong counts, all caught by reading the text, none caught by a better pattern.** The rule this repository already has is the right one and I keep having to apply it: a count from a search is not a finding until it has been read back against what it counted.

## What This Test Cannot Prove

- Six runs an arm, one scenario, one model, and a criterion written and applied by the same person.
- It says nothing about a scenario that genuinely supports three examples, where a hard count would have nothing to strain against and the question would not arise.
- The stacked figure observation is a count on twelve runs of one prompt on one transcript. It is not a comparison and no p value is offered for it.
- It says nothing about whether adding the guardrail to the prompt would work. That is the next test, and this page is its baseline.

## The Change to Test Next

That was [done immediately](business-case-prompt-guardrail-test.md), with a fresh control arm rather than this page's nine of twelve. **The guardrail works on the prompt: none of six against five of six, p of 0.015**, and it is adopted.

It also costs something. No run carrying it gave any aggregate sense of scale, not even the seventy-two analyst-hours a week that the criterion explicitly permits, where four of six without it did. That page records it as the open question.
