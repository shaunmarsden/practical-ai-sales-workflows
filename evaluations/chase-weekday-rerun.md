# Naming the Weekday: A Twelve-Run Re-Run

On 10th September 2026 I changed the chase scenario to name its weekdays, because the [stale-date test](chase-stale-date-test.md) found its answer key claiming a date clash the input never showed. This page re-runs both versions to see whether the fix produced the behaviour the key asks for.

**It didn't.** The fix stays anyway, for a different reason.

## What the Answer Key Requires

> The skill must show that conflict rather than describe the transcript as overdue or promised unconditionally.

Alex promised the transcript by Thursday afternoon and announced his leave the next day. The call is dated Tuesday 7th July, so the promised Thursday is 9th July, two days into a leave that began on the 8th.

## What I Decided in Advance

The test: does the output say, as a fact drawn from the dates, that the promised Thursday afternoon falls inside Alex's leave, or that the leave began before the promised date? Listing it as an unknown to confirm doesn't count. Nor does saying events overtook the promise without linking its date to the leave dates.

If the version with weekdays showed the clash in two of six runs or fewer, naming the weekday hadn't done its job, and I'd rethink the change.

## Method

I made 12 runs, with the same model and a fresh context each time, no rubric, no access to this repository, and the answer key removed at the line the scenario's own warning names. Six runs used the scenario before the weekdays, and six used the current version. Both used the published [chase sequence prompt](../templates/chase-sequence-prompt.md), unchanged, and the two scenario files differ on three lines. I scored them without knowing which version each came from.

## Result

| | Runs | Stated that the promised date falls inside the leave |
| --- | ---: | ---: |
| Scenario without weekdays | 6 | **0** |
| Scenario with weekdays | 6 | **1** |

**The version with weekdays fell below my threshold.** Fisher's exact test on one of six against zero of six gives p = 0.5, which is nothing at all. The one run that did it wrote that the promised date "falls inside his stated away window (8th to 20th July)".

No run got the date wrong. None put the promised Thursday on the 10th, when the CRM task was due.

## Something I Noticed Afterwards

Three of the six runs with weekdays gave the promised date as 9th July. None of the six without could. The one-tailed p is 0.09. I didn't plan to measure this, and six runs a side can't separate it from chance, so I'm recording it, not claiming it. If it's real, naming the weekday got half the runs to work out the date, and only one of the three drew the conclusion. **Stating a date isn't the same as noticing what it clashes with.**

## The Judgement Call, and Which Way It Cuts

One run comes close without passing. It says the CRM task reflects the plan of 7th July, "not the fact, now known, that Alex is unreachable until 20th July". That sets the promise against the leave through the task and never compares the dates, so I scored it as a no. It's in the version without weekdays. A looser reading would pass it, making the result one of six against one of six, which strengthens the finding.

## What This Means

The weekday change fixed an over-claim in the answer key, which is why I made it, and it stays: an input a reader can't check is a defect whether or not fixing it moves a model. It didn't produce the behaviour the key demands: **five of six runs still miss it with the dates spelled out.**

I had two possible causes for the original miss: an input that didn't state the clash, and an instruction that was too narrow. The stale-date test ruled out the instruction and this rules out the input. I haven't found the cause. All 12 runs decided to wait rather than chase, as the scenario asks, so they missed one supporting fact, not the right answer.

## What This Re-Run Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the test myself.
- It says nothing about the skill, only the prompt. The [repeat-run findings](repeat-run-findings.md) record two skill runs that did show the clash, on the version where it could only be inferred.

## The Change to Test Next

I next tested a required step rather than a principle, copied from the [person reference ledger](../.agents/skills/opportunity-handover/SKILL.md), which fixed the invented-pronoun failure when a plain instruction didn't. **It's the first change on this thread I haven't rejected**, at five of six against two of six. The [test](chase-dated-commitment-ledger-test.md) says why its evidence is weaker than that table looks.
