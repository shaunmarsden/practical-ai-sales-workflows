# Real Blocker Diagnosis Prompt

Copy the prompt below, then add who was expected on the call, who turned up, each attendee's role where known, what each of them said, and anything already confirmed about who holds budget or sign-off authority.

```text
Act as a careful sales call diagnostician.

Use only the information I provide. Do not invent a hidden motive, a reason, or a decision-maker that I have not actually described.

Produce the following sections:

1. Who was actually on the call
Compare who was expected with who actually attended. Name any unplanned or last-minute attendee explicitly.

2. Role against stated concern
For each attendee, compare their role or title against what they actually said. Flag any mismatch plainly. If someone's stated concern shifted partway through, say what changed and which concern stayed open.

3. Stated reason versus checkable fact
For each concern raised, state it exactly as given, then note separately what would actually resolve it. Do not guess at an underlying motive with nothing behind it.

4. Who actually decides
Do not treat enthusiasm or being the point of contact as confirmation of authority. If nobody has explicitly confirmed holding budget or sign-off authority, say so, and name anyone else who was mentioned as a further approver, without assuming they are definitely the real blocker.

5. Recommended next step
Name the specific next question or person to identify, not a generic follow-up.

Rules:
- Do not assert a hidden motive the evidence does not support; flag the mismatch, do not invent the explanation for it
- Do not treat a plausible-sounding answer as proof an objection is fully resolved if the underlying authority or motive question was never tested
- Do not contact anyone not already on the thread; recommend the next question, do not draft it as if sending it
```

## Before You Use the Output

- Check that any mismatch it flags rests on something someone said or did, not plausible-sounding guesswork
- Decide yourself whether and how to raise a question about another office, another team or someone's authority. This suggests what to check, not how to put it to the prospect
- Confirm who holds sign-off authority before you treat a deal as further along than it is
