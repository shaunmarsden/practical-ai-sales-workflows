# CRM Hygiene Prompt: The Missing-Record Step

## Status

**Twelve runs, six a side, on the pasteable prompt.** The [missing-record step](crm-hygiene-missing-record-finding.md) was added to the skill and deliberately not to the prompt, because that would have been a second untested change. The recipe card therefore carried the older behaviour while the skill did not, which is a difference a reader would meet without being told. This test closes that.

The change is adopted. The prompt now carries the step, and the recipe card was rebuilt from it.

## Why the Prompt Needed Its Own Test

The skill test does not transfer. A skill file is a long instruction sheet with its own guardrail list and stop conditions; the prompt is four hundred words a person pastes into a chat window, structured as a numbered checklist. A step that works in one is not therefore a step that works in the other, and this repository has already found the two artefacts behaving differently on the same scenario.

## What Was Run

The same fictional [contact-level export](../examples/fictional-crm-contact-export.md) the skill test used, carrying eight anomalies, of which two matter here: one row with the full trail an opportunity would normally follow and no opportunity, and one decoy with no opportunity and nothing logged since the enquiry.

Six runs against the prompt extracted unchanged from the published template, and six against the prompt with the step added. Fresh isolated context each time, given only the prompt and the export, told to read nothing else. Criteria, thresholds and the falsification condition were written before either arm ran.

The scratchpad holding the original skill-test input had been reaped by the operating system, so the input was rebuilt from the published example. Its table was verified line by line as identical to the tested one before any run.

## The Result

| Check | Published prompt | Prompt with the step |
| --- | ---: | ---: |
| Flagged the absent opportunity at all | 6 of 6 | 6 of 6 |
| Filed it as an ordinary missing field | 6 of 6 | 0 of 6 |
| Named evidence outside the export before anything is created | 0 of 6 | 6 of 6 |
| Treated the evidenced row and the decoy as different kinds of thing | 2 of 6 | 6 of 6 |
| Wrongly treated the decoy as a record that should exist | 0 of 6 | 0 of 6 |
| Still caught the six ordinary hygiene problems | 6 of 6 | 6 of 6 |

Every published-prompt run put the absent record in the same summary row as the blank owner: "Missing critical fields, 3". The registered thresholds for adoption were separation and outside evidence both at or above five of six, with no regression and no over-firing. All four were met.

## The Prompt Was Worse Than the Skill, Not Equally Bad

**One published-prompt run told the user to create the record.** It wrote that the row was "worth creating the opportunity record rather than treating it as incomplete data". No run of the published skill did that in six runs; they all stopped at flagging. So the prompt did not merely share the skill's blind spot, it went one step further into the failure the guardrail exists to prevent, on the artefact that a reader is most likely to paste without reading the surrounding page.

That is one run of six and not a rate. It is reported because it happened and because it is worse than what the skill arm produced, not because six runs can measure how often it would.

## A Scoring Error Worth Recording

The first pass at scoring the outside-evidence row was done by pattern rather than by reading, and it was wrong in both directions. Two published-prompt runs were marked as naming outside evidence when the only match was the word "calendar" in a note about which date counted as today. One changed-prompt run was marked as not naming it when it had, in different words: "the meeting record, the call and email logs, and whatever process should have created the opportunity". Reading the runs corrected two false positives and one false negative.

The published figures are the ones from reading. This is the seventh time in this repository's testing that a count from a search has been wrong until it was read back, and it is recorded here for the same reason as the other six.

## What This Supports

- The pasteable prompt carried the same blind spot as the skill, and the step transfers to it: none of six filed the absent record as an ordinary missing field, against six of six before.
- The step does not over-fire. No run in either arm treated the unevidenced row as a record that should exist, which was the main risk of teaching a method to look for absences.
- Nothing regressed. All twelve runs still caught the confident duplicate, the near-duplicate that must not be merged on name alone, the blank owner, the stale complete record, the early-stage close date and the demo row.
- The skill and the prompt now behave the same way on this scenario, so the recipe card and the skill no longer disagree.

## What This Does Not Support

- One fictional scenario, one model, six runs a side, built and scored by the same person.
- It does not show the step helps on a real export. The real case that prompted all of this was reconstructed by hand, and no published method has been run against it.
- The create-the-record run is one instance, not a measured rate, and six runs cannot tell whether it would recur.
- Detection is not comparable between the arms, because the changed prompt names the pattern the input contains. Detection was already six of six in the published arm with no hint, so no detection claim rests on the second set.
- It is not an independent external test.

## Next Evidence

The two artefacts now agree, so the useful next test is a harder input rather than another artefact: an export where the trail is genuinely ambiguous rather than clearly strong or clearly absent, since a method that only separates the easy cases has not been tested on the one that matters. After that, a real export with a genuinely missing record, run prospectively so the method is used before the answer is known.
