#!/usr/bin/env python3
"""Repository safety and quality checks.

Runs a set of cheap, deterministic checks that catch the mistakes that are
easy to make in a public repository of this kind: broken links, malformed
skill frontmatter, examples that are not clearly labelled as fictional,
accidental employer or private references, secret-like values, unfinished
placeholder text, a committed private context file, duplicate skill names,
a skill missing any human-review or limitation language, email addresses,
phone numbers, em dashes and smart quotes in reader-facing copy, a scored
evaluation whose headline total disagrees with its own rubric table, and
any term in an optional local, never-committed blocklist
(.github/private-blocklist.txt).

Not covered, and not realistically checkable by a deterministic script: an
unexpected commercial figure. That needs a person who knows what the real
numbers should look like.

These checks confirm structure and hygiene. They do not, and cannot, judge
whether the commercial content is correct. That still needs a person.

Run locally from the repository root:

    python3 .github/scripts/repo_checks.py

Exits 0 if everything passes, 1 if any check fails.
"""

import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install it with: pip install pyyaml")
    sys.exit(2)

failures = []


def tracked_files():
    out = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True, check=True
    ).stdout
    return [f for f in out.splitlines() if f]


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


ALL = tracked_files()
MD = [f for f in ALL if f.endswith(".md")]
# Content scanned for private/secret/placeholder patterns. Exclude the checker
# itself, which necessarily contains the very patterns it searches for.
CONTENT = [f for f in ALL if f.endswith((".md", ".html")) and not f.startswith(".github/")]


def fail(check, path, detail):
    failures.append((check, path, detail))


# 1. Broken relative links in Markdown
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for f in MD:
    base = os.path.dirname(f)
    for i, line in enumerate(read(f).splitlines(), 1):
        for target in LINK.findall(line):
            t = target.strip()
            if t.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path = t.split("#")[0]
            if not path:
                continue
            resolved = os.path.normpath(os.path.join(base, path))
            if not os.path.exists(resolved):
                fail("broken-link", f"{f}:{i}", f"{t} -> {resolved}")


# 2. Skill frontmatter is valid YAML with name and description
for f in ALL:
    if not (f.startswith(".agents/skills/") and f.endswith("SKILL.md")):
        continue
    text = read(f)
    if not text.startswith("---"):
        fail("skill-frontmatter", f, "missing opening --- frontmatter fence")
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("skill-frontmatter", f, "missing closing --- frontmatter fence")
        continue
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        fail("skill-frontmatter", f, f"invalid YAML: {e}")
        continue
    for key in ("name", "description"):
        if not isinstance(meta.get(key), str) or not meta.get(key).strip():
            fail("skill-frontmatter", f, f"missing or empty '{key}'")


# 3. Examples must be clearly labelled as fictional
for f in MD:
    if not f.startswith("examples/"):
        continue
    if not re.search(r"fiction", read(f), re.IGNORECASE):
        fail("example-not-labelled-fictional", f,
             "no 'fictional' label found in the file")


# 4. Employer name and private links do not belong in the public repo
EMPLOYER = re.compile(r"\b(aicore|theaicore|the management academy)\b", re.IGNORECASE)
PRIVATE_LINK = re.compile(
    r"https?://[^\s)]*(?:docs\.google\.com|hubspot\.com|\.sharepoint\.com|"
    r"atlassian\.net|notion\.so)[^\s)]*",
    re.IGNORECASE,
)
# The employer name is otherwise blocked everywhere in this repository (see
# CONTRIBUTING.md's vendor-neutral rule): no workflow, skill, example or
# guide should name it. The one deliberate exception is the README's own
# About Me section, where the real person behind this repository names
# their real employer as part of their own personal bio, not as repository
# content. Matched on the exact line so any future change to that line
# requires a deliberate update here, rather than silently widening what is
# allowed.
EMPLOYER_ALLOWLIST = {
    ("README.md", "I am Shaun Marsden, a solutions consultant at AiCore. "
                  "This project is where I keep track of what I've "
                  "actually found useful, and share it."),
}
PUBLIC_FORM_ALLOWLIST = {
    "https://docs.google.com/forms/d/e/"
    "1FAIpQLSdBC8yOUiylKemlvzrZc2FJ9QD0Pjz592ebPaItAubBRwCUbA/"
    "viewform",
}
for f in CONTENT:
    for i, line in enumerate(read(f).splitlines(), 1):
        stripped = line.strip()
        if EMPLOYER.search(line) and (f, stripped) not in EMPLOYER_ALLOWLIST:
            fail("employer-reference", f"{f}:{i}", line.strip()[:120])
        for match in PRIVATE_LINK.finditer(line):
            private_url = match.group().rstrip(".,;")
            if private_url not in PUBLIC_FORM_ALLOWLIST:
                fail("private-link", f"{f}:{i}", line.strip()[:120])


