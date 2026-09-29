# Applied Examples: A Twelve-Run Test That Corrects Its Own Premise

The [stacked figure test](business-case-stacked-figure-test.md) named this as the next question about the Build a Business Case skill. Reading the wording before running anything showed that half the question was my own reporting error. Twelve runs, scored without knowing which version was which, then showed the other half isn't there either.

## What This Repository Said, and What the Files Say

Two pages here said the skill and the prompt both ask for three applied examples, and that across six runs the instruction was never followed.

The prompt does ask for three. In a numbered list headed "Produce the document with these parts", item three is "Three applied examples".

The skill doesn't. Its bullet says "**Applied examples**: three is a good number", in a list where other items say "always present" and "present, with a real figure". The softer wording is deliberate. The skill also has a stop condition for when the confirmed detail is too thin to tailor the examples at all.

All six runs in that earlier test were runs of the skill. So "an instruction that has never once been followed" was measuring whether the skill obeyed an instruction it doesn't contain. The prompt's one run produced a single grounded example and said plainly why the other two were missing. [Its own review](aldercroft-business-case-prompt-review.md) recorded that as a strength, not a failure.

Four pages carried some version of the wrong claim. I've corrected them.

## The Gap That Was Left

The earlier counts were one, zero, zero, one, zero and one. **Three of those six runs produced no applied example at all**, on a scenario that sets out one manual task in depth. A business case with no worked example has dropped the part that links a cost to the work, so that's what this test went after.

## The Change and the Criterion

I replaced one line and changed nothing else:

> **Applied examples**: at least one is required, and one for each distinct manual task the sources establish in enough detail to describe. Three is a good number when the source material supports three. If it supports fewer, produce the ones it supports and say plainly which detail is missing, rather than padding to a number or leaving the section out.

The pass mark, written down before any run: does the output contain at least one applied example that names the specific manual task the transcript sets out, its cost, what the proposed solution addresses, and what changes as a result? It needs all four, because that's what the bullet asks of an example. A cost section giving the six-hour estimate isn't an applied example. Nor is a sentence that mentions reconciliation in passing.

What would count against the change, also fixed in advance: if the published skill produces at least one such example in five or six of its six runs, the earlier three in six was normal variation. Then the change isn't needed, and I don't adopt it.

Two more rules, fixed in advance. If both versions score six of six, the pass mark was too easy, and I add no runs to rescue a result. Any example that would read the same in another prospect's document counts as padding, whether or not it meets the pass mark.

## Method

Twelve runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md), with its answer key removed at the line its own warning names. Same model, a fresh isolated context each time, no rubric and no access to this repository. Six used the skill as published, and six had that one line changed. I made every run for this test.

I scored the runs without knowing which version each came from. I copied the twelve inputs to neutrally named files under a mapping that was generated but never displayed, and opened the mapping only after scoring all twelve. This is new here. I scored every earlier comparison on this page knowing which version I was reading. A first attempt printed the mapping, so I threw it away and made a new one.

## Result

| | Runs | At least one grounded applied example |
| --- | ---: | ---: |
| Skill as published | 6 | **6** |
| Skill with the line | 6 | **6** |

**12 of 12. The published skill passed often enough that the change isn't needed, so I'm not adopting it.** There's no significance test to run, because both versions passed completely.

No run produced a second or third example. There was no padding in any of the 12, and padding is the one thing the guardrail against generic examples was there to prevent.

## What the Runs Did

Every run built a single example around reconciliation matching: the 12 analysts, the six-hour estimate labelled as Tomasz's own untimed observation, the line-by-line matching as the work the pilot would take over, and the reduction of half or more as a gut feel formed from a demo. Seven gave it its own "Applied example" heading. Five put the same four things under a heading about the manual task instead. The pass mark counts those, because it was about content, not labels.

The weakest of the twelve never says in its own words what the proposed solution addresses. It describes the problem, the two cost inputs and the expected reduction instead. It's the run a second scorer would most likely mark differently, and it turned out to use the changed line.

## Something I Noticed Afterwards, With No Claim Attached

Six of the 12 said why there's only one example, usually naming the accounts payable aside that was ruled out on the call. By version, that's four of six with the changed line and two of six without it, a one-tailed p of 0.28.

**This wasn't the pass mark, I noticed it afterwards, and six runs a side can't tell it from chance.** I've recorded it rather than acted on it, because the last test on this skill turned exactly this kind of cell into a published claim that later had to be corrected. If it's worth testing, it needs its own pass mark decided in advance, and its own runs.

## Why the Earlier Count Cannot Be Rechecked

The earlier counts were of how many of three appeared. On this test's pass mark, that's three of six, against six of six here.

**That isn't a before-and-after comparison, and I offer no p value for one.** Five of those six outputs were never published, so I can't now check whether the three zeros were real. The skill has also changed since, gaining the stacked figure guardrail, the em dash rule and the human check line, so the two sets of runs read different files.

What I can check is that all three published Aldercroft outputs contain an applied example: the [prompt output](../examples/aldercroft-business-case-prompt-output.md) under its own heading, the [check requirement output](../examples/aldercroft-business-case-check-requirement-output.md) too, and the [guardrail output](../examples/aldercroft-business-case-guardrail-output.md) under headings about the problem and what the pilot would test.

## Two Things the Input Carried, Recorded Before Running

Both versions carried them the same way, so neither can explain a difference between them, and neither mentions applied examples.

- The skill's own evidence footer tells the model that the Aldercroft scenario's live traps are an unmeasured time estimate and an unconfirmed future headcount, and describes the stacked figure defect and its guardrail. The [stacked figure test](business-case-stacked-figure-test.md) already recorded this problem: notes written for a human reader reach the model.
- The fictional-disclosure blockquote in the transcript names the same two traps, and it sits above the re-run line. Anyone who copies everything above that line, as told, hands the model part of the answer key. That's a fault in the re-run instruction, not the skill, and it affects every earlier test on this transcript. When I checked properly afterwards, I found the same thing in 15 published inputs and six skill footers. All are now fixed.

## What This Test Cannot Prove

- One scenario, one model. Aldercroft sets out one manual task in depth, so this says nothing about a source that really supports three examples.
- Twelve runs on a pass mark both versions passed completely show the change isn't needed here. They don't show the current wording is the best there is.
- Scoring without knowing the version removes one bias and leaves the others. I wrote the pass mark, wrote the change and scored every run.
- It says nothing about the prompt, which is the file that asks for three.

## What Changed

**Nothing in the skill.** "Three is a good number" stays as it is. The case for changing it rested on a fault that six fresh runs didn't reproduce once.

I've corrected the four pages that carried the wrong claim.

## The Change to Test Next

The next question was whether the prompt's firm "Three applied examples" causes padding on a source that supports only one. I [tested that over 12 runs](business-case-padding-test.md), and it doesn't. No run in either version produced an ungrounded example, and all 12 produced exactly one and said why there weren't three.

That test found something else along the way. **Nine of its 12 runs produced the stacked figure**, the fault the guardrail was written for, because the guardrail is in the skill but not the prompt. Adding it to the prompt is now the next change to test, starting from nine of 12.
