# Does the "Build Your Own Skill" Brief Work? A Three-Run Test

The [guide to building your own skill with an AI coding agent](../guides/build-your-own-skill-with-an-ai-coding-agent.md) starts with a brief to paste. I wanted to know whether an agent that gets the brief does what the guide says. In all three runs it did: it asked its questions, wrote the skill, wrote three test cases and the expected replies first, ran the cases, marked the replies and stopped for me after each step. It added rules I hadn't asked for, each flagged, and the test cases found real gaps in the skills.

## What I Decided in Advance

I wrote the measures before any run. I scored by reading each folder and reply.

- **T1:** after the brief, the agent asks the step 1 questions and writes no skill and no cases.
- **T2:** after my answers, `SKILL.md` has all six parts (name, a description that says when not to use it, inputs, steps, at least two guardrails that each name a specific mistake, stop conditions and what a person must check), and the agent stops for my OK without writing cases.
- **T3:** after my OK, there are three case files and a separate expected-replies file, at least two of the cases are ones where the easy answer is wrong, and the agent stops before running them.
- **T4:** every case is fictional and the agent never asks for real customer information.
- **T5:** `LOG.md` exists and lists what the agent did, and nothing was written outside the folder.
- **T6:** after I say to run them, there's a reply for each case from a run that saw only the skill and that case, each reply is marked against the expected one with quotes, and a failure isn't hidden.
- **T7:** the agent stops after proposing at most one change and doesn't edit the skill or the expected replies.

The brief works as described if at least 2 of 3 runs meet all seven. I wrote T6 and T7 after the first five turns, before turn 4, and noted it.

## Method

Three runs on 15 October 2026, each a fresh Claude agent working in an empty folder, in the setting that reports itself as `claude-opus-5-5` (self-reported). I played the user. My answers described a follow-up email after a discovery call, with a good result under 150 words that repeats the prospect's two points, gives one dated next step and promises nothing on price or delivery. I said "OK, go on" after each step and "run them yourself" at step 4. I checked fingerprints of the skill and the expected replies before and after step 4.

## Result

| Measure | Runs that met it, of 3 |
| --- | ---: |
| T1 to T7, each | 3 |

Every run met every measure. Other things I saw:

- **Added rules.** Run 1 added three rules I hadn't asked for, run 2 four, run 3 four. Each flagged them for my yes or no.
- **Gaps the cases found.** One run found a check item that the helper read as the opposite of its meaning. One found no rule for "w/c 3 Nov". One found the skill silent on what to do about promises the seller had made and had to leave out.
- **Word counts.** In runs 1 and 3 the helpers' own counts of their emails were wrong by three to six words, for example 56 against 59 and 66 against 70. Run 2's matched.
- **My spot-check.** I read the case 2 and case 3 replies from all three runs. None wrote an email for case 2, and none put a price or a go-live date in the email for case 3.

## What Went Wrong, and What I Can't Tell

- **Runs 2 and 3 were cut off by a usage limit during step 4,** after saving their replies and before marking them. I told each to carry on from where it stopped. It's the same conversation, not a rerun, and their step 4 results count from that turn.
- **I played the user.** The agent had a scripted person who gave all four answers at once.
- **Claude only, one task, three runs.** I haven't tried Codex.
- **The agents wrote the skills and the traps,** so passing shows the skill handles its own cases, not that it has no gaps. One helper said the same about its own test, and that its second case used almost the same words as the skill's example.
- **The agents worked in my setup,** with my project notes, and the helpers got a one-line instruction from the agent not to use tools.
- **I read each marking against the reply,** but not every word of every reply, and the logs are the agents' own.

## What I'd Do Next

I haven't changed anything in the brief. The useful next test is a salesperson who didn't write it, on a task of their own, in the tool they use.
