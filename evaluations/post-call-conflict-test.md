# Post-Call Evidence: Does the Skill Matter When the Sources Disagree?

The [post-call one-paragraph test](post-call-one-paragraph-test.md) found that a short plain call needed no instructions at all. I'd said the skill's structure might matter when a call, a CRM record and an email thread disagree, because the skill has a source order and a `conflict` label for that case. So I built a call with five disagreements planted in it and ran the skill, a 250-word paragraph and the bare request, twelve times each. Every one of the 36 replies passed all seven of my measures. The test couldn't separate them.

## What I Tested

I wrote a fictional [27-minute call, a CRM record and a two-message email thread](../examples/brackenridge-conflicting-sources-input.md) for a freight company. The call contradicts the other two sources in four places:

- **Close date.** The CRM says 30 November. On the call, anything over £25,000 goes to a board that meets on 14 January.
- **Decision maker.** The CRM names a finance director who left in September.
- **Budget.** The CRM says confirmed at £45,000. On the call there's no budget line and a guess of £30,000 to £40,000.
- **Volume data.** An email promised it by 9 October. On the call it hasn't been pulled.

It also holds a second-hand remark ("finance would not object") and two conditional offers, an introduction and a November pilot.

The three versions:

- **Skill:** the published `SKILL.md`, with its two closing pointer paragraphs removed.
- **Paragraph:** the paragraph below, which I wrote from the skill. Unlike the one in the [last test](post-call-one-paragraph-test.md), it carries the skill's source order and its rule to treat the CRM as possibly stale.

```text
Analyse the call transcript, CRM record and emails I give you and turn them into an evidence pack I can check before I use it. Label each finding as confirmed (directly supported by what I gave you), estimate (a number presented as approximate), second-hand, inference or unknown, and label a conflict where two sources disagree. When sources differ, trust them in this order: what was said on this call, then written commitments in current emails, then the CRM record, which you should treat as possibly stale, then earlier notes. Show me the disagreement instead of quietly choosing the convenient version, and mark CRM information as potentially stale where the call differs. Never upgrade an estimate, second-hand comment or inference into a confirmed fact. Preserve conditional wording such as "should", "subject to approval" and "I need to check", and do not treat a discussed next step as agreed unless the evidence shows agreement. Never invent a meeting, deadline, budget, authority, urgency or commitment. Record each commitment with its owner, action, timing and conditions. Separate real buying signals from polite interest, capture concerns without guessing what sits behind them, and list what is missing. Propose one sensible next action. Give me a short summary, the actions, a draft follow-up email and suggested CRM updates, all as drafts for me to review. Do not claim to send anything or change the CRM. If the sources are too incomplete to support a conclusion, say so and ask for the minimum extra information. End with what I must check before using this. No em dashes or emojis.
```
- **Task line only:** the request and the three sources, with no instructions.

Every version got the same request: "Here is the transcript from my call with Brackenridge Freight Services today, our CRM record for them, and an email thread from earlier this month. The company and the people are fictional. Please produce the call summary, the next actions, a draft follow-up email and suggested CRM updates."

## What I Decided in Advance

Seven pass-or-fail measures, scored by reading each whole reply:

1. The reply says the CRM's 30 November conflicts with the call, and doesn't present it as current.
2. It says the named finance director left, and shows the acting lead's sign-off as unconfirmed.
3. It doesn't present the budget as confirmed, and shows the conflict.
4. It notes the 9 October promise wasn't kept, and shows the new timing as conditional.
5. It shows "finance would not object" as second-hand.
6. It shows the introduction and the November pilot as conditional.
7. The draft email and suggested CRM updates don't rely on the stale or unconfirmed items.

The paragraph matches the skill if the means are within 0.5 and no measure differs by four runs of twelve. If the task line alone came within 0.5 of the paragraph, I'd say the instructions added little even here. I added no runs, and I'd rerun an unusable reply once.

## Method

I made 36 runs on 15 October 2026, six on each of two model settings per version, in fresh conversations. The settings report themselves as `claude-opus-5-5` and `claude-haiku-5-5`, which is self-reported. Each run read its input from a file and wrote its reply to another. I scored by reading and could usually tell which version a reply came from. The published example uses the £ sign to meet this repository's style check. The runs saw the figures written in words and as "pounds", and nothing else differs.

## Result

| | Skill | Paragraph | Task line only |
| --- | ---: | ---: | ---: |
| Usable replies, of 12 | 12 | 12 | 12 |
| Measures passed, of 7, in every reply | 7 | 7 | 7 |
| Mean words a reply | 1,813 | 2,204 | 1,157 |

By my readings, **the paragraph matches the skill**, and **the task line alone is within 0.5 of the paragraph**. The instructions added nothing these measures could see, even with five planted disagreements.

## What the Result Shows

**Both models caught every disagreement without being told how.** Each reply put the call above the CRM record, called the record out of date in the right places and kept the second-hand and conditional points apart from the facts. The bare request did this as well as the skill.

**The structure showed in length, not in catching.** The paragraph's replies were about 2,200 words and the skill's about 1,800, against 1,150 for the bare request. All the extra words were labelled tables and evidence lists. They make a reply easier to check line by line and slower to read.

**One small difference outside my measures.** Two of the twelve bare-request replies proposed a specific January date for the CRM close date, 31 January 2027 and "end of January". None of the paragraph's replies did. They said to clear the field or choose a date yourself. One skill reply suggested 14 January 2027, the earliest board date, with a note that it wasn't agreed. I hadn't set this as a measure, and two replies of twelve is a pointer, not a result.

## What Went Wrong, and What I Can't Tell

- **The test sat at the ceiling.** Nothing separated the three versions, so it can't say whether the skill adds anything on a harder case. Each disagreement was stated plainly in a source. A harder case might make the AI infer a conflict across three sources, or bury one in a much longer input.
- **I wrote the paragraph knowing the skill and the planted disagreements,** and put the source-order sentences into it because I knew they mattered here.
- **One first reply declined** (a bare-request reply on the smaller model), saying the chat was for my repository. I reran it once and the rerun was usable. In the [previous test](post-call-one-paragraph-test.md) seven declined when I'd removed the word "fictional". Here I kept it in the request, which may be why only one did. I didn't test that.
- **One scenario, scored by me, not blind,** with seven measures I chose.
- **The skill arm lacked its output-schema page,** as when a seller pastes the file.
- **I didn't inspect the tool logs.**

## What I'd Do Next

I haven't changed the skill or the prompt. I'd stop testing paragraphs against this skill. Three tests on three skills have now found a short paragraph, or on two of them the bare request, doing as well as the full skill on what I measured. The honest next step is a short page saying where that held and where it didn't, with the limits. That's a claim about the skills in this repository, so I'd want to write it deliberately and not as a footnote to a test page.
