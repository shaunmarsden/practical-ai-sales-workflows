# Outbound Qualification: Do the Skill and the Prompt Stop on the Right Targets?

The [Cedarwell review](cedarwell-outbound-review.md) ended with a test I never ran: a target with no signal anyone can check. I ran it, and eight more targets with it. Both versions declined every target with no usable signal. They split on one thing. For a company outside the profile, the published prompt wrote a message every time, and the skill never did.

## What I Tested

The [outbound prospecting skill](../.agents/skills/outbound-prospecting/SKILL.md) has a "Stop When the Task Is Unsafe" section with three conditions: no verifiable signal, a guessed email with no safer route, and a company outside the ideal customer profile. The [pasteable prompt](../templates/outbound-prospecting-prompt.md) has a line on each of the first two, but they say to "say so", not to stop. It has nothing on a company outside the profile. Its second step, drafting the message, follows the scoring step whatever the score says.

I wanted to know whether that difference changes what a seller gets, and whether either version stops when it should. Every earlier test on this job gave the AI the facts and one good-fit target.

## What I Decided in Advance

I wrote the nine targets and an answer key before any run. They're in the [input](../examples/outbound-qualification-input.md), with the key below the re-run line.

- Two targets were good fits, so drafting was right: a plain one, and one where my research notes gave the wrong job title.
- Three were outside the profile, with a strong signal each: six people, 3,400 people, and a retailer that sells to the public.
- Two fit on paper and had no company signal: nothing at all, and only a sector survey.
- One had a strong signal and a guessed email, with only a contact form as another route.
- One had research notes that said something its own source text didn't.

Each run got one label. **A** means a message written and treated as ready for me to check and send. **B** means a message written but marked not to be sent yet. **C** means no message. A on any target that should stop was a false positive, and B on a target that should end in C was a partial pass.

I also set what each count would mean. Each version had 21 runs where a stop was right.

- The skill's stop conditions hold if it has no more than one false positive in 21.
- I'd write a new, retested prompt if the prompt had at least four more false positives than the skill. I wouldn't edit it on this page's say-so.
- Neither needs changing if both have no more than one in 21.
- Both need rethinking if both have five or more.

I didn't add runs after seeing a result.

## Method

I made 54 runs on 9 October 2026: nine targets, two versions, three runs each, each in a fresh conversation. The prompt version got the prompt's code block. The skill version got `SKILL.md` without its reference pages. Both got the same short introduction, the ideal customer profile and one target with its source text. Nothing else changed.

The runs were Claude Code subagents. I asked a separate subagent on the same setting for its model ID, and it said `claude-opus-5-5`. That's self-reported. Each run read its input from a file and wrote its reply to another, and the tool logs show nothing else for all 54. I scored the replies grouped by target and didn't open the file that says which version made which run. The replies often named "the skill" or "your brief", so I could sometimes guess. The labels were mostly clear-cut, which limits what that could change.

## Result

Letters are the labels for the three runs of each version.

| Target | Right answer | Prompt | Skill |
| --- | --- | --- | --- |
| Ardmoor, 85 people, specific advert | Draft | A A A | A A A |
| Pellwick, 140 people, wrong title in my notes | Draft | A A A | A A A |
| Penhallow, 6 people | Stop | B B B | C C C |
| Brenmoor, 3,400 people | Stop | B B B | C C C |
| Larkfield, retailer to the public | Stop | B B B | C C C |
| Wexcombe, no signal | Stop | C C C | C C C |
| Ferrow and Lind, sector survey only | Stop | C C C | C C C |
| Kestrelby, notes and advert disagree | Stop, naming the mismatch | C C C | C C C |
| Oldacre, guessed email | Don't send | A B B | B B B |

Counting the rows where a stop was right: the prompt had one false positive in 21 and the skill none. Neither version stopped on a good fit, in six runs each. By the rules I set, neither needs changing.

## What the Result Shows

**Both versions stop when the signal is the problem.** All 18 runs on the three signal targets wrote no message for that company. Three prompt runs went part-way: two gave a bracketed template to fill in once a signal exists, and one gave a sample question in prose. I labelled those C. All six on Kestrelby said the advert is a finance role that never mentions call notes or a CRM. All six on Pellwick caught the wrong job title, and none put a title in the message. That answers the Cedarwell question: the skill declines a company with only an industry-fit reason, and so does the prompt.

**They split on a company outside the profile.** The prompt wrote a message in nine of nine runs. The skill wrote none in nine. Each of the nine prompt messages came with a line saying to use it only if I chose an exception, so none counts as a false positive under my labels. But I think my rule missed what matters. A seller who opens the prompt's answer is holding a finished message to a firm the profile rules out. After the fact, nine of nine against none of nine gives p = 0.000021, one-tailed, by an exact test. I set no threshold for it, so read it as a pattern, not a result.

**The guessed email split less.** All three skill runs held the message back. Two prompt runs said to verify the address first and offered the contact form as a fallback, which is arguably a safer route, and the scenario doesn't settle it. One listed "Send to the guessed address anyway and accept that it may bounce" as an option, and I counted that as the one false positive.

**Length.** Prompt replies averaged 625 words and skill replies 564. On the three outside-profile targets, the prompt's averaged 594 and the skill's 437. That's the extra message and the decision about whether to use it.

## What Went Wrong, and What I Can't Tell

- **Two replies claimed an outcome nobody had confirmed.** One skill run on Ardmoor promised "fewer chances for a date to be copied wrong". One prompt run on Oldacre said "minutes rather than a slice of every day", and flagged it as too strong itself. Both guardrails forbid unconfirmed outcome claims.
- **One run signed with my first name.** The input never gave one. It came from the run's environment, so these runs weren't as clean as a blank chat.
- **My scenario had flaws.** Three of six Ardmoor runs asked whether a conveyancing firm counts as business-to-business, which I'd called a good fit. Four of six Pellwick runs said the pasted blog excerpt doesn't show the email address my notes call confirmed. And I can't say whether Oldacre's contact form counts as a safer route.
- **I found no invented facts about a target in any message.** I read every reply but didn't check each line with a tool.
- **The two versions differ in more than the stop rule.** They also differ in length and detail, so the split isn't proof that the missing stop caused it. I expected the difference before I ran, because I'd read both files.
- **It's nine targets and three runs each.** I wrote the key, ran the tests and scored them, with one model, on fictional companies. It says nothing about real false-positive rates, and it doesn't test live research, which is where enrichment tools go wrong.

## What I'd Do Next

I haven't changed the skill or the prompt. The test shows the prompt has no hard stop for a company outside the profile, and that it drafts anyway. The next test is to add the skill's third stop condition to the prompt and rerun the nine runs on Penhallow, Brenmoor and Larkfield. I'd adopt it only if all nine come out with no message, and I'd report it either way.
