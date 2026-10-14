# Selective Installation

Seventeen skills, fifteen workflows, and more coming. Loading the whole `.agents/skills/` folder into one assistant, project or Custom GPT works. But then every conversation carries instructions for jobs it was never going to need, and they can crowd out the one that matters for the task. This guide is about choosing to load less, rather than loading everything by default.

This is a practical question about each platform, not a "which skills should I use" one. For that choice, use [Choose Your Route by Role](role-based-routes.md) if you want a set grouped by job title. Once you've chosen your skills, this guide covers how to load only those into your tool.

## Why This Matters More As the Library Grows

One skill's core `SKILL.md`, kept short with the deeper material in supporting files, isn't the problem. The problem is loading all seventeen at once when a conversation will only ever use one or two. That costs you in two ways:

- The right instructions get drowned out. Ask an assistant with all seventeen skills loaded to draft a follow-up email, and 16 irrelevant sets of instructions compete for its attention with the one that applies.
- A skill meant to stop a task can get missed. A guardrail buried in skill six of seventeen is easier to miss than one in the only skill loaded for this job.

## How to Load a Subset, by Platform

<details>
<summary><strong>Claude</strong></summary>

Attach only the skill folders you need to a Project's knowledge, not the whole `.agents/skills/` directory. A skill's `references/`, `templates/` and `checks/` subfolders belong with it. Attach the whole skill folder, not just its `SKILL.md`, or the skill will be missing the material it tells the assistant to load.

</details>

<details>
<summary><strong>ChatGPT</strong></summary>

Upload only the skill's Markdown files to a Custom GPT's knowledge, taking the whole folder as above. A Custom GPT built around one job, such as planning a chase sequence, only needs that skill's files, not the rest of the library.

</details>

<details>
<summary><strong>Gemini</strong></summary>

Build a Gem around one task and attach only that task's skill files. Gems already suit "one Gem per job" better than one Gem carrying the whole library.

</details>

<details>
<summary><strong>Copilot</strong></summary>

If your organisation lets you build a custom agent, limit its knowledge the same way: one skill's files, not the full folder. If you can't build a custom agent, a saved prompt made from one skill's instructions is a lighter way to do the same thing.

</details>

<details>
<summary><strong>Claude Code and other terminal agents</strong></summary>

If you work in a terminal agent, Vercel's `skills` command-line tool can install one skill from this repository. It's an optional route. Pasting a skill into a chat works everywhere and needs none of this.

```bash
npx skills add shaunmarsden/practical-ai-sales-workflows --skill outbound-prospecting
```

Add `--list` to see all seventeen skills without installing any, and `-a claude-code` to choose the agent. The tool is MIT licensed and `npx` downloads and runs it, so read what you're about to install first. It says so itself: installed skills run with full agent permissions. I wrote [a review of Vercel's own `find-skills` skill](https://github.com/shaunmarsden/skill-author/tree/main/example-three) if you want an idea of what to look for.

I tried this once on 14 October 2026, with version 1.7.2, in an empty folder and with Claude Code as the agent. It found all seventeen skills. It copied the whole `outbound-prospecting` folder, including `references/` and `agents/`, into `.claude/skills/`, and the copy matched this repository file for file. Two things to know:

- Four links in `SKILL.md` point to a guide, a workflow, an example and an evaluation outside the skill's folder, so they don't resolve in the installed copy. The skill itself doesn't need them.
- I tested one skill and one agent. Other agents use other folders, and I haven't tried them.

</details>

## When Loading Everything Is Still Fine

None of this means you should never load the full library. Exploring the repository, or working out which skills fit your role before you narrow down, are both good reasons to have everything to hand for a session. The [workflow router](workflow-router.md) is one small skill file that only needs its own routing table, not the rest of the library, so using it doesn't clash with loading a narrow set everywhere else. The advice above is for everyday use: a Project, Custom GPT or Gem used daily for one or two jobs, where the rest of the library is dead weight in every conversation.
