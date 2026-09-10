# Naming the Weekday: A Twelve-Run Re-Run

The chase scenario was changed on 10th September 2026 to name its weekdays, because the [stale-date test](chase-stale-date-test.md) found its answer key claiming a date conflict the input never established. This re-runs the scenario on both versions to see whether the fix produced the behaviour the answer key asks for.

**It did not.** The fix was still worth making, and the reason is worth being precise about.

## What the Answer Key Requires

> The skill must show that conflict rather than describe the transcript as overdue or promised unconditionally.

The conflict is between the transcript Alex promised by Thursday afternoon and the leave he announced the next day. With the call now dated Tuesday 7th July, the promised Thursday is 9th July, two days into a leave that began on the 8th.

## The Criterion and the Conditions

**The criterion, written down before any run:** does the output state that the promised Thursday afternoon falls inside Alex's leave, or that the leave began before the promised date, as a fact drawn from the dates? Naming it as an unknown to confirm is not a yes. Saying the commitment was overtaken by events, without connecting the promised date to the leave dates, is not a yes either, because that is equally true of the CRM task and does not show the conflict.

**The interest condition, also fixed in advance:** if the runs on the version with weekdays state the conflict no more often than two of six, naming the weekday did not achieve what it was done for and the input change should be reconsidered rather than kept on the grounds that it reads better.

**Contingencies, fixed in advance.** Both arms were run fresh rather than reusing the stale-date test's runs, since six of those carried a different prompt and all twelve came from a different session. Miscomputation of the date was to be recorded as an observation.

## Method

Twelve blind runs, same model, a fresh isolated context each time, no rubric and no access to this repository, answer key removed at the line the scenario's own warning names. Six on the scenario as it stood before the weekdays, six on the current version. The published [chase sequence prompt](../templates/chase-sequence-prompt.md) in both arms, unchanged, and the two scenario files differ on three lines and nothing else.

Scored without knowing which arm each run came from, with the mapping opened only afterwards.

## Result

| | Runs | Stated that the promised date falls inside the leave |
| --- | ---: | ---: |
| Scenario without weekdays | 6 | **0** |
| Scenario with weekdays | 6 | **1** |

**The interest condition was met.** One of six is not the behaviour the answer key asks for, and Fisher's exact on one of six against zero of six gives p = 0.5, which is nothing at all.

The single run that met it put it plainly: the commitment was "to share the transcript by Thursday afternoon (9th July), subject to internal approval. That date falls inside his stated away window (8th to 20th July), so the absence of a transcript by 10th July is already explained by his being away".

## The Pre-Registered Observation

**No run miscomputed the date.** Nothing said the promised Thursday was the 10th. Two runs mention both Thursday and 10th July in one sentence, correctly, because 10th July is the CRM task's due date.

## A Post-Hoc Observation, Labelled As One

Three of the six runs on the version with weekdays stated the promised date as 9th July. None of the six without weekdays stated a date at all, which they could not have done. One-tailed p on that cell is 0.09.

**This was not the pre-registered observation.** What was registered was miscomputation, and this is a different measure noticed afterwards. Six runs a side cannot separate it from nothing, and it is recorded rather than claimed.

If it is real, it says something narrow and useful: naming the weekday got half the runs to work out the date, and only one of those three went on to draw the conclusion. **Stating a date is not the same as noticing what it collides with.**

## The Judgement Call, and Which Way It Cuts

One run reads close to the criterion without meeting it. It says the CRM task "reflects the plan as it stood on 7th July (transcript expected Thursday afternoon), not the fact, now known, that Alex is unreachable until 20th July". That contrasts the promised transcript with the leave, but it does it through the task and never compares the two dates, so it is scored as a no.

**That run is in the arm without weekdays.** Under a looser reading it would be a yes, which would make the result one of six against one of six and remove even the difference of one. The looser reading makes the finding stronger, not weaker.

## What This Means

The weekday change fixed an over-claim in the answer key, which was the reason for making it, and it stays. What it did not do is produce the behaviour the answer key demands: **that requirement is unmet in five of six runs even with the dates spelled out.**

So the gap is not in the input. Before this re-run there were two candidate explanations for the original miss, the input being unstateable and the instruction being too narrow. The [stale-date test](chase-stale-date-test.md) rejected the instruction as the cause and this rejects the input. Neither is the answer, and the honest position is that nobody has found the cause yet.

Every one of the twelve runs decided to wait rather than chase, which is the decision the scenario asks for. This is a failure to surface one specific supporting fact, not a wrong answer.

## What This Re-Run Cannot Prove

- Six runs an arm, one scenario, one model, and a criterion written and applied by the same person. Blind scoring removes knowing the arm and nothing else.
- It cannot show that the weekday change is useless, only that it did not produce this behaviour. An input a reader cannot verify is a defect whether or not fixing it moves a model.
- It says nothing about the skill, only the prompt. The [repeat-run findings](repeat-run-findings.md) record two runs of the skill that did show the clash, on the version where it could only be inferred, which is the opposite result on a different artefact and worth someone testing properly.

## The Change to Test Next

The two obvious causes are eliminated, so the next hypothesis has to be more specific than "the wording is too narrow". The candidate worth pre-registering is an instruction to check every dated commitment against every known absence or unavailability window, as a step rather than a principle, on the pattern of the [person reference ledger](../.agents/skills/opportunity-handover/SKILL.md) that fixed the invented-pronoun failure when a plain instruction did not.
