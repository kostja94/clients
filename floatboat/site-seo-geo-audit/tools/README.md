# Floatboat Audit Tools

Python utilities for `floatboat-site-seo-geo-audit`. **No third-party dependencies** — stdlib only.

**Requirements**: Python 3.10+

---

## Scripts

| Script | Purpose | Example |
|--------|---------|---------|
| `crawl_probe.py` | HTTP status, body size, H1, JSON-LD presence | `python crawl_probe.py --tier t0+t1` |
| `sitemap_diff.py` | Sitemap count + gap URL detection | `python sitemap_diff.py` |
| `ai_ua_probe.py` | AI crawler user-agent 403 check | `python ai_ua_probe.py` |
| `schema_extract.py` | JSON-LD types + missing fields | `python schema_extract.py` |
| `combo_store_sample.py` | Random combo detail sample | `python combo_store_sample.py -n 30 --seed 20260820` |

---

## Recommended Audit Pipeline

```powershell
cd floatboat/site-seo-geo-audit/tools

python crawl_probe.py --tier t0+t1 --json > ../audit-artifacts/crawl.json
python sitemap_diff.py --json > ../audit-artifacts/sitemap.json
python ai_ua_probe.py --json > ../audit-artifacts/ai_ua.json
python schema_extract.py --json > ../audit-artifacts/schema.json
python combo_store_sample.py -n 30 --seed 20260820 --json > ../audit-artifacts/combo.json
```

Create `audit-artifacts/` locally; do not commit unless user requests.

---

## Exit Codes

| Code | Meaning |
|:----:|---------|
| 0 | All checks in script passed thresholds |
| 1 | One or more failures detected |
| 2 | Could not fetch sitemap or fatal error |

Agent should paste tool output into audit report appendices.

---

## Notes

- Tools hit **production** floatboat.ai — rate-limit yourself; do not loop 500+ URLs in one run.
- `combo_store_sample.py` fetches sitemap once, then samples — safe for routine audits.
- For full meta duplicate scan across all live URLs, use Screaming Frog (sitemap may only list ~31 hub URLs).
