#!/usr/bin/env python3
"""Verify relative markdown links under skills/. Skips fenced/inline code."""
import re
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[2] / "skills"
FENCE_RE = re.compile(r"```[\s\S]*?```|`[^`\n]+`")
LINK_RE = re.compile(r"(?<!\])\]\(([^)]+)\)")


def strip_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def main() -> int:
    broken: list[tuple[str, str, str]] = []
    checked = 0
    file_count = 0

    for md in sorted(SKILLS.rglob("*.md")):
        file_count += 1
        text = strip_code(md.read_text(encoding="utf-8", errors="replace"))
        rel_md = md.relative_to(SKILLS).as_posix()
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if "#" in target:
                target = target.split("#", 1)[0]
            if not target or target.startswith("/"):
                continue
            checked += 1
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                broken.append((rel_md, target, str(resolved)))

    print(f"Files: {file_count}")
    print(f"Relative links checked: {checked}")
    print(f"Broken: {len(broken)}")
    for rel_md, target, resolved in broken:
        print("---")
        print(f"File: {rel_md}")
        print(f"Link: {target}")
        print(f"Resolved: {resolved}")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
