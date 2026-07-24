# Downloadable Cross-Platform Skill Packages

Everything in this repository already works by cloning or browsing the whole thing. This is a smaller, separate idea: a single downloadable package for one skill, built for someone who wants that one skill in their own AI tool without pulling in the rest of the repository.

Built ahead of the usual real-use-evidence bar, on the project owner's own call rather than waiting for testing to show a bundle is useful. This guide documents the structure and demonstrates it once, against an existing skill; it does not publish an actual ZIP file, since a maintained duplicate copy would drift from the real skill files the moment either changed.

## What a Package Contains

- **The skill itself.** Its `SKILL.md` and everything in `references/`, `templates/` and `checks/`, exactly as it exists in [`.agents/skills/`](https://github.com/shaunmarsden/practical-ai-sales-workflows/tree/main/.agents/skills).
- **A plain-English guide.** What the skill is for and when to use it, in the same voice as [What Is a Sales AI Skill?](what-is-a-sales-ai-skill.md).
- **A fictional case.** The skill's own worked example, already required by [CONTRIBUTING.md](../CONTRIBUTING.md)'s completeness bar.
- **An output template.** Where one exists as its own file; otherwise the output shape described inline in `SKILL.md`.
- **The evaluation rubric.** The [sales AI output rubric](../evaluations/sales-ai-output-rubric.md), so a package carries the same scoring standard the rest of the repository uses, not a bundle-specific one.
- **Product-specific installation notes.** Where this skill's files actually go in Claude, ChatGPT, Gemini and Copilot: attached to a Project's or Custom GPT's knowledge, built into a Gemini Gem, or turned into a saved prompt for a tool without a knowledge-upload feature.

## Demonstrated Once: Identify Buyer Indecision

[identify-buyer-indecision](../.agents/skills/identify-buyer-indecision/SKILL.md) is used here because it already has every piece a package needs, without anything invented for this demonstration. Assembling a package for it means gathering exactly these existing files, unchanged:

1. `SKILL.md`
2. `references/output-contract.md`
3. `references/fictional-example.md`
4. `templates/output-template.md`
5. `checks/checklist.md`
6. The relevant excerpt of the [sales AI output rubric](../evaluations/sales-ai-output-rubric.md)
7. A short installation note per platform: attach the whole folder above to a Claude Project's knowledge, a Custom GPT's knowledge, or a Gemini Gem; use a saved prompt built from the same files for Copilot or any tool without a knowledge-upload feature.

That is the complete package. Nothing in it is new content; it is exactly what already exists, gathered into one place instead of six.

## Support a Manual Route, Never Claim Identical Behaviour

Every package must work by pasting the files into whichever tool the user actually has, not only by a platform-specific upload feature. State plainly that behaviour will not be identical across Claude, ChatGPT, Gemini and Copilot, since each interprets instructions and enforces structure slightly differently; a package guarantees the same instructions were given, not the same output every time.

## What Is Deliberately Not Built Yet

No installer, no ZIP file, and no automated packaging script exists. Building one before a manually-assembled package has actually been tried and found useful would be automating a process nobody has confirmed is worth the automation. If this idea moves further, the next real step is trying the manual assembly above with an actual user outside this repository, not building tooling around an unproven bundle.
