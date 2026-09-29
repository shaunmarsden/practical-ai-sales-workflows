# Chase Stale-Date Wording: A Twelve-Run Test

The [chase prompt review](hartwell-chase-prompt-review.md) named a change and never made it. I made it, tested it and rejected it.

## What I Tested

That review found the run never mentioned Alex's own promise to share the transcript by Thursday afternoon. The scenario puts that promise up against his later leave. The prompt's stale-date line said:

> If a task, reminder or date was set before something later changed the picture, say so rather than treating it as current.

The run applied that to the CRM task but not to Alex's promise. **The review said it couldn't tell why.** Either the wording reads as only about reminders set internally, or that one run missed it. It named the fix and the re-run, and neither happened until now.

## The Change

I widened one sentence and changed nothing else:

> If a task, reminder, date or commitment was set before something later changed the picture, say so rather than treating it as current. That includes a commitment the prospect made themselves, such as a date they offered to send something by, not only a task or reminder set internally.

## What I Decided in Advance

Before any run, I wrote down the test: does the output mention Alex's own promise to share the transcript by Thursday afternoon? It has to refer to that promise. The word Thursday as a suggested send date for a new message doesn't count.

I also decided that if the prompt without the widened sentence mentioned the promise in four or more of its six runs, the wording wasn't the cause. The original miss would be a one-off, and I wouldn't adopt the change.

If both versions came out six of six or zero of six, the test couldn't separate them, and I wouldn't add runs to rescue a result. I'd note whether a run also said the promised Thursday clashed with the leave, but that wasn't the test.

## Method

I ran the prompt 12 times on the [Hartwell chase scenario](../examples/hartwell-chase-input.md), with the answer key removed at the line its own warning names. I used the same model and a fresh context each time, with no rubric and no access to this repository. Six runs used the prompt as it then stood, and six had the one sentence widened. **The prompt has since changed for a different reason**, so I name the versions here by the sentence under test, not by what was published then. I made every run for this test.

I scored them without knowing which version each came from, as in the [applied examples test](business-case-applied-examples-test.md). I copied the 12 outputs to files with neutral names, under a key I never looked at until I'd scored all 12.

## Result

| | Runs | Named Alex's Thursday commitment |
| --- | ---: | ---: |
| Prompt without the widened sentence | 6 | **4** |
| Prompt with the sentence widened | 6 | **6** |

**The plain prompt hit my threshold exactly, so I didn't adopt the change.** Four of six runs without the widened sentence named the promise. That puts the original miss down to ordinary variation, not the wording.

Fisher's exact test on the misses, zero of six against two of six, one-tailed: p = 0.45. There's nothing there, and I'd set the threshold to apply whatever the arithmetic said.

**This is the second time I've thought "the wording caused it" and been proved wrong by running the plain version properly instead of reasoning about the instruction.** The [check requirement test](business-case-check-requirement-test.md) was the first.

## What the Ten Runs Did With It

All ten that named the promise treated it as overtaken by the leave, not as broken or overdue, which is what the scenario's answer key asks for. Two put it well. One wrote that treating "he said Thursday" as a missed deadline worth raising would be wrong. Another said the promise "cannot currently be read as met, broken, or lapsed".

The two runs that missed it, both without the widened sentence, didn't ignore the transcript. Both asked whether internal approval was ever given, and both said the CRM task was set before the auto-reply. Neither connected Alex's own date to anything.

## The More Interesting Finding

This wasn't what I was testing. **Three of the 12 runs noticed that the scenario never says which weekday 7th July was.** So they wouldn't say whether the promised Thursday fell inside the leave. One listed it as an unknown to confirm rather than assume. A fourth run stated flatly that the promise "falls inside that away period".

They were right that the scenario didn't say. The clash followed from the dates unless 7th July was itself a Thursday, which the scenario never ruled out. So the inference was strong but not certain. **The answer key claimed more than the input showed**, so I fixed the input rather than softening the answer key.

**The input now names the weekdays.** The call is Tuesday 7th July, and the promised Thursday afternoon is 9th July, two days into a leave that began on the 8th. The CRM task fell due the day after it. That changed published test material, so the four records scored against the earlier version each say so: this test, the [chase decision review](hartwell-chase-review.md), the [chase prompt review](hartwell-chase-prompt-review.md) and the [repeat run findings](repeat-run-findings.md). All 12 runs on this page used the version without weekdays.

## What This Test Cannot Prove

- Six runs a version. It can reject the idea it was built to test, which it did at exactly the threshold I set, but it can't show a small effect. Four of six against six of six isn't a result the other way either.
- One scenario, one model, and I wrote and applied the test myself. Scoring without knowing the version removes one bias, not that one.
- The test is about naming the promise, not handling it well. All ten that named it handled it the way the answer key asks, but I noticed that afterwards and didn't score it.
- One scoring call could go the other way with a second scorer. One of the two misses does mention Alex's plan to send the transcript, "he said should be able to, subject to internal approval", but never the date. If the test were about naming the promise and not its timing, that run would count, and the version without the widened sentence would score five of six. The threshold is hit either way.

## What Changed

**Nothing in the prompt.** I didn't adopt the widened sentence, and the published wording stays.

**The scenario now names its weekdays**, so the dates show the Thursday clash rather than implying it, and the answer key says so. The last section of the [chase prompt review](hartwell-chase-prompt-review.md) records that I made, tested and rejected its proposed change.

## The Change to Test Next

Once the scenario named its weekdays, I ran it again: [12 more runs, six a side](chase-weekday-rerun.md). Naming the weekday didn't produce the behaviour the answer key asks for either. One of six said the promised date falls inside the leave, against none of six without the weekdays. So neither the instruction nor the input was the cause. What did work was a [required step rather than a principle](chase-dated-commitment-ledger-test.md). That was the third test on this thread and the first change it hasn't rejected.
