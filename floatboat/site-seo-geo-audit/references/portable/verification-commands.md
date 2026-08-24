# Verification Commands — Floatboat Audit

> Copy-paste commands for Windows PowerShell and cross-platform curl.
> **Last updated**: 2026-08-20

---

## Quick Health Check (5 minutes)

```powershell
# robots
curl -sI https://floatboat.ai/robots.txt

# sitemap
curl -sI https://floatboat.ai/sitemap.xml

# homepage size
curl -s https://floatboat.ai/ | Measure-Object -Character

# llms.txt
curl -sI https://floatboat.ai/llms.txt

# selfware markdown
curl -sI https://floatboat.ai/selfware.md
```

---

## SSR / SPA Shell Detection

```powershell
# Compare body size — shell usually < 10KB
curl -s https://floatboat.ai/pricing | Measure-Object -Character
curl -s https://floatboat.ai/combostore | Measure-Object -Character
curl -s https://floatboat.ai/combostore/bracket-boss-1nKR69 | Measure-Object -Character

# Check for root div only (bad sign)
curl -s https://floatboat.ai/pricing | Select-String -Pattern "<h1"
```

---

## AI User-Agent Probes

```powershell
curl -sI -A "OAI-SearchBot" https://floatboat.ai/
curl -sI -A "PerplexityBot" https://floatboat.ai/blog/ai-scheduling-agent
curl -sI -A "Claude-SearchBot" https://floatboat.ai/pricing
curl -sI -A "GPTBot" https://floatboat.ai/
```

Or run batch:

```powershell
python tools/ai_ua_probe.py --urls https://floatboat.ai/ https://floatboat.ai/pricing https://floatboat.ai/blog/calendar-driven-ai-vs-chat-ai
```

---

## robots.txt Content

```powershell
curl -s https://floatboat.ai/robots.txt
curl -s https://floatboat.ai/robots.txt | findstr /i "perplexity openai claude google-extended content-signal sitemap gptbot"
```

---

## Schema / JSON-LD

```powershell
curl -s https://floatboat.ai/ | findstr /i "application/ld+json"
curl -s https://floatboat.ai/pricing | findstr /i "FAQPage SoftwareApplication"
```

Or:

```powershell
python tools/schema_extract.py --urls https://floatboat.ai/ https://floatboat.ai/pricing
```

---

## Sitemap Analysis

```powershell
# Count URLs
curl -s https://floatboat.ai/sitemap.xml | findstr /i "<loc>" | Measure-Object -Line

# Check specific URL present
curl -s https://floatboat.ai/sitemap.xml | findstr /i "floatim use-cases integrations"
```

Or:

```powershell
python tools/sitemap_diff.py
```

---

## Meta Spot Check

```powershell
curl -s https://floatboat.ai/ | findstr /i "<title>"
curl -s https://floatboat.ai/ | findstr /i "description"
curl -s https://floatboat.ai/alternatives/chatgpt-alternative | findstr /i "<title>"
```

---

## Sitemap Gap URLs (must verify present)

```powershell
$gap = @(
  "/use-cases",
  "/use-cases/for-solopreneur",
  "/integrations",
  "/models",
  "/floatim",
  "/zh/",
)
# Removed — do not probe: floatcup-2026 (404)
$sm = curl -s https://floatboat.ai/sitemap.xml
foreach ($p in $gap) {
  if ($sm -match [regex]::Escape($p)) { Write-Host "OK $p" } else { Write-Host "MISSING $p" }
}
```

---

## Full Tool Pipeline

From skill directory:

```powershell
cd floatboat/site-seo-geo-audit

python tools/crawl_probe.py --tier t0
python tools/sitemap_diff.py
python tools/ai_ua_probe.py
python tools/schema_extract.py --tier t0
python tools/combo_store_sample.py --n 30 --seed 20260820
```

---

## External Validators (manual)

| Tool | URL | Use for |
|------|-----|---------|
| Rich Results Test | https://search.google.com/test/rich-results | Schema errors |
| URL Inspection | Google Search Console | Index status |
| PageSpeed Insights | https://pagespeed.web.dev/ | T0 CWV spot check |
| isitagentready | https://isitagentready.com/ | Agent-ready score (optional) |
