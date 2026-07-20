# Roadmap

What is actually being worked on, in three honest buckets, followed by a longer backlog of ideas to revisit later. Not a promise of dates, just a record of what is next and why. The one current priority is in Now. Everything under Backlog is unprioritised, not committed, and may never happen.

## Now

- **Real usability feedback**: get even one or two real salespeople to try a workflow and say honestly whether it saved time or just moved the work around, rather than relying on my own judgement of my own output. More testers would be better, but one honest outside opinion beats none, and running a workflow on my own real, sanitised deal and logging where it helped versus where I had to redo its work counts as a first data point. This is the highest-value item left and the one that needs real people, not more writing.

## Done Recently

- **An interactive setup prompt**: [templates/interactive-setup-prompt.md](templates/interactive-setup-prompt.md), a standalone, tool-agnostic asset that interviews the user question by question in a fresh conversation and writes the finished, tailored setup prompt for them, as an alternative to filling in the About Me Worksheet by hand.
- **A second business case test scenario**: [Bramfield Insurance Group](examples/bramfield-business-case-transcript.md), a distinct late-stage transcript with a conditional two-year price instead of a flat figure and a Finance Director reader who was never on a call, plus its [output](examples/bramfield-business-case-output.md), [evaluation](evaluations/bramfield-business-case-review.md), and a second [skill reference](.agents/skills/build-business-case/references/bramfield-example.md).
- **A public quality bar**: [CONTRIBUTING.md](CONTRIBUTING.md) sets out the nine things that make a workflow or skill actually complete, the fictional content rules, honest scoring guidance, and house style. Complements [METHODOLOGY.md](METHODOLOGY.md) and [RESPONSIBLE-USE.md](RESPONSIBLE-USE.md) rather than duplicating them.
- **A buyer indecision vertical**: a [workflow](workflows/07-buyer-indecision.md), [prompt template](templates/buyer-indecision-prompt.md), a [fictional scenario](examples/calderwood-indecision-input.md), a [worked response](examples/calderwood-indecision-response.md), and a [scored evaluation](evaluations/calderwood-indecision-review.md). Handles the willing buyer who keeps delaying, by reducing the risk of deciding rather than pushing, and only after confirming it is genuine indecision and not an objection, an approval gate or a disqualification.
- **A pipeline evidence review vertical**: a [workflow](workflows/06-pipeline-evidence-review.md), [prompt template](templates/pipeline-evidence-review-prompt.md), a [fictional multi-deal pipeline snapshot](examples/fictional-pipeline-snapshot.md), a [worked review](examples/fictional-pipeline-review.md), and a [scored evaluation](evaluations/fictional-pipeline-review-eval.md). It separates the recorded CRM stage from the state the evidence actually supports, read-only, with every change left for a person to approve.
- **Repository safety and quality checks**: a GitHub Actions workflow that catches broken links, malformed skill frontmatter, unlabelled examples, employer or private references, secret-like values and placeholder text before anything merges.
- **The harder synthetic test is complete** across all three models: a genuinely ambiguous objection run three times each in Claude, ChatGPT and Gemini, [written up in full](evaluations/northstar-objection-ambiguous-test.md). Finding: the guardrails held on all nine runs (no invented facts, no discount, no false disqualification, always an isolate step), but which driver each model treated as primary varied, with Claude the least consistent and ChatGPT the most. The test earned one concrete skill change: the [objection-response skill](.agents/skills/objection-response/SKILL.md) now explicitly flags a shrinking rationale as distinct from a timing objection.
- **The objection-handling vertical is complete**: it now has a [workflow walkthrough](workflows/05-objection-handling.md), a [prompt template](templates/objection-handling-prompt.md), a [worked example](examples/northstar-objection-response.md), and a [scored review](evaluations/northstar-objection-review.md), alongside the existing [skill](.agents/skills/objection-response/SKILL.md), matching pre-call, post-call, handover, and lost-opportunity review.
- **An evaluation standard** for repeated and cross-model runs: see the [evaluations README](evaluations/README.md) and templates.

## Later

- Make CRM hygiene (duplicates, ownership, stale records) less painful to keep up to date, building on the pipeline evidence review now shipped.
- Find a sensible way to actually measure time saved and output quality, not just assume a workflow helps because it reads well.
- n8n or similar automation, once the underlying workflows are proven stable enough to hand to something unattended.
- Better voices for the interactive demo, if a real (non-browser) TTS API is ever worth the cost and complexity for what is currently a one-page static demo.
- Purposeful visuals for sharing, best done in a concentrated session: a social preview card and a cross-model comparison graphic are the highest-value pieces. Several process diagrams already exist as Mermaid and render on GitHub, so they do not need rebuilding as static images.

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

Only add a script where a deterministic check is genuinely useful. A structure check can confirm that required sections exist. It cannot prove that the commercial judgement is correct.

#### Source and evidence standards

