# Private Sales Context

This folder tells the AI about your sales role without putting your company's information in the public project.

The Hartwell examples are fictional and the same for everyone. Your private sales context says how you work, what your company sells and which rules the AI should follow for your role.

## Create Your Private File

The easiest way is to open the repository in Codex or Claude Code and say:

> Help me set up my private sales context.

The agent copies `sales-context.md.example` to `sales-context.md` and asks only for what it needs to start.

If you're happy using a terminal, you can make the copy yourself from the repository folder:

```text
cp context/sales-context.md.example context/sales-context.md
```

Git ignores the new `context/sales-context.md` file. The example and this guide stay public.

## What May Be Safe to Include

- Your own role and responsibilities
- A plain English description of what the company sells
- General customer types and problems you solve
- Your preferred writing style
- Your normal sales stages, if your company allows it
- Tools you use and the actions that need your approval
- Links to approved public or internal sources, if your company allows them

Use the [About Me Worksheet](../templates/about-me-worksheet.md) to gather the basics. Use the [AI Sales Setup Prompt](../templates/ai-sales-setup-prompt.md) if you also want standing instructions for another AI tool.

## What Should Stay Elsewhere

Don't use this file as a customer database.

Keep these in approved company systems:

- Customer and prospect records
- Real call transcripts and emails
- Private pricing or commercial terms
- Passwords, API keys and secrets
- Confidential contracts, policies or internal links
- Information your employer doesn't allow in the AI tool you're using

Give it the least you can. A useful description of your role beats a copy of the whole CRM.

## Optional: Map Your Own Qualification Method

You might use a named qualification method (MEDDIC, BANT, a custom internal framework) or your own names for pipeline stages. If your employer allows it, [the sales methodology overlay](sales-methodology-overlay.md.example) lets a workflow such as pipeline evidence review or objection handling use your language and criteria instead of generic ones. Copy it the same way:

```text
cp context/sales-methodology-overlay.md.example context/sales-methodology-overlay.md
```

Git ignores this file too. It's optional: every workflow here works without it.

## How the Agent Uses It

The agent reads the file when a task needs your company or role context. It uses confirmed information as it stands, labels anything it infers and leaves missing information as unknown.

You can still tour the repository, read guides and run fictional examples without this file.

If you'd rather not create it, give the minimum context by hand in one conversation. Don't write that information into tracked repository files.

## Public Research Still Needs Your Confirmation

You can give the agent your company name and public website. If it can browse, it can use public research to draft parts of the context.

Public information doesn't prove an internal sales problem, process, price or policy. The agent must label research as inferred until you confirm it. Your corrections come first.

## Update or Remove It

Ask the agent to review the context when your role, product, process or writing style changes. It should update only the sections you confirm.

To remove it, delete `context/sales-context.md` from your local copy. The public example stays, so you can set it up again later.

## Never Commit These

Don't add `context/sales-context.md` or `context/sales-methodology-overlay.md` to a commit, pull request or public repository.

Before you publish a change, check that Git still ignores them:

```text
git check-ignore -v context/sales-context.md context/sales-methodology-overlay.md
```
