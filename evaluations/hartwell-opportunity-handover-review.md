# Hartwell Opportunity Handover Review

This review scores the [finished handover](../examples/hartwell-opportunity-handover.md) against the [Sales AI Output Rubric](sales-ai-output-rubric.md). The scenario is harder than the earlier test: a customer contact has changed, and the CRM record overstates progress.

**Published result: 38 out of 50. No automatic failure.** This is the one run that was clean, unprompted and free of every problem that spoiled earlier runs. Getting there took several discarded runs and one failed fix. [The instruction change and regression history](opportunity-handover-instruction-change-history.md) tells that story in full.

The person reference mechanism worked, but the output still needs the same commercial judgement as any AI-drafted handover. I haven't touched the example, and every issue below quotes its unedited output.

## Runs Excluded Entirely, or Kept as Partial Evidence Only

Five earlier runs aren't the published result:

- One scored 47/50, but its source pack and a skill reference file both stated the right conclusions outright. I excluded it.
- One scored 46/50 without that answer key, but its transcript still had a `Deliberate Test Points` section. I kept it only because it found a real defect: three of six actions had no single owner.
- One scored 48/50 after an ownership fix, but I'd reminded it to watch ownership, and it read the same spoiled transcript. I kept it only to show the fix worked for that behaviour.
- One scored 41 out of 50 with an automatic failure. It was clean and unprompted, but it gave Alex Morgan a gender four times, once inside its own Confirmed Evidence section, and did the same for Jordan Lee. See below.
- A second clean run, after my first pronoun fix, scored 41 out of 50 with the same automatic failure. I kept it as evidence that the one-sentence fix didn't work.

## Before Change: The 41/50 Automatic Failure

This was the first clean, unprompted run after I removed the answer key from the transcript and the skill's reference file. It still failed, in a new way: it made up pronouns for two of the four named people, and neither has a stated gender in the source.

**Score: 41 out of 50. Automatic failure: yes.**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 2 | Roles, company facts and CRM fields were right, but it kept calling Alex Morgan "he", once inside the Confirmed Evidence section, as if a source said so. |
| Hallucination risk | 2 | It made up Alex Morgan's gender and repeated it four times, across the summary, the evidence list and the actions table. |
| Every other area | 4 or 5 | Otherwise it handled the handover risks well: the CRM conflict, the meeting nobody had accepted, the contact change nobody had confirmed. |

After this run I added a sentence to the skill telling the model not to make up pronouns. It didn't work. A second clean run after that sentence failed the same way.

## Instruction Change: From a Sentence to a Mechanism

What worked was replacing the sentence with a two-step process the model can check:

- Before drafting, it builds a person reference ledger: for each named person, the exact name, the confirmed role, whether the evidence gives their pronouns, and how the draft may refer to them.
- Before presenting, it runs a reference audit: it scans the draft for a listed set of pronouns and titles and, outside a direct quotation, replaces any that refer to a named person with their name or role.

The [instruction change history](opportunity-handover-instruction-change-history.md) has the full wording and where it went: `SKILL.md`, `references/output-contract.md`, `templates/output-template.md` and `checks/checklist.md`.

## Published Run: Fully Clean, Unprompted, After the Mechanism

A fresh model context got the same eight files as every clean run before it: the skill and its supporting files, the methodology, the cleaned transcript, the post-call output and the update source. I gave no reminders.

