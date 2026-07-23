#!/usr/bin/env python3
"""Repository safety and quality checks.

Runs a set of cheap, deterministic checks that catch the mistakes that are
easy to make in a public repository of this kind: broken links, malformed
skill frontmatter, examples that are not clearly labelled as fictional,
accidental employer or private references, secret-like values, unfinished
placeholder text, a committed private context file, duplicate skill names,
a skill missing any human-review or limitation language, email addresses,
phone numbers, and any term in an optional local, never-committed
blocklist (.github/private-blocklist.txt).

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
    r"https?://[^\s)]*(docs\.google\.com|hubspot\.com|\.sharepoint\.com|"
    r"atlassian\.net|notion\.so)",
    re.IGNORECASE,
)
for f in CONTENT:
    for i, line in enumerate(read(f).splitlines(), 1):
        if EMPLOYER.search(line):
            fail("employer-reference", f"{f}:{i}", line.strip()[:120])
        if PRIVATE_LINK.search(line):
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
