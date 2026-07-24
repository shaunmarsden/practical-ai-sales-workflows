# Future Interfaces

Four ideas from the backlog's Learning Tools and Future Interfaces section, written up as fuller design specs rather than left as short stubs. None of these exist as software. This repository is Markdown, prompts and instructions, read in a chat; building any of the four below is a genuinely separate software project, not a file added here. Writing the spec now, before any of it is built, means a future build has something to check its decisions against, the same reasoning behind writing down the workflow-composition principles elsewhere in this backlog.

Built ahead of the usual real-use-evidence bar, on the project owner's own call. Each spec below stays a spec: what it would do, what it must never do, and what it depends on already existing here. None of it is scoped for who builds it or when.

## Fictional Sales Role-Play Simulator

A fuller version of the [pre-call objection roleplay drill](../templates/pre-call-objection-roleplay-prompt.md), as a proper practice environment rather than a single prompt.

**What it would do:** the AI plays a fictional prospect, built from fixed source material so the same scenario is repeatable; the salesperson responds in character; the system records which pieces of evidence the salesperson actually uncovered during the exchange, not just whether the conversation felt like it went well; an unsupported claim or an invented commitment made by the salesperson mid-roleplay gets flagged, not rewarded; coaching follows the exercise, tied to specific moments in the transcript.

**What it must never do:** score or reward closing at any cost. A roleplay that rates "got to yes fastest" above "asked the harder question" would train exactly the wrong instinct. It must also never let the fictional prospect concede a point it was not scripted to concede, since that would teach a salesperson that pressure works rather than that evidence works.

**What it depends on:** the same fictional-content discipline as everything else here, a scripted prospect built from fixed source material, not an improvising character with no ground truth to score against; and the [sales AI output rubric](../evaluations/sales-ai-output-rubric.md) or something built specifically for scoring a conversation rather than a document.

## Interactive Evidence Workspace

A local interface showing the state of a longer, multi-step workflow run, rather than a single chat transcript a person has to scroll back through.

**What it would show:** sources loaded; evidence and its source links; facts, inferences, unknowns and conflicts, kept visually distinct; workflow progress; the actual instruction used for this run, not a hidden default; draft outputs; what still needs approval; run and correction history.

**What it must never do:** let anything progress past an approval point without the person present. The whole point of surfacing "approval still required" as its own visible state is to make skipping it a visible, deliberate choice, not something that happens by default because no one was watching.

**What it depends on:** the same working-folder and run-log principles as the rest of this backlog's workflow-composition ideas, since this interface is really those principles given a visual surface rather than a plain-text log; and [Skill Handoff Contracts](skill-handoff-contracts.md), since a multi-step run's evidence state needs to survive a handoff between skills without quietly losing its confirmed/inferred/unknown labels.

## Explainable Lead-Qualification View

A visual read on a prospect's fit, built to be inspected rather than trusted on sight.

**What it would show:** confirmed fit, possible fit, disqualifying evidence, missing information, and public signals, each in its own visible category, plus what those signals do not prove, shown alongside them rather than left implicit.

**What it must never do:** collapse into a single opaque number. A 0 to 100 fit score with no visible components is exactly the failure mode this exists to avoid: it looks precise and explains nothing. If a score is shown at all, every component, its weight, and its limitation must be visible and configurable, not fixed inside a model nobody can inspect.

**What it depends on:** [Fit and Limitations Review](../workflows/13-fit-and-limitations-review.md)'s existing three-way classification (good fit, poor fit, genuinely uncertain) as the categories this view would visualise, not a new classification invented for the interface; and the same discipline used elsewhere in outbound prospecting for stating what a public signal does and does not prove, rather than treating it as settled evidence.

## Before-and-After Instruction Testing Interface

A way to compare two versions of the same instruction against the same fictional case, side by side, rather than trusting memory of how the old version used to behave.

**What it would show:** both instruction versions, both raw outputs, a diff of what actually changed in the output, not just the instruction, scores for each under the [sales AI output rubric](../evaluations/sales-ai-output-rubric.md), and a place for human review notes on what the difference actually means.

**What it must never do:** present a model's own before-and-after scoring as independent proof that the new version is better. A score generated by the same kind of model being evaluated is a starting point for a person's judgement, not a substitute for it; this interface should support that evaluation, never stand in for it.

**What it depends on:** the [instruction-change and regression history template](../templates/instruction-change-history-template.md), whose manual version this interface would make faster to use, not a new discipline this invents.

## What Ties These Together

All four assume the workflows and skills they visualise or test already exist and already work by hand. None of them is a reason to skip the manual version first; each is explicitly a faster or clearer surface for a discipline already proven here in plain Markdown and a chat window.
