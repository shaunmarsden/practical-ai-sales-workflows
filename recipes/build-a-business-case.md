# 📄 Recipe: Build a Business Case

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Turning call evidence into a tailored business case for the decision maker who was not on the call, built or audited so it could not apply unchanged to a different prospect.

## You need

- The current call transcript or discovery notes
- Any existing draft to audit
- Confirmed commercial detail already agreed (pricing tier, start date, named contact)

## You'll get

A headed, prose business case, with:

- A personalised title
- Applied examples grounded in the actual call
- A commercial section
- A risk or data section
- A time commitment section
- Honest next steps

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/business-case-prompt.md -->
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
- Never multiply two unmeasured figures together and present the product. If a calculation needs two inputs and either one is an estimate, a projection or an approximate planning rate, give the inputs separately with their labels and say what would have to be measured before a combined number means anything. Labelling the product as an estimate does not fix this: one number reads as more solid than the two guesses behind it, and a reader who skims will carry the number and leave the labels behind
- Do not soften or remove the risk or data section
- Hyperlinks go on descriptive text. No bare URLs, and never refer to an attachment that was not actually sent
- No em dashes, no emojis
- Write dates with an ordinal suffix, for example 20th July
- Do not send the document, and do not treat it as approved. Prepare it for a person
- If the confirmed detail is too thin to personalise the examples, say so and ask for the minimum missing detail instead of writing a generic case
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Skill](../.agents/skills/build-business-case/SKILL.md)**  
Also: [Audit checklist](../.agents/skills/build-business-case/references/audit-checklist.md) · [Hartwell example](../examples/hartwell-business-case-output.md) · [Bramfield example](../examples/bramfield-business-case-output.md) · [Harder test: a pre-pilot projection](../examples/aldercroft-business-case-output.md)

## The AI cannot decide

- Which commercial figures the business is actually prepared to honour
- Whether the risk or data section is accurate for this prospect's real systems
- Who the actual reader is, if it is not the prospect

## You must check

- Every figure, quote, date or commitment is one that was actually established, not invented
- The applied examples are specific to this call, not generic enough to fit any prospect
- Nothing reads as a guarantee of an outcome

## Then

Confirm every commercial figure and the risk section are accurate, then send it and update the CRM yourself. Sending stays under explicit human approval.

---

Want the fuller method, the evidence classification rules, or further worked tests, including one built entirely on pre-pilot projections rather than measured results? Open the [skill](../.agents/skills/build-business-case/SKILL.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
