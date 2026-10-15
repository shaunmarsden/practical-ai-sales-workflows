# Do the Skills Need Their Length? What the Tests Found

I've tested the skills in this repository against much shorter versions of themselves. On most of what I measured, a short paragraph did as well as the full skill, and on some of it so did the bare request. Where the instructions mattered, it was one rule at a time: a stop, a guardrail or a required step that names a specific mistake the AI doesn't avoid on its own. This page pulls the tests together and says what they can't tell me. It adds no new runs.

## What I Compared

The short version is a paragraph I wrote from the skill. It has the same labels, guardrails and stop conditions, in a few hundred words, with no structure and no reference pages. So the result isn't that a seller could write the paragraph. I wrote it with the skill open. The result is that, for these measures, the skill's length wasn't what did the work.

## The Four Tests

| Test | Job | Versions | What I found |
| --- | --- | --- | --- |
| [Outbound qualification](outbound-qualification-stop-test.md) and [one paragraph](outbound-one-paragraph-test.md) | Choosing an outbound target and deciding whether to draft | Skill, prompt, 250-word paragraph | The prompt had no stop for a company outside the profile and wrote a message for 9 of 9 such targets. The skill wrote none. The paragraph, which carried the stop, wrote none. It held back on 2 of 3 runs on one good fit that the skill drafted for. |
| [Post-call evidence, short call](post-call-one-paragraph-test.md) | Turning a call into an evidence pack | Skill, 200-word paragraph, bare request | Six of seven measures were passed by every usable reply of every version. The seventh, giving Alex a gender the transcript doesn't, failed in 3 of 11 skill replies, 6 of 12 paragraph replies and 1 of 10 bare-request replies. |
| [Post-call evidence, conflicting sources](post-call-conflict-test.md) | The same, with a CRM record and emails that disagree with the call | Skill, 250-word paragraph, bare request | All 36 replies passed all seven measures. |
| Career pivot, [three rounds](https://github.com/shaunmarsden/commercial-career-pivot-workbench/blob/main/evaluations/one-prompt-comparison.md) in [another repository](https://github.com/shaunmarsden/commercial-career-pivot-workbench) | Planning a move into a new commercial role | One-line prompt, careful paragraph, full workflow | The careful paragraph gave no unsourced pay or demand figures, and neither did the workflow. On planted CV problems, without a cue in the input, the three flagged 61, 67 and 68 of 72. The workflow flagged a skill the CV only lists, and its replies were about three times as long. |

## Where Instructions Did Make a Difference

Each of these is a specific rule, and the version without it failed:

- **A stop for a company outside the profile.** The prompt without it wrote a message for 9 of 9 such targets, and the skill with it wrote none. See the [qualification test](outbound-qualification-stop-test.md).
- **A guardrail against stacking two unmeasured figures into a pound total.** None of ten skill runs with it produced the total, against 4 of 9 without it. The prompt, which lacked the line, produced it in 9 of 12. See the [stacked figure test](business-case-stacked-figure-test.md) and the [padding test](business-case-padding-test.md).
- **A required step that lists dated commitments before drafting.** It was 6 of 6 against 0 of 6 on stating a date clash the skill kept missing. See the [skill ledger test](chase-skill-ledger-test.md).
- **Asking for pay figures.** The bare one-line prompt gave them, labelled as unchecked estimates. The careful paragraph and the workflow gave none. See the [career pivot comparison](https://github.com/shaunmarsden/commercial-career-pivot-workbench/blob/main/evaluations/one-prompt-comparison.md).

In all four, the useful line names a mistake the model makes by default and says what to do instead.

## Where They Didn't

Labelling a finding as confirmed, estimated or second-hand, keeping "should" and "subject to approval" conditional, putting the call above a stale CRM record, and catching problems planted in a CV: the bare request did these about as well as the skill. Both model settings I used are already careful on a short, plain task.

The one thing that separated the post-call versions was the gender slip, and nothing in the skill or the paragraph mentions it. Haiku with the paragraph did worst, 5 of 6. That's the other half of the pattern: a rule you haven't written can't help.

## What the Length Cost

The replies to the longer versions were longer. In the post-call tests the skill's ran to about 1,300 to 1,800 words and the paragraph's to 1,800 to 2,200, against 970 to 1,150 for the bare request. In the career pivot tests, the workflow's replies ran to about three times the length of a plain prompt's. The extra words were labelled tables and evidence lists, which are easier to check line by line and slower to read. In a [reader test](https://github.com/shaunmarsden/commercial-career-pivot-workbench/blob/main/evaluations/reader-test.md), a reply cut the unsupported details a reader carried into a CV summary from 2.0 to between 0.7 and 1.0, but the workflow's long reply did no better than a one-line prompt's.

## What I Can't Tell

- **I wrote every short version knowing the skill and the test.** A paragraph written cold might leave a rule out.
- **Most of these tests sat at or near the ceiling.** When every version passes, the test can't say whether the skill helps on a harder case.
- **Each test is one scenario, scored by me.** I wrote the scenarios and the measures, and I could usually tell which version a reply came from.
- **They are fictional companies on two model settings.** The runs ran inside a coding tool with my project notes, and the model names are self-reported.
- **I didn't measure what a skill is for.** A skill saves you retyping the process, carries rules for rarer mistakes than I tested, and hands the same method to someone who wouldn't think to ask for it. I tested whether it improved a reply, not whether it saved effort or whether it holds up across a team.
- **I didn't test live use,** and I haven't had anyone outside run these tests.

## What I'd Do With It

I'm not cutting any skill, and I'm not changing one on the strength of this page. The tests say two things about how to write them:

- **Keep the stops and guardrails.** They are the part with evidence behind it.
- **Add a rule when I've seen the failure.** A new rule should name a mistake an AI made in a run, as the guardrails above do. Length that only restates what the model already does adds reading and no result I could find.

The claim on the [skills guide](../guides/what-is-a-sales-ai-skill.md), that a skill makes repeated work more consistent, is about not explaining the process each time. These tests don't bear on it either way.
