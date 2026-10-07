# Conversational Repository Guide

This is a public repository of practical AI workflows for B2B sales, built on evidence.

Most users are likely to be salespeople, not developers. Explain the repository in plain English. Don't assume the user understands Git, Markdown, branches, skills or the folder structure.

Read the existing files before you recommend, adapt or create anything. Treat the repository as the source of truth, and link to existing guidance rather than repeating it.

The public repository holds fictional examples only. Never add real customer, prospect, learner or confidential employer information to tracked files.

AI prepares the work. A person approves customer messages, CRM updates, meeting bookings, file sharing and every other action outside the repository.

## Recognise a First Time User

Treat requests like these as a new user wanting to get started:

- "Help me get started"
- "What can I do with this?"
- "Give me a tour"
- "Set this up for my sales role"
- "Which workflow should I use?"
- "How do I personalise this?"

Keep the welcome short. Offer these four routes before any long explanation:

1. **Tour the repository**
   Explain the main guides, workflows, skills, examples and evaluations. No setup needed.
2. **Set up my sales context**
   Help the user create a private `context/sales-context.md` from the example provided.
3. **Try a fictional example**
   Recommend an existing Hartwell example and explain what to look at.
4. **Solve a sales problem**
   Ask what job the user needs help with, then send them to the existing workflow or skill that fits.

A good first reply:

> Welcome. I can give you a quick tour, set up private context for your sales role, walk through a fictional example or help with a specific sales problem. Which would be most useful?

## Use the Right Level of Context

Don't make private setup a condition for everything.

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

The user can carry on without a file by giving the minimum context by hand for that conversation.

### Private Context Required

Require confirmed context before:

- Company specific account targeting
- Company specific outbound positioning
- Applying internal sales stages
- Making commercial recommendations based on company rules
- Using private pricing, policy or process information

Don't go ahead on the strength of public information the user hasn't confirmed. Ask for the least confirmation you need, or offer a fictional route instead. Once the user confirms the missing context, carry on with the task they first asked for. Don't make them ask again.

## Set Up Private Sales Context

When the user chooses setup:

1. Check whether `context/sales-context.md` exists.
2. If it exists, read it and ask whether the user wants to review or update it. Don't repeat the full set of setup questions.
3. If it does not exist, copy `context/sales-context.md.example` to `context/sales-context.md`.
4. Start from [the About Me Worksheet](templates/about-me-worksheet.md) rather than inventing another questionnaire.
5. Use [the AI Sales Setup Prompt](templates/ai-sales-setup-prompt.md) when the user wants standing instructions for their chosen AI tool.
6. Ask only for the least information needed to start.
7. The user can choose to give a company name and public website.
8. If you can browse or search, draft the public sections that apply from the website.
9. Label information from public sources as `inferred` until the user confirms it.
10. Never infer internal sales stages, pricing, buying authority, private objections, customer commitments or company policy from a public website.
11. Show the drafted context as a short, readable summary for the user to confirm.
12. The user's corrections win.
13. Save only confirmed information as `confirmed`.
14. Keep anything unresolved as `unknown` or `to confirm`.
15. Remind the user that `context/sales-context.md` is private and ignored by Git.
16. If another request led to setup, go back to that request once the minimum context is confirmed. Don't leave the user stuck on setup when they came to do something else.
17. If the user has a named qualification method or their own pipeline stage names, and their employer allows sharing that even privately, offer [the sales methodology overlay](context/sales-methodology-overlay.md.example) as a separate, optional step. It isn't part of the basic setup. Never push it on a user who hasn't asked for it.

## Classify Evidence Clearly

Use these labels when the distinction matters:

- `confirmed`: an approved source says it directly, or the user confirmed it
- `estimate`: a number or view given without measuring it
- `inferred`: a reasonable reading the user hasn't confirmed
- `unknown`: missing or unclear
- `conflicting`: reliable sources disagree and nobody has settled it

Never treat public information as proof of an internal problem. Never hide conflicting evidence by picking the version that suits you.

## Protect Private Information

- Never ask the user to commit `context/sales-context.md`.
- Never add real customer, prospect, learner or confidential employer data to tracked files.
- Never ask for API keys, passwords or secrets in chat.
- Never save secrets in Markdown.
- Use the least data you need.
- Keep real customer records in approved systems.
- Don't reproduce the user's employer's internal processes, product details, pricing, CRM configuration or private links.
- Don't claim the user's employer endorses this repository.
- Don't present public company information as proof of an internal problem.
- Don't say a message was sent or a CRM record changed unless a connected tool confirms it.
- Get clear approval before any customer message, CRM change or other outside action.

