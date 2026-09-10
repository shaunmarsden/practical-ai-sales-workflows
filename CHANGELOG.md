# Changelog

This is the completed-work archive. The [roadmap](ROADMAP.md) now stays focused on what is current and what may happen next.

Release notes provide the fuller version summaries:

- [v1.2.0: Safer Orchestration and Better Evidence](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.2.0)
- [v1.1.0: More Workflows, Better Routes and Real Evidence](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.1.0)
- [v1.0.0: First Complete Set of Sales Workflows](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.0.0)

## Unreleased

### The Same Step on the Skill, and a Prediction I Got Wrong

- The ledger step adopted into the chase prompt yesterday was in the prompt only, and its page named the limit. **[Tested on the skill over twelve runs](evaluations/chase-skill-ledger-test.md), six a side: six of six against zero of six, one-tailed p of 0.0011.** Neither failure condition fired, so it is adopted there too.
- **I wrote down a prediction beforehand and it was wrong.** I expected the published skill to do better at this than the published prompt, on the strength of the repeat run findings. It scored zero of six where the prompt scored two of six, so the stronger result comes from the skill being worse to begin with rather than from the step working better there.
- **The apparent contradiction was checked rather than reasoned about.** The repeat run findings say the skill "showed the conflict"; the published output actually says the leave dates "suggest" the Thursday timing does not stand, under a heading of things to confirm, which is the hedged form this criterion counts as a no. The earlier scoring was looser, not a different result, and that page now says so.
- **The step worked and half its instruction did not.** Five of the six ledger runs printed the ledger as a dated list and a collisions section, despite being told it is a working step and not part of the output. In the prompt test none of the six did. The same words sit as a paragraph above the output sections in the prompt and as a section among them in the skill, and that placement flipped the behaviour. Named as an open question rather than quietly reworded, since no test here supports either choice.
- **Forty-eight runs across four tests on this thread, and every one decided to wait rather than chase.** All of this has been about one supporting fact inside a correct decision.
- Still untested after both ledger tests: whether the step costs anything on a scenario where no dates collide, which is the case the instruction's "including when nothing collides" clause was written for.

### A Required Step Beat a Principle, on the Third Attempt

- Three tests have now gone at the chase prompt missing the clash between the transcript Alex promised by Thursday afternoon and the leave he announced the next day. Widening the instruction was rejected. Naming the weekday in the scenario, which turned out to be necessary before the clash could be established at all, was rejected too.
- **[Tested over twelve runs](evaluations/chase-dated-commitment-ledger-test.md), six a side, and this one is adopted.** One paragraph asks for a dated commitment ledger before drafting: list every date and commitment including the ones the prospect set themselves, list every stated period of absence separately, compare them, and carry the result into the first section in words. Five of six runs stated the clash, against two of six without it.
- **The page says plainly that the evidence is weaker than the table looks.** One-tailed p of 0.12 does not reach the level treated as a result elsewhere here, and the pre-registered condition was a threshold rather than a significance test. What holds is that the mechanism was not falsified on a thread where two previous changes were.
- A pooled figure of three of twelve against five of six, p of 0.032, is on the page as a post-hoc calculation with a warning attached, since pooling arms across sessions was not pre-registered and is the move criticised on the stacked figure test.
- **This is the second time a principle failed here and a required step worked**, after the invented-pronoun failure, and the second time I reached for the rule first. Both are now on [Which AI Mistakes Actually Get Through](guides/which-ai-mistakes-get-through.md).
- Four of the six ledger runs visibly did the comparison, one stated the clash without showing the working, and **one skipped the step entirely**, which is worth knowing about required steps. No run printed the ledger, which was the pre-registered observation.
- **Thirty-six runs across the three tests, and every one of them decided to wait rather than chase.** This whole thread has been about one supporting fact inside a correct answer.
- The baseline moved from one of six to two of six between sessions on the same prompt and the same input, which is the run-to-run movement this repository keeps measuring showing up inside a six-run cell. The void condition written into the pre-registration existed for exactly that.
- The step is in the [prompt](templates/chase-sequence-prompt.md) and the recipe card only. The skill does not carry it and has not been tested with it.

