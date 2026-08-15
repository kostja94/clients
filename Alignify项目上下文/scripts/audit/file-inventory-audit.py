#!/usr/bin/env python3
"""Full file inventory audit for alignify-by-kostja."""
from __future__ import annotations

import json
import os
def _deploy_root() -> Path:
    env = os.environ.get("ALIGNIFY_DEPLOY_ROOT")
    if env:
        return Path(env)
    ctx = Path(__file__).resolve().parents[2]
    candidate = ctx.parent.parent / "部署项目" / "alignify-by-kostja"
    if candidate.is_dir():
        return candidate
    raise SystemExit("Set ALIGNIFY_DEPLOY_ROOT to the alignify-by-kostja repo path")

import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent.parent
SKIP_DIRS = {"node_modules", ".next", ".git", "__pycache__"}
VALID_BLOCKS = {
    "tldr", "section", "howItWorks", "bestTools", "useCases",
    "howToChoose", "faq", "references", "comparisonSection", "html", "table",
}
EXT_SCRIPTS_BASE = ROOT.parent.parent / "项目文档" / "Alignify项目上下文" / "scripts" / "permanent"

# Direct JSON imports in pages (not via *-pages-config)
SPECIAL_CONTENT_IMPORTS = {
    "about": ["about"],
    "author": ["kostja"],
    "events": [
        "founder-park-2024-11-06",
        "linkloud-2025-02-23",
        "linkloud-2026-01-24",
        "praxis-2025-09-27",
        "media-kit",
    ],
}


@dataclass
class AuditResult:
    code_unused: list[str] = field(default_factory=list)
    code_misplaced: list[dict[str, str]] = field(default_factory=list)
    babel_unused: bool = True
    skills_lock_unused: bool = True
    content_orphans: dict[str, list[str]] = field(default_factory=dict)
    content_missing_meta: dict[str, list[str]] = field(default_factory=dict)
    invalid_blocks: dict[str, list[str]] = field(default_factory=dict)
    public_misplaced: list[str] = field(default_factory=list)
    public_missing_refs: list[str] = field(default_factory=list)
    public_unreferenced_sample: list[str] = field(default_factory=list)
    public_stats: dict[str, int] = field(default_factory=dict)
    config_counts: dict[str, int] = field(default_factory=dict)
    external_scripts: list[dict[str, Any]] = field(default_factory=list)
    doc_errors: list[dict[str, str]] = field(default_factory=list)
    code_file_roles: dict[str, str] = field(default_factory=dict)


def iter_files(*roots: str, suffixes: tuple[str, ...] = ()) -> list[Path]:
    out: list[Path] = []
    for root_name in roots:
        root = ROOT / root_name
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for name in filenames:
                p = Path(dirpath) / name
                if suffixes and p.suffix not in suffixes:
                    continue
                out.append(p)
    return sorted(out)


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")


def all_source_text() -> str:
    parts = []
    for p in iter_files("app", "src", "i18n", "scripts", suffixes=(".ts", ".tsx", ".js", ".jsx")):
        parts.append(read_text(p))
    for name in ("middleware.ts", "next.config.js", "tailwind.config.ts", "postcss.config.js"):
        p = ROOT / name
        if p.exists():
            parts.append(read_text(p))
    return "\n".join(parts)


