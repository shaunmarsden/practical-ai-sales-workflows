# Progressive Disclosure

A skill's `SKILL.md` is the file an AI assistant loads every time the skill runs. If it holds the full method, a fictional example, an output template and a review checklist all in one file, every run pays to load all of it, whether it needs the deeper material or not. Progressive disclosure means keeping the core instruction short enough to load every time. The deeper material, such as examples, templates and reference notes, goes into supporting files that open only when a step calls for them.

Most skills here are already built this way. This guide names the pattern and checks the skill library against it. It doesn't introduce anything new.

## What Belongs in the Core File

`SKILL.md` should carry only what every run needs: the purpose, what inputs to gather, the steps of the method, the guardrails, when to stop, and what still needs a person. That's the instruction. Everything else supports particular moments in it and isn't part of it.

## What Belongs in a Supporting File

- A fictional example (`references/*-example.md`), read once to check against a worked case, not reloaded at every step.
- An output contract (`references/output-contract.md`), loaded when a skill's limits need stating in full. It's separate from the shorter guardrail list already in `SKILL.md`.
- An output template (`templates/output-template.md`), loaded only when it's time to format the final answer.
- A human review checklist (`checks/checklist.md`), loaded only once there's something to review.

## Auditing the Current Skill Library

Every `SKILL.md` in this repository, as it stood on 8th October 2026:

| Skill | Lines | Supporting files |
| --- | --- | --- |
| [prepare-for-sales-call](../.agents/skills/prepare-for-sales-call/SKILL.md) | 86 | Source pack, template, output and evaluation, linked from the wider repository rather than duplicated locally |
| [review-objection-patterns](../.agents/skills/review-objection-patterns/SKILL.md) | 88 | Two fictional logs, outputs and evaluations, linked from the wider repository rather than duplicated locally |
| [identify-buyer-indecision](../.agents/skills/identify-buyer-indecision/SKILL.md) | 37 | Output contract, template, checklist, fictional example |
| [fit-and-limitations-review](../.agents/skills/fit-and-limitations-review/SKILL.md) | 52 | Fictional example |
| [champion-enablement](../.agents/skills/champion-enablement/SKILL.md) | 56 | Output contract, template, checklist, fictional example |
| [real-blocker-diagnosis](../.agents/skills/real-blocker-diagnosis/SKILL.md) | 56 | Fictional example |
| [crm-hygiene-review](../.agents/skills/crm-hygiene-review/SKILL.md) | 65 | Fictional example and evaluation, linked from the wider repository rather than duplicated locally |
| [review-lost-opportunity](../.agents/skills/review-lost-opportunity/SKILL.md) | 65 | Fictional example |
| [pipeline-evidence-review](../.agents/skills/pipeline-evidence-review/SKILL.md) | 65 | Fictional example and evaluation, linked from the wider repository rather than duplicated locally |
| [objection-response](../.agents/skills/objection-response/SKILL.md) | 69 | Fictional example |
| [workflow-router](../.agents/skills/workflow-router/SKILL.md) | 77 | None; the routing table itself is the core instruction |
| [outbound-prospecting](../.agents/skills/outbound-prospecting/SKILL.md) | 78 | Fictional example |
| [draft-follow-up-email](../.agents/skills/draft-follow-up-email/SKILL.md) | 80 | Template and checklist |
| [plan-chase-sequence](../.agents/skills/plan-chase-sequence/SKILL.md) | 87 | Reference notes on sequence stages |
| [build-business-case](../.agents/skills/build-business-case/SKILL.md) | 89 | Audit checklist, two fictional examples |
| [opportunity-handover](../.agents/skills/opportunity-handover/SKILL.md) | 88 | Output contract, template, checklist, fictional example |
| [extract-post-call-evidence](../.agents/skills/extract-post-call-evidence/SKILL.md) | 94 | Output schema, fictional example |

Every core file is under 100 lines, and the longest is extract-post-call-evidence at 94. Every skill with deeper material, such as an example, a template or a checklist, keeps it in a separate file rather than inside `SKILL.md`. Most files have grown since I first wrote this, because every skill picked up the same raw copy and front matter instruction, and later the no em dashes rule. No supporting file was folded back in, and nothing here fails the pattern. The audit's real use is as something to check the next skill against, so a longer `SKILL.md` gets caught at review rather than growing unnoticed.

## What to Watch For

- A `SKILL.md` that starts to include a full worked example, rather than linking to `references/*-example.md`.
- A guardrail list in `SKILL.md` that grows into something close to a full output contract. At that point it should become its own `references/output-contract.md`, as [identify-buyer-indecision](../.agents/skills/identify-buyer-indecision/SKILL.md) already does.
- A skill that keeps working only because the person running it has memorised the parts that used to be in the file. That's a sign the core file has drifted past what a first-time reader could follow.
