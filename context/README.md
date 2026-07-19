# Private Sales Context

This folder lets the repository understand your sales role without putting your company information into the public project.

The public Northstar examples are fictional and the same for everyone. Your private sales context describes how you work, what your company sells and which rules the AI should follow for your role.

## Create Your Private File

The easiest route is to open the repository in Codex or Claude Code and say:

> Help me set up my private sales context.

The agent will copy `sales-context.md.example` to `sales-context.md` and ask only for the information needed to begin.

If you are comfortable using a terminal, you can make the copy yourself from the repository folder:

```text
cp context/sales-context.md.example context/sales-context.md
```

The new `context/sales-context.md` file is ignored by Git. The example and this guide remain public.

## What May Be Safe to Include

- Your own role and responsibilities
- A plain English description of what the company sells
- General customer types and problems you solve
- Your preferred writing style
- Your normal sales stages, if your company permits this
- Tools you use and the actions that require your approval
- Links to approved public or internal sources, if your company permits them

Use the [About Me Worksheet](../templates/about-me-worksheet.md) to gather the basics. Use the [AI Sales Setup Prompt](../templates/ai-sales-setup-prompt.md) if you also want standing instructions for another AI tool.

## What Should Stay Elsewhere

Do not use this file as a customer database.

Keep these in approved company systems:

- Customer and prospect records
- Real call transcripts and emails
- Private pricing or commercial terms
- Passwords, API keys and secrets
- Confidential contracts, policies or internal links
- Information your employer does not allow in the AI tool you are using

Use the minimum information needed. A useful role description is better than a copy of the entire CRM.

## How the Agent Uses It

The agent reads the file when a task needs your company or role context. It uses confirmed information directly, keeps inferences labelled and leaves missing information as unknown.

You can still tour the repository, read guides and run fictional examples without creating this file.

If you choose not to create it, provide the minimum context manually in one conversation. That information should not be written into tracked repository files.

## Public Research Still Needs Your Confirmation

You may give the agent your company name and public website. It can use public research to draft parts of the context when browsing is available.

Public information is not proof of an internal sales problem, process, price or policy. The agent must label research as inferred until you confirm it. Your corrections take priority.

## Update or Remove It

Ask the agent to review the context when your role, product, process or writing style changes. It should update only the sections you confirm.

To remove it, delete `context/sales-context.md` from your local repository. The public example will remain available if you want to set it up again later.

## Never Commit It

Do not add `context/sales-context.md` to a commit, pull request or public repository.

Before publishing a change, check that Git still ignores it:

```text
git check-ignore -v context/sales-context.md
```
