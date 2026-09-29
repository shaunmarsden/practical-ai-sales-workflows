# Naming the Weekday: A Twelve-Run Re-Run

I changed the chase scenario on 10th September 2026 to name its weekdays. The [stale-date test](chase-stale-date-test.md) had found its answer key claiming a date clash the input never showed. This page re-runs the scenario on both versions to see whether the fix produced the behaviour the answer key asks for.

**It didn't.** The fix was still worth making, and I want to be exact about why.

## What the Answer Key Requires

> The skill must show that conflict rather than describe the transcript as overdue or promised unconditionally.

The clash is between the transcript Alex promised by Thursday afternoon and the leave he announced the next day. With the call now dated Tuesday 7th July, the promised Thursday is 9th July, two days into a leave that began on the 8th.

## What I Decided in Advance

Before any run, I wrote down the test: does the output say, as a fact drawn from the dates, that the promised Thursday afternoon falls inside Alex's leave, or that the leave began before the promised date? Listing it as an unknown to confirm doesn't count. Nor does saying events overtook the promise, without linking the promised date to the leave dates. That's equally true of the CRM task and doesn't show the clash.

I also decided that if the version with weekdays showed the clash in two of six runs or fewer, naming the weekday hadn't done its job. I'd then rethink the input change rather than keep it because it reads better.

I ran both versions fresh rather than reusing the stale-date test's runs, since six of those used a different prompt and all 12 came from a different session. I'd note any run that got the date wrong.

## Method

I made 12 runs, with the same model and a fresh context each time, no rubric and no access to this repository. I removed the answer key at the line the scenario's own warning names. Six runs used the scenario as it was before the weekdays, and six used the current version. Both used the published [chase sequence prompt](../templates/chase-sequence-prompt.md), unchanged. The two scenario files differ on three lines and nothing else.

I scored the runs without knowing which version each came from, and only looked at the key afterwards.

## Result

| | Runs | Stated that the promised date falls inside the leave |
| --- | ---: | ---: |
| Scenario without weekdays | 6 | **0** |
| Scenario with weekdays | 6 | **1** |

**The version with weekdays fell below my threshold.** One of six isn't the behaviour the answer key asks for. Fisher's exact test on one of six against zero of six gives p = 0.5, which is nothing at all.

The one run that did it put it plainly: the commitment was "to share the transcript by Thursday afternoon (9th July), subject to internal approval. That date falls inside his stated away window (8th to 20th July), so the absence of a transcript by 10th July is already explained by his being away".

## The Thing I Planned to Note

**No run got the date wrong.** None said the promised Thursday was the 10th. Two runs mention both Thursday and 10th July in one sentence, correctly, because 10th July is when the CRM task was due.

## Something I Noticed Afterwards

Three of the six runs on the version with weekdays gave the promised date as 9th July. None of the six without weekdays gave a date at all, which they couldn't have. The one-tailed p on that is 0.09.

**I didn't plan to measure this.** I'd planned to note wrong dates, and this is a different thing I spotted later. Six runs a side can't tell it from chance, so I'm recording it, not claiming it.

If it's real, it says something narrow and useful. Naming the weekday got half the runs to work out the date, and only one of those three went on to draw the conclusion. **Stating a date isn't the same as noticing what it clashes with.**

## The Judgement Call, and Which Way It Cuts

One run comes close to the test without passing it. It says the CRM task "reflects the plan as it stood on 7th July (transcript expected Thursday afternoon), not the fact, now known, that Alex is unreachable until 20th July". That sets the promised transcript against the leave, but through the task, and it never compares the two dates. So I scored it as a no.

**That run is in the version without weekdays.** Under a looser reading it would pass, making the result one of six against one of six and removing even the difference of one. The looser reading makes the finding stronger, not weaker.

## What This Means

The weekday change fixed an over-claim in the answer key, which is why I made it, and it stays. But it didn't produce the behaviour the answer key demands. **Five of six runs still miss it even with the dates spelled out.**

So the gap isn't in the input. Before this re-run I had two possible causes for the original miss: an input that didn't state the clash, and an instruction that was too narrow. The [stale-date test](chase-stale-date-test.md) ruled out the instruction and this rules out the input. I haven't found the cause yet.

All 12 runs decided to wait rather than chase, which is the decision the scenario asks for. This is a failure to bring up one supporting fact, not a wrong answer.

## What This Re-Run Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the test myself. Scoring without knowing the version removes that one bias and nothing else.
- It can't show the weekday change is useless, only that it didn't produce this behaviour. An input a reader can't check is a defect whether or not fixing it moves a model.
- It says nothing about the skill, only the prompt. The [repeat-run findings](repeat-run-findings.md) record two runs of the skill that did show the clash, on the version where it could only be inferred. That's the opposite result on a different file, and worth someone testing properly.

## The Change to Test Next

The next thing I tested was a required step rather than a principle. It copies the [person reference ledger](../.agents/skills/opportunity-handover/SKILL.md), which fixed the invented-pronoun failure when a plain instruction didn't. **It's the first change on this thread I haven't rejected**, at five of six against two of six. It's [recorded here](chase-dated-commitment-ledger-test.md), with the reasons its evidence is weaker than that table looks.
