#!/usr/bin/env python3
"""Strict quality audit for static-image Tools articles (skills P0/P1)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

DEPLOY = Path(__file__).resolve().parents[3] / "alignify-by-kostja"
if not DEPLOY.exists():
    DEPLOY = Path(r"D:\部署项目\alignify-by-kostja")

TOOLS = DEPLOY / "content" / "tools"
META_PATH = DEPLOY / "src" / "data" / "tools-meta.ts"
PUBLIC = DEPLOY / "public"

SLUGS = [
    "image",
    "image-generator",
    "image-editor",
    "image-enhancer",
    "image-relighting",
    "background-changer",
    "headshot-generator",
    "logo-generator",
    "poster-generator",
    "tattoo-generator",
    "avatar",
    "image-to-video",
]

GENERIC_EXCERPT_PATTERNS = [
    "帮助用户快速实现目标",
    "提升工作效率和创造力",
    "助力业务增长",
    "help users achieve",
    "boost productivity and creativity",
    "suitable for teams of all sizes",
]

REQUIRED_TYPES = {
    "tldr",
    "howItWorks",
    "bestTools",
    "faq",
}


def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "")


def zh_chars(s: str) -> int:
    return len(re.sub(r"\s+", "", strip_html(s)))


def en_chars(s: str) -> int:
    return len(strip_html(s))


def en_words(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9']+", strip_html(s)))


def load_json(slug: str, loc: str) -> dict:
    return json.loads((TOOLS / loc / f"{slug}.json").read_text(encoding="utf-8"))


def extract_meta(slug: str) -> dict | None:
    if not META_PATH.exists():
        return None
    text = META_PATH.read_text(encoding="utf-8")
    m = re.search(rf'"{re.escape(slug)}"\s*:\s*\{{([\s\S]*?)\n  \}},', text)
    if not m:
        return None
    block = m.group(1)
    en_t = re.search(r'en:\s*\{\s*title:\s*"([^"]+)"', block)
    zh_t = re.search(r'zh:\s*\{\s*title:\s*"([^"]+)"', block)
    en_d = re.search(r'en:\s*\{\s*title:[^}]+description:\s*"([^"]+)"', block)
    zh_d = re.search(r'zh:\s*\{\s*title:[^}]+description:\s*"([^"]+)"', block)
    return {
        "en_title": en_t.group(1) if en_t else "",
        "zh_title": zh_t.group(1) if zh_t else "",
        "en_desc": en_d.group(1) if en_d else "",
        "zh_desc": zh_d.group(1) if zh_d else "",
    }


def collect_best_tools(blocks: list) -> list[dict]:
    out: list[dict] = []
    for b in blocks:
        for key in ("tools", "categories"):
            items = b.get(key)
            if not isinstance(items, list):
                continue
            for item in items:
                if isinstance(item, dict) and item.get("description"):
                    out.append(item)
                if isinstance(item, dict) and isinstance(item.get("tools"), list):
                    out.extend(t for t in item["tools"] if t.get("description"))
    return out


def walk_strings(obj: Any, out: list[str]) -> None:
    if isinstance(obj, str):
        out.append(obj)
    elif isinstance(obj, dict):
        for v in obj.values():
            walk_strings(v, out)
    elif isinstance(obj, list):
        for v in obj:
            walk_strings(v, out)


def internal_slugs_from_data(data: dict, *, exclude_types: set[str] | None = None) -> dict[str, int]:
    exclude_types = exclude_types or set()
    strings: list[str] = []
    for block in data.get("blocks", []):
        if block.get("type") in exclude_types:
            continue
        walk_strings(block, strings)
    counts: dict[str, int] = {}
    for s in strings:
        for href in re.findall(r"""href=['"]([^'"]+)['"]""", s):
            m = re.search(r"/(?:zh/)?tools/([a-z0-9-]+)", href)
            if m:
                slug = m.group(1)
                counts[slug] = counts.get(slug, 0) + 1
    return counts


def faq_link_audit(faq_items: list, body_slug_counts: dict[str, int]) -> list[str]:
    errs: list[str] = []
    faq_slugs: set[str] = set()
    for item in faq_items:
        ans = item.get("answer", "")
        links = re.findall(r"""href=['"]([^'"]+)['"]""", ans)
        if len(links) > 2:
            errs.append(f"FAQ answer has {len(links)} links (>2)")
        for href in links:
            m = re.search(r"/(?:zh/)?tools/([a-z0-9-]+)", href)
            if m:
                faq_slugs.add(m.group(1))
    if len(faq_slugs) > 3:
        errs.append(f"FAQ distinct slugs {len(faq_slugs)} > 3")
    dup = {s for s in faq_slugs if body_slug_counts.get(s, 0) > 0}
    if dup:
        errs.append(f"FAQ slugs duplicate body: {dup}")
    return errs


def audit_slug(slug: str, loc: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    path = TOOLS / loc / f"{slug}.json"
    if not path.exists():
        return [f"missing {path}"], []

    data = load_json(slug, loc)
    blocks = data.get("blocks", [])
    layout = data.get("blogLayout", {})
    prefix = f"{loc}/{slug}"

    # P0-1 conclusion before FAQ
    idx_faq = next((i for i, b in enumerate(blocks) if b.get("type") == "faq"), -1)
    idx_con = next(
        (
            i
            for i, b in enumerate(blocks)
            if b.get("type") == "section"
            and (
                b.get("id") == "conclusion"
                or "结论" in (b.get("title") or "")
                or "Conclusion" in (b.get("title") or "")
            )
        ),
        -1,
    )
    if idx_faq >= 0 and idx_con >= 0 and idx_con > idx_faq:
        errors.append(f"{prefix}: conclusion after FAQ (E7)")

    # P0-2 FAQ count
    faq = next((b for b in blocks if b.get("type") == "faq"), None)
    faq_items = faq.get("items", []) if faq else []
    if len(faq_items) < 8:
        errors.append(f"{prefix}: FAQ {len(faq_items)} < 8 (E8)")

    # P0-3 FAQ links (body = all blocks except faq)
    body_counts = internal_slugs_from_data(data, exclude_types={"faq"})
    slug_counts = internal_slugs_from_data(data)
    errors.extend(f"{prefix}: {e}" for e in faq_link_audit(faq_items, body_counts))

    # duplicate slug links R4 (exclude self)
    for s, n in slug_counts.items():
        if s != slug and n > 1:
            errors.append(f"{prefix}: slug /{s}/ linked {n} times (R4)")

    if len(slug_counts) < 5:
        errors.append(f"{prefix}: distinct internal slugs {len(slug_counts)} < 5 (R1)")

    # P0-5/6 BestTools
    tools = collect_best_tools(blocks)
    if not tools and slug not in ("image",):
        warnings.append(f"{prefix}: no bestTools descriptions found")
    desc_lens = []
    for t in tools:
        desc = t.get("description", "")
        short = t.get("shortDescription", "")
        dl = zh_chars(desc) if loc == "zh" else en_chars(desc)
        desc_lens.append(dl)
        min_desc = 100 if loc == "zh" else 280
        min_short = 4 if loc == "zh" else 10
        sl = zh_chars(short) if loc == "zh" else en_chars(short)
        name = t.get("name") or t.get("id") or "?"
        if dl < min_desc:
            errors.append(f"{prefix}: {name} description {dl} < {min_desc} (E12)")
        if sl < min_short:
            errors.append(f"{prefix}: {name} shortDescription {sl} < {min_short}")

    # truncated descriptions (legacy export bug)
    for block in blocks:
        for tool in collect_best_tools([block]):
            desc = tool.get("description", "")
            if desc.rstrip().endswith("还。") or desc.rstrip().endswith("还."):
                errors.append(f"{prefix}: truncated description on {tool.get('id')}")

    if desc_lens:
        mn, mx = min(desc_lens), max(desc_lens)
        if mn > 0 and mx / mn > 3:
            warnings.append(f"{prefix}: bestTools max/min ratio {mx/mn:.1f} > 3 (E16)")

    # Excerpt
    exc = layout.get("excerpt", "")
    el = zh_chars(exc) if loc == "zh" else en_chars(exc)
    if loc == "zh" and el < 80:
        warnings.append(f"{prefix}: excerpt {el} chars < 80")
    if loc == "en" and el < 200:
        warnings.append(f"{prefix}: excerpt {el} chars < 200")
    for pat in GENERIC_EXCERPT_PATTERNS:
        if pat in exc:
            errors.append(f"{prefix}: generic excerpt pattern '{pat}' (E14)")

    # H1 no year
    h1 = layout.get("title", "")
    if re.search(r"20\d{2}", h1):
        errors.append(f"{prefix}: H1 contains year (E5)")

    # Structure
    types = {b.get("type") for b in blocks}
    missing = REQUIRED_TYPES - types
    if slug != "image" and missing:
        warnings.append(f"{prefix}: missing block types {missing}")

    # howItWorks
    hiw = next((b for b in blocks if b.get("type") == "howItWorks"), None)
    if hiw:
        tb = hiw.get("technologyBase", "")
        tb_len = zh_chars(tb) if loc == "zh" else en_words(tb)
        min_tb = 220 if loc == "zh" else 140
        if tb_len < min_tb:
            warnings.append(f"{prefix}: technologyBase {tb_len} < {min_tb}")
        adv = hiw.get("advantages") or []
        if len(adv) < 3:
            errors.append(f"{prefix}: howItWorks advantages {len(adv)} < 3 (E15)")

    # howToChoose 5 steps
    htc = next((b for b in blocks if b.get("type") == "howToChoose"), None)
    if htc:
        steps = htc.get("steps") or []
        if len(steps) != 5:
            errors.append(f"{prefix}: howToChoose steps {len(steps)} != 5")

    # references
    refs = next((b for b in blocks if b.get("type") == "references"), None)
    ref_n = len(refs.get("items", [])) if refs else 0
    if ref_n < 3:
        warnings.append(f"{prefix}: references {ref_n} < 3 (P2-4)")

    # FAQ answer length
    for i, item in enumerate(faq_items):
        ans = item.get("answer", "")
        al = zh_chars(ans) if loc == "zh" else en_words(ans)
        min_a = 40 if loc == "zh" else 40
        if al < min_a:
            warnings.append(f"{prefix}: FAQ[{i}] answer too short ({al})")

    # Meta (once per slug)
    return errors, warnings


def audit_meta(slug: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    meta = extract_meta(slug)
    if not meta:
        warnings.append(f"{slug}: could not parse tools-meta.ts")
        return errors, warnings
    for loc, key_best, key_year in (
        ("en", "Best", r"\(2026\)"),
        ("zh", "最佳", r"（2026）"),
    ):
        title = meta[f"{loc}_title"]
        if key_best not in title:
            errors.append(f"{slug} meta {loc} title missing '{key_best}' (E1)")
        if not re.search(key_year, title):
            errors.append(f"{slug} meta {loc} title missing year (E3)")
        if loc == "zh" and "：" not in title and ":" not in title:
            errors.append(f"{slug} meta zh title missing colon subtitle (E2)")
        if loc == "en" and ": " not in title:
            errors.append(f"{slug} meta en title missing colon subtitle (E2)")
        desc = meta[f"{loc}_desc"]
        if "DALL-E" in desc or "DALL·E 3" in desc:
            warnings.append(f"{slug} meta {loc} description mentions retired DALL-E")
        # at least 2 product-like tokens (comma separated)
        parts = re.split(r"[,、]", desc)
        products = [p.strip() for p in parts if len(p.strip()) > 2][:5]
        if len(products) < 2:
            warnings.append(f"{slug} meta {loc} description may lack 2 products (E4)")

    return errors, warnings


def main() -> int:
    print("=== audit-image-cluster-article-quality (strict) ===\n")
    all_errors: list[str] = []
    all_warnings: list[str] = []
    seen_meta: set[str] = set()

    for slug in SLUGS:
        if slug not in seen_meta:
            e, w = audit_meta(slug)
            all_errors.extend(e)
            all_warnings.extend(w)
            seen_meta.add(slug)
        for loc in ("zh", "en"):
            e, w = audit_slug(slug, loc)
            all_errors.extend(e)
            all_warnings.extend(w)

    if all_warnings:
        print(f"WARNINGS ({len(all_warnings)}):")
        for w in all_warnings:
            print(f"  - {w}")
        print()

    if all_errors:
        print(f"ERRORS ({len(all_errors)}):")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print("OK: no P0 errors")
    if all_warnings:
        print(f"({len(all_warnings)} warnings — strict mode would still pass P0)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
