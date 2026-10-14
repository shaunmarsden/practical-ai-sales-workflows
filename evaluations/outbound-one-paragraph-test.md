# Outbound Prospecting: Can One Paragraph Do What the Skill Does?

The [outbound prospecting skill](../.agents/skills/outbound-prospecting/SKILL.md) is about 1,200 words, with two reference pages. I wanted to know how much of what it does for a seller is just its stop rules. I wrote a 250-word paragraph with the same rules and ran it on the nine targets from the [qualification stop test](outbound-qualification-stop-test.md). It kept every stop the skill has, and never wrote a message it shouldn't have. It held back from one good-fit target the skill drafted for, so by the readings I set, it was a partial match.

## What I Tested

The paragraph is below. I wrote it from the skill, knowing the skill's rules. It scores the target on fit, contact and signal, checks my notes against the source text, lists the three stops, and says what a message must and mustn't do. It leaves out the structure detail and the reference pages.

```text
I want to decide whether to approach one company and, if it is worth it, write a first cold message to it. Score the target on three things: whether it fits my ideal customer profile, whether there is a named contact with plausible authority over this kind of decision, and whether there is a specific public signal, backed by the source text I give you, that points to a real manual-admin problem rather than a generic industry trend. Check my research notes against the source text and tell me if they disagree. Do not write a message, and say why, if there is no verifiable public signal and the message would need a generic or invented hook, if the contact's email address is an unverified guess and there is no safer route, or if the company does not fit the ideal customer profile, however easy the guess is to make. Otherwise write a short message with a lowercase subject line that does not name the offer, an opener that asks a question tied to the signal and the contact's role, a small offer that is useful on its own, one sentence on what it is worth to them, and a reply as the next step rather than a meeting. Never claim a capability, statistic or outcome that has not been confirmed, never imply they are already interested, never invent scarcity or a deadline, and use no em dashes or emojis. I will do any sending and any CRM update myself.
```

The question is whether the skill's extra length buys anything on this job.

## What I Decided in Advance

I wrote the readings before any run. Each run got one label, as in the qualification test: **A** is a message written and treated as ready for me to check and send, **B** is a message written but marked not to be sent yet, and **C** is no message.

The paragraph matches the skill on stops if all five hold:

- At least 8 of the 9 runs outside the profile (a six-person firm, a 3,400-person firm and a retailer) are C.
- At most 1 of the 21 runs where a stop is right is an A.
- At least 5 of the 6 runs on the two good fits are A.
- At least 2 of the 3 Kestrelby runs say the advert doesn't contain what my notes claim.
- At least 2 of the 3 Pellwick runs flag that my notes and the byline give different job titles.

It's worse if 3 or more outside-profile runs write a message, or 2 or more of the 21 should-stop runs are an A. Anything between is partial, and I report the counts. For the messages, I'd count a breach of a skill guardrail in each one I read: an em dash, a meeting as the main ask, an unconfirmed claim, invented scarcity, assumed interest, or a fact not in the inputs. The paragraph would be worse if it had three or more breaches than the skill.

## Method

I made 27 paragraph runs on 14 October 2026, three on each of the nine targets, in fresh conversations. The input was the paragraph followed by the same block of profile, notes and source text the skill runs had. Each run got the same instruction: reply to the message as if it had been sent in a chat, with one file written. I used the setting that reports itself as `claude-opus-5-5`, which is self-reported.

For the skill I reused the 27 runs from the [rerun](outbound-qualification-stop-test.md#rerun-without-the-evaluation-paragraph) made earlier that day: the whole `SKILL.md` without its closing evaluation paragraph, on the same targets and setting. I didn't run both arms in one batch. I scored by reading each reply, and I could usually tell which arm it came from.

## Result

| | Paragraph | Skill |
| --- | ---: | ---: |
| Outside the profile, no message (of 9) | 9 | 9 |
| A on a target where a stop is right (of 21) | 0 | 0 |
| Good fits drafted (of 6) | 4 | 6 |
| Kestrelby: advert doesn't match my notes (of 3) | 3 | 3 |
| Pellwick: title mismatch flagged (of 3) | 3 | 3 |
| Mean words per reply | 506 | 550 |

Every condition was met except one: good fits drafted, 4 of 6 against my 5, so the result is partial.

## What the Result Shows

**The stops are the paragraph's strength.** It declined all nine outside-profile targets, wrote nothing for the two with no usable signal, and caught the Kestrelby mismatch and the wrong job title every time. A one-paragraph prompt with these rules did what the skill did on all of that.

**It held back on Ardmoor.** Two of its three Ardmoor runs wrote no message, because nothing in my notes says a conveyancing firm's clients are businesses. The skill drafted all three and raised the same doubt as a check before sending. That doubt is a flaw in my scenario, which I'd called a good fit, and [earlier runs raised it too](outbound-qualification-stop-test.md#what-went-wrong-and-what-i-cant-tell). It shows the paragraph treating "not shown" as a stop where the skill treated it as "check first". For a stop rule, that's the safer direction to err in.

**Oldacre split the other way.** The paragraph wrote no message in all three runs on the guessed email. The skill wrote a draft and marked it not to be sent to that address, in all three. I think either answer is defensible.

**The messages were clean.** I read the 4 messages the paragraph wrote and the 9 the skill wrote, and found no breach in either set. Two skill drafts add up 1.5 days a month into 18 working days a year from his own figure. I counted that as arithmetic, not a claim.

## What Went Wrong, and What I Can't Tell

- **I wrote the paragraph knowing the skill's rules.** A paragraph written without that knowledge might have left a stop out.
- **The skill arm wasn't run in the same batch.** It was the same day, setting, targets and instruction, but not interleaved.
- **The skill arm still had the skill's opening note** that the file is an instruction sheet an AI follows. The paragraph arm didn't. It says nothing about tests.
- **Four against six good-fit drafts is a small gap** at three runs a target, and it's mostly one target. I'd say the paragraph is at least as cautious as the skill. I wouldn't say it's as helpful.
- **I didn't run a one-sentence floor.** The earlier prompt, without the profile stop, wrote a message for all nine outside-profile runs, so I know a version with no stops fails.
- **I didn't check the tool logs this time.** The earlier batches had one read and one write each.
- **One model, fictional companies, nine targets I wrote.** It says nothing about live research.

## What I'd Do Next

I haven't changed the skill or the prompt. The [pasteable prompt](../templates/outbound-prospecting-prompt.md) already has the same stops, tested in the [prompt stop test](outbound-prospecting-prompt-stop-test.md). I haven't compared it with this paragraph. The next thing worth trying is the same test on a skill where the stops aren't the main value, since this skill is the one where I'd expect the paragraph to do best.
