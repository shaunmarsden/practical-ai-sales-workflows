# Output Contract: Opportunity Handover

This contract defines the strict boundaries for this skill. The AI must adhere to these rules without exception.

## What the AI MUST Do

- **Confirm the recipient and the reason for the handover** before producing anything. A handover written for nobody in particular tends to drift into generic content.
- **Record the date or relative position of every important source.** A handover's whole purpose is showing the newest reliable position, not the most complete-sounding one.
- **Show a material disagreement between sources rather than picking one silently.** A CRM stage that reads further along than the emails support is exactly the kind of thing a handover exists to surface.
- **Keep confirmed, estimate, inference, unknown and conflicting labels distinct throughout**, not folded into one confident narrative.
- **Report any change in the receiving contact or customer-side owner explicitly**, rather than quietly updating a name in the background.
- **Give every action one accountable internal owner.** Even where the party who must act is external, uncertain, or not yet assigned, name the internal person responsible for chasing it. "The customer," "unassigned," or a list of several names is not an owner.
- **Build a person reference ledger before drafting.** For every named person, record their exact name, confirmed role, whether pronouns are explicitly supplied by the evidence, and the permitted reference form. Do not include this ledger in the finished output unless a failure could not be resolved.
- **Run a full reference audit before presenting the handover.** Scan the complete draft for he, him, his, himself, she, her, hers, herself, they, them, their, theirs, themselves, Mr, Mrs, Ms, and any other unsupported personal characteristic. Outside a direct source quotation, replace every one of these that refers to a named individual with that person's exact name or confirmed role.
- **Refuse to present the handover as complete if the audit finds an unresolved unsupported personal reference.** State that the reference audit failed and name the exact line that needs a person to fix, rather than publishing it anyway.

## What the AI MUST NOT Do

- **No invented customer intent, urgency, authority, budget, dates or commitments.** If it was not actually given, it does not appear as though it was.
- **No qualified opportunity while a material condition is open.** Budget, authority, timeline or procurement left unresolved means the opportunity is not described as qualified.
- **No internal suggestion presented as a customer agreement.** An idea this skill generates, or one the seller raised internally, stays labelled as a suggestion until the customer has actually agreed to it.
- **No silent choice between conflicting sources.** When material sources disagree, the disagreement is shown, not resolved by picking whichever version is more convenient.
- **No possible project upgraded to an agreed delivery plan.** A discussed idea stays provisional until the receiving person and the customer have both actually accepted it.
- **No eligibility, compliance or policy decision.** This skill prepares a handover; it does not decide whether a customer qualifies for anything.
- **No irrelevant personal or sensitive information.** Include only what the receiving person genuinely needs for continuity.
- **No claim that a link was opened when only its address was supplied.** Say the source was named, not that its contents were checked.
- **No sending a message, drafting inside an email system, updating a CRM, changing ownership, or creating tasks or calendar events.** Every one of these stays a proposed next action for a person to carry out.
- **No external action described as completed without evidence.** A proposed action stays proposed unless something in the supplied evidence actually confirms it happened.
- **No third-person personal pronoun for a named individual anywhere in the finished handover**, outside a direct quotation. Use the person's exact name or confirmed role instead, every time, even where it repeats.
- **No honorific** (Mr, Mrs, Ms or similar) **unless the evidence explicitly supplies one and it is genuinely needed.**
- **No inferred gender, seniority, nationality, location, age or relationship** from a name, a role, or the surrounding text, and no transferring one person's stated attribute to a different person.
