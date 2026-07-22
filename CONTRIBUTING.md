# Contributing

This is the checklist for adding or judging a piece of content in this repository, whether that is a new sales workflow, a skill, or a change to an existing one. It exists so "done" means the same thing every time, not whatever felt sufficient on the day.

It complements, and does not replace, [METHODOLOGY.md](METHODOLOGY.md) (how the underlying method is built) and [RESPONSIBLE-USE.md](RESPONSIBLE-USE.md) (what does and does not belong here). Read those first if you have not. This file is the practical checklist that sits on top of both.

## When a Workflow or Skill Counts as Complete

A new sales problem is not finished when the idea is good. It is finished when all of the following exist:

1. **A plain-English guide.** A `workflows/*.md` file following the house pattern: an At a Glance table, a three-step method diagram, a `Start Here` section, collapsible detail, a check-before-you-send list, and what to measure. See any existing workflow file for the exact shape.
2. **A bounded AI instruction**, if the task genuinely benefits from repeatability. Not every workflow needs a skill in `.agents/skills/`; add one only where doing the same thing the same way, safely, actually matters. See [what is a sales AI skill](guides/what-is-a-sales-ai-skill.md).
3. **Fictional source material.** A scenario built for the purpose, not adapted from a real deal. See the fictional-content rules below.
4. **A completed output.** The workflow or skill actually run against the fictional scenario, not just described.
5. **An honest evaluation.** The output scored against the [sales AI output rubric](evaluations/sales-ai-output-rubric.md), with a real score, not a rounded-up one.
6. **Known failure conditions.** What the workflow must not do: invented facts, unauthorised commitments, manufactured urgency, disparaging a named competitor, and whatever else is specific to that problem.
7. **Human approval points**, stated explicitly wherever the output could lead to an external action, a message, a CRM change, a commercial term.
8. **Valid links and a clean public-data check.** Every relative link resolves, and the content passes the [repository checks](.github/scripts/repo_checks.py) (also run automatically in CI on every pull request).
9. **Evidence the workflow was actually tested**, not just written. A worked example plus its scored evaluation is that evidence. If it has not been run against a realistic case, it is a draft, not a finished workflow.

If you cannot point to all nine, it is not done yet. That is fine. Say what is missing rather than presenting it as complete.

## Fictional Content Rules

- Every company, person, transcript, email and figure must be invented for this purpose. Do not adapt a real deal, even lightly disguised.
- Reuse an existing fictional universe where the story genuinely continues (Hartwell Analytics for anything post-call onward, Cedarwell Group for outbound with no call yet). Invent a new one only when the existing cast does not fit the scenario, as with the pipeline review's multi-deal snapshot or the buyer indecision example.
- Every example file should say plainly, near the top, that it is fictional and what it was created to test. The [repository checks](.github/scripts/repo_checks.py) enforce that examples contain the word "fictional".
- A deliberate test point is more useful than a clean success. Build scenarios with a real trap in them (an objection that reads one way on the surface and means another, a deal whose recorded stage overstates the evidence) so the evaluation has something real to catch.

## Scoring an Output Honestly

Use the [sales AI output rubric](evaluations/sales-ai-output-rubric.md) every time, not a one-off scoring scheme invented for a single skill.

- Score each of the ten areas on its own merit. A strong overall impression does not excuse a weak individual score.
- Write a one-line reason for every score, not just a number.
- A defensible judgement call, such as diagnosing which objection bucket applies or which stage a deal is really in, is not automatically a 5 on hallucination risk. If a reasonable person could read it differently, say so and score it accordingly. Several evaluations in this repository score 3 or 4 on hallucination risk for exactly this reason; that is honesty, not a defect.
- Record what worked, what needed checking, and what you would change next time. A finished evaluation includes at least one thing that needed checking. If nothing did, look harder before assuming the run was flawless.
- Where useful, note a concrete next test, a harder or more ambiguous version of the same scenario that would stress the workflow further.

## Repeated and Cross-Model Runs

For a single worked example, one honest run is enough. Before treating a workflow as reliable rather than merely working once, see the [evaluations README](evaluations/README.md) and the [test run template](evaluations/test-run-template.md) for running the same scenario repeatedly, across models, and recording where the runs agreed and where they diverged.

## House Style

Reader-facing copy (guides, workflows, drafts inside examples) follows the [writing style guide](guides/writing-style-and-formatting.md): plain and direct, contractions, no filler ("just checking in", "hope you're well"), no em dashes, ordinal dates, prose over lists except for genuine enumeration.

Repository-facing documentation (this file, `AGENTS.md`, evaluations) can be a little more procedural, but should still avoid corporate jargon, inflated claims, and unnecessary ceremony.

The public repository stays vendor-neutral. Do not name Shaun's employer, reproduce its internal processes, pricing or programme detail, or imply the repository is endorsed by any employer.

## Before Opening a Pull Request

- Run `python3 .github/scripts/repo_checks.py` locally. It also runs automatically in CI, but catching a failure before you push saves a round trip. To run it automatically on every commit instead of remembering by hand, enable the repository's local hook once with `git config core.hooksPath .github/hooks`.
- If you want to flag your own project-specific private terms (a real client name, an internal codename) without editing the checker itself, list them one per line in `.github/private-blocklist.txt`. That file is gitignored and never committed; the checker reads it if it exists and silently skips this check if it does not.
- Confirm every new or changed relative link resolves.
- If you are extending an existing sales problem, check whether a guide already covers it (`guides/where-to-start.md`, `guides/get-more-from-your-ai.md`, `guides/getting-started-with-ai.md`) before writing a new explanation. Link to the existing guide rather than repeating it.
- Keep the branch and pull request focused on one piece of work. A mixed pull request that touches unrelated files is harder to review honestly.
- Never merge your own pull request without explicit sign-off from Shaun. Draft pull requests are the default; leave them open for review.

## What Does Not Belong Here

See [RESPONSIBLE-USE.md](RESPONSIBLE-USE.md) for the full list. In short: no real customer, prospect or employer data, no secrets or credentials, no confidential internal process, and nothing that assumes autonomous action. Every workflow prepares work for a person to check, approve and send.
