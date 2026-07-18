# Northstar Business Case Review

This review scores the [worked business case](../examples/northstar-business-case-output.md) against the [sales AI output rubric](sales-ai-output-rubric.md).

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | Names, figures, pricing and roles match both transcripts |
| Evidence fidelity | 5 | The measured pilot figure and the earlier unmeasured estimate are correctly kept distinct |
| Fact separation | 5 | The compliance confirmation is clearly flagged as pending, not delivered |
| Missing information | 5 | The QBR date and the compliance sign-off are both flagged as outstanding |
| Commercial usefulness | 5 | The figure Priya needs to approve is stated plainly, with the calculation shown |
| Next step clarity | 4 | The next step is clear, but exact timing depends on two people neither of whom has confirmed a date yet |
| Tone | 4 | Reads as a proposal for Priya, not a letter to Alex, though Shaun would still want a final pass before it goes out |
| Privacy | 5 | No account executive is named individually, as instructed |
| Approval discipline | 5 | The document is explicitly a draft; nothing is presented as sent, approved or confirmed |
| Hallucination risk | 4 | No invented date, no invented compliance sign-off, and the customer success team mention was correctly left out as a non-commitment |

## What Worked

- The pilot's measured time saving was kept separate from the earlier call's unmeasured estimate, even though both describe a similar-sounding number.
- The document was written for Priya as the actual reader, third person throughout, not addressed to Alex.
- The £4,320 annual figure was calculated correctly from the confirmed per-seat price and seat count, without introducing a new unconfirmed number.
- The compliance confirmation was stated as requested and in progress, not as already resolved.
- The QBR date was left as an explicit placeholder rather than converted into a guessed calendar date.
- The passing comment about a possible customer success team expansion was left out of the document entirely, rather than turned into a second commitment.

## What Needed Checking

- Shaun should confirm the QBR date with Alex and update the document before it goes to Priya.
- The compliance confirmation should be chased and the document updated once it arrives, or the outstanding line kept if it has not.
- A short tone pass would help the document sound exactly like Shaun's own writing rather than a generic business case.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The one thing worth watching on future business cases: a call that mentions a plausible-sounding future expansion (like the customer success team here) needs the same discipline every time, correctly excluded rather than included as a soft addition to the ask.

## Next Test

Run the same two transcripts and skill in ChatGPT, Claude and Gemini, and score each output using the same rubric. Pay particular attention to whether every model keeps the measured pilot figure and the earlier unmeasured estimate distinct, since that is the trap most likely to collapse into one undifferentiated number.
