# Changelog

This is the completed-work archive. The [roadmap](ROADMAP.md) now stays focused on what is current and what may happen next.

Release notes provide the fuller version summaries:

- [v1.2.0: Safer Orchestration and Better Evidence](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.2.0)
- [v1.1.0: More Workflows, Better Routes and Real Evidence](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.1.0)
- [v1.0.0: First Complete Set of Sales Workflows](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.0.0)

## Unreleased

### All Seventeen Skills Now Tell the Model Not to Use Em Dashes

- Only four of seventeen did. The style rule forbids them and a check enforces it on every tracked file including published outputs, so every output from the other thirteen had to be hand-converted before it could be committed. That is where a record saying "reproduced unedited" after a silent edit came from.
- **[Tested over thirty-three runs](evaluations/em-dash-rule-test.md).** Twenty-eight earlier runs of Build a Business Case, none carrying the rule, all contained em dashes, between ten and thirty-one each. Five runs with the rule contained none, and no en dashes either. One-tailed p of 0.0000042. The baseline came free from three earlier tests, so no control arm was needed.
- The stacked-figure guardrail still holds alongside it. All five runs cited Finance's thirty-five pound rate, one in words, and none combined it with the untimed estimate. The two instructions do not interfere.
- A new check stops a skill added later shipping without the rule. Retro-tested against the state before this change: it fires on exactly the thirteen.
- **This is a maintenance and disclosure fix, not an output-quality one**, and the page says so. Nothing about a business case is worse for containing an em dash. It also says plainly that one skill was tested while thirteen were changed, which is a weaker claim than the guardrail's.
- In Identify Buyer Indecision the rule is a numbered, bold-labelled directive rather than a bullet, because that file's list is numbered and bold-labelled. A first pass appended a plain bullet and broke the format.

### The Guardrail Is Not Too Blunt

- The [stacked figure test](evaluations/business-case-stacked-figure-test.md) named one worry about the guardrail it had just supported: the scored run refused so thoroughly that a CFO got no sense of scale. Six more blind runs tested whether it also suppresses arithmetic that is sound, three each on Hartwell and Bramfield, the two business case scenarios that carry a confirmed seat count and a confirmed per-seat price.
- **All six produced the combined total, and every figure is correct.** £4,320 a year on Hartwell in three of three; £18,720 for year one on Bramfield in three of three, with £16,200 for year two, £1,560 a month and £34,920 across both years appearing in two each. The criterion and the contingency were both fixed before any run, and by that contingency no control arm was needed.
- The criterion was not mine to choose. Hartwell's own reference file already says "the annual total can be calculated from it", so the repository had already decided that arithmetic is expected there.
- Two checks made while the outputs were open, neither of them the criterion: all three Bramfield runs attached the two-year condition to the discounted year-two rate, which is that scenario's headline trap, and none of the six combined an unmeasured figure with money.
- **This corrects an attribution rather than a claim.** The Aldercroft run scored four for commercial usefulness because a CFO got no sense of scale, and I put that down to the instruction. On this evidence it was the scenario: Aldercroft has nothing measured to combine, so refusing was correct and the missing scale is the source material's fault.
- Twenty-five runs across the two tests. The guardrail blocks what it was written to block and permits what it should permit, so this thread is closed.

### A Guardrail That a Test Actually Supported

- The previous test found a real defect: four of six runs of Build a Business Case multiplied an untimed estimate by an approximate planning rate into one pound figure, and one annualised it. A [guardrail](.agents/skills/build-business-case/SKILL.md) against combining two unmeasured figures was written for it and then [tested over nineteen runs](evaluations/business-case-stacked-figure-test.md) in a two by two, criterion fixed in writing first.
- **Supported and kept.** None of the ten runs carrying the guardrail produced a combined figure. Four of the nine without it did. Guardrail alone against the plain baseline is zero of five against three of five; collapsing over the other variable it is zero of ten against four of nine, one-tailed p of 0.033. This is the first change to this repository that a test has supported rather than rejected or failed to separate from noise.
- **The design had to change partway through, because of something I had written myself.** The note added in the previous test warns a human reader that this defect exists, and these files are pasted into a model as instructions, so it was also instructing the model. Ten further runs were added to separate the two. The warning's own effect turned out to be indistinguishable from noise and no claim is made for it.
- **A mistake inside the test is recorded on the page.** After the first nine runs I reported that the warning had probably suppressed the defect on its own. That rested on a three-run baseline of two of three; two more baseline runs moved it to three of five and the comparison evaporated. Over-reading a three-run baseline is the exact error this line of testing exists to avoid.
- The worst of the nineteen runs came from the skill as it stood: £2,520 a week, annualised to £131,000, plus £65,000 a year of projected reclaimed capacity, all from two unmeasured inputs and one gut feel, put in front of a CFO as illustrative.
- Named next: whether the guardrail is too blunt. The scored run kept the two inputs in separate sections rather than adjacent with their labels, which is more than the instruction asks and leaves a reader with no sense of scale.

