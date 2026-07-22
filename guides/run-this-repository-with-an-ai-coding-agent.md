# Run This Repository With an AI Coding Agent

Open this repository in Codex or Claude Code and say:

> Help me get started.

The agent will explain what is here, help you set up private context, show you a fictional example or route you to the right sales workflow. You do not need to understand the folder structure first.

## What the Agent Does Here

Codex and Claude Code can read the repository instructions and work across its guides, workflows, skills, examples and evaluations.

They can help you find and adapt the material. They do not replace your judgement, send customer messages or change your CRM without approval.

## Open the Repository

If the repository is already on your computer, open its folder in your AI coding agent.

If it is not, copy it from GitHub first:

```text
git clone https://github.com/shaunmarsden/practical-ai-sales-workflows.git
```

Cloning means making a local working copy that can receive future updates. If you are not comfortable with the terminal, ask someone to help with this one step or use GitHub's download option for a read only copy.

### Codex

Open the local repository folder in Codex as your workspace, start a conversation and say "help me get started". Codex reads the root `AGENTS.md` as the repository's standing guidance.

### Claude Code

Open a terminal in the local repository folder, start Claude Code and say "help me get started". The short `CLAUDE.md` points Claude to the same shared guidance in `AGENTS.md`.

## Choose One of Four Routes

The agent will offer:

1. **Tour the repository**
   See the main guides, workflows, skills, examples and evaluations without setting anything up.
2. **Set up my sales context**
   Create a private local file describing your role, company and working rules.
3. **Try a fictional example**
   Walk through an existing Hartwell example before using any real information.
4. **Solve a sales problem**
   Choose the job you need help with and use the relevant existing workflow or skill.

Reply with the route you want. You do not need to write a detailed prompt.

## Set Up Private Sales Context

Your private context lives in `context/sales-context.md`. It is made from the public example but ignored by Git, so it should not appear in commits or pull requests.

Ask the agent:

> Help me set up my private sales context.

It will use the existing [About Me Worksheet](../templates/about-me-worksheet.md), ask for the minimum useful information and show you a summary before saving confirmed details.

You may give it a company name and public website. Public research must remain labelled as inferred until you confirm it. The agent must not guess internal stages, prices, policies, buying authority or customer problems from a website.

Read [the private context guide](../context/README.md) before adding company information.

You can skip this setup and give the minimum information manually for one conversation. A tour and every fictional example work without private context.

## Try a Fictional Example First

The Hartwell examples let you see the method without using customer data.

A good first request is:

> Walk me through the fictional Hartwell post call example. Show me what the workflow got right and what still needed checking.

The agent should read:

- [The fictional transcript](../examples/hartwell-post-call-transcript.md)
- [The finished output](../examples/hartwell-post-call-output.md)
- [The honest evaluation](../evaluations/hartwell-post-call-review.md)

## Personalise a Workflow

Tell the agent the sales job you need help with, not the AI feature you want to use.

For example:

> I need to prepare for a sales call. Show me the existing workflow and help me adapt it to my role.

The agent should inspect the relevant existing workflow, skill, example and evaluation before suggesting changes. It should use confirmed private context when the task depends on your company or role.

There is no single setup that fits every salesperson or business. Keep what helps, change the terminology and leave out anything that does not match your process.

## Keep a Person in Control

The agent may draft or recommend work. You still approve:

- Customer and prospect messages
- CRM updates and stage changes
- Meeting bookings
- Prices, discounts and commercial commitments
- Files shared outside your organisation
- Any other external action

Do not accept a claim that something was sent or changed unless a connected tool confirms it.

## Do Not Put These in the Repository

- Real customer or prospect records
- Real call transcripts and emails
- Passwords, API keys or secrets
- Confidential pricing, policies or internal links
- Private employer processes or CRM configuration
- Anything your company does not permit in the AI tool you are using

Keep real customer material in approved company systems. Use fictional examples when the real information is not necessary.

## Update the Repository Safely

If you want the agent to improve the public repository, say:

> Create a branch, make the change, show me the diff and open a draft pull request. Do not merge it.

A branch is a separate copy of the work where a change can be made safely. A pull request is the review page showing exactly what would change. Nothing should be merged into the main version until you have reviewed it and explicitly asked for the merge.

The agent should check the existing files, keep the change focused, validate links and leave private context out of the pull request.

## Acknowledgement

The conversational repository onboarding idea was inspired in part by [Akshat Thakur's GTM Engine](https://github.com/akshathakurr/gtm-engine). No code or wording was copied, and the projects are not affiliated.