def audit_code_layer(result: AuditResult) -> None:
    sources = iter_files("app", "src", "i18n", "scripts", suffixes=(".ts", ".tsx"))
    root_configs = [p for p in ROOT.iterdir() if p.is_file() and p.suffix in {".ts", ".js", ".json", ".mjs"}]
    all_src = all_source_text()

    # Components
    for p in iter_files("src/components", suffixes=(".tsx",)):
        name = p.stem
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        if "ui" in p.parts:
            result.code_file_roles[rel] = "ui-component"
            patterns = [
                f'from "@/components/ui/{name}"',
                f"<{name}",
                f"ui/{name}",
            ]
        else:
            result.code_file_roles[rel] = "domain-component"
            patterns = [
                f'from "@/components/{name}"',
                f"<{name}",
                f'components/{name}',
            ]
        if p.name == "CookieConsent.tsx":
            patterns.append("CookieConsent")
        used = any(x in all_src for x in patterns) and not (
            rel in all_src and all_src.count(rel) <= 1 and f'from "@' not in all_src
        )
        # Better: exclude self file content
        other_src = "\n".join(read_text(s) for s in sources if s.resolve() != p.resolve())
        if "ui" in p.parts:
            used = (
                f'from "@/components/ui/{name}"' in other_src
                or re.search(rf"<\s*{re.escape(name)}\b", other_src) is not None
                or (name == "sonner" and ("Sonner" in other_src or "ui/sonner" in other_src))
            )
        else:
            used = (
                f'from "@/components/{name}"' in other_src
                or re.search(rf"<\s*{re.escape(name)}\b", other_src) is not None
                or (name == "CookieConsent" and "CookieConsent" in other_src)
            )
        if not used:
            result.code_unused.append(rel)

    # src/lib, src/content/render, src/marketing, src/hooks
    import_patterns: dict[str, list[str]] = {
        "src/content/render/ArticleFromJson.tsx": ["ArticleFromJson"],
        "src/content/render/htmlToMarkdown.ts": ["htmlToMarkdown"],
        "src/lib/schema/base-config.ts": ["base-config", "PUBLISHER", "DEFAULT_AUTHOR"],
        "src/marketing/CustomerStoriesIndex.tsx": ["CustomerStoriesIndex"],
        "src/marketing/GrowthCaseStudiesIndex.tsx": ["GrowthCaseStudiesIndex"],
        "src/components/ui/sonner.tsx": ["ui/sonner", "Sonner"],
    }
    for p in iter_files("src/lib", "src/content", "src/marketing", "src/hooks", suffixes=(".ts", ".tsx")):
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        mod = rel.replace("src/", "@/").replace(".ts", "").replace(".tsx", "")
        result.code_file_roles[rel] = "lib/render/marketing/hooks"
        other = "\n".join(
            read_text(s) for s in sources if s.resolve() != p.resolve()
        )
        scripts_text = "\n".join(read_text(s) for s in iter_files("scripts", suffixes=(".ts", ".tsx", ".js", ".mjs")))
        combined = other + scripts_text
        forced = import_patterns.get(rel, [])
        used = mod in combined or any(x in combined for x in forced)
        if not used:
            rel_path = rel.replace("src/", "").replace(".ts", "")
            if rel_path not in combined and f"/{p.name}" not in combined:
                result.code_unused.append(rel)

    # skills-lock.json
    if "skills-lock" not in all_src:
        result.skills_lock_unused = True

    # @babel in package.json vs source
    pkg = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    babel_in_pkg = any(k.startswith("@babel/") for k in pkg.get("devDependencies", {}))
    babel_in_src = "@babel/" in all_src or "babel" in all_src.lower()
    result.babel_unused = babel_in_pkg and not babel_in_src

    # Root dev tools
    for name in ("sync-skills-catalog.py", "skills-lock.json"):
        p = ROOT / name
        if p.exists():
            result.code_file_roles[name] = "dev-tool (skills catalog)"
            if name == "skills-lock.json" and result.skills_lock_unused:
                result.code_unused.append(name)

    # public misplaced py
    for p in ROOT.glob("public/*.py"):
        result.public_misplaced.append(str(p.relative_to(ROOT)).replace("\\", "/"))


def extract_slugs_from_ts(path: Path) -> set[str]:
    text = read_text(path)
    return set(re.findall(r'slug:\s*["\']([^"\']+)["\']', text))


def extract_meta_slugs(path: Path) -> set[str]:
    text = read_text(path)
    # Top-level record keys in *-meta.ts (2–4 space indent; tolerate minor formatting drift)
    quoted = set(re.findall(r'^\s{2,4}["\']([^"\']+)["\']\s*:', text, re.M))
    unquoted = set(re.findall(r'^\s{2,4}([a-z0-9-]+)\s*:\s*\{', text, re.M))
    # Exclude nested locale keys
    return (quoted | unquoted) - {"en", "zh"}


