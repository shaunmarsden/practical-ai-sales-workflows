# Roadmap

What is actually being worked on, in three honest buckets, followed by a longer backlog of ideas to revisit later. Not a promise of dates, just a record of what is next and why. The one current priority is in Now. Everything under Backlog is unprioritised, not committed, and may never happen.

## Now

- **Keep testing against real work as it comes up.** Not a batch exercise, and not blocking anything else: when a real objection, a real pipeline check, or a real anything else comes up, run the matching workflow on it and see honestly whether it held up. Twelve verticals have real evidence behind them now. Two, hand over an opportunity and move a stalled decision, had no real material available as of 24 July 2026; check back on 7 August 2026 for whether a genuine case has turned up for either. Prepare for a sales call is deliberately excluded from this gap, since it is used live in a chat rather than as something tested and recorded this way.

## Done Recently

- **Added a sibling repositories scoping guide, still gated on its own hard condition.** Built ahead of the usual bar, on the project owner's own call, the same override applied elsewhere tonight. The new [guide](guides/sibling-repositories.md) is deliberately a scoping document, not a start: it names what would transfer directly to another function's version of this repository (the house style discipline, CONTRIBUTING.md's completeness bar, the repository-checks discipline, the public-data boundary) against what a genuine practitioner from that function would have to define from scratch (the real jobs, what a good output looks like, real evidence and testing), and restates the one hard condition unchanged: no sibling repository starts without that practitioner already in place. Names no specific function, practitioner, or timeline.

- **Wrote full design specs for the four Learning Tools and Future Interfaces backlog ideas, still distant ideas, not software.** Built ahead of the usual bar, on the project owner's own call, the same override applied elsewhere tonight; unlike those other overrides, this one does not ship a working guide or workflow, since building any of the four as actual software is a genuinely separate project this repository does not undertake. The new [design document](guides/future-interfaces.md) expands each of the four short backlog stubs, the role-play simulator, the interactive evidence workspace, the explainable lead-qualification view, and the before-and-after instruction testing interface, into what it would do, what it must never do, and which existing repository material it would depend on rather than reinvent. Nothing here is built; the value is having a fuller spec to check a future build against, if one is ever started.

- **Added a downloadable skill packages guide, documenting the structure without publishing an actual ZIP.** Built ahead of the usual real-use-evidence bar (the backlog item said wait for testing to show a bundle is useful), on the project owner's own call. The new [guide](guides/downloadable-skill-packages.md) lists what a package should contain (the skill, a plain-English guide, a fictional case, an output template, the evaluation rubric, per-platform installation notes) and demonstrates the structure once against [identify-buyer-indecision](.agents/skills/identify-buyer-indecision/SKILL.md), an existing skill that already has every required piece. Deliberately stops short of publishing an actual ZIP or building any packaging tooling, since a maintained duplicate would drift from the real skill files the moment either changed, and no installer has been asked for yet.

- **Added a selective installation guide, the per-platform mechanics of loading only a chosen subset of skills.** Built ahead of the usual real-use-evidence bar, on the project owner's own call. The new [guide](guides/selective-installation.md) covers Claude, ChatGPT, Gemini and Copilot, and is deliberately mechanical: it assumes the "which skills" decision is already made via [Choose Your Route by Role](guides/role-based-routes.md) or a curated bundle, and covers only how to actually load that subset without carrying the rest of the library's instructions into every conversation.

- **Added the missing working state and an explicit structure to evidence-supported opportunity state.** The [pipeline evidence review workflow](workflows/06-pipeline-evidence-review.md) and [prompt](templates/pipeline-evidence-review-prompt.md) already separated the recorded CRM stage from the evidence-supported state; the backlog's own list of working states named one, commercial review, that the existing list was missing, so it is now added alongside the others. Both files now also state explicitly that the recorded stage and the evidence-supported state must be shown side by side, with any conflict named, before a next step is suggested, rather than that structure being implicit in how the review already happened to read.

- **Promoted the outbound campaign learning review from a prompt-only structure to a full workflow, the sixteenth job in the repository.** Built ahead of its own stated bar, on the project owner's own call: the backlog item said to prove the structure helps on a real campaign first, before it earned a fictional example, an evaluation and a place in the main problem list. It now has all three: [workflows/14-outbound-campaign-learning-review.md](workflows/14-outbound-campaign-learning-review.md), a fictional Cedarwell-style campaign comparison with a deliberate trap (two variables changed at once, a small second sample), a [scored evaluation](evaluations/cedarwell-campaign-review-eval.md), and a [recipe card](recipes/review-an-outbound-campaign.md). Wired into the README's main problem list, recipes/README.md, AGENTS.md and role-based-routes.md, all updated from fifteen jobs to sixteen. The backlog note is honest that a fictional test and score are not a substitute for the real-campaign test its own prompt has always called for; that real test still has not happened.

- **Added three outbound and chase-sequence backlog items: signal-to-hypothesis, company-first versus signal-first, and channel-escalation logic.** Built ahead of the usual real-use-evidence bar, on the project owner's own call. The [outbound prospecting skill](.agents/skills/outbound-prospecting/SKILL.md) now links a new [signal-to-hypothesis reference](.agents/skills/outbound-prospecting/references/signal-to-hypothesis.md): a six-part structure (signal and source, possible relevance, what it does not prove, a verifying question, a safe outreach angle, reasons not to use it), three concrete signal categories that are checkable facts rather than guesses (follower size, ad spend, active hiring for a role the offer would replace), and the difference between starting company-first from a defined list versus signal-first from a public event. The [plan-chase-sequence skill](.agents/skills/plan-chase-sequence/SKILL.md)'s [sequence-stages reference](.agents/skills/plan-chase-sequence/references/sequence-stages.md) now documents channel-escalation as decision logic only, do not move channels before the first one has had a fair chance to be read, explicitly leaving out any automated cross-channel triggering or auto-dialling as not fitting this repository's human-approval-first model.

- **Added a curated bundles guide, grouping existing recipe cards into three starting packs.** Built ahead of the usual real-use-evidence bar, on the project owner's own call, the same way role-based routes was: a Sales AI starter pack, a post-call pack, and a deal progression pack, each a page of links to [recipe cards](recipes/README.md) that already exist, no installer. The [guide](guides/curated-bundles.md) says plainly that the three groupings are a starting guess, worth revisiting once real use shows whether they are the ones people actually reach for.

- **Added a progressive disclosure guide, naming a pattern already in use and auditing the current skill library against it.** The new [guide](guides/progressive-disclosure.md) states what belongs in a skill's core `SKILL.md` (the method itself, gathered on every run) versus a supporting file (a fictional example, an output contract, a template, a checklist, loaded only when that specific step needs it), then checks all eleven current skills against it. Every core file sits under ninety lines, and every skill with deeper material already keeps it in a separate file; nothing failed the audit. The guide's ongoing value is having a place to check the next skill against, so a `SKILL.md` that starts growing past this pattern gets caught at review time.

- **Piloted the standard skill package on a second skill, champion-enablement.** The [skill](.agents/skills/champion-enablement/SKILL.md) already had a fictional Hartwell example; it now also has an [output contract](.agents/skills/champion-enablement/references/output-contract.md) stating what the AI must and must not do, an [output template](.agents/skills/champion-enablement/templates/output-template.md) for the finished package, and a [human review checklist](.agents/skills/champion-enablement/checks/checklist.md), matching the structure already piloted on identify-buyer-indecision. Both pilots so far started from a skill that already had a working fictional example; the backlog note is updated to say the harder, more useful test is a skill without one yet, which is the case that would actually show whether the structure earns its way into CONTRIBUTING.md's baseline rather than staying optional.

- **Added a composing-longer-workflows guide, covering the seven remaining backlog items under Workflow composition and traceability.** Built as a deliberate project-owner override of the usual real-use-evidence bar, the same way role-based routes was. The new [guide](guides/composing-longer-workflows.md) documents working folders and run logs, visible progress for longer runs, spend checkpoints before paid enrichment, keeping a manual route alongside any connector, choosing method before platform, separating AI judgement from code mechanics, and keeping instructions visible even when configurable. States plainly throughout that these are principles to build to, not a description of software that exists in this repository now; nothing here executes automatically today.

- **Added role-based routes, a guide for readers who would rather start from their job title than a list of sales problems.** Built ahead of the usual real-use-evidence bar, on the project owner's own call rather than waiting for usability testing to show a need, the same way several other verticals were launched ahead of that bar. The new [guide](guides/role-based-routes.md) groups the same fifteen existing jobs by which ones actually come up for an account executive, a sales manager, RevOps, customer success, or someone doing founder-led sales, pointing only to recipe cards that already exist rather than duplicating any of them. Linked from the README's "Three Ways to Start" section and from AGENTS.md's guide list. It needs a real test like everything else here, specifically whether the five groupings actually match how people in those seats work.

- **The weekly operating review is real-tested, composed entirely from this week's other real findings.** Built as a genuine composition rather than fresh analysis, exactly as the [workflow](workflows/10-weekly-operating-review.md) requires: pipeline movement correctly stated as not yet measurable, since this was the first report with no earlier snapshot to compare against; outreach activity correctly marked unmeasured rather than assumed to be zero, since only a couple of unrelated sends were visible from one inbox; and the items needing attention pulled directly from other real reviews already run this week, a CRM duplicate and stale test records, a stalled opportunity with an unresolved objection worth reviving, three funding objections that look similar but are not, rather than re-deriving any of it from scratch. Every guardrail held cleanly. No skill change needed; recorded as real evidence the composition model works when the underlying reviews genuinely exist, not just in the fictional worked example.

- **Objection pattern review is real-tested, and it correctly refused to call a surface pattern real.** Checked against three real accounts where a funding-related objection came up in each. Surface pattern: all three mention the same funding mechanism. Actual driver in each: a specific compliance rule in one, an internal optics problem in another, a resource-prioritisation fight in the third, three genuinely different underlying causes, not one repeated issue. Concluding "one funding objection, one standard answer" would have been exactly the mistake this skill exists to prevent, and its existing guidance, checking the driver rather than the wording, using its own worked competitor-name example, handled this correctly with no gap found. No skill change needed; recorded as real evidence that the guardrail holds on genuinely messy, real data, not just a fictional case built to test it.

- **Fit and limitations review is real-tested, and it found a real evidence conflict the skill did not name.** Checked against a real account where one role's day-to-day tasks were a clear good fit, structured, recurring data-submission work, while the stakeholder raising the objection described that same role in general terms as clinical and interpretive, the opposite framing. The [skill](.agents/skills/fit-and-limitations-review/SKILL.md), [workflow](workflows/13-fit-and-limitations-review.md) and [prompt](templates/fit-and-limitations-review-prompt.md) had no guidance for this specific situation, a stakeholder's general characterisation of a role conflicting with the specific tasks described for that same role, so it would have been tempting to quietly pick whichever reading suited the classification, the tasks to support a sale or the characterisation to support the objection. All three now say to name the conflict directly instead.

- **Champion enablement is real-tested, and the guardrails correctly stopped it from running.** Checked against a real account with a plausible internal champion and a proposed next step (build a case, take it to a named further stakeholder). The [skill](.agents/skills/champion-enablement/SKILL.md) requires a champion to have actually agreed to carry a case internally before it produces anything, and the real evidence only had a suggested approach on the seller's side, not confirmation the champion had agreed to present it. It correctly stopped rather than drafting a package on an unmet precondition. The one further stakeholder named in the evidence was known only by title, with nothing established about their actual concerns, which the skill's guardrail against inferring a priority from a job title alone would have correctly refused to fill in. No skill change needed; recorded as real evidence that the guardrail holds under a genuine, ambiguous case, not just a fictional one.

- **CRM hygiene review is real-tested, and it found a category the workflow was missing.** Checked against a real, messy CRM export: alongside genuine prospects sat several records that were not prospects at all, test entries, practice runs, and internal demo data left in the live pipeline. The [workflow](workflows/08-crm-hygiene-review.md) and [prompt](templates/crm-hygiene-review-prompt.md) only had categories for duplicates, missing fields, stale records and stage mismatches, none of which fit a record that should not really be scored as pipeline in the first place. A record like this is different from a duplicate (the same real prospect twice) or a missing field (a real prospect with a gap), so it is now flagged as its own category, with the recommendation to archive or delete it rather than fill it in. The same real export also produced a clean confirmation of an existing rule: a genuine duplicate, the same person and company entered twice with the name and company simply reversed, is exactly the kind of confident finding the workflow already knows how to catch.

- **Review a lost opportunity is real-tested, and it found a genuine gap in the classification.** Checked against a real deal that stalled after a specific, unresolved objection: an answer or workaround was actually sent back, and then contact from both sides simply stopped, no rejection, no reply. The [skill](.agents/skills/review-lost-opportunity/SKILL.md) and [workflow](workflows/04-lost-opportunity-review.md) only offered four categories (disqualification, timing, stakeholder change, unresolved objection), none of which fit a case where nobody actually said no and no decision was ever made on either side. A fifth category, no decision at all, now names this pattern explicitly, since the right next action differs: follow up on the answer already sent, rather than wait for an external trigger the way the other four categories imply. A second, smaller finding from the same test: the deal's own CRM stage was an internal, undefined label, which is now called out directly as something to confirm rather than infer from its name or position, in both the skill and the workflow's checklist.

- **Build a business case is real-tested, and mostly held up well.** Checked against a real, recently-used business case document: the [build-business-case skill](.agents/skills/build-business-case/SKILL.md)'s core guardrails all matched real practice exactly, third-person framing for a reader who was not on the call, next steps that never imply the process is finished once the document is sent, live descriptive hyperlinks, and a dedicated data or security section consistent with what was actually said. Two structural rules did not match. The skill said "headed prose, not a table"; real practice pairs a compact summary table (company, role, product or programme, start date) with a fully prose case underneath, so the rule now allows that hybrid rather than treating it as a violation. The skill described each applied example as a short paragraph; real practice used a sub-heading plus an expected impact line plus measurable early success indicators, a stronger and more scannable shape now named as the better default. Both changes are in the [skill](.agents/skills/build-business-case/SKILL.md) and the [audit checklist](.agents/skills/build-business-case/references/audit-checklist.md).

- **Three more reader-friendly diagrams**: an [evidence-labels diagram](assets/diagrams/how-this-repository-labels-evidence.svg) for [METHODOLOGY.md](METHODOLOGY.md), a [growth path](assets/diagrams/get-more-from-your-ai.svg) for [Get More From Your AI](guides/get-more-from-your-ai.md), and a new version of [How I Approach It](README.md). All three replace dense prose or basic Mermaid boxes with playful native SVGs checked at the size they actually appear on GitHub.

- **A workflow router**: a [guide](guides/workflow-router.md), [skill](.agents/skills/workflow-router/SKILL.md), and [portable prompt](templates/workflow-router-prompt.md) that reads a plain-English description of a sales situation and hands off to whichever of the fifteen existing workflows actually fits, without solving the task itself. Grounded in the real "use this when" line already documented in each workflow, not a separately invented routing scheme, and names the confusions worth checking explicitly (stalled decision versus objection, chase versus lost-opportunity review, fit review versus business case). The worked example in the guide deliberately tests the first of those: a description that could read as an unstated objection but has no specific concern actually raised. Built as a guide and skill rather than a numbered workflow file, the same treatment as skill handoff contracts, since it is cross-cutting infrastructure, not a new sales problem in itself.

- **A private sales-methodology overlay**: [a template](context/sales-methodology-overlay.md.example) alongside the existing `sales-context.md.example`, letting a reader map their own approved qualification method (MEDDIC, BANT, or their own framework) and pipeline stage names onto the public workflows without publishing internal definitions, stage rules or CRM configuration. Every field is labelled `evidence required` or `judgement call`, so the same discipline the public workflows already use carries into private, unpublished detail rather than being dropped once the file is private. `repo_checks.py` now checks this new private file the same way it already checked `sales-context.md`: never committed, always listed in `.gitignore`, tested by deliberately committing a copy and confirming the checker catches it before reverting.

- **A fit and limitations review vertical**: a [workflow](workflows/13-fit-and-limitations-review.md), [prompt template](templates/fit-and-limitations-review-prompt.md), a fictional [Kellow scenario](examples/kellow-fit-review-input.md) and [output](examples/kellow-fit-review-output.md), a [scored evaluation](evaluations/kellow-fit-review-review.md) (47/50), and a [skill](.agents/skills/fit-and-limitations-review/SKILL.md). A new fictional company rather than a Hartwell continuation, since the scenario needed a genuine mixed result (one team a clean fit, one a real mismatch, one honestly undecided) that Hartwell's clean-success story could not credibly supply. Built to deliberately test the skill's core guardrail: a shared, ownerless team structure is tempting to describe as a rollout advantage, when the real story is an unresolved integration and ownership problem, and the worked output states the mismatch plainly instead. Also updates the [repo overview diagram](README.md) and recipe card count to fifteen. Built ahead of this repository's own usual bar of real-use evidence before a new vertical, as part of the same deliberate pre-launch push as champion enablement; fictional-tested only for now.

- **An instruction-change and regression history template**: [a template](templates/instruction-change-history-template.md) recording, every time a skill's actual instructions change because a test found something wrong, the original wording, the test case, the raw output, the specific failure, the exact change, the rerun result, and what improved against what did not. Includes a standing six-point regression checklist (an information request doesn't become an agreed meeting, a second-hand detail stays second-hand, a missing date stays unknown, an unauthorised commitment triggers a stop, a genuine disqualification isn't argued with, no external action is treated as completed without confirmation) to check on every change, not just the one being tested, so fixing one failure doesn't quietly reopen a guardrail that already worked. Linked from the [evaluations README](evaluations/README.md).

- **Outbound prospecting is real-tested, and the result was mixed in an interesting way.** A genuine first-touch message, sent for real, was checked against the [outbound-prospecting skill](.agents/skills/outbound-prospecting/SKILL.md): a company-specific analysis already produced for the target, shared directly in the message with a straight ask for time to discuss it, rather than a smaller front-end offer promised for later. It got a fast, positive reply. That structure was not one the skill described at all, so it now names both as valid shapes and says to match the shape to what is actually true, rather than blending them. The subject line used, on the other hand, directly broke the subject-line rule added last session (naming the analysis outright rather than reading as an internal message), and still got a reply within the hour. Recorded honestly as one data point against a rule written with real confidence, not as proof the rule is wrong; one real result is not enough to change it either way, and it needs more evidence before either happens.

- **A pre-launch visual pass**: a new [repo-wide sales cycle image](README.md) grouping all fifteen jobs by where they sit in a deal, placed right before the long per-problem list so a reader sees the shape of the whole repository before scrolling it. The detailed workflow diagrams remain available inside each workflow, while the README now uses a simpler overview designed for a nontechnical salesperson. Also found and fixed six em dashes in [the interactive demo](docs/index.html), the one house-style rule that page had never actually been checked against, since `repo_checks.py` only scans Markdown, not HTML.

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

- **A GitHub social preview image**, so the repository shows something other than a blank card when the link is shared. Built as a native SVG and exported to PNG rather than generated with Gemini, since a Gemini attempt at the earlier "Where Should I Start" visual came back with an unremovable watermark. The [SVG source](assets/social/github-social-preview.svg) and [PNG export](assets/social/github-social-preview.png) are both tracked in the repository and uploaded through the repository's Settings, which is where GitHub actually reads the preview from.

- **Workflow recipe cards**: a [one-page card](recipes/README.md) per sales job, fifteen in total, each self-contained (what it helps with, what you need, what it produces, what the AI cannot decide, what you must check, what to do next) so a reader never has to open the full workflow to use one. Built from what already existed in each workflow's At a Glance table and check-before-you-send list, not new content, and linked from the main [README](README.md) and [AGENTS.md](AGENTS.md) alongside the existing routes rather than replacing them.

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

**Piloted on a second skill**, see [Done Recently](#done-recently) above for [champion-enablement](.agents/skills/champion-enablement/SKILL.md). Still not a repository-wide requirement; CONTRIBUTING.md's quality bar still only requires `SKILL.md` plus references where a fictional test genuinely helps. Two pilots in, both on skills that already had a fictional example to build the contract, template and checklist around; the harder test is a skill that does not yet have one, which would show whether the structure earns its own fictional example rather than only formalising one that already existed. Hold off on making it a blanket requirement until that harder case has been tried.

Only add a script where a deterministic check is genuinely useful. A structure check can confirm that required sections exist. It cannot prove that the commercial judgement is correct.

#### Source and evidence standards

**Shipped**, see [Done Recently](#done-recently) above.

#### Lightweight repository checks

**Shipped**, see [.github/scripts/repo_checks.py](.github/scripts/repo_checks.py), which runs in CI on every push and pull request. Covered: broken relative links, invalid skill frontmatter, examples not labelled as fictional, accidentally committed private context files, unfinished placeholder text, duplicate skill names, and a skill missing human-review or limitation language.

#### Public-data pre-commit scanner

**Shipped**, see [Done Recently](#done-recently) above. Still not covered, and likely never deterministically checkable: an unexpected commercial figure, which needs a person who knows what the real numbers should look like.

#### Instruction-change and regression history

**Shipped**, see [Done Recently](#done-recently) above for the [template](templates/instruction-change-history-template.md).

#### Progressive disclosure

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/progressive-disclosure.md).

#### Curated bundles

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/curated-bundles.md).

### Workflow composition and traceability

#### Workflow router

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/workflow-router.md).

#### Skill handoff contracts

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/skill-handoff-contracts.md).

#### Working folders and run history

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/composing-longer-workflows.md).

