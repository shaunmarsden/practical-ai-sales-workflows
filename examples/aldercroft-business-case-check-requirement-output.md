# Aldercroft Business Case Output, Skill With the Check Requirement

> This is a worked output created from the fictional [Aldercroft pre-pilot transcript](aldercroft-business-case-transcript.md) using the [Build a Business Case skill](../.agents/skills/build-business-case/SKILL.md) after one line was added to it. Aldercroft Group, Tomasz Nowicki, Priya Deshmukh and every figure are invented. Nothing has been sent, approved or changed in a CRM.

This is the first of the three modified-skill runs in the [check requirement test](../evaluations/business-case-check-requirement-test.md), chosen for the record by a rule set before any run happened rather than picked afterwards. The skill and the transcript went into a fresh isolated context, with the transcript's answer key removed first as its own warning instructs.

**One edit was made, and it is the finding this run threw up.** The raw output contained twenty-three em dashes, which this repository's own style rule and CI check forbid, so they were converted to commas, colons and full stops. The choice of replacement in each place is mine, and in eight places a bare comma would have left a splice so a full stop was used instead. No words were added, removed or reordered. The Build a Business Case skill did not tell the model to avoid em dashes when this run was made, and all six runs in the test produced between thirteen and twenty-three of them. All seventeen skills now carry that rule. The [chase sequence prompt](../templates/chase-sequence-prompt.md), which carried it even then, produced none. See the [test](../evaluations/business-case-check-requirement-test.md) for what that means for every other published output here.

---

# A Pilot Business Case for Operations Directors Running Manual Transaction Reconciliation

*Prepared by Tomasz Nowicki, Operations Director, for Priya Deshmukh, Chief Financial Officer*

| Company | Role | Programme | Start date |
|---|---|---|---|
| Aldercroft Group | Operations Director (Tomasz Nowicki), presenting to CFO Priya Deshmukh | Paid pilot: automated matching of internal transaction records against supplier invoices | **UNKNOWN: not agreed on the call; to be confirmed once budget is approved** |

---

## Why This Is Coming to You Now

Aldercroft's reconciliation team of twelve analysts currently matches internal transaction records against supplier invoices line by line, entirely by hand. Tomasz Nowicki, who runs the team, has looked at an automated alternative and believes it is worth testing properly before asking for anything larger. No pilot has run yet. Every performance figure in this document is a projection from a product demonstration, not a measured result from Aldercroft's own data. That distinction is deliberate, and it is the reason this case asks for a pilot rather than a rollout.

## The Problem Today

Twelve analysts each spend roughly six hours a week on manual line-by-line reconciliation matching. That figure is Tomasz's own estimate, formed from watching the team work. It has never been formally timed, so it should be read as a working estimate rather than a measured baseline. The work is described as tedious and error-prone, which is the usual profile for tasks worth automating, but the six-hour figure itself still needs to be verified before it is repeated outside this document.

## Applied Example: Reconciliation Matching

**The manual task and its cost.** Twelve analysts each spend an estimated six hours a week matching transaction records to supplier invoices by hand. Using Finance's own blended loaded rate of £35 an hour for the team, an approximate planning average across the group, not each analyst's individual salary, that estimated manual effort represents roughly **£2,520 a week** in team time, built entirely on the unmeasured six-hour figure above.

**What the proposed solution addresses.** Automated matching would take over the line-by-line comparison work itself, leaving analysts to review exceptions rather than check every line manually.

**What changes as a result: projected, not measured.** Tomasz's own expectation, based on the product demonstration rather than any test against Aldercroft's own data, is that this could cut the manual matching time by around half, possibly more, once the process beds in. He was explicit on the call that this is a gut-feel projection tied to what he saw in the demo, not a commitment, and that Aldercroft has not tested it on their own data. Applying that projected range to the estimate above gives a **projected reduction of roughly £1,260 a week or more**. That is a figure built on two unverified inputs stacked together, included here only to explain why a measured pilot is worth funding, not as a number the business should expect to bank.

