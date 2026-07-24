# Selective Installation

Eleven skills, sixteen workflows, and growing. Loading the entire `.agents/skills/` folder into one assistant, project, or Custom GPT works, but it means every conversation carries instructions for jobs that conversation was never going to need, which can crowd out the instruction that actually matters for the task at hand. This guide is about loading less, deliberately, rather than everything by default.

This is a mechanical, per-platform question, not a "which skills should I use" one. For that decision, use [Choose Your Route by Role](role-based-routes.md) if you want a subset grouped by job title. Once a specific set of skills is chosen, this guide covers how to actually load only those into a given tool.

## Why This Matters More As the Library Grows

A single skill's core `SKILL.md`, kept short and pushing deeper material into supporting files, is not the problem on its own. The problem is loading all eleven at once into a context a single conversation will only ever use one or two of. Two concrete costs:

- **Relevance dilution.** An assistant asked to draft a follow-up email, with all eleven skills loaded, has ten irrelevant instruction sets competing for attention against the one that actually applies.
- **A skill meant to stop a task can get missed.** A guardrail buried in skill six of eleven is easier to miss than one in the only skill loaded for this specific job.

## How to Load a Subset, by Platform

<details>
<summary><strong>Claude</strong></summary>

Attach only the specific skill folders you actually need to a Project's knowledge, rather than the whole `.agents/skills/` directory. A skill's `references/`, `templates/` and `checks/` subfolders belong with it; attach the whole skill folder, not just its `SKILL.md`, or the skill will be missing the material it explicitly tells the assistant to load.

</details>

<details>
<summary><strong>ChatGPT</strong></summary>

Upload only the relevant skill's Markdown files to a Custom GPT's knowledge, in the same complete-folder way as above. A Custom GPT built around one specific job, for example chase-sequence planning, only needs that skill's own files, not the rest of the library.

</details>

<details>
<summary><strong>Gemini</strong></summary>

Build a Gem around one task and attach only that task's skill files. A Gem is already a natural fit for "one Gem per job" rather than one Gem carrying the entire library.

</details>

<details>
<summary><strong>Copilot</strong></summary>

If your organisation allows building a custom agent, scope its knowledge the same way: the specific skill's files, not the full folder. If a custom agent is not available to you, a saved prompt built from one skill's own instructions works as a lighter equivalent.

</details>

## When Loading Everything Is Still Fine

None of this is a rule against ever loading the full library. Exploring the repository, or deciding which skills actually fit your role before narrowing down, are both good reasons to have everything available for a session. The [workflow router](workflow-router.md) is itself a single, small skill file that only needs its own routing table loaded, not the rest of the library, so using it does not conflict with loading a narrow subset everywhere else. The guidance above is for the steady-state case: a Project, Custom GPT, or Gem used every day for one or two specific jobs, where the rest of the library is dead weight in every single conversation.
