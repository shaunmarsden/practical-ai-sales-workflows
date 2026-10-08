# Comparison With Similar Projects

There are plenty of public repositories of reusable AI instructions for B2B sales, and several are far more popular than this one. If you're deciding whether to use this one, you should be able to see how it differs without taking my word for it.

So this page compares structure, not quality. Does a repository publish a worked example, a score for its own output, the rubric behind that score, evidence from real work, and a score from someone other than its author? You can check those. I can't fairly judge whether other people's writing is any good.

Star counts and structure are as I found them on 4 September 2026. I read each repository's file tree, then opened up to eight of its skill files and searched the text inside them. A dash means I couldn't find it, not that it isn't there.

| Project | Stars | Shape | Worked example | Published score | Stated rubric | Real-use log | Outside scoring |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| **practical-ai-sales-workflows** (this) | 2 | 17 sales jobs, 15 workflows, 17 skills (15 jobs have one, and the 17 include the router and a second follow-up skill) | Yes, fictional, [linked from every job](EVIDENCE-STATUS.md) | Yes, one to four scored cases per job, [listed in the matrix](EVIDENCE-STATUS.md) | Yes, [ten areas out of 50](evaluations/sales-ai-output-rubric.md) | Yes, [16 of 17 jobs](CHANGELOG.md#real-use-findings) | **No, none** |
| [OneWave-AI/claude-skills](https://github.com/OneWave-AI/claude-skills) | 285 | About 200 skills across sales, marketing, design, engineering | Reference material inside skills | Not found | Rubrics the skills apply, not for scoring output | Not found | Not found |
| [w95/awesome-claude-corporate-skills](https://github.com/w95/awesome-claude-corporate-skills) | 189 | 166 skills grouped by corporate role | `examples/` folders, holding instructions rather than outputs | Not found | Not found | Not found | Not found |
| [vonarmen-wq/forward-deployed-selling](https://github.com/vonarmen-wq/forward-deployed-selling) | 74 | Enterprise sales methodology, capabilities and references | **Yes, a labelled teaching artifact on a fictional company** | Not found | Not found | Not found | Not found |
| [matteotitta/genesys-skills](https://github.com/matteotitta/genesys-skills) | 35 | 168 skills for B2B SaaS go-to-market | Output templates per skill | Not found | **A scoring harness, though no rubric files ship with it** | Not found | Not found |
| [TheCraigHewitt/sales-skills](https://github.com/TheCraigHewitt/sales-skills) | 21 | 21 skills across the B2B sales lifecycle | **Yes, inline in the skill files, 4 of 8 I sampled** | Not found | Not found | Not found | Not found |
| [Prospeda/gtm-skills](https://github.com/Prospeda/gtm-skills) | 21 | About 2,500 prompts for sales and go-to-market | Not found | Not found | Not found | Not found | Not found |

## Notes on Each Project

**vonarmen-wq/forward-deployed-selling** does worked examples properly, and in one way better than I do. Its main example calls itself a teaching artifact, says the company is fictional, and says plainly that its citations are placeholders showing where real sources would go. That last sentence is more careful than most of what I read for this page, some of mine included.

**matteotitta/genesys-skills** has the only scoring machinery in the table: a harness that scores a finished artifact out of 100 the same way every time and returns pass or fail. Two catches. It expects you to supply a `rubric.json` for each skill, and I found no rubric files in the repository, so you set the criteria; they aren't published. And it scores something different from my rubric: whether the structure is complete, not whether the output sticks to the evidence. Still, a repeatable check on output shape is real engineering that this repository doesn't have.

**OneWave-AI/claude-skills** and **w95/awesome-claude-corporate-skills** are far bigger and far more used than this repository, about a hundred times more on stars. Breadth matters: if you want a skill you can use today, 200 serve you better than 17.

**TheCraigHewitt/sales-skills** is the closest in shape to this one: a set of named sales jobs with an instruction for each. It puts its worked examples inside its skill files rather than in a separate folder. One example is labelled as the quality bar for the output, which is a good idea I haven't used.

The two repositories overlap less than I first thought, and I checked rather than guessed. The clear matches are objection handling, pipeline review, and their win-loss against my lost-opportunity review. Their call debrief is close to my post-call follow up. Theirs then goes wider than mine on outbound channels and deal mechanics: cold call, direct mail, event networking, referral intros, negotiation, proposal pricing, sales comp, forecasting and demo scripts have no match here. Mine goes deeper into what's going wrong mid-deal: briefing a champion, CRM honesty, spotting the real blocker, a stalled decision, an opportunity handover and a fit check have no match there. About a third of each list maps onto the other.

**Prospeda/gtm-skills** goes for volume, with about 2,500 prompts across sales and go-to-market.

## Where This Repository Loses

**No outside scoring, here or anywhere in the table.** I produced every score in this repository myself, against a rubric I wrote, after running the test myself. That's the biggest weakness of everything here. [Evidence Status](EVIDENCE-STATUS.md) and every evaluation say so, and more testing by me can't fix it. I haven't solved a problem the rest of the field has; I've written mine down.

**Few stars.** The table shows two on 4 September 2026, and GitHub showed four on 8 October 2026. Popularity doesn't prove quality, but it does show use, and use is how problems get found. The repositories above this one have had far more contact with real readers.

**Fewer jobs than most.** Seventeen against 21, 166, 168 and about 200. If you want the most coverage, this isn't the repository for it.

**Most of the fictional tests here are single runs.** The [ambiguous objection stability test](evaluations/hartwell-objection-ambiguous-test.md) ran one input nine times, three each across three models. Claude scored 46 to 49 but picked a different main diagnosis in every run, while ChatGPT and Gemini stayed on the same one. Three more tests have been [repeated once each](evaluations/repeat-run-findings.md): one held exactly and two came out higher. A further 16 compared an instruction with and without one change, mostly on the business case and chase jobs, usually with six runs a version. [Evidence Status](EVIDENCE-STATUS.md) lists all 18. Everything else is a single run. Where a job shows two, three or four scored cases, those are separate scenarios, not repeats.

## What This Repository Has That the Others Do Not

One thing, and it's narrow: **published scores for its own outputs, against a stated rubric, with the failures written down.** Every one of the seventeen jobs has at least one scored evaluation showing what the output got wrong as well as right, and sixteen have a logged finding from real sales work.

That's worth exactly what one person's scoring is worth, as the last section says.

## If I Have Got Something Wrong

If your project is in this table and I've described it wrongly, or it belongs here and isn't, [open an issue](https://github.com/shaunmarsden/practical-ai-sales-workflows/issues/new) or [say so in Discussions](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions) and I'll correct it. My method is at the top, and it's still a sample: a file tree plus up to eight skill files per repository. If I've made a mistake somewhere I haven't looked, tell me and I'll fix it rather than defend it.

## Corrections

An earlier version of this page said none of the tests here had ever been run twice. That was wrong: the ambiguous objection stability test had already run one input nine times.

A first version of this page looked only at file and folder names. It got a row wrong, marking a repository as having no worked example when four of its eight skill files had one inline. That's why I now open the skill files as well.