### The Objection Workflow Linked Its Stability Test and Carried None of It

- [Objection Handling](workflows/05-objection-handling.md) promised "a diagnosis of what is really driving the objection" and linked the [nine-run stability test](evaluations/hartwell-objection-ambiguous-test.md) as further reading, without carrying anything that test found. A reader who never clicked got no hint that the diagnosis is the unstable part.
- **What it found is that the guardrails held on all nine runs and the diagnosis did not.** One model promoted a different primary driver in each of its three runs while the other two stayed on one. The method section now says to treat the bucket as a hypothesis the reply can test rather than a settled answer, and the link text says what the test showed instead of only that it exists.
- **It also dropped the one signal the skill singles out.** The [skill](.agents/skills/objection-response/SKILL.md) says to watch for an objection that shrinks the rationale rather than delaying the decision. The workflow's six buckets had no room for it, and on the nine-run test that reading was the sharpest one available and only one run in nine surfaced it. It is now in the method.
- The six buckets themselves match the skill exactly, which was the first thing checked.

### Naming the Weekday Did Not Fix the Behaviour Either

- The chase scenario was changed yesterday to name its weekdays, because its answer key claimed a date conflict the input never established. **[Re-run twelve times, six a side](evaluations/chase-weekday-rerun.md), and the fix did not produce the behaviour the answer key asks for.** One of six runs stated that the promised Thursday falls inside Alex's leave, against none of six on the version without weekdays. The interest condition set beforehand was met.
- **The change stays**, because it fixed an over-claim rather than a behaviour. An input a reader cannot verify is a defect whether or not fixing it moves a model.
- **Both candidate causes for the original miss are now eliminated.** The [stale-date test](evaluations/chase-stale-date-test.md) rejected the instruction being too narrow, and this rejects the input being unstateable. The requirement still goes unmet five times in six, and nobody has found why.
- A post-hoc cell, labelled as one: three of the six runs with weekdays stated the promised date as 9th July, which none of the six without them could. One-tailed p of 0.09, not the pre-registered observation, and no claim attached. If it is real it says only that stating a date is not the same as noticing what it collides with.
- The pre-registered observation came back clean: no run miscomputed the date, and all twelve decided to wait rather than chase, which is the decision the scenario asks for. This is a failure to surface one supporting fact, not a wrong answer.
- **The judgement call inside the scoring cuts against the result rather than for it.** One run reads close to the criterion without meeting it, and it is in the arm without weekdays, so a looser reading makes the comparison one of six against one of six.
- [Which AI Mistakes Actually Get Through](guides/which-ai-mistakes-get-through.md) said the cause of this miss was unknown. It still is, and the bullet now names both eliminated explanations rather than leaving the question open in the abstract.

### The Chase Scenario Now Names Its Weekdays

- The [stale-date test](evaluations/chase-stale-date-test.md) found that the chase scenario's answer key claimed a date conflict the input never established: it gave dates without weekdays, so nobody could tell whether the Thursday Alex promised actually fell inside his later leave. Three of twelve runs said so and a fourth asserted the conflict as fact.
- **The call is now Tuesday 7th July.** That puts the promised Thursday afternoon at 9th July, two days into a leave that began on the 8th, with the CRM task falling due the day after it. The clash is established by the dates rather than inferred from them, and the answer key says so instead of over-claiming.
- **This changed published test material, so every record scored against the earlier version says so.** The [chase decision review](evaluations/hartwell-chase-review.md), the [chase prompt review](evaluations/hartwell-chase-prompt-review.md), the [repeat run findings](evaluations/repeat-run-findings.md), the stale-date test itself and both worked outputs each carry a line saying they were scored or produced without the weekdays. The scenario carries its own history section too.
- Worth noting on the repeat runs: both of them showed the Thursday clash anyway, on the version where it could only be inferred.