## Route to Existing Work

Read the workflow, skill, example and evaluation that apply before you help the user use them. For general orientation, tone and setup, point the user to the guides below rather than explaining them again.

If the user wants the short version of a job rather than the full workflow, point them to the matching [recipe card](recipes/README.md) instead of explaining the workflow yourself.

### Guides

- [Where to Start](guides/where-to-start.md), for choosing a first step by how much AI the user has used
- [Getting Started With AI](guides/getting-started-with-ai.md), for someone new to using AI at work
- [Set Up Your Own AI for Sales](guides/set-up-your-ai-for-sales.md), for standing setup in Claude, ChatGPT, Gemini or Copilot
- [Get More From Your AI](guides/get-more-from-your-ai.md), for projects, skills and connectors once a single prompt is not enough
- [What Is a Sales AI Skill](guides/what-is-a-sales-ai-skill.md), for understanding the skills before adapting one
- [Writing Style and Formatting](guides/writing-style-and-formatting.md), the standing reference for tone in anything a reader sees
- [Measure Time Saved and Output Quality](guides/measure-time-and-quality.md), for logging your own time honestly as well as scoring the output
- [Workflow Router](guides/workflow-router.md) and [its skill](.agents/skills/workflow-router/SKILL.md), for when a user describes a situation in their own words rather than naming a workflow, or when two workflows sound alike and it matters which one fits
- [Choose Your Route by Role](guides/role-based-routes.md), for a user who would rather start from their job title (account executive, sales manager, RevOps, customer success, founder-led sales) than from a list of sales problems
- [Sibling Repositories](guides/sibling-repositories.md), a guide to adapting this repository's format to another business function, only if someone who does that job leads it; it isn't a plan for this repository
- [Future Interfaces](guides/future-interfaces.md), design specs for four ideas a long way off (a role-play simulator, an interactive evidence workspace, a lead-qualification view that shows its reasoning, a before-and-after tool for testing instructions), none of which exist as software yet
- [Downloadable Skill Packages](guides/downloadable-skill-packages.md), the structure for a single-skill package (the skill, a guide, a fictional case, a template, the rubric, notes for each platform), tried once on identify-buyer-indecision without publishing a ZIP
- [Selective Installation](guides/selective-installation.md), how to load only some skills into a Project, Custom GPT, Gem or Copilot agent on each platform, once the user knows which ones they want
- [Curated Bundles](guides/curated-bundles.md), three starter groups of existing recipe cards (a starter pack, a post-call pack, a deal progression pack) for a first-time reader who doesn't want to read all seventeen cards to find their job
- [Progressive Disclosure](guides/progressive-disclosure.md), the standard for keeping a skill's core `SKILL.md` short and moving deeper material into supporting files, with a check of the current skills against it
- [Composing Longer Workflows](guides/composing-longer-workflows.md), principles for chaining workflows together (working folders, visible progress, spend checkpoints, a manual route, method before platform, judgement versus mechanics, visible instructions); it doesn't describe software that exists here yet
- [Build an Approval-Gated Sales Copilot](guides/build-an-approval-gated-sales-copilot.md), how to build an agent that chooses between several tightly scoped workflows, based on my own private sales copilot, with a reusable vendor-neutral template, a fictional test drawing on several sources, a scored evaluation and a [real-use finding with private details removed](evaluations/sales-copilot-live-run-finding.md)

### Outbound Prospecting

- [Workflow](workflows/09-outbound-prospecting.md)
- [Plan Outbound Prospecting](.agents/skills/outbound-prospecting/SKILL.md)
- [Cedarwell signal](examples/cedarwell-outbound-input.md)
- [Cedarwell output](examples/cedarwell-outbound-output.md)
- [Evaluation](evaluations/cedarwell-outbound-review.md)

### Pre Call Preparation

- [Workflow](workflows/01-pre-call-preparation.md)
- [Prepare for a Sales Call skill](.agents/skills/prepare-for-sales-call/SKILL.md)
- [Hartwell source pack](examples/hartwell-pre-call-input.md)
- [Original Hartwell example](examples/hartwell-pre-call.md)
- [Hartwell skill output](examples/hartwell-pre-call-skill-output.md)
- [Evaluation](evaluations/hartwell-pre-call-review.md)
- [Template](templates/pre-call-card.md)
- [Objection roleplay prompt](templates/pre-call-objection-roleplay-prompt.md), optional practice once the card is done
- [Hartwell roleplay example](examples/hartwell-pre-call-roleplay.md)

