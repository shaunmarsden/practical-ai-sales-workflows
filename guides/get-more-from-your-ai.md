# Get More From Your AI

The [setup prompt](../templates/ai-sales-setup-prompt.md) gets you a well-briefed assistant. This page covers what comes next, once a single prompt stops being enough.

![Five layers for getting more from AI: a setup prompt, a project, a skill, a connection and an automation. Move up only when the current layer saves time, and keep human checking throughout.](../assets/diagrams/get-more-from-your-ai.svg)

## Remember These Three Things

### 📚 More Context Beats a Cleverer Prompt

A better-written prompt still only knows what fits in one message. A project full of your own reference material knows your job.

### 🔁 Repeatable Beats Reworded

If you write a new version of the same prompt every week, the method should become a skill. You don't need a better prompt.

### 🔌 Live Connections Remove Copying, Not Judgement

Pasting in a transcript or a CRM record works, but it's the slowest way. A live connection removes the copying, not the checking. You still have to pick the right source and notice when the data is stale or beside the point. A connection also often exposes more than the one record you meant to pull. Decide what a new connector can reach and what it's allowed to do before you switch it on. It isn't a free upgrade.

## Layer 2: Projects and Knowledge Bases

A project is a lasting workspace you can attach your reference material to. The AI then answers from your own context every time, not just from what fits in one prompt.

Set one up once you notice you're pasting the same background into more than a couple of conversations a week.

What's worth uploading:

- A short product or service one-pager, in plain English
- Your ICP and a description of your typical buyer
- A handful of your own past outputs you're happy with, as a style guide, with anything sensitive removed
- Your own playbooks or method notes, such as your objection responses or your rules for chasing

The same privacy rule applies here as everywhere else. Check what your company allows before you upload anything that could identify a real customer, deal or internal process.

<details>
<summary><strong>Where is this in each tool?</strong></summary>

- Claude: Projects, with files attached to the project's knowledge.
- ChatGPT: a Custom GPT's knowledge files, or Projects, depending on which you use.
- Gemini: a Gem with files attached, or a connected Workspace document.
- Copilot: often the least setup of the four, because it already reads files you keep in SharePoint or OneDrive without you attaching anything. Ask your IT team what's already connected before assuming you need to upload something.

Menu names and storage limits change over time, so look for "knowledge," "files," or "attach" in whatever project or assistant feature your tool has.

</details>

## Layer 3: Skills Instead of Reworded Prompts

A skill writes a method down once: what good output looks like, what to check before showing it, and what the AI must never invent or decide by itself. Instead of writing a new prompt each time you do the same task, you install the method once and it applies the same way every time.

This repository's [skills library](what-is-a-sales-ai-skill.md#try-the-skills-library) is a working set of these for common sales tasks. Install one instead of starting from scratch.

To build your own, the "How do I adapt one for my sales process?" section in [What Is a Sales AI Skill?](what-is-a-sales-ai-skill.md) takes you through the questions to ask. The skill files in this repository's [`.agents/skills/`](https://github.com/shaunmarsden/practical-ai-sales-workflows/tree/main/.agents/skills) folder show the shape one takes, and you can copy them: what it's for, the checks it runs, and what it must never do without you.

<details>
<summary><strong>Where is this in each tool?</strong></summary>

- Claude: Skills, uploaded to a Project's knowledge or added as a standalone skill, depending on your plan.
- ChatGPT: a Custom GPT's instructions, or a saved prompt you reuse rather than rewrite.
- Gemini: a Gem built around one task.
- Copilot: a custom agent, if your organisation lets you build one. If not, a saved prompt you reuse works just as well as a start, the same as in any other tool.

Whatever tool you use, what matters is that the method lives somewhere you can reuse it, not what the tool calls it. If Copilot is the only tool your organisation gives you, that's a normal place to start, not a lesser one, and everything in this layer still applies.

</details>

## Layer 4: Connectors and Integrations

A connector gives your AI tool live access to a system you already use, such as a CRM, a calendar, email or a transcription tool. It then reads real, current context, instead of you copying it in by hand each time.

