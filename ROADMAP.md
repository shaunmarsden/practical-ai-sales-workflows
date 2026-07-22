# Roadmap

What is actually being worked on, in three honest buckets, followed by a longer backlog of ideas to revisit later. Not a promise of dates, just a record of what is next and why. The one current priority is in Now. Everything under Backlog is unprioritised, not committed, and may never happen.

## Now

- **Keep testing against real work as it comes up.** Not a batch exercise, and not blocking anything else: when a real objection, a real pipeline check, or a real anything else comes up, run the matching workflow on it and see honestly whether it held up. Four verticals have real evidence behind them now; the rest do not yet, and that gap closes naturally through use rather than by scheduling more tests.

## Done Recently

- **A pre-launch visual pass**: a new [repo-wide overview diagram](README.md) grouping all fourteen verticals by where they sit in a deal, placed right before the long per-problem list so a reader sees the shape of the whole repository before scrolling it. Audited all fourteen workflows' existing Mermaid diagrams for consistency first; found them already uniform (same flowchart style, three steps, same node and arrow syntax), so nothing needed fixing there. Also found and fixed six em dashes in [the interactive demo](docs/index.html), the one house-style rule that page had never actually been checked against, since `repo_checks.py` only scans Markdown, not HTML.

- **An outbound campaign learning review structure**: [a prompt](templates/outbound-campaign-learning-review-prompt.md) covering what to record after a real outbound campaign, audience, signal source, offer and message, the single variable actually tested, raw numbers through to qualified opportunities, and what makes the comparison uncertain. Deliberately not built as a full workflow with a fictional example and scored evaluation yet, following the backlog item's own explicit instruction to try the structure on a real campaign first and check whether it leads to a better next test, not just a tidy report, before it earns the same treatment as the tested verticals.

- **A champion enablement vertical**: a [workflow](workflows/12-champion-enablement.md), [prompt template](templates/champion-enablement-prompt.md), a fictional [Hartwell scenario](examples/hartwell-champion-enablement-input.md) and [output](examples/hartwell-champion-enablement-output.md), a [scored evaluation](evaluations/hartwell-champion-enablement-review.md) (47/50), and a [skill](.agents/skills/champion-enablement/SKILL.md). Continues the Hartwell story rather than inventing a new one: Alex Morgan, the existing champion, needs to carry the already-built business case to Priya Chen at the QBR, plus a short internal note to Hartwell's Head of IT and Compliance chasing a still-outstanding data-handling confirmation. Built to deliberately test, and hold, the guardrail against assuming a stakeholder's priority from their job title: Priya's actual confirmed concern is CRM visibility, not the AE quota or deal velocity her Sales Director title might suggest. Built ahead of this repository's own usual bar of real-use evidence before a new vertical, as part of a deliberate pre-launch content push; it is fictional-tested only for now, same as every other vertical before its own first real test.

- **Chase sequence follow-up structure**: the [plan-chase-sequence skill](.agents/skills/plan-chase-sequence/SKILL.md) and its [sequence stages reference](.agents/skills/plan-chase-sequence/references/sequence-stages.md) now state the shape across early, middle, late and final chases as an escalating-friction curve, not an escalating-urgency one: the earliest chase can carry the real ask, later ones ask for something smaller. Each chase should also stand alone rather than assume the earlier ones were read. A new rule against reminding a quiet prospect that previous messages were sent is scoped carefully to exclude the close-out stage, whose entire job is to acknowledge the sequence honestly, so the new rule does not quietly contradict guidance already there.

- **Outbound message structure refinements are complete**: the [outbound prospecting skill](.agents/skills/outbound-prospecting/SKILL.md) and [workflow](workflows/09-outbound-prospecting.md) state the front-end-offer distinction explicitly, add a subject-line and preview-text rule, and add two anti-pattern guardrail lines against manufactured interest and invented scarcity. Applied, not just written: the subject line in the existing [Cedarwell worked example](examples/cedarwell-outbound-output.md) was updated to actually follow the new rule, with the change noted in [its evaluation](evaluations/cedarwell-outbound-review.md), and a new [deliberately weak version of the same message](examples/cedarwell-outbound-weak-example.md) breaks every guardrail on purpose, annotated point by point, alongside the good one.

