# Pick the Right Proof Point: Not Worth Adding

## Status

**The method didn't beat a plain instruction, so I left it out.**

## The Job

You have several case studies. Which one should you use with this buyer, if any, and what can you honestly claim from it?

Nothing here helps with that. Some pages mention proof points, such as the [lost opportunity review](../workflows/04-lost-opportunity-review.md) and the [chase skill](../.agents/skills/plan-chase-sequence/SKILL.md), but none helps you choose one. The [business case skill](../.agents/skills/build-business-case/SKILL.md) sorts evidence into confirmed, inference and unknown, but only about the buyer's own situation. The [router](../.agents/skills/workflow-router/SKILL.md) has no route for it, though the [Sales Copilot example](../guides/build-an-approval-gated-sales-copilot.md) lists "Select an Approved Proof Point" as one of its routes.

So the gap was real. It turned out not to matter.

## What I Tested

My method checks each proof point. Is it the same problem? Did it happen to people like the buyer's? Was it measured? Could something else explain the result? Can you share it? Would using it stretch what happened? It also allows the answer "none of these". The full method is at the bottom of this page.

I compared it with a plain instruction, the kind a seller would type:

> You are helping a salesperson choose a proof point. Read the buyer brief and proof library below and answer the question at the end. Be careful not to overclaim.

I ran each version six times. Each run saw only its instructions and the scenario. Before I wrote the method or ran anything, I wrote down what would count as a pass or a fail. I scored all 12 runs without knowing which version produced which.

## The Scenario

I made up the scenario. Dominic Achebe runs field operations at Vantry Water, which has 140 field engineers. They finish each job on a handheld app, then type the same notes into a second system by hand. Dominic thinks this takes six hours a week each, but he's never measured it. His director wants the cost justified and wants to know whether the change will cut errors in the records, which Dominic cares about more. He said: "Every vendor shows me a number from someone else's business. My jobs vary more than a typical site. I want to know what actually transfers."

The library has seven proof points. Each has a catch.

| Proof point | The catch |
| --- | --- |
| Kelbrook Water | Same industry, but about call centre times, not this problem |
| Orrindale Energy | A projected £840,000 a year, worked out by pre-sales and never measured |
| Pennhallow Facilities | Same task and a big drop, but they replaced their handhelds at the same time |
| Danecourt Logistics | Measured and clean, but the people were planners at desks, not engineers in the field |
| Sallowfield Water | The best match, and the only one with error figures, but it's under NDA and can't be described even without the name |
| Braylock Gas | Praise from a customer, with no numbers |
| Halewood Water | Same industry, task and people, measured with nothing else changed, and cleared to share, but only a pilot of 12 engineers, with the other 95 not measured |

The right answer is the least impressive one. Use Halewood for the hours, and keep it to the 12 engineers rather than scaling it up to 140. On errors, there's nothing you can use, because you can't share the only proof point that measured them.

## What Happened

Both versions did equally well on everything I'd decided to measure.

| | Plain instruction | Method |
| --- | ---: | ---: |
| Treated the estimate as a real result | 0 of 6 | 0 of 6 |
| Used the NDA proof point | 0 of 6 | 0 of 6 |
| Gave the product credit for a drop the new handhelds may have caused | 0 of 6 | 0 of 6 |
| Scaled the 12-engineer pilot up to 140 | 0 of 6 | 0 of 6 |
| Claimed a match that wasn't there | 0 of 6 | 0 of 6 |
| Made up a figure, quote or customer | 0 of 6 | 0 of 6 |
| Forced in a proof point where none fitted | 0 of 6 | 0 of 6 |
| Chose Halewood | 6 of 6 | 6 of 6 |
| Said nothing usable covers errors | 6 of 6 | 6 of 6 |
| Explained why the NDA one was out, rather than skipping it | 6 of 6 | 6 of 6 |

I'd decided in advance that if the plain instruction failed once or not at all, the method wasn't worth adding. It didn't fail at all.

## The One Difference

Every method run reminded the seller to check the sharing permission was still valid before sending. No plain-instruction run did. That matters, because permission given last year may not hold now.

But I hadn't planned to measure it. I only noticed it after everything I had planned to measure came out the same. That's when you'd go looking for a reason to keep your own method. I first counted it with a quick search, then checked again with a wider search, and made sure that search could find the point. The count held.

It's worth a line in a guide. It isn't worth a new workflow, skill, recipe card and prompt. Adding those would also mean updating 22 places, across 17 files, that say how many jobs, skills or workflows there are.

## Two Small Mistakes

One method run got Halewood's size wrong. It treated the 95 unmeasured engineers as the whole workforce. The real total is 107, and four other runs got it right, three of them plain-instruction runs.

One plain-instruction run offered a guess about errors, clearly labelled as untested. That isn't a failure, but no other run came closer to guessing.

## What This Doesn't Show

It doesn't show the job isn't real. It shows this method didn't beat a plain instruction here.