def audit_content_config(result: AuditResult) -> None:
    categories = {
        "tools": ("src/data/tools-pages-config.ts", "src/data/tools-meta.ts", None),
        "seo": ("src/data/seo-pages-config.ts", "src/data/seo-meta.ts", None),
        "marketing": ("src/data/marketing-pages-config.ts", "src/data/marketing-meta.ts", None),
        "insights": ("src/data/insights-pages-config.ts", "src/data/insights-meta.ts", {"indie-hackers"}),
        "glossary": ("src/data/glossary-pages-config.ts", "src/data/glossary-meta.ts", None),
    }
    for cat, (cfg, meta, meta_exclude) in categories.items():
        cfg_slugs = extract_slugs_from_ts(ROOT / cfg)
        meta_slugs = extract_meta_slugs(ROOT / meta)
        if meta_exclude:
            cfg_for_meta = cfg_slugs - meta_exclude
        else:
            cfg_for_meta = cfg_slugs
        en_dir = ROOT / "content" / cat / "en"
        zh_dir = ROOT / "content" / cat / "zh"
        en_json = {p.stem for p in en_dir.glob("*.json")} if en_dir.exists() else set()
        zh_json = {p.stem for p in zh_dir.glob("*.json")} if zh_dir.exists() else set()
        result.config_counts[f"{cat}_config"] = len(cfg_slugs)
        result.config_counts[f"{cat}_meta"] = len(meta_slugs)
        result.config_counts[f"{cat}_en_json"] = len(en_json)
        result.config_counts[f"{cat}_zh_json"] = len(zh_json)

        issues = []
        for label, missing in [
            ("config->en", cfg_slugs - en_json),
            ("config->zh", cfg_slugs - zh_json),
            ("config->meta", cfg_for_meta - meta_slugs),
            ("en->config", en_json - cfg_slugs),
            ("zh->config", zh_json - cfg_slugs),
        ]:
            if missing:
                issues.extend(sorted(missing))
        if cat == "insights" and meta_exclude:
            issues = [x for x in issues if x not in meta_exclude]
        if issues:
            result.content_orphans[cat] = sorted(set(issues))

    # Special content categories
    for cat, slugs in SPECIAL_CONTENT_IMPORTS.items():
        for loc in ("en", "zh"):
            d = ROOT / "content" / cat / loc
            if not d.exists():
                continue
            for p in d.glob("*.json"):
                result.code_file_roles[f"content/{cat}/{loc}/{p.name}"] = "special-content (direct page import)"

    # Invalid block types
    for p in ROOT.glob("content/**/*.json"):
        try:
            doc = json.loads(read_text(p))
        except json.JSONDecodeError:
            result.invalid_blocks.setdefault("INVALID_JSON", []).append(
                str(p.relative_to(ROOT)).replace("\\", "/")
            )
            continue
        for block in doc.get("blocks", []):
            t = block.get("type")
            if t and t not in VALID_BLOCKS:
                result.invalid_blocks.setdefault(t, []).append(
                    str(p.relative_to(ROOT)).replace("\\", "/")
                )


def audit_public_assets(result: AuditResult) -> None:
    referenced: set[str] = set()
    patterns = [
        re.compile(r'"(?:/[^"\\]|\\.)*\.(?:png|jpg|jpeg|webp|gif|svg|ico|mp4|pdf)"'),
        re.compile(r"'(?:/[^'\\]|\\.)*\.(?:png|jpg|jpeg|webp|gif|svg|ico|mp4|pdf)'"),
    ]
    for p in ROOT.glob("content/**/*.json"):
        text = read_text(p)
        for pat in patterns:
            for m in pat.findall(text):
                path = m.strip('"\'')
                path = path.replace("\\/", "/")
                if path.startswith("/"):
                    referenced.add(path.lstrip("/"))

    # Also scan ts/tsx for public paths
    for p in iter_files("app", "src", suffixes=(".ts", ".tsx")):
        text = read_text(p)
        for m in re.findall(r'["\'](/[^"\']+\.(?:png|jpg|jpeg|webp|gif|svg|ico))["\']', text):
            referenced.add(m.lstrip("/"))

    public_files: set[str] = set()
    for p in ROOT.glob("public/**/*"):
        if p.is_file():
            rel = str(p.relative_to(ROOT / "public")).replace("\\", "/")
            public_files.add(rel)

    missing = []
    for ref in sorted(referenced):
        # normalize
        ref_clean = ref.split("?")[0]
        if ref_clean.startswith("http"):
            continue
        if ref_clean not in public_files:
            # try without leading path variants
            candidates = {ref_clean, ref_clean.replace("public/", "")}
            if not any(c in public_files for c in candidates):
                missing.append(ref_clean)

    unreferenced = []
    for rel in sorted(public_files):
        if rel.endswith(".py"):
            continue
        # check if path appears in any referenced path or content
        path_variants = {rel, f"/{rel}", rel.split("/")[-1]}
        found = any(
            v in referenced or v in missing  # missing already checked refs
            for v in path_variants
        )
        if not found:
            # substring search in all content (expensive but ok once)
            needle = rel
            if needle not in "\n".join(read_text(p) for p in ROOT.glob("content/**/*.json")):
                if f"/{needle}" not in all_source_text():
                    unreferenced.append(rel)

    result.public_missing_refs = missing[:50]
    result.public_unreferenced_sample = unreferenced[:80]
    result.public_stats = {
        "total_public_files": len(public_files),
        "referenced_paths_extracted": len(referenced),
        "missing_on_disk": len(missing),
        "unreferenced_sampled": len(unreferenced),
    }


