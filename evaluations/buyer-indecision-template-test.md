# Does a Pasted Skill Lose Its Template? A Twelve-Run Test

The [identify-buyer-indecision skill](../.agents/skills/identify-buyer-indecision/SKILL.md) told the AI to use an output template, and linked to it by a relative path. When you paste `SKILL.md` into a chat, as the README says to, that link doesn't open. I wanted to know what that costs. It costs the structure. None of 6 replies to the linked version used the template's four sections and eleven fields. With the template written into the file, all 6 did, and the classification, the boundaries and the quotes held. I made that change. I'd found the same thing in [another repo of mine](https://github.com/shaunmarsden/evidence-labelled-meeting-notes/blob/main/evaluations/template-in-skill-test.md) the same day, and wanted to see whether it was specific to that skill.

## What I Tested

I gave an AI the skill text, then one deal, and asked it to analyse it. The task line was the same every time: "Here is a late-stage deal I need help with. The company and the people are fictional. Please analyse it." I tested two versions of the skill:

- **Linked.** `SKILL.md` as it was, with the template linked by a relative path.
- **Written in.** The same, with the existing template written out where the link was. Nothing else changed.

In both I removed the last paragraph, which points to the worked examples and scored tests, so a reply couldn't take a hint from it. The shipped file keeps it. The output contract and checklist links stayed relative in both versions, so those weren't tested.

Three deals, each with a larger and a smaller model:

- **Wrenmoor Analytics**, from [the Wrenmoor example](../examples/wrenmoor-indecision-input.md). I used everything above its "re-running" line, and took out the paragraph that explains the pattern.
- **Apex Logistics**, from [the fictional example](../.agents/skills/identify-buyer-indecision/references/fictional-example.md). I used its context and evidence, and took out its expected diagnosis and the line that says it was made to test the skill.
- **Harrowgate Veterinary Group**, a new deal I wrote for this test:

```text
# Harrowgate Veterinary Group

This scenario is entirely fictional. Harrowgate Veterinary Group, Bertram Oakes, Mirela Coste and every date and figure are invented.

## Context

- **Account:** Harrowgate Veterinary Group (fictional)
- **Stage:** Negotiation / Pending Signature
- **Stakeholders:** Bertram Oakes (Operations Director, champion and economic buyer), Mirela Coste (IT Security Lead)

## What Has Actually Happened

- Bertram has been positive throughout. After the demo he said: "This is exactly what the practices have been asking for."
- Price and terms were agreed on the last call. Bertram: "Pricing works. Send me the order form when you're ready."
- The order form went out nine days ago. It has not come back.

## Bertram's Most Recent Message

> "Sorry for the slow reply. I'm ready to sign, but Mirela has to review our data handling document before anything goes out under my name. She's got your security report already and told me she has everything she needs. Her review is booked in for Tuesday 12 November. I'll send the order form back the moment she's done."
```

> **Re-running this yourself?** Copy everything above this line and stop here. The section below says what each reply was scored on, so including it turns the test into an open-book exam and the result will look better than it should.

## What I Decided in Advance

I wrote four pass-or-fail measures before any run, and scored each reply by reading it.

1. **Shape.** The reply has all four numbered sections of the template (Evidence Extracted, Diagnosis, Inferences and Unknowns, Recommended Next Steps) and all eleven fields in them (Stated Position, Direct Quotes, Context, Primary Classification, Underlying Fear or Risk, Confidence Level, Inferences, Missing Evidence, Do Not Do, Suggested Approach, Questions to Ask), allowing small wording changes.
2. **Classification.** A single choice from the template's list that matches my key. For Wrenmoor, Genuine Indecision. For Harrowgate, Approval Dependency. For Apex, which the repo calls deliberately ambiguous, either Genuine Indecision or Standard Objection, but only if the reply names the other reading.
3. **Boundaries.** No discount, extension, guarantee or deadline suggested, no drafted customer email, no invented date, owner or commitment, and no mind-reading beyond the evidence.
4. **Quotes.** Everything under Direct Quotes appears in the deal, and inferences are labelled as inferences.

I'd change the skill only if the written-in version passed measure 1 in at least 5 of 6 replies and at least 3 more than the linked version, and each of measures 2 to 4 in at least 5 of 6, with none more than one lower than the linked version. I added no runs.

## Method

Twelve runs on 20 October 2026 in fresh conversations, on settings that report themselves as `claude-opus-5-5` and `claude-haiku-5-5`. Both names are self-reported. Each run read its input from a file and wrote its reply to another. I scored by reading, and I could usually tell which version a reply came from.

## Result

| Passes, of 6 | Linked | Template written in |
| --- | ---: | ---: |
| 1. Shape | 0 | 6 |
| 2. Classification | 6 | 5 |
| 3. Boundaries | 6 | 6 |
| 4. Quotes | 6 | 6 |
| Mean words a reply | 755 | 762 |

The written-in version met the line I'd set, so I made the change.

## What the Result Shows

**A pasted skill can't use a link.** Four of the 6 replies to the linked version said the skill's linked files weren't included or that they hadn't opened them. The other 2 built their own layout without comment. The layouts were sensible. They ran from "What the facts say" to "Verdict", and none was the template's.

**Writing the template in worked with both models.** The larger and smaller model each used the template on all three deals.

**The diagnosis didn't depend on the template.** Wrenmoor was Genuine Indecision in all 4 replies, and Harrowgate was Approval Dependency in all 4. The linked version got there as well as the written-in one. What the template changed was the format of the answer.

**Four of the 6 replies to the written-in version still said the output contract and checklist weren't included.** Those links are unchanged.

**The one lower score.** On Apex, all 4 replies called it a standard objection and not indecision. Three named the other reading, such as fear of being locked in for two years, or a pattern of vague delays that would change the diagnosis. One smaller-model reply to the written-in version didn't, so it failed measure 2.

## What Went Wrong, and What I Can't Tell

- **I got a date wrong.** I wrote "Tuesday 12 November" without checking a calendar. All 4 Harrowgate replies noticed it isn't a Tuesday in 2026, using the year from their setting, which the deal doesn't give. The note was useful and didn't change a score. I left the scenario as I tested it.
- **Apex is a judgement.** Whether a reply "names the other reading" is mine to call, and the repo's own key says either label is defensible.
- **One reply made up an organisation.** A smaller-model reply to the written-in version said a "deal desk" must approve any pilot. Nothing in the deal mentions one. It's a small slip and offered no concession, so I didn't fail it.
- **I haven't tested a run from a folder,** where the AI can open the linked file. This only shows what happens when the file is pasted.
- **Six runs a version, three deals, one skill.** I wrote one of the three deals, and took pattern-naming lines out of the other two, so they aren't the published inputs. I scored by reading and could usually tell the arms apart. The replies came from two model settings, run inside a coding tool with my project notes.
- **The template is now in two places,** `SKILL.md` and `templates/output-template.md`. If I change one I change the other.

## What I'd Do Next

I haven't made this change to any other skill. [Progressive disclosure](../guides/progressive-disclosure.md) says templates belong in separate files, and I'd be giving that up skill by skill. Each skill that links its template would need its own test first.
