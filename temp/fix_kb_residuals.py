#!/usr/bin/env python3
"""Fix remaining KB dedupe audit issues across knowledge/tools."""
import re
import sys
from pathlib import Path

ROOT = Path(r"e:\clients\Alignify\knowledge\tools")
sys.path.insert(0, str(Path(__file__).parent))
from audit_kb_dedupe import parse_sections, section_text, extract_products, extract_urls, normalize_url, audit_file


def unbold_products(text: str, products: set) -> str:
    for p in sorted(products, key=len, reverse=True):
        text = re.sub(rf"\*\*{re.escape(p)}([^*]*?)\*\*", rf"{p}\1", text)
    return text


def fix_compare_section(lines: list, sections: dict) -> bool:
    key = "对比与测评"
    if key not in sections or "外链索引" not in sections:
        return False
    links = section_text(lines, sections, "外链索引")
    links_p = extract_products(links)
    s, e = sections[key]
    block = "\n".join(lines[s:e])
    overlap = extract_products(block) & links_p
    if len(overlap) < 3:
        return False
    new_block = unbold_products(block, overlap)
    if len(extract_products(new_block) & links_p) >= 3:
        new_block = unbold_products(new_block, links_p)
    lines[s:e] = new_block.splitlines()
    return True


def fix_capability_section(lines: list, sections: dict) -> bool:
    key = "能力栈"
    if key not in sections or "外链索引" not in sections:
        return False
    links = section_text(lines, sections, "外链索引")
    links_p = extract_products(links)
    s, e = sections[key]
    block = "\n".join(lines[s:e])
    overlap = {p for p in (extract_products(block) & links_p) if len(p) > 4}
    if len(overlap) < 4:
        return False
    new_block = unbold_products(block, overlap)
    lines[s:e] = new_block.splitlines()
    return True


def fix_duplicate_urls_in_ext(lines: list, sections: dict) -> bool:
    if "外链索引" not in sections:
        return False
    links = section_text(lines, sections, "外链索引")
    link_urls = {normalize_url(u) for u in extract_urls(links)}
    changed = False
    for sec_name in ["延伸阅读", "延伸阅读_2", "站外"]:
        if sec_name not in sections:
            continue
        s, e = sections[sec_name]
        new_lines = []
        for line in lines[s:e]:
            urls = [normalize_url(u) for u in extract_urls(line)]
            if urls and all(u in link_urls for u in urls) and "§外链索引" not in line:
                changed = True
                continue
            new_lines.append(line)
        if changed:
            lines[s:e] = new_lines
    return changed


def fix_tools_product_types_unbold(lines: list, sections: dict) -> bool:
    key = "工具与产品类型"
    if key not in sections or "外链索引" not in sections:
        return False
    links = section_text(lines, sections, "外链索引")
    links_p = extract_products(links)
    s, e = sections[key]
    block = "\n".join(lines[s:e])
    overlap = extract_products(block) & links_p
    if len(overlap) < 4:
        return False
    new_block = unbold_products(block, overlap)
    lines[s:e] = new_block.splitlines()
    return True


def rename_further_reading(text: str) -> str:
    return text.replace("## 延伸阅读与参考材料", "## 延伸阅读 · 站内外")


def fix_preamble_boundary_slugs(text: str) -> str:
    """Remove backtick slug pointers in 勿与混买 line when duplicated in 分流表."""
    lines = text.splitlines()
    if not lines:
        return text
    first_h2 = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    split_idx = next((i for i, l in enumerate(lines) if re.match(r"^## 与相邻 slug 分流", l)), None)
    if split_idx is None:
        return text
    split_text = "\n".join(lines[split_idx:first_h2 + 50])
    split_slugs = set(re.findall(r"`([a-z0-9-]+)`", split_text))
    if len(split_slugs) < 2:
        return text
    for i in range(min(first_h2, 12)):
        if "勿与" in lines[i] and "混买" in lines[i]:
            for slug in split_slugs:
                lines[i] = re.sub(rf"→\s*`\*\*{re.escape(slug)}\*\*`", "→ 见 §与相邻 slug 分流", lines[i])
                lines[i] = re.sub(rf"→\s*`{re.escape(slug)}`", "→ 见 §与相邻 slug 分流", lines[i])
                lines[i] = re.sub(rf"·\s*`\*\*{re.escape(slug)}\*\*`", "", lines[i])
            lines[i] = re.sub(r"\s{2,}", " ", lines[i]).strip()
            break
    return "\n".join(lines)


def process_file(fp: Path) -> list[str]:
    actions = []
    text = fp.read_text(encoding="utf-8")
    orig = text
    text = rename_further_reading(text)
    if text != orig:
        actions.append("rename延伸阅读")
    text = fix_preamble_boundary_slugs(text)
    lines = text.splitlines()
    sections, _ = parse_sections(text)
    if fix_compare_section(lines, sections):
        actions.append("compare_unbold")
    sections, _ = parse_sections("\n".join(lines))
    if fix_capability_section(lines, sections):
        actions.append("capability_unbold")
    sections, _ = parse_sections("\n".join(lines))
    if fix_duplicate_urls_in_ext(lines, sections):
        actions.append("ext_dedupe_urls")
    sections, _ = parse_sections("\n".join(lines))
    if fix_tools_product_types_unbold(lines, sections):
        actions.append("tools_types_unbold")
    new_text = "\n".join(lines)
    if new_text != orig:
        fp.write_text(new_text, encoding="utf-8")
    return actions


def main():
    changed = []
    for fp in sorted(ROOT.rglob("*.md")):
        acts = process_file(fp)
        if acts:
            changed.append((fp.relative_to(ROOT).as_posix(), acts))
    print(f"Updated {len(changed)} files")
    for path, acts in changed[:30]:
        print(f"  {path}: {', '.join(acts)}")
    if len(changed) > 30:
        print(f"  ... and {len(changed) - 30} more")


if __name__ == "__main__":
    main()
