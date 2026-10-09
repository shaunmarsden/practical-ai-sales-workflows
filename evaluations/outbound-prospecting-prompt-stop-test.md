# Giving the Outbound Prompt Two Stops: A Three-Step Test

The [qualification stop test](outbound-qualification-stop-test.md) found that the published prompt wrote a message for every company outside the profile, and the skill wrote none. I added the skill's missing stop to the prompt and tested it. My first version fell short of the rule I'd set, my second fixed both stops and over-stopped on one target, and a third check on clean good fits passed. The prompt now has both stops.

## What I Changed

Two edits to [the prompt](../templates/outbound-prospecting-prompt.md), both mirroring a stop the [skill](../.agents/skills/outbound-prospecting/SKILL.md) already has.

- **The profile stop**, added after the "Score it down" paragraph: "If the target doesn't fit the ideal customer profile I gave you, say so and stop. Don't draft a message, however strong the signal is."
- **The email rule**, reworded in place. It used to say to say so if the address is a guess. It now adds "and don't treat the message as ready to send until the address has been checked".

I tested them in two steps. Version A had the profile stop alone. Version B had both.

## What I Decided in Advance

Same nine targets, labels and key as the qualification test. Each version got 27 runs, three per target, in fresh conversations. I wrote each version's rule before its runs.

**Version A** would be adopted only if all of these held:

- all nine runs on the three outside-profile targets wrote no message;
- at most one of six runs on the two good fits wasn't a draft;
- at most one of twelve runs on the other four targets was a draft recommended for sending.

**Version B** would be adopted only if all of these held:

- the same outside-profile result;
- at most one of six not a draft on the two good fits;
- no draft recommended for sending on the three no-signal or mismatch targets;
- no draft recommended for sending on the guessed-email target.

I added no runs to either version after seeing its result. The third check below is a new test, and I say so.

## Result

| | Old prompt | Version A | Version B |
| --- | ---: | ---: | ---: |
| Outside the profile, runs with no message, of 9 | **0** | **9** | **9** |
| No-signal, trend and mismatch targets, drafts, of 9 | 0 | 0 | 0 |
| Guessed email, drafts recommended for sending, of 3 | 1 | 2 | 0 |
| Good fits not drafted, of 6 | 0 | 1 | 3 |

The old column is the published prompt's 27 runs from the earlier test, made the same day.

**Version A failed my rule.** It fixed the outside-profile case. But two of its three guessed-email runs treated the draft as ready to send, against my limit of one in twelve across the other targets. The sentence doesn't touch that case. The old prompt had one in three, so this may be ordinary variation, but the rule was the rule, so I didn't adopt it.

**Version B failed my rule on the good fits.** Both stops worked. All nine outside-profile runs wrote no message. None of the three guessed-email runs treated the draft as ready to send. All nine no-signal and mismatch runs stopped, and the three Kestrelby runs named the mismatch. But on Ardmoor, a conveyancing firm, none of the three runs recommended a draft. Two stopped, one held the message back, and each said nothing in my notes shows Ardmoor serves businesses. Pellwick was drafted in all three runs.

## The Check on Clean Good Fits

My notes never say Ardmoor serves businesses, and three of six runs of the old prompt and the skill raised the same doubt. So I judged Ardmoor a flawed good fit, not a clean over-stop. I won't call that a pass, since the rule failed as written. I wrote two new targets that are unambiguously business-to-business and fit the profile on every line, with a specific advert and a confirmed email: a 90-person equipment finance firm and a 60-person architecture practice. I decided beforehand that I'd adopt Version B only if at most one of six runs wasn't a draft.

**All six were drafts.** Version B adopted. I wrote those two targets after seeing the Ardmoor result, so they're a response to a failure, not an independent test. They're easy fits, and they say little about borderline ones.

## What Went Wrong, and What I Can't Tell

- **I ran three versions and adopted the one that passed.** That flatters it. Version A's result and Version B's Ardmoor result are the other side of the same record.
- **On a borderline fit, the new prompt stops.** On Ardmoor it did so in three of three runs. I think that's right, since the profile says business-to-business and my notes didn't show it. A seller who disagrees should put the evidence in the notes or widen the profile.
- **The guessed-email result is small.** Three runs on one target. Contact forms are still offered as a fallback in the replies, and the scenario doesn't say whether a form counts as a safer route.
- **One model, fictional companies, a key I wrote**, and I scored the runs. The replies named the stop they were following, so I could usually tell which version I was reading. Which version produced a run didn't change what counted as a draft.
- **It doesn't test live research.** All three versions got the facts in the prompt.
- **I haven't changed the skill.** It already had both stops.

## What the Prompt Does Now

The recipe card for [Find the Next Prospect](../recipes/find-the-next-prospect.md) carries the same text, rebuilt from the prompt. The sales repository's own rule is that a prompt changes only with a new test, and this page is that test.