#### Visible progress and cancellable runs

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/composing-longer-workflows.md).

#### Cost and approval checkpoints

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/composing-longer-workflows.md).

#### Manual route first

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/composing-longer-workflows.md).

#### Method before platform

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/composing-longer-workflows.md).

#### Separate judgement from orchestration

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/composing-longer-workflows.md).

#### Configurable but visible instructions

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/composing-longer-workflows.md).

### Sales workflow ideas

#### Pre-call objection roleplay drill

**Shipped**, see [Done Recently](#done-recently) above for the [prompt](templates/pre-call-objection-roleplay-prompt.md). The fuller practice environment described below under Learning tools and future interfaces remains unbuilt.

#### Outbound campaign learning review

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/14-outbound-campaign-learning-review.md). Promoted to a full workflow ahead of its own stated bar (a real campaign proving the structure actually helps first), on the project owner's own call. Still needs the real-campaign test its own prompt has always called for; a fictional test and an honest score are not a substitute for that.

#### Signal-to-hypothesis outbound

**Shipped**, see [Done Recently](#done-recently) above for the [reference](.agents/skills/outbound-prospecting/references/signal-to-hypothesis.md).

#### Company-first and signal-first prospecting

**Shipped**, see [Done Recently](#done-recently) above for the same [reference](.agents/skills/outbound-prospecting/references/signal-to-hypothesis.md).

#### Outbound message structure refinements

**Shipped**, see [Done Recently](#done-recently) above.

#### Chase sequence follow-up structure

**Shipped**, see [Done Recently](#done-recently) above for the [plan-chase-sequence skill](.agents/skills/plan-chase-sequence/SKILL.md).

#### Channel-escalation sequencing for a stalled chase

**Shipped**, see [Done Recently](#done-recently) above for the [reference](.agents/skills/plan-chase-sequence/references/sequence-stages.md), decision logic only, no automation.

#### Pipeline evidence review

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/06-pipeline-evidence-review.md).

#### Evidence-supported opportunity state

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/06-pipeline-evidence-review.md) and [prompt](templates/pipeline-evidence-review-prompt.md).

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

**Shipped**, see [Done Recently](#done-recently) above for the [workflow](workflows/13-fit-and-limitations-review.md). Built ahead of the usual real-use-evidence bar for a new vertical, as part of a deliberate pre-launch push; it needs a real test like everything else here.

### Navigation, packaging and private configuration

#### Role-based routes

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/role-based-routes.md).

#### Private sales-methodology overlay

**Shipped**, see [Done Recently](#done-recently) above for the [template](context/sales-methodology-overlay.md.example).

#### Selective installation and platform guidance

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/selective-installation.md).

#### Workflow recipe cards

**Shipped**, see [Done Recently](#done-recently) above for the [recipe cards](recipes/README.md).

#### Downloadable cross-platform skill packages

**Shipped**, see [Done Recently](#done-recently) above for the [guide](guides/downloadable-skill-packages.md).

#### Missing-workflow request template

**Shipped**, see [Done Recently](#done-recently) above.

### Learning tools and future interfaces

These are distant ideas. They may become separate software projects if the simpler repository workflows prove useful first.

#### Fictional sales role-play simulator

**Shipped as a spec**, see [Done Recently](#done-recently) above for the [design document](guides/future-interfaces.md). Still a distant idea; nothing here is built as software.

#### Interactive evidence workspace

**Shipped as a spec**, see [Done Recently](#done-recently) above for the same [design document](guides/future-interfaces.md).

#### Explainable lead-qualification view

**Shipped as a spec**, see [Done Recently](#done-recently) above for the same [design document](guides/future-interfaces.md).

#### Before-and-after instruction testing interface

**Shipped as a spec**, see [Done Recently](#done-recently) above for the same [design document](guides/future-interfaces.md).

### AI literacy and tooling guides

Raised from a rough brain dump, 24 July 2026. Checked first against everything already here: customer comms and chase sequencing, setting an AI up as a salesperson, connecting other systems, and getting started at all are already covered by the [Chase a Quiet Prospect recipe](recipes/chase-a-quiet-prospect.md) and the existing [Get More From Your AI](guides/get-more-from-your-ai.md), [Set Up Your Own AI for Sales](guides/set-up-your-ai-for-sales.md), [Getting Started With AI](guides/getting-started-with-ai.md) and [Where to Start](guides/where-to-start.md) guides. These four are the genuinely new ground once that overlap is removed.

#### NotebookLM and Gemini Notebook

A plain-English guide to source-grounded notebook tools specifically, distinct from the general project/knowledge-base pattern already covered in [Get More From Your AI](guides/get-more-from-your-ai.md): what they are actually good for (a bounded set of real sources, not a general assistant), and where that differs from a Project or a Gem.

#### Notetaker and transcript tools

A guide to call-transcript tools (Granola-style) as a category: what they capture, the manual-paste alternative for anyone without one, and how a transcript from one of these feeds directly into the existing [extract post call evidence](.agents/skills/extract-post-call-evidence/SKILL.md) skill.

#### Agent orchestrators, explained

A plain-English explainer: what an agent orchestrator actually is, what it can genuinely help with, and how someone would start using one, aimed at a reader who has heard the term but not used one. Distinct from [Composing Longer Workflows](guides/composing-longer-workflows.md), which is architecture principles for this repository's own future, not a tool explainer for the reader. Worth a short, related note on Google Apps Script as a lightweight, code-based alternative for someone who wants to script a specific integration without a full orchestration platform.

#### Models and token management

A guide to the actual practical differences between models (not a benchmark chase) and what token management means for a working salesperson: why a long conversation degrades, when to start a fresh one, and what actually belongs in a Project's knowledge versus in every single message.

### Beyond this repository

#### Sibling repositories for other business functions

**Shipped as a scoping guide**, see [Done Recently](#done-recently) above for the [guide](guides/sibling-repositories.md). Still not a plan for this repository, and still gated on the same hard condition it always was: a genuine practitioner from that function driving it. Nothing here starts one.
