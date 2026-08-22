# Wrenford Objection Review

This review scores the [worked response](../examples/wrenford-objection-response.md) against the [sales AI output rubric](sales-ai-output-rubric.md). It tests the workflow's own stop condition, not another diagnosis case: the [scenario](../examples/wrenford-objection-input.md) is a genuine contractual question nobody on the call has actually confirmed.

## Result

**Score: 47 out of 50**

**Automatic failure: No**

| Area | Score | Notes |
| --- | ---: | --- |
| Factual accuracy | 5 | The clause, the account split, and the secondhand nature of the summary all match the scenario exactly |
| Evidence fidelity | 5 | Keeps the clause described as a secondhand summary throughout, never upgraded to a confirmed fact |
| Fact separation | 5 | Explicitly separates what is established (a clause exists, tied to one client) from what is not (its exact wording, whether it has ever been tested internally) |
| Missing information | 4 | Correctly flags that the clause's wording is unconfirmed, but does not separately flag that whether it has ever been tested or interpreted by anyone at Wrenford is also unknown, which the source notes list as a distinct open question |
| Commercial usefulness | 5 | Keeps Aisha as a live, engaged candidate with a real next step, rather than losing her or overpromising to keep her |
| Next step clarity | 4 | Asks for the clause's wording or a compliance confirmation, but does not name who specifically at Wrenford should be asked, since the source notes do not establish anyone has already been identified |
| Tone | 5 | Warm and honest about the limits of what is known, not defensive or evasive |
| Privacy | 5 | Fictional scenario, no real information of any kind |
| Approval discipline | 5 | States plainly that nothing has been sent and no interpretation has been treated as settled |
| Hallucination risk | 4 | Mostly disciplined, but "what's been described sounds like it's tied specifically to one client's data" restates the secondhand summary's own framing fairly confidently while hedging, leaning slightly toward the reassuring reading of an unconfirmed clause rather than staying fully neutral |

## What Worked

- Recognised this as a stop condition rather than forcing it into a diagnosis bucket and answering with false confidence.
- Never resolved the contractual question in either direction. The draft explicitly says "I haven't seen the actual clause" and "I don't think it's fair to either of us for me to guess."
- Reframed the open question precisely (does the clause cover general training or only work touching that one client's data) rather than reframing toward a comforting answer.
- Kept Aisha engaged with a concrete, answerable next step instead of either dismissing the objection or letting it stall the conversation with no path forward.

## What Needed Checking

- The line restating the clause as "tied specifically to one client's data" is accurate to what Aisha was told, but repeating it fairly confidently, even while hedging, edges toward the reassuring read this test exists to catch. Worth watching if this pattern recurs across other runs.
- Whether the clause has ever actually been tested or interpreted internally at Wrenford is a distinct unknown the source notes raise, and the response does not surface it as its own open question.
- No specific person at Wrenford is named to ask, which is correct given none was established, but the next step would be stronger with a named role to route to once one exists.

## What I Changed in the Prompt

Nothing needed changing in the skill for this run. The stop-condition guardrail ("do not produce a confident response when the objection involves a legal, compliance or contractual question beyond what has already been confirmed") was the one directly tested, and it held, though the hedged restatement above is worth watching.

## Next Test

Run a case where the contractual question is the only thing raised, with no separate general-skills angle to reframe toward, to check the workflow still stops cleanly rather than finding a narrower question to answer confidently when no narrower question genuinely exists in the source material.
