# Floatboat Agent-Ready Checklist (llms.txt & AI Discovery)

> Agent-ready enhancements for generative engines and AI crawlers.
> Floatboat site type: **SaaS + Content/Blog hybrid** — prioritize discoverability and extractable facts over protocol theater.
> **Last updated**: 2026-08-20

---

## Relevance Tiers

| Mark | Meaning |
|:----:|---------|
| 🔴 | Strongly recommended for Floatboat |
| 🟡 | Optional enhancement |
| ⚪ | Not applicable — do not deploy for score alone |

---

## Checklist

### Discoverability

| # | Item | Tier | Pass standard | P |
|---|------|:----:|---------------|---|
| A1 | robots.txt + sitemap | 🔴 | Both accessible; sitemap in robots | P0 |
| A2 | `/llms.txt` exists | 🔴 | HTTP 200; text/plain | **404 live (2026-08-20)** | P1 |
| A3 | llms.txt links use floatboat.ai | 🔴 | No wrong-domain links | P1 |
| A4 | llms.txt content current | 🔴 | Product facts, pricing link, key routes match live site | P1 |
| A5 | Link response header | 🟡 | `Link: <https://floatboat.ai/sitemap.xml>; rel="sitemap"` on homepage | P2 |
| A6 | RSS/Atom alternate | 🟡 | `<link rel="alternate" type="application/rss+xml">` for blog | P2 |

### Content Consumption

| # | Item | Tier | Pass standard | P |
|---|------|:----:|---------------|---|
| B1 | `/selfware.md` serves readable content | 🔴 | 200; Markdown or HTML with full text (live: HTML ~28KB) | P1 |
| B2 | Markdown content negotiation | 🟡 | `Accept: text/markdown` returns clean MD on key pages | P2 |
| B3 | `<link rel="alternate" type="text/markdown">` | 🟡 | In HTML head for blog posts | P2 |
| B4 | `/sitemap.md` human-readable map | 🟡 | Optional parallel to XML sitemap | P2 |

### Bot Policy

| # | Item | Tier | Pass standard | P |
|---|------|:----:|---------------|---|
| C1 | Content-Signal in robots.txt | 🔴 | **Live ✅** — verify values match policy | P1 |
| C2 | Search bots Allow | 🔴 | Per robots-ai-crawlers.md | P0 |

### Protocol Discovery (usually ⚪ for Floatboat)

| # | Item | Tier | Notes |
|---|------|:----:|-------|
| D1 | MCP Server Card | ⚪ | Only if public MCP server exists |
| D2 | `/.well-known/api-catalog` | ⚪ | Only if public API catalog |
| D3 | Agent Skills manifest | ⚪ | `/skill.md` optional; must be real Markdown if deployed |
| D4 | x402 / commerce protocols | ⚪ | Not applicable |

**Rule**: Never deploy empty MCP cards, fake OAuth, or placeholder API catalogs.

---

## Recommended llms.txt Template

Save at `https://floatboat.ai/llms.txt`:

```markdown
# Floatboat

> Calendar-driven proactive agent OS for solopreneurs. Desktop app (Mac + Windows) where your calendar becomes the runtime — agents prep before meetings, execute on deadlines, and follow up after.

## Key Facts

- Product: Floatboat — Proactive Agent OS
- Company: AOE Tech Labs Limited
- Category: Calendar-Driven AI / Agentic Calendar
- Platforms: macOS, Windows
- Integrations: 3,500+ tools via MCP + IACT
- Stores: Combo Store (`/combostore`) + Workflow Store (homepage CTA — verify live route)
- Models: DeepSeek, MiniMax, GLM, Kimi, GPT, Claude, Gemini — built in, no API keys
- Sister product: FloatIM (Agent-Native IM) — https://im.floatboat.ai

## Primary Pages

- Home: https://floatboat.ai/
- Pricing: https://floatboat.ai/pricing
- Download: https://floatboat.ai/download
- About: https://floatboat.ai/about
- Combo Store (Agent Skills): https://floatboat.ai/combostore
- Marketplace: https://floatboat.ai/marketplace
- Showcases: https://floatboat.ai/showcases
- Alternatives hub: https://floatboat.ai/alternatives
- Use Cases: https://floatboat.ai/use-cases
- Integrations: https://floatboat.ai/integrations
- Models: https://floatboat.ai/models
- FloatIM: https://floatboat.ai/floatim
- Blog: https://floatboat.ai/blog

## Definition Pages (for AI citation)

- What is Calendar-Driven AI: https://floatboat.ai/blog/calendar-driven-ai-vs-chat-ai
- AI Scheduling Agent: https://floatboat.ai/blog/ai-scheduling-agent
- Claude Cowork alternative context: https://floatboat.ai/alternatives/chatgpt-alternative

## Optional

- Selfware protocol: https://floatboat.ai/selfware.md
- Sitemap: https://floatboat.ai/sitemap.xml

## Contact

- Website: https://floatboat.ai
- Support: (fill from live footer)

Last updated: YYYY-MM-DD
```

**Audit rules for llms.txt**:
1. Every URL must return 200 HTML (or text for selfware.md)
2. Blog list in llms.txt must ⊆ sitemap blog URLs
3. Stats (integrations count, model list) must match live marketing copy
4. Update `Last updated` on each quarterly audit

---

## isitagentready.com Usage

Optional external scan: https://isitagentready.com/

| Score | Floatboat interpretation |
|-------|-------------------------|
| 0–1 | Missing basics — fix robots/sitemap first |
| 2 | Add Content-Signal |
| 3 | Add llms.txt + Markdown paths |
| 4+ | Only pursue if real MCP/API exists |

Record score in audit appendix — do not treat as KPI.

---

## Verification

```powershell
curl -sI https://floatboat.ai/llms.txt
curl -s https://floatboat.ai/llms.txt
curl -sI https://floatboat.ai/selfware.md
curl -sI https://floatboat.ai/ | findstr /i "link"
```
