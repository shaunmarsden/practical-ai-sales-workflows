# The Em Dash Rule: A Thirty-Three Run Test

This is the smallest test here, on the least interesting fault. It's worth recording for what the fault was costing, not for what it changes in any output.

## The Problem

This repository's [style rule](../guides/writing-style-and-formatting.md) bans em dashes, and a CI check enforces that on every tracked file, published model outputs included. Only four of the seventeen skills told the model not to use them.

So I had to convert every output from the other thirteen by hand before I could commit it. That's how the undisclosed-conversion problem started. A published record that says "reproduced unedited" after a silent edit is worse than any em dash.

**This fixes upkeep and disclosure, not output quality.** A business case is no worse for containing an em dash.

## The Baseline, Which Came Free

Three earlier tests had already produced 28 runs of Build a Business Case. Six came from the [check requirement test](business-case-check-requirement-test.md). Sixteen came from the [stacked figure test](business-case-stacked-figure-test.md), whose other three runs are the check requirement test's own. Six came from its follow-up on whether the guardrail was too blunt. **All 28 contain em dashes**, between ten and 31 each. I didn't need a control.

## The Change

I added "No em dashes, no emojis" to the guardrails of every skill that lacked it, 13 in all, worded to match the four that already had it. In Identify Buyer Indecision it's a numbered, bold-labelled instruction rather than a bullet, because that file's list is numbered and bold-labelled.

## The Criterion and the Result

**Set before any run:** does the output contain at least one em dash?

Five runs of Build a Business Case with the rule added, on the Aldercroft scenario, each in a fresh context with the answer key removed as before.

| | Runs | Contained an em dash |
| --- | ---: | ---: |
| Twenty-eight earlier runs, no rule | 28 | **28** |
| With the rule | 5 | **0** |

A one-tailed Fisher's exact test gives p = 0.0000042. None of the five contained an en dash either.

**The rule works.** It's the cheapest change I've tested here and the most clearly effective.

## Two Things Checked Alongside

**The stacked-figure guardrail still works with both rules in place.** All five runs cited Finance's £35 rate, one of them in words rather than with a £ sign, and none combined it with the untimed six-hour estimate. The two instructions don't interfere.

**A check now enforces the rule**, so a skill added later can't ship without it and quietly bring back the hand-conversion problem. I tested the check against the files as they were before this change, and it fires on all 13.

## What This Test Cannot Prove

- **I tested one skill and changed 13.** That's extrapolation, and a weaker claim than the guardrail's. Twelve of them carry this rule because of a test on the thirteenth. My only defence is that the rule is one clear instruction about one character, not a judgement about content.
- One scenario, one model. It says nothing about whether the rule holds on an input where an em dash really is the natural punctuation.
- I didn't make the 28 baseline runs for this purpose. They're a fair baseline because none had the rule, but they came from three tests with three versions of the skill file, so they differ in other ways.
- I haven't published an output with this test. The finding is a count of one character, and a sixth Aldercroft business case in `examples/` would be clutter, not evidence.
