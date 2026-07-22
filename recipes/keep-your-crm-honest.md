# Recipe: Keep Your CRM Honest

One job, one page. Everything you need is here; nothing else in the repository is required to use this.

| | |
| --- | --- |
| **Helps with** | Auditing a CRM export for the structural problems that quietly make it unreliable: duplicates, missing fields, stale records and dates that do not fit the stage, without touching anything or judging why a specific deal has stalled |
| **You need** | A CRM export or list covering the records you want checked: company, contact, owner, stage, value, close date, last activity |
| **You'll get** | Likely and possible duplicates kept clearly separate, records missing critical fields, stale records, and dates that do not fit their stage, all flagged for a person to act on |
| **Open** | [Workflow](../workflows/08-crm-hygiene-review.md) · [Prompt](../templates/crm-hygiene-review-prompt.md) · [Worked example](../examples/fictional-crm-hygiene-review.md) |
| **The AI cannot decide** | Whether two similar-looking records are actually the same company, or whether a record that looks complete is genuinely current rather than stale |
| **You must check** | Every likely duplicate is confident, based on more than a similar-sounding name; possible duplicates are kept separate and flagged for your check, not merged; the review stops at flagging a date, not diagnosing why the deal stalled |
| **Then** | Confirm any suggested duplicate yourself before merging, and make every field correction and CRM change directly; nothing here merges, deletes or changes a record on its own |

Want the fuller method or where this stops and the pipeline evidence review starts? Open the [workflow](../workflows/08-crm-hygiene-review.md) itself.
