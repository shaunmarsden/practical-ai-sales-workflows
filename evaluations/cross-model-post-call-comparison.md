# Cross-Model Post-Call Comparison

Run 19 July 2026: the same [Northstar transcript](../examples/northstar-post-call-transcript.md) and the same [post-call follow-up prompt](../templates/post-call-follow-up-prompt.md), pasted as one message into a completely fresh conversation in Claude, ChatGPT and Gemini, with no prior context in any of them. Each output is scored against the same [sales AI output rubric](sales-ai-output-rubric.md).

This compares corrections needed, not which answer reads most polished. A fluent answer that quietly invents a confirmed meeting is worse than a plainer one that correctly says the time is still pending.

## Method Note

Claude was run in a brand new conversation, separate from the one used to build this repository, specifically so the result wasn't just Claude confirming something it had already been told the answer to. ChatGPT and Gemini were run by Shaun directly, since this environment's browser tooling is blocked from reaching either domain; the raw outputs were pasted back unedited before scoring.

**Microsoft Copilot is not included in this run, and that gap is worth naming rather than leaving quiet.** A genuine comparison would cover it: it's frequently the only AI tool a salesperson has access to, since plenty of organisations lock the choice down to whatever their IT department has already rolled out, and Copilot users deserve the same evidence as everyone else, not an assumption that the other three are the default and Copilot is an afterthought. It's missing here for a plain reason: neither Shaun nor this environment currently has access to it to run the test honestly. If that changes, this is the first thing to add.

## Result

| Model | Score |
| --- | ---: |
| ChatGPT | 49 / 50 |
| Claude | 46 / 50 |
| Gemini | 42 / 50 |

**Automatic failure: none of the three.** No model invented a confirmed meeting, claimed an external action as completed, or presented an estimate as measured fact.

## Scoring Detail

| Area | ChatGPT | Claude | Gemini |
| --- | ---: | ---: | ---: |
| Factual accuracy | 5 | 4 | 4 |
| Evidence fidelity | 5 | 5 | 4 |
| Fact separation | 5 | 5 | 5 |
| Missing information | 5 | 5 | 3 |
| Commercial usefulness | 5 | 5 | 4 |
| Next step clarity | 4 | 4 | 4 |
| Tone | 5 | 4 | 4 |
| Privacy | 5 | 5 | 5 |
| Approval discipline | 5 | 5 | 5 |
| Hallucination risk | 5 | 4 | 4 |

## What All Three Got Right

- Correctly labelled the fifteen-to-thirty-minute admin figure as Alex's own unmeasured estimate, in every section where it appeared.
- Preserved every conditional word: the transcript approval, Thursday afternoon, and Tuesday morning were all kept pending rather than upgraded into firm commitments.
- Did not invent a product, price, or implementation date, correctly noticing the transcript never actually names what Shaun is selling.
- Framed every CRM update and email draft as a suggestion for human review, not a completed action.
- No em dashes, no invented urgency, no filler phrases in any of the three follow-up emails.

## Where Each Model Actually Differed

### Claude: one real self-check miss

Claude's follow-up email draft opens the meeting-time paragraph with "I have checked my diary and can offer the following slots," immediately followed by a placeholder: "[INSERT CONFIRMED TIME OPTIONS BEFORE SENDING.]" Those two lines contradict each other: the diary has explicitly not been checked yet, that is the entire reason for the placeholder. Claude's own "Final Accuracy Check" section, which correctly caught several other risks, did not catch this one. A real flaw, and a useful reminder that a model's self-check step is not automatically thorough just because the section exists.

### Gemini: thinnest missing-information section, one soft overreach

Gemini's "Missing Information" section listed four items, against ChatGPT's ten and Claude's eight. It did not flag that the call date itself is unknown (so relative timings can't be converted to calendar dates, a rule the prompt states directly), and did not notice that no product or service is actually named anywhere in the transcript. Separately, Gemini's email sign-off reads "I look forward to reviewing the results together next week," which is milder than Claude's diary error but still overstates things: no meeting is confirmed, and "next week" reads more definite than "a review was proposed, pending a time." Gemini's own accuracy check did not catch this either.

### ChatGPT: most thorough, one minor clarity blur

ChatGPT's actions table used "Shaun and Alex" as a joint owner for two rows (running the example together, reviewing the result together). That's an honest description of what those steps actually are, but it's less crisp for "who owns the next move" than a single-owner row, which is what cost it a point on next step clarity, the only criterion it didn't score a perfect 5 on. Otherwise this was the strongest run: it explicitly cited the prompt's own call-date rule, added an explicit "Inferences: none relied upon" line showing it had actively checked itself for smuggled-in assumptions, and its Final Accuracy Check used a consistent "this would overstate it, corrected to X" structure that mapped cleanly onto genuine risks rather than restating obvious rules.

## What This Actually Suggests

In this one run, ChatGPT needed the fewest corrections, Claude needed one real one, and Gemini needed a couple, including a self-check that missed the thing its own email got slightly wrong. That is not the same as "ChatGPT is better at this task." It is one transcript, one prompt, one run per model, with no control over each provider's default settings, reasoning effort, or model version at the time Shaun ran his two.

## Honest Caveat and Next Test

This is a single data point. Before drawing any real conclusion about which model to default to for this kind of work, the same comparison should be repeated with: a different transcript (ideally one with a genuinely ambiguous or ugly signal rather than another clean traps-only case), the same models run more than once each to see how much the corrections needed vary between runs of the same model, and the exact model version and any relevant settings noted for each provider, since these change often enough that a comparison from July 2026 may not hold in a few months.
