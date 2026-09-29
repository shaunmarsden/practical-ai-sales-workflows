# Future Interfaces

These are four ideas from the Learning Tools and Future Interfaces part of the backlog, written up as fuller designs rather than left as short notes. None of them exists as software. This repository is Markdown, prompts and instructions, read in a chat. Building any of the four would be a separate software project, not a file added here.

I've written the designs now, before anything is built, so a future build has something to check its decisions against. It's the same reason I wrote down the rules for composing longer workflows. I did this before any real use called for it, which is earlier than I'd usually publish. Each design says what it would do, what it must never do, and what it needs to exist here first. None says who would build it or when.

## Fictional Sales Role-Play Simulator

A fuller version of the [pre-call objection roleplay drill](../templates/pre-call-objection-roleplay-prompt.md): a proper place to practise, not a single prompt.

The AI would play a fictional prospect, built from fixed source material so the same scenario can be run again. The salesperson replies in character. The system records which pieces of evidence the salesperson uncovered, not just whether the conversation felt good. If the salesperson makes an unsupported claim or invents a commitment mid-roleplay, it gets flagged, not rewarded. Coaching follows, tied to specific moments in the transcript.

It must never score or reward closing at any cost. A roleplay that rates "got to yes fastest" above "asked the harder question" would train the wrong instinct. The fictional prospect must also never give up a point it wasn't scripted to give up. That would teach a salesperson that pressure works, not evidence.

It needs the same rules for fictional content as everything else here: a scripted prospect built from fixed source material, not an improvising character with nothing true to score against. It also needs the [sales AI output rubric](../evaluations/sales-ai-output-rubric.md), or something built to score a conversation rather than a document.

## Interactive Evidence Workspace

A local screen showing the state of a longer workflow run, so a person doesn't have to scroll back through a chat.

It would show the sources loaded; the evidence and links to its sources; facts, inferences, unknowns and conflicts, each kept visibly apart; how far the workflow has got; the instruction used for this run, not a hidden default; draft outputs; what still needs approval; and the history of the run and its corrections.

It must never let anything move past an approval point without the person there. Showing "approval still required" as its own visible state makes skipping it a visible, deliberate choice. It shouldn't happen by default because nobody was watching.

It needs the working-folder and run-log rules from the backlog's ideas on composing workflows, because this screen is those rules made visual instead of a plain-text log. It also needs [Skill Handoff Contracts](skill-handoff-contracts.md), because the evidence in a long run has to pass between skills without quietly losing its confirmed/inferred/unknown labels.

## Explainable Lead-Qualification View

A visual read on a prospect's fit, built to be checked, not trusted on sight.

It would show confirmed fit, possible fit, disqualifying evidence, missing information and public signals, each in its own category. Next to them, it would show what those signals don't prove, rather than leaving that unsaid.

It must never shrink to a single number nobody can see into. A fit score from 0 to 100 with no visible parts is the very failure this exists to avoid: it looks precise and explains nothing. If it shows a score at all, every part, its weight and its limits must be visible and adjustable, not fixed inside a model nobody can inspect.

It needs the three-way sort that [Fit and Limitations Review](../workflows/13-fit-and-limitations-review.md) already uses (good fit, poor fit, genuinely uncertain) as its categories, not a new one made up for the screen. It also needs the rule used in outbound prospecting here: say what a public signal does and doesn't prove, rather than treating it as settled evidence.

## Before-and-After Instruction Testing Interface

A way to compare two versions of an instruction on the same fictional case, side by side, instead of trusting your memory of how the old version behaved.

It would show both versions of the instruction, both raw outputs, and what changed in the output, not just in the instruction. It would score each against the [sales AI output rubric](../evaluations/sales-ai-output-rubric.md), with space for a person's notes on what the difference means.

It must never present a model's own before-and-after scores as independent proof that the new version is better. A score from the same kind of model being tested is a starting point for a person's judgement, not a replacement for it. This screen should support that judgement, never stand in for it.

It needs the [instruction-change and regression history template](../templates/instruction-change-history-template.md). The screen would make the manual version quicker to use; it wouldn't invent a new process.

## What Ties These Together

All four assume the workflows and skills they show or test already exist and already work by hand. None is a reason to skip the manual version. Each is a quicker or clearer way to do something already shown to work here in plain Markdown and a chat window.