### A Test That Rejected Its Own Hypothesis, and Corrected a Published Claim

- The [business case prompt review](evaluations/aldercroft-business-case-prompt-review.md) said the prompt outscored the skill partly because it requires a human-check section and the skill did not. One line was added to the skill to test that, and then it was actually tested: [six blind runs](evaluations/business-case-check-requirement-test.md) of the same scenario, three on the skill as published and three with the line, with the criterion and the falsification condition written down before any run.
- **The hypothesis was rejected.** Two of three unmodified runs already named the absent pilot cost, so the published record's miss was inside the skill's own variation rather than caused by a missing instruction. All three unmodified runs also produced a human-check section without being told to, so the section was never the variable. The prompt review and the skill file are both corrected in place rather than quietly left standing.
- **The added line is kept and labelled as weakly evidenced, not as a fix.** Three runs each cannot separate three from three against two from three. It stays because one unmodified run is a real instance of the failure it describes, and the page says plainly that reverting one line is the whole cost of preferring no unevidenced changes at all.
- Two better-evidenced findings came out of the same six runs. **Four of six runs multiplied an untimed estimate by an approximate planning rate into a single pound figure**, one annualised to £131,000, and the worst run of the six came from the published version of the skill. That is a replicated defect rather than a hypothesis, and it is named as the next change to test with the criterion already fixed.
- **Every one of the six runs used em dashes**, between thirteen and twenty-three each. Only four of seventeen skills and four of twenty-one prompt templates tell the model not to, and this skill is not one of them. The chase prompt, which does carry the rule, produced none. Since the style check forbids the character in every tracked file including published outputs, and no example here discloses a punctuation conversion, the [new output](examples/aldercroft-business-case-check-requirement-output.md) discloses its own and says which replacements were judgement rather than a mechanical swap.

### Every Recipe Card Now Has a Prompt on It

- The [Build a Business Case card](recipes/build-a-business-case.md) was the last of the seventeen with nothing to paste. A [business case prompt](templates/business-case-prompt.md) now exists, condensed from the skill, and the card carries it. All seventeen cards are now genuinely one page.
- It was [scored on its own](evaluations/aldercroft-business-case-prompt-review.md) on Aldercroft, the hardest of the three business case scenarios: **49 out of 50**, run blind in an isolated context with the answer key stripped first. The skill scored 46 on the same scenario.
- **That three point gap is not a result, and the record says so twice.** One to three points is inside the run-to-run movement already measured here. More importantly, one of the three points is plausibly my own design choice rather than the model's judgement: the prompt makes a human-check section a required numbered part listing every figure needing confirmation, and the skill leaves it to be produced voluntarily. The skill's run produced one anyway and it did not flag the missing pilot cost; the prompt's run did. That is testable by adding the same requirement to the skill, which the review names as the next change and the skill file now says out loud.
- The run also caught something the scenario's own answer key does not list: no solution or product name was ever established on the call, and it said so rather than quietly naming one. It declined to multiply two unmeasured figures into a headline saving, which is exactly what cost the skill's run a mark. And it produced one applied example instead of the three asked for, explaining why rather than padding, which is the place a second scorer is most likely to disagree with me.
- Reviewing this turned up a gap in my earlier scoring rather than in either output: neither run produced the three applied examples both artefacts ask for, and the skill's review never flagged it.

### A Prompt for the Chase Card, Written and Scored

- The [Chase a Quiet Prospect card](recipes/chase-a-quiet-prospect.md) had nothing to paste. It is the most-visited card in this repository and its only route to doing the job was a skill file that opens by saying it is not written to be read start to finish. A [chase sequence prompt](templates/chase-sequence-prompt.md) now exists, condensed from the skill, and the card carries it.
- It was [scored on its own](evaluations/hartwell-chase-prompt-review.md) rather than borrowing the skill's result: **46 out of 50** on the fictional Hartwell scenario, run blind in an isolated context with the scenario's answer key stripped first. The skill scored 48 twice on the same scenario. That two point gap is inside the run-to-run movement this repository has already measured, so it is not evidence the prompt is worse, and the record says so.
- What the prompt's run missed is worth more than the total. Alex promised the transcript by Thursday and then went away from the 8th, and the case is built so those two conflict. The run handled the conditional approval well and repeatedly, and never mentioned Thursday. The skill's run did. Whether the prompt's stale-date instruction reads too narrowly or one run was unlucky needs a second run to separate, and the review names that as the next change to test rather than guessing.
- Build a Business Case is now the only card without a prompt, and a new check keeps the stated count honest. Check 18 counts skills, workflows and cards, not cards carrying a prompt, so "sixteen of the seventeen" had nothing watching it.

