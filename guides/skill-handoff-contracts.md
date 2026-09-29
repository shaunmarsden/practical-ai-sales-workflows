# Skill Handoff Contracts

New to skills? Start with [What Is a Sales AI Skill?](what-is-a-sales-ai-skill.md), then come back here.

Several skills here are meant to run one after another on the same call. [Extract post call evidence](../.agents/skills/extract-post-call-evidence/SKILL.md) runs first. Then [draft a follow-up email](../.agents/skills/draft-follow-up-email/SKILL.md) or [build a business case](../.agents/skills/build-business-case/SKILL.md) works from what it found.

Passing the first skill's raw output into the second usually works. But it quietly drops the thing that made the first skill worth running: which parts were confirmed, which were only an inference or an estimate, and which were still missing. Without that, the second skill can't tell an estimate from a fact. The point of keeping evidence apart from judgement is lost at the very moment the work changes hands.

A handoff between two skills should state six things:

- **What is confirmed.** Directly supported by a source, and not softened or upgraded on the way across.
- **What is inferred, or estimated.** Carried across with its original label. An estimate stays an estimate. It doesn't become a fact just because it survived one more step.
- **What is missing.** A gap the first skill found and couldn't fill. The second skill shouldn't quietly fill it either.
- **Which source supports each material point.** Enough that a person could check it without running the first skill again.
- **What the next skill is allowed to do with it.** A confirmed fact can be stated plainly. An estimate can be used, but only if it's still labelled as one. A gap shouldn't turn into an assumption halfway through the second skill's output.
- **What still requires a person.** Carried forward, not reset. If the first skill flagged something for a person to review, the second skill keeps that flag. It doesn't get to settle the matter itself.

## A Worked Example

This uses the fictional [Hartwell post-call transcript](../examples/hartwell-post-call-transcript.md) and its [completed output](../examples/hartwell-post-call-output.md). If extract post call evidence ran first, its handoff to draft follow-up email would look roughly like this.

**Confirmed:** Alex Morgan is Head of Revenue Operations at Hartwell Analytics. The team has eight account executives. HubSpot is the CRM. CRM updates can be delayed by one or two days. Alex doesn't want emails sent automatically.

**Estimate:** Alex's own figure of 15 to 30 minutes of admin per call, which Alex said wasn't measured. It goes forward as an estimate, not as a measured fact.

**Missing:** the date of the call, so relative timings can't be turned into calendar dates. Whether Priya wants anything specific included. What the recording package supports.

**Source per point:** each point above traces to a specific line in the transcript or something Alex said on the call, not a summary written from memory.

**What draft follow-up email is allowed to do with this:** personalise the opening line and the resource summary using the confirmed facts and the labelled estimate. Say that Thursday afternoon depends on Alex's internal approval, and isn't a firm date. Leave a placeholder for the Tuesday review time rather than inventing one.

**What still requires a person:** me checking my own diary before those times go in the email. Alex's internal approval before the transcript is shared. Whether to send the email at all.

All six are already in the Final Accuracy Check section of the [worked output](../examples/hartwell-post-call-output.md). The contract isn't new content. It spells out, at the point where one skill hands to the next, what the finished output already had to get right by the end.

## Where This Applies Now

The clearest handoff today is extract post call evidence into draft follow-up email. The same evidence pack is also the right input for build a business case, when a business case is called for. Neither skill states the handoff as a step of its own yet. Each assumes it gets evidence in roughly this shape. The next step is to add the six fields above to a skill's "Gather the Inputs" section, where that skill takes another skill's output rather than raw notes. That's a change to the instructions, not new software.

## What This Is Not

This is a standard for writing things down and working carefully, not a new automation. Nothing here suggests one skill should feed its output straight into the next without a person looking at it in between. A handoff contract makes a manual step safer and more consistent. It isn't a reason to take the person out of it.