# 5. Secret-like values
SECRETS = [
    ("openai-key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("github-pat", re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}")),
    ("github-fine-grained-pat", re.compile(r"github_pat_[A-Za-z0-9_]{30,}")),
    ("aws-access-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("google-api-key", re.compile(r"AIza[0-9A-Za-z_\-]{35}")),
    ("slack-token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("private-key-block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("bearer-token", re.compile(r"[Bb]earer\s+[A-Za-z0-9._\-]{20,}")),
]
for f in CONTENT:
    text = read(f)
    for name, pat in SECRETS:
        if pat.search(text):
            fail("secret-like-value", f, f"matched {name} pattern")


# 6. Unfinished placeholder text
PLACEHOLDER = re.compile(r"\b(TODO|FIXME|TKTK|XXX)\b|lorem ipsum", re.IGNORECASE)
for f in CONTENT:
    for i, line in enumerate(read(f).splitlines(), 1):
        if PLACEHOLDER.search(line):
            fail("placeholder-text", f"{f}:{i}", line.strip()[:120])


# 7. Private context files must never be committed, and must stay ignored
PRIVATE_CONTEXT_FILES = ["context/sales-context.md", "context/sales-methodology-overlay.md"]
gitignore = read(".gitignore") if os.path.exists(".gitignore") else ""
for private_file in PRIVATE_CONTEXT_FILES:
    if private_file in ALL:
        fail("committed-private-context", private_file,
             "private context file must never be committed")
    if private_file not in gitignore:
        fail("gitignore-missing-rule", ".gitignore",
             f"{private_file} is not listed in .gitignore")


# 8. Duplicate skill names (a copy-pasted skill folder that was never renamed)
skill_names = {}
for f in ALL:
    if not (f.startswith(".agents/skills/") and f.endswith("SKILL.md")):
        continue
    text = read(f)
    if not text.startswith("---"):
        continue  # already caught by check 2
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        continue
    name = meta.get("name")
    if isinstance(name, str) and name.strip():
        skill_names.setdefault(name.strip(), []).append(f)
for name, files in skill_names.items():
    if len(files) > 1:
        fail("duplicate-skill-name", ", ".join(files),
             f"multiple skills declare name '{name}'")


# 9. A skill missing any human-review, approval or limitation language
HUMAN_REVIEW = re.compile(
    r"human review|human approval|requires? (explicit )?approval|"
    r"stop when the task is unsafe|apply the guardrails",
    re.IGNORECASE,
)
for f in ALL:
    if not (f.startswith(".agents/skills/") and f.endswith("SKILL.md")):
        continue
    if not HUMAN_REVIEW.search(read(f)):
        fail("missing-human-review-language", f,
             "no human review, approval, or limitation language found")


# 10. Email addresses
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
for f in CONTENT:
    for i, line in enumerate(read(f).splitlines(), 1):
        for m in EMAIL.finditer(line):
            fail("email-address", f"{f}:{i}", m.group())


# 11. Phone numbers. A single regex for this is either too loose (catches
# currency figures, scores, dates) or too strict (misses real formats), so
# this finds digit-and-separator candidates first, then filters by total
# digit count and a leading + or 0, which is what actually distinguishes a
# phone number from a figure like "48,000" or a date like "19 July 2026".
PHONE_CANDIDATE = re.compile(r"\+?\(?\d[\d\s().\-]{7,}\d")


def looks_like_phone(candidate):
    digits = re.sub(r"\D", "", candidate)
    if not (9 <= len(digits) <= 15):
        return False
    return candidate.strip().startswith("+") or digits.startswith("0")


for f in CONTENT:
    for i, line in enumerate(read(f).splitlines(), 1):
        for m in PHONE_CANDIDATE.finditer(line):
            if looks_like_phone(m.group()):
                fail("phone-number", f"{f}:{i}", m.group().strip())


# 12. Optional local blocklist. Never committed (listed in .gitignore), so
# this lets a reader flag their own project-specific private terms, a real
# client name, an internal codename, without editing this script or the
# public repository ever containing the term it is flagging.
BLOCKLIST_PATH = ".github/private-blocklist.txt"
if os.path.exists(BLOCKLIST_PATH):
    terms = [
        t.strip() for t in read(BLOCKLIST_PATH).splitlines()
        if t.strip() and not t.strip().startswith("#")
    ]
    for f in CONTENT:
        text = read(f)
        for term in terms:
            if term.lower() in text.lower():
                fail("private-blocklist-term", f,
                     f"matched blocklisted term '{term}'")


# 13. Punctuation that reader-facing copy is not meant to contain.
# guides/writing-style-and-formatting.md states both rules outright ("No em
# dashes. Rewrite using a comma, colon or full stop instead." and "No smart
# quotes or curly apostrophes. Use the straight ASCII forms.") and
# CONTRIBUTING.md extends both to the repository's own prose.
#
# The em dash half exists because it had been fixed by hand in nineteen
# separate commits before any check did it. The smart quote half exists
# because a stated rule with nothing enforcing it is exactly how the em dash
# kept coming back; six were removed by hand shortly before the rule was
# written down, and word processors reintroduce them silently on paste.
#
# En dashes are still not checked, because no rule here mentions them.
# Characters are referred to by escape rather than literal so this file never
# flags itself, and .github/ is outside CONTENT in any case.
#
# If a fictional example ever needs to quote a model output that genuinely
# contained one of these, that is a real false positive: put it in a fenced
# code block and exclude the path here.
BANNED_PUNCTUATION = {
    "\u2014": ("em-dash", "replace with a comma, colon or full stop"),
    "\u201c": ("smart-quote", "replace with a straight double quote"),
    "\u201d": ("smart-quote", "replace with a straight double quote"),
    "\u2018": ("smart-quote", "replace with a straight single quote"),
    "\u2019": ("smart-quote", "replace with a straight apostrophe"),
}
for f in CONTENT:
    for i, line in enumerate(read(f).splitlines(), 1):
        for character, (label, remedy) in BANNED_PUNCTUATION.items():
            if character in line:
                fail(label, f"{f}:{i}",
                     f"{remedy} (guides/writing-style-and-formatting.md)")


# 14. A scored evaluation's headline total must match its own rubric table.
# Five evaluations disagreed with their own tables before this check existed,
# by one or two points each, and the error survived for months because nobody
# re-adds a column of ten numbers when the table above it looks reasonable.
#
# Each "Score: N out of M" line is paired with the table that follows it, so a
# file holding more than one scored run is checked run by run rather than as a
# whole. A table is only checked when it is fully itemised, meaning its row
# count times five equals the stated maximum. A deliberately summarised table,
# for example one row reading "Every other area | 4 or 5", cannot be added up
# and is skipped rather than guessed at; hartwell-opportunity-handover-review.md
# has one of each and only its itemised run is checked.
SCORE_LINE = re.compile(r"^\*\*Score:\s*(\d+)\s+out of\s+(\d+)", re.M)
RUBRIC_ROW = re.compile(r"^\|\s*([A-Za-z][^|]*?)\s*\|\s*(\d+)\s*\|", re.M)
for f in CONTENT:
    text = read(f)
    marks = list(SCORE_LINE.finditer(text))
    for i, mark in enumerate(marks):
        stated, maximum = int(mark.group(1)), int(mark.group(2))
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        rows = RUBRIC_ROW.findall(text[mark.end():end])
        if len(rows) * 5 != maximum:
            continue
        total = sum(int(value) for _, value in rows)
        if total != stated:
            line = text[:mark.start()].count("\n") + 1
            fail("score-total", f"{f}:{line}",
                 f"table sums to {total} but the line states {stated} "
                 f"out of {maximum}")


# 15. Every skill must be reachable from the library guide.
#
# The guide is the plain-English page a new reader is sent to first, and it says
# "Open any skill below" as though its list were complete. It stopped being
# maintained: four skills existed for weeks with their own workflow and recipe
# card while appearing nowhere on it. Each was reachable elsewhere, so nothing
# looked broken from any single page.
LIBRARY_GUIDE = "guides/what-is-a-sales-ai-skill.md"
if os.path.isdir(".agents/skills") and os.path.exists(LIBRARY_GUIDE):
    guide = read(LIBRARY_GUIDE)
    for skill in sorted(os.listdir(".agents/skills")):
        if not os.path.isfile(f".agents/skills/{skill}/SKILL.md"):
            continue
        if f"skills/{skill}/SKILL.md" not in guide:
            fail("skill-not-in-library", LIBRARY_GUIDE,
                 f"{skill} exists but is not linked from the skills library")


# 16. The portable router prompt must offer the same routes as the router skill.
#
# The prompt is advertised as doing the same job as the skill, pasted straight
# into a chat tool. It drifted to fifteen routes while the skill had seventeen,
# so anyone using the portable version could not be routed to two workflows
# that exist. Nothing pointed the two files at each other.
ROUTER_SKILL = ".agents/skills/workflow-router/SKILL.md"
ROUTER_PROMPT = "templates/workflow-router-prompt.md"
if os.path.exists(ROUTER_SKILL) and os.path.exists(ROUTER_PROMPT):
    skill_routes = set(re.findall(
        r"^\|[^|]+\|\s*\[([^\]]+)\]\([^)]+\)\s*\|$", read(ROUTER_SKILL), re.M))
    prompt_routes = set(re.findall(r"^- ([^:]+):", read(ROUTER_PROMPT), re.M))
    if skill_routes and prompt_routes:
        for missing in sorted(skill_routes - prompt_routes):
            fail("router-drift", ROUTER_PROMPT,
                 f"the router skill offers '{missing}' but this prompt does not")
        for extra in sorted(prompt_routes - skill_routes):
            fail("router-drift", ROUTER_PROMPT,
                 f"this prompt offers '{extra}' but the router skill does not")


# 17. Every recipe card must be reachable from at least one role route.
#
# The role guide claims to group "the same seventeen jobs" by which come up in
# each seat. It reached sixteen: one card appeared under no role at all, so the
# claim was false while the number in it was still right.
ROLE_GUIDE = "guides/role-based-routes.md"
if os.path.isdir("recipes") and os.path.exists(ROLE_GUIDE):
    roles = read(ROLE_GUIDE)
    for card in sorted(os.listdir("recipes")):
        if not card.endswith(".md") or card == "README.md":
            continue
        if f"recipes/{card}" not in roles:
            fail("card-not-in-any-role", ROLE_GUIDE,
                 f"recipes/{card} is reachable from no role route")


# 18. A stated count of skills, workflows or recipe cards must be the real one.
#
# One guide opened with "Eleven skills, sixteen workflows" when it was seventeen
# and fifteen, and built its whole argument on the wrong figure. Another opened
# with "Seventeen workflows" and said "fifteen" twice further down the same
# page. Prose counts go stale the moment anything is added, and nobody recounts
# a directory to check a sentence.
NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20,
}