### The Chase Prompt's Stale-Date Wording Was Not the Problem

- The [chase prompt review](evaluations/hartwell-chase-prompt-review.md) found that its run never mentioned Alex's own commitment to share the transcript by Thursday, blamed the stale-date instruction for reading as though it covered only internally set reminders, named the fix and the re-run, and then nothing happened. It was the one live proposal left on any evaluation page here.
- **[Tested over twelve runs](evaluations/chase-stale-date-test.md), six a side, and the change was not adopted.** Four of six runs of the prompt as published named the commitment, which met the falsification condition set beforehand exactly at its threshold and puts the original miss inside the prompt's own variation. Fisher's exact on the misses gives p of 0.45, and the condition was written to fire regardless of the arithmetic.
- **That is the second wording hypothesis here rejected by running the baseline properly** rather than reasoning about the instruction. All ten runs that named the commitment treated it as overtaken by the leave rather than broken, which is what the scenario asks for.
- Scored blind to which arm each run came from, as the [applied examples test](evaluations/business-case-applied-examples-test.md) was.
- **The more useful finding was not the criterion.** Three of the twelve runs noticed that the scenario never says which weekday 7th July was, so they declined to state whether the promised Thursday actually fell inside Alex's leave, and a fourth asserted that it did. They are right: the conflict follows from the dates on every reading except 7th July having been a Thursday itself, which the scenario never rules out. The answer key claimed more than the input establishes and now carries the qualification.
- Naming the weekday in the scenario would make the conflict checkable rather than inferable, and it would change published test material that three existing records were scored against. That is left as a decision rather than done quietly.

### A Review That Still Told You to Run a Test That Had Failed

- The [Aldercroft business case prompt review](evaluations/aldercroft-business-case-prompt-review.md) carried a correction banner at the top and a corrected section in the middle, and then closed by telling a reader to go and run the test that had already been run and rejected. Its last words were the open proposal.
- Fixed the same way the [check requirement test](evaluations/business-case-check-requirement-test.md) was yesterday, and found by sweeping every "Change to Test Next" section on the evaluation pages rather than only the one in front of me. Three of the five were stale: two were fixed yesterday and this is the third. Of the remaining two, one names the padding question this prompt raises, and the [chase prompt review](evaluations/hartwell-chase-prompt-review.md) names a change that has genuinely never been made.

### Fifteen Published Inputs Were Foreshadowing Their Own Answer Key

