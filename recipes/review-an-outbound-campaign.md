# 📤 Recipe: Review an Outbound Campaign

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Reading what an outbound campaign's actual numbers support once it has run its course, rather than trusting the impression a good-looking reply rate leaves behind.

## You need

- The audience, the signal or list source used, the message and offer
- What changed since the last comparable campaign
- The raw numbers: delivered, replies, positive replies, meetings booked and attended, qualified opportunities

## You'll get

- What actually changed since the last comparable campaign
- The raw numbers read straight
- Whether the comparison is genuinely conclusive
- What to keep, stop, or test next

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/outbound-campaign-learning-review-prompt.md -->
```text
Act as a careful reviewer of an outbound campaign's actual result, not its impression.

Use only the numbers and detail I give you. Do not treat reply rate alone as the result, and do not imply a conclusion my sample size cannot actually support.

Record the following, exactly as I have described it, not a tidied-up version:

1. The audience: who this went to, and why it was selected.
2. The signal or data source used to build the list or angle.
3. The front-end offer, the message itself, and the call to action.
4. The single variable actually being tested here, and what was deliberately kept the same as the last comparable campaign. If more than one thing changed at once, say so plainly rather than picking one to credit.
5. The raw numbers: messages delivered, total replies, positive replies, meetings booked, meetings attended, and qualified opportunities that came from them.
6. Anything that makes this comparison uncertain: a small sample, a mixed audience, a data source that changed partway through, a benchmark from somewhere else being used as if it were this campaign's own baseline.
7. What to keep, stop, or test next, based only on what these numbers actually support.

Rules:
- Never present one campaign, a small sample, or someone else's benchmark as proof of what should work everywhere.
- Compare like with like. A change in audience and a change in message at the same time cannot be credited to either one alone.
- Mark a small or mixed sample as inconclusive rather than reading a trend into it.
- If reply rate looks good but meetings or qualified opportunities do not follow, say so rather than stopping the review at the more flattering number.
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Workflow](../workflows/14-outbound-campaign-learning-review.md)**  
Also: [Prompt](../templates/outbound-campaign-learning-review-prompt.md) · [Worked example](../examples/cedarwell-campaign-review-output.md)

## The AI cannot decide

- Which specific variable to test next if more than one changed at once
- What sample size would actually make the next test conclusive

## You must check

- Whether more than one thing changed since the last campaign
- Whether a small or mixed sample has genuinely been marked inconclusive
- Whether the review stopped at a flattering reply rate instead of checking meetings and qualified opportunities too

## Then

Decide what to actually keep, stop, or test next yourself; this proposes a read of the numbers, not the decision.

---

Want the fuller method? Open the [workflow](../workflows/14-outbound-campaign-learning-review.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
