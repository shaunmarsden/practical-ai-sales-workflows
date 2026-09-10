# Which AI Mistakes Actually Get Through

Every mistake on this page was made by a real AI tool on a real run recorded in this repository, and every row links to the scored evaluation it came from. Nothing here is illustrative.

They are sorted by one thing: **whether a person reading the output carefully would have noticed.**

That turns out to matter more than how bad the mistake looks. The mistakes that are easy to laugh at cost nothing, because you catch them before you send anything. The ones that cost you are the mistakes that read like sourced fact.

## The Ones You Catch Immediately

These are real, they are all from scored runs here, and none of them has ever cost anything.

| What the model did | Where |
| --- | --- |
| Wrote an email that narrated its own compliance, "I have not assumed...", instead of reading like something a person would send | [Bench, Hartwell follow-up](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| Answered a request for "something showing the impact so I can get this approved" with an eleven-section, seventeen-item prohibited-claims list | [Bench, Elmsworth business case](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| Promised a decision-maker numbers in week five, on a plan whose own phase three sits at week seven | [Bench, Elmsworth business case](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| Produced between ten and thirty-one em dashes per run, across twenty-eight runs, against a house style that forbids them | [Em dash rule test](../evaluations/em-dash-rule-test.md) |
| Made a spelling error, and in another run leaked context from its own session | [Bench, Elmsworth business case](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |

You read these and fix them in the time it takes to notice. They are worth recording because they are the visible face of AI failure, and they are not the expensive one.

## The Ones That Get Through

Every one of these reads as sourced. That is what makes them expensive.

| What the model did | Why it survives a read | Where |
| --- | --- | --- |
| **Invented a person's gender and used it four times**, including once inside its own Confirmed Evidence section, cited as if the pronoun were part of what the email confirmed. Did the same for a second named person. | Nobody proofreads a pronoun. It carries no figure, no date and no claim, so there is nothing to check it against. | [Handover review, 41/50, automatic failure](../evaluations/hartwell-opportunity-handover-review.md) |
| **Multiplied an untimed estimate by an approximate planning rate**, annualised it to £131,000, then projected £65,000 a year of reclaimed capacity from an untested "half, maybe more". Labelled it illustrative. | Three derived figures, each carrying the labels of the guesses behind them, and a reader who skims takes the number and leaves the labels. | [Stacked figure test](../evaluations/business-case-stacked-figure-test.md) |
| **Signed an outreach email with a sender's name the case never supplied.** Two of four runs on the same case did it; two did not. | A signature is the last thing you read and the first thing you assume is yours. | [Bench, Marlow pre-call](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Invented a price, "£900", that appears nowhere in the source.** | A number in a document about money looks like it came from the pricing page. | [Bench, Osmond objection](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Stated "this should take 2-3 weeks" as fact**, with no basis anywhere in the notes. | It reads like something the customer said. | [Bench, Hartwell follow-up](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Turned a passing worry into a rating**, logging "Account Risk / Sensitivity: High" from a comment that was caution, not a score. | Once it is in a field with a label, it looks like data. | [Bench, Hartwell follow-up](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Invented a cost question, a quarter and a fortnight** the notes never record, and misstated what the customer had asked no questions about. | The invented detail is specific. Vagueness announces itself; specificity does not. | [Bench, Osmond objection](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Filed three contested items under "Confirmed"**: a go-live date two sources disagree about, one person's impression of search speed, and a plan whose own open item was outstanding. | They are under a heading that says Confirmed. That is the whole problem. | [Adoption, Netherford update](https://github.com/shaunmarsden/practical-ai-adoption/blob/main/examples/netherford-internal-update-example.md) |
| **Invented an owner for a job that had none, in all three runs.** Twice it named a real person from the notes, once it wrote "probably you", where the notes say only that the job needs a new owner. It also named a month the notes never state. | An action list with an owner against every row looks finished. A missing owner is the one thing an action list is supposed to surface. | [Adoption, Ambleforth action list](https://github.com/shaunmarsden/practical-ai-adoption/blob/main/evaluations/ambleforth-action-list-review.md) |
| **Named a fix as the answer immediately after its own notes flagged that link as unconfirmed.** | The contradiction is two paragraphs apart. | [Bench, Marlow pre-call](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Proposed the rebuttal the case explicitly warned against**, as though it were a neutral question. | It is a sensible-sounding next step. You have to know the case to know it is the wrong move. | [Bench, Osmond objection](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |

## The Pattern

The expensive mistakes share a shape. **They are confident, specific, and formatted like the things around them.**

An invented quarter looks like a sourced quarter. A pronoun looks like grammar. A number under a heading looks like a figure. None of them announces itself as a guess, which is exactly why an ordinary read does not catch them: you are checking whether the writing is good, and the writing is fine.

That is the distinction that matters, and it is not about model quality. On one case here, [nine runs across three models](../evaluations/hartwell-objection-ambiguous-test.md) invented no facts at all. On another, [four of six runs](../evaluations/business-case-check-requirement-test.md) of the same skill produced the same stacked figure. The failure follows the task, not the tool.

## Two Things This Repository Learned the Hard Way

**A general instruction telling the model not to do it does not necessarily work.** After the invented-pronoun failure, a plain sentence was added to the skill saying not to invent gender or pronouns. A second clean rerun scored exactly the same, 41 out of 50, with the same automatic failure. What eventually worked was a mechanism rather than a rule: a required step to build a reference ledger of every named person before drafting, and a required audit pass scanning for specific tokens before presenting. That whole sequence, including the failed attempt, is [recorded as it happened](../evaluations/opportunity-handover-instruction-change-history.md).

**Editing is not checking.** The one real-work failure recorded across these repositories was [a report that went out with an incorrect figure](https://github.com/shaunmarsden/practical-ai-adoption/blob/main/evidence/real-use-ai-assisted-fact-check-failure.md) after an ordinary editing pass. Improving how a sentence reads tells you nothing about whether the number in it is right. Those are two different jobs and only one of them was being done.

## Where This Page Is Weaker Than It Looks

The honest version of a page like this has to include the times the method did not help.

- **The stacked figure ran four times in six before there was anything to stop it.** It had already cost a hallucination-risk mark on a published record, on a £65,520 version of the same mistake, and it took [sixteen more runs](../evaluations/business-case-stacked-figure-test.md) to establish that a guardrail fixed it.
- **One prompt here missed a conflict its own skill caught, and it took three tests and thirty-six runs to find anything that helped.** A promised delivery date sat inside a period of stated leave and [the prompt's run never mentioned it](../evaluations/hartwell-chase-prompt-review.md). [Widening the instruction](../evaluations/chase-stale-date-test.md) was rejected. [Naming the weekday in the scenario](../evaluations/chase-weekday-rerun.md), which turned out to be necessary before the clash could be established at all, was rejected too. What moved it was [a required step rather than a principle](../evaluations/chase-dated-commitment-ledger-test.md), the same shape as the fix above, at five of six against two of six with a p of 0.12. This is the page's second entry for that lesson and the second time I reached for a rule first.
- **A claim on this page that did not survive being checked.** It said an instruction asking for three applied examples had never once been followed, and that both the business case skill and its prompt ask for three. Only the prompt does; the skill says three is a good number, and all six runs behind that count were runs of the skill. [Twelve blind runs](../evaluations/business-case-applied-examples-test.md) then found every run producing the one grounded example the scenario supports. The error was mine and it made a tidier point than the evidence did.
- **Every score here was given by one person, using a rubric this project wrote, on outputs this project produced.** Nobody outside has scored anything. [Evidence Status](../EVIDENCE-STATUS.md) marks that column "Not yet" for all seventeen jobs, and [scoring one output](../evaluations/score-this-yourself.md) takes about fifteen minutes if you want to be the first.

## What to Do With This

Nothing on this page argues that AI output is untrustworthy. It argues something narrower and more useful: **the mistakes worth building a habit around are not the ones that are fun to point at.**

If you want the shortest version of that habit, every [recipe card](../recipes/README.md) carries a "You must check" section, and they differ by job rather than repeating one list. What they have in common is the question behind the second table above: is this claim traceable to something somebody actually said, or does it just read that way. Those sections exist because of the rows in that table, not the first one.
