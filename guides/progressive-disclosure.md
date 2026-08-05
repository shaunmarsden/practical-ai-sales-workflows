# Progressive Disclosure

A skill's `SKILL.md` is the file an AI assistant loads every time the skill runs. If it tries to hold the full method, a fictional example, an output template and a review checklist all in one file, every run pays the cost of loading all of it, whether that run needs the deeper material or not. Progressive disclosure means keeping the core instruction short enough to load on every use, and pushing the deeper material, examples, templates, reference notes, into supporting files that are only opened when a specific step actually calls for them.

This is already how most skills in this repository are built. This guide names the pattern explicitly and checks the existing skill library against it, rather than introducing something new.

## What Belongs in the Core File

`SKILL.md` should carry only what is needed on every single run: the purpose, what inputs to gather, the method's actual steps, the guardrails, when to stop, and what still needs a person. That is the instruction itself. Everything else is support material for specific moments in that instruction, not part of it.

## What Belongs in a Supporting File

- **A fictional example** (`references/*-example.md`), read once to calibrate against a worked case, not reloaded on every step of every run.
- **An output contract** (`references/output-contract.md`), loaded when a skill's boundaries need stating in full, separate from the shorter guardrail list already in `SKILL.md`.
- **An output template** (`templates/output-template.md`), loaded only at the point of formatting the final answer.
- **A human review checklist** (`checks/checklist.md`), loaded only once there is something to review.

## Auditing the Current Skill Library

Every `SKILL.md` in this repository, checked at the time of writing:

| Skill | Lines | Supporting files |
| --- | --- | --- |
| [prepare-for-sales-call](../.agents/skills/prepare-for-sales-call/SKILL.md) | 84 | Source pack, template, output and evaluation, linked from the wider repository rather than duplicated locally |
| [review-objection-patterns](../.agents/skills/review-objection-patterns/SKILL.md) | 88 | Two fictional logs, outputs and evaluations, linked from the wider repository rather than duplicated locally |
| [identify-buyer-indecision](../.agents/skills/identify-buyer-indecision/SKILL.md) | 36 | Output contract, template, checklist, fictional example |
| [fit-and-limitations-review](../.agents/skills/fit-and-limitations-review/SKILL.md) | 51 | Fictional example |
| [champion-enablement](../.agents/skills/champion-enablement/SKILL.md) | 55 | Output contract, template, checklist, fictional example |
| [crm-hygiene-review](../.agents/skills/crm-hygiene-review/SKILL.md) | 57 | Fictional example and evaluation, linked from the wider repository rather than duplicated locally |
| [review-lost-opportunity](../.agents/skills/review-lost-opportunity/SKILL.md) | 64 | Fictional example |
| [pipeline-evidence-review](../.agents/skills/pipeline-evidence-review/SKILL.md) | 64 | Fictional example and evaluation, linked from the wider repository rather than duplicated locally |
| [objection-response](../.agents/skills/objection-response/SKILL.md) | 66 | Fictional example |
| [workflow-router](../.agents/skills/workflow-router/SKILL.md) | 73 | None; the routing table itself is the core instruction |
| [outbound-prospecting](../.agents/skills/outbound-prospecting/SKILL.md) | 77 | Fictional example |
| [draft-follow-up-email](../.agents/skills/draft-follow-up-email/SKILL.md) | 76 | Template and checklist |
| [plan-chase-sequence](../.agents/skills/plan-chase-sequence/SKILL.md) | 76 | Reference notes on sequence stages |
| [build-business-case](../.agents/skills/build-business-case/SKILL.md) | 81 | Audit checklist, two fictional examples |
| [extract-post-call-evidence](../.agents/skills/extract-post-call-evidence/SKILL.md) | 91 | Output schema, fictional example |

Every core file sits close to or just past ninety lines, and every skill with deeper material, an example, a template, a checklist, keeps it in a separate file rather than folded into `SKILL.md` itself. The one file now just over ninety lines (extract-post-call-evidence, at 91) grew there because every skill in this repository picked up the same two-line raw-copy and front-matter instruction, not because a supporting file got folded back in; nothing here fails the pattern. The audit's actual value is in having a place to check the next skill against, so a longer, more elaborate `SKILL.md` gets caught at review time rather than growing unnoticed.

## What to Watch For

- A `SKILL.md` that starts including a full worked example inline, rather than linking to `references/*-example.md`.
- A guardrail list in `SKILL.md` that grows into something closer to a full output contract, at which point it should become its own `references/output-contract.md`, as [identify-buyer-indecision](../.agents/skills/identify-buyer-indecision/SKILL.md) already does.
- A skill that keeps working, but only because whoever is running it has memorised the parts that used to be inline, which is a sign the core file has drifted past what a first-time reader could actually follow.
