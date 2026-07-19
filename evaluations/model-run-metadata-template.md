# Model Run Metadata Template

Copy this for each individual run when doing a repeated or cross-model evaluation. The point is just enough detail that someone else could tell what conditions produced this output, without collecting metadata that is not actually available to a normal user (most consumer AI tools do not expose temperature, seed, or exact model checksum).

| Field | Value |
| --- | --- |
| Model | e.g. Claude, ChatGPT, Gemini |
| Model version, if shown | e.g. Claude Sonnet 4.5, GPT-5, Gemini 2.5 Pro |
| Date run | |
| Run number | e.g. 1 of 3 |
| Conversation state | Fresh conversation, or existing project/custom instructions in effect |
| Input given | Link to or copy of the exact prompt/transcript used |
| Any deviation from the standard input | Note anything you had to change to get the model to accept the input (e.g. split into two messages) |

## Notes

- "Fresh conversation" matters more than it looks. A model with your prior context, custom instructions, or an established style already primed will not perform the same as one starting cold. Say which one you tested.
- If a run had to be restarted, reworded, or split up to work at all, that is itself a finding. Record it rather than quietly using the version that worked.