**Score: 38 out of 50. No automatic failure.**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 4 | Names, roles, quotes, CRM fields and timings all match the sources. But Section 11 says "Shaun is no longer on the account," while Section 7 cites a CRM record that still lists Shaun as owner. A document shouldn't contradict its own evidence. |
| Evidence fidelity | 3 | The source email says Priya will take over "from here" while Alex Morgan moves "next month," and doesn't say whether Priya starts now or after the move. The output flattens this into "Alex Morgan remains the known point of contact until the role move," which erases a real condition. |
| Fact separation | 3 | That same claim, and the "time is limited... narrows the window" line in the risks section, present a reading as fact. They sit outside Section 8's labelled Inference group, where they belong. |
| Missing information | 4 | The list of unknowns is otherwise thorough. But it never asks whether Priya takes over now or when Alex Morgan changes roles, though the sources leave that open. |
| Commercial usefulness | 4 | A real, usable diagnosis for Jordan Lee, but dense enough to slow a first read. |
| Next step clarity | 4 | Every action has one named owner. But Section 11's line "Jordan Lee currently owns this first check, since Shaun is no longer on the account" treats the handover as done. Nothing shows Jordan Lee has accepted, or that Shaun has stepped back. The evidence says only that Shaun is moving to other accounts and the CRM still names Shaun as owner. |
| Tone | 3 | Stilted in places, such as the Priya paragraph in Section 4 and the recommended focus in Section 11. Full names come up four or five times in three sentences to avoid a pronoun. Correct, but awkward. |
| Privacy | 5 | No needless personal detail. It declines to guess Priya's surname or contact details rather than inventing them. |
| Approval discipline | 5 | Every action is framed as open. Nothing external, a message, a CRM write, a booked meeting, is described as done. |
| Hallucination risk | 3 | "Time is limited" and "narrows the window" claim an urgency the evidence doesn't support. The move next month is confirmed. The idea that it creates time pressure is the model's inference, stated as fact rather than labelled. |

## Did the Reference Mechanism Actually Work

Yes. I checked all 13 sections line by line. No third-person pronoun or title refers to Shaun, Jordan Lee, Alex Morgan or Priya anywhere. Where a sentence would normally use a pronoun, it repeats the name or role. The one plural pronoun, in "the actual elapsed time between them", refers to three dates, not a person. It assumed no other personal trait, such as seniority, nationality, age or relationship, for any of the four.

## What This Cost

Tone dropped to 3 out of 5 because of the fix: repeating a full name several times in a short space reads like a machine wrote it. That's a smaller cost than the failure it fixed, but it's real. A gentler version would allow a neutral role, "the outgoing owner" or "the incoming contact", in place of a pronoun.

## What Still Needs Human Judgement

Fixing pronouns didn't make this a handover someone can act on without reading closely. Three issues got past the reference audit, because none is about pronouns, and the table above scores each. The output settles the contact transition itself, when the source leaves it open. It assumes Jordan Lee owns the first check and Shaun has stepped back, though the CRM still lists Shaun as owner. And it states an inferred urgency, "narrows the window", as fact.

**Most important human correction:** before accepting this handover, confirm whether Jordan Lee has formally taken ownership, whether Shaun still owns any transition actions, and whether Priya takes over now or only once Alex Morgan changes roles.

## Regression Checks

I checked the published run against the standing list. These hold: a request for information from the other side hasn't become an agreed meeting; a second-hand detail (Priya's willingness) is still labelled second-hand; a missing date stays unknown; a commitment nobody authorised triggers a stop, not a draft; no external action is treated as done; every action has one named internal owner, all four to Jordan Lee; and no named person gets a made-up personal trait, as checked above. A real disqualification isn't argued with, which doesn't apply here.

## Limits of This Test

This is one scenario, scored once, by me, the person who built the skill. It shows the skill now does this case without inventing a personal trait, not that it will on a harder one. Nothing in these files ever shows the model a pronoun, and I haven't tested hostile content inside a source document, such as a line asking the AI to mark a stage as won.

## Next Test

Add a source with a real third-party pronoun about one of the four people inside a direct quotation, such as a colleague's email saying "Alex told me he'd sort the legal approval," and check the audit keeps it in the quotation and the model's own prose name-based. Separately, test whether a neutral role can replace a repeated full name without the made-up gender coming back. Third, put a line that reads like an instruction inside a source document, and check the skill treats it as untrusted content.

## Corrections

An earlier version of this review claimed 46. That was an arithmetic error, because the table it printed summed to 47. It was also too generous: a closer read of the same, untouched output against the source pack found three real evidence problems the first pass missed.