Define which sources are acceptable and how they should affect an output. Prioritise:

1. direct evidence supplied for the sales task;
2. official product or platform documentation;
3. public primary research;
4. clearly named sales methods;
5. identifiable practitioner material;
6. model interpretation, labelled as interpretation.

The standard should also cover conflicting sources, estimates, vendor claims and the difference between public company context and confirmed customer need.

#### Lightweight repository checks

Consider a small GitHub Actions check for predictable repository errors:

- broken relative links;
- invalid skill frontmatter;
- duplicate skill names;
- missing limitations or human-review language;
- examples not clearly labelled as fictional;
- accidentally committed private context files;
- internal or confidential references;
- unfinished placeholder text.

Keep this proportionate to the size of the repository.

#### Public-data pre-commit scanner

Add a local check that flags possible confidential or personal information before it reaches a public commit.

Potential checks include:

- email addresses and phone numbers;
- API keys, tokens and credentials in URLs;
- private Google Docs, HubSpot or CRM links;
- configured customer, employer and person names;
- unexpected commercial figures;
- private-context files or CRM exports;
- custom blocklist patterns.

The first version should report possible issues for human review. It should not automatically rewrite or delete source material.

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

Define what one skill passes to the next. For example, a post-call evidence skill might pass confirmed facts, commitments, objections and unknowns to a follow-up skill.

A handoff should state:

- what is confirmed;
- what is inferred;
- what is missing;
- which source supports each material point;
- what the next skill is allowed to do;
- what still requires a person.

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

A short prompt addition to the existing [pre-call preparation workflow](workflows/01-pre-call-preparation.md): have the AI play a sceptical version of the actual prospect persona and push back on the planned pitch, using only what is already established about them, so the salesperson gets a few minutes of live pushback practice before a real call rather than rehearsing alone in their head.

This is deliberately lightweight, a single prompt bolted onto the existing workflow, not the fuller practice environment described below under Learning tools and future interfaces. Build this one first if either gets picked up; it needs no new interface, no run history and no scoring, just a good prompt.

#### Signal-to-hypothesis outbound

Turn public company signals into clearly labelled commercial hypotheses:

- observed signal and source;
- possible relevance;
- what it does not prove;
- a question that could verify it;
- a safe outreach angle;
- reasons not to use it.

#### Company-first and signal-first prospecting

Document two different starting routes:

- company-first, when there is a defined account list or market;
- signal-first, when accounts are discovered from a relevant public event.

Both routes should include evidence checks before contact discovery or enrichment.

#### Pipeline evidence review

Check whether recorded stages, close dates, stakeholders and next steps are supported by available evidence.

The output should flag unsupported or stale fields without accusing the salesperson or treating CRM data as automatically correct.

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

Audit an approved fictional or user-provided CRM export for:

- missing critical fields;
- exact and possible duplicates;
- stale records;
- unsupported close dates or stages;
- missing owners or contacts;
- cleanup priorities.

The first version should be read-only and require a person to approve every merge, deletion or CRM update. Any scoring thresholds should be configurable rather than presented as universal facts.

#### Weekly sales operating review

Create a report from whatever approved data is available, while clearly marking missing sections.

Potential sections include:

- pipeline movement;
- meetings and commitments;
- outreach activity;
- new signals;
- items needing attention;
- three evidence-backed priorities for the next week.

Never fabricate a metric to complete a dashboard. Compare with earlier reports only when a genuine baseline exists.

#### Objection pattern review

Analyse repeated objections across several opportunities while keeping observed patterns separate from assumed root causes.

Useful fields might include the exact objection, stage, speaker role, diagnosed driver, response, outcome and confidence.

#### Buyer indecision

Distinguish late-stage fear of making the wrong decision from an ordinary objection, missing information, timing issue, approval dependency, reduced business rationale, soft no or genuine disqualification.

The workflow must not invent pilots, discounts, contract flexibility, implementation promises or risk-removal commitments.

#### Champion enablement and multithreading

Help an internal supporter communicate a well-evidenced case to other stakeholders. Possible outputs include a decision summary, internal email, role-specific evidence and questions that remain unanswered.

Do not assume a stakeholder's priorities from their job title. Do not contact additional stakeholders or go over the main contact's head without explicit approval and appropriate context.

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

Create short routes into existing workflows for users who want to complete one job without reading the whole repository.

Each recipe should include:

- what the recipe helps with;
- what information is needed;
- what it will produce;
- which guide, prompt or skill to open;
- what the AI cannot decide;
- what a person must check;
- what to do next.

Do not publish unsupported time-saved claims. Encourage users to record their own manual, AI-assisted and checking time.

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

Add a future issue template that asks:

- What sales job are you trying to complete?
- What information do you normally have?
- What output do you need?
- What mistakes would make it unsafe?
- What still requires a person?
- How do you currently do it?

Use requests as evidence for backlog decisions rather than accepting broad suggestions without context.

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
