#!/usr/bin/env python3
"""Remove heroHtml from all content/*.md frontmatter (E44).

Handles multiline YAML blocks (indented or flush-left HTML after `heroHtml: |`).

Usage:
  python strip-hero-html-frontmatter.py --root "E:/自有部署项目/alignify production"
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERO_LINK_RE = re.compile(r'<a\s+href="([^"]+)"[^>]*>([^<]+)</a>', re.I)
YAML_KEY_RE = re.compile(r"^[A-Za-z0-9_]+:\s*", re.M)
HTML_LINE_RE = re.compile(r"^\s*<", re.M)
FIRST_H2_BLOCK_RE = re.compile(
    r"(<!-- block:section -->\s*\n##[^\n]+\n\n)([^\n]+(?:\n(?![#\n<!--])[^\n]+)*)",
    re.M,
)


def strip_hero_from_head(head: str) -> tuple[str, str | None]:
    hero_lines: list[str] = []
    out: list[str] = []
    in_hero = False

    for line in head.splitlines():
        if in_hero:
            if YAML_KEY_RE.match(line):
                in_hero = False
                out.append(line)
                continue
            if HTML_LINE_RE.match(line) or (line.startswith("  ") and line.strip()):
                hero_lines.append(line.strip() if line.startswith("  ") else line)
                continue
            if not line.strip():
                continue
            # unknown line inside hero — still discard while in hero mode
            hero_lines.append(line)
            continue

        if line.strip().startswith("heroHtml:"):
            in_hero = True
            hero_lines = []
            continue

        out.append(line)

    hero_html = "\n".join(hero_lines).strip() if hero_lines else None
    return "\n".join(out).rstrip(), hero_html


def preserve_hero_links(body: str, hero_html: str | None) -> tuple[str, list[str]]:
    if not hero_html:
        return body, []
    added: list[str] = []
    links = HERO_LINK_RE.findall(hero_html)
    missing = [(href, text.strip()) for href, text in links if href not in body]
    if not missing:
        return body, added

    m = FIRST_H2_BLOCK_RE.search(body)
    if not m:
        return body, [h for h, _ in missing]

    first_para = m.group(2).rstrip()
    zh = any("\u4e00" <= c <= "\u9fff" for c in first_para)
    suffix_parts: list[str] = []
    for href, text in missing:
        clean = re.sub(r"\s*→\s*$", "", text)
        if zh:
            suffix_parts.append(f"延伸阅读见 [{clean}]({href})。")
        else:
            suffix_parts.append(f"Related: [{clean}]({href}).")
        added.append(href)

    sep = "。" if zh else ". "
    new_para = first_para
    if not new_para.endswith(("。", ".", "!", "?")):
        new_para += "。" if zh else "."
    new_para = new_para + (" " if not zh else "") + " ".join(suffix_parts)
    new_body = body[: m.start(2)] + new_para + body[m.end(2) :]
    return new_body, added


def clean_orphan_html_in_head(head: str) -> str:
    """Remove HTML lines accidentally left in frontmatter (partial strip recovery)."""
    out: list[str] = []
    for line in head.splitlines():
        if HTML_LINE_RE.match(line):
            continue
        out.append(line)
    return "\n".join(out).rstrip()


def process_file(path: Path, dry_run: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n([\s\S]*?)\r?\n---\r?\n?", text)
    if not m:
        return {"path": str(path), "changed": False}

    head_raw, body = m.group(1), text[m.end() :]
    needs_work = "heroHtml:" in head_raw or HTML_LINE_RE.search(head_raw)
    if not needs_work:
        return {"path": str(path), "changed": False}

    head_clean, hero_html = strip_hero_from_head(head_raw)
    head_clean = clean_orphan_html_in_head(head_clean)
    new_body, added = preserve_hero_links(body, hero_html)
    new_text = f"---\n{head_clean}\n---\n{new_body}"

    if new_text == text:
        return {"path": str(path), "changed": False}

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return {
        "path": str(path),
        "changed": True,
        "links_preserved": added,
        "dry_run": dry_run,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=r"E:\自有部署项目\alignify production")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    content = root / "content"
    if not content.is_dir():
        print(f"content/ not found under {root}", file=sys.stderr)
        return 1

    changed = 0
    for path in sorted(content.rglob("*.md")):
        result = process_file(path, args.dry_run)
        if result.get("changed"):
            changed += 1
            rel = path.relative_to(root)
            n = len(result.get("links_preserved") or [])
            extra = f" (+{n} links)" if n else ""
            print(f"{'[dry-run] ' if args.dry_run else ''}fixed: {rel}{extra}")

    print(f"\nDone: {changed} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