def _count_dir(path, predicate):
    return sum(1 for e in os.listdir(path) if predicate(e)) if os.path.isdir(path) else None


_SKILLS = _count_dir(".agents/skills",
                     lambda e: os.path.isfile(f".agents/skills/{e}/SKILL.md"))
_WORKFLOWS = _count_dir("workflows",
                        lambda e: e.endswith(".md") and e != "README.md")
_RECIPES = _count_dir("recipes",
                      lambda e: e.endswith(".md") and e != "README.md")
# "jobs" and "cards" are the reader-facing words for a recipe card, and are
# counted the same way. One card is one sales job, which is also one row of the
# evidence matrix.
ACTUAL = {
    "skills": _SKILLS,
    "workflows": _WORKFLOWS,
    "recipe cards": _RECIPES,
    "cards": _RECIPES,
    "jobs": _RECIPES,
    "sales jobs": _RECIPES,
}
# Only a number of ten or more is treated as a total. Below that the same
# words are doing a different job: "two workflows sound similar", "two skills
# in sequence" mean a pair, not a count of everything here. That leaves a
# genuine total under ten unchecked, which is the right trade while this
# repository has seventeen of one and fifteen of the other.
COUNT_FLOOR = 10
COUNT_CLAIM = re.compile(
    r"\b(%s)\s+(recipe cards|sales jobs|skills|workflows|cards|jobs)\b"
    % "|".join(w for w, n in NUMBER_WORDS.items() if n >= COUNT_FLOOR),
    re.I)