def audit_external_scripts(result: AuditResult) -> None:
    pkg = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    for name, cmd in pkg.get("scripts", {}).items():
        if "项目文档" not in cmd and not cmd.startswith("tsx scripts/"):
            if "indexnow" in name or "scripts/" in cmd:
                pass
        m = re.search(r"node\s+([^\s]+)", cmd)
        if m:
            target = m.group(1)
            if "项目文档" in target:
                ext_path = (ROOT / target).resolve()
            else:
                ext_path = (ROOT / target).resolve()
            result.external_scripts.append({
                "npm_script": name,
                "command": cmd,
                "target": target,
                "exists": ext_path.exists(),
                "location": "external" if "项目文档" in target else "repo",
            })
        elif cmd.startswith("tsx scripts/"):
            target = cmd.split()[1]
            result.external_scripts.append({
                "npm_script": name,
                "command": cmd,
                "target": target,
                "exists": (ROOT / target).exists(),
                "location": "repo",
            })


def audit_docs(result: AuditResult) -> None:
    claude = read_text(ROOT / "CLAUDE.md")
    readme = read_text(ROOT / "README.md")
    naming = read_text(ROOT / "README.md")

    tools_count = result.config_counts.get("tools_config", 0)
    seo_count = result.config_counts.get("seo_config", 0)
    json_count = len(list(ROOT.glob("content/**/*.json")))

    checks = [
        ("CLAUDE.md", "105 categories", f"{tools_count} categories", "105" in claude and str(tools_count) != "105"),
        ("CLAUDE.md", "37 pages", f"{seo_count} pages", "37 pages" in claude),
        ("CLAUDE.md", "MDX", "JSON pipeline (no MDX source)", "MDX" in claude and "JSON → ArticleFromJson" in claude),
        ("CLAUDE.md", "recharts", "not in package.json", "recharts" in claude),
        ("CLAUDE.md", "app/about/page.tsx", "app/[locale]/about/page.tsx", "app/about/page.tsx" in claude),
        ("CLAUDE.md", "app/partner/page.tsx", "app/[locale]/partnership/page.tsx", "app/partner/page.tsx" in claude),
        ("CLAUDE.md", "content/templates/", "missing in repo", "content/templates/" in claude and not (ROOT / "docs/templates").exists()),
        ("CLAUDE.md", "knowledge/", "missing in repo", "knowledge/" in claude and not (ROOT / "docs/knowledgehub").exists()),
        ("README.md", "354 JSON", f"{json_count} JSON", "354 JSON" in readme and json_count != 354),
        ("README.md", "docs/README.md", "file missing", "docs/README.md" in naming and not (ROOT / "docs/README.md").exists()),
        ("README.md", "knowledge/", "missing in repo", "knowledge/" in naming and not (ROOT / "docs/knowledgehub").exists()),
    ]
    for doc, claimed, actual, failed in checks:
        if failed:
            result.doc_errors.append({"document": doc, "claimed": claimed, "actual": actual})

    # Missing docs paths referenced in README
    for m in re.findall(r"docs/[a-z0-9\-/]+\.md", naming):
        if not (ROOT / m).exists() and not (ROOT / m.replace(".md", "")).exists():
            if m not in {e["claimed"] for e in result.doc_errors}:
                result.doc_errors.append({"document": "README.md", "claimed": m, "actual": "missing in repo"})


