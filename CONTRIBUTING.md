# Contributing

This is the checklist for adding or judging content here, whether that's a new sales workflow, a skill or a change to one that exists. It's here so "done" means the same thing every time, not whatever felt like enough on the day.

It adds to [METHODOLOGY.md](METHODOLOGY.md) (how the method works) and [RESPONSIBLE-USE.md](RESPONSIBLE-USE.md) (what does and doesn't belong here). It doesn't replace them. Read those first if you haven't.

## When a Workflow or Skill Counts as Complete

A new sales problem isn't finished when the idea is good. It's finished when all of these exist:

1. A plain-English guide. That's a `workflows/*.md` file in the house pattern: an At a Glance table, a three-step method diagram, a `Start Here` section, collapsible detail, a check-before-you-send list, and what to measure. Any existing workflow file shows the exact shape.
2. A tightly scoped AI instruction, if the task gains from being done the same way each time. Not every workflow needs a skill in `.agents/skills/`. Add one only where doing the same thing the same way, safely, matters. See [what is a sales AI skill](guides/what-is-a-sales-ai-skill.md).
3. Fictional source material: a scenario made for the purpose, not adapted from a real deal. See the fictional-content rules below.
4. A finished output. Run the workflow or skill against the fictional scenario; don't just describe it.
5. An evaluation. Score the output against the [sales AI output rubric](evaluations/sales-ai-output-rubric.md), with the real score, not a rounded-up one.
6. Known failure conditions. What the workflow must not do: invent facts, make commitments nobody authorised, invent urgency, run down a named competitor, and anything else specific to that problem.
7. Human approval points, stated wherever the output could lead to action outside the company: a message, a CRM change, a commercial term.
8. Working links and a clean public-data check. Every relative link resolves, and the content passes the [repository checks](.github/scripts/repo_checks.py). CI also runs them on every pull request.
9. Evidence that the workflow was tested, not just written. A worked example and its scored evaluation are that evidence. If nobody has run it against a realistic case, it's a draft.

If you can't point to all nine, it isn't done yet. That's fine. Say what's missing rather than calling it complete.

## Fictional Content Rules

- Invent every company, person, transcript, email and figure for this purpose. Don't adapt a real deal, even in disguise.
- Reuse an existing fictional world where the story carries on: Hartwell Analytics for anything from the call onwards, Cedarwell Group for outbound before any call. Invent a new one only when the existing cast doesn't fit, as with the pipeline review's snapshot of several deals or the buyer indecision example.
- Every example file should say plainly, near the top, that it's fictional and which skill or workflow it tests. **Name the job, not the difficulty.** What the scenario turns on belongs below the re-run line with the answer key, or in the evaluation. That's because the re-run warning tells a reader to copy everything above that line. An earlier version of this rule asked for "what it was created to test". As a result, 15 published inputs hinted at their own answer key in the one part of the file a re-runner is told to keep.
- The same goes for a skill's pointer to a test scenario. The skill gets pasted into the model with the input, so a footer saying what the harder test turns on gives the answer away just as the input would. Say that a scenario is harder, and leave what makes it harder to its evaluation.
- The [repository checks](.github/scripts/repo_checks.py) make sure examples contain the word "fictional". They can't enforce the rule above. I tried two mechanical stand-ins, blockquote length and phrasing shared between the disclosure and the answer key, and neither told the leaking files from the clean ones.
- A deliberate test point is more useful than a clean success. Put a real trap in the scenario, such as an objection that reads one way on the surface and means another, or a deal whose recorded stage claims more than the evidence shows. Then the evaluation has something real to catch.

## Scoring an Output Honestly

Use the [sales AI output rubric](evaluations/sales-ai-output-rubric.md) every time, not a one-off scheme made up for a single skill.

- Score each of the ten areas on its own. A strong overall impression doesn't excuse a weak score in one area.
- Write a one-line reason for every score, not just a number.
- A judgement call you can defend, such as which objection bucket applies or which stage a deal is really in, isn't automatically a 5 on hallucination risk. If a reasonable person could read it differently, say so and score it that way. Several evaluations here score 3 or 4 on hallucination risk for this reason. That's honest scoring, not a fault.
- Record what worked, what needed checking and what you'd change next time. A finished evaluation includes at least one thing that needed checking. If nothing did, look harder before you assume the run was perfect.
- Where it helps, note a next test: a harder or more ambiguous version of the same scenario that would push the workflow further.

## Repeated and Cross-Model Runs

For a single worked example, one run is enough. Before you treat a workflow as reliable rather than as something that worked once, see the [evaluations README](evaluations/README.md) and the [test run template](evaluations/test-run-template.md). They cover running the same scenario several times and across models, and recording where the runs agreed and where they differed.

## House Style

Reader-facing copy (guides, workflows, drafts inside examples) follows the [writing style guide](guides/writing-style-and-formatting.md): plain and direct, contractions, no filler ("just checking in", "hope you're well"), no em dashes, no smart quotes or curly apostrophes, ordinal dates, prose over lists except for genuine enumeration.

The same applies to everything else here, evaluations included. Follow Orwell's six rules, set out in the style guide: short words, cut what you can (repeated points, and any sentence that doesn't move the argument), active voice, everyday words over jargon. Write in the first person. An evaluation reports what I tested and what happened, not how careful the test was. Skills and prompt blocks are the exception: they're tested instructions, so change them only with a new test.

A rewrite changes what a page says, not only how it reads. After you rewrite, check that the new text keeps the original's scope, certainty, emphasis and cause. Don't let clearer wording turn evidence into a stronger claim, a reasonable reading into a fact, two things that happen together into one causing the other, or an opinion into something that sounds settled. If clearer or more persuasive wording would claim more than the evidence supports, keep the weaker claim.

The public repository stays vendor-neutral. Don't name my employer, reproduce its internal processes, pricing or programme detail, or imply the repository is endorsed by any employer. The one deliberate exception is the README's own About Me section, where I name my real employer as part of my own personal bio, not as repository content; `repo_checks.py` allowlists that exact line and nowhere else.

## Before Opening a Pull Request

- Run `python3 .github/scripts/repo_checks.py` locally. CI runs it too, but catching a failure before you push saves a round trip. To run it on every commit without having to remember, turn on the repository's local hook once with `git config core.hooksPath .github/hooks`.
- To flag your own private terms (a real client name, an internal codename) without editing the checker, list them one per line in `.github/private-blocklist.txt`. Git ignores that file, so it's never committed. The checker reads it if it exists and quietly skips this check if it doesn't.
- Check every new or changed relative link resolves.
- If you're extending an existing sales problem, check whether a guide already covers it (`guides/where-to-start.md`, `guides/get-more-from-your-ai.md`, `guides/getting-started-with-ai.md`) before writing a new explanation. Link to that guide rather than repeating it.
- Keep the branch and pull request to one piece of work. A pull request that mixes in unrelated files is harder to review properly.
- Never merge your own pull request without my sign-off. Open pull requests as drafts by default, and leave them open for review.

## What Does Not Belong Here

[RESPONSIBLE-USE.md](RESPONSIBLE-USE.md) has the full list. In short: no real customer, prospect or employer data, no secrets or credentials, no confidential internal process, and nothing that assumes the AI acts on its own. Every workflow prepares work for a person to check, approve and send.

## Licence

This repository is [MIT licensed](LICENSE). Use, adapt and share any of it, including in a commercial sales team, with attribution and without warranty.
