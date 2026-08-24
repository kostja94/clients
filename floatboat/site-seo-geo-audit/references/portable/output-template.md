# Audit Report Output Template

> Standard deliverable format for floatboat-site-seo-geo-audit runs.
> **Last updated**: 2026-08-20

---

## File Outputs

| Deliverable | Path | When |
|-------------|------|------|
| Human checklist (updated) | `floatboat/site-seo-geo-audit/floatboat-seo-geo-checklist.md` | Every full audit |
| Agent session report | Conversation using this template | Every run |
| Weekly handoff block | Paste into SEO weekly data package | Optional |

---

## Report Header

```markdown
# Floatboat SEO/GEO Audit Report

**Site**: https://floatboat.ai  
**Mode**: {full | delta | pre-launch}  
**Audit date**: YYYY-MM-DD  
**Auditor**: {agent / human}  
**Previous audit**: YYYY-MM-DD or none  
**Tools run**: crawl_probe.py, sitemap_diff.py, ai_ua_probe.py, …

---
```

---

## Executive Summary (3–5 sentences)

Cover:
1. Overall health (Green / Yellow / Red)
2. Top 3 P0 findings
3. GEO visibility baseline change (if prompt snapshot run)
4. Sitemap/index delta since last audit

---

## Scorecard

| Part | Name | Items checked | Pass | Warn | Fail | Pass rate |
|:----:|------|:-------------:|:----:|:----:|:----:|:---------:|
| 1 | Crawlability & SSR | | | | | |
| 2 | robots & AI crawlers | | | | | |
| 3 | Sitemap & indexing | | | | | |
| 4 | Meta & on-page | | | | | |
| 5 | Schema | | | | | |
| 6 | hreflang & /zh/ | | | | | |
| 7 | Extractability | | | | | |
| 8 | Agent-ready | | | | | |
| 9 | Internal links | | | | | |
| 10 | Entity & off-site | | | | | |
| 11 | Measurement | | | | | |

---

## P0 Actions (this month)

```markdown
| # | Finding | URL / scope | Fix owner | Evidence |
|---|---------|-------------|-----------|----------|
| 1 | | | Engineering / Content / SEO | curl output / screenshot |
```

---

## Findings by Part

Use consistent finding IDs: `{PART}-{SEQ}` e.g. `P3-001`

```markdown
### P3-001 — Sitemap missing /floatim

- **Severity**: P0
- **Tags**: [SEO] [Both]
- **Evidence**: `sitemap_diff.py` output; curl 200 https://floatboat.ai/floatim
- **Pass standard**: URL in sitemap.xml with lastmod
- **Recommendation**: Add to sitemap; submit GSC
- **Planned gap?**: No — page is live
```

---

## Planned Gaps (documented, not fail)

```markdown
| Item | Status | Notes |
|------|--------|-------|
| Skills Leaderboard | Not live | P0 product roadmap |
| /vs/claude-cowork | Using /alternatives/* instead | URL strategy decision pending |
```

---

## Appendix A — Response Snapshots

| URL | HTTP | Content-Type | Size (bytes) | Notes |
|-----|:----:|--------------|-------------:|-------|
| / | 200 | text/html | | |
| /robots.txt | 200 | text/plain | | |
| /sitemap.xml | 200 | application/xml | | |
| /llms.txt | | | | |

---

## Appendix B — Schema Extract

Paste JSON-LD summary from `schema_extract.py` for T0 pages.

---

## Appendix C — Combo Store Sample

| URL | title unique | bytes | words est | dup title group |
|-----|:------------:|------:|----------:|-----------------|

---

## Appendix D — GEO Prompt Snapshot (if run)

Link to filled baseline table from prompt-library.md.

---

## Weekly Report Handoff Block

```text
===AUDIT_OBSERVATIONS===
Audit date: YYYY-MM-DD
Mode: full

P0:
- [P0] {finding one-liner}
- [P0] {finding one-liner}

P1:
- [P1] {finding one-liner}

Planned gaps (not bugs):
- {gap item}

Next audit due: YYYY-MM-DD
===END===
```

---

## Checklist Update Instructions

After full audit, update `floatboat-seo-geo-checklist.md`:
1. Refresh **二、现状核对总表** status column
2. Update **Last updated** date in file header
3. Fill **十五、验证命令** appendix snapshots (or paste into **证据** columns per Part)
4. Revise **十四、P0 / P1 / P2 汇总**
5. Append row to **十六、审计历史**
