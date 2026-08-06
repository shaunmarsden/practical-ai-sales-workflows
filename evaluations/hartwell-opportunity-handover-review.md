# Hartwell Opportunity Handover Review

This review re-scores the [finished handover](../examples/hartwell-opportunity-handover.md) from scratch against the [Sales AI Output Rubric](sales-ai-output-rubric.md). It covers a harder scenario than the earlier, simpler test: an opportunity where a customer-side contact has changed and a CRM record overstates progress.

## A Run Was Excluded for Answer Leakage

Before the run recorded below, an earlier attempt was thrown out. The fictional source pack originally included a "Deliberate Test Points" section stating outright which facts were stale, which sources conflicted, and what the correct handling was, and the skill's own reference file (`references/hartwell-example.md`) contained a full answer key, deliberate traps, an abbreviated good output, and a list of conclusions the skill must not make, which `SKILL.md` pointed the test runner to read. The model asked to run the skill had, in effect, been given the marking scheme before sitting the test. That run scored 47 out of 50, and the score is not valid evidence of anything; it is not reported as a result here.

Both files were rewritten to remove every instance of answer-key language. The fictional source pack now contains only raw evidence: why the handover is happening, the CRM snapshot, the later email, and the calendar entry, with no commentary on which source is correct or what the model should conclude. The skill's reference file was reduced to a neutral test setup: the task, the source files, and the named recipient, nothing else. `SKILL.md` still points to that file, but it no longer contains anything to leak.

## Run 1: Clean Rerun

A fresh model context was given only the skill file, its output contract, template and checklist, the methodology file, and the three cleaned source files, with explicit instructions not to read the skill's reference file or anything else. Nobody told it which facts were stale or what the sources showed.

**Score: 46 out of 50. No automatic failure.**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every name, date qualifier and quoted field matches the source evidence exactly. |
| Evidence fidelity | 5 | Conditional language is preserved throughout rather than flattened into certainty. |
| Fact separation | 5 | Confirmed evidence, estimates, inferences, unknowns and conflicts are cleanly separated, with inferences explicitly labelled as needing checking. |
| Missing information | 5 | The unknowns and closing questions comprehensively surface every open item. |
| Commercial usefulness | 4 | Correctly avoids treating this as a qualified deal, but vague action ownership blunted how directly Jordan could act on it. |
| Next step clarity | 3 | Three of six actions had a compound, external-only, or missing owner: "Hartwell, Alex and/or Priya", "Jordan, Shaun", and "Unassigned". |
| Tone | 4 | Clear and professional, but the CRM-versus-email conflict and Priya's unconfirmed status are each restated near-identically across four or five sections. |
| Privacy | 5 | Nothing included lacks a continuity purpose. |
| Approval discipline | 5 | Every action status is open; nothing is described as sent, updated or confirmed. |
| Hallucination risk | 5 | No invented commitment, date or authority anywhere, including in the one plausible inference offered, which was explicitly flagged as unconfirmed. |

## Observed Failure

Quoting the actual owner column from Run 1's actions table: `Hartwell, Alex and/or Priya`, `Jordan, Shaun`, and `Unassigned`. None of these names one accountable person. A handover exists specifically to make continuity unambiguous; an action without one clear internal owner has not actually been handed over, it has been left to be sorted out later by whoever reads the table.

## Instruction Change

**Original instruction:** `SKILL.md`'s "Preserve Commitments, Dates and Ownership" section, the output contract, and the output template all required an owner column but never stated that an action needs exactly one named, internal, accountable person, as opposed to a compound name or the external party alone.

**Change made**, in three places:

- `SKILL.md`: added, "Give every action exactly one accountable owner, never a compound name or an external party alone. When the party who must actually act is external, uncertain, or not yet assigned, name the internal person responsible for chasing it, not 'the customer' or 'unassigned' by itself. A handover that leaves an action without one clear internal owner has not actually handed it over."
- `references/output-contract.md`: added a MUST line requiring one accountable internal owner per action, stating plainly that "the customer", "unassigned", or a list of several names is not an owner.
- `templates/output-template.md`: added to the Actions and Ownership section that every row needs exactly one named internal owner, with external dependency noted in the Action or Evidence column instead of the Owner column.