### Post Call Evidence and Follow Up

- [Workflow](workflows/02-post-call-follow-up.md)
- [Extract Post Call Evidence](.agents/skills/extract-post-call-evidence/SKILL.md)
- [Draft Follow Up Email](.agents/skills/draft-follow-up-email/SKILL.md)
- [Hartwell transcript](examples/hartwell-post-call-transcript.md)
- [Hartwell output](examples/hartwell-post-call-output.md)
- [Evaluation](evaluations/hartwell-post-call-review.md)

### Fit and Limitations Review

- [Workflow](workflows/13-fit-and-limitations-review.md)
- [Fit and Limitations Review skill](.agents/skills/fit-and-limitations-review/SKILL.md)
- [Kellow scenario](examples/kellow-fit-review-input.md)
- [Kellow output](examples/kellow-fit-review-output.md)
- [Evaluation](evaluations/kellow-fit-review-review.md)

### Business Cases

- [Build Business Case](.agents/skills/build-business-case/SKILL.md)
- [Hartwell transcript](examples/hartwell-business-case-transcript.md)
- [Hartwell output](examples/hartwell-business-case-output.md)
- [Hartwell evaluation](evaluations/hartwell-business-case-review.md)
- [Bramfield transcript](examples/bramfield-business-case-transcript.md), a second test with conditional multi-year pricing and a Finance Director reader
- [Bramfield output](examples/bramfield-business-case-output.md)
- [Bramfield evaluation](evaluations/bramfield-business-case-review.md)

### Champion Enablement

- [Workflow](workflows/12-champion-enablement.md)
- [Champion Enablement skill](.agents/skills/champion-enablement/SKILL.md)
- [Hartwell scenario](examples/hartwell-champion-enablement-input.md)
- [Hartwell output](examples/hartwell-champion-enablement-output.md)
- [Evaluation](evaluations/hartwell-champion-enablement-review.md)

### Chase Planning

- [Plan Chase Sequence](.agents/skills/plan-chase-sequence/SKILL.md)
- [Hartwell chase scenario](examples/hartwell-chase-input.md)
- [Hartwell chase decision](examples/hartwell-chase-output.md)
- [Evaluation](evaluations/hartwell-chase-review.md)

### Objection Handling

- [Workflow](workflows/05-objection-handling.md)
- [Respond to an Objection](.agents/skills/objection-response/SKILL.md)
- [Hartwell input](examples/hartwell-objection-input.md)
- [Hartwell response](examples/hartwell-objection-response.md)
- [Evaluation](evaluations/hartwell-objection-review.md)

### Objection Pattern Review

- [Workflow](workflows/11-objection-pattern-review.md)
- [Review Objection Patterns skill](.agents/skills/review-objection-patterns/SKILL.md)
- [Fictional objection log](examples/fictional-objection-pattern-log.md)
- [Fictional objection pattern review](examples/fictional-objection-pattern-review.md)
- [Evaluation](evaluations/fictional-objection-pattern-review-eval.md)
- [Second fictional log](examples/fictional-objection-pattern-log-two.md)
- [Second skill output](examples/fictional-objection-pattern-review-two.md)
- [Second evaluation](evaluations/fictional-objection-pattern-second-eval.md)

### Buyer Indecision

- [Workflow](workflows/07-buyer-indecision.md)
- [Identify Buyer Indecision skill](.agents/skills/identify-buyer-indecision/SKILL.md), which only diagnoses; use it with the prompt below for the response
- [Calderwood scenario](examples/calderwood-indecision-input.md)
- [Calderwood response](examples/calderwood-indecision-response.md)
- [Evaluation](evaluations/calderwood-indecision-review.md)
- [Real-use boundary finding](evaluations/buyer-indecision-real-use-finding.md)

### Opportunity Handover

- [Workflow](workflows/03-opportunity-handover.md)
- [Opportunity Handover skill](.agents/skills/opportunity-handover/SKILL.md)
- [Hartwell transcript](examples/hartwell-post-call-transcript.md) and [post-call output](examples/hartwell-post-call-output.md)
- [Hartwell handover update](examples/hartwell-opportunity-handover-update.md), a harder fictional test with conflicting notes and a change of contact
- [Hartwell handover](examples/hartwell-opportunity-handover.md)
- [Evaluation](evaluations/hartwell-opportunity-handover-review.md)
- [Real-use finding](evaluations/opportunity-handover-real-use-finding.md)

