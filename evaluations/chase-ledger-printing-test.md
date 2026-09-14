# Should the Ledger Be Printed: A Twelve-Run Test

Two tests found five of six runs printing the dated commitment ledger as a list of dates and a collisions section, despite the skill saying "the ledger is a working step, not part of the finished output". Both named the same next question, and both framed it as one about output quality: is the printing a defect or an improvement?

**That was the wrong question to answer first.** An instruction that asserts something and is ignored five times in six is wrong as written whichever way the quality question goes, and the standard here is that an instruction either holds or gets changed. So this tested whether it can be made to hold.

## The Change

The last sentence of the ledger section replaced, nothing else altered.

Before:

> The ledger is a working step, not part of the finished output.

After:

> Do not put the ledger itself in the output. No list of dates, no table, no section headed with a date check or a collision check: the finding belongs in a sentence inside the first section you produce, and the working that produced it stays out.

## The Criterion and Three Ways to Resolve

**The criterion, fixed before any run.** Does the output contain the ledger, meaning a list or table of dates, or a section headed as a date or collision check, as opposed to the finding stated in prose inside another section? A sentence naming two dates while making the point is not the ledger. A bulleted set of dates under its own heading is.

All three resolutions were written down in advance:

- **The wording can fix it**, if the strengthened arm prints in two or fewer of six while the current arm prints in four or more. Adopt it.
- **The wording cannot fix it**, if the strengthened arm still prints in four or more of six. Then stop asserting something that does not hold, and change the instruction to permit the ledger instead.
- **There is nothing to fix**, if the current arm prints in two or fewer of six.

**A veto that could block adoption even on a clean result.** The step exists to get the date clash stated. If the strengthened arm stated it in fewer than four of its six runs, against six of six measured on this scenario in the [skill test](chase-skill-ledger-test.md), tightening would have cost the behaviour the step was added for.

## Method

Twelve blind runs on the current Hartwell chase scenario, answer key removed at the line its own warning names, same model, a fresh isolated context each time, no rubric and no access to this repository. Six of the skill as it then stood, six with that sentence replaced. The two inputs differ by that sentence and nothing else. Scored without knowing which arm each run came from.

## Result

| | Runs | Printed the ledger | Stated the date clash | Median length |
| --- | ---: | ---: | ---: | ---: |
| Current wording | 6 | **6** | 6 | 726 words |
| Strengthened wording | 6 | **0** | 6 | 587 words |

**Complete separation, p = 0.0011. The first resolution fires and the strengthened wording is adopted.**

**The veto did not fire.** Every run in both arms stated the clash, so suppressing the printing cost nothing on the measure the step exists for. All six strengthened runs made the point in the first paragraph of their opening section, which is where the instruction now says it belongs.

## What Adoption Does and Does Not Settle

This makes the instruction honest. It does not show the output is better.

**What it does buy is a number for the argument.** The ledger costs about 139 words, a quarter of the output, and what it gives a reader is a visible audit trail of the date check. Nobody had measured that before, and the whole question had been carried as an unquantified worry about clutter across two test pages.

A reader who would rather see the working can now make that trade knowing its size. **The instruction is changed because it was asserting something untrue, not because the shorter output has been shown to be the better one.**

## Scope

**The prompt is not changed.** Its paragraph form of the same instruction produced no printed ledger in any of the twelve runs of the [prompt test](chase-dated-commitment-ledger-test.md), so there is nothing there to fix, and changing an artefact whose behaviour has not been measured with the new wording is the mistake the [em dash rule test](em-dash-rule-test.md) names about itself.

## A Mistake I Made While Scoring This

My first pass scored one of the twelve as not stating the clash. It does, in its opening paragraph: "Alex's own commitment ... and the CRM task chasing him for it both fall inside the window he later confirmed he'd be away."

The search pattern looked for "falls inside" and "inside his away period" and missed "fall inside the window". **That is the third incomplete search in a day**, after a case-sensitive check that made a file look like it lacked the ledger step, and a rename sweep that missed the phrase "the published arm". Every one of them would have put a wrong count on a page. The fix is not a better pattern; it is that a count from a search gets read back against the text before it goes anywhere.

## What This Test Cannot Prove

- Six runs an arm, one scenario, one model, and a criterion written and applied by the same person.
- It settles whether the printing can be suppressed, not whether it should be. The 139 words are a measurement of the cost, not a judgement about it.
- The length figure is a median of six outputs on one scenario. It says the ledger is roughly a quarter of this output, not that it is a quarter of any output.
- The current arm printed six of six here against five of six in each of the two earlier tests. Consistent, and all three are single measurements of a small cell.

## The Change to Test Next

Nothing on this thread. Across six tests and seventy-two runs the step is adopted on both artefacts, tested for harm on a scenario with nothing to find, and its instruction now holds. The open questions left are about other jobs.
