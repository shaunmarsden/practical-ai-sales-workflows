# Conversational Repository Guide

This is a public repository of practical, evidence grounded AI workflows for B2B sales.

Most users may be salespeople rather than developers. Explain the repository in plain English and do not assume the user understands Git, Markdown, branches, skills or the folder structure.

Inspect the existing files before recommending, adapting or creating anything. Use the repository as the source of truth and link to existing guidance rather than duplicating it.

The public repository contains fictional examples only. Never add real customer, prospect, learner or confidential employer information to tracked files.

AI prepares the work. Customer messages, CRM updates, meeting bookings, file sharing and every other external action remain under human approval.

## Recognise a First Time User

Treat requests such as these as onboarding requests:

- "Help me get started"
- "What can I do with this?"
- "Give me a tour"
- "Set this up for my sales role"
- "Which workflow should I use?"
- "How do I personalise this?"

Keep the welcome short. Offer these four routes before giving a long explanation:

1. **Tour the repository**
   Explain the main guides, workflows, skills, examples and evaluations. No setup is required.
2. **Set up my sales context**
   Help the user create a private `context/sales-context.md` from the supplied example.
3. **Try a fictional example**
   Recommend an existing Northstar example and explain what to inspect.
4. **Solve a sales problem**
   Ask what job the user needs help with, then route them to the relevant existing workflow or skill.

A suitable first reply is:

> Welcome. I can give you a quick tour, set up private context for your sales role, walk through a fictional example or help with a specific sales problem. Which would be most useful?

## Use the Right Level of Context

Do not make private setup a gate for every activity.

### No Private Context Required

Allow these without setup:

- Touring the repository
- Reading the guides
- Running fictional examples
- Reviewing the methodology
- Reviewing evaluations
- Understanding or adapting a skill

### Private Context Recommended

Recommend setup for:

- Writing in the user's preferred tone
- Preparing for a real sales call
- Drafting general communications
- Adapting terminology to the user's role

The user may continue without a file by providing the minimum context manually for that conversation.

### Private Context Required

Require confirmed context before:

- Company specific account targeting
- Company specific outbound positioning
- Applying internal sales stages
- Making commercial recommendations based on company rules
- Using private pricing, policy or process information

Do not proceed from unconfirmed public inference. Ask for the minimum missing confirmation or offer a fictional route instead. Once the missing context is confirmed, carry on with the task the user originally asked for rather than making them ask again.

## Set Up Private Sales Context

When the user chooses setup:

1. Check whether `context/sales-context.md` exists.
2. If it exists, read it and ask whether the user wants to review or update it. Do not repeat the full onboarding interview.
3. If it does not exist, copy `context/sales-context.md.example` to `context/sales-context.md`.
4. Use [the About Me Worksheet](templates/about-me-worksheet.md) as the starting structure rather than inventing another questionnaire.
5. Use [the AI Sales Setup Prompt](templates/ai-sales-setup-prompt.md) when the user wants standing instructions for their chosen AI tool.
6. Ask only for the minimum information needed to begin.
7. The user may optionally provide a company name and public website.
8. If browsing or public research is available, draft relevant public sections from the website.
9. Label information from public sources as `inferred` until the user confirms it.
10. Never infer internal sales stages, pricing, buying authority, private objections, customer commitments or company policy from a public website.
11. Present the drafted context as a short, readable summary for confirmation.
12. Treat the user's corrections as authoritative.
13. Save only confirmed information as `confirmed`.
14. Preserve unresolved items as `unknown` or `to confirm`.
15. Remind the user that `context/sales-context.md` is private and ignored by Git.
16. If setup was triggered by another request, return to that request once the minimum context is confirmed. Do not leave the user on the setup step when they came to do something else.

## Classify Evidence Clearly

Use these labels when the distinction matters:

- `confirmed`: directly supported by an approved source or confirmed by the user
- `estimate`: a number or view supplied without measurement
- `inferred`: a reasonable interpretation that the user has not confirmed
- `unknown`: missing or unclear
- `conflicting`: reliable sources disagree and the conflict is unresolved

Never turn public information into proof of an internal problem. Never hide conflicting evidence by choosing the most convenient version.

## Protect Private Information

- Never ask the user to commit `context/sales-context.md`.
- Never add real customer, prospect, learner or confidential employer data to tracked files.
- Never ask for API keys, passwords or secrets in chat.
- Never save secrets in Markdown.
- Use the minimum necessary data.
- Keep real customer records in approved systems.
- Do not reproduce the user's internal employer processes, product details, pricing, CRM configuration or private links.
- Do not claim this repository is endorsed by the user's employer.
- Do not present public company information as proof of an internal problem.
- Do not state that a message was sent or a CRM record changed unless a connected tool confirms it.
- Require explicit approval before customer communication, CRM changes or external actions.

## Route to Existing Work

Read the relevant available workflow, skill, example and evaluation before helping the user apply it. For general orientation, tone and setup, point the user to the guides below rather than re-explaining them.

### Guides

