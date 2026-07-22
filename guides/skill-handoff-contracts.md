# Skill Handoff Contracts

New to skills entirely? Start with [What Is a Sales AI Skill?](what-is-a-sales-ai-skill.md) first, then come back here.

Several skills in this repository are meant to run one after another on the same call: [extract post call evidence](../.agents/skills/extract-post-call-evidence/SKILL.md) first, then [draft a follow-up email](../.agents/skills/draft-follow-up-email/SKILL.md) or [build a business case](../.agents/skills/build-business-case/SKILL.md) from what it found. Passing the first skill's raw output into the second one usually works. It also quietly drops the one thing that made the first skill worth running at all: which parts of that output were confirmed, which were only an inference or an estimate, and which were still missing. Without that, the second skill has no way to tell an estimate from a fact, and the whole point of separating evidence from judgement in the first place is lost at exactly the point it gets handed over.

A handoff between two skills should state six things:

- **What is confirmed.** Directly supported by a source, not softened or upgraded in the handing over.
- **What is inferred, or estimated.** Carried across with its original label. An estimate stays an estimate; it does not become a fact just because it survived one more step.
- **What is missing.** A gap the first skill found and could not fill. The second skill should not quietly fill it either.
- **Which source supports each material point.** Enough that a person could check it without re-running the first skill.
- **What the next skill is allowed to do with it.** A confirmed fact can be stated plainly. An estimate can be used, but only if it is still labelled as one. A gap should not be turned into an assumption partway through the second skill's own output.
- **What still requires a person.** Carried forward, not reset. If the first skill flagged something for human review, the second skill inherits that flag; it does not get to resolve it on the second skill's own authority.

## A Worked Example

Using the fictional [Hartwell post-call transcript](../examples/hartwell-post-call-transcript.md) and its [completed output](../examples/hartwell-post-call-output.md): if extract post call evidence ran first, its handoff to draft follow-up email would look roughly like this.

**Confirmed:** Alex Morgan is Head of Revenue Operations at Hartwell Analytics. The team has eight account executives. HubSpot is the CRM. CRM updates can be delayed by one or two days. Alex does not want emails sent automatically.

**Estimate:** Alex's own figure of fifteen to thirty minutes of admin per call, explicitly unmeasured. Carried forward as an estimate, not restated as a measured fact.

**Missing:** the call date itself, so relative timings cannot be converted into calendar dates. Whether Priya wants anything specific included. What the recording package actually supports.

**Source per point:** each of the above traces to a specific line in the transcript or a specific statement Alex made on the call, not a summary written from memory of it.

**What draft follow-up email is allowed to do with this:** personalise the opening line and the resource summary using the confirmed facts and the labelled estimate. State that Thursday afternoon is conditional on Alex's internal approval, not a firm date. Leave a placeholder for the Tuesday review time rather than inventing one.

**What still requires a person:** Shaun checking his own diary before those times go in the email. Alex's internal approval before the transcript is shared. Whether to actually send the email at all.

Every one of those six things is already present in the [worked output](../examples/hartwell-post-call-output.md)'s own Final Accuracy Check section. The contract here is not new content: it is making explicit, at the handoff point between the two skills, what the finished output already had to get right by the end.

## Where This Applies Now

The clearest existing handoff is extract post call evidence into draft follow-up email, and the same evidence pack is also the right input for build a business case when a business case is actually warranted. Neither skill currently states the handoff as its own explicit step; each assumes it is given evidence in roughly this shape. Making the six fields above an explicit part of a skill's own "Gather the Inputs" section, when it is meant to consume another skill's output rather than raw notes, is the concrete next step, not a new piece of software.

## What This Is Not

This is a documentation and discipline standard, not a new automation. Nothing here is proposing that one skill should pipe its output straight into the next without a person looking at it in between. A handoff contract makes a manual step safer and more consistent; it is not a reason to remove the person from it.
