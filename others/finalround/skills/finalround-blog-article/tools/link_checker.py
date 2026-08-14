#!/usr/bin/env python3
"""FinalRound link checker (G2/G6 + F red lines, context-aware).

Checks:
  - Internal links resolve to allowed path prefixes (G6).
  - Forbidden paths (e.g. /zh) are not linked.
  - F1 red-line phrases: free-trial *promotions* absent. FAQ-style clarifications
    like "Is there a free trial? No." are ALLOWED (context-aware).
  - F2 old-product words: only FAIL when used as *current features*; references to
    retired items ("The old Scan Code button is retired") are ALLOWED.
  - F4 internal-decision phrases absent.
  - F5 "undetectable" not used as a standalone primary claim (warns on any occurrence).
  - F6 conversion paths (/download /subscription /getting-started /try /special-discount)
    NOT linked in body copy (buttons only, 2026-08-11 decision).

Usage:
    python tools/link_checker.py ../../blog/NN-{slug}.md [--forbidden /zh] [--check-live]
Exit code 0 = PASS (warnings allowed), 1 = FAIL.
"""
import argparse
import re
import sys
import urllib.request

ALLOWED_PREFIXES = [
    "/blog/",
    "/interview-copilot",
    "/ai-mock-interview",
    "/general-interview",
    "/coding-copilot",
    "/phone-interview",
    "/hirevue",
    "/ai-resume-builder",
    "/ai-job-hunter",
    "/auto-apply",
    "/cover-letter-generator",
    "/linkedin-profile-optimizer",
    "/linkedin-resume-builder",
    "/resume-checker",
    "/career-coach",
    "/recruiters-hotline",
    "/salary-to-hourly-calculator",
    "/qa-pairs",
    "/interview-notes",
    "/use-cases/",
    "/compare/",
    "/interview-prep",
    "/interview-questions",
    "/glossary",
    "/community/",
    "/tech-layoffs",
    "/",
]

# Conversion paths — forbidden in body copy (2026-08-11 decision); carried by buttons
CONVERSION_PREFIXES = [
    "/download",
    "/subscription",
    "/getting-started",
    "/try",
    "/special-discount",
]

# F1: promotional free-trial phrases (promotions only; clarifications exempted)
F1_PROMOTIONS = [
    r"try\s+(it\s+)?free",
    r"start\s+(your\s+)?free\s+trial",
    r"free\s+live\s+interview",
    r"try\s+copilot\s+free",
    r"sign\s+up\s+for\s+free",
    r"get\s+.*?free\s+trial",
]
# "free trial" in a clarification/negation context is allowed
F1_NEGATION = re.compile(
    r"(no\s+free\s+trial|without\s+.*?free\s+trial|is\s+there\s+[^?]{0,30}\?|"
    r"not\s+.*?free\s+trial|there's\s+no\s+free\s+trial|there\s+is\s+no\s+free\s+trial)",
    re.IGNORECASE,
)

# F2: old product-form words; only FAIL when used as current features
F2_WORDS = [
    "Scan Code", "Listen Check", "audio meters", "launch window",
    "standalone Practice tab", "web mock room",
]
# Context markers that make an F2 reference compliant (retired/removed/old)
F2_RETIRED = re.compile(
    r"(old|retired|removed|gone|no\s+longer|replaced|discontinued|was\b|were\b|deprecated)",
    re.IGNORECASE,
)

F4_PHRASES = [
    r"SEO implication", r"recommended framing", r"content patterns to retire",
    r"content patterns to introduce", r"site architecture",
]

F5_WORD = re.compile(r"\bundetectable\b", re.IGNORECASE)


def extract_links(text: str):
    """Return (internal_links, external_links) markdown links after frontmatter."""
    body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", body)
    internal, external = [], []
    for link in links:
        if link.startswith("http://") or link.startswith("https://"):
            external.append(link)
        elif link.startswith("/"):
            internal.append(link)
    return internal, external


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--forbidden", action="append", default=[])
    ap.add_argument("--check-live", action="store_true")
    args = ap.parse_args()

    with open(args.path, encoding="utf-8") as f:
        text = f.read()

    errors, warnings = [], []
    internal, external = extract_links(text)

    # G6: internal links must match an allowed prefix
    for link in internal:
        if not any(link.startswith(p) for p in ALLOWED_PREFIXES):
            errors.append(f"G6: internal link not in whitelist: {link}")
    for fbd in args.forbidden:
        for link in internal:
            if link.startswith(fbd):
                errors.append(f"G6: forbidden path linked: {link}")

    # F6: conversion paths forbidden in body copy (carried by buttons only)
    for link in internal:
        if any(link.startswith(p) for p in CONVERSION_PREFIXES):
            errors.append(f"F6: conversion path linked in body (button only): {link}")

    # F1: free-trial promotions (negation/clarification contexts exempt)
    for phrase in F1_PROMOTIONS:
        for m in re.finditer(phrase, text, re.IGNORECASE):
            window = text[max(0, m.start() - 80):m.end() + 40]
            if F1_NEGATION.search(window):
                continue  # clarification ("no free trial") — allowed
            errors.append(f"F1: free-trial promotion found: '{m.group(0)}'")

    # F2: old product-form words as current features (retired contexts exempt)
    for word in F2_WORDS:
        for m in re.finditer(re.escape(word), text, re.IGNORECASE):
            window = text[max(0, m.start() - 80):m.end() + 80]
            if F2_RETIRED.search(window):
                continue  # reference to retired item — allowed
            errors.append(f"F2: old product-form word used as current feature: '{word}'")

    # F4: internal-decision phrases
    for phrase in F4_PHRASES:
        if re.search(phrase, text, re.IGNORECASE):
            errors.append(f"F4: internal-decision phrase found: '{phrase}'")

    # F5: "undetectable" — warn (primary-claim judgment is human)
    for m in F5_WORD.finditer(text):
        warnings.append(f"F5: 'undetectable' used at char {m.start()} — ensure not primary claim")

    # G2: live external link check (optional)
    if args.check_live:
        for link in external[:5]:
            try:
                req = urllib.request.Request(link, method="HEAD",
                                             headers={"User-Agent": "Mozilla/5.0"})
                urllib.request.urlopen(req, timeout=10)
            except Exception:
                warnings.append(f"G2: external link may be dead: {link}")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        for w in warnings:
            print(f"  ! {w}")
        sys.exit(1)
    print("PASS: links and red lines OK")
    for w in warnings:
        print(f"  ! {w}")
    sys.exit(0)


if __name__ == "__main__":
    main()
