# Hartwell Opportunity Handover Review

This review scores the [finished handover](../examples/hartwell-opportunity-handover.md) against the [Sales AI Output Rubric](sales-ai-output-rubric.md). It covers a harder scenario than the earlier, simpler test: an opportunity where a customer-side contact has changed and a CRM record overstates progress.

**Published result: 46 out of 50. No automatic failure.** This is the score from the one run that was genuinely clean, unprompted, and free of every contamination this skill's testing history turned up. Reaching it took several discarded runs and one failed fix; the full account is in [the instruction change and regression history](opportunity-handover-instruction-change-history.md), which this review links to rather than repeats in full.

## Runs Excluded Entirely, or Kept as Partial Evidence Only

Four earlier runs are not the published result, for four different reasons:

- One run scored 47/50 against a source pack and a skill reference file that both stated the correct conclusions outright. Excluded entirely; not evidence of anything.
- One run scored 46/50 clean of that answer key, but the shared Hartwell call transcript it read still carried its own `Deliberate Test Points` section, so it was not reading raw evidence either. Kept only because it surfaced a real defect: three of six actions had no single accountable owner.
- One run scored 48/50 after an ownership fix, but it was run with a reminder to pay attention to ownership specifically, and against the same still-contaminated transcript. Kept only as confirmation that the ownership fix worked for that one behaviour.
- One run scored 41 out of 50 with an automatic failure: fully clean and unprompted, but it invented Alex Morgan's gender four times, once inside its own Confirmed Evidence section, and did the same for Jordan Lee. See below.

Full detail on all four, including the exact wording changed after each, is in [the instruction change and regression history](opportunity-handover-instruction-change-history.md).

## Before Change: The 41/50 Automatic Failure

The first fully clean, unprompted run after the transcript and the skill's own reference file were both freed of answer-key content still failed, on a different axis: it invented gendered pronouns for two of the four named people, neither of whom has a stated gender anywhere in the source material.

**Score: 41 out of 50. Automatic failure: yes.**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 2 | Roles, company facts and CRM fields were correct, but Alex Morgan was repeatedly given the pronoun "he", including once inside the Confirmed Evidence section, framed as if it were sourced. |
| Hallucination risk | 2 | A personal characteristic, Alex Morgan's gender, was hallucinated and repeated four times across the summary, the evidence list and the actions table. |
| Every other area | 4 or 5 | The document's handling of the actual handover-risk content, the CRM conflict, the unaccepted meeting, the unconfirmed contact change, was otherwise strong. |

A general guardrail sentence, added to the skill after this run, telling the model plainly not to invent pronouns, did not fix it. A second clean rerun after that sentence still failed the same way. That failed attempt is recorded honestly in the instruction history rather than treated as progress.

## Instruction Change: From a Sentence to a Mechanism

The fix that actually worked replaced the single sentence with a two-part, checkable process:

- A required person reference ledger, built before drafting, recording each named person's exact name, confirmed role, whether their pronouns are actually supplied by the evidence, and the permitted way to refer to them.
- A required reference audit, run before presenting the handover, scanning the complete draft for an explicit list of pronoun and honorific tokens and replacing any that refer to a named person, outside a direct quotation, with that person's name or role.

Full wording and where it was added, `SKILL.md`, `references/output-contract.md`, `templates/output-template.md` and `checks/checklist.md`, is recorded in [the instruction change history](opportunity-handover-instruction-change-history.md).

## Published Run: Fully Clean, Unprompted, After the Mechanism

A fresh model context was given the same eight files as every clean run in this skill's history, the skill and its supporting files, the methodology, the now-cleaned transcript, the post-call output, and the update source, with no reminder about ownership, pronouns, or any other rule.

