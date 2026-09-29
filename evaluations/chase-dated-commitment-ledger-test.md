# The Dated Commitment Ledger: A Twelve-Run Test

Three tests have now gone after the same defect. The [chase prompt review](hartwell-chase-prompt-review.md) found a run that never mentioned the transcript Alex promised by Thursday afternoon, a promise the scenario puts inside his later leave. I [rejected](chase-stale-date-test.md) widening the instruction. I [rejected too](chase-weekday-rerun.md) naming the weekday in the scenario, which was needed before the clash could be shown at all.

**This is the first change on this thread I haven't rejected.** It takes the same form as the fix for the invented-pronoun failure: a required step rather than a principle.

## The Change

I added one paragraph before the prompt's list of sections and changed nothing else:

> Before writing any of the sections below, build a dated commitment ledger. List every date, deadline or commitment in what I have given you, including any the prospect set for themselves, and separately list every period anyone is stated to be away, unavailable or not monitoring messages. Then check each date in the first list against each period in the second and note which of them fall inside one. Carry that result into section 1 in words, including when nothing collides. The ledger itself is a working step, not part of the output.

## What I Decided in Advance

Before any run, I wrote down the test. It's the same one the weekday re-run used, so the two can be compared. Does the output say, as a fact drawn from the dates, that the promised Thursday afternoon falls inside Alex's leave, or that the leave began before the promised date? Listing it as an unknown to confirm doesn't count. Nor does saying events overtook the promise, without linking the promised date to the leave dates, since that's equally true of the CRM task.

If the version with the ledger showed the clash in two or fewer of its six runs, the step hadn't worked either, and I wouldn't adopt it.

I added a rule the earlier tests on this thread didn't have. If the version without the ledger showed the clash in four or more of six, it would have moved a long way from the one of six I'd measured the day before on the same prompt and scenario. Then I couldn't read the comparison at all.

## Method

I made 12 runs on the current chase scenario, with the answer key removed at the line its own warning names. I used the same model and a fresh context each time, with no rubric and no access to this repository. Six used the prompt as it was before the step, and six had the paragraph added. **The prompt now has the step**, so "published" today means the second version. I name the versions below by what they contain. I ran both fresh rather than reusing the previous day's runs, and scored them without knowing which version each came from.

## Result

| | Runs | Stated that the promised date falls inside the leave |
| --- | ---: | ---: |
| Prompt without the step | 6 | **2** |
| Prompt with the step | 6 | **5** |

**The step passed both of my thresholds, so I adopted it.**

**The evidence is weaker than the table looks.** Fisher's exact test on five of six against two of six, one-tailed, gives p = 0.12. That's short of what I've treated as a result elsewhere, and my test was a threshold, not a significance test. What I can say is that the step survived, on a thread where two earlier changes didn't.

I also ran a sum I hadn't planned, so treat it as background, not the result. The previous day's six runs without the step got one of six on the same scenario. Adding them in gives three of 12 against five of six, and p = 0.032. I didn't plan to pool runs across sessions, and it's the move I criticised on the [stacked figure test](business-case-stacked-figure-test.md), so this test doesn't rest on it.

## What the Step Did

Four of the six ledger runs visibly did the comparison, opening section 1 with a line like "Checking the dates against that away period" or "Collision check". A fifth stated the clash without showing the working. **The sixth did neither.** It never mentioned the promised date at all, so a model can still skip a required step entirely.

The two runs without the step that passed got there without being told to compare dates. That's worth remembering before treating the step as the only way to get this behaviour.

**The thing I planned to note came back clean.** No run printed the ledger as a table or list. All six kept it as a working step, as told.

## What Didn't Move, in Any of the Thirty-Six Runs

**Every run across all three tests on this thread decided to wait rather than chase.** Thirty-six out of thirty-six. This whole line of work has been about one supporting fact inside a correct answer, not a wrong decision, and it's worth keeping that in proportion.

## The Plain Prompt Moved Between Sessions

The prompt without the step got one of six on this scenario yesterday and two of six today. Same prompt, same input. **That's the run-to-run movement I keep measuring, showing up inside a group of six.** It's why I wrote the rule about the plain prompt moving before I had any numbers.

## What This Test Cannot Prove

- Six runs a version, one scenario, one model, and I wrote and applied the test myself. Scoring without knowing the version removes that one bias and nothing else.
- p = 0.12 supports adopting a change that costs one paragraph. It wouldn't support a claim that the step reliably produces the behaviour.
- **The step is in the prompt only.** The [Plan a Chase Sequence skill](../.agents/skills/plan-chase-sequence/SKILL.md) doesn't have it and hasn't been tested with it. The em dash rule is the warning against changing many files on the strength of one test.
- It says nothing about whether the ledger helps on an input with no date clash, where the instruction asks for a line saying nothing collides. None of these 12 runs was that case.

## The Change to Test Next

I've now answered both halves of this question.

For the first half, I [tested the step on the skill](chase-skill-ledger-test.md). It separated the two versions completely: six of six against zero of six, p of 0.0011. Before either had the step, the skill turned out to be worse at this than the prompt, the opposite of what I'd predicted in writing.

For the second, on a [scenario built with no clash in it](chase-no-collision-test.md), neither version invented one. So the step doesn't create a clash where there is none.
