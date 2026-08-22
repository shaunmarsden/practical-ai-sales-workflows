# Real Blocker Diagnosis Prompt

Copy the prompt below, then add who was expected on the call, who actually attended, each attendee's role where known, what each of them actually said, and anything already confirmed about who holds budget or sign-off authority.

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

- Check that any flagged mismatch is actually supported by something someone said or did, not just plausible-sounding speculation
- Decide yourself whether and how to raise a cross-office, cross-team, or authority question; this proposes what is worth checking, not how to phrase it to the prospect
- Confirm who actually holds sign-off authority before treating a deal as further along than it is
