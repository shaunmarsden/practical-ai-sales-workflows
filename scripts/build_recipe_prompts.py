#!/usr/bin/env python3
"""Put each recipe card's prompt on the card itself.

Every card used to say "everything you need is here" and then send the reader
to another file for the one thing they actually needed, the prompt. This copies
the canonical prompt into the card so the sentence is true.

The prompt has one home per job, listed in SOURCES below. This script copies
from that home into the card between two HTML comment markers, so nobody edits
a card's prompt by hand and no card can quietly disagree with the prompt the
repository publishes. Check 24 in .github/scripts/repo_checks.py enforces that,
reading the source path out of the marker itself.

Two cards are deliberately absent from SOURCES. Build a Business Case and
Chase a Quiet Prospect have no standalone prompt anywhere in the repository,
only a skill, so there is nothing to inline for them yet and their opening
line says so instead of claiming otherwise.

Run from the repository root:

    python3 scripts/build_recipe_prompts.py

It is idempotent. Exits 1 if a source or a marker pair is missing.
"""

import os
import re
import sys

# card -> the file that holds the canonical prompt for that job
SOURCES = {
    "brief-your-champion": "templates/champion-enablement-prompt.md",
    "check-whether-it-actually-fits": "templates/fit-and-limitations-review-prompt.md",
    "find-the-next-prospect": "templates/outbound-prospecting-prompt.md",
    "follow-up-after-a-sales-call": "templates/post-call-follow-up-prompt.md",
    "get-a-weekly-view": "templates/weekly-operating-review-prompt.md",
    "hand-over-an-opportunity": "templates/opportunity-handover-prompt.md",
    "handle-an-objection": "templates/objection-handling-prompt.md",
    "keep-your-crm-honest": "templates/crm-hygiene-review-prompt.md",
    "move-a-stalled-decision": "templates/buyer-indecision-prompt.md",
    # The only prompt that does not live in templates/. It sits in the
    # workflow, and moving it would change a page nobody asked me to change.
    "prepare-for-a-sales-call": "workflows/01-pre-call-preparation.md",
    "review-a-lost-opportunity": "templates/lost-opportunity-review-prompt.md",
    "review-an-outbound-campaign": "templates/outbound-campaign-learning-review-prompt.md",
    "review-your-pipeline": "templates/pipeline-evidence-review-prompt.md",
    "spot-a-real-objection-pattern": "templates/objection-pattern-review-prompt.md",
    "spot-the-real-blocker": "templates/real-blocker-diagnosis-prompt.md",
}

# Pre-call prep is the one job whose prompt tells the reader to fill in a
# separate template, so inlining only the prompt would leave that card still
# needing another file open. Its template goes on the card too.
EXTRAS = {
    "prepare-for-a-sales-call": (
        "templates/pre-call-card.md",
        "## And the card it fills in",
        "Paste this underneath the prompt, then your own research below that.",
    ),
}

HEADING = "## Paste this into your AI tool"
FOOTER = ("Then paste your own notes underneath it. Everything the prompt "
          "needs is listed under **You need** above.")
# The default footer says notes come next, which is wrong on the one card
# where a template goes in between.
FOOTERS = {
    "prepare-for-a-sales-call": (
        "This prompt refers to a card template, which is the next block, so "
        "paste that in too."),
}
# The outer pair wraps everything this script generates, so a rebuild replaces
# exactly its own output and cannot eat a hand-written section next to it. The
# inner pair names the file each block was copied from, which is what check 24
# reads.
REGION_BEGIN = "<!-- prompts:begin -->"
REGION_END = "<!-- prompts:end -->"
BEGIN = "<!-- prompt:begin source={source} -->"
END = "<!-- prompt:end -->"
FENCE = re.compile(r"^```text\n(.*?)^```$", re.M | re.S)


def canonical_prompt(path):
    """The pasteable text a source file publishes, or None.

    A prompt file wraps it in a text fence. A template like the pre-call card
    is the whole document below its title, because the structure is the thing
    being pasted. Check 24 imports this function rather than reimplementing
    it, so the build and the check cannot disagree about what a card holds.
    """
    text = open(path, encoding="utf-8").read()
    match = FENCE.search(text)
    if match:
        return match.group(1)
    if text.lstrip().startswith("# "):
        body = text.split("\n", 1)[1] if "\n" in text else ""
        return body.strip("\n") or None
    return None


def one_block(source, prompt, heading, footer):
    return "\n".join([
        heading, "",
        BEGIN.format(source=source),
        "```text",
        prompt.rstrip(),
        "```",
        END, "",
        footer,
    ])


def region(card):
    blocks = [one_block(SOURCES[card], canonical_prompt(SOURCES[card]),
                        HEADING, FOOTERS.get(card, FOOTER))]
    if card in EXTRAS:
        source, heading, footer = EXTRAS[card]
        blocks.append(one_block(source, canonical_prompt(source),
                                heading, footer))
    return "\n".join([REGION_BEGIN, ""] + ["\n\n".join(blocks)] + ["", REGION_END])


def main():
    if not os.path.isdir("recipes"):
        sys.exit("run this from the repository root")

    problems = []
    for card, source in sorted(SOURCES.items()):
        if not os.path.exists(f"recipes/{card}.md"):
            problems.append(f"recipes/{card}.md does not exist")
        for src in [source] + ([EXTRAS[card][0]] if card in EXTRAS else []):
            if not os.path.exists(src):
                problems.append(f"{card}: source {src} does not exist")
            elif canonical_prompt(src) is None:
                problems.append(f"{card}: no pasteable text found in {src}")
    for card in EXTRAS:
        if card not in SOURCES:
            problems.append(f"{card}: has an extra block but no prompt source")
    if problems:
        for p in problems:
            print("FAIL", p)
        sys.exit(1)

    for card, source in sorted(SOURCES.items()):
        path = f"recipes/{card}.md"
        text = open(path, encoding="utf-8").read()
        fresh = region(card)

        if REGION_BEGIN in text and REGION_END in text:
            head, rest = text.split(REGION_BEGIN, 1)
            tail = rest.split(REGION_END, 1)[1]
            text = head + fresh + tail
        else:
            if "## Open" not in text:
                print("FAIL", f"{card}: no '## Open' section to insert before")
                sys.exit(1)
            text = text.replace("## Open", fresh + "\n\n## Open", 1)

        open(path, "w", encoding="utf-8").write(text)
        extra = f" + {EXTRAS[card][0]}" if card in EXTRAS else ""
        print(f"  {card:34s} <- {source}{extra}")

    print(f"inlined {len(SOURCES)} prompts, {len(EXTRAS)} extra block(s)")


if __name__ == "__main__":
    main()
