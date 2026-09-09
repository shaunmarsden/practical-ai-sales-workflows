# Aldercroft Business Case Output, Skill With the Stacked-Figure Guardrail

> This is a worked output created from the fictional [Aldercroft pre-pilot transcript](aldercroft-business-case-transcript.md) using the [Build a Business Case skill](../.agents/skills/build-business-case/SKILL.md) with the guardrail against combining two unmeasured figures. Aldercroft Group, Tomasz Nowicki, Priya Deshmukh and every figure are invented. Nothing has been sent, approved or changed in a CRM.

This is the first of the guardrail runs in the [stacked figure test](../evaluations/business-case-stacked-figure-test.md), chosen by the same rule used last time, the first run rather than the best. The skill and the transcript went into a fresh isolated context with the transcript's answer key removed first, as its own warning instructs.

**One edit was made.** The raw output contained thirty em dashes, which this repository's style rule and CI check forbid, so they were converted to colons, commas and full stops. The choice in each place is mine and four would have left a splice, so those became full stops. No words were added, removed or reordered. That the model produces them at all is [a finding from the previous test](../evaluations/business-case-check-requirement-test.md), and the skill did not tell it not to when this run was made. All seventeen skills now carry that rule, [tested over thirty-three runs](../evaluations/em-dash-rule-test.md).

---

# DRAFT: Business Case (pre-pilot, unmeasured projections), requires human review before sending

**Note on inputs:** This draft is built entirely from a 22-minute discovery call transcript (Aldercroft Group, Shaun and Tomasz Nowicki). No pilot has run. No product or programme name, pricing, start date, or pilot time/resource commitment was established on the call. Those gaps are marked `unknown` below rather than filled with a plausible guess, per the source material. There is nothing to draw them from.

---

## Summary

| | |
|---|---|
| Company | Aldercroft Group |
| Prospect / role | Tomasz Nowicki, Operations Director (reconciliation team) |
| Reader of this document | Priya Deshmukh, CFO: was not on the discovery call |
| Product / programme | `unknown`: not named on the call |
| Ask | Budget approval for a paid pilot, reconciliation team only, with a defined measurement period |
| Start date | `unknown`: not discussed |

---

## Business Case: Reconciliation Pilot for Operations Directors Running Manual Transaction Matching

*For Priya Deshmukh, CFO, Aldercroft Group*

Tomasz Nowicki, Operations Director, is asking for budget to run a paid pilot testing whether an automated matching solution can reduce the manual effort his team currently puts into transaction reconciliation. This document sets out what his team does today, what the pilot would test, and what it does not yet know, so that the pilot, not this document, is what produces the numbers a fuller business case would eventually rely on.

### The problem as Tomasz describes it

Aldercroft's twelve analysts each manually reconcile the company's internal transaction records against supplier invoices, matching line by line. Tomasz describes it as tedious and error-prone work. By his own estimate, made from watching the team, not from a formal time study, each analyst spends roughly six hours a week on it. He was explicit that this has never been timed formally, so it should be read as a working estimate rather than a measured baseline.

### What the pilot would test

Tomasz's early view, formed from a product demonstration rather than from any test against Aldercroft's own data, is that the proposed solution could cut that reconciliation time by roughly half, possibly more, once bedded in. He was equally explicit that this is a gut feel, not a number he is prepared to stand behind yet. That is the specific gap a paid pilot with a defined measurement period is meant to close: replacing an estimate and a demo impression with a result measured on Aldercroft's own transaction and invoice data.

### Cost inputs: kept separate, not combined into a headline saving

Three figures are in play here, and each is either an estimate or an approximation rather than a measured fact:

