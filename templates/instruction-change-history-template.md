# Instruction Change and Regression History Template

Use this when a test, real or fictional, finds something wrong and you change a skill's instructions. It records why each instruction changed, so the new version doesn't replace the old one with no trace of the reason.

## The Record

| Field | What goes here |
| --- | --- |
| Original instruction version | Quote or link to the exact wording before the change (a specific commit, or the relevant lines) |
| Test case | What you ran: a fictional scenario, or an anonymised real one, with a link if there is one |
| Raw outputs | The output itself, not a paraphrase of it |
| Rubric scores | Scored against the [sales AI output rubric](../evaluations/sales-ai-output-rubric.md), area by area |
| Observed failure | What went wrong, quoting the problem line rather than describing it in general terms |
| Instruction change | The exact wording added, removed or changed, and why this change fixes that failure |
| Rerun outputs | The output after the change, from the same or an equivalent test case |
| Score difference | Before and after, area by area where it moved, not just a new total |
| What improved | Specific and honest, not "it's better now" |
| What did not | At least one thing, if there is one. If a change seems to have fixed everything, look again before you believe it |

## Regression Checks

Before you treat a change as safe to ship, check it hasn't broken a guardrail that already worked. Check these on every change, not just the one you're testing:

- An information request from the other side has not become an agreed meeting
- A second-hand or reported detail is still labelled second-hand, not upgraded to confirmed
- A missing date stays unknown, not filled with a plausible guess
- An unauthorised commitment (a discount, a guarantee, a timeline nobody approved) triggers a stop rather than getting drafted anyway
- A real disqualification is accepted, not argued with
- No external action (a message sent, a CRM record changed, a meeting booked) is treated as already completed without a person confirming it

A change that fixes its target but breaks one of these hasn't made things better. Check the list every time, not only when something feels risky.

## Why This Exists

It's easy to change a skill's instructions and easy to forget you did. Without a record, "why does the skill say that" has no answer beyond someone's memory of a bad run months ago. This record keeps the reason for an instruction around longer than the person who wrote it.
