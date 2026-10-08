# Which AI Mistakes Actually Get Through

A real AI tool made every mistake on this page, on a real run recorded in this repository or one of its sibling repositories. Every row links to the scored evaluation it came from. None of it is made up to illustrate a point.

I've sorted them by one thing: **whether a person reading the output carefully would have noticed.**

That matters more than how bad the mistake looks. The mistakes that are easy to laugh at cost nothing, because you catch them before you send anything. The ones that cost you read like sourced fact.

## The Ones You Catch Immediately

These are real, they all come from scored runs here, and none of them has ever cost anything.

| What the model did | Where |
| --- | --- |
| Wrote an email that described its own rule-following, "I have not assumed...", instead of reading like something a person would send | [Bench, Hartwell follow-up](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| Answered a request for "something showing the impact so I can get this approved" with an 11-section, 17-item list of claims not to make | [Bench, Elmsworth business case](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| Promised a decision-maker numbers in week five, on a plan whose own phase three sits at week seven | [Bench, Elmsworth business case](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| Produced between 10 and 31 em dashes per run, across 28 runs, against a house style that bans them | [Em dash rule test](../evaluations/em-dash-rule-test.md) |
| Made a spelling mistake, and in another run leaked context from its own session | [Bench, Elmsworth business case](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |

You spot these and fix them in seconds. They're worth recording because they're the kind of AI failure people see, and they're not the expensive kind.

## The Ones That Get Through

Every one of these reads as if it came from a source. That's what makes them expensive.

| What the model did | Why it survives a read | Where |
| --- | --- | --- |
| **Invented a person's gender and used it four times**, once inside its own Confirmed Evidence section, cited as if the pronoun were part of what the email confirmed. It did the same for a second named person. | Nobody proofreads a pronoun. It carries no figure, no date and no claim, so there's nothing to check it against. | [Handover review, 41/50, automatic failure](../evaluations/hartwell-opportunity-handover-review.md) |
| **Multiplied an untimed estimate by a rough planning rate**, turned it into a yearly £131,000, then projected £65,000 a year of time won back from an untested "half, maybe more". Labelled it illustrative. | Three figures, each built on guesses and carrying their labels, and a reader who skims takes the number and leaves the labels. | [Stacked figure test](../evaluations/business-case-stacked-figure-test.md) |
| **Signed an outreach email with a sender's name the case never gave.** Two of the four Claude runs on the same case did it; two didn't. | A signature is the last thing you read and the first thing you assume is yours. | [Bench, Marlow pre-call](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Invented a price, "£900", that appears nowhere in the source.** | A number in a document about money looks like it came from the pricing page. | [Bench, Osmond objection](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Stated "this should take 2-3 weeks" as fact**, with nothing in the notes to back it. | It reads like something the customer said. | [Bench, Hartwell follow-up](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Turned a passing worry into a rating**, logging "Account Risk / Sensitivity: High" from a comment that was caution, not a score. | Once it's in a labelled field, it looks like data. | [Bench, Hartwell follow-up](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Invented a cost question, a quarter and a fortnight** the notes never record, and got wrong what the customer had asked no questions about. | The invented detail is specific. Vagueness gives itself away; specific detail doesn't. | [Bench, Osmond objection](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Filed three disputed items under "Confirmed"**: a go-live date two sources disagree about, one person's impression of search speed, and a plan whose own open item was still open. | They sit under a heading that says Confirmed. That's the whole problem. | [Adoption, Netherford update](https://github.com/shaunmarsden/practical-ai-adoption/blob/main/examples/netherford-internal-update-example.md) |
| **Invented an owner for a job that had none, in all three runs.** Twice it named a real person from the notes, and once it wrote "probably you", where the notes say only that the job needs a new owner. It also named a month the notes never give. | An action list with an owner on every row looks finished. A missing owner is the one thing an action list is meant to show. | [Adoption, Ambleforth action list](https://github.com/shaunmarsden/practical-ai-adoption/blob/main/evaluations/ambleforth-action-list-review.md) |
| **Named a fix as the answer straight after its own notes flagged that link as unconfirmed.** | The contradiction is two paragraphs apart. | [Bench, Marlow pre-call](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |
| **Proposed the rebuttal the case warned against**, as if it were a neutral question. | It sounds like a sensible next step. You have to know the case to know it's the wrong move. | [Bench, Osmond objection](https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md) |

## The Pattern

The expensive mistakes have the same shape. **They're confident, specific, and formatted like the things around them.**

An invented quarter looks like a sourced quarter. A pronoun looks like grammar. A number under a heading looks like a figure. None of them looks like a guess, which is why an ordinary read doesn't catch them. You're checking whether the writing is good, and the writing is fine.

That's the difference that matters, and it isn't about how good the model is. On one case here, [nine runs across three models](../evaluations/hartwell-objection-ambiguous-test.md) invented no facts at all. On another, [four of six runs](../evaluations/business-case-check-requirement-test.md) of the same skill produced the same stacked figure. The failure follows the task, not the tool.

## Two Things I Learned by Getting Them Wrong

**Telling the model not to do it doesn't always work.** After the invented pronoun, I added a plain sentence to the skill saying not to invent gender or pronouns. A second clean rerun scored exactly the same, 41 out of 50, with the same automatic failure. What worked in the end was a step, not a rule. The skill now has to list every named person before drafting, then scan for certain words before showing its answer. The whole sequence, including the attempt that failed, is [recorded as it happened](../evaluations/opportunity-handover-instruction-change-history.md).

**Editing isn't checking.** One real-work failure recorded across these repositories was [a report that went out with a wrong figure](https://github.com/shaunmarsden/practical-ai-adoption/blob/main/evidence/real-use-ai-assisted-fact-check-failure.md) after an ordinary editing pass. Making a sentence read better tells you nothing about whether the number in it is right. Those are two different jobs, and only one of them was being done.

## Where This Page Falls Short

These are the times the method didn't help, or where the evidence is thinner than it looks.

The stacked figure turned up in four runs out of six before anything stopped it. It had already cost a mark for invented content on a published record, on a £65,520 version of the same mistake. It then took [16 more runs](../evaluations/business-case-stacked-figure-test.md) to show that a guardrail fixed it.

One prompt here missed a conflict its own skill caught, and it took three tests and 36 runs to find anything that helped. A promised delivery date fell inside a stated period of leave, and [the prompt's run never mentioned it](../evaluations/hartwell-chase-prompt-review.md). I rejected [widening the instruction](../evaluations/chase-stale-date-test.md). I also rejected [naming the weekday in the scenario](../evaluations/chase-weekday-rerun.md), though it turned out I had to do that before anyone could show the clash at all. What moved it was [a required step rather than a principle](../evaluations/chase-dated-commitment-ledger-test.md), the same shape as the fix above. It scored five of six against two of six on the prompt, and [six of six against zero of six on the skill](../evaluations/chase-skill-ledger-test.md). That's the second time this page records the lesson, and the second time I reached for a rule first.

One claim on this page didn't survive checking. It said nobody had ever followed an instruction asking for three applied examples, and that both the business case skill and its prompt ask for three. Only the prompt does. The skill says three is a good number, and all six runs behind that count were runs of the skill. [12 runs, scored without knowing which was which](../evaluations/business-case-applied-examples-test.md), then found every run producing the one grounded example the scenario supports. The mistake was mine, and it made a tidier point than the evidence did.

I gave every score here myself, using a rubric I wrote, on outputs I produced. Nobody outside has scored anything. [Evidence Status](../EVIDENCE-STATUS.md) marks that column "Not yet" for all seventeen jobs. [Scoring one output](../evaluations/score-this-yourself.md) takes about 15 minutes if you want to be the first.

## What to Do With This

Nothing on this page says AI output can't be trusted. It says something narrower and more useful: **the mistakes worth building a habit around aren't the ones that are fun to point at.**

For the shortest version of that habit, every [recipe card](../recipes/README.md) has a "You must check" section, and each one fits its job rather than repeating one list. What they share is the question behind the second table above: can you trace this claim to something somebody said, or does it just read that way? Those sections exist because of the rows in that table, not the first one.
