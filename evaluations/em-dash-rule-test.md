# The Em Dash Rule: A Thirty-Three Run Test

This is the smallest test on this page, on the least interesting defect, and it is worth recording because of what it was costing rather than what it changes about any output.

## The Problem

This repository's [style rule](../guides/writing-style-and-formatting.md) forbids em dashes and a CI check enforces it on every tracked file, published model outputs included. Only four of the seventeen skills told the model not to use them.

So every output from the other thirteen had to be converted by hand before it could be committed. That is where the undisclosed-conversion problem came from: a published record that says "reproduced unedited" after a silent edit is worse than the em dash ever was.

**This is a maintenance and disclosure fix, not an output-quality one.** Nothing about a business case is worse for containing an em dash.

## The Baseline, Which Came Free

Twenty-eight runs of Build a Business Case were made across three earlier tests: six in the [check requirement test](business-case-check-requirement-test.md), sixteen in the [stacked figure test](business-case-stacked-figure-test.md), whose other three runs are the check requirement test's own, and six in its bluntness follow-up. **Every one of the twenty-eight contains em dashes**, between ten and thirty-one each. No control arm was needed.

## The Change

"No em dashes, no emojis" added to the guardrails of every skill that lacked it, thirteen in all, worded to match the four that already had it. In Identify Buyer Indecision it is a numbered, bold-labelled directive rather than a bullet, because that file's list is numbered and bold-labelled.

## The Criterion and the Result

**Fixed before any run:** does the output contain at least one em dash?

Five blind runs of Build a Business Case with the rule added, on the Aldercroft scenario, isolated context and answer key stripped as before.

| | Runs | Contained an em dash |
| --- | ---: | ---: |
| Twenty-eight earlier runs, no rule | 28 | **28** |
| With the rule | 5 | **0** |

Fisher's exact, one-tailed: p = 0.0000042. None of the five contained an en dash either.

**The rule holds.** It is the cheapest change tested here and the most clearly effective.

## Two Things Checked Alongside

**The stacked-figure guardrail still holds with both rules present.** All five runs cited Finance's thirty-five pound rate, one of them in words rather than with a currency symbol, and none combined it with the untimed six-hour estimate. The two instructions do not interfere.

**A check now enforces it**, so a skill added later cannot ship without the rule and quietly reintroduce the hand-conversion problem. It was retro-tested against the state before this change and fires on all thirteen.

## What This Test Cannot Prove

- **One skill was tested and thirteen were changed.** That is extrapolation, and it is a weaker claim than the guardrail's. Twelve of them carry this rule on the strength of a test run on the thirteenth, and the only defence is that the rule is a single unambiguous instruction about a single character rather than a judgement about content.
- One scenario, one model. It says nothing about whether the rule holds on an input where an em dash is genuinely the natural punctuation.
- The twenty-eight baseline runs were not made for this purpose. They are a fair baseline because none of them carried the rule, but they were produced across three different tests with three different versions of the skill file, so they vary in other ways.
- No output is published with this test. The finding is a count of a character, and a sixth Aldercroft business case in `examples/` would be clutter rather than evidence.
