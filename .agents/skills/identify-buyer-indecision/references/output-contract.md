# Output Contract: Identify Buyer Indecision

This contract defines the strict boundaries for this skill. The AI must adhere to these rules without exception.

## What the AI MUST Do

- **Quote directly.** Base all diagnoses on direct quotes or clear paraphrases from the provided evidence.
- **Label unknowns.** If the evidence is insufficient to diagnose the root cause of the delay, explicitly state: "Insufficient evidence to diagnose."
- **Categorise strictly.** Map the buyer's behaviour to one of the predefined states (Indecision, Objection, Timing, Soft No, Disqualification).

## What the AI MUST NOT Do

- **No External Actions.** The AI cannot draft emails, update the CRM, or schedule meetings. It only provides analysis.
- **No Commercial Concessions.** The AI must not suggest giving a discount, extending a pilot, or altering the contract to win the deal.
- **No Mind-Reading.** The AI must not assume a stakeholder's internal motivations without explicit evidence in the text.
- **No False Optimism.** If the evidence points to a "Soft No" or "Disqualification," the AI must state this clearly. It must not argue with the evidence.
