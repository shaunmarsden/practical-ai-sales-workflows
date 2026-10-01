# Chase Stale-Date Wording: A Twelve-Run Test

The [chase prompt review](hartwell-chase-prompt-review.md) named a change and never made it. I made it, tested it and rejected it.

## What I Tested

That review found the run never mentioned Alex's promise to share the transcript by Thursday afternoon, which the scenario puts against his later leave. The prompt's stale-date line said:

> If a task, reminder or date was set before something later changed the picture, say so rather than treating it as current.

The run applied that to the CRM task but not to the promise. The review couldn't tell whether the wording was too narrow or that one run missed it.

## The Change

I widened one sentence and changed nothing else:

> If a task, reminder, date or commitment was set before something later changed the picture, say so rather than treating it as current. That includes a commitment the prospect made themselves, such as a date they offered to send something by, not only a task or reminder set internally.

## What I Decided in Advance

The test: does the output mention Alex's own promise to share the transcript by Thursday afternoon? Thursday as a suggested send date for a new message doesn't count.

If the prompt without the widened sentence mentioned the promise in four or more of six runs, the wording wasn't the cause and I wouldn't adopt the change. If both versions came out six of six or zero of six, I wouldn't add runs to rescue a result.

## Method

I ran the prompt 12 times on the [Hartwell chase scenario](../examples/hartwell-chase-input.md), with the answer key removed at the line its own warning names. Same model, a fresh context each time, no rubric, no access to this repository. Six runs used the prompt as it then stood, and six had the sentence widened. The prompt has since changed for a different reason, so I name versions by the sentence under test.

I scored without knowing which version each run came from, as in the [applied examples test](business-case-applied-examples-test.md), using files with neutral names.

## Result

| | Runs | Named Alex's Thursday commitment |
| --- | ---: | ---: |
| Prompt without the widened sentence | 6 | **4** |
| Prompt with the sentence widened | 6 | **6** |

**The plain prompt hit my threshold exactly, so I didn't adopt the change, and the prompt stays as published.** The original miss was ordinary variation. Fisher's exact test on the misses, zero of six against two of six, one-tailed: p = 0.45.

It's the second time running the plain version proved "the wording caused it" wrong. The [check requirement test](business-case-check-requirement-test.md) was the first.

## What the Ten Runs Did With It

All ten that named the promise treated it as overtaken by the leave, not as broken or overdue, as the answer key asks. The two that missed it asked whether internal approval was ever given, and said the CRM task was set before the auto-reply. Neither connected Alex's own date to anything.

## The More Interesting Finding

This wasn't what I was testing. **Three of the 12 runs noticed that the scenario never says which weekday 7th July was**, so they wouldn't say whether the promised Thursday fell inside the leave. One listed it as an unknown to confirm. A fourth stated flatly that the promise "falls inside that away period".

They were right. The clash followed from the dates unless 7th July was itself a Thursday, which the scenario never ruled out. **The answer key claimed more than the input showed**, so I fixed the input rather than softening the key.

**The input now names the weekdays.** The call is Tuesday 7th July, and the promised Thursday afternoon is 9th July, two days into a leave that began on the 8th. All 12 runs on this page used the version without weekdays, and so did the other three records scored against it, which each say so: the [chase decision review](hartwell-chase-review.md), the [chase prompt review](hartwell-chase-prompt-review.md) and the [repeat run findings](repeat-run-findings.md).

## What This Test Cannot Prove

- Six runs a version. It can reject the idea it was built to test but can't show a small effect.
- One scenario, one model, and I wrote and applied the test myself. Scoring without knowing the version removes one bias, not that one.
- It tests naming the promise, not handling it well. I noticed afterwards that all ten handled it as the answer key asks, and didn't score it.
- One scoring call could go the other way. One of the two misses mentions Alex's plan to send the transcript, "he said should be able to, subject to internal approval", but not the date. If that counted, the version without the widened sentence would score five of six. The threshold is hit either way.

## The Change to Test Next

I [ran the scenario again](chase-weekday-rerun.md) with the weekdays named. One of six said the promised date falls inside the leave, against none of six without them, so neither the instruction nor the input was the cause. What worked was a [required step rather than a principle](chase-dated-commitment-ledger-test.md), the first change on this thread I haven't rejected.