for f in CONTENT:
    # The changelog records what was true when each entry was written, so its
    # counts are history rather than claims about the repository now.
    if f == "CHANGELOG.md":
        continue
    for i, line in enumerate(read(f).splitlines(), 1):
        for word, noun in COUNT_CLAIM.findall(line):
            actual = ACTUAL.get(noun.lower())
            stated = NUMBER_WORDS[word.lower()]
            if actual is not None and stated != actual:
                fail("stale-count", f"{f}:{i}",
                     f"says {word.lower()} {noun.lower()}, but there are {actual}")


# 19. A job the evidence matrix shows as untested must be named in the roadmap.
#
# The roadmap says "The current gaps are simple" and then lists them, so it is
# making a claim about being complete. It said one job lacked a logged
# real-work test when the matrix showed two: the sentence was written on 6
# August and Spot the Real Blocker arrived on 22 August, so the roadmap
# understated its own gap list for four weeks. The matrix is the source of
# truth; this only checks the roadmap has not fallen behind it.
MATRIX, ROADMAP = "EVIDENCE-STATUS.md", "ROADMAP.md"
if os.path.exists(MATRIX) and os.path.exists(ROADMAP):
    roadmap = read(ROADMAP)
    for line in read(MATRIX).splitlines():
        if not line.startswith("| ["):
            continue
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not cells[4].startswith("Not yet"):
            continue
        job = re.match(r"\[([^\]]+)\]", cells[0])
        if job and job.group(1) not in roadmap:
            fail("roadmap-gap-missing", ROADMAP,
                 f"'{job.group(1)}' has no logged real use in {MATRIX} "
                 f"but is not named here")


