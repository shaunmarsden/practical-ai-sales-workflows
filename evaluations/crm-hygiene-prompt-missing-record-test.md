# CRM Hygiene Prompt: The Missing-Record Step

## Status

**Twelve runs, six a side, on the pasteable prompt.** I added the [missing-record step](crm-hygiene-missing-record-finding.md) to the skill but not to the prompt, on purpose, because that would have been a second untested change. The recipe card kept the older behaviour while the skill didn't. This test closes that gap.

I've adopted the change. The prompt carries the step, and I rebuilt the recipe card from it.

## Why the Prompt Needed Its Own Test

A skill is a long instruction sheet with its own guardrails and stop conditions. The prompt is 400 words pasted into a chat window as a numbered checklist. A step that works in one needn't work in the other.

## What Was Run

I used the same fictional [contact-level export](../examples/fictional-crm-contact-export.md) as the skill test. It carries eight problems. Two matter here: a row with the full trail an opportunity would normally follow but no opportunity, and a decoy with no opportunity and nothing logged since the enquiry.

Six runs used the prompt exactly as published in the template, and six used it with the step added. Each ran in a fresh context with only the prompt and the export. I wrote down the pass marks and the adoption thresholds before either version ran.

I had to rebuild the original skill-test input from the published example, and checked its table line by line against the tested one. They were identical.

## The Result

| Check | Published prompt | Prompt with the step |
| --- | ---: | ---: |
| Flagged the missing opportunity at all | 6 of 6 | 6 of 6 |
| Filed it as an ordinary missing field | 6 of 6 | 0 of 6 |
| Named evidence outside the export before anything is created | 0 of 6 | 6 of 6 |
| Treated the row with evidence and the decoy as different kinds of thing | 3 of 6 | 6 of 6 |
| Wrongly treated the decoy as a record that should exist | 0 of 6 | 0 of 6 |
| Still caught the six ordinary hygiene problems | 6 of 6 | 6 of 6 |

Every published-prompt run put the missing record in the same summary row as the blank owner: "Missing critical fields, 3".

Telling the two rows apart and naming outside evidence both had to reach five of six, with nothing worse and no false alarms. All four conditions were met.

## The Prompt Was Worse Than the Skill

**One published-prompt run told the user to create the record.** It wrote that the row was "worth creating the opportunity record rather than treating it as incomplete data". No run of the published skill did that in six. So the prompt went one step further into the failure the guardrail exists to prevent, in the file a reader is most likely to paste without reading the page around it. One run of six isn't a rate.

## A Scoring Error

I first scored the outside-evidence row by searching for words rather than reading, and got it wrong both ways. Two published-prompt runs matched only on the word "calendar", in a note about which date counted as today. One changed-prompt run named outside evidence in other words. Reading fixed two false passes and one false fail. The published figures come from reading. Counts from searches have gone wrong before: the [chase ledger test](chase-ledger-printing-test.md) records a third case and the [padding test](business-case-padding-test.md) a fourth.

## What This Supports

- The pasteable prompt had the same blind spot as the skill, and the step carries over to it. The recipe card and the skill now agree.
- The step doesn't fire when it shouldn't. No run in either version treated the row without evidence as a record that should exist, which was the main risk.
- Nothing got worse. All twelve runs still caught the six ordinary problems.

## What This Does Not Support

- One fictional scenario, one model, six runs a side, all built and scored by me. It isn't independent.
- It doesn't show the step helps on a real export. The real case behind all this was rebuilt by hand, and no published method has been run against it.
- You can't compare how often the two versions found the gap, because the changed prompt names the pattern the input contains. The published prompt had already found it six of six with no hint.

## Next Evidence

The useful next test is a harder input: an export where the trail is truly unclear, not clearly strong or clearly absent. Then a real export with a really missing record, run before the answer is known.

## Corrections

An earlier version of this page gave the published prompt 2 of 6 on treating the two rows as different kinds of thing. On a second reading it's 3 of 6. One run wrote of the decoy: "Looks like it never moved past the initial enquiry." The first scoring missed it. The decision to adopt stands.

An earlier version also called the scoring error above the seventh, and referred to six others. Only the two linked above are numbered anywhere in the repository.
