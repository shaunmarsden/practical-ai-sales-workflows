# The Ledger Step Where Nothing Collides: A Twelve-Run Harm Test

Both ledger tests, [on the prompt](chase-dated-commitment-ledger-test.md) and [on the skill](chase-skill-ledger-test.md), left the same gap open and named it: nothing had tested what a step asking for a collision check does when there is no collision to find. That is the case its own "including when nothing collides" clause exists for.

**This is a harm test rather than an improvement test.** The question is whether the step makes a run invent a conflict.

## It Needed a New Scenario

Every published input here was checked first. Only the Hartwell chase scenario has both dates and a stated period of unavailability, and there they overlap by construction, so there was nothing to test the step against.

[Tarnside Freight](../examples/tarnside-chase-input.md) was written for this and is published with it. It is deliberately the mirror of the existing chase scenario: Ruth Alderman promised exception forms by Friday 5th June, today is Thursday 11th June, and the two unavailability windows she mentioned, a depot system freeze from 15th to 26th June and a conference on the 30th and 1st, are both in the future and cover neither date. **Nothing collides, and saying so is the correct answer.**

There is also no stated reason for the silence, which is the opposite of the Hartwell case, so the correct decision changes too.

## The Criterion and the Harm Condition

**The criterion, fixed before any run.** Does the output assert that a dated commitment falls inside a stated period of unavailability, when no such overlap exists in the material? Any such assertion is a false collision and counts against the arm that produced it.

**The harm condition.** If the ledger arm produces a false collision in two or more of six while the arm without it produces none, the step causes harm here, and it gets reworded or reverted rather than kept, with both earlier pages annotated to say it was adopted on one case shape only.

**A secondary measure, recorded and not the criterion.** Does the output state that nothing collides, which the step asks for in as many words?

## Method

Twelve blind runs on the Tarnside scenario, answer key removed at the line its own warning names, same model, a fresh isolated context each time, no rubric and no access to this repository. Six of the skill as it stood before the ledger section and six as it stands now, differing by that section and nothing else. Scored without knowing which arm each run came from.

## Result

| | Runs | False collisions | Stated that nothing collides |
| --- | ---: | ---: | ---: |
| Skill without the step | 6 | **0** | 0 |
| Skill with the ledger step | 6 | **0** | 5 |

**No run in either arm invented a collision. The harm condition did not fire, and the step is kept.**

Three runs without the step and three with it referred to the freeze while planning when a later chase should land, which is a use of the dates rather than a claim about them. None of the twelve said a commitment fell inside a window that it did not.

On the secondary measure the step does what it says: five of six runs carrying it stated in plain words that nothing collides, against none of the six without it. One-tailed p = 0.0076. **The sixth conveyed the same thing in different words**, writing that the freeze "doesn't start until the 15th and the conference isn't until the 30th, neither is active now", so in substance it is six of six and the wording measure is the strict version.

## The Decision Flipped, and Both Arms Agree

**All twelve runs decided to chase now**, where all forty-eight runs across the earlier tests on this thread decided to wait. That is the scenario working as designed rather than a finding about the step, and it was written into the pre-registration as expected.

It is worth stating anyway: the step did not distort the decision on a scenario where the right answer is the opposite of the one it was developed on.

## The Printing Behaviour Replicated

Five of the six ledger runs printed the ledger, as a dated list under its own heading, despite the instruction saying it is a working step and not part of the finished output. That is the same five of six as the [skill test](chase-skill-ledger-test.md), where the prompt version produced none.

**Two tests now agree that the section form of this instruction gets printed and the paragraph form does not.** That is no longer a one-off observation, and it makes the open question about whether to permit or prevent the printing worth answering rather than noting.

## What This Test Cannot Prove

- Six runs an arm, one scenario, one model, and a criterion written and applied by the same person.
- **It closes the gap for false positives only**, which is exactly what the pre-registration said it would do. It says nothing about whether the step wastes a reader's attention, lengthens the output unhelpfully, or crowds out something else, none of which this criterion measures.
- The scenario is new and was written by the person testing the step. It was built to have no collision, so it cannot be used to argue that the step is harmless in general, only that it did not manufacture one here.
- No output is published with this test and no run is scored against the rubric. The finding is a count of false collisions, and a first worked Tarnside output would be a separate piece of work with its own review.

## The Change to Test Next

Whether the ledger should be printed. Two tests now show that it is, five of six times, against an instruction saying it should not be, and the honest position is that nobody has decided whether that is a defect or an improvement. That needs a criterion about the output a person has to read, which is a different kind of measure from anything on this thread so far.