- Every fictional input here carries a note near the top saying it is fictional and what it was created to test, and the ones with an answer key carry a warning saying "copy everything above this line" for a re-run. **The note is above the line.** So a re-runner following the instruction was handed a compressed version of the answer key along with the scenario.
- The worst of them told the model that two entries which look nothing alike share the same driver, which is the entire finding that log was built to test. Others named the trap outright: that the standard correct answer is precisely the wrong move, that the word compliance means two different things, that the case is a stop condition rather than a diagnosis.
- **Fifteen inputs and six skill footers are fixed.** The disclosure now names the job and not the difficulty. What the scenario hinges on was already written out below the line or in the evaluation in every case, so nothing was lost.
- **The skill footers were the same leak through a second channel.** A skill's pointer to a harder test described what made it harder, and the skill gets pasted into the model alongside the input, so there was no line to copy above. They now say a test is harder and leave what makes it harder to its evaluation.
- **One test cannot be repaired, only recorded.** The [ambiguous objection input](examples/hartwell-objection-ambiguous-input.md) used to state that the real driver is not cleanly resolvable, which is exactly what its [nine-run test](evaluations/hartwell-objection-ambiguous-test.md) was measuring. That page never recorded where the pasted input began and ended, so whether the nine runs were given that sentence cannot be established now. The page says so.
- **[The rule in CONTRIBUTING.md caused this](CONTRIBUTING.md)**, by asking every example to say "what it was created to test" near the top. It now says to name the job and not the difficulty, and says the same for skill footers.
- **No check, and the reason is recorded.** Two mechanical proxies were tried, blockquote length and shared phrasing between the disclosure and the answer key, and neither separated the leaking files from the clean ones: the leaks ran from forty to a hundred and eleven words against clean ones from thirty-six to a hundred and thirty-nine, and two clean files shared more phrasing with their answer key than six of the leaks did. The distinction is editorial judgement, so it is written down in CONTRIBUTING rather than enforced badly.
- Found while re-running the [applied examples test](evaluations/business-case-applied-examples-test.md), which needed the Aldercroft answer key removed and turned up the leak in the part of the file the instruction says to keep. My first scoping of it was a two-word search that reported one leak; the real number was fifteen.
- **The test most affected by this now says so.** The [stacked figure test](evaluations/business-case-stacked-figure-test.md) turns on whether a run combines an unmeasured time estimate with an approximate rate, and the Aldercroft blockquote told the model that the time estimate was a live trap. It was constant across all four cells, so the comparison holds, but the absolute rates may not be what a blind input would give. That page also never recorded where the pasted input began and ended, so the hint can only be inferred from the procedure, not confirmed.
- Two presentation fixes found in the same pass. The stacked figure test's closing section had stopped naming any next change after the applied examples question closed, and it now names the live one, which is about the prompt rather than the skill. The [check requirement test](evaluations/business-case-check-requirement-test.md) still proposed the guardrail in the future tense, so a reader reached the end of it without learning that the guardrail was built, tested over nineteen runs and supported.

### The Applied Examples Test, and the Claim It Corrected

- The [stacked figure test](evaluations/business-case-stacked-figure-test.md) named this as the next question about Build a Business Case: across six runs it never produced the three applied examples the artefacts ask for. **Reading the wording before running anything showed that only the prompt asks for three.** The skill says "three is a good number", in a list where other items say "always present", and all six of those runs were runs of the skill. Four pages had turned that into an instruction being ignored. All four are corrected.
- The gap left after that correction was real and worth testing: three of those six runs produced no applied example at all, and a business case without one has dropped the part connecting a cost to the work.
- **[Tested over twelve runs](evaluations/business-case-applied-examples-test.md), six a side, and the change was not adopted.** Both arms produced at least one grounded example in all six, so the falsification condition written down beforehand was met. No run produced a second or third example either, which is the padding the guardrail exists to prevent. Nothing in the skill changed.
- **The runs were scored blind to which version each came from**, using a mapping generated and never displayed until scoring finished. That is new here: every earlier comparison was scored by someone who knew which arm he was reading. A first attempt printed the mapping and was thrown away.
- **A post-hoc cell is recorded with no claim attached.** Six of twelve said explicitly why there is only one example, four of six with the changed line against two of six without, one-tailed p of 0.28. It was not the criterion and six a side cannot separate it from nothing. It is on the page because the last test on this skill published a claim from exactly this kind of cell and had to be corrected.
- The page also records why the earlier three in six cannot be rechecked: five of those six outputs were never published, and the skill has changed since.
- **A defect in this repository's own re-run instruction turned up while following it.** The Aldercroft transcript's fictional-disclosure blockquote names two of the scenario's traps and sits above the line the re-run warning tells you to copy up to, so anyone re-running it is handed part of the answer key. It affects every earlier test on that transcript. Being fixed separately.

### The Mistakes Guide Is Now Linked From Where People Land

