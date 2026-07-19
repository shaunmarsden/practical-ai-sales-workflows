# Roadmap

What is actually being worked on, in three honest buckets. Not a promise of dates, just a record of what is next and why.

## Now

- **A harder synthetic test**, not just a clean transcript: a genuinely ambiguous objection with real mixed signals, run three times per model instead of once, using the [test run template](evaluations/test-run-template.md), to check whether the diagnosis stays stable or swings between runs. A single clean pass proves a workflow can work, not that it reliably does.

## Done Recently

- **The objection-handling vertical is complete**: it now has a [workflow walkthrough](workflows/05-objection-handling.md), a [prompt template](templates/objection-handling-prompt.md), a [worked example](examples/northstar-objection-response.md), and a [scored review](evaluations/northstar-objection-review.md), alongside the existing [skill](.agents/skills/objection-response/SKILL.md), matching pre-call, post-call, handover, and lost-opportunity review.
- **An evaluation standard** for repeated and cross-model runs: see the [evaluations README](evaluations/README.md) and templates.

## Next

- **Real usability feedback**: get 3 to 5 actual salespeople to try a workflow and say honestly whether it saved time or just moved the work around, rather than relying on my own judgement of my own output. This is the highest-value item left and the one that needs real people, not more writing.

## Later

- Make CRM and pipeline reviews less painful to keep up to date.
- Find a sensible way to actually measure time saved and output quality, not just assume a workflow helps because it reads well.
- n8n or similar automation, once the underlying workflows are proven stable enough to hand to something unattended.
- Better voices for the interactive demo, if a real (non-browser) TTS API is ever worth the cost and complexity for what is currently a one-page static demo.
