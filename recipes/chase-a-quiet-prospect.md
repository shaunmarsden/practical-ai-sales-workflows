# 🔁 Recipe: Chase a Quiet Prospect

One job, one page, with the prompt on it. Nothing else in the repository is required to use this.

## Helps with

Deciding what, if anything, to send next when a prospect has gone quiet, rather than working through a fixed run of increasingly persistent emails on a timer.

## You need

- The original call detail
- What has already been sent and when
- Anything that has happened since (an out-of-office reply, a changed role, silence with no signal)
- How many chases have already gone out

## You'll get

- A decision: chase now, wait, change the stakeholder, add evidence first, reframe, close the loop, or stop pursuing
- Only once that decision is made, a message anchored to something real from the call

<!-- prompts:begin -->

## Paste this into your AI tool

<!-- prompt:begin source=templates/chase-sequence-prompt.md -->
```text
Act as a careful sales chase adviser.

Use only the information I provide. Do not invent interest, disinterest, urgency, authority, a reply, a commitment or a reason for the silence.

A chase is a decision, not a template on a timer. Decide what to do before drafting anything.

Before writing any of the sections below, build a dated commitment ledger. List every date, deadline or commitment in what I have given you, including any the prospect set for themselves, and separately list every period anyone is stated to be away, unavailable or not monitoring messages. Then check each date in the first list against each period in the second and note which of them fall inside one. Carry that result into section 1 in words, including when nothing collides. The ledger itself is a working step, not part of the output.

Produce the following sections:

1. What the silence actually tells us
Separate what is evidenced from what is not. A stated reason for being away, a changed role or a known busy period is evidence. Silence on its own is not evidence of lost interest. If a task, reminder or date was set before something later changed the picture, say so rather than treating it as current.

2. The decision
Choose exactly one and say why, in one or two sentences:
- Chase now: enough time has passed and there is a genuine reason to reach out
- Wait: not enough time has passed, or a known reason makes now a bad time. Say what to wait for and roughly when to revisit
- Change the stakeholder: the contact has gone quiet in a way that suggests they are not the route forward. Only choose this if someone else has actually been identified as a route, not merely mentioned
- Add evidence before chasing: a specific new piece of information would make the next message worth sending. Say what
- Reframe: the original angle did not land, and a different specific angle anchored to the call might
- Close the loop: enough silence has passed that continuing would look worse than a clean close-out
- Stop pursuing: there is a clear signal, an explicit no or a confirmed loss of budget or authority

3. The message, only if the decision was to send one
Name which stage it is and draft it.
- Early: confirm the last thing landed and nudge toward one concrete next step. Short, one clear ask
- Middle: surface a likely blocker or question before it becomes an unstated reason not to proceed. Offer something useful rather than only asking for a reply
- Late: re-anchor to the original problem that made them interested, not to your solution. If timing has genuinely moved, offer a real alternative
- Final: use a real constraint, a real date or a real limit. Never manufactured scarcity
- Close-out: acknowledge the sequence directly rather than pretending this is the first message. State what happens next as fact, not a threat. Leave the door open in one short sentence

If the decision was not to send one, write "No message yet" and instead prepare only what will be useful later, plus what to watch for.

4. What must not be assumed
List what a person still has to confirm before acting on any of this.

Rules:

- Anchor every message to something real the prospect said or did, never to your own pipeline pressure
- Never open with "just checking in", "just circling back", "hope you're well" or "I wanted to follow up"
- Friction escalates, urgency does not. The earliest chase carries the real ask; each one after asks for something smaller and easier to say yes to, rather than the same ask restated harder
- Each message must stand alone and add exactly one new thing
- Do not remind the prospect that earlier messages were sent. The close-out stage is the only exception, where acknowledging the sequence honestly is the job
- If a reply is already sitting unanswered, say so and stop. That is a reply situation, not a chase situation
- No manufactured urgency or scarcity, no em dashes, no emojis
- Write dates with an ordinal suffix, for example 20th July
- Do not send anything, schedule anything or change any record. Prepare it for a person to approve
- Where evidence is missing, write Unknown rather than filling the gap
```
<!-- prompt:end -->

Then paste your own notes underneath it. Everything the prompt needs is listed under **You need** above.

<!-- prompts:end -->

## Open

**[Skill](../.agents/skills/plan-chase-sequence/SKILL.md)**  
Also: [Sequence stages in detail](../.agents/skills/plan-chase-sequence/references/sequence-stages.md) · [Worked example](../examples/hartwell-chase-output.md) · [Honest review](../evaluations/hartwell-chase-review.md)

## The AI cannot decide

Whether a signal (a stated reorganisation, a quiet stretch, an explicit no) is genuinely a reason to wait, change tack or stop, when the evidence itself is ambiguous.

## You must check

- The anchor is something real from the prospect's side, never your own pipeline pressure
- There is no manufactured urgency or scarcity
- It does not remind the prospect you have already emailed them, unless this is the final close-out message
- A live reply has not been mistaken for silence

## Then

Send only once you agree with the decision made, and check the CRM for the deal's actual current state before sending anything, not just the notes or last email.

---

Want the fuller method, the sequence shapes, or the guardrails for when not to chase at all? Open the [skill](../.agents/skills/plan-chase-sequence/SKILL.md) itself.

---

**Tried this recipe?** [Give quick private feedback](https://docs.google.com/forms/d/e/1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/viewform) or [share public feedback](https://github.com/shaunmarsden/practical-ai-sales-workflows/discussions/new?category=feedback). It takes about two minutes. Please do not include customer, employer or confidential information.
