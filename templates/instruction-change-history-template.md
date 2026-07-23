# Instruction Change and Regression History Template

Use this when a skill's actual instructions change because a test, real or fictional, found something wrong. The point is a repeatable record of why an instruction changed, not just the new version replacing the old one with no trace of what prompted it.

## The Record

| Field | What goes here |
| --- | --- |
| Original instruction version | Quote or link to the exact wording before the change (a specific commit, or the relevant lines) |
| Test case | What was run: a fictional scenario, or an anonymised real one, with a link if one exists |
| Raw outputs | The actual output produced, not a paraphrase of it |
| Rubric scores | Scored against the [sales AI output rubric](../evaluations/sales-ai-output-rubric.md), area by area |
| Observed failure | What specifically went wrong, quoting the problem line rather than describing it in general terms |
| Instruction change | The exact wording added, removed or changed, and why this specific change addresses the specific failure observed |
| Rerun outputs | The output produced after the change, from the same or an equivalent test case |
| Score difference | Before and after, area by area where it moved, not just a new total |
| What improved | Specific and honest, not "it's better now" |
| What did not | At least one thing, if there genuinely is one. If a change fixed everything with no remaining weakness, look again before assuming that is true |

## Regression Checks

Before treating an instruction change as safe to ship, confirm it has not quietly broken a guardrail that already worked. A short, standing list worth checking on every change, not just the one being tested:

- An information request from the other side has not become an agreed meeting
- A second-hand or reported detail is still labelled second-hand, not upgraded to confirmed
- A missing date stays unknown, not filled with a plausible guess
- An unauthorised commitment (a discount, a guarantee, a timeline nobody approved) triggers a stop rather than getting drafted anyway
- A genuine disqualification is not argued with
- No external action (a message sent, a CRM record changed, a meeting booked) is treated as already completed without a person confirming it

A change that fixes the one failure it targeted while breaking one of these is not a net improvement. Check the list every time, not only when something feels risky.

## Why This Exists

A skill's instructions are easy to change and easy to lose track of changing. Without a record like this, "why does the skill say that" has no answer beyond someone's memory of a bad run months ago. This template exists so the reasoning behind an instruction survives longer than the person who wrote it does.