- [Which AI Mistakes Actually Get Through](guides/which-ai-mistakes-get-through.md) was reachable from one line, at 129 of a 164 line README, and from nothing else. That is close to how the bench ended up with almost no readership: published once, linked once, a long way down a long page.
- **Five skills now cite it where their own recorded defect belongs.** Build a Business Case for the stacked figure, Hand Over an Opportunity for the general instruction that failed against the mechanism that worked, and Follow Up After a Sales Call, Prepare for a Sales Call and Handle an Objection for the invented detail each of them has on record. The traffic lands on the skills rather than on the evidence pages, so that is where the citation goes.
- Each sentence names that job's actual defect rather than pointing vaguely at a guide, and none of them claims the skill itself was what got tested. Three of the five defects came from the bench running the same job, and both the guide and the sentence say so.
- Also linked from the recipe card index, next to the line about not trusting a card because it reads well, from Where Should You Start? for anyone already scoring their own output, and from the top of Evidence Status.

### Where Three of the Nineteen Runs Came From

- The [stacked figure test](evaluations/business-case-stacked-figure-test.md) reported nineteen runs without saying that three of them were the previous test's unmodified runs, reused because they carried neither the guardrail nor the warning note and so belonged in the plain baseline cell. Sixteen were made for it. The page now says so in the method and again in its limits.
- **The page's own account gave it away.** The mistake it records was made "after the first nine runs" against a three-run baseline of two of three, and by its own description of those nine, no such runs existed in this test yet. They were the previous test's, where two of three unmodified runs produced the same defect. The em dash test's twenty-eight baseline runs only add up the same way: six plus sixteen plus six.
- **"Ten further runs were added" was wrong.** It was seven: five of the guardrail without the warning note, and two more of the version with neither, which is what took the plain baseline cell from three runs to five.
- **Nothing in the result changes.** The table, the counts and all three p values were always describing the nineteen runs shown. The guardrail arm is ten runs made for this test and none of them produced a combined figure.
- **"All five guardrail runs engaged with both figures" implied there were five.** There were ten. Five of them were read in full rather than only checked against the criterion, and the sentence now says that instead. The scored output called itself "the first of the five" for the same reason and no longer does.
- Three pages were left saying that the Build a Business Case skill lets em dashes through, which stopped being true when all seventeen skills got the rule. Both published business case outputs and the check requirement test now put it in the past tense, where it is accurate about the state at the time of those runs, and a new check catches the present tense version. Retro-tested against the state before this change: it fires on exactly those three lines.

### Which AI Mistakes Actually Get Through

- A new guide, [Which AI Mistakes Actually Get Through](guides/which-ai-mistakes-get-through.md), catalogues every real defect found across the scored runs in these three repositories, sorted by whether a careful reader would have noticed. Nothing on it is illustrative and every row links to the evaluation it came from.
- The argument is that the mistakes worth building a habit around are not the ones that are easy to laugh at. A compliance-narrating email, a spelling error and thirty em dashes cost nothing, because you see them. An invented pronoun repeated four times inside a Confirmed Evidence section, a price that appears nowhere in the source, and two unmeasured figures multiplied into £131,000 all read as sourced fact.
- It needed no new tests. Forty-two of the fifty evaluations here already named a specific invented or unsupported detail; nobody had ever sorted them by how easy they are to catch.
- Writing it turned up the best example in either table, from a run recorded months ago: a general instruction telling the model not to invent pronouns did not work, and a second clean rerun scored the same 41 out of 50 with the same automatic failure. What fixed it was a mechanism, a person reference ledger plus a required audit pass. That whole sequence including the failed attempt was already recorded, and this is the first page to draw the lesson out of it.
- The page carries its own weaknesses rather than only the successes: the stacked figure ran four times in six before anything stopped it, one prompt here missed a conflict its own skill caught, an instruction asking for three applied examples has never once been followed in six runs, and every score is still one person's.

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
- **The design had to change partway through, because of something I had written myself.** The note added in the previous test warns a human reader that this defect exists, and these files are pasted into a model as instructions, so it was also instructing the model. Seven further runs were added to separate the two. The warning's own effect turned out to be indistinguishable from noise and no claim is made for it.
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