- **Skill handoff contracts**: a new [guide](guides/skill-handoff-contracts.md) stating the six things that should pass between two skills run in sequence on the same call (what's confirmed, what's inferred or estimated, what's missing, which source backs each point, what the next skill may do with it, what still requires a person). Grounded in a real worked example rather than an abstract rule: the extract-post-call-evidence to draft-follow-up-email handoff, annotated against the existing fictional [Hartwell post-call output](examples/hartwell-post-call-output.md), which already had to get every one of these six things right to be a finished example. A documentation and discipline standard, not new automation; nothing here proposes piping one skill's output into the next without a person in between.

- **A pull request template**: [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md), pre-loaded into every new PR, mirroring what [CONTRIBUTING.md](CONTRIBUTING.md) already asks for rather than a new bar. Prompted by a plain question worth recording here: even before any outside contributor shows up, forking and a pull request is already the only route into this repository; nobody can push or merge without it being reviewed and merged deliberately. The template makes the existing bar visible at the point someone opens a PR rather than something they have to go and find first.

- **Source and evidence standards**: a new section 4, "Weigh Every Kind of Source the Same Way," in [METHODOLOGY.md](METHODOLOGY.md), covering sources beyond a specific deal's own evidence, product documentation, public primary research, named sales methods, practitioner material, and model interpretation, in that order. Complements the existing deal-evidence order in section 3 rather than replacing it, and covers the standard's other requirements directly: a vendor's own product claim is not proof of a customer's confirmed need, public company context stays background rather than evidence of an internal problem, and a disagreement between two sources at different levels gets named rather than smoothed over. Required renumbering the rest of the file's sections; nothing else in the repository linked to a specific section anchor, so nothing else needed updating.

- **A missing-workflow request template**: a [GitHub issue form](.github/ISSUE_TEMPLATE/missing-workflow.yml) asking what sales job someone was trying to complete, what they normally have to work with, what output they need, what would make it unsafe, what still needs a person, and how they do it today without AI. A checkbox up front asks whether the existing workflows and recipe cards were actually checked first, so a request is evidence for a real gap, not a broad suggestion with no context behind it.

- **The public-data pre-commit scanner is complete**: [repo_checks.py](.github/scripts/repo_checks.py) now also flags email addresses and phone numbers, and reads an optional local, never-committed blocklist (`.github/private-blocklist.txt`) for project-specific private terms. A real local git hook at [.github/hooks/pre-commit](.github/hooks/pre-commit) runs the same checks on every commit once enabled with `git config core.hooksPath .github/hooks`, so this no longer depends on remembering to run it by hand or waiting for CI. Still not covered, and likely never will be: an unexpected commercial figure, which needs a person who actually knows what the real numbers should look like, not a regular expression.

- **A cross-model comparison chart**: [an SVG](evaluations/assets/cross-model-comparison.svg) added to the [cross-model post-call comparison](evaluations/cross-model-post-call-comparison.md), showing the overall score and the per-criterion breakdown for ChatGPT, Claude and Gemini. Built directly from the real scored numbers already in that write-up, not generated by an image tool, since a chart's bar heights need to be provably correct rather than a good likeness. The single-run caveat is baked into the image itself, not left to surrounding text alone. The remaining piece of the "purposeful visuals for sharing" idea, alongside the social preview image below.

- **A GitHub social preview image**, so the repository shows something other than a blank card when the link is shared. Generated with Gemini rather than built by hand, since image generation is not something this repository's own tools do; set via the repository's Settings, not a tracked file, so it will not appear in any diff.

- **Workflow recipe cards**: a [one-page card](recipes/README.md) per sales job, thirteen in total, each self-contained (what it helps with, what you need, what it produces, what the AI cannot decide, what you must check, what to do next) so a reader never has to open the full workflow to use one. Built from what already existed in each workflow's At a Glance table and check-before-you-send list, not new content, and linked from the main [README](README.md) and [AGENTS.md](AGENTS.md) alongside the existing routes rather than replacing them.

- **Two more real usability tests, both earned real fixes.** Post-call follow-up was run against a real call and checked against the email actually sent afterwards: the sent version was genuinely richer than the draft in places a generic template could not reach, which led to two fixes now in [the draft-follow-up-email skill](.agents/skills/draft-follow-up-email/references/template-and-checklist.md). A chase-sequence test on a real, stalled deal turned up a sharper problem: Granola and Gmail alone showed a plausible stall, but the CRM's own activity timeline recorded an explicit decline and a since-corrected stage, something neither notes nor email ever surfaced. Nothing was sent on that deal. The general lesson, that meeting notes and email are not a substitute for the CRM and the CRM is not a substitute for them, is now a standing rule in [METHODOLOGY.md](METHODOLOGY.md).

- **The first real usability tests are done, and both found something real.** Objection handling was run on a live objection: the diagnosis and response structure held up, but a commercial figure the draft treated as confirmed, because it came from an earlier real email, turned out to be wrong; that fix is now in [RESPONSIBLE-USE.md](RESPONSIBLE-USE.md). Pipeline evidence review was run on a real, meeting-notes-derived pipeline: 5 of 7 deals were accurate as flagged, 1 was correctly flagged as unconfirmed and has since resolved on its own (the review working as intended, not a miss), and 1 was a genuine error, a deal included that was not actually the reviewer's to manage, now fixed with a new ownership check in [the workflow](workflows/06-pipeline-evidence-review.md). Both fixes were earned from real use, not invented.

- **An objection pattern review vertical**: a [workflow](workflows/11-objection-pattern-review.md), [prompt template](templates/objection-pattern-review-prompt.md), a [fictional objection log](examples/fictional-objection-pattern-log.md), a [worked analysis](examples/fictional-objection-pattern-review.md), and a [scored evaluation](evaluations/fictional-objection-pattern-review-eval.md) (47/50). Reuses two objections already on record (Hartwell's Copilot and price objections) and adds four fresh ones, deliberately built so one surface pattern (Copilot mentioned three times) turns out not to be a real single issue, while a genuinely different one (a compliance question raised twice, in unrelated sectors) is. The point of the workflow is telling those two apart, not just counting recurrences.
- **A way to measure time saved and output quality**: [guides/measure-time-and-quality.md](guides/measure-time-and-quality.md) and the [time and quality log](templates/time-and-quality-log.md). Logs manual, AI-assisted and checking time honestly (checking time counts, a workflow that did not help is real data too), used alongside the existing [output rubric](evaluations/sales-ai-output-rubric.md) rather than instead of it. This is the tool the "Now" priority above needs whenever a real workflow gets tried, by anyone, including Shaun himself on his own sanitised deal.
- **A pre-call objection roleplay prompt**: [templates/pre-call-objection-roleplay-prompt.md](templates/pre-call-objection-roleplay-prompt.md), a short addition to the existing [pre-call preparation workflow](workflows/01-pre-call-preparation.md), not a new vertical. The AI plays a sceptical version of the actual prospect, grounded only in the completed call card, and gives an honest debrief afterwards. Includes one illustrative example, [a roleplay exchange built from the existing Hartwell pre-call scenario](examples/hartwell-pre-call-roleplay.md). Deliberately has no scored evaluation, matching the backlog item's own scope: this is practice, not something to score.
- **A weekly operating review vertical**: a [workflow](workflows/10-weekly-operating-review.md), [prompt template](templates/weekly-operating-review-prompt.md), a [fictional input](examples/fictional-weekly-operating-review-input.md), a [worked report](examples/fictional-weekly-operating-review-output.md), and a [scored evaluation](evaluations/fictional-weekly-operating-review-eval.md) (46/50). Deliberately composes the pipeline evidence review and CRM hygiene review's findings into one weekly view rather than re-analysing anything, and refuses to invent a trend on a first report with no baseline to compare against. Building it surfaced a real error in the already-shipped CRM hygiene review (Harbourview's close date was wrongly listed as passed; it is five days in the future), fixed in both places, which is itself evidence that composing one workflow's output into another is a genuinely effective way to catch mistakes a single review misses.
- **The outbound prospecting vertical is complete**: it had only a skill, no workflow, worked example or evaluation, the one gap against [CONTRIBUTING.md](CONTRIBUTING.md)'s own completeness bar. Now has a [workflow](workflows/09-outbound-prospecting.md), a [prompt template](templates/outbound-prospecting-prompt.md), a full [Cedarwell signal](examples/cedarwell-outbound-input.md) and [output](examples/cedarwell-outbound-output.md) built from the skill's existing scenario, and a [scored evaluation](evaluations/cedarwell-outbound-review.md) (46/50), alongside the existing [skill](.agents/skills/outbound-prospecting/SKILL.md).
- **A CRM hygiene review vertical**: a [workflow](workflows/08-crm-hygiene-review.md), [prompt template](templates/crm-hygiene-review-prompt.md), a [fictional CRM export](examples/fictional-crm-export.md), a [worked review](examples/fictional-crm-hygiene-review.md), and a [scored evaluation](evaluations/fictional-crm-hygiene-review-eval.md) (45/50). Flags likely and possible duplicates, missing fields and stale records, read-only, and deliberately stays out of the stage-accuracy question the pipeline evidence review already covers. Building this one surfaced two real errors in its own worked example (a wrong "more recently active" claim, an undercounted set of blank-contact rows), both caught by checking the review line by line against its own source data before scoring it, which is exactly the discipline worth repeating on a real export.
- **An interactive setup prompt**: [templates/interactive-setup-prompt.md](templates/interactive-setup-prompt.md), a standalone, tool-agnostic asset that interviews the user question by question in a fresh conversation and writes the finished, tailored setup prompt for them, as an alternative to filling in the About Me Worksheet by hand.
- **A second business case test scenario**: [Bramfield Insurance Group](examples/bramfield-business-case-transcript.md), a distinct late-stage transcript with a conditional two-year price instead of a flat figure and a Finance Director reader who was never on a call, plus its [output](examples/bramfield-business-case-output.md), [evaluation](evaluations/bramfield-business-case-review.md), and a second [skill reference](.agents/skills/build-business-case/references/bramfield-example.md).
- **A public quality bar**: [CONTRIBUTING.md](CONTRIBUTING.md) sets out the nine things that make a workflow or skill actually complete, the fictional content rules, honest scoring guidance, and house style. Complements [METHODOLOGY.md](METHODOLOGY.md) and [RESPONSIBLE-USE.md](RESPONSIBLE-USE.md) rather than duplicating them.
- **A buyer indecision vertical**: a [workflow](workflows/07-buyer-indecision.md), [prompt template](templates/buyer-indecision-prompt.md), a [fictional scenario](examples/calderwood-indecision-input.md), a [worked response](examples/calderwood-indecision-response.md), and a [scored evaluation](evaluations/calderwood-indecision-review.md). Handles the willing buyer who keeps delaying, by reducing the risk of deciding rather than pushing, and only after confirming it is genuine indecision and not an objection, an approval gate or a disqualification.
- **A pipeline evidence review vertical**: a [workflow](workflows/06-pipeline-evidence-review.md), [prompt template](templates/pipeline-evidence-review-prompt.md), a [fictional multi-deal pipeline snapshot](examples/fictional-pipeline-snapshot.md), a [worked review](examples/fictional-pipeline-review.md), and a [scored evaluation](evaluations/fictional-pipeline-review-eval.md). It separates the recorded CRM stage from the state the evidence actually supports, read-only, with every change left for a person to approve.
- **Repository safety and quality checks**: a GitHub Actions workflow that catches broken links, malformed skill frontmatter, unlabelled examples, employer or private references, secret-like values and placeholder text before anything merges.
- **The harder synthetic test is complete** across all three models: a genuinely ambiguous objection run three times each in Claude, ChatGPT and Gemini, [written up in full](evaluations/hartwell-objection-ambiguous-test.md). Finding: the guardrails held on all nine runs (no invented facts, no discount, no false disqualification, always an isolate step), but which driver each model treated as primary varied, with Claude the least consistent and ChatGPT the most. The test earned one concrete skill change: the [objection-response skill](.agents/skills/objection-response/SKILL.md) now explicitly flags a shrinking rationale as distinct from a timing objection.
- **The objection-handling vertical is complete**: it now has a [workflow walkthrough](workflows/05-objection-handling.md), a [prompt template](templates/objection-handling-prompt.md), a [worked example](examples/hartwell-objection-response.md), and a [scored review](evaluations/hartwell-objection-review.md), alongside the existing [skill](.agents/skills/objection-response/SKILL.md), matching pre-call, post-call, handover, and lost-opportunity review.
- **An evaluation standard** for repeated and cross-model runs: see the [evaluations README](evaluations/README.md) and templates.

## Later

- A worked example of a dedicated automation or orchestration tool, once the underlying workflows are proven stable enough to hand to something unattended. See the orchestrator section in [Get More From Your AI](guides/get-more-from-your-ai.md) for the concept; no specific tool has been named, since it is a bigger technical step than anything else in the repository and not every reader needs it.
- Better voices for the interactive demo, if a real (non-browser) TTS API is ever worth the cost and complexity for what is currently a one-page static demo.

## Backlog

These are ideas worth revisiting after the workflows already in the repository have been tested with real salespeople.

They are not delivery commitments and they are not listed in priority order. The current priority remains usability testing (see Now) and improving what is already here.

### How an idea moves out of the backlog

Before building one of these, check that it:

- solves a problem observed in real use;
- can be tested with fictional or approved public material;
- keeps facts, inferences, unknowns and conflicting evidence separate;
- leaves emails, CRM changes and external actions under human approval;
- can be evaluated honestly;
- does not require confidential employer or customer information;
- adds more value than improving an existing workflow.

### Quality and maintainability

#### Standard skill package

Test a consistent structure on one skill before applying it across the repository:

```text
SKILL.md
references/output-contract.md
references/fictional-example.md
templates/output-template.md
checks/checklist.md
```

**Piloted** on the [identify-buyer-indecision skill](.agents/skills/identify-buyer-indecision/SKILL.md), a diagnosis-only skill paired with the existing buyer indecision workflow and prompt. Not yet a repository-wide requirement; CONTRIBUTING.md's quality bar still only requires `SKILL.md` plus references where a fictional test genuinely helps. Decide whether this richer structure earns its way into that requirement, or stays optional, once it has been used on a second skill.

Only add a script where a deterministic check is genuinely useful. A structure check can confirm that required sections exist. It cannot prove that the commercial judgement is correct.

#### Source and evidence standards

**Shipped**, see [Done Recently](#done-recently) above.

#### Lightweight repository checks

**Shipped**, see [.github/scripts/repo_checks.py](.github/scripts/repo_checks.py), which runs in CI on every push and pull request. Covered: broken relative links, invalid skill frontmatter, examples not labelled as fictional, accidentally committed private context files, unfinished placeholder text, duplicate skill names, and a skill missing human-review or limitation language.

#### Public-data pre-commit scanner

**Shipped**, see [Done Recently](#done-recently) above. Still not covered, and likely never deterministically checkable: an unexpected commercial figure, which needs a person who knows what the real numbers should look like.

#### Instruction-change and regression history

Create a repeatable record for improving a skill after testing:

```text
Original instruction version
Test case
Raw outputs
Rubric scores
Observed failure
Instruction change
Rerun outputs
Score difference
What improved
What did not
```

Add regression checks for critical guardrails, such as:

- an information request does not become an agreed meeting;
- a second-hand objection remains second-hand;
- a missing date remains unknown;
- an unauthorised commitment triggers a stop;
- a genuine disqualification is not argued with;
- no external action is treated as completed without confirmation.

#### Progressive disclosure

Keep core skill instructions short enough to load when needed. Put deeper examples, templates and reference notes in supporting files so every task does not load the entire repository.

#### Curated bundles

Once users show that they need them, group existing skills into simple packages such as:

- Sales AI starter pack;
- Post-call pack;
- Deal progression pack.

Start with a page that links the relevant files. Do not build an installer until the bundle itself has been tested.

### Workflow composition and traceability

#### Workflow router

Build a lightweight router that recommends an existing workflow based on:

- the user's goal;
- the sales stage;
- the evidence available;
- the main blocker;
- whether private company context is required.

The router should not solve the underlying task. It should produce a clean handoff containing:

- the objective;
- evidence currently available;
- important missing information;
- the recommended workflow and skill;
- why the route fits;
- what the next skill may produce;
- what still requires a person.

It should route to existing skills rather than contain every method itself.

#### Skill handoff contracts

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/skill-handoff-contracts.md).

#### Working folders and run history

For longer workflows, consider a simple project structure that separates:

```text
input/
intermediate/
output/
run-log.md
```

The run log should record what was used, what was produced, what was skipped, any corrections and which actions were actually completed.

#### Visible progress and cancellable runs

For longer tasks, show the user where the workflow has reached:

```text
Sources loaded
Evidence extracted
Conflicts found
Draft produced
Human review required
```

Future integrated tools should let the user stop, retry or replace instructions before an external action occurs. Failed runs should leave enough information to understand what happened without pretending the task completed.

#### Cost and approval checkpoints

Where a workflow may use paid enrichment, research or automation tools, add explicit review points before spending more credits or taking an external action.

A useful pattern is:

```text
collect
review quality
filter
review again
enrich
human approval
act
```

#### Manual route first

Every integrated workflow should retain a manual route using pasted or uploaded information. Providers and connectors should remain optional, with limitations and fallbacks stated clearly.

#### Method before platform

Choose the sales method before choosing a product-specific tool.

A platform adapter should implement an already understood workflow. It should not become the source of the sales method merely because the platform exposes an API or connector.

#### Separate judgement from orchestration

Keep the AI responsible for tasks such as classification, drafting and identifying gaps. Keep code or automation responsible for repeatable mechanics such as file handling, scheduling and API calls.

Do not automate a workflow until the manual version is stable and its failure conditions are understood.

#### Configurable but visible instructions

Provide a safe default instruction for each workflow while allowing the user to inspect and adapt it.

Record when a custom instruction was used. Do not hide the instruction that produced a recommendation, score or customer-facing draft.

### Sales workflow ideas

#### Pre-call objection roleplay drill

**Shipped**, see [Done Recently](#done-recently) above for the [prompt](templates/pre-call-objection-roleplay-prompt.md). The fuller practice environment described below under Learning tools and future interfaces remains unbuilt.

#### Outbound campaign learning review

**The structure is written**, see [Done Recently](#done-recently) above for [the prompt](templates/outbound-campaign-learning-review-prompt.md). Deliberately not a full workflow yet: use it on a real campaign first and check whether it actually leads to a better next test, not just a tidy report, before it earns a fictional example, an evaluation, and a place in the main problem list alongside the tested verticals.

#### Signal-to-hypothesis outbound

Turn public company signals into clearly labelled commercial hypotheses:

- observed signal and source;
- possible relevance;
- what it does not prove;
- a question that could verify it;
- a safe outreach angle;
- reasons not to use it.

Worth naming a few concrete, verifiable signal categories rather than leaving "a specific signal" abstract: audience or follower size as a proxy for growth intent, active ad spend as a proxy for investment intent, and active hiring for a role the offer would replace as a proxy for a live, current problem. All three are checkable facts, not a guess about internal state, so they fit the existing [outbound prospecting skill](.agents/skills/outbound-prospecting/SKILL.md)'s requirement for a real, verifiable signal rather than a generic industry trend.

#### Company-first and signal-first prospecting

Document two different starting routes:

- company-first, when there is a defined account list or market;
- signal-first, when accounts are discovered from a relevant public event.

Both routes should include evidence checks before contact discovery or enrichment.

#### Outbound message structure refinements

**Shipped**, see [Done Recently](#done-recently) above.

#### Chase sequence follow-up structure

**Shipped**, see [Done Recently](#done-recently) above for the [plan-chase-sequence skill](.agents/skills/plan-chase-sequence/SKILL.md).

#### Channel-escalation sequencing for a stalled chase

Flagged rather than recommended: the idea of a defined channel order (email, then a different channel, then a call) once a prospect has gone quiet on the first one. The underlying sequencing logic, do not escalate to a new channel before the first one has had a fair chance to be read, might be worth documenting as a principle. Most of the practical implementation of this (automated cross-channel triggers, auto-dialling) does not fit this repository's human-approval-first model and should not be built as described; if this moves forward at all, it should be the decision logic only, left for a person to act on.

#### Pipeline evidence review

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/06-pipeline-evidence-review.md).

#### Evidence-supported opportunity state

Separate the recorded CRM stage from the state supported by current evidence.

Possible working states include:

- exploring;
- qualification incomplete;
- problem confirmed;
- value case incomplete;
- stakeholder approval required;
- decision process unclear;
- commercial review;
- paused with a dated reason;
- lost;
- disqualified.

Before proposing a next action, state:

- the recorded stage;
- the evidence-supported state;
- any conflict between them;
- what must be confirmed before progression.

These states must remain configurable and should not be treated as universal sales stages.

#### Read-only CRM hygiene review

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/08-crm-hygiene-review.md).

#### Weekly sales operating review

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/10-weekly-operating-review.md).

#### Objection pattern review

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/11-objection-pattern-review.md).

#### Buyer indecision

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/07-buyer-indecision.md) and the [identify-buyer-indecision skill](.agents/skills/identify-buyer-indecision/SKILL.md).

#### Champion enablement and multithreading

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/12-champion-enablement.md). Built ahead of the usual real-use-evidence bar for a new vertical, as part of a deliberate pre-launch push; it needs a real test like everything else here.

