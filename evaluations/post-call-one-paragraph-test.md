# Post-Call Evidence: Can One Paragraph Do What the Skill Does?

The [outbound one-paragraph test](outbound-one-paragraph-test.md) was on a skill whose value is mostly its stop rules. I wanted to know what happens on a job that is mostly structure and labels. The [extract post call evidence skill](../.agents/skills/extract-post-call-evidence/SKILL.md) labels each finding as confirmed, an estimate, second-hand, an inference or unknown, and keeps conditional wording conditional. I ran it, a 200-word paragraph of my own and a one-line request against the Hartwell call transcript. By the readings I set, the paragraph matched the skill. So did the one-line request, which is the finding I didn't expect. Six of the seven things I checked were passed by every reply that wasn't a refusal. The seventh was giving Alex a gender the transcript never gives, and none of the three versions prevented it.

## What I Tested

Three versions, twelve runs each, six on each of two model settings:

- **Skill:** the published `SKILL.md`, with its two closing paragraphs removed. They point to a scored evaluation and describe a failure on a similar case, which is the cue I [now strip in every arm](../CONTRIBUTING.md). The page it tells the AI to read for its output schema wasn't supplied, as when a seller pastes the file.
- **Paragraph:** the paragraph below, which I wrote from the skill's labels, guardrails, stop condition and review line.
- **Task line only:** just the request.

```text
Analyse the call transcript I give you and turn it into an evidence pack I can check before I use it. Label each finding as confirmed (directly supported by what I gave you), estimate (a number presented as approximate), second-hand, inference or unknown, and flag any conflict between sources. Never upgrade an estimate, second-hand comment or inference into a confirmed fact. Preserve conditional wording such as "should", "subject to approval" and "I need to check", and do not treat a discussed next step as agreed unless the transcript shows agreement. Never invent a meeting, deadline, budget, authority, urgency or commitment. Record each commitment with its owner, action, timing and conditions. Separate real buying signals from polite interest, capture concerns without guessing what sits behind them, and list what is missing. Propose one sensible next action. Give me a short summary, the actions, a draft follow-up email and suggested CRM updates, all as drafts for me to review. Do not claim to send anything or change the CRM. If the transcript is too incomplete to support a conclusion, say so and ask for the minimum extra information. End with what I must check before using this. No em dashes or emojis.
```

All three got the same request: "Here is the transcript from my call with Hartwell. Please produce the call summary, the next actions, a draft follow-up email and suggested CRM updates." The input was the [Hartwell post-call transcript](../examples/hartwell-post-call-transcript.md), with the line saying it was made to test a workflow removed and "Fictional" taken out of the title.

## What I Decided in Advance

I wrote seven pass-or-fail measures before any run, from the test points the [post-call review](hartwell-post-call-review.md) lists:

1. The 15 to 30 minute admin time is shown as an estimate.
2. Alex's anonymised transcript is shown as conditional on an internal check.
3. The Tuesday meeting is shown as proposed, not confirmed.
4. Alex gets no gender, since the transcript gives none. Priya is "she" in the transcript, so that's allowed.
5. No calendar date is invented from "Thursday", "Tuesday" or "today".
6. No pricing, purchase or implementation commitment is recorded as agreed.
7. The meeting tool's package, and whether it gives full transcripts, is shown as unchecked.

I scored each reply by reading it, from 0 to 7. The paragraph matches the skill if its mean is within 0.5 of the skill's and no measure differs by four or more runs of twelve. If the task line alone came within 0.5 of the paragraph, I'd say the instructions added little on this job. I added no runs, and I'd rerun an unusable reply once.

## Method

I made 36 runs on 15 October 2026, in fresh conversations, on the settings that report themselves as `claude-opus-5-5` and `claude-haiku-5-5`. Both are self-reported. Each run read its input from a file and wrote its reply to another. I scored by reading and could usually tell which version a reply came from.

## Result

| | Skill | Paragraph | Task line only |
| --- | ---: | ---: | ---: |
| Usable replies, of 12 | 11 | 12 | 10 |
| Gave Alex a gender | 3 | 6 | 1 |
| Mean score, of 7 | 6.73 | 6.50 | 6.90 |
| Mean words a reply | 1,310 | 1,803 | 972 |

Measures 1, 2, 3, 5, 6 and 7 passed in every usable reply of every version. Measure 4 was the only one that separated them. By model, the failures on measure 4 were:

| | Skill | Paragraph | Task line only |
| --- | ---: | ---: | ---: |
| Opus | 1 of 6 | 1 of 6 | 0 of 6 |
| Haiku | 2 of 5 | 5 of 6 | 1 of 4 |

By my readings, **the paragraph matches the skill**. Its mean is 0.23 below, and the biggest gap on one measure, six of twelve against three of eleven, is under four runs. And **the task line alone is within 0.5 of the paragraph**, at 0.40 above it. So on this job the instructions added little that these measures could see.

## What the Result Shows

**All three versions kept the evidence straight.** Every usable reply called the admin time an estimate, kept the transcript conditional, left the Tuesday time open and marked the meeting tool as unchecked. Without any instruction, the task line alone did the same. Both models are already careful with a short, plain transcript.

**The gender slip is the one failure, and the instructions didn't stop it.** The [post-call review](hartwell-post-call-review.md) records that one published output made the same slip. Neither the skill nor my paragraph says anything about pronouns, and neither helped. Haiku with the paragraph did worst, in five of six runs. Its replies were the longest, which gives more room to slip, but I didn't test that.

**The paragraph made the longest replies.** About 1,800 words against 1,300 for the skill and 970 for the task line. A reader checking the output has more to read for no gain on these measures.

## What Went Wrong, and What I Can't Tell

- **Seven first replies declined, and three declined again.** They said the chat was for my repository and that the call was live account work, and pointed to a skill in my own tools. The runs had my project notes, which say that, and I'd removed the word "fictional", so the call looked real. I reran each once, as I'd set out. Four then produced a reply. Skill 1 and task line only 2 still declined and aren't scored, which is why the counts differ. The paragraph arm never declined, I think because it says what job to do.
- **Most of the measures were at the ceiling.** Six of seven were passed every time, so the test could show a difference on only one.
- **I wrote the paragraph knowing the skill, and chose the measures knowing the transcript's test points.** The skill was also built on this transcript.
- **One transcript, one job.** Hartwell is the call the skill was written for. A messy, long or contradictory call is where I'd expect the skill's structure to matter, and I didn't test one.
- **The skill arm lacked its output-schema page.** A seller who pastes the file doesn't have it either.
- **One rerun made five tool calls, not three.** I didn't inspect the logs.
- **Scored by reading, not blind.**

## What I'd Do Next

I haven't changed the skill or the prompt. The useful next test is one on a long call with a real conflict in it, such as a CRM record that disagrees with what was said. The skill has a rule for that, and a short transcript can't show whether a paragraph would catch it.
