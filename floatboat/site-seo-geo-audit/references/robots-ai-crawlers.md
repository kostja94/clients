# Floatboat robots.txt & AI Crawler Policy

> Crawler governance for floatboat.ai audits.
> **Last updated**: 2026-08-20 (live robots.txt verified)

---

## Live robots.txt Facts (2026-08-20)

Floatboat uses **Cloudflare-managed** robots rules. Key live lines:

```
User-agent: *
Content-Signal: search=yes,ai-train=no,use=reference
Allow: /

User-agent: Google-Extended
Disallow: /

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: meta-externalagent
Disallow: /

User-agent: Amazonbot
Disallow: /

User-agent: Applebot-Extended
Disallow: /

Sitemap: https://floatboat.ai/sitemap.xml
```

**Not explicitly named**: OAI-SearchBot, PerplexityBot, Claude-SearchBot — they inherit `User-agent: * Allow: /`.

---

## Audit Implications

| Finding | Severity | Notes |
|---------|:--------:|-------|
| Content-Signal present | ✅ Pass | Format differs from template — no explicit `ai-input=yes` |
| Google-Extended Disallow | ⚠️ P1 | Team may want Allow for Gemini-side GEO |
| Training bots Disallow | ✅ Expected | GPTBot, ClaudeBot, etc. |
| `*` Allow | ✅ Pass | Search/citation bots not blocked at HTTP layer |
| HTTP 200 for Disallow bots | ℹ️ Info | robots Disallow ≠ 403; use robots parser + policy doc |

---

## Recommended vs Live Gap

If GEO strategy requires broader AI indexing, team may change:

| Item | Live | GEO-oriented target |
|------|------|---------------------|
| Google-Extended | Disallow | Allow |
| Content-Signal | `search=yes,ai-train=no,use=reference` | Add `ai-input=yes` if policy allows |
| Explicit OAI-SearchBot Allow | Implicit via `*` | Optional explicit stanza for clarity |

---

## AI User-Agent Reference

| User-Agent | Operator | Live effective access |
|------------|----------|----------------------|
| **OAI-SearchBot** | OpenAI Search | Allow (via `*`) |
| **PerplexityBot** | Perplexity | Allow (via `*`) |
| **Claude-SearchBot** | Anthropic Search | Allow (via `*`) |
| **GPTBot** | OpenAI Training | **Disallow** |
| **ClaudeBot** | Anthropic Training | **Disallow** |
| **Google-Extended** | Google AI extension | **Disallow** |
| **Googlebot** | Google Search | Allow (via `*`) |

---

## Audit Checks

| # | Check | Pass | Method | P |
|---|-------|------|--------|---|
| R1 | robots.txt 200 text/plain | ✅ | curl -sI | P0 |
| R2 | Sitemap declaration | Points to floatboat.ai/sitemap.xml | Read body | P0 |
| R3 | Content-Signal present | Any valid Content-Signal line | grep | P1 |
| R4 | Google-Extended policy documented | Allow or Disallow + rationale | grep + decision log | P1 |
| R5 | Training bots Disallow | GPTBot, ClaudeBot | grep | P1 |
| R6 | Search bots not HTTP-blocked | ai_ua_probe.py 200 for OAI-SearchBot, PerplexityBot | tool | P0 |
| R7 | Sitemap has no 404 URLs | workflowstore must not 404 | sitemap_diff --probe-dead | P0 |

---

## Verification Commands

```powershell
curl -s https://floatboat.ai/robots.txt
curl -s https://floatboat.ai/robots.txt | findstr /i "content-signal google-extended gptbot perplexity"
python tools/ai_ua_probe.py
python tools/sitemap_diff.py --probe-dead
```

---

## Decision Log Template

| Decision | Live (2026-08-20) | Target | Owner |
|----------|-------------------|--------|-------|
| Content-Signal | search=yes,ai-train=no,use=reference | | |
| Google-Extended | Disallow | Allow? | |
| llms.txt | 404 | Deploy | |
