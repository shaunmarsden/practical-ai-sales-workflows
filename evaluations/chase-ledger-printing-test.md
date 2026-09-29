# Should the Ledger Be Printed: A Twelve-Run Test

Two tests found five of six runs printing the dated commitment ledger as a list of dates and a collisions section. The skill said "the ledger is a working step, not part of the finished output". Both tests named the same next question, and both saw it as one about quality: is the printing a defect or an improvement?

**That was the wrong question to answer first.** An instruction that's ignored five times in six is wrong as written, whichever way the quality question goes. An instruction here either holds or gets changed. So I tested whether it can be made to hold.

## The Change

I replaced the last sentence of the ledger section and changed nothing else.

Before:

> The ledger is a working step, not part of the finished output.

After:

> Do not put the ledger itself in the output. No list of dates, no table, no section headed with a date check or a collision check: the finding belongs in a sentence inside the first section you produce, and the working that produced it stays out.

## What I Decided in Advance

Before any run, I wrote down the test. Does the output contain the ledger, meaning a list or table of dates, or a section headed as a date or collision check? The alternative is the finding stated in prose inside another section. A sentence naming two dates while making the point isn't the ledger. A bulleted set of dates under its own heading is.

I wrote down all three possible outcomes in advance:

- The wording can fix it, if the stronger version prints in two or fewer of six while the current version prints in four or more. Then I adopt it.
- The wording can't fix it, if the stronger version still prints in four or more of six. Then I stop claiming something that doesn't hold, and change the instruction to allow the ledger.
- There's nothing to fix, if the current version prints in two or fewer of six.

I also set one rule that could block adoption even on a clean result. The step exists to get the date clash stated. If the stronger version stated it in fewer than four of its six runs, against six of six on this scenario in the [skill test](chase-skill-ledger-test.md), tightening would have cost the very behaviour the step was added for.

## Method

I made 12 runs on the current Hartwell chase scenario, with the answer key removed at the line its own warning names. I used the same model and a fresh context each time, with no rubric and no access to this repository. Six used the skill as it then stood, and six had that sentence replaced. The two inputs differ by that sentence and nothing else. I scored them without knowing which version each came from.

## Result

| | Runs | Printed the ledger | Stated the date clash | Median length |
| --- | ---: | ---: | ---: | ---: |
| Current wording | 6 | **6** | 6 | 726 words |
| Strengthened wording | 6 | **0** | 6 | 587 words |

**Complete separation, p = 0.0011. The wording can fix it, so I adopted the stronger version.**

**It didn't cost the behaviour.** Every run in both versions stated the clash. All six stronger runs made the point in the first paragraph of their opening section, which is where the instruction now says it belongs.

## What This Settles and What It Doesn't

This makes the instruction true. It doesn't show the output is better.

**What it does give is a number.** The ledger costs about 139 words, a quarter of the output. In return a reader sees the date check being done. Nobody had measured that before. Across two test pages it had been a vague worry about clutter.

A reader who'd rather see the working can now make that trade knowing its size. **I changed the instruction because it claimed something untrue, not because the shorter output is shown to be better.**

## Scope

**The prompt isn't changed.** Its paragraph version of the same instruction produced no printed ledger in any of the 12 runs of the [prompt test](chase-dated-commitment-ledger-test.md), so there's nothing to fix. Changing a file whose behaviour with the new wording hasn't been measured is the mistake the [em dash rule test](em-dash-rule-test.md) admits to.

## A Mistake I Made While Scoring This

My first pass scored one of the 12 as not stating the clash. It does, in its opening paragraph: "Alex's own commitment ... and the CRM task chasing him for it both fall inside the window he later confirmed he'd be away."

My search looked for "falls inside" and "inside his away period" and missed "fall inside the window". **That was my third incomplete search in a day.** The first was a case-sensitive check that made a file look as if it lacked the ledger step. The second was a rename sweep that missed the phrase "the published arm". Each would have put a wrong count on a page. A better pattern isn't the fix. The fix is to read any count from a search back against the text before it goes anywhere.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the test myself.
- It settles whether the printing can be stopped, not whether it should be. The 139 words measure the cost. They don't judge it.
- The length figure is a median of six outputs on one scenario. It says the ledger is roughly a quarter of this output, not of any output.
- The current version printed six of six here, against five of six in each of the two earlier tests. That's consistent, but all three are single measurements of a small group.

## The Change to Test Next

Nothing on this thread. Across six tests and 72 runs, I've adopted the step on both the prompt and the skill, tested it for harm on a scenario with nothing to find, and its instruction now holds. The open questions left are about other jobs.
