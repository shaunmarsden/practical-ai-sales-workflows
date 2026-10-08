# Hartwell Business Case Review

This page scores the [worked business case](../examples/hartwell-business-case-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Names, figures, pricing and roles match both transcripts |
| Evidence fidelity | 5 | Keeps the measured pilot figure and the earlier unmeasured estimate apart |
| Fact separation | 5 | Flags the compliance confirmation as pending, not delivered |
| Missing information | 5 | Flags both the QBR date and the compliance sign-off as outstanding |
| Commercial usefulness | 5 | States plainly the figure Priya has to approve, and shows the sum |
| Next step clarity | 4 | The next step is clear, but the exact timing depends on two people, neither of whom has confirmed a date |
| Tone | 4 | Reads as a proposal for Priya, not a letter to Alex, though I'd still want a final pass before it goes out |
| Privacy | 5 | Names no account executive, as instructed |
| Approval discipline | 5 | The document is clearly a draft, and nothing is presented as sent, approved or confirmed |
| Hallucination risk | 4 | No invented date, no invented compliance sign-off, and it rightly left out the mention of the customer success team, which wasn't a commitment |

## What Worked

It kept the pilot's measured time saving apart from the earlier call's unmeasured estimate, even though the two numbers sound alike.

It wrote the document for Priya as the real reader, in the third person throughout, not addressed to Alex.

It worked out the £4,320 annual figure correctly from the confirmed price per seat and seat count, without adding a new unconfirmed number.

It stated the compliance confirmation as requested and in progress, not already resolved.

It left the QBR date as a clear placeholder rather than guessing a calendar date.

It left the passing comment about a possible customer success team expansion out of the document entirely, rather than turning it into a second commitment.

## What Needed Checking

I should confirm the QBR date with Alex and update the document before it goes to Priya.

Rereading the output against both transcripts, I found three claims they don't support. The Time Commitment section promises a thirty-minute onboarding session per person, and nobody mentions that on either call. The same-day CRM visibility paragraph says the suggested updates were ready on the day of the call, but Alex only said they were "genuinely useful". The pilot section says two changes were measured directly and then lists three, when only the admin time was timed. Those lines should come out before the document goes to Priya, and they sit awkwardly beside the "no invented" notes in the table above.

The compliance confirmation should be chased, and the document updated once it arrives. If it hasn't arrived, the outstanding line stays.

A short tone pass would help the document sound like my own writing rather than a generic business case.

## What I Changed in the Prompt

Nothing in the skill needed changing for this run. One thing is worth watching on future business cases. When a call mentions a possible future expansion (like the customer success team here), it needs the same care every time: left out, not added as a soft extra to the ask.

## Next Test

Run the same two transcripts and skill in ChatGPT, Claude and Gemini, and score each output against the same rubric. Watch in particular whether every model keeps the measured pilot figure and the earlier unmeasured estimate apart, since that's the trap most likely to merge them into one number.
