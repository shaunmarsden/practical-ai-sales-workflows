# Downloadable Cross-Platform Skill Packages

Everything here already works if you clone or browse the whole repository. This is a smaller, separate idea: one downloadable package for one skill, for someone who wants that skill in their own AI tool without the rest.

I wrote this before any testing showed a package is useful, which is earlier than I'd usually publish. This guide sets out the structure and tries it once, on an existing skill. It doesn't publish a ZIP file, because a second copy would drift from the real skill files as soon as either changed.

## What a Package Contains

- The skill itself: its `SKILL.md` and everything in `references/`, `templates/` and `checks/`, exactly as it sits in [`.agents/skills/`](https://github.com/shaunmarsden/practical-ai-sales-workflows/tree/main/.agents/skills).
- A plain-English guide to what the skill is for and when to use it, in the same voice as [What Is a Sales AI Skill?](what-is-a-sales-ai-skill.md).
- A fictional case: the skill's own worked example, which [CONTRIBUTING.md](../CONTRIBUTING.md) already requires.
- An output template, where one exists as its own file. Otherwise, the output shape described in `SKILL.md`.
- The [sales AI output rubric](../evaluations/sales-ai-output-rubric.md), so a package is scored the same way as the rest of the repository, not by its own standard.
- Installation notes for each product: where the files go in Claude, ChatGPT, Gemini and Copilot. That means attaching them to a Project's or Custom GPT's knowledge, building them into a Gemini Gem, or turning them into a saved prompt for a tool that can't take uploaded knowledge.

## Demonstrated Once: Identify Buyer Indecision

I used [identify-buyer-indecision](../.agents/skills/identify-buyer-indecision/SKILL.md) because it already has every piece a package needs, with nothing made up for this. Building its package means gathering these existing files, unchanged:

1. `SKILL.md`
2. `references/output-contract.md`
3. `references/fictional-example.md`
4. `templates/output-template.md`
5. `checks/checklist.md`
6. The relevant part of the [sales AI output rubric](../evaluations/sales-ai-output-rubric.md)
7. A short installation note for each platform: attach the whole folder above to a Claude Project's knowledge, a Custom GPT's knowledge, or a Gemini Gem. For Copilot, or any tool that can't take uploaded knowledge, use a saved prompt built from the same files.

That's the whole package. None of it is new. It's what already exists, gathered in one place instead of six.

## Support a Manual Route, Never Claim Identical Behaviour

Every package must work by pasting the files into whatever tool you have, not only through one platform's upload feature. Say plainly that Claude, ChatGPT, Gemini and Copilot won't behave the same, because each reads instructions and follows structure a little differently. A package makes sure each tool got the same instructions. It doesn't promise the same output every time.

## What Is Deliberately Not Built Yet

There's no installer, no ZIP file and no packaging script. Building one before anyone has tried a hand-built package and found it useful would mean automating something nobody has shown is worth it. If this goes further, the next step is to try the manual version above with a real user outside this repository, not to build tools around an untested package.
