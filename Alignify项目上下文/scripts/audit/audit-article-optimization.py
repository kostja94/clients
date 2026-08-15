#!/usr/bin/env python3
"""Audit article optimization vs knowledge blocks."""
import json, os, re
from pathlib import Path

ARTICLE_DIR = str(Path(__file__).resolve().parents[2].parent.parent / "部署项目" / "alignify-by-kostja" / "content" / "tools" / "en")
KB_DIR = str(Path(__file__).resolve().parents[2] / "docs" / "knowledgehub" / "tools")

def extract_signals(text):
    s = {}
    s["quantified"] = len(re.findall(r'\d+%|\$\d+[\.\d]*[MBK]|\d+\.\d+\s*billion|\d+\.\d+\s*million|\d+,\d{3}', text))
    s["named_src"] = len(re.findall(r'(?i)G2|Reddit|Product.Hunt|Trustpilot|Gartner|Forrester|arXiv|Veracode|OWASP|CVE-|Apiiro|Fortune|McKinsey|a16z|Sequoia|TechCrunch|Bloomberg|GitHub.*stars', text))
    s["has_market"] = bool(re.search(r'(?i)(billion|million).*market|valuation|ARR|MRR|CAGR|market.size', text))
    s["has_risk"] = bool(re.search(r'(?i)risk|compliance|regulation|privacy|security.*audit|bias.*audit|ethical|GDPR|SOC.2|legal', text))
    s["has_pricing"] = bool(re.search(r'\$\d+[\.\d]*\s*(/|per).*(month|year|user)', text))
    s["is_generic"] = len(re.findall(r'(?i)wide.range|various.tools|cutting.edge|innovative.solution|robust|seamless|comprehensive.suite|state.of.the.art', text)) > 3 and s["quantified"] < 3
    s["score"] = (3 if s["quantified"] >= 5 else 0) + (3 if s["named_src"] >= 2 else 0) + (2 if s["has_market"] else 0) + (1 if s["has_risk"] else 0) + (1 if s["has_pricing"] else 0) - (5 if s["is_generic"] else 0)
    return s

results = {"OPTIMIZED": [], "PARTIALLY": [], "KB_RICH_THIN": [], "NEEDS_WORK": [], "STUB": [], "UNOPTIMIZED": []}

for fname in sorted(os.listdir(ARTICLE_DIR)):
    if not fname.endswith('.json'):
        continue
    slug = fname.replace('.json', '')
    with open(os.path.join(ARTICLE_DIR, fname), 'r', encoding='utf-8') as f:
        article = json.load(f)
    text = json.dumps(article)
    art_kb = round(len(text)/1024, 1)

    kb_path = os.path.join(KB_DIR, f"{slug}.md")
    kb_size = os.path.getsize(kb_path) if os.path.exists(kb_path) else 0
    kb_kb = round(kb_size/1024, 1)

    s = extract_signals(text)

    if s["score"] >= 7:
        cat = "OPTIMIZED"
    elif s["score"] >= 4:
        cat = "PARTIALLY"
    elif s["score"] >= 0 and kb_size >= 10240:
        cat = "KB_RICH_THIN"
    elif s["score"] >= 0 and 2000 <= kb_size < 10240:
        cat = "NEEDS_WORK"
    elif kb_size < 2000:
        cat = "STUB"
    else:
        cat = "UNOPTIMIZED"

    results[cat].append((slug, art_kb, kb_kb, s["score"], s["quantified"], s["named_src"]))

for cat in ["OPTIMIZED", "PARTIALLY", "KB_RICH_THIN", "NEEDS_WORK", "STUB", "UNOPTIMIZED"]:
    items = results[cat]
    if cat == "OPTIMIZED":
        label = "OPTIMIZED - KB research incorporated (strong data, named sources, market intel)"
    elif cat == "PARTIALLY":
        label = "PARTIALLY OPTIMIZED - Some KB research present, gaps remain"
    elif cat == "KB_RICH_THIN":
        label = "KB RICH / ARTICLE THIN - KB has deep research, article doesn't use it (HIGH PRIORITY)"
    elif cat == "NEEDS_WORK":
        label = "NEEDS WORK - Both KB and article coverage thin"
    elif cat == "STUB":
        label = "STUB - KB is sub-1KB placeholder, article generic"
    else:
        label = "UNOPTIMIZED - KB exists but article appears generic/outdated"
    print(f"\n## {label} ({len(items)} articles)")
    print(f"{'Slug':<30} {'Art':>6} {'KB':>6} {'Sc':>3} {'Dat':>4} {'Src':>4}")
    print("-" * 60)
    for slug, ak, kk, sc, qt, ns in sorted(items, key=lambda x: -x[3]):
        print(f"{slug:<30} {ak:>5}KB {kk:>5}KB {sc:>3} {qt:>4} {ns:>4}")

total = sum(len(v) for v in results.values())
print(f"\n{'='*60}")
print(f"SUMMARY ({total} articles)")
for cat, label in [("OPTIMIZED", "Fully optimized"), ("PARTIALLY", "Partially optimized"), ("KB_RICH_THIN", "KB rich, article thin (P0)"), ("NEEDS_WORK", "Both need work"), ("STUB", "KB stub"), ("UNOPTIMIZED", "Unoptimized")]:
    print(f"  {label:<30} {len(results[cat]):>3}")
