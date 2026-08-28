#!/usr/bin/env python3
"""
Wrap bare HTML tables and convert GFM pipe tables to childrenHtml blocks (format A).

Usage (from anywhere):
  python migrate-tables-to-childrenhtml.py
  python migrate-tables-to-childrenhtml.py --deploy-root "E:/自有部署项目/alignify production"
  python migrate-tables-to-childrenhtml.py --dry-run
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

FENCE_START = "<!-- childrenHtml:start -->"
FENCE_END = "<!-- childrenHtml:end -->"

TABLE_DIV_RE = re.compile(
    r'<div class="(?:content-html|article-scroll-wrap)">\s*<table>.*?</table>\s*</div>',
    re.DOTALL,
)

# Multiline: outer wrapper may include caption <p> (insights indie-hackers)
TABLE_DIV_WRAPPED_RE = re.compile(
    r'<div>\s*<p>[^<]*</p>\s*<div class="content-html">\s*<table>.*?</table>\s*</div>\s*</div>',
    re.DOTALL,
)

BARE_TABLE_RE = re.compile(
    r'<table>.*?</table>',
    re.DOTALL,
)

GFM_ROW_RE = re.compile(r"^\|.+\|$")
GFM_SEP_RE = re.compile(r"^\|[\s\-:|]+\|$")

BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def default_deploy_root() -> Path:
    candidates = [
        Path(r"E:\自有部署项目\alignify production"),
        Path(__file__).resolve().parents[3] / "部署项目" / "alignify-by-kostja",
    ]
    for p in candidates:
        if (p / "content").is_dir():
            return p
    raise SystemExit("Set --deploy-root to alignify production repo")


def fenced_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    pos = 0
    while True:
        start = text.find(FENCE_START, pos)
        if start == -1:
            break
        end = text.find(FENCE_END, start)
        if end == -1:
            break
        spans.append((start, end + len(FENCE_END)))
        pos = end + len(FENCE_END)
    return spans


def in_fenced(spans: list[tuple[int, int]], idx: int) -> bool:
    return any(s <= idx < e for s, e in spans)


def cell_to_html(cell: str) -> str:
    out = cell.strip()
    out = BOLD_RE.sub(r"<strong>\1</strong>", out)
    out = LINK_RE.sub(r'<a href="\2">\1</a>', out)
    return out


def gfm_table_to_html(block_lines: list[str]) -> str:
    if len(block_lines) < 2:
        return "\n".join(block_lines)

    header = [cell_to_html(c) for c in block_lines[0].strip().strip("|").split("|")]
    body_rows = block_lines[2:] if GFM_SEP_RE.match(block_lines[1].strip()) else block_lines[1:]

    thead = "<thead><tr>" + "".join(f"<th>{c}</th>" for c in header) + "</tr></thead>"
    tbody_parts: list[str] = []
    for row_line in body_rows:
        if not GFM_ROW_RE.match(row_line.strip()):
            continue
        cells = [cell_to_html(c) for c in row_line.strip().strip("|").split("|")]
        tbody_parts.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
    tbody = "<tbody>" + "".join(tbody_parts) + "</tbody>"
    return (
        f"{FENCE_START}\n"
        f'<div class="content-html"><table>{thead}{tbody}</table></div>\n'
        f"{FENCE_END}"
    )


def _gfm_col_count(row: str) -> int:
    return len(row.strip().strip("|").split("|"))


def convert_gfm_tables(text: str, spans: list[tuple[int, int]]) -> tuple[str, int]:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    converted = 0
    offset = 0

    while i < len(lines):
        line = lines[i]
        line_start = offset
        offset += len(line)

        if in_fenced(spans, line_start) or not GFM_ROW_RE.match(line.strip()):
            out.append(line)
            i += 1
            continue

        block: list[str] = [line.rstrip("\r\n")]
        header_cols = _gfm_col_count(block[0])
        j = i + 1
        while j < len(lines):
            s = lines[j].strip()
            if GFM_ROW_RE.match(s):
                block.append(s)
                j += 1
                continue
            if s == "" and j + 1 < len(lines):
                nxt = lines[j + 1].strip()
                if GFM_ROW_RE.match(nxt) and _gfm_col_count(nxt) == header_cols:
                    j += 1
                    continue
            break

        if len(block) >= 2 and (len(block) == 2 or GFM_SEP_RE.match(block[1])):
            html_block = gfm_table_to_html(block)
            if not html_block.endswith("\n"):
                html_block += "\n"
            out.append(html_block)
            if j < len(lines) and lines[j].strip() == "":
                out.append("\n")
                j += 1
            converted += 1
            i = j
            continue

        out.append(line)
        i += 1

    return "".join(out), converted


def _wrap_match(m: re.Match[str], spans: list[tuple[int, int]], counter: list[int]) -> str:
    if in_fenced(spans, m.start()):
        return m.group(0)
    counter[0] += 1
    inner = m.group(0)
    return f"{FENCE_START}\n{inner}\n{FENCE_END}"


def wrap_bare_html_tables(text: str) -> tuple[str, int]:
    spans = fenced_spans(text)
    wrapped = [0]

    def repl(m: re.Match[str]) -> str:
        return _wrap_match(m, spans, wrapped)

    new_text = TABLE_DIV_WRAPPED_RE.sub(repl, text)
    spans = fenced_spans(new_text)
    new_text = TABLE_DIV_RE.sub(repl, new_text)

    def repl_bare(m: re.Match[str]) -> str:
        if in_fenced(spans, m.start()):
            return m.group(0)
        wrapped[0] += 1
        table = m.group(0)
        return f"{FENCE_START}\n<div class=\"content-html\">{table}</div>\n{FENCE_END}"

    spans = fenced_spans(new_text)
    new_text = BARE_TABLE_RE.sub(repl_bare, new_text)
    return new_text, wrapped[0]


def migrate_file(text: str) -> tuple[str, dict[str, int]]:
    stats = {"gfm": 0, "wrap": 0}
    spans = fenced_spans(text)
    text, gfm = convert_gfm_tables(text, spans)
    stats["gfm"] = gfm
    text, wrap = wrap_bare_html_tables(text)
    stats["wrap"] = wrap
    return text, stats


def main() -> None:
    ap = argparse.ArgumentParser(description="Migrate tables to childrenHtml format A")
    ap.add_argument("--deploy-root", type=Path, default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = args.deploy_root or default_deploy_root()
    content = root / "content"
    if not content.is_dir():
        raise SystemExit(f"Missing content dir: {content}")

    files_changed = 0
    total_gfm = total_wrap = 0

    for path in sorted(content.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        migrated, stats = migrate_file(original)
        if migrated == original:
            continue
        files_changed += 1
        total_gfm += stats["gfm"]
        total_wrap += stats["wrap"]
        rel = path.relative_to(root)
        print(f"{'[dry-run] ' if args.dry_run else ''}{rel}: gfm={stats['gfm']} wrap={stats['wrap']}")
        if not args.dry_run:
            path.write_text(migrated, encoding="utf-8")

    mode = "dry-run" if args.dry_run else "done"
    print(
        f"{mode}: {files_changed} files, "
        f"{total_gfm} GFM tables converted, {total_wrap} bare HTML tables wrapped"
    )


if __name__ == "__main__":
    main()