# 20. The changelog's real-use count must match the evidence matrix.
#
# The matrix marks a job "Test logged" in its real-use column; the changelog
# states how many jobs have one. Those two numbers drifted apart: the changelog
# said twelve while the matrix marked fourteen, because two jobs have their
# finding in a dedicated file rather than in the changelog summary, and nobody
# re-counted. The repository was understating its own evidence.
MATRIX_FILE, CHANGELOG_FILE = "EVIDENCE-STATUS.md", "CHANGELOG.md"
if os.path.exists(MATRIX_FILE) and os.path.exists(CHANGELOG_FILE):
    logged = len(re.findall(r"^\|.*\|\s*\[Test logged\]\([^)]+\)\s*\|",
                            read(MATRIX_FILE), re.M))
    claim = re.search(r"\b(%s)\s+jobs have a logged finding"
                      % "|".join(NUMBER_WORDS), read(CHANGELOG_FILE), re.I)
    if logged and claim:
        stated = NUMBER_WORDS[claim.group(1).lower()]
        if stated != logged:
            fail("real-use-count", CHANGELOG_FILE,
                 f"says {claim.group(1).lower()} jobs have a logged finding, "
                 f"but {MATRIX_FILE} marks {logged} as Test logged")


# Report
if failures:
    print(f"Repository checks failed ({len(failures)} issue(s)):\n")
    for check, path, detail in failures:
        print(f"  [{check}] {path}")
        print(f"      {detail}")
    print("\nFix the issues above, or adjust the check in "
          ".github/scripts/repo_checks.py if it is a false positive.")
    sys.exit(1)

print(f"All repository checks passed ({len(MD)} Markdown files scanned).")
sys.exit(0)
