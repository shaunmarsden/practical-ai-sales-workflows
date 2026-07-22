# Practical AI Sales Workflows

<p>
  <img alt="Status: Building in public" src="https://img.shields.io/badge/status-building%20in%20public-2563eb">
  <img alt="Focus: B2B sales" src="https://img.shields.io/badge/focus-B2B%20sales-16a34a">
  <img alt="Examples: Fictional" src="https://img.shields.io/badge/examples-fictional-7c3aed">
</p>

AI gets talked about a lot in sales. I wanted somewhere to document the things I have actually tried.

These are practical workflows for everyday sales jobs. Pick a problem, see what the workflow produces and use anything that helps.

> AI helps with the preparation. The salesperson is still responsible for the judgement.

**Want the repository to guide you?** Open it in Codex or Claude Code and say "help me get started". The agent can give you a tour, set up private sales context, run a fictional example or route you to the right workflow. [See the simple guide](guides/run-this-repository-with-an-ai-coding-agent.md).

## 🧭 Three Ways to Start

**🌱 New to AI, or want to set it up properly first?** [Find your starting point](guides/where-to-start.md) based on how much you have actually used AI already, then [fill in the About Me Worksheet](templates/about-me-worksheet.md) and [copy the setup prompt](templates/ai-sales-setup-prompt.md), or skip the worksheet and use the [interactive setup prompt](templates/interactive-setup-prompt.md), which asks you the same questions in conversation and writes the finished prompt for you. This works in Claude, ChatGPT, Gemini, Copilot, or anything else with a custom instructions field. If Copilot is the only one your organisation gives you access to, that is a completely normal starting point, not a lesser one.