It helps most with pulling in a call transcript instead of pasting it, checking a CRM record before drafting a follow-up, or reading your calendar to suggest meeting times that work.

The catch is that this layer is the most likely to need IT or admin approval, especially at a larger company. It's also where "what am I actually allowed to connect this to" matters most. If you don't control the settings of your AI tool, much of this may not be open to you, and that's fine. Layers 2 and 3 work perfectly well without it.

<details>
<summary><strong>Where is this in each tool?</strong></summary>

- Claude: connectors, where your plan has them, for tools such as a CRM, calendar or email.
- ChatGPT: connectors or Actions, depending on your plan and what your organisation has switched on.
- Gemini: Workspace integration, since Gemini already sits inside Gmail, Calendar and Docs for many users.
- Copilot: Microsoft Graph connectors. These are a real strength if your company already runs on Microsoft 365, because Outlook, Teams and SharePoint data is often reachable with less setup than a third-party connector elsewhere. Ask whoever runs it what's already switched on.

What's available changes often and varies a lot by plan and company policy. Treat this as a list of things to ask for, not a promise of what you already have.

</details>

## Layer 5: Automations and Agents

An automation or agent starts on a trigger, such as a schedule, a new CRM record or an email arriving, rather than waiting for you to start a conversation. It can run several steps by itself before coming back to you. This is where AI stops being something you talk to and starts doing a piece of your job in the background.

For a worked version of the coordination method you can inspect, see [Build an Approval-Gated Sales Copilot](build-an-approval-gated-sales-copilot.md). It includes a reusable template, a hard fictional source pack, the finished output and a score. It rests on my own report of using it at work, not on independent testing.

Some to try: a daily brief that reads your calendar and CRM each morning and tells you what needs attention; an agent that drafts a first-touch email for you to review as soon as a new lead lands in your CRM; or a weekly check for pipeline records with no next step.

### When the Trigger and the Action Live in Different Tools

Sometimes the thing you want to automate spans systems your AI tool can't see into. A new lead lands in the CRM. That should trigger an AI-drafted first-touch email, which a person must approve before anything is sent. A separate automation tool sits between those systems and chains the steps together, with an approval step before anything reaches a customer.

This is a much bigger step than anything else on this page. It usually means hosting something yourself or paying for a separate account, and building the connections yourself rather than ticking a setting in a tool you already use. Do it once the simpler layers above have proved themselves and you trust them, not as a first move. Not every reader needs it, and nobody should feel behind for not having it.

This layer also has the least room for error. The ground rules from the [setup prompt](../templates/ai-sales-setup-prompt.md) apply more strictly here, not less, because nobody reviews each step the way you'd review a single reply:

- Draft and prepare. Don't let it send an email or write to your CRM by itself, unless you set up that one action on purpose and trust it after watching it work
- Never let anything that reaches a customer run unsupervised until you've watched it do the task by hand, correctly, several times
- Give it the narrowest trigger and the narrowest job you can. "Draft a reply when this specific kind of email arrives" is safer and more useful than "handle my inbox"

<details>
<summary><strong>Where is this in each tool?</strong></summary>

- Claude: scheduled or multi-step agent runs, where your plan has them.
- ChatGPT: scheduled tasks, or a Custom GPT with Actions that run when you tell them to.
- Gemini: Workspace automation features, or a script your organisation builds around it.
- Copilot: Power Automate flows connected to Copilot. IT usually sets these up rather than a single user, but ask for them if your company already uses Power Automate for anything else, because the groundwork may already be there.

This is the newest and fastest-changing layer of all four. Treat the names above as things to ask about, not a promise of what your plan has today.

</details>

## Which Layer Is Worth Your Time Right Now

- If you explain the same background every time you start a conversation, set up a project.
- If you rewrite a version of the same prompt every week, turn it into a skill.
- If you keep copying and pasting from another tool into your AI conversation, and your company allows it, look at a connector.
- If you do the same multi-step task on a schedule or every time something happens, and you've already trusted the manual version several times, look at an automation or agent, with the ground rules above.

Move up a layer when the one you're on stops saving you anything, not because the next one sounds more advanced.