#### Fit and limitations review

Help a seller document where an offer is a good fit, a poor fit or still uncertain. Use approved product evidence and avoid turning limitations into disguised strengths.

This could support honest discovery, objections, business cases and disqualification.

### Navigation, packaging and private configuration

#### Role-based routes

If usability testing shows a need, add short routes for account executives, sales managers, RevOps, customer success and founder-led sales. These should point to existing material rather than duplicate it.

#### Private sales-methodology overlay

Let users map their own approved qualification or sales method onto the repository without publishing internal definitions, stage rules or CRM configuration.

The private template should distinguish fields requiring direct customer evidence from fields that permit salesperson judgement.

#### Selective installation and platform guidance

As the skill library grows, explain how to install or load only the skills needed for a role or task. Avoid forcing users to load a large catalogue that may crowd out the most relevant instructions.

#### Workflow recipe cards

**Shipped**, see [Done Recently](#done-recently) above for the [recipe cards](recipes/README.md).

#### Downloadable cross-platform skill packages

Once testing shows that a bundle is useful, publish a small ZIP containing:

- the skill;
- a plain-English guide;
- a fictional case;
- an output template;
- the evaluation rubric;
- product-specific installation notes.

Support a manual route for ChatGPT, Claude, Gemini and other assistants where practical. Do not claim identical behaviour across products.

#### Missing-workflow request template

**Shipped**, see [Done Recently](#done-recently) above.

### Learning tools and future interfaces

These are distant ideas. They may become separate software projects if the simpler repository workflows prove useful first.

#### Fictional sales role-play simulator

A fuller version of the [pre-call objection roleplay drill](#pre-call-objection-roleplay-drill) above under Sales workflow ideas, as a proper practice environment where:

- the AI plays a fictional prospect from fixed source material;
- the salesperson responds;
- the system records which evidence was uncovered;
- unsupported claims or invented commitments are flagged;
- coaching is provided after the exercise.

The simulator should test judgement and evidence gathering, not reward closing at any cost.

#### Interactive evidence workspace

A future local interface could show:

- sources loaded;
- evidence and source links;
- facts, inferences, unknowns and conflicts;
- workflow progress;
- the instruction used;
- draft outputs;
- approval still required;
- run and correction history.

The user should be able to cancel, rerun or change instructions before anything external happens.

#### Explainable lead-qualification view

A future visual view could separate:

- confirmed fit;
- possible fit;
- disqualifying evidence;
- missing information;
- public signals;
- what those signals do not prove.

Avoid a single opaque 0 to 100 score unless every component, weight and limitation is visible and configurable.

#### Before-and-after instruction testing interface

Allow a user to compare two instruction versions against the same fictional case, preserving raw outputs, scores, differences and human review notes.

This should support evaluation. It should not present model-generated scoring as independent proof.
