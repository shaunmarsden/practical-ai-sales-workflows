# Instruction Change and Regression History: Opportunity Handover

This follows [the instruction change and regression history template](../templates/instruction-change-history-template.md). The opportunity-handover skill went through several rounds of a real test finding a real problem, an instruction changing, and a rerun. That record should outlast this pull request's discussion. [The main handover evaluation](hartwell-opportunity-handover-review.md) links here and carries the published score. This file explains why the instructions look the way they do.

I haven't tidied any of this up. I threw out two runs as contaminated before either change below could be tested properly. The second change, on pronouns, didn't work the first time. Both are recorded as they happened.

## Change 1: Action Ownership

| Field | Record |
| --- | --- |
| Original instruction version | `SKILL.md`'s "Preserve Commitments, Dates and Ownership" section, the output contract and the output template all asked for an owner column. None said an action needs exactly one named, internal, accountable person, rather than a compound name or the external party alone. See the version at [commit b834e6b](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/b834e6b058f18558c150124cb91479932a444d0/.agents/skills/opportunity-handover/SKILL.md). |
| Test case | A fictional handover from me to Jordan Lee for the Hartwell Analytics account, run clean (no reminder about ownership or anything else) against the transcript, post-call output and update source. It was the first run not contaminated by the skill's own answer-key reference file. But the shared transcript still had an undiscovered `Deliberate Test Points` section at this point, so I treat it as partial evidence, not a fully clean overall score (the main evaluation explains why). |
| Raw outputs | The full raw output of this run isn't kept as its own commit. It was replaced in the working tree before the next commit. The relevant part, the full Actions and Ownership table, is quoted below. The next commit, [51db524](https://github.com/shaunmarsden/practical-ai-sales-workflows/commit/51db5242f2da261347d0212910c6e8055b72e20), records this finding in its message and holds the raw output after the fix, described under Rerun outputs. |
| Rubric scores | 46 out of 50. Next step clarity: 3. Every other area: 4 or 5. No automatic failure. |
| Observed failure | The owner column from this run's actions table read: `Hartwell, Alex and/or Priya`, `Jordan, Shaun`, and `Unassigned`. None of these names one accountable person. |
| Instruction change | Added to `SKILL.md`: "Give every action exactly one accountable owner, never a compound name or an external party alone. When the party who must actually act is external, uncertain, or not yet assigned, name the internal person responsible for chasing it, not 'the customer' or 'unassigned' by itself. A handover that leaves an action without one clear internal owner has not actually handed it over." I added a matching MUST line to `references/output-contract.md`. I also updated the Actions and Ownership section of `templates/output-template.md` to say every row needs exactly one named internal owner, with any external dependency written in the action or evidence text, not the owner field. |
| Rerun outputs | See [commit 51db524](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/51db5242f2da261347d0212910c6e8055b72e20/examples/hartwell-opportunity-handover.md) for the full raw output. This rerun had an added reminder to "pay particular attention to the ownership requirement," so it's a targeted check on this one change, not a clean overall test. I keep it as evidence for this change only. |
| Score difference | Next step clarity went from 3 to 5. Every other area held its score. The total went from 46 to 48 in that targeted run. |
| What improved | All six actions in the rerun had exactly one named owner, five for the incoming salesperson and one for the outgoing one. The external dependency (for example, Hartwell's legal team clearing an approval) sat in the status and evidence columns rather than creeping back into the owner column as a compound name. |
| What did not | The rerun's problem with tone and repetition, the same three cautions repeated across five or more sections, didn't change, since the change wasn't aimed at it. |

I treat this change as resolved. It held again, cleanly, in the final published run in [the main evaluation](hartwell-opportunity-handover-review.md#final-run-fully-clean-unprompted), where all seven actions had one named owner with no reminder about ownership at all.

## Change 2: Pronouns and Personal References

This change took two rounds. The first didn't work.

### Round 1: A General Guardrail Sentence

| Field | Record |
| --- | --- |
| Original instruction version | Nothing. Before I found this failure, no file in this skill mentioned pronouns or personal characteristics at all. See [commit 51db524](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/51db5242f2da261347d0212910c6e8055b72e20/.agents/skills/opportunity-handover/SKILL.md), which comes before this change. |
| Test case | A fully clean run with no prompting. It was given only the skill file and its supporting files, plus the transcript, post-call output and update source, with the skill's own reference file left out and no reminder about any rule. Before this run I'd moved the last `Deliberate Test Points` section out of the shared transcript and into the post-call review, so neither the skill's reference material nor the transcript gave away the answer key. This run showed up the invented-pronoun failure. |
| Raw outputs | [Commit f118a95's version of the example](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/f118a9518e7007130475caae6cbd002a5adef16/examples/hartwell-opportunity-handover.md) is this run's raw output, apart from dash formatting. |
| Rubric scores | 41 out of 50. Factual accuracy: 2. Hallucination risk: 2. Every other area 4 or 5. **Automatic failure: yes.** |
| Observed failure | Four invented pronouns for Alex Morgan, whose gender no source states: "Alex said he would 'chase legal again this week'" (current position); "Alex's email states he is 'moving into a new role'" (people and confirmed roles); "and that he would 'chase legal again this week.' **Source: Alex's email**" (confirmed evidence, cited as if the email confirmed the pronoun); "referencing Alex's statement that he would chase it" (actions and ownership). The same run also invented pronouns for Jordan Lee, whose gender is just as unstated. |
| Instruction change | I added one sentence to `SKILL.md`'s guardrail list, `references/output-contract.md`'s MUST NOT list and `checks/checklist.md`. It said not to invent gender, pronouns or other personal characteristics, to use a person's name or neutral wording when pronouns aren't given, and never to carry one person's pronouns over to someone else. |
| Rerun outputs | A second fully clean run after adding the sentence, with the same eight files and no reminder of any kind. |
| Score difference | None. The rerun still scored 41 out of 50 with the same automatic failure. Alex again got "he" and "his" repeatedly, including in the Confirmed Evidence section. |
| What improved | Nothing measurable. The general sentence didn't change how the model handled this failure. |
| What did not | The core problem. The model still used a gendered pronoun for a name it read as probably a man's, in a document that was otherwise careful to label real unknowns as unknown. |

**I record this round as a failed fix, not a partial success.** One added sentence, among many other guardrail sentences the model was already following, wasn't strong enough to stop a gender guess from a name. The lesson I took forward wasn't "add a stronger sentence" but "add a mechanism that forces a checkable step," which is Round 2 below.

### Round 2: A Person Reference Ledger and a Mandatory Audit

| Field | Record |
| --- | --- |
| Original instruction version | The Round 1 sentence above, in `SKILL.md`, `references/output-contract.md` and `checks/checklist.md`, which Round 1's rerun showed wasn't enough. |
| Test case | The same eight files and no reminder, as in the clean Round 1 runs: `SKILL.md`, `references/output-contract.md`, `templates/output-template.md`, `checks/checklist.md`, `METHODOLOGY.md`, the transcript with its `Deliberate Test Points` section already removed, the post-call output, and the update source. |
| Raw outputs | Recorded in [the main evaluation](hartwell-opportunity-handover-review.md) with its score, and kept as the current `examples/hartwell-opportunity-handover.md` in this pull request. |
| Rubric scores | See the main evaluation for the full scoring table. |
| Observed failure (from Round 1, carried forward as the thing this round must fix) | The four quoted cases above, plus the same pattern for Jordan Lee. |
| Instruction change | I replaced the Round 1 sentence in `SKILL.md` with a set process. First, a required "Build a Person Reference Ledger Before Drafting" step. For every named person it lists exact name, confirmed role, whether pronouns are given, and how they may be referred to. The rules: use name or role, not a third-person pronoun, outside direct quotation; no invented title; and nothing carried over from one person to another. Second, a required "Run a Reference Audit Before Presenting the Handover" step. It names the exact words to scan for (he, him, his, himself, she, her, hers, herself, they, them, their, theirs, themselves, Mr, Mrs, Ms, and other personal characteristics). If an unsupported reference is still there, the handover is held back and the failing line named. I added the same process to `references/output-contract.md` as MUST and MUST NOT lines, to `templates/output-template.md` as a formatting instruction on the People and Confirmed Roles section, and to `checks/checklist.md` as a review question. |
| Rerun outputs | See the main evaluation's final run section for the result. |
| Score difference | See the main evaluation. I don't state a result here, so this file and the main evaluation can't disagree if one is updated and not the other. |
| What improved | See the main evaluation. |
| What did not | See the main evaluation. |

## Regression Checks

Run these against both changes together, on the latest clean rerun, before treating either as safe:

- A request for information from the other side hasn't become an agreed meeting.
- A second-hand detail is still labelled second-hand.
- A missing date stays unknown.
- An unauthorised commitment triggers a stop rather than being drafted anyway.
- A real disqualification isn't argued with (not applicable here, since the evidence has no disqualification).
- No external action is treated as already done.
- Every action has exactly one named internal owner (the Change 1 check, now standing).
- No named person gets an invented gender, pronoun, title or other personal characteristic (the Change 2 check, now standing on the published clean run).

See [the main evaluation](hartwell-opportunity-handover-review.md) for which of these hold now.
