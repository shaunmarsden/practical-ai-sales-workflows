# The Ledger Step Where Nothing Collides: A Twelve-Run Harm Test

Both ledger tests, [on the prompt](chase-dated-commitment-ledger-test.md) and [on the skill](chase-skill-ledger-test.md), left the same gap and named it. Nothing had tested what a step asking for a collision check does when there's no collision to find. That's the case its own "including when nothing collides" clause is for.

**This tests for harm, not improvement.** The question is whether the step makes a run invent a conflict.

## It Needed a New Scenario

I checked every published input first. Only the Hartwell chase scenario has both dates and a stated time when someone is away, and there they overlap by design, so there was nothing to test the step against.

I wrote [Tarnside Freight](../examples/tarnside-chase-input.md) for this and published it with the test. It's the mirror of the existing chase scenario, on purpose. Ruth Alderman promised exception forms by Friday 5th June, and today is Thursday 11th June. She mentioned two times she'd be unavailable: a depot system freeze from 15th to 26th June, and a conference on the 30th and 1st. Both are in the future and cover neither date. **Nothing collides, and saying so is the right answer.**

There's also no stated reason for the silence, the opposite of the Hartwell case, so the right decision changes too.

## The Criterion and the Harm Condition

**The pass mark, fixed before any run.** Does the output claim that a dated commitment falls inside a stated period of unavailability, when the material has no such overlap? Any such claim is a false collision and counts against the version that made it.

**The harm test.** If the ledger version makes a false collision in two or more of six while the version without it makes none, the step causes harm here. Then it gets reworded or removed, not kept, and both earlier pages get a note saying it was adopted on one kind of case only.

**A second measure, recorded but not the pass mark.** Does the output say that nothing collides, which the step asks for in as many words?

## Method

Twelve runs on the Tarnside scenario, with the answer key removed at the line its own warning names. Same model, a fresh isolated context each time, no rubric and no access to this repository. Six used the skill as it stood before the ledger section, and six used it as it stands now. They differ by that section and nothing else. I scored them without knowing which version each run came from.

## Result

| | Runs | False collisions | Stated that nothing collides |
| --- | ---: | ---: | ---: |
| Skill without the step | 6 | **0** | 0 |
| Skill with the step | 6 | **0** | 5 |

**No run in either version invented a collision. The step did no harm here, so I've kept it.**

Three runs without the step and three with it mentioned the freeze when planning when a later chase should land. That uses the dates rather than making a claim about them. None of the twelve said a commitment fell inside a window when it didn't.

On the second measure the step does what it says. Five of six runs with it said in plain words that nothing collides, against none of the six without it. One-tailed p = 0.0076. **The sixth said the same thing in other words**, writing that the freeze "doesn't start until the 15th and the conference isn't until the 30th, neither is active now". So in substance it's six of six, and the wording measure is the strict version.

## The Decision Flipped, and Both Versions Agree

**All twelve runs decided to chase now**, where all 48 runs across the earlier tests on this thread decided to wait. That's the scenario working as designed, not a finding about the step, and I'd written it down in advance as expected.

It's still worth saying: the step didn't distort the decision on a scenario where the right answer is the opposite of the one it was built on.

## The Printing Happened Again

Five of the six ledger runs printed the ledger, as a dated list under its own heading, though the instruction says it's a working step and not part of the finished output. That's the same five of six as the [skill test](chase-skill-ledger-test.md), where the prompt version printed none.

**Two tests now agree that the section form of this instruction gets printed and the paragraph form doesn't.** It's no longer a one-off, so the open question of whether to allow or prevent the printing is worth answering, not just noting.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and a pass mark written and applied by me.
- **It only closes the gap for false alarms**, which is what I said in advance it would do. It says nothing about whether the step wastes a reader's attention, makes the output longer than it should be, or crowds out something else. The pass mark measures none of those.
- I wrote the scenario, and I'm the one testing the step. I built it to have no collision, so it can't show the step is harmless in general, only that it didn't invent one here.
- No output is published with this test, and no run is scored against the rubric. The finding is a count of false collisions. A first worked Tarnside output would be separate work with its own review.

## The Change to Test Next

The next question was whether the ledger should be printed at all. I [tested that next](chase-ledger-printing-test.md) by asking first whether the instruction could be made to hold, not whether the printing is good. It can: zero of six against six of six, with the date clash still stated in every run of both versions, so I've adopted the stronger wording. That doesn't settle whether the shorter output is better. The test puts a number on the trade instead of making the call: the ledger is about 139 words, roughly a quarter of the output.
