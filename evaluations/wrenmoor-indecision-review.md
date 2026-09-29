# Wrenmoor Buyer Indecision Review

This page scores the [worked response](../examples/wrenmoor-indecision-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests a harder pattern than the [Calderwood test](calderwood-indecision-review.md). Here each reason the buyer gives is fair on its own and does get resolved, but a new reason turns up straight after. In Calderwood the same unresolved reason kept coming back.

## Result

**Score: 46 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Gets the three reasons, the order they were resolved and the exact wording of Farrah's messages right |
| Evidence fidelity | 5 | Keeps the pattern of one reason resolved after another as the real signal, rather than flattening it into one soft delay |
| Fact separation | 4 | Mostly careful, but states "the chain has no visible end" as settled fact. It's really the diagnosis's own inference from three data points, with no confirmed fourth |
| Missing information | 4 | Flags that a phased rollout is only conditional, but doesn't flag that the 34-seat count was confirmed without rechecking the price for that number, a separate open commercial detail |
| Commercial usefulness | 5 | Offers a different play from either pushing on the offsite or waiting for it, and treats the offsite as fair throughout |
| Next step clarity | 4 | Asks Farrah to name a specific week, which is concrete, but doesn't say what happens if she doesn't, or replies with another open-ended reason |
| Tone | 5 | Names the pattern without blame, and says it isn't a criticism |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | Says plainly that nothing has been sent, and leaves the phased-rollout option out of the draft since it isn't confirmed as available |
| Hallucination risk | 4 | Three concrete data points support the pattern, which is stronger than one unclear request. But it's still an inference about an unstated internal reason, and the response's own condition to re-diagnose if a specific concern comes up does real work to keep it honest |

## What Worked

It refused to call reason one or two indecision on its own, because a real budget or headcount question still open would be a fair reason to wait. The diagnosis only firms up once the pattern across all three shows.

It treated the team offsite as a fair reason in its own right rather than arguing with it, while still naming the sequence around it. That avoids the obvious trap of disputing a dated, believable constraint.

It didn't invent a date for "right after" the offsite. It built the next step around getting Farrah to name one.

It left the phased-rollout option out of the draft reply, keeping it conditional in the method section rather than sending a term nobody had confirmed.

## What Needed Checking

"The chain has no visible end" is a strong claim from three data points. It's a reasonable read, but a person should confirm nothing fair is still open before treating the diagnosis as settled. For instance, was the price for 34 seats ever rechecked?

The draft doesn't say what happens if Farrah's next reply gives a fourth soft reason rather than a firm week. The pipeline decision section covers this for the diagnosis, but the draft reply doesn't.

The link between seat count and price is the one commercial detail this test found that the response doesn't raise as an open question. It's worth checking directly rather than assuming it was settled along with the headcount.

## What I Changed in the Prompt

Nothing in the skill needed changing for this run. The skill has to rule out a real chain of dependencies before calling something indecision, and to treat each reason as fair while it's still open. Both held, even against a pattern built to look like careful checking at every step. The offsite was the hardest single test point in this scenario, and the skill didn't treat it as a clean outside blocker just because it had a date.

## Next Test

Run a case where the pattern looks the same, three reasons resolved in turn, but the third turns out to be a real, confirmed outside blocker, not another soft reason. That checks whether the skill stops treating the sequence as proof of indecision once a real block is confirmed, rather than applying the pattern whatever the evidence later shows.