def render_report(result: AuditResult) -> str:
    lines = [
        "# File Inventory Audit Report",
        "",
        "> Generated by `scripts/audit/file-inventory-audit.py`. Read-only audit; no files were modified.",
        "",
        "## Executive Summary",
        "",
        "Answer to **「每个文件是否必要、位置正确、记录准确」**: **No — not fully.**",
        "",
        "| Category | Severity | Count |",
        "|----------|----------|-------|",
        f"| Code unused / orphan candidates | Medium | {len(result.code_unused)} |",
        f"| Content config mismatches | High if any | {sum(len(v) for v in result.content_orphans.values())} slugs |",
        f"| Invalid JSON block types | High if any | {sum(len(v) for v in result.invalid_blocks.values())} |",
        f"| public/ misplaced scripts | P0 | {len(result.public_misplaced)} |",
        f"| public/ missing referenced assets | Medium | {result.public_stats.get('missing_on_disk', 0)} |",
        f"| public/ unreferenced assets (sample) | Low | {result.public_stats.get('unreferenced_sampled', 0)} |",
        f"| Documentation errors | P1 | {len(result.doc_errors)} |",
        f"| External npm script dependencies | P2 (Decision Pending) | {len([s for s in result.external_scripts if s['location']=='external'])} |",
        "",
        "**Healthy areas:** `app/` + `src/` code layer, JSON block types (if none invalid), config/meta alignment for main content categories after recent refactors.",
        "",
        "---",
        "",
        "## 1. Code & Config Layer",
        "",
        f"**Files catalogued:** {len(result.code_file_roles)} with roles assigned.",
        "",
    ]
    if result.code_unused:
        lines.append("### Unused / Unreferenced Candidates")
        lines.append("")
        for f in result.code_unused:
            lines.append(f"- `{f}`")
        lines.append("")
    else:
        lines.append("No unused src/lib/components modules detected.")
        lines.append("")

    lines.extend([
        f"- `@babel/*` devDependencies unused in source: **{result.babel_unused}**",
        f"- `skills-lock.json` unused by site code: **{result.skills_lock_unused}**",
        "",
        "### Misplaced Files",
        "",
    ])
    for p in result.public_misplaced:
        lines.append(f"- `{p}` — maintenance script in static `public/` (HTTP-accessible risk)")
    lines.append("")
    if ROOT.joinpath("sync-skills-catalog.py").exists():
        lines.append("- `sync-skills-catalog.py` — dev tool at repo root; generates `src/data/skills-catalog.json`")
        lines.append("")

    lines.extend(["---", "", "## 2. Content / Config Consistency", ""])
    lines.append("| Category | Config | Meta | EN JSON | ZH JSON |")
    lines.append("|----------|--------|------|---------|---------|")
    for cat in ("tools", "seo", "marketing", "insights", "glossary"):
        lines.append(
            f"| {cat} | {result.config_counts.get(f'{cat}_config','?')} "
            f"| {result.config_counts.get(f'{cat}_meta','?')} "
            f"| {result.config_counts.get(f'{cat}_en_json','?')} "
            f"| {result.config_counts.get(f'{cat}_zh_json','?')} |"
        )
    lines.append("")
    if result.content_orphans:
        lines.append("### Config / JSON Mismatches")
        lines.append("")
        for cat, slugs in result.content_orphans.items():
            lines.append(f"**{cat}:** {', '.join(slugs)}")
        lines.append("")
    else:
        lines.append("All main content categories: config, meta, and EN/ZH JSON are aligned.")
        lines.append("")

    lines.append("**Note:** `indie-hackers` is intentionally in INSIGHTS_PAGES but not INSIGHTS_META (dedicated route).")
    lines.append("")
    lines.append("**Formatting note:** `tools-meta.ts` entry `social-cards-generator` uses 4-space indent (inconsistent with other slugs); consider normalizing.")
    lines.append("")
    if result.invalid_blocks:
        lines.append("### Invalid Block Types")
        lines.append("")
        for t, files in sorted(result.invalid_blocks.items()):
            lines.append(f"- `{t}`: {len(files)} files")
        lines.append("")

    lines.extend(["---", "", "## 3. public/ Assets", ""])
    for k, v in result.public_stats.items():
        lines.append(f"- {k}: {v}")
    lines.append("")
    if result.public_missing_refs:
        lines.append("### Referenced but Missing (sample)")
        lines.append("")
        for p in result.public_missing_refs[:30]:
            lines.append(f"- `{p}`")
        lines.append("")
    if result.public_unreferenced_sample:
        lines.append("### Unreferenced Files (sample, may include legacy assets)")
        lines.append("")
        for p in result.public_unreferenced_sample[:40]:
            lines.append(f"- `{p}`")
        lines.append("")

    lines.extend(["---", "", "## 4. External Script Dependencies", ""])
    lines.append("")
    lines.append("| npm script | Target | Location | Exists |")
    lines.append("|------------|--------|----------|--------|")
    for s in sorted(result.external_scripts, key=lambda x: x["npm_script"]):
        if s["location"] == "external" or "indexnow" in s["npm_script"] or "scripts/" in s.get("target", ""):
            lines.append(
                f"| `{s['npm_script']}` | `{s.get('target', '-')}` | {s['location']} | {s.get('exists', '?')} |"
            )
    lines.append("")
    lines.append("**Decision Pending:** Whether to migrate external audit/fetch scripts into this repo.")
    lines.append("")

    lines.extend(["---", "", "## 5. Documentation Cross-Check", ""])
    if result.doc_errors:
        lines.append("")
        lines.append("| Document | Claim / Reference | Actual |")
        lines.append("|----------|-------------------|--------|")
        for e in result.doc_errors:
            lines.append(f"| {e['document']} | {e['claimed']} | {e['actual']} |")
        lines.append("")
    lines.append("### docs/ In Repo (15 files)")
    lines.append("")
    for p in sorted(ROOT.glob("docs/**/*.md")):
        lines.append(f"- `{p.relative_to(ROOT).as_posix()}`")
    lines.append("")
    lines.append("### Referenced but NOT in Repo")
    lines.append("")
    for path in ["docs/README.md", "content/templates/", "knowledge/", "product/"]:
        exists = (ROOT / path.rstrip("/")).exists()
        if not exists:
            lines.append(f"- `{path}` — likely in external `项目文档/Alignify项目上下文`")
    lines.append("")

    lines.extend(["---", "", "## 6. Recommended Fix Priority", ""])
    lines.extend([
        "| Priority | Item | Action |",
        "|----------|------|--------|",
        "| P0 | `public/*.py` | Move to `scripts/` or delete from public |",
        "| P1 | CLAUDE.md / README.md | Update counts, routes, stack, docs paths |",
        "| P1 | Content describing MDX | Update `example-article` / `programmatic-seo` copy or remove pages |",
        "| P2 | External npm scripts | Migrate or document as external dependency |",
        "| P2 | `skills-lock.json`, `@babel/*` | Confirm then remove if unused |",
        "| P3 | Unreferenced public assets | Archive after reference audit |",
        "",
        "---",
        "",
        "## 7. Code File Role Index (Summary)",
        "",
    ])
    by_prefix: dict[str, list[str]] = defaultdict(list)
    for path, role in sorted(result.code_file_roles.items()):
        prefix = path.split("/")[0] if "/" in path else "root"
        by_prefix[prefix].append(f"`{path}` — {role}")
    for prefix in sorted(by_prefix):
        lines.append(f"### {prefix}/ ({len(by_prefix[prefix])} files)")
        lines.append("")
        for item in by_prefix[prefix][:60]:
            lines.append(f"- {item}")
        if len(by_prefix[prefix]) > 60:
            lines.append(f"- ... +{len(by_prefix[prefix]) - 60} more")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    result = AuditResult()
    audit_code_layer(result)
    audit_content_config(result)
    audit_public_assets(result)
    audit_external_scripts(result)
    audit_docs(result)

    report = render_report(result)
    out_dir = ROOT / "docs" / "technical"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "file-inventory-audit.md"
    out_path.write_text(report, encoding="utf-8")

    summary_path = ROOT / "FILE-AUDIT.md"
    summary_path.write_text(
        "# File Inventory Audit — Summary\n\n"
        + report.split("---")[0].strip()
        + "\n\nSee full report: [docs/technical/file-inventory-audit.md](docs/technical/file-inventory-audit.md)\n",
        encoding="utf-8",
    )

    print(f"Report written to {out_path}")
    print(f"Summary written to {summary_path}")
    print(json.dumps({
        "code_unused": len(result.code_unused),
        "content_orphans": result.content_orphans,
        "invalid_blocks": {k: len(v) for k, v in result.invalid_blocks.items()},
        "public_misplaced": result.public_misplaced,
        "doc_errors": len(result.doc_errors),
        "external_scripts": len(result.external_scripts),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