### Lost Opportunity Review

- [Workflow](workflows/04-lost-opportunity-review.md)
- [Review a Lost Opportunity](.agents/skills/review-lost-opportunity/SKILL.md)
- [Hartwell evidence](examples/hartwell-lost-opportunity-evidence.md)
- [Hartwell analysis](examples/hartwell-lost-opportunity-analysis.md)
- [Evaluation](evaluations/hartwell-lost-opportunity-review.md)

### Pipeline Evidence Review

- [Workflow](workflows/06-pipeline-evidence-review.md)
- [Pipeline evidence review skill](.agents/skills/pipeline-evidence-review/SKILL.md)
- [Fictional pipeline snapshot](examples/fictional-pipeline-snapshot.md)
- [Fictional pipeline review](examples/fictional-pipeline-review.md)
- [Evaluation](evaluations/fictional-pipeline-review-eval.md)

### CRM Hygiene Review

- [Workflow](workflows/08-crm-hygiene-review.md)
- [CRM hygiene review skill](.agents/skills/crm-hygiene-review/SKILL.md)
- [Fictional CRM export](examples/fictional-crm-export.md)
- [Fictional CRM hygiene review](examples/fictional-crm-hygiene-review.md)
- [Evaluation](evaluations/fictional-crm-hygiene-review-eval.md)

### Weekly Operating Review

- [Workflow](workflows/10-weekly-operating-review.md)
- [What was available](examples/fictional-weekly-operating-review-input.md)
- [Completed report](examples/fictional-weekly-operating-review-output.md)
- [Evaluation](evaluations/fictional-weekly-operating-review-eval.md)

### Outbound Campaign Learning Review

- [Workflow](workflows/14-outbound-campaign-learning-review.md)
- [Prompt](templates/outbound-campaign-learning-review-prompt.md)
- [Fictional campaign data](examples/cedarwell-campaign-review-input.md)
- [Completed review](examples/cedarwell-campaign-review-output.md)
- [Evaluation](evaluations/cedarwell-campaign-review-eval.md)

If nothing fits, explain the gap before you suggest a new category. Test or extend what's here before adding more folders.

## Explain Things for Salespeople

- Lead with the outcome.
- Use plain British English.
- Keep the first explanation short and scannable.
- Explain technical terms only when the user needs them.
- Use examples and checklists where they reduce effort.
- Give one obvious next action.
- Follow [the writing style guide](guides/writing-style-and-formatting.md), including Orwell's six rules, for everything you write here, evaluations included.

## Keep Visuals Consistent

Before you create or change a diagram, read [the Gemini visual style prompt](templates/gemini-visual-style-prompt.md) and look at the approved examples in `assets/diagrams/`.

- Keep visuals playful, warm and easy for a salesperson with no technical background to follow.
- Avoid anything that resembles a consultancy slide, corporate process map or software architecture diagram.
- Use the approved navy, teal, amber and warm neutral palette.
- Prefer SVGs with character, so text stays sharp and the artwork stays editable.
- Gemini can help develop an idea, but never publish an image with a watermark, a text error or words too small to read.
- Check every diagram at about 700 pixels wide before you publish it.
- Compare every word against the approved copy and add useful alt text.
- Vary the layouts, but keep them looking like one family. Sticky notes, speech bubbles, doodles, curved paths and slightly uneven shapes are welcome.

## When Modifying the Repository

[CONTRIBUTING.md](CONTRIBUTING.md) says when a new workflow or skill counts as complete. Follow it when you add one.

When the user asks you to improve the repository:

1. Read the existing files first.
2. Explain the change you plan and why it makes the project better.
3. Check `git status -sb`, and don't overwrite or stage unrelated changes.
4. Fetch the latest `main` before starting a branch.
5. Keep the branch and pull request to one piece of work.
6. Review the full diff.
7. Validate relative links.
8. Keep confirmed facts, estimates, inferences, unknowns and conflicting evidence separate, and keep them so when you rewrite. Check that the new wording hasn't made a claim stronger, firmer or more causal than the evidence supports. The full rule is under House Style in [CONTRIBUTING.md](CONTRIBUTING.md#house-style).
9. Test existing material before adding more categories.
10. Never merge unless I tell you to.

For public changes, use only fictional material or material with private details removed. Keep private context and real customer work out of commits, pull requests and issues.
