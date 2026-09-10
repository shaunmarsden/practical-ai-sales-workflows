# Applied Examples: A Twelve-Run Test That Corrects Its Own Premise

The [stacked figure test](business-case-stacked-figure-test.md) named this as the next question about the Build a Business Case skill. Reading the wording before running anything showed that half the question was my own reporting error, and twelve blind runs then showed the other half is not there either.

## What This Repository Said, and What the Files Say

Two pages here said that the skill and the prompt both ask for three applied examples, and that across six runs the instruction was never followed.

**The prompt does ask for three.** In a numbered list headed "Produce the document with these parts", item three is "Three applied examples".

**The skill does not.** Its bullet says "**Applied examples**: three is a good number", in a list where other items say "always present" and "present, with a real figure". The softer wording is doing deliberate work, and the skill also has a stop condition for when the confirmed detail is too thin to personalise the examples at all.

**All six runs in that earlier test were runs of the skill.** So "an instruction that has never once been followed" was measuring compliance with an instruction that artefact does not contain. The prompt's one run produced a single grounded example and said plainly why the other two were absent, which [its own review](aldercroft-business-case-prompt-review.md) recorded as a strength rather than a failure.

Four pages carried some version of the wrong claim. They are corrected.

## The Gap That Was Actually Left

The earlier counts were one, zero, zero, one, zero and one. **Three of those six runs produced no applied example at all**, on a scenario that establishes one manual task in depth. A business case with no worked example has dropped the part that connects a cost to the work, so that is what this test went after.

## The Change and the Criterion

One line replaced, and nothing else altered:

> **Applied examples**: at least one is required, and one for each distinct manual task the sources establish in enough detail to describe. Three is a good number when the source material supports three. If it supports fewer, produce the ones it supports and say plainly which detail is missing, rather than padding to a number or leaving the section out.

**The criterion, written down before any run:** does the output contain at least one applied example that names the specific manual task the transcript establishes, its cost, what the proposed solution addresses, and what changes as a result? All four, which is what the bullet asks of an example. A cost section stating the six-hour estimate is not an applied example, and a sentence mentioning reconciliation in passing is not one either.

**The falsification condition, also fixed in advance:** if the skill as published produces at least one such example in five or six of its six runs, the earlier three in six was inside its own variation, the change is not needed, and it is not adopted.

**Two contingencies, fixed in advance.** If both arms produce six of six, the criterion was too easy, and no further runs get added to rescue a result. Any example that would read the same in another prospect's document is recorded as padding whether or not it meets the criterion.

## Method

Twelve blind runs on the [Aldercroft transcript](../examples/aldercroft-business-case-transcript.md) with its answer key removed at the line its own warning names, same model, a fresh isolated context each time, no rubric and no access to this repository. Six of the skill as published, six with that one line changed. Every run was made for this test.

**The runs were scored without knowing which arm each came from.** The twelve inputs were copied to neutrally named files under a mapping that was generated and never displayed, and the mapping was opened only after all twelve had been scored. This is new here, and it exists because every earlier comparison on this page was scored by someone who knew which version he was reading. A first attempt printed the mapping, so it was thrown away and regenerated.

## Result

| | Runs | At least one grounded applied example |
| --- | ---: | ---: |
| Skill as published | 6 | **6** |
| Skill with the line | 6 | **6** |

**Twelve of twelve. The falsification condition was met and the change is not adopted.** No Fisher test is offered, because there is nothing to test: both arms passed completely.

**No run produced a second or third example.** Zero padding across twelve runs, which is the one thing the guardrail against generic examples was there to prevent.

## What the Runs Actually Did

Every one built a single example around reconciliation matching: the twelve analysts, the six-hour estimate labelled as Tomasz's own untimed observation, the line-by-line matching as the work the pilot would take over, and the half-or-more reduction as a gut feel formed from a demo. Seven gave it an "Applied example" heading of its own. Five put the same four things under a heading about the manual task instead, which the criterion counts, because the criterion was about content rather than labelling.

The weakest of the twelve against the criterion never states what the proposed solution addresses in its own words, describing the problem, the two cost inputs and the expected reduction instead. It is the run a second scorer is most likely to mark differently, and it turned out to be in the arm carrying the changed line.

## A Post-Hoc Observation With No Claim Attached

Six of the twelve said explicitly why there is only one example, usually naming the accounts payable aside that was ruled out on the call. Split by arm that is four of six with the changed line against two of six without it, one-tailed p of 0.28.

**This was not the criterion, it was noticed afterwards, and six runs a side cannot separate it from nothing.** It is recorded here rather than acted on because the last test on this skill produced a published claim from exactly this kind of cell and had to be corrected. If it is worth testing, it needs its own pre-registration and its own runs.

## Why the Earlier Count Cannot Be Rechecked

The earlier counts were counts of how many of three appeared. On this test's criterion that is three of six, against six of six here.

**That is not a before-and-after comparison and no p value is offered for one.** Five of those six outputs were never published, so whether the three zeros were real cannot now be checked. The skill has also changed since, gaining the stacked figure guardrail, the em dash rule and the human check line, so the two sets of runs were given different files.

What can be checked is that all three published Aldercroft outputs contain an applied example: the [prompt output](../examples/aldercroft-business-case-prompt-output.md) under a heading of its own, the [check requirement output](../examples/aldercroft-business-case-check-requirement-output.md) likewise, and the [guardrail output](../examples/aldercroft-business-case-guardrail-output.md) under headings about the problem and what the pilot would test.

## Two Things the Input Carried, Recorded Before Running

Both arms carried them identically, so neither is a differential confound, and neither mentions applied examples.

- **The skill's own evidence footer** tells the model that the Aldercroft scenario's live traps are an unmeasured time estimate and an unconfirmed future headcount, and describes the stacked figure defect and its guardrail. This is the dual-purpose problem the [stacked figure test](business-case-stacked-figure-test.md) already recorded: documentation written for a human reader reaches the model.
- **The transcript's fictional-disclosure blockquote names those same two traps, and it sits above the re-run line.** Anyone following the instruction to copy everything above that line hands the model part of the answer key. That is a defect in the re-run instruction rather than in the skill, and it affects every earlier test on this transcript. Scoping it properly afterwards found the same thing in fifteen published inputs and six skill footers, all now fixed.

## What This Test Cannot Prove

- One scenario, one model. Aldercroft establishes one manual task in depth, so this says nothing about a source that genuinely supports three examples.
- Twelve runs on a criterion both arms passed completely establishes that the change is unnecessary here. It does not establish that the current wording is the best available.
- Blind scoring removes one bias and leaves the others. I wrote the criterion, wrote the change, and scored every run.
- It says nothing about the prompt, which is the artefact that actually asks for three.

## What Changed

**Nothing in the skill.** "Three is a good number" stays exactly as it is, and the case for changing it rested on a defect that six fresh runs did not reproduce once.

The four pages carrying the wrong claim are corrected in place.

## The Change to Test Next

Whether the prompt's hard "Three applied examples" causes padding on a source that supports one. Its single run did not pad, and one run is not evidence either way. That is a question about the prompt rather than the skill, and it would need the same blind scoring this test used.
