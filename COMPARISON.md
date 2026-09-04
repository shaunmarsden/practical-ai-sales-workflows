# Comparison With Similar Projects

Public repositories offering reusable AI instructions for B2B sales are not scarce, and several are far more popular than this one. If you are deciding whether to use this repository, you should be able to see how it differs without taking my word for it.

So this page compares by structure rather than by quality: whether a repository publishes a worked example, a score for its own output, the rubric behind that score, evidence from real work, and a score from somebody other than its author. Those are checkable. Whether the writing is any good is not something I can fairly judge about other people's work.

Star counts and structure as I found them on 4 September 2026. Method: I read each repository's file tree, then opened up to eight of its skill files and searched the text inside them, because a first pass that only looked at file and folder names got one of these rows wrong. A dash means I could not find it, not that it does not exist.

| Project | Stars | Shape | Worked example | Published score | Stated rubric | Real-use log | Outside scoring |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| **practical-ai-sales-workflows** (this) | 2 | 17 sales jobs, 17 skills, 15 workflows | Yes, fictional, [linked from every job](EVIDENCE-STATUS.md) | Yes, one to four scored cases per job, [listed in the matrix](EVIDENCE-STATUS.md) | Yes, [ten areas out of 50](evaluations/sales-ai-output-rubric.md) | Yes, [14 of 17 jobs](CHANGELOG.md#real-use-findings) | **No, none** |
| [OneWave-AI/claude-skills](https://github.com/OneWave-AI/claude-skills) | 285 | About 200 skills across sales, marketing, design, engineering | Reference material inside skills | Not found | Rubrics the skills apply, not for scoring output | Not found | Not found |
| [w95/awesome-claude-corporate-skills](https://github.com/w95/awesome-claude-corporate-skills) | 189 | 166 skills grouped by corporate role | `examples/` folders, holding instructions rather than outputs | Not found | Not found | Not found | Not found |
| [vonarmen-wq/forward-deployed-selling](https://github.com/vonarmen-wq/forward-deployed-selling) | 74 | Enterprise sales methodology, capabilities and references | **Yes, a labelled teaching artifact on a fictional company** | Not found | Not found | Not found | Not found |
| [matteotitta/genesys-skills](https://github.com/matteotitta/genesys-skills) | 35 | 168 skills for B2B SaaS go-to-market | Output templates per skill | Not found | **A scoring harness, though no rubric files ship with it** | Not found | Not found |
| [TheCraigHewitt/sales-skills](https://github.com/TheCraigHewitt/sales-skills) | 21 | 21 skills across the B2B sales lifecycle | **Yes, inline in the skill files, 4 of 8 I sampled** | Not found | Not found | Not found | Not found |
| [Prospeda/gtm-skills](https://github.com/Prospeda/gtm-skills) | 21 | About 2,500 prompts for sales and go-to-market | Not found | Not found | Not found | Not found | Not found |

## Honest Notes

**vonarmen-wq/forward-deployed-selling** does the worked-example discipline properly, and in one respect better than I do. Its canonical example labels itself a teaching artifact, states that the company is fictional, and says outright that its citations are placeholders showing where real sources would attach. That last sentence is more careful than most of what is published in this space, mine included in places.

**matteotitta/genesys-skills** ships the only scoring machinery in the table: a deterministic harness that scores a finished artifact out of 100 and returns pass or fail. Two honest qualifications. It expects a per-skill `rubric.json` that you supply, and I found no rubric files in the repository, so the criteria are yours rather than published. And it scores a different thing from my rubric, structural completeness rather than evidence fidelity. A repeatable gate on output shape is still a real piece of engineering that this repository does not have.

**OneWave-AI/claude-skills** and **w95/awesome-claude-corporate-skills** are far larger and far more used than this repository, roughly a hundredfold on stars. Breadth is a real service: somebody looking for a skill they can use today is better served by 200 than by 17.

**TheCraigHewitt/sales-skills** is the closest in shape to this one, a set of named sales jobs with an instruction for each, and it does the worked-example discipline inside its skill files rather than in a separate folder. One of its examples is explicitly labelled the quality bar for the output, which is a good idea I have not used.

The two repositories overlap less than I first assumed, and I checked rather than guessing. Clear equivalents are objection handling, pipeline review and win-loss against my lost-opportunity review, with call debrief close to my post-call follow up. Theirs then goes wider than mine on outbound channels and commercial mechanics: cold call, direct mail, event networking, referral intros, negotiation, proposal pricing, sales comp, forecasting and demo scripts have no equivalent here. Mine goes deeper into mid-deal diagnosis: briefing a champion, CRM honesty, spotting the real blocker, a stalled decision, an opportunity handover and a fit check have no equivalent there. About a third of either list maps onto the other.

**Prospeda/gtm-skills** is the volume play, about 2,500 prompts across sales and go-to-market.

## Where This Repository Loses

**Outside scoring: nobody has done it, here or anywhere in the table.** Every score in this repository was produced by one person, me, scoring against a rubric I wrote, having also run the test. That is the single largest limitation of everything here, it is stated in [Evidence Status](EVIDENCE-STATUS.md) and in every evaluation, and no amount of further self-testing addresses it. I have not solved a problem the rest of the niche has; I have written mine down.

**Two stars.** Popularity is not evidence of quality, but it is evidence of use, and use is how problems get found. The repositories above it in the table have had far more contact with real readers than this one has.

**Fewer jobs than most.** Seventeen against 21, 166, 168 and about 200. If you want coverage, this is not the repository with the most of it.

**No fictional test here has been run twice.** Every scored evaluation in this repository is a single run. Where a job shows two, three or four scored cases, those are different scenarios, not repeats of the same one, so none of them tells you whether a score would hold on a second attempt. That matters because I have measured what a single run is worth, on a sibling project rather than here: repeating one identical prompt on identical input moved its score by up to five points, and a seven-point gap turned out to be as little as two. Not one score in this repository has had that check.

## What This Repository Has That the Others Do Not

One thing, and it is narrow: **published scores for its own outputs, against a stated rubric, with the failures written down.** Every one of the seventeen jobs has at least one scored evaluation showing what the output got wrong as well as right, and fourteen have a logged finding from real sales work.

That is worth exactly what one person's scoring is worth, which is the point of the previous section.

## If I Have Got Something Wrong

If your project is in this table and I have mischaracterised it, or it belongs here and is missing, [open an issue](https://github.com/shaunmarsden/practical-ai-sales-workflows/issues/new) or [say so in Discussions](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions) and I will correct it. My method is described at the top and it is still a sample: a file tree plus up to eight skill files read per repository. A first version of this page looked only at file and folder names and got a row wrong, marking a repository as having no worked example when four of its eight skill files carried one inline. If I have made the same kind of mistake somewhere I have not looked, tell me and I will fix it rather than defend it.
