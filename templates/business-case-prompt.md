# Business Case Prompt

Copy the prompt below, then add your call transcript or discovery notes, any commercial detail already confirmed, and who will actually read the document.

```text
Act as a careful business case writer for a B2B sale.

Use only the information I provide. Do not invent a figure, quote, date, commitment or requirement that my sources do not establish. A business case that would read the same for a different prospect unchanged has failed at its one job.

Work out who actually reads this document before you write a word of it. If the reader is someone other than the prospect I spoke to, a manager, a budget holder or a board, write in the third person about the prospect's situation. Only write in the direct second person if the prospect is genuinely the sole decision maker reading their own case.

Decide what to state as fact in this order:

1. Direct statements from the call or notes
2. Commercial detail already confirmed in this conversation
3. Company information already established, such as size, sector or systems in use
4. Public information about the company, which is context, not proof of an internal problem

Label every detail as you go:

- confirmed: the prospect stated it directly, or it was already given to me
- inference: a reasonable reading of their role or sector, still worth checking
- unknown: something a section needs that nothing established

An unknown gets a placeholder held open and clearly marked. Never answer an unknown with an inference dressed up as fact, and never replace a detail I have already confirmed with a generic placeholder.

Produce the document with these parts:

1. Title
Personalised to the prospect's actual role and sector, not the bare product name.

2. The case itself
Headed prose, read start to finish by somebody forming a view. A short summary table above it is fine, but the case must read as an argument, not a second reference grid.

3. Three applied examples
Each one names the specific manual task and its cost, what the proposal addresses, and what changes as a result, all drawn from my sources. A sub-heading with the expected impact and a few measurable early indicators is the stronger version where the material supports it. If an example would read the same in another prospect's document, go back to the source material.

4. Commercial section
Only figures the prospect has actually seen or agreed. Not internal pricing mechanics that mean nothing to an external reader.

5. Risk, data or compliance section
Always present, with its own heading, worded to match what the prospect actually said about their own systems and data handling. Never a boilerplate reassurance, and never something that contradicts them.

6. Time or resource commitment
Present, with a real figure.

7. Next steps
Honest about what actually happens next. Never imply that sending this document finishes the process.

8. What a person must check before this is sent
List every figure, claim and section that needs human confirmation, and anything you had to mark unknown.

Rules:

- Every claim traces to something in my sources, or it is labelled
- Do not soften or remove the risk or data section
- Hyperlinks go on descriptive text. No bare URLs, and never refer to an attachment that was not actually sent
- No em dashes, no emojis
- Write dates with an ordinal suffix, for example 20th July
- Do not send the document, and do not treat it as approved. Prepare it for a person
- If the confirmed detail is too thin to personalise the examples, say so and ask for the minimum missing detail instead of writing a generic case
```

## Before You Use the Output

- Check every commercial figure is one your business is actually prepared to honour
- Check the risk and data section against what the prospect really said about their systems, not against what sounds reassuring
- Check nothing reads as a guarantee of an outcome
- Check any projection is still described as a projection, and that the more flattering end of an estimate has not quietly become the headline
- Confirm who the reader is before sending, and send nothing until you have approved it yourself

## Honest Note on This Prompt

This is condensed from the [Build a Business Case skill](../.agents/skills/build-business-case/SKILL.md), which is the fuller version and carries the [audit checklist](../.agents/skills/build-business-case/references/audit-checklist.md) this leaves out. The skill and this prompt are separate artefacts, tested separately. The skill scored 47, 46 and 46 on three different fictional scenarios; this prompt has its own [scored test](../evaluations/aldercroft-business-case-prompt-review.md) on the hardest of the three. Do not read either score as evidence for the other.