The scenario may be too easy. Every catch shows in the proof point descriptions, so a careful reader spots them all without help. A harder test would hide the NDA note in a longer entry. Or it would offer two close proof points, so choosing takes judgement. If a test like that separated the two versions, the method would be worth testing again.

This is also one scenario, one model and six runs each, and I wrote the method and scored every run.

## Corrections

An earlier version of this page gave a 330-word summary of the method and called it the full text. It also said adding a job would change nine places rather than 22, and that three runs got the 107 total right rather than four. I've fixed all three.

## The Method I Tested

<details>
<summary><strong>The method, word for word as the six runs read it</strong></summary>

I've removed only the addresses of its four links. They pointed at files that don't exist, because I never published the method.

```text
---
name: proof-point-selection
description: Decide which of several proof points, case studies or past results should be used with a specific buyer, and state exactly what each one entitles you to claim. Use when more than one example is available and you need to choose between them, or when you suspect the most impressive one is not the most defensible. Do not use this to write the follow-up itself, or to judge whether the product fits the buyer at all; use the fit-and-limitations-review skill for that.
---

# Pick the Right Proof Point

> Landed here directly rather than clicking through from a guide? This file is the instruction sheet an AI assistant follows, not written for a first read start to finish. What is a sales AI skill? has the plain-English version.

You do not need to install anything to try this once. The lines between the dashes at the very top are just this file's label; leave them in. On GitHub, copy this using the **Raw** button near the top of the page rather than selecting the rendered text, so the tables and links below paste in cleanly. Send the whole file as your first message in any AI chat tool, then follow it with your actual inputs.

This chooses between the proof points you already have, on relevance and evidential strength rather than on size of number, and says what each one does and does not let you claim.

## Gather the Inputs

What the buyer actually said they are concerned about, in their own words where possible, and the candidate proof points with whatever the record holds about each: what the customer did, what changed, how that was established, who it happened to, and whether it can be shared.

## Start From the Buyer's Concern

Write down what the buyer is worried about before looking at the library. If they raised more than one concern, take each separately: a proof that answers one does not answer another, and merging them is how a strong result on the wrong question gets through. Choosing first and justifying afterwards is the failure this step exists to prevent.

## Separate What Was Measured From What Was Estimated

For each candidate say plainly which it is: measured before and after by a stated method, estimated or modelled from assumptions, reported by the customer without measurement, or qualitative only. A modelled figure is not a result, whatever its size, and a warm quotation is not a number. Carry that label with the claim every time, so the distinction survives into whatever gets written.

## Check Whether the Result Is Attributable

A measured change is evidence for your product only if nothing else plausible changed at the same time. Where the record shows another change in the same period, the honest reading is that the result cannot be attributed to one cause. Saying so is not a weakness in the proof point; failing to say it is a weakness in the claim.

## Check What You Are Allowed to Share

Some evidence is real, relevant and unusable. Confidential or unapproved material stays internal, and that covers describing the result without naming the customer: an anonymous account of a single identifiable deployment is still a disclosure. If the closest proof is the one that cannot be shared, you have no usable proof for that point, not a quietly reworded version of it.

## Judge the Problem and the Context Separately

Same industry is not the same problem. A result from the buyer's own sector on a different workflow is a worse fit than the same workflow in another sector, and reading "same industry" as relevance is the most common way an unrelated number gets used. Ask separately whether the people are comparable: their role, their working conditions, and anything about the setting that plausibly drove the result. Say which of the two matches and which does not, rather than collapsing both into one impression of closeness.

## Say What the Proof Entitles You to Claim

State the claim in the narrowest form the source supports: what was measured, over what period, for how many people, in what role. Do not scale a result measured on a small group into a figure for the buyer's whole organisation. Where the buyer needs a number for their own organisation, the honest offer is to measure it with them rather than to multiply somebody else's.

## Be Willing to Return Nothing

For any concern where no candidate is close enough on problem, context, evidence and permission, say that plainly and stop. Naming the gap is more useful than a stretched proof, and a buyer who has asked what actually transfers will notice the stretch.

## Apply the Guardrails

- Never present an estimate, a model or a projection as a measured result.
- Never use confidential or unapproved evidence externally, named or unnamed.
- Never attribute a result to your product where the record shows another change in the same period.
- Never scale a result beyond the group it was measured on.
- Never invent a figure, a quotation, a customer or a similarity.
- Never choose the most impressive candidate over the most defensible one, and say so when those differ.
- No em dashes, no emojis.

## Stop When the Task Is Unsafe

Do not produce a selection when:

- The buyer's concern is not established well enough to judge relevance against it
- The record does not say how any result was arrived at, so measured and estimated cannot be told apart
- The request is to make one particular proof point fit, rather than to find which one does
- The request is to use evidence the record marks as confidential or unapproved

## Require Human Review

Selecting a proof point is not sending one. Before anything goes out, a person confirms that the sharing permission is still current, since permission changes and a library goes out of date, and that they will stand behind the claim in the form it is finally written.

Read the fictional proof library and completed selection for a worked test, and the honest evaluation for how it scored.
```

</details>
