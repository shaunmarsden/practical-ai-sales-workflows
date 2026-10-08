# My Sales Copilot: Internal Use Finding

## Status

**Internal use, reported by me as the builder. Not independent validation.**

My private sales copilot is in use, on my own report. This finding rests on that and on my review of its current private instructions on 5th August 2026. I haven't reproduced any real customer records, messages, transcripts, employer process or private agent instructions.

## What I Checked Directly

The private instructions describe an agent that brings several workflows together. It can:

- understand several sales command modes;
- pull approved evidence from calendar, email, CRM, meeting notes and documents;
- choose among specialist workflows, each with fixed limits;
- separate facts, estimates, inferences, unknowns and conflicts;
- prepare meeting plans, follow-up work and proposed CRM changes;
- require approval before writing to any outside system;
- stop when the evidence points to waiting, checking or doing nothing.

That supports calling it an **approval-gated orchestration agent**, not a single skill or a separate sales job.

## What Internal Use Supports

- A private agent exists.
- I say I use it in live sales work.
- It's meant to cover more than one sales job and more than one source of evidence.
- The way it runs keeps external actions under human approval.
- The private method is mature enough to draw out a public design pattern that doesn't depend on any vendor.

## What It Does Not Support

- No public log shows how often it's used.
- No measured time saving is available.
- No conversion, revenue or productivity outcome is credited to the agent.
- I've now published one cleaned live run as a formal finding (see below), but it's one run, by me, not a pattern of use.
- No outside user has tested the public template.
- The instructions alone don't prove every connector, permission or specialist route works as written.

## Findings From the Instruction Audit

### Strong Controls

- Fast commands have limited output, such as one action or no more than three priorities.
- Retrieval is meant to be narrow, not a default search of every connected system.
- Fixed commitments and stated timing limits come before stale activity.
- Specialist work goes to the right workflow rather than being repeated inside one large instruction.
- Facts, estimates, assumptions and unknowns are kept apart.
- Customer messages, CRM changes and other writes need exact approval.
- The agent may wait, stop or archive rather than default to another chase.

### Hard Controls Added to the Public Method After Review

I've confirmed these five controls are in the public guide, template and fictional test that came out of this review. I believe I also made matching changes to the private agent's own instructions, but this review didn't independently check that private, saved setup.

- Every named specialist route must be confirmed as installed and available before use. A missing route must be reported, not hidden behind a generic fallback.
- Both the written instructions and the connected-app permissions must be checked. Actions that face customers, change records or are hard to undo still need approval, even when a tool could technically do them.
- Qualification and eligibility language has a hard stop while budget, authority, timeline, procurement or another major condition is unresolved.
- When sources disagree, the agent must follow the stated order of sources and show the contradiction, rather than default to the first source it checked.
- Every external write needs an instruction that names the exact action. That includes drafts inside a system, CRM writes, tasks, stage moves, calendar changes, message actions and document edits.

### Controls That Still Need Ongoing Checking

- During this review I couldn't check two private route names against the specialist list currently available.
- It still needs a formal set of repeatable tests for missing tools, conflicting records, meetings about to start and unsupported proof claims.

## Public Method Extracted

The general method is now written up in:

- [Build an Approval-Gated Sales Copilot](../guides/build-an-approval-gated-sales-copilot.md)
- [Approval-Gated Sales Copilot Template](../templates/approval-gated-sales-copilot-template.md)
- [Fictional source pack](../examples/fictional-sales-copilot-source-pack.md)
- [Fictional output](../examples/fictional-sales-copilot-output.md)
- [Scored evaluation](fictional-sales-copilot-review.md)
- [Live-run finding](sales-copilot-live-run-finding.md)

## Next Evidence

The next big gap is an independent attempt, not another internal run by me: a salesperson outside this project adapting the public template with their own approved information, and reporting where it helps or fails.
