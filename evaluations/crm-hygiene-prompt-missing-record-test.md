# CRM Hygiene Prompt: The Missing-Record Step

## Status

**Twelve runs, six a side, on the pasteable prompt.** I added the [missing-record step](crm-hygiene-missing-record-finding.md) to the skill but not to the prompt, on purpose, because that would have been a second untested change. So the recipe card kept the older behaviour while the skill didn't, and a reader would meet that difference without being told. This test closes that gap.

I've adopted the change. The prompt now carries the step, and I rebuilt the recipe card from it.

## Why the Prompt Needed Its Own Test

The skill test doesn't carry over. A skill file is a long instruction sheet with its own guardrail list and stop conditions. The prompt is 400 words a person pastes into a chat window, set out as a numbered checklist. A step that works in one won't necessarily work in the other, and I've already found the two behaving differently on the same scenario.

## What Was Run

I used the same fictional [contact-level export](../examples/fictional-crm-contact-export.md) as the skill test. It carries eight problems, and two matter here: one row with the full trail an opportunity would normally follow but no opportunity, and one decoy with no opportunity and nothing logged since the enquiry.

Six runs used the prompt exactly as published in the template, and six used the prompt with the step added. Each ran in a fresh isolated context with only the prompt and the export, and was told to read nothing else. I wrote down the pass marks, the thresholds and what would count against the change before either version ran.

The operating system had deleted the scratchpad holding the original skill-test input, so I rebuilt the input from the published example. Before any run, I checked its table line by line against the tested one. They were identical.

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

I'd set the thresholds for adopting the change in advance. Telling the two rows apart and naming outside evidence both had to reach five of six or more, with nothing getting worse and no false alarms. All four were met.

## The Prompt Was Worse Than the Skill, Not Equally Bad

**One published-prompt run told the user to create the record.** It wrote that the row was "worth creating the opportunity record rather than treating it as incomplete data". No run of the published skill did that in six runs. They all stopped at flagging it. So the prompt didn't just share the skill's blind spot. It went one step further into the failure the guardrail exists to prevent, and it did so in the file a reader is most likely to paste without reading the page around it.

That's one run of six, not a rate. I've reported it because it happened and because it's worse than anything the skill runs produced, not because six runs can measure how often it would happen.

## A Scoring Error

I first scored the outside-evidence row by searching for words rather than reading, and got it wrong both ways. I marked two published-prompt runs as naming outside evidence when the only match was the word "calendar", in a note about which date counted as today. I marked one changed-prompt run as not naming it when it had, in other words: "the meeting record, the call and email logs, and whatever process should have created the opportunity". Reading the runs fixed two false passes and one false fail.

The published figures come from reading. Counts from searches have gone wrong before in my testing: the [chase ledger test](chase-ledger-printing-test.md) records a third case and the [padding test](business-case-padding-test.md) a fourth. I've recorded this one for the same reason.

## What This Supports

- The pasteable prompt had the same blind spot as the skill, and the step carries over to it. None of six filed the missing record as an ordinary missing field, against six of six before.
- The step doesn't fire when it shouldn't. No run in either version treated the row without evidence as a record that should exist. That was the main risk of teaching a method to look for things that are missing.
- Nothing got worse. All twelve runs still caught the clear duplicate, the near-duplicate that mustn't be merged on name alone, the blank owner, the stale complete record, the early-stage close date and the demo row.
- The skill and the prompt now behave the same way on this scenario, so the recipe card and the skill agree.

## What This Does Not Support

- One fictional scenario, one model, six runs a side, all built and scored by me.
- It doesn't show the step helps on a real export. The real case behind all this was rebuilt by hand, and no published method has been run against it.
- The create-the-record run is one case, not a measured rate, and six runs can't tell whether it would happen again.
- You can't compare how often the two versions found the gap, because the changed prompt names the pattern the input contains. The published prompt had already found it six of six with no hint, so no claim about finding it rests on the second set.
- It isn't an independent test.

## Next Evidence

The two files now agree, so the useful next test is a harder input, not another file. That means an export where the trail is truly unclear, not clearly strong or clearly absent. A method that only separates the easy cases hasn't been tested on the one that matters. After that, a real export with a record that's really missing, run as it happens so the method is used before the answer is known.

## Corrections

An earlier version of this page gave the published prompt 2 of 6 on treating the two rows as different kinds of thing. On a second reading it's 3 of 6. One run wrote of the decoy: "Looks like it never moved past the initial enquiry." The first scoring missed it. It doesn't change the decision to adopt.

An earlier version also called the scoring error above the seventh, and referred to six others. Only the two linked above are numbered anywhere in the repository, so it couldn't show the rest.
