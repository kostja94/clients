#!/usr/bin/env python3
"""
Migrate legacy Tailwind-styled h3/h4/p inside childrenHtml blocks to Markdown headings
and paragraphs. Keeps ul/ol/table/layout divs in childrenHtml per anatomy.md §四·一.

Usage:
  python migrate-childrenhtml-headings.py [--dry-run] [--file PATH] [CONTENT_ROOT]
"""

from __future__ import annotations

import argparse
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

DEFAULT_ROOT = Path(r"E:/自有部署项目/alignify production/content/marketing")

CHILDREN_START = "<!-- childrenHtml:start -->"
CHILDREN_END = "<!-- childrenHtml:end -->"

BLOCK_RE = re.compile(
    re.escape(CHILDREN_START) + r"\n?(.*?)\n?" + re.escape(CHILDREN_END),
    re.DOTALL,
)

NEEDS_MIGRATION = re.compile(
    r'<h[34]\s+class="text-lg|<p\s+class="text-base\s+md:text-lg\s+leading-relaxed',
    re.IGNORECASE,
)

LEGACY_H3_CLASS = "text-lg"
LEGACY_P_CLASS = "text-base"


class InlineHtmlToMd(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._link_text: list[str] = []
        self._link_href: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if tag == "strong":
            self.parts.append("**")
        elif tag == "em":
            self.parts.append("*")
        elif tag == "br":
            self.parts.append(" ")
        elif tag == "a":
            self._link_href = attr.get("href")
            self._link_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "strong":
            self.parts.append("**")
        elif tag == "em":
            self.parts.append("*")
        elif tag == "a":
            text = "".join(self._link_text).strip()
            href = self._link_href or ""
            self.parts.append(f"[{text}]({href})")
            self._link_text = []
            self._link_href = None

    def handle_data(self, data: str) -> None:
        if self._link_href is not None:
            self._link_text.append(data)
        else:
            self.parts.append(data)

    def get_markdown(self) -> str:
        text = "".join(self.parts)
        text = re.sub(r"\s+", " ", text).strip()
        return unescape(text)


def tag_inner_md(tag: Tag) -> str:
    parser = InlineHtmlToMd()
    parser.feed(tag.decode_contents())
    return parser.get_markdown()


def is_legacy_h3(tag: Tag) -> bool:
    classes = tag.get("class") or []
    return tag.name == "h3" and any(LEGACY_H3_CLASS in c for c in classes)


def is_legacy_h4(tag: Tag) -> bool:
    classes = tag.get("class") or []
    return tag.name == "h4" and any("font-semibold" in c for c in classes)


def is_legacy_p(tag: Tag) -> bool:
    classes = tag.get("class") or []
    return tag.name == "p" and any(LEGACY_P_CLASS in c for c in classes)


def is_layout_container(tag: Tag) -> bool:
    """Atomic HTML blocks — keep intact in childrenHtml."""
    if tag.name in ("ul", "ol", "table", "img"):
        return True
    if tag.name != "div":
        return False
    classes = " ".join(tag.get("class") or [])
    if "grid" in classes:
        return True
    if "content-html" in classes and tag.find("table"):
        return True
    return False


def heading_md(tag: Tag) -> str:
    level = 3 if tag.name == "h3" else 4
    title = tag_inner_md(tag)
    anchor = tag.get("id")
    prefix = "#" * level
    if anchor:
        return f"{prefix} {title} {{#{anchor}}}\n"
    return f"{prefix} {title}\n"


def is_legacy_h3_tag(tag: Tag) -> bool:
    return is_legacy_h3(tag)


def simplify_li_paragraphs(html: str) -> str:
    """Remove legacy <p> wrappers inside <li> — content stays in list item."""
    if LEGACY_P_CLASS not in html and "text-base md:text-lg" not in html:
        return html
    soup = BeautifulSoup(html, "html.parser")
    for p in soup.find_all("p"):
        classes = " ".join(p.get("class") or [])
        if LEGACY_P_CLASS in classes and p.parent and p.parent.name == "li":
            p.unwrap()
    return str(soup)


def iter_nodes(nodes) -> list[Tag | NavigableString]:
    out: list[Tag | NavigableString] = []
    for node in nodes:
        if isinstance(node, NavigableString):
            if str(node).strip():
                out.append(node)
        elif isinstance(node, Tag):
            if node.name == "ol" and node.find(is_legacy_h3_tag):
                for li in node.find_all("li", recursive=False):
                    out.extend(iter_nodes(li.children))
                continue
            if is_layout_container(node):
                out.append(node)
            elif node.name == "li" and node.find(is_legacy_h3_tag):
                out.extend(iter_nodes(node.children))
            elif node.name in ("div", "section") and not is_layout_container(node):
                out.extend(iter_nodes(node.children))
            else:
                out.append(node)
    return out


def migrate_block(inner: str) -> str | None:
    if not NEEDS_MIGRATION.search(inner):
        return None

    soup = BeautifulSoup(f"<root>{inner}</root>", "html.parser")
    root = soup.root
    nodes = iter_nodes(root.children)

    md_chunks: list[str] = []
    html_chunks: list[str] = []

    def flush_html() -> None:
        if html_chunks:
            combined = "\n".join(html_chunks).strip()
            if combined:
                md_chunks.append(f"{CHILDREN_START}\n{combined}\n{CHILDREN_END}")
            html_chunks.clear()

    for node in nodes:
        if isinstance(node, NavigableString):
            continue
        if is_legacy_h3(node) or is_legacy_h4(node):
            flush_html()
            md_chunks.append(heading_md(node))
            continue
        if is_legacy_p(node):
            flush_html()
            text = tag_inner_md(node)
            if text:
                md_chunks.append(f"{text}\n")
            continue
        html_chunks.append(simplify_li_paragraphs(str(node).strip()))

    flush_html()
    result = "\n\n".join(c.rstrip() for c in md_chunks).strip()
    if not result or result == inner.strip():
        return None
    return result + "\n"


def migrate_file(path: Path, dry_run: bool = False) -> tuple[bool, int]:
    text = path.read_text(encoding="utf-8")
    total_changes = 0
    max_passes = 20

    for _ in range(max_passes):
        changes = 0

        def replacer(m: re.Match[str]) -> str:
            nonlocal changes
            inner = m.group(1)
            migrated = migrate_block(inner)
            if migrated is None:
                return m.group(0)
            changes += 1
            return migrated.rstrip("\n") + "\n"

        new_text = BLOCK_RE.sub(replacer, text)
        if changes == 0:
            break
        total_changes += changes
        text = new_text

    if total_changes and not dry_run:
        path.write_text(text, encoding="utf-8")

    return total_changes > 0, total_changes


def collect_files(root: Path, single: Path | None) -> list[Path]:
    if single:
        return [single]
    return sorted(root.glob("**/*.md"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("content_root", nargs="?", default=str(DEFAULT_ROOT))
    ap.add_argument("--file", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = Path(args.content_root)
    files = collect_files(root, args.file)
    touched = 0

    for f in files:
        changed, n = migrate_file(f, dry_run=args.dry_run)
        if changed:
            touched += 1
            mode = "would update" if args.dry_run else "updated"
            print(f"{mode}: {f} ({n} pass(es))")

    print(f"\nDone: {touched} file(s) {'would be ' if args.dry_run else ''}migrated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