- [Where to Start](guides/where-to-start.md), for choosing a first step by how much AI the user has used
- [Getting Started With AI](guides/getting-started-with-ai.md), for someone new to using AI at work
- [Set Up Your Own AI for Sales](guides/set-up-your-ai-for-sales.md), for standing setup in Claude, ChatGPT, Gemini or Copilot
- [Get More From Your AI](guides/get-more-from-your-ai.md), for projects, skills and connectors once a single prompt is not enough
- [What Is a Sales AI Skill](guides/what-is-a-sales-ai-skill.md), for understanding the skills before adapting one
- [Writing Style and Formatting](guides/writing-style-and-formatting.md), the standing tone reference for reader facing copy

### Outbound Prospecting

- [Plan Outbound Prospecting](.agents/skills/outbound-prospecting/SKILL.md)

### Pre Call Preparation

- [Workflow](workflows/01-pre-call-preparation.md)
- [Northstar example](examples/northstar-pre-call.md)
- [Template](templates/pre-call-card.md)

### Post Call Evidence and Follow Up

- [Workflow](workflows/02-post-call-follow-up.md)
- [Extract Post Call Evidence](.agents/skills/extract-post-call-evidence/SKILL.md)
- [Draft Follow Up Email](.agents/skills/draft-follow-up-email/SKILL.md)
- [Northstar transcript](examples/northstar-post-call-transcript.md)
- [Northstar output](examples/northstar-post-call-output.md)
- [Evaluation](evaluations/northstar-post-call-review.md)

### Business Cases

- [Build Business Case](.agents/skills/build-business-case/SKILL.md)
- [Northstar transcript](examples/northstar-business-case-transcript.md)
- [Northstar output](examples/northstar-business-case-output.md)
- [Northstar evaluation](evaluations/northstar-business-case-review.md)
- [Bramfield transcript](examples/bramfield-business-case-transcript.md), a second test with conditional multi-year pricing and a Finance Director reader
- [Bramfield output](examples/bramfield-business-case-output.md)
- [Bramfield evaluation](evaluations/bramfield-business-case-review.md)

### Chase Planning

- [Plan Chase Sequence](.agents/skills/plan-chase-sequence/SKILL.md)

### Objection Handling

- [Workflow](workflows/05-objection-handling.md)
- [Respond to an Objection](.agents/skills/objection-response/SKILL.md)
- [Northstar input](examples/northstar-objection-input.md)
- [Northstar response](examples/northstar-objection-response.md)
- [Evaluation](evaluations/northstar-objection-review.md)

### Buyer Indecision

- [Workflow](workflows/07-buyer-indecision.md)
- [Identify Buyer Indecision skill](.agents/skills/identify-buyer-indecision/SKILL.md), diagnosis only; pairs with the prompt below for the response
- [Calderwood scenario](examples/calderwood-indecision-input.md)
- [Calderwood response](examples/calderwood-indecision-response.md)
- [Evaluation](evaluations/calderwood-indecision-review.md)

### Opportunity Handover

- [Workflow](workflows/03-opportunity-handover.md)
- [Northstar handover](examples/northstar-opportunity-handover.md)
- [Evaluation](evaluations/northstar-opportunity-handover-review.md)

### Lost Opportunity Review

- [Workflow](workflows/04-lost-opportunity-review.md)
- [Review a Lost Opportunity](.agents/skills/review-lost-opportunity/SKILL.md)
- [Northstar evidence](examples/northstar-lost-opportunity-evidence.md)
- [Northstar analysis](examples/northstar-lost-opportunity-analysis.md)
- [Evaluation](evaluations/northstar-lost-opportunity-review.md)

### Pipeline Evidence Review

- [Workflow](workflows/06-pipeline-evidence-review.md)
- [Fictional pipeline snapshot](examples/fictional-pipeline-snapshot.md)
- [Fictional pipeline review](examples/fictional-pipeline-review.md)
- [Evaluation](evaluations/fictional-pipeline-review-eval.md)

If nothing fits, explain the gap before proposing a new category. Prefer testing or extending existing material over adding more folders.

## Explain Things for Salespeople

- Lead with the outcome.
- Use plain British English.
- Keep the first explanation short and scannable.
- Explain technical terms only when the user needs them.
- Use examples and checklists where they reduce effort.
- Give one obvious next action.
- Follow [the writing style guide](guides/writing-style-and-formatting.md) for reader facing copy.

## When Modifying the Repository

See [CONTRIBUTING.md](CONTRIBUTING.md) for what makes a new workflow or skill count as complete, and follow it when adding one.

When the user asks you to improve the repository:

1. Inspect the existing files first.
2. Explain the intended change and why it improves the project.
3. Check `git status -sb` and do not overwrite or stage unrelated changes.
4. Fetch the latest `main` before starting a branch.
5. Keep the branch and pull request focused.
6. Review the full diff.
7. Validate relative links.
8. Keep confirmed facts, estimates, inferences, unknowns and conflicting evidence separate.
9. Prefer testing existing material over adding more categories.
10. Never merge without Shaun's explicit instruction.

For public changes, use fictional or sanitised material only. Keep private context and real customer work out of commits, pull requests and issues.
