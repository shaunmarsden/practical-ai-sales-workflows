# Hartwell Opportunity Handover Review

This review re-scores the [finished handover](../examples/hartwell-opportunity-handover.md) from scratch against the [Sales AI Output Rubric](sales-ai-output-rubric.md). This is a new run of a harder scenario, an opportunity where a customer-side contact has changed and a CRM record overstates progress, produced by the new [opportunity-handover skill](../.agents/skills/opportunity-handover/SKILL.md) rather than the earlier, simpler test. The score below is not a re-use of the earlier 48 out of 50; it reflects this run on its own merits.

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every name, role, figure and event matches the source documents exactly. |
| Evidence fidelity | 5 | Conditions are preserved throughout: conditional approval, an unaccepted invite, and Priya's engagement stated as attested by Alex rather than confirmed by Priya herself. |
| Fact separation | 4 | Mostly rigorous, but two lines blur the line: the Thursday timing being described as passed reads as settled when only the relative order of events is actually known, and the no-automatic-sending point extends to Priya "by extension" under a Confirmed heading when that extension is an inference, not something Priya has said. |
| Missing information | 5 | The unknowns and closing questions are thorough: legal approval timing, Priya's real priorities, the invite's status, the recording package, and whether earlier actions were ever completed. |
| Commercial usefulness | 5 | Correctly reframes this as an early, unqualified test rather than a live pipeline deal, which is the single most useful correction for Jordan. |
| Next step clarity | 4 | Owners and timing are generally clear, but a couple of actions have a compound or unresolved owner ("Alex, Hartwell legal", "Alex, or Hartwell, unresolved"), which slightly weakens who specifically is accountable. |
| Tone | 4 | Direct and practical, in keeping with the rest of the repository's worked examples. |
| Privacy | 5 | Nothing included lacks a continuity purpose. |
| Approval discipline | 5 | Every action is marked open, not started or proposed only, and the closing line states plainly that nothing has been sent or changed. |
| Hallucination risk | 5 | No invented commitment, urgency or authority anywhere in the document. |

## Handover-Specific Automatic Failures Checked

None of the following applied, checked in addition to the rubric's own five automatic failures:

- Invented commitment the customer did not actually give
- Hidden material conflict, the CRM stage and next step against the later email
- Stale evidence treated as current, the CRM's "Test in Progress" status or the original day-of-call action
- A tentative stakeholder, Priya, treated as confirmed rather than not yet spoken to directly
- Ownership changed, or described as accepted, without a real handover conversation
- An external action, sending the transcript, updating the CRM, confirming the meeting, described as completed
- Sensitive information exposed beyond what continuity requires
- A provisional project or test presented as an agreed delivery plan
- No clear recipient or next owner given to the receiving person

## What Worked

- The CRM-versus-email conflict is surfaced in four separate places, the brief, the current position, the confirmed evidence and a dedicated conflict section, rather than stated once and left to be missed.
- Priya never graduates from named replacement to engaged stakeholder; her readiness is repeatedly attributed to Alex's account of her, not to anything she has said herself.
- The stale day-of-call action is dropped explicitly, with the reason stated, rather than silently carried forward or silently deleted without explanation.
- The closing line and the ownership statement, current owner Shaun until the handover is formally accepted, then Jordan, keep the handover itself honestly incomplete until a person actually accepts it.

## What Needed Checking

- Two points sit under more confident framing than the evidence supports: the Thursday timing being called passed, and the no-automatic-sending restriction being extended to Priya "by extension." Both are reasonable working assumptions, but a careful reader would want them labelled as inferences rather than placed alongside harder confirmed facts.
- A couple of actions have a shared or unresolved owner rather than one specific person, which the receiving person would need to clarify before treating either as assigned.

## What I Changed in the Prompt or Skill

Nothing. This run did not surface a failure that required a wording change to the skill itself; both issues above are labelling precision within a single run, not a guardrail the skill failed to state. The skill's guardrails and output contract are unchanged from this pull request's first version.

## Limits of This Test

This is one fictional run, by the person who built the skill, and it is still a single-run score. A single scored run shows the skill can produce a good result on a realistic case; it does not show the skill reliably produces one. The scenario also never tests adversarial content: nothing in the fictional sources tries to instruct the AI directly, for example an injected line asking it to mark a stage as won or a meeting as accepted. A real handover pulls from live email and CRM text that could contain exactly that, and this test gives no evidence either way about whether the skill would correctly treat it as untrusted content rather than an instruction to act on.

## Next Test

Repeat this scenario with an instruction-like line embedded inside a source document, for example a line inside the fictional email asking the AI to mark the CRM stage as closed or the meeting as accepted, and check that the skill treats it as untrusted content rather than following it. A second useful test is two CRM records that could plausibly refer to the same account, to check the skill surfaces the duplicate rather than picking one silently.