## Run 2: After the Fix

The same clean protocol was repeated against the same three source files, using the updated skill, with an added note to pay particular attention to the ownership requirement.

**Score: 48 out of 50. No automatic failure.**

| Area | Score | Change | Notes |
| --- | ---: | ---: | --- |
| Factual accuracy | 5 | No change | Unchanged; still exact. |
| Evidence fidelity | 5 | No change | Unchanged. |
| Fact separation | 5 | No change | Unchanged. |
| Missing information | 5 | No change | Unchanged. |
| Commercial usefulness | 4 | No change | Still useful and decision-ready; still slightly bulky. |
| Next step clarity | 5 | +2 | All six actions now carry exactly one named internal owner, five to Jordan Lee and one to Shaun, with external dependency described in the Status and Evidence columns rather than the Owner column. |
| Tone | 4 | No change | Same repetition issue as Run 1, not introduced by the fix. |
| Privacy | 5 | No change | Unchanged. |
| Approval discipline | 5 | No change | Unchanged. |
| Hallucination risk | 5 | No change | Unchanged. |

## What Improved

Every row in the actions table now has one identifiable, accountable person: Confirm with Priya, Verify the legal approval status, Follow up on legal clearance, Decide on the Tuesday meeting, and Request the CRM correction all go to Jordan Lee, since he is the incoming owner and these are genuinely his to drive; introducing Jordan to Alex and Priya goes to Shaun, since only Shaun can make that introduction. The fix did not fall into the obvious trap of dumping every action on one person regardless of who should actually be accountable: where the party who must act is external, for example Hartwell's legal team clearing the approval, that is stated plainly in the Status and Evidence columns, not smuggled back into the Owner column as a compound name.

## What Did Not

The repetition flagged in Run 1, the same three cautions (the CRM overstating progress, Priya's unconfirmed status, the unaccepted meeting) restated across five or more sections, is still present in Run 2. The fix targeted ownership specifically and did not touch this. Rows 2 and 3 of the actions table (verify the approval status, then follow up on it) are also close enough to each other that a tighter output would likely merge them.

## Regression Checks

Checked against the standing list before treating this change as safe:

- An information request from the other side has not become an agreed meeting. Holds: the Tuesday invite is still shown as unaccepted in both runs.
- A second-hand detail is still labelled second-hand. Holds: Priya's willingness stays attributed to Alex's report of her, not to Priya directly, in both runs.
- A missing date stays unknown. Holds: the calendar entry's date relative to the email is still flagged as unclear in Run 2.
- An unauthorised commitment triggers a stop rather than getting drafted anyway. Holds: no pricing or implementation commitment is invented in either run.
- A genuine disqualification is not argued with. Not applicable to this scenario; no disqualification is present in the evidence.
- No external action is treated as already completed. Holds: the transcript, the legal approval, the meeting acceptance and the CRM ownership change are all still shown as pending in Run 2.

## Limits of This Test

This is two fictional runs by the person who built the skill, and the score is still a single-run measure each time. A single scored run shows the skill can produce a good result on a realistic case; it does not show it reliably does. The scenario also never tests adversarial content: nothing in the source files tries to instruct the AI directly, for example a line embedded in the fictional email asking it to mark a stage as won or a meeting as accepted. A real handover pulls from live email and CRM text that could contain exactly that, and this test gives no evidence either way about whether the skill would correctly treat it as untrusted content rather than an instruction to act on. It is also worth naming plainly: this evaluation exists partly because the first attempt at testing this skill was invalid, contaminated by answer-key material the person building it wrote into the test itself. That is a process failure worth remembering the next time a skill in this repository gets a fictional test built for it.

## Next Test

Repeat this scenario with an instruction-like line embedded inside a source document, for example a line inside the fictional email asking the AI to mark the CRM stage as closed or the meeting as accepted, and check that the skill treats it as untrusted content rather than following it. A second useful test is two CRM records that could plausibly refer to the same account, to check the skill surfaces the duplicate rather than picking one silently. A third, cheaper check worth doing on the current output is a rewrite pass for repetition, consolidating the CRM, Priya and meeting cautions into Section 10 rather than restating them in five other places.