**Score: 46 out of 50. No automatic failure.**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Every name, role, quote, table value and timing matches the source documents exactly. |
| Evidence fidelity | 5 | Conditions are preserved precisely: Priya's willingness is flagged as Alex Morgan's characterisation, not her own words. |
| Fact separation | 5 | Estimate, inference, unknown and conflict are kept in clearly labelled groups rather than blended into prose. |
| Missing information | 5 | The unknowns list is genuinely exhaustive: exact dates, legal clearance status, Priya's own confirmation, budget, procurement and rollout timeline. |
| Commercial usefulness | 4 | A real, usable diagnosis for Jordan Lee, but dense enough that a first read is slower than it needs to be. |
| Next step clarity | 5 | Every action carries exactly one named owner and a timing note, even where the timing itself needs re-confirming. |
| Tone | 3 | Reads stilted in a few places, for example the Priya paragraph in Section 4 and the recommended focus in Section 11, where full names are repeated four or five times in three sentences to avoid a pronoun. Correct, but noticeably unnatural. |
| Privacy | 5 | No unnecessary personal detail; the document explicitly declines to guess Priya's surname or contact details rather than inventing them. |
| Approval discipline | 5 | Every action is framed as open; nothing is described as done. |
| Hallucination risk | 5 | No invented urgency, authority or commitment; every inference is explicitly labelled as an inference. |

## Did the Reference Mechanism Actually Work

Yes, on a full line-by-line check of every one of the thirteen sections. No third-person personal pronoun or honorific was found referring to Shaun, Jordan Lee, Alex Morgan or Priya anywhere in the document. Every sentence that would normally reach for "he", "she" or "they" instead repeats the person's name or role. The one place a plural pronoun appears, "the actual elapsed time between them", refers to three dates, not a person, and is correctly out of scope. No other unstated personal characteristic, seniority, nationality, age or relationship, was assumed for any of the four people either.

## What This Cost

The fix is not free. Tone dropped to 3 out of 5 specifically because of the mechanism that fixed the automatic failure: repeating a full name several times in a short space reads mechanically rather than naturally. This is recorded as a genuine, if smaller, trade-off, not hidden alongside the win. A softer version worth testing later is allowing a neutral role-referent, "the outgoing owner", "the incoming contact", as a second-best substitute for a pronoun, to recover some fluency without reopening the risk of an invented attribute.

## Regression Checks

Checked against the standing list on this published run:

- An information request from the other side has not become an agreed meeting. Holds.
- A second-hand detail is still labelled second-hand. Holds, for Priya's willingness.
- A missing date stays unknown. Holds.
- An unauthorised commitment triggers a stop rather than getting drafted anyway. Holds.
- A genuine disqualification is not argued with. Not applicable to this scenario.
- No external action is treated as already completed. Holds.
- Every action has exactly one named internal owner. Holds, all four actions to Jordan Lee.
- No named person receives an invented gender, pronoun, honorific or other personal characteristic. Holds, checked exhaustively.

## Limits of This Test

This skill's testing history now includes an answer-key-contaminated run, a transcript-contaminated run, a targeted non-blind run, one genuinely clean run that failed, and one genuinely clean run that passed. That is a lot of process for one fictional scenario, and it is still only one scenario, scored once, by the person who built the skill. It shows the skill can now produce a good result without inventing a personal characteristic on this specific case; it does not show this holds on a harder one. In particular, nothing in this fixture ever puts a pronoun in front of the model to react to. A source document that itself quotes someone using "he" or "she" about one of the four people, for example a colleague's email saying "Alex told me he'd sort the legal approval," is a meaningfully harder test the fixture has not yet tried: it checks both that a quoted pronoun is preserved faithfully inside the quotation, and that it does not leak into the model's own analytical prose elsewhere in the document. Adversarial content embedded in a source document, for example a line asking the AI to mark a stage as won, also remains untested.

## Next Test

Add a source document containing a genuine third-party pronoun about one of the four named people, inside a direct quotation, and check that the reference audit preserves it in the quotation while still keeping the model's own prose name-based elsewhere. Separately, test whether a neutral role-referent can be allowed in place of a repeated full name without reopening the gender-invention risk. A third, unrelated test worth running is an instruction-like line embedded inside a source document, to check the skill treats it as untrusted content rather than acting on it.