**Measurable early success indicators for the pilot** (what the pilot is designed to actually establish):
- Measured average hours per analyst per week spent on manual matching, compared against the six-hour estimate above
- Percentage reduction in manual matching time actually achieved, compared against the ~50%-or-more projection above
- Completeness of the audit trail, every matched item traceable to what was matched and by whom
- Analyst-reported error rate on exception handling versus the current fully manual process

## Commercial Ask

This case asks for budget approval to run a defined, paid pilot with the current reconciliation team of twelve, not a full rollout. Tomasz was explicit that the next case to Priya should be built on Aldercroft's own measured numbers, not on the projections above.

**The specific pilot investment figure was not discussed on the call and is not included here.** It needs to be agreed and inserted before this goes to Priya. See the Human Check section below.

## Risk, Data and Compliance

The data involved is transaction and invoice data: amounts, supplier names, and reference numbers. No customer personal data and no card numbers are part of this process. Priya's stated concern, as relayed by Tomasz, is audit trail. She will want a clear record of what was matched and by whom, since this process feeds directly into Aldercroft's own financial reporting. Any solution proposed here needs to preserve a full audit trail against that specific requirement, not a general assurance about security that doesn't speak to what she actually asked about.

## Time and Resource Commitment

The pilot would run against the team's current headcount of twelve analysts, with no change to that number assumed anywhere in this case. Tomasz was clear that any future headcount increase is unconfirmed, subject to a hiring committee and budget round, and should not be built into this or any figure above.

**The length of the "defined measurement period" for the pilot was not set on the call.** Beyond running against the current team, no other resourcing commitment (implementation effort, training time, IT involvement) was discussed. Both are flagged in the Human Check section below rather than filled in here.

## Next Steps

This document is what Tomasz will bring to Priya to request pilot budget. Sending it does not itself constitute approval. If Priya approves, the next steps are to agree a start date and measurement period, run the pilot against the current team of twelve, and measure the indicators above. A second business case, built on Aldercroft's own measured results rather than the projections in this one, would follow before any decision on a wider rollout.

## Human Check: Confirm Before This Goes to Priya

- [ ] **Pilot investment figure: UNKNOWN.** Not discussed on the call. Must be added before this document is usable.
- [ ] **Pilot start date: UNKNOWN.**
- [ ] **Pilot duration / measurement period length: UNKNOWN.** The call only established that it should be "defined," not how long.
- [ ] The £35/hour blended rate is Finance's approximate planning average, not each analyst's actual salary, confirm it's acceptable to cite externally on that basis.
- [ ] The six-hours-per-week manual matching estimate is Tomasz's own unmeasured observation, confirm he's comfortable it being quoted to the CFO as such.
- [ ] The "around half, possibly more" reduction is Tomasz's own projection from the demo, not a vendor guarantee, confirm the wording keeps that clearly labelled as a projection.
- [ ] The derived £2,520/week cost estimate and £1,260+/week projected reduction are both built on the two unverified figures above, confirm it's acceptable to include this calculation, or whether it should be cut and left qualitative.
- [ ] Confirm scope stays limited to the reconciliation team only. Tomasz flagged a similar manual-matching problem in accounts payable purely as a future thought and was explicit it should not be folded into this document. It isn't, and it should stay that way.
- [ ] Confirm the current headcount of twelve is what appears throughout. The possible Q2 increase to seventeen analysts is unconfirmed and must not appear anywhere in this case, per Tomasz's explicit instruction on the call.
- [ ] Confirm the audit-trail wording above actually matches what Priya needs to see for financial-reporting sign-off. This document repeats what Tomasz relayed of her concern, not her own words.
- [ ] Confirm correct spelling and titles for Tomasz Nowicki and Priya Deshmukh, and the correct formal name for Aldercroft Group, before external use.

---

*This case was built entirely from a single 22-minute pre-pilot discovery call. No pilot has run at Aldercroft Group. Every performance and cost figure above is either a stated estimate/projection from that call or a calculation built directly from those estimates, and is labelled as such throughout. Nothing above should be read as a measured result or a commitment.*
