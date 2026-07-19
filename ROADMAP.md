# Roadmap

What is actually being worked on, in three honest buckets. Not a promise of dates, just a record of what is next and why.

## Now

- Nothing currently in progress. The eight sales problems, the AI-enablement layer, the interactive demo, and the evaluation standard in this folder are the current [v1.0.0 release](https://github.com/shaunmarsden/practical-ai-sales-workflows/releases/tag/v1.0.0).

## Next

- **A harder synthetic test**, not just a clean transcript: conflicting notes, a change of contact, or an ambiguous objection, run three times per model instead of once, using the [test run template](evaluations/test-run-template.md). A single clean pass proves a workflow can work, not that it reliably does.
- **Complete the objection-handling vertical**: it currently has a skill ([.agents/skills/objection-response](.agents/skills/objection-response/SKILL.md)) but no dedicated `workflows/*.md` walkthrough or scored worked example, unlike pre-call, post-call, handover, and lost-opportunity review.
- **Real usability feedback**: get 3 to 5 actual salespeople to try a workflow and say honestly whether it saved time or just moved the work around, rather than relying on my own judgement of my own output.

## Later

- Make CRM and pipeline reviews less painful to keep up to date.
- Find a sensible way to actually measure time saved and output quality, not just assume a workflow helps because it reads well.
- n8n or similar automation, once the underlying workflows are proven stable enough to hand to something unattended.
- Better voices for the interactive demo, if a real (non-browser) TTS API is ever worth the cost and complexity for what is currently a one-page static demo.