### The Evidence Now Links From the Skills People Actually Open

- Twelve skill files now link the scored evidence behind them. Repository traffic showed that the skills are what visitors open, while the evidence status page, the comparison and the evaluations folder pull almost nothing, so the evidence was sitting where nobody looks. Eleven of those twelve link a scored evaluation they did not link before. This adds no new evidence, it makes what already existed reachable from the instruction sheet rather than two clicks away or not at all.
- Five skills also link [Sales Proof Bench](https://github.com/shaunmarsden/sales-proof-bench) where one of its fictional cases covers the same job: pre-call prep, the follow-up email, the post-call evidence pack, objection diagnosis and the business case. Those bench runs used a bare task request with no method attached, so each link says plainly that it shows what the job looks like without a skill rather than testing the skill. The bench has never tested a skill, and none of these lines claim it has.
- Every skill except the Workflow Router now reaches a scored evaluation from its own file or its worked example. No evaluation of the router exists yet.

### A Second Lost-Opportunity Real-Use Finding

- Logged a [real-use recovery finding](evaluations/lost-opportunity-recovery-real-use-finding.md) for Review a Lost Opportunity. A real opportunity that had stopped responding was reviewed against the method, a different and more senior route was identified, and outreach the salesperson approved was followed by a positive reply and a booked call. The finding states plainly that one case does not show the method or the AI caused either, and that nothing is known about whether the opportunity closed. It sits alongside the earlier no-decision finding rather than replacing it, since that one records the review correctly refusing to act.

### The Outbound Campaign Review, Tested on Real Work

- Reviewed a real, completed three-round outbound campaign against [the outbound campaign learning review](workflows/14-outbound-campaign-learning-review.md) and logged the [finding](evaluations/outbound-campaign-real-use-finding.md). The campaign produced no replies and no calls from 45 prospects, and roughly a fifth of the addresses bounced, so the list failed before the messages could be tested. Nearly every variable moved on nearly every prospect, 43 distinct angles across 45 prospects, which means the messaging is untested rather than disproved and nothing is attributable. Reviewing real records also exposed three gaps a fictional example cannot: delivery is not recorded, only bounces; meetings attended and qualified opportunities have no column; and the call to action is not captured at all. What to keep, stop or test next stays a human decision, as the method requires.

### A Third Objection-Handling Test

- Added a third fictional test for Handle an Objection (Thornbury Housing Association), where the surface wording of the objection matches an ordinary circumstances or budget objection exactly, and the standard, factually correct playbook answer to that bucket is precisely the wrong move, since the prospect already accepted the underlying fact and was raising something else entirely (internal optics during a sensitive period). Scored 47 out of 50; the skill correctly avoided re-arguing a settled point and avoided manufacturing urgency during a sensitive period.
- Updated the evidence-status matrix's Handle an Objection row to reflect four scored tests rather than three.

### A Harder Fit and Limitations Test

- Added a second fictional test for Check Whether It Actually Fits (Aldermere Pharmaceuticals), where two teams both raise something described as a "compliance" issue, meaning genuinely different things: a structural capability gap (no GxP validation) for one, and an administrative step with a known precedent (a data processing agreement) for the other. Scored 47 out of 50; the skill correctly kept the two apart rather than generalising one word into one shared verdict.
- Updated the evidence-status matrix's Check Whether It Actually Fits row to reflect two scored cases rather than one.

### A Harder Real-Blocker Test

- Added a second fictional test for Spot the Real Blocker (Oakriven Facilities Group), where the enthusiastic contact himself proposes a plan to get an enrolment far enough along that the actual decision-maker would face something already done rather than a genuine upfront choice. Scored 47 out of 50; the skill correctly named the proposed process itself as the thing to avoid, not only the underlying authority as unconfirmed, and correctly declined to treat the contact's optimism as bad faith.
- Updated the evidence-status matrix's Spot the Real Blocker row to reflect two scored cases rather than one.

### A Fourth Objection-Pattern Test, Inverted

- Added a fourth fictional log for Spot a Real Objection Pattern that inverts the series' usual trap: instead of similar wording hiding different drivers, two entries with opposite-looking behaviour, an abrupt call termination out of suspicion and a calm professional request for an NDA and a reference call, share the same underlying legitimacy driver. The pattern rests on exactly two distinct deals, the smallest sample this skill's own rules treat as a candidate at all, and the review correctly held it at low confidence rather than overstating it. Scored 47 out of 50.
- Updated the evidence-status matrix's Spot a Real Objection Pattern row to reflect four scored tests rather than three.

### Spot the Real Blocker

- Added a seventeenth sales job: a workflow, skill, portable prompt, recipe card, fictional Rowcastle test and scored evaluation for checking whether the person on a call is actually the decision-maker, and whether their stated objection is the real one or standing in for something unstated. Added to the workflow router's table, alongside a fix for Review an Outbound Campaign, which had no route in that table at all.
- One fictional test only. No independent or real-use evidence yet.

### Harder Objection-Handling Tests

- Added a harder fictional test for Handle an Objection, built around the objection-response skill's own stop condition: a genuine contractual question nobody on the call has actually confirmed, rather than another diagnosis case. Scored 47 out of 50; the skill correctly refused to resolve the clause in either direction and reframed toward the specific unconfirmed question instead.
- Wired in an existing but previously unlinked stability test that runs a deliberately ambiguous objection three times each across three different models and checks whether the diagnosed driver holds steady. It did not, by design: the point of the test is that a genuinely ambiguous objection can reasonably diagnose to more than one driver, and the test surfaces that rather than hiding it.
- Updated the evidence-status matrix's Handle an Objection row to reflect three scored tests rather than one.

### Harder Buyer-Indecision Test

- Added a harder fictional test for Move a Stalled Decision (Wrenmoor Analytics / Farrah Osei), where each stated reason to delay is individually legitimate and genuinely gets resolved, only for a new, unrelated reason to appear immediately after. Scored 46 out of 50; the skill correctly declined to read the first two reasons as indecision while they were still open, and correctly did not accept a dated, plausible-looking team offsite as a clean external blocker once it was the third reason in the same pattern.
- Updated the evidence-status matrix's Move a Stalled Decision row to reflect two scored cases rather than one.

### Harder Business-Case Test

- Added a third fictional test for Build a Business Case (Aldercroft Group / Tomasz Nowicki), built entirely from pre-pilot projections rather than measured pilot results. Scored 46 out of 50; the skill correctly asked for pilot approval rather than rollout approval, matching what was actually agreed, and correctly excluded an unconfirmed future headcount number that would have inflated the projected saving.
- Updated the evidence-status matrix's Build a Business Case row to reflect three scored cases rather than two.

### Harder Objection-Pattern Test

- Added a third fictional test for Spot a Real Objection Pattern, an eight-entry log where five distinct applicants stall or withdraw after learning a personal enrolment actually requires an employer attestation, alongside two decoy entries that share the surface shape of the pattern, someone else's input being needed, but not its actual driver: a spouse and a household budget decision in one, an explicitly unrelated new job in the other. Scored 47 out of 50; the skill correctly excluded both decoys by reading what the applicants actually said, rather than grouping by stage or outcome shape alone.
- Updated the evidence-status matrix's Spot a Real Objection Pattern row to reflect three scored tests rather than two.

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

Fifteen jobs have a logged finding from sanitised real sales work. Twelve are summarised below, and four have a dedicated file because each carries a caveat worth reading in full. Those do not add to fifteen because Review a Lost Opportunity appears in both: the earlier no-decision summary is below, and the later recovery case has its own file.

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

The four with a dedicated file:

- **Move a Stalled Decision:** [a real-use boundary finding](evaluations/buyer-indecision-real-use-finding.md). A real opportunity was correctly classified as a policy and timing blocker rather than buyer indecision, so this shows the method declining to fire rather than firing well.
- **Hand Over an Opportunity:** [a real-use finding across eleven handovers](evaluations/opportunity-handover-real-use-finding.md). Evidence for the underlying method, and explicitly not yet a test of the current public skill unchanged.
- **Review a Lost Opportunity:** [a recovery finding](evaluations/lost-opportunity-recovery-real-use-finding.md), where the review identified a different route and the approved outreach was followed by a reply and a booked call. The no-decision summary above is the same job's earlier finding.
- **Review an Outbound Campaign:** [a real campaign reviewed against the method](evaluations/outbound-campaign-real-use-finding.md). No replies and no calls from 45 prospects, with roughly a fifth of the addresses bouncing, so the finding is mostly about the list and the records rather than the messages.

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
