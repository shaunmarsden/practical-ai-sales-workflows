# Changelog

This is the completed-work archive. The [roadmap](ROADMAP.md) now stays focused on what is current and what may happen next.

Release notes provide the fuller version summaries:

- [v1.2.0: Safer Orchestration and Better Evidence](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.2.0)
- [v1.1.0: More Workflows, Better Routes and Real Evidence](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.1.0)
- [v1.0.0: First Complete Set of Sales Workflows](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.0.0)

## Unreleased

### Spot the Real Blocker

- Added a seventeenth sales job: a workflow, skill, portable prompt, recipe card, fictional Rowcastle test and scored evaluation for checking whether the person on a call is actually the decision-maker, and whether their stated objection is the real one or standing in for something unstated. Added to the workflow router's table, alongside a fix for Review an Outbound Campaign, which had no route in that table at all.
- One fictional test only. No independent or real-use evidence yet.

## v1.2.0, 7 August 2026

Moved beyond adding individual sales workflows into testing how they can be coordinated safely, and made the evidence behind every job easier to inspect.

### Approval-Gated Sales Copilot

- Added a public guide and a vendor-neutral composition template for an approval-gated sales copilot, an orchestration layer that chooses between existing bounded workflows rather than a new, seventeenth sales job.
- Added a fictional multi-source orchestration test and its scored evaluation.
- Added a sanitised finding describing my private sales copilot's reported internal use, kept clearly labelled as builder-reported, not independent evidence.
- Added the method's first sanitised live-run finding: a real request where the public method prioritised a fixed meeting over a wider pipeline search, kept retrieval narrow, verified the relevant specialist route before using it, and surfaced an attendee-identity ambiguity across connected records rather than guessing. Nothing was sent, booked or changed; every external write stayed behind approval. One live run is not proof the method is reliable or that anyone outside the project has adopted it.

### Stronger Skills and Harder Tests

- Added a reusable opportunity-handover skill, alongside a harder fictional regression test built on a stalled handover with conflicting CRM and email evidence and a change of contact. Testing exposed two real problems along the way: actions without one clear accountable owner, and invented pronouns for people whose gender the evidence never stated. The first was fixed and confirmed working on a clean rerun. The second needed a checkable mechanism, a person reference ledger and a mandatory reference audit, rather than a guardrail sentence, and a careful re-read of the same output still found further interpretive overreach worth catching. The final, honestly scored result is 38 out of 50, not the higher scores an earlier, less careful pass produced.
- Added a reusable pre-call preparation skill with an inspectable fictional source pack. A scored comparison showed the skill's structured, source-traced output scored notably higher than the earlier example, and a fresh-agent rerun against a different fictional company confirmed the improvement generalised rather than being specific to one wording.
- Added a second scored test for the objection-pattern skill, covering duplicate deals, a hidden shared driver behind different wording, and a misleadingly similar phrase with a different actual cause. A fresh-agent rerun against a separate fictional log confirmed the same discipline held.
- Added a scored fictional test for Chase a Quiet Prospect, showing why current CRM evidence should override a stale reminder rather than triggering another chase.

### Clearer Evidence

- Added an evidence-status matrix so a visitor can see, for each of the sixteen sales jobs, whether a workflow, skill, fictional test, real use or independent test actually exists, rather than treating availability as proof of anything.
- Logged sanitised real-use findings for Hand Over an Opportunity and Move a Stalled Decision. The stalled-decision finding is a negative-boundary case: a real delay correctly classified as a policy and timing blocker, not evidence the method can move a genuinely indecisive buyer.
- Added a private two-minute feedback form, a public GitHub Discussions feedback route, a structured response template and a public visitor feedback log, so future feedback has somewhere to land and be tracked openly.
- Replaced the detailed project-history roadmap with a short Now, Next and Later view.
- Made the interactive demonstration's fictional-data wording clearer and added a direct route to try the follow-up workflow.

### Known Gaps

- Review an Outbound Campaign still has no logged real-campaign test.
- Move a Stalled Decision has a real negative-boundary finding, but still no positive real case involving genuine buyer indecision.
- No sales job has a logged independent external user test yet.
- The Sales Copilot has one sanitised builder-run live finding, but no independent attempt.
- Feedback is being left to arrive organically through the existing feedback form and Discussions link, rather than being manufactured through a recruited session.

## v1.1.0, 27 July 2026

Expanded the repository from eight sales jobs to sixteen, added clearer routes for nontechnical readers and recorded evidence from real sales work.

### Real Use Findings

Twelve jobs have a logged finding from sanitised real sales work:

- **Find the Next Prospect:** a real first-touch message earned a quick positive reply, while also challenging one confident subject-line rule.
- **Follow Up After a Sales Call:** comparison with the email actually sent exposed where a generic draft missed useful detail.
- **Check Whether It Actually Fits:** a real case exposed conflicting evidence between a stakeholder's broad description and the specific work being done.
- **Build a Business Case:** a real business case showed that a compact summary table could work well alongside headed prose.
- **Brief Your Champion:** a real case correctly stopped because the proposed champion had not agreed to carry the case internally.
- **Chase a Quiet Prospect:** CRM evidence overturned a plausible chase suggested by meeting notes and email alone, so nothing was sent.
- **Handle an Objection:** a real test found that a previously used commercial figure was no longer reliable.
- **Spot a Real Objection Pattern:** three similar surface objections turned out to have three different underlying drivers.
- **Review a Lost Opportunity:** a real stalled deal exposed a missing classification, no decision at all.
- **Review Your Pipeline:** a real review found five accurate flags, one correctly unconfirmed deal and one ownership error.
- **Keep Your CRM Honest:** a real export exposed test and demo records that were neither prospects nor ordinary missing-data cases.
- **Get a Weekly View Without Building a Dashboard:** a real weekly view composed existing findings without inventing trends where no baseline existed.

Real inputs remain private. Only the sanitised finding and any resulting method change are recorded publicly.

### Used Live Without a Formal Test

- **Prepare for a Sales Call** is used live in an AI conversation, but no separate formal test finding has been logged.

### Known Evidence Gaps

- Move a Stalled Decision has a fictional scored test but no suitable real case yet.
- Hand Over an Opportunity has a fictional scored test but no suitable real case yet.
- Review an Outbound Campaign has a fictional scored test but no completed real-campaign test yet.
- No sales job has yet completed a logged independent external user test.

### Library and Navigation

- Added eight more sales jobs, bringing the total to sixteen.
- Added one-page recipe cards, a printable cheat sheet, a workflow router, routes by role and curated starting bundles.
- Added or expanded portable skills, including pipeline evidence review and CRM hygiene review.
- Added selective installation, progressive disclosure and skill-packaging guidance.
- Added a live demonstration showing a fictional transcript becoming evidence-labelled output.

### Quality and Packaging

- Added repository checks, a local pre-commit hook and a pull request template.
- Added consistent diagrams, a social preview image and a cross-model comparison chart.
- Added versioned releases, repository topics, a profile README and a pinned featured repository.
- Added clearer public-data, source-weighing and human-approval rules.

## v1.0.0, 19 July 2026

Published the first complete set of eight practical sales jobs:

- Find the Next Prospect
- Prepare for a Sales Call
- Follow Up After a Sales Call
- Build a Business Case
- Chase a Quiet Prospect
- Handle an Objection
- Hand Over an Opportunity
- Review a Lost Opportunity

The first release also included the shared methodology, responsible-use rules, fictional worked examples, a common scoring rubric and the first cross-model comparison.