- **Time affected:** roughly 6 hours per analyst per week (Tomasz's estimate, unmeasured)
- **Projected reduction:** roughly 50% or more (Tomasz's gut feel from a demo, not tested on Aldercroft's data)
- **Cost per hour:** approximately £35, Aldercroft Finance's blended loaded rate for the team, Finance's own description is that this is a planning average across the group, not an exact figure per person

These are given separately, with their sources, deliberately. Multiplying them together would produce a single "annual saving" figure that reads as far more solid than the three unverified inputs behind it, none of which has been measured yet. That combined number is exactly what the pilot exists to produce responsibly, and is not something this document should anticipate.

**Scope note:** the case is built around the current headcount of twelve analysts only. Tomasz mentioned a possible addition of five more analysts by Q2, but was explicit that this is unconfirmed, still subject to a hiring committee decision, and could be cut depending on the budget round. He asked directly that the case not be built around seventeen. It has not been.

### What the pilot would need to establish (measurable, early indicators)

- A formally timed baseline of current per-analyst reconciliation time, replacing the six-hour estimate
- A measured reduction in time-on-task after the pilot period, on Aldercroft's own transaction and invoice data, not the demo
- Confirmation from Finance of which rate to apply once real figures exist, given the £35 figure is a planning average
- Evidence that the audit trail requirement below is actually met in practice, not just in design

### Risk, data and audit trail

The data involved is transaction and invoice data, amounts, supplier names, and reference numbers. Tomasz was clear there is no customer personal data and no card numbers involved. Separately, he flagged that Priya will specifically want to know whether the process preserves a clear, reviewable audit trail of what was matched and by whom, since this work feeds Aldercroft's own financial reporting. That requirement is noted here as something the pilot must demonstrate, not something already shown. No audit trail capability has been verified yet, only described as a requirement to design for and confirm during the pilot.

### Scope

This case covers the reconciliation team only. Tomasz separately mentioned that Aldercroft's accounts payable team has a similar manual matching problem, but was explicit that this is a distinct, future conversation and asked that it not be folded into this document. It has not been.

### Commercial

`unknown`, no pricing has been discussed or agreed with Aldercroft on this call. This section needs input before the document is finalized; it should not be left blank without a placeholder, and it should not be filled with an assumed figure.

### Time or resource commitment

`unknown`, the call did not establish what running the pilot would require from Aldercroft's side (analyst time, IT involvement, data access setup, or duration). This needs to be confirmed before the document goes to Priya.

### Next steps

The ask to Priya is for budget approval to run a paid pilot, scoped to the reconciliation team only, with a defined measurement period. The explicit purpose of that pilot is to produce Aldercroft's own numbers, a real baseline and a real reduction, so that any future case for a wider rollout is built on measured results rather than the projections in this document. Approving budget for the pilot is the next step; it is not itself a decision to proceed to a full rollout, and sending this document does not complete or replace that decision. It is the basis for a conversation Priya and Tomasz still need to have.

### Links

None. No attachment, deck, or supporting document was referenced or sent as part of this call, so none is linked here.

---

## Human check: confirm before this goes to Priya

- [ ] The six-hours-per-analyst-per-week figure is Tomasz's own unmeasured estimate, confirm it should appear in the case at all, and that it is clearly labelled as an estimate, not fact
- [ ] The "roughly half, possibly more" reduction figure is Tomasz's gut feel from a demo, untested on Aldercroft's own data, confirm it is not being read as a promised outcome
- [ ] The £35/hour blended rate is Finance's planning average, not an exact per-analyst cost, confirm Finance is comfortable with it appearing at all, even labelled as approximate
- [ ] Confirm no combined "annual saving" figure has been introduced anywhere downstream of this draft (e.g., if this is copied into a slide or email)
- [ ] Confirm the case is built around 12 analysts only, the possible five additional Q2 hires must not appear as a basis for any figure, since Tomasz was explicit they are unconfirmed and could be cut
- [ ] Product/programme name: `unknown`, needs to be supplied
- [ ] Start date: `unknown`, needs to be supplied
- [ ] Commercial/pricing figure: `unknown`, no pricing was discussed with Aldercroft; needs to be supplied or the section needs sign-off to remain open
- [ ] Pilot time/resource commitment from Aldercroft's side: `unknown`, needs to be supplied
- [ ] Audit trail requirement, currently described only as a requirement to meet, not a demonstrated capability; confirm this is accurate before it goes to a CFO who will specifically ask about it
- [ ] Confirm accounts payable has not been folded into this document anywhere (Tomasz explicitly asked for it to stay out)
- [ ] Confirm the ask stated to Priya is pilot budget only, not a full rollout ask

**This draft has not been checked by a person and must not be sent to Aldercroft, or to Priya specifically, until every item above is confirmed.**