**🎯 Know the sales problem you want help with?** Jump straight to [Choose a Sales Problem](#-choose-a-sales-problem) below and pick from prospecting, call prep, follow-up, business case, chasing, objections, handover, or a lost-opportunity review.

**🧪 Want to see it work before you read anything else?** [Watch a skill actually work &rarr;](https://shaunmarsden.github.io/practical-ai-sales-workflows/). It shows the fictional Hartwell transcript turning into evidence-labelled output, live, with every line traced back to where it came from. Then check the [honest scores](evaluations/sales-ai-output-rubric.md) and the [cross-model comparison](evaluations/cross-model-post-call-comparison.md) rather than taking the demo's word for it.

Once a single setup prompt stops being enough on its own, [Get More From Your AI](guides/get-more-from-your-ai.md) covers projects and knowledge bases, turning repeated prompts into skills, and connecting real tools like a CRM or a transcription app.

## 🎯 Choose a Sales Problem

Want the short version, one page per job, nothing else to read? [Open the recipe cards](recipes/README.md) instead.

```mermaid
flowchart TB
    subgraph S1["Before there is a deal"]
        A1["Find the Next Prospect"]
    end
    subgraph S2["Around the call"]
        A2["Prepare for a Sales Call"]
        A3["Follow Up After a Sales Call"]
    end
    subgraph S3["Build the case"]
        A4["Build a Business Case"]
        A5["Help a Champion Carry Your Case"]
    end
    subgraph S4["Keep it moving"]
        A6["Chase a Quiet Prospect"]
        A7["Handle an Objection"]
        A8["Spot a Real Objection Pattern"]
        A9["Move a Stalled Decision"]
    end
    subgraph S5["Where it ends up"]
        A10["Hand Over an Opportunity"]
        A11["Review a Lost Opportunity"]
    end
    subgraph S6["Manage the whole pipeline, runs alongside"]
        A12["Review Your Pipeline"]
        A13["Keep Your CRM Honest"]
        A14["Get a Weekly View"]
    end
    S1 --> S2 --> S3 --> S4 --> S5
```

Fourteen jobs, grouped by where they sit in a deal. Pipeline management runs alongside the others rather than after them; it is not a step every deal passes through in order.

### 🔎 Find the Next Prospect

Pick a target and draft a first-touch message worth a reply, without a generic hook or a meeting-led ask.

**Start here:** [Open the workflow](workflows/09-outbound-prospecting.md) · [See the Cedarwell signal](examples/cedarwell-outbound-input.md) · [See the completed output](examples/cedarwell-outbound-output.md) · [See a deliberately weak version, for contrast](examples/cedarwell-outbound-weak-example.md) · [Use the prompt](templates/outbound-prospecting-prompt.md)

**Use with AI:** [Plan outbound prospecting](.agents/skills/outbound-prospecting/SKILL.md)

**Just the one page:** [Recipe card](recipes/find-the-next-prospect.md)

### 📞 Prepare for a Sales Call

Pull scattered information into one short call card that you can scan during the conversation.

**Start here:** [Open the workflow](workflows/01-pre-call-preparation.md) · [See the Hartwell example](examples/hartwell-pre-call.md) · [Use the card template](templates/pre-call-card.md)

**Optional practice:** [Roleplay pushback before the call](templates/pre-call-objection-roleplay-prompt.md) · [See what it produces](examples/hartwell-pre-call-roleplay.md)

**Just the one page:** [Recipe card](recipes/prepare-for-a-sales-call.md)

### ✉️ Follow Up After a Sales Call

Turn a transcript or clear notes into a summary, actions, email draft and CRM suggestions without inventing momentum.

**Start here:** [Open the workflow](workflows/02-post-call-follow-up.md) · [See the finished output](examples/hartwell-post-call-output.md) · [Use the prompt](templates/post-call-follow-up-prompt.md)

**Use with AI:** [Learn what a sales AI skill is](guides/what-is-a-sales-ai-skill.md) · [Extract evidence from the call](.agents/skills/extract-post-call-evidence/SKILL.md) · [Draft the follow-up email](.agents/skills/draft-follow-up-email/SKILL.md)

**Just the one page:** [Recipe card](recipes/follow-up-after-a-sales-call.md)

### 📄 Build a Business Case

Turn call evidence into a tailored business case for the person who was not on the call.

**Start here:** [See the Hartwell transcript](examples/hartwell-business-case-transcript.md) · [See the finished business case](examples/hartwell-business-case-output.md) · [Read the honest review](evaluations/hartwell-business-case-review.md)

**A second, different test:** [See the Bramfield transcript](examples/bramfield-business-case-transcript.md) · [See the finished business case](examples/bramfield-business-case-output.md) · [Read the honest review](evaluations/bramfield-business-case-review.md): a conditional two-year price instead of a flat figure, and a Finance Director reader who was never on a call

**Use with AI:** [Build or audit a business case](.agents/skills/build-business-case/SKILL.md)

**Just the one page:** [Recipe card](recipes/build-a-business-case.md)

### 🗣️ Help a Champion Carry Your Case

Prepare an internal champion to present or forward your case to other stakeholders, without assuming what they care about from their job title, and without contacting anyone beyond the champion yourself.

**Start here:** [Open the workflow](workflows/12-champion-enablement.md) · [See the Hartwell scenario](examples/hartwell-champion-enablement-input.md) · [See the completed output](examples/hartwell-champion-enablement-output.md) · [Read the honest review](evaluations/hartwell-champion-enablement-review.md)

**Use with AI:** [Champion enablement](.agents/skills/champion-enablement/SKILL.md)

**Just the one page:** [Recipe card](recipes/help-a-champion-carry-your-case.md)

### 🔁 Chase a Quiet Prospect

Decide what, if anything, to send next, rather than working through a fixed run of increasingly persistent emails.

**Use with AI:** [Plan the chase sequence](.agents/skills/plan-chase-sequence/SKILL.md)

**Just the one page:** [Recipe card](recipes/chase-a-quiet-prospect.md)

### 🙅 Handle an Objection

Diagnose what is actually driving a stated objection before answering it, rather than arguing with the surface wording.

**Start here:** [Open the workflow](workflows/05-objection-handling.md) · [See the Hartwell response](examples/hartwell-objection-response.md) · [Use the prompt](templates/objection-handling-prompt.md)

**Use with AI:** [Respond to an objection](.agents/skills/objection-response/SKILL.md)

**Just the one page:** [Recipe card](recipes/handle-an-objection.md)

### 📚 Spot a Real Objection Pattern

Look across several deals for a repeated objection, and check whether it is genuinely one issue or several unrelated situations that just sound similar.

**Start here:** [Open the workflow](workflows/11-objection-pattern-review.md) · [See the fictional objection log](examples/fictional-objection-pattern-log.md) · [See the completed analysis](examples/fictional-objection-pattern-review.md) · [Use the prompt](templates/objection-pattern-review-prompt.md)

**Just the one page:** [Recipe card](recipes/spot-a-real-objection-pattern.md)

### 🕰️ Move a Stalled Decision

Help a willing buyer who keeps delaying the final yes, by making the decision safer rather than selling harder, once you have confirmed it is genuine indecision and not something else.

**Start here:** [Open the workflow](workflows/07-buyer-indecision.md) · [See the Calderwood scenario](examples/calderwood-indecision-input.md) · [See the completed response](examples/calderwood-indecision-response.md) · [Use the prompt](templates/buyer-indecision-prompt.md)

**Use with AI:** [Identify buyer indecision](.agents/skills/identify-buyer-indecision/SKILL.md), a diagnosis-only skill that pairs with the prompt above

**Just the one page:** [Recipe card](recipes/move-a-stalled-decision.md)

### 🤝 Hand Over an Opportunity

Pass the current position, evidence, risks and next action to another person without making the deal sound further along than it is.

**Start here:** [Open the workflow](workflows/03-opportunity-handover.md) · [See the Hartwell handover](examples/hartwell-opportunity-handover.md) · [Use the prompt](templates/opportunity-handover-prompt.md)

**Just the one page:** [Recipe card](recipes/hand-over-an-opportunity.md)

### 📪 Review a Lost Opportunity

Work out honestly whether a closed or stalled deal is actually over, or just blocked, before deciding whether there is a real way back in.

**Start here:** [Open the workflow](workflows/04-lost-opportunity-review.md) · [See the Hartwell analysis](examples/hartwell-lost-opportunity-analysis.md) · [Use the prompt](templates/lost-opportunity-review-prompt.md)

**Use with AI:** [Review a lost opportunity](.agents/skills/review-lost-opportunity/SKILL.md)

**Just the one page:** [Recipe card](recipes/review-a-lost-opportunity.md)

### 📊 Review Your Pipeline

Check whether the stages, close dates and next steps in your CRM are actually supported by the evidence you hold, rather than trusting the pipeline because it is written down.

**Start here:** [Open the workflow](workflows/06-pipeline-evidence-review.md) · [See the fictional pipeline snapshot](examples/fictional-pipeline-snapshot.md) · [See the completed review](examples/fictional-pipeline-review.md) · [Use the prompt](templates/pipeline-evidence-review-prompt.md)

**Just the one page:** [Recipe card](recipes/review-your-pipeline.md)

### 🧹 Keep Your CRM Honest

Audit a CRM export for duplicates, missing fields and stale records, so you can trust it before using it for a total or a report, without touching anything yourself.

**Start here:** [Open the workflow](workflows/08-crm-hygiene-review.md) · [See the fictional CRM export](examples/fictional-crm-export.md) · [See the completed review](examples/fictional-crm-hygiene-review.md) · [Use the prompt](templates/crm-hygiene-review-prompt.md)

**Just the one page:** [Recipe card](recipes/keep-your-crm-honest.md)

### 📋 Get a Weekly View Without Building a Dashboard

Pull pipeline, meetings, outreach and new signals into one honest weekly report, composing what other workflows already found rather than redoing the analysis, and marking anything missing instead of guessing it.

**Start here:** [Open the workflow](workflows/10-weekly-operating-review.md) · [See what was available](examples/fictional-weekly-operating-review-input.md) · [See the completed report](examples/fictional-weekly-operating-review-output.md) · [Use the prompt](templates/weekly-operating-review-prompt.md)

**Just the one page:** [Recipe card](recipes/get-a-weekly-view.md)

## 🧭 How I Approach It

```mermaid
flowchart TB
    A["1. Start with the problem<br/>Use safe, relevant information"]
    B["2. Let AI prepare<br/>Organise, draft and spot gaps"]
    C["3. Keep a person in control<br/>Check, decide, act and improve"]
    A --> B --> C
```

The full approach is explained in the [methodology](METHODOLOGY.md), with the public data boundaries in [responsible use](RESPONSIBLE-USE.md). [Contributing](CONTRIBUTING.md) sets out when a workflow or skill actually counts as complete.

New to using AI at work at all? Start with [getting started with AI](guides/getting-started-with-ai.md). The [writing style guide](guides/writing-style-and-formatting.md) is the standing tone and formatting reference behind every draft in this repository.

## 🧪 See One Complete Test

The Hartwell example follows one fictional sales conversation from the call to the finished follow up.

**[Read the transcript](examples/hartwell-post-call-transcript.md)** → **[See the finished output](examples/hartwell-post-call-output.md)** → **[Read the honest review](evaluations/hartwell-post-call-review.md)**

You can also score your own result using the [sales AI output rubric](evaluations/sales-ai-output-rubric.md), and [log your own time saved](guides/measure-time-and-quality.md) rather than assuming a workflow helps because it reads well.

Curious whether the model actually matters? [See the same test run cold in Claude, ChatGPT and Gemini](evaluations/cross-model-post-call-comparison.md), scored the same way.

## 🛡️ Rules That Matter

- Keep facts, estimates and assumptions separate
- Do not invent commitments, dates or customer intent
- Keep sensitive information out of unapproved tools
- Require a person to approve emails and CRM changes

## About Me

I am Shaun Marsden and I work in B2B sales. I am using this project to learn what AI is genuinely useful for in the job and to share the things worth keeping.

This is an independent learning project. Every company, person and conversation in the examples is fictional.

## What I Want to Try Next

**Right now:** real usability feedback, getting even one or two actual salespeople to try a workflow and say honestly whether it saved time or just moved the work around, rather than trusting my own judgement of my own output.

**After that:**

- CRM hygiene (duplicates, ownership, stale records), building on the pipeline evidence review already here
- A genuine way to measure time saved and output quality, not just assume a workflow helps because it reads well
- Purposeful visuals for sharing, a social preview card and a cross-model comparison graphic, best done as a concentrated session rather than squeezed in

See [ROADMAP.md](ROADMAP.md) for the full picture, including the longer backlog of ideas still to validate.
