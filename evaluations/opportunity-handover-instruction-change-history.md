# Instruction Change and Regression History: Opportunity Handover

This follows [the instruction change and regression history template](../templates/instruction-change-history-template.md). It exists because the opportunity-handover skill went through several rounds of a real test finding a real problem, an instruction changing, and a rerun, and that record should survive longer than this pull request's discussion does. It is linked from [the main handover evaluation](hartwell-opportunity-handover-review.md), which carries the published score; this file carries the reasoning behind why the instructions look the way they do.

Nothing here has been tidied up to make the process look cleaner than it was. Two runs were thrown out for contamination before either of the changes below could be tested properly, and the second change, on pronouns, did not work on its first attempt. Both are recorded as they actually happened.

## Change 1: Action Ownership

| Field | Record |
| --- | --- |
| Original instruction version | `SKILL.md`'s "Preserve Commitments, Dates and Ownership" section, the output contract, and the output template all required an owner column but never stated that an action needs exactly one named, internal, accountable person, as opposed to a compound name or the external party alone. See the version at [commit b834e6b](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/b834e6b058f18558c150124cb91479932a444d0/.agents/skills/opportunity-handover/SKILL.md). |
| Test case | A fictional handover from Shaun to Jordan Lee for the Hartwell Analytics account, run clean (no reminder about ownership or anything else) against the transcript, post-call output and update source. This was the first run not contaminated by the skill's own answer-key reference file, though the shared transcript still carried an undiscovered `Deliberate Test Points` section at this point, so it is treated as partial evidence, not a fully clean overall score (see the main evaluation for why). |
| Raw outputs | The full raw output of this run is not preserved as its own commit; it was superseded in the working tree before the next commit. The relevant excerpt, the full Actions and Ownership table, is quoted below. The commit that followed, [51db524](https://github.com/shaunmarsden/practical-ai-sales-workflows/commit/51db5242f2da261347d0212910c6e8055b72e20), documents this finding in its commit message and carries the post-fix raw output described under Rerun outputs. |
| Rubric scores | 46 out of 50. Next step clarity: 3. Every other area: 4 or 5. No automatic failure. |
| Observed failure | Quoting the actual owner column from this run's actions table: `Hartwell, Alex and/or Priya`, `Jordan, Shaun`, and `Unassigned`. None of these names one accountable person. |
| Instruction change | Added to `SKILL.md`: "Give every action exactly one accountable owner, never a compound name or an external party alone. When the party who must actually act is external, uncertain, or not yet assigned, name the internal person responsible for chasing it, not 'the customer' or 'unassigned' by itself. A handover that leaves an action without one clear internal owner has not actually handed it over." A matching MUST line was added to `references/output-contract.md`, and the Actions and Ownership section of `templates/output-template.md` was updated to say every row needs exactly one named internal owner, with external dependency captured in the action or evidence text instead of the owner field. |
| Rerun outputs | See [commit 51db524](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/51db5242f2da261347d0212910c6e8055b72e20/examples/hartwell-opportunity-handover.md) for the full raw output. This rerun included an added reminder to "pay particular attention to the ownership requirement," so it is a targeted regression check, not a blind overall test; it is kept as evidence for this specific change only. |
| Score difference | Next step clarity moved from 3 to 5. Every other area held at its prior score. Total moved from 46 to 48 in that targeted run. |
| What improved | All six actions in the rerun carried exactly one named owner, five to the incoming salesperson and one to the outgoing one, with the external dependency (for example, Hartwell's legal team clearing an approval) described in the status and evidence columns rather than smuggled back into the owner column as a compound name. |
| What did not | The rerun's tone and repetition issue, the same three cautions restated across five or more sections, was untouched by this change, since the change was not aimed at it. |

This change is treated as resolved: it held up again, cleanly, in the final published run recorded in [the main evaluation](hartwell-opportunity-handover-review.md#final-run-fully-clean-unprompted), where all seven actions carried one named owner with no reminder given about ownership at all.

## Change 2: Pronouns and Personal References

This change took two rounds. The first did not work.

### Round 1: A General Guardrail Sentence

| Field | Record |
| --- | --- |
| Original instruction version | Nothing. Before this failure was found, no file in this skill addressed pronouns or personal characteristics at all. See [commit 51db524](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/51db5242f2da261347d0212910c6e8055b72e20/.agents/skills/opportunity-handover/SKILL.md), which predates this change. |
| Test case | A fully clean, unprompted rerun, given only the skill file and its supporting files plus the transcript, post-call output and update source, with the skill's own reference file excluded and no reminder about any rule. By this point the source pack and the skill's reference file were both free of answer-key content, but the shared transcript itself still carried its own `Deliberate Test Points` section, discovered only after this run, so this run is also not the one whose score is published. |
| Raw outputs | [Commit f118a95's version of the example](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/f118a9518e7007130475caae6cbd002a5adef16/examples/hartwell-opportunity-handover.md) is this run's raw output, dash formatting aside. |
| Rubric scores | 41 out of 50. Factual accuracy: 2. Hallucination risk: 2. Every other area 4 or 5. **Automatic failure: yes.** |
| Observed failure | Quoting four instances of an invented pronoun for Alex Morgan, whose gender no source states: "Alex said he would 'chase legal again this week'" (current position); "Alex's email states he is 'moving into a new role'" (people and confirmed roles); "and that he would 'chase legal again this week.' **Source: Alex's email**" (confirmed evidence, cited as if the pronoun were part of what the email confirmed); "referencing Alex's statement that he would chase it" (actions and ownership). The same run separately invented pronouns for Jordan Lee, whose gender is equally unstated. |
| Instruction change | Added to `SKILL.md`'s guardrail list, `references/output-contract.md`'s MUST NOT list, and `checks/checklist.md`: a sentence stating that gender, pronouns and other personal characteristics must not be invented, that a person's name or neutral wording should be used when pronouns are not supplied, and that one person's pronouns must never be carried over to someone else. |
| Rerun outputs | A second fully clean run, produced after this sentence was added, using the same eight-file protocol and no reminder of any kind. |
| Score difference | None. The rerun still scored 41 out of 50 with the same automatic failure: Alex was again given "he" and "his" repeatedly, including inside the Confirmed Evidence section. |
| What improved | Nothing measurable. The general sentence did not change the model's behaviour on this specific failure. |
| What did not | The core problem: the model still defaulted to a gendered pronoun for a name it read as likely to belong to a man, even in a document that was otherwise careful to label a genuine unknown as unknown everywhere else. |

**This round is recorded as a failed fix, not a partial success.** A single added sentence, sitting alongside many other guardrail sentences the model was already following correctly, was not a strong enough mechanism to override whatever makes a name-based gender guess feel automatic. The lesson taken forward was not "add a stronger sentence" but "add a mechanism that forces a checkable step," which is Round 2 below.

### Round 2: A Person Reference Ledger and a Mandatory Audit

| Field | Record |
| --- | --- |
| Original instruction version | The Round 1 sentence described above, present in `SKILL.md`, `references/output-contract.md` and `checks/checklist.md`, and confirmed not sufficient by Round 1's rerun. |
| Test case | The same eight-file, no-reminder protocol as every clean run in this history: `SKILL.md`, `references/output-contract.md`, `templates/output-template.md`, `checks/checklist.md`, `METHODOLOGY.md`, the transcript (by now also cleaned of its own `Deliberate Test Points` section), the post-call output, and the update source. |
| Raw outputs | Recorded in [the main evaluation](hartwell-opportunity-handover-review.md) alongside its score, and preserved as the current `examples/hartwell-opportunity-handover.md` in this pull request. |
| Rubric scores | See the main evaluation for the full scoring table. |
| Observed failure (from Round 1, carried forward as the thing this round must fix) | The four quoted instances above, plus the same pattern for Jordan Lee. |
| Instruction change | Replaced the single Round 1 sentence with a concrete process in `SKILL.md`: a required "Build a Person Reference Ledger Before Drafting" step, listing exact name, confirmed role, whether pronouns are explicitly supplied, and the permitted reference form for every named person, with a rule to use name or role instead of a third-person pronoun outside direct quotation, no invented honorific, and no attribute transferred between people. Paired with a required "Run a Reference Audit Before Presenting the Handover" step, naming the exact tokens to scan for (he, him, his, himself, she, her, hers, herself, they, them, their, theirs, themselves, Mr, Mrs, Ms, and other personal characteristics) and requiring the handover to be withheld, with the failing line named, if an unresolved unsupported reference remains. The same mechanism was added to `references/output-contract.md` as MUST and MUST NOT lines, to `templates/output-template.md` as a formatting-level instruction on the People and Confirmed Roles section, and to `checks/checklist.md` as a specific review question. |
| Rerun outputs | See the main evaluation's final run section for the result. |
| Score difference | See the main evaluation. This history does not state a result here, to avoid this file and the main evaluation disagreeing if one is updated and not the other. |
| What improved | See the main evaluation. |
| What did not | See the main evaluation. |

## Regression Checks

Run against both changes together, on the most recent clean rerun, before treating either as safe:

- An information request from the other side has not become an agreed meeting.
- A second-hand detail is still labelled second-hand.
- A missing date stays unknown.
- An unauthorised commitment triggers a stop rather than getting drafted anyway.
- A genuine disqualification is not argued with (not applicable to this scenario; no disqualification is present in the evidence).
- No external action is treated as already completed.
- Every action has exactly one named internal owner (the Change 1 regression check, now standing).
- No named person receives an invented gender, pronoun, honorific or other personal characteristic (the Change 2 regression check, currently the open question this history exists to track).

See [the main evaluation](hartwell-opportunity-handover-review.md) for which of these currently hold.
