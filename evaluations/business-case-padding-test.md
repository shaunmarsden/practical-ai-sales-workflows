# Does the Hard Count Cause Padding: A Twelve-Run Test

The [applied examples test](business-case-applied-examples-test.md) ended by naming this worry. The business case prompt makes "Three applied examples" a numbered, required part. The skill only ever said three was a good number. And the Aldercroft transcript covers only one manual task in depth. A run that produced three grounded examples from it would have to invent two.

**That doesn't happen, but the test found something worse along the way.**

## The Criterion and the Condition

**The pass mark, set before any run.** Does the output contain an applied example that isn't grounded in a task the transcript covers? An example counts as ungrounded if it describes work, a saving or a process the transcript doesn't contain, or if it would read the same in another prospect's document. That second test comes from the prompt's own wording and the skill's guardrail. I didn't make it up for this page.

I ruled out the accounts payable remark in advance as a second grounded task. The transcript mentions it only to exclude it, so an example built on it would invent detail the call doesn't give.

**What would prove me wrong.** If the prompt as it stands produces no ungrounded example in six runs, the hard count doesn't cause padding on this scenario, and I change nothing.

## Method

Twelve runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with its answer key removed at the line its own warning names. Same model, a fresh context each time, no rubric and no access to this repository. Six used the prompt as it stands. Six had the count removed and the skill's softer wording in its place. That item was the only difference. I scored them without knowing which version each came from.

## Result

| | Runs | Ungrounded examples | Produced exactly one grounded example |
| --- | ---: | ---: | ---: |
| Prompt with the hard count | 6 | **0** | 6 |
| Prompt with the count removed | 6 | **0** | 6 |

**That's the result I'd said would prove me wrong, so I've changed nothing.** The hard count doesn't cause padding on this scenario.

**All 12 did better than just not padding.** Every run gave one applied example and said in the document why there weren't three. Every one also rightly excluded the accounts payable remark, usually citing Tomasz's request to keep it out. Several listed the least detail a second example would need.

So the worry the [prompt review](aldercroft-business-case-prompt-review.md) raised doesn't hold here, and its single run wasn't luck. It's what 12 of 12 do.

## What the Runs Did Instead, Which Is Worse

**Nine of the 12 produced a pound figure built from Tomasz's untimed six-hour estimate and Finance's rough £35 rate.** Seven turned it into a yearly figure of about £131,000. Two went further and forecast about £65,000 a year of freed-up time from an untested "half, maybe more".

That's the stacked figure. I [tested it over nineteen runs](business-case-stacked-figure-test.md), wrote a guardrail for it, and use it as the main example of a mistake that reads like a sourced fact.

**The guardrail is in the skill, not the prompt.** The skill produced no combined figure in ten runs with the guardrail. The prompt has no such line, and produces one in nine of 12.

It's spread evenly across the two versions in this test, four of six against five of six. You'd expect that from something the reworded item has nothing to do with. **I hadn't planned to measure this. I noticed it with the outputs open, and it's a count of a fault, not a comparison, so it doesn't need two versions to mean something.**

The [recipe card](../recipes/build-a-business-case.md) carries the prompt, so the prompt is the one people are most likely to use.

## The Fourth Incomplete Search in Two Days

When I first scored whether runs say why there aren't three examples, I marked two of the 12 as not saying. Both do. One writes "there is not yet enough confirmed detail to add a second or third example without inventing detail that was not established on the call", and my search looked for "not enough confirmed detail".

Before that came a case-sensitive check that made a file look like it lacked a step, a rename sweep that missed one wording, and a search for clash statements that missed "fall inside the window". **Four wrong counts, all caught by reading the text, none by a better search.** This repository already has the right rule, and I keep having to apply it: a count from a search isn't a finding until I've read it back against what it counted.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the pass mark myself.
- It says nothing about a scenario that does support three examples. There a hard count would have nothing to strain against, and the question wouldn't come up.
- The stacked figure point is a count from 12 runs of one prompt on one transcript. It isn't a comparison, and I don't give a p value for it.
- It says nothing about whether adding the guardrail to the prompt would work. That's the next test, and this page is its starting point.

## The Change to Test Next

I [did that straight away](business-case-prompt-guardrail-test.md), with a fresh control rather than reusing this page's nine of 12. **The guardrail works on the prompt: none of six against five of six, p of 0.015**, and I adopted it.

It also has a cost. No run with the guardrail gave any overall sense of scale, not even the seventy-two analyst-hours a week the pass mark allows. Four of six without it did. That page records it as the open question.
