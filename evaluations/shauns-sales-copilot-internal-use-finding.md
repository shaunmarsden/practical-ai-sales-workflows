# Shaun's Sales Copilot: Internal Use Finding

## Status

**Builder-reported internal use. Not independent validation.**

Shaun reports that his private sales copilot is in use. This finding is based on that statement and a review of its current private instruction set on 5th August 2026. No real customer records, messages, transcripts, employer process or private agent instructions are reproduced here.

## What Was Directly Inspected

The private instruction set describes a composition agent that can:

- interpret several sales command modes;
- retrieve approved evidence from calendar, email, CRM, meeting notes and documents;
- choose among bounded specialist workflows;
- separate facts, estimates, inferences, unknowns and conflicts;
- prepare meeting plans, follow-up work and proposed CRM changes;
- require explicit approval before external writes;
- stop when the evidence supports waiting, verification or no action.

This supports classifying it as an **approval-gated orchestration agent**, not a single skill or a seventeenth sales job.

## What Internal Use Supports

- A private agent exists.
- Its builder reports using it in live sales work.
- The intended use covers more than one sales job and more than one evidence source.
- The operating model keeps external actions under human approval.
- The private method is mature enough to extract a public, vendor-neutral design pattern.

## What It Does Not Support

- No frequency of use is logged publicly.
- No measured time saving is available.
- No conversion, revenue or productivity outcome is attributed to the agent.
- No sanitised live run has yet been published as a formal finding.
- No independent external user has tested the public template.
- The instruction set alone does not prove that every connector, permission or specialist route works as written.

## Findings From the Instruction Audit

### Strong Controls

- Fast commands have bounded output, including one action or no more than three priorities.
- Retrieval is meant to be narrow rather than a default search of every connected system.
- Fixed commitments and explicit timing boundaries take priority over stale activity.
- Specialist work is routed rather than duplicated inside one large instruction.
- Facts, estimates, assumptions and unknowns are separated.
- Customer communication, CRM changes and other writes require exact approval.
- The agent is allowed to wait, stop or archive rather than default to another chase.

### Controls That Need Ongoing Checking

- Named specialist routes can be renamed, retired or unavailable. Two private route names could not be verified against the currently available specialist list during this review.
- Written instructions and the agent builder's actual app permissions must match. A prose rule does not remove a permission granted in the interface.
- Qualification and eligibility language needs a hard stop while material conditions remain unresolved.
- A formal regression pack is still needed for missing tools, conflicting records, near-starting meetings and unsupported proof claims.

## Public Method Extracted

The general method is now documented in:

- [Build an Approval-Gated Sales Copilot](../guides/build-an-approval-gated-sales-copilot.md)
- [Approval-Gated Sales Copilot Template](../templates/approval-gated-sales-copilot-template.md)
- [Fictional source pack](../examples/fictional-sales-copilot-source-pack.md)
- [Fictional output](../examples/fictional-sales-copilot-output.md)
- [Scored evaluation](fictional-sales-copilot-review.md)

## Next Evidence

The next useful step is one sanitised run log showing the request, sources used, decision prepared, human correction and actions deliberately left unperformed. After that, an independent salesperson should try the public fictional pack or adapt the template with approved information and report where it helps or fails.
