# Floatboat Site SEO/GEO Audit — Project Config

> **Self-contained project facts for audit.** Agent reads this in Phase 0 only.
> **Last updated**: 2026-08-20 (live-verified against floatboat.ai same day)

---

## Live Baseline Snapshot (2026-08-20)

> Re-verify on every audit. Historical counts from 2026-06 (~620 sitemap URLs) are **obsolete**.

| Signal | Live state (2026-08-20) |
|--------|-------------------------|
| **Sitemap URL count** | **31** (single urlset — not index) |
| **Sitemap blog posts** | **0** (only `/blog` hub) — posts live but unlisted |
| **Sitemap combo details** | **0** (only `/combostore` hub) — details live but unlisted |
| **Sitemap dead URL** | `/workflowstore` → **404** (listed in sitemap) |
| **llms.txt** | **404** |
| **floatcup-2026** | **404** (campaign removed) |
| **Route** | `/combostore` ✅ · `/combo-store` ❌ 404 |
| **New surfaces** | `/marketplace` ✅ · `/showcases` ✅ · `/workflowstore` ❌ |
| **/zh/** | **200** · `/zh/pricing` **200** |
| **Content-Signal** | **Present** in robots.txt (Cloudflare managed) |
| **Google-Extended** | **Disallow** in robots.txt |
| **Home schema** | Organization, WebSite, SoftwareApplication, FAQPage ✅ |
| **Pricing schema** | Missing SoftwareApplication + FAQPage on `/pricing` (live) |
| **Blog schema** | `/blog/calendar-driven-ai-vs-chat-ai` missing BlogPosting (live) |
| **Org schema gap** | legalName + sameAs missing sitewide (live) |
| **Integrations copy** | **3,500+** tools (homepage) |
| **Product narrative** | Calendar-Driven Proactive Agent OS + Combo Store + **Workflow Store** + FloatIM |

## Domains

| Domain | Role | Audit scope |
|--------|------|-------------|
| **https://floatboat.ai** | Primary marketing + product site (canonical) | Full audit |
| **https://im.floatboat.ai** | FloatIM product app (sister product) | Cross-domain entity check only |
| **https://floatboat.lovable.app** | Dev preview | Out of scope unless user requests |

---

## Brand & Entity

| Field | Value |
|-------|-------|
| Product name | Floatboat |
| Legal entity | AOE Tech Labs Limited |
| Copyright | © 2026 AOE Tech Labs Limited |
| Founder | Tan Shaoqing (谭少卿) |
| Founded | 2025-11 |
| Funding | Seed ~$2M — HongShan (Sequoia China seed) + Weiguang Ventures, 2026-03 |
| Primary category | Calendar-Driven AI / Proactive Agent OS / Agentic Calendar |
| One-line (EN) | The proactive agent OS where your calendar becomes the runtime — agents prep before meetings, execute on deadlines, and follow up after, automatically. |
| Target audience (EN) | solopreneur / solo founder / creator / small business owner / 2–5 person studio |
| Target audience (ZH) | 一人公司 / 单人创始人 |
| Integrations claim | 3,500+ tools via MCP + IACT |
| Platforms | Mac, Windows desktop app |

---

## Language Strategy

| Site | Path | Primary keywords | Avoid as EN head terms |
|------|------|------------------|------------------------|
| English (default) | `/` (no prefix) | solopreneur, solo founder, Calendar-Driven AI, Proactive Agent OS | "one-person company" as main EN keyword |
| Chinese | `/zh/` | 一人公司, 单人创始人, 日历驱动 AI | Machine-translated thin pages |

---

## Site Scale

> **Always verify live** via `tools/sitemap_diff.py --probe-dead`. Do not assume historical counts.

| Segment | Historical (2026-06, obsolete) | Live expectation (2026-08-20) |
|---------|------:|---|
| Sitemap total | ~620 | **~31** — re-count each audit |
| Blog posts in sitemap | ~87 | **Often 0** — hub only; posts may still be live |
| Combo Store details in sitemap | ~506 | **Often 0** — hub only; details may still be live |
| Alternatives in sitemap | 13 | 13 ✅ |
| Use Cases (live, often sitemap gap) | 5 | 5 pages HTTP 200 |
| Product landing (live, often sitemap gap) | integrations, models, floatim | HTTP 200; check sitemap |
| Removed | floatcup-2026 | **404** — do not audit as live |
| New (2026-08) | — | `/marketplace`, `/showcases` in sitemap; `/workflowstore` **404 bug** |

**Critical indexing risk**: When sitemap lists only hubs, run spot checks on live `/blog/{slug}` and `/combostore/{id}` even if absent from sitemap.

---

## Core Positioning (audit copy alignment)

**Hero messaging (EN)**:
- *The Proactive Agent OS that Runs Work from the Calendar*
- *Calendar-Driven AI — Not Another Chat Box*
- *Stop Prompting. Start Your Calendar.*

**Differentiation axis**: Calendar-Driven (proactive, event-triggered) vs Chat-Based (reactive, prompt-triggered).

| Dimension | Chat-Based AI | Floatboat |
|-----------|---------------|-----------|
| Trigger | User types prompt | Calendar events |
| Context | Session resets | Per-event Agent Workspace persists |
| Presence | Browser tab | Desktop app (Mac + Windows) + FloatIM |

---

## Planned Gaps (doc vs live — flag in every audit)

| Planned route / feature | Live state (2026-08-20) | Priority |
|-------------------------|------------------------|----------|
| `/vs/claude-cowork` comparison hub | Use `/alternatives/*` (13 pages live) | P1 — URL strategy |
| Skills Leaderboard | Not confirmed live | P0 |
| `/combostore/submit` | Not confirmed — hub at `/combostore` only | P1 |
| FloatIM sub-routes `/floatim/protocols`, `/floatim/vs-floatboat` | Only `/floatim` live | P1 |
| `/zh/use-cases/one-person-company` | `/zh/` + `/zh/pricing` live; full zh matrix TBD | P1 |
| **Workflow Store** `/workflowstore` | In sitemap but **404** | **P0 bug** |
| `/marketplace` | Live + in sitemap | Verify SEO |
| `/showcases` | Live + in sitemap | Verify SEO |
| floatcup-2026 campaign | **Removed (404)** | — |
| Blog posts + combo details in sitemap | **Missing** (hubs only) | **P0 indexing** |
| Organization legalName + sameAs in schema | Missing sitewide | P1 |
| Pricing FAQPage + SoftwareApplication schema | Missing on `/pricing` | P0 |
| Blog BlogPosting schema | Missing on sampled pillar post | P0 |
| llms.txt | **404** | P1 |

---

## AI Crawler Policy

**Live robots.txt (2026-08-20)** — Cloudflare-managed block plus site rules:

| User-agent | Live policy |
|------------|-------------|
| `*` | Allow `/` + `Content-Signal: search=yes,ai-train=no,use=reference` |
| Google-Extended, GPTBot, ClaudeBot, CCBot, Bytespider, … | **Disallow** |
| OAI-SearchBot / PerplexityBot | **Not named** — fall under `*` Allow |

Audit notes:
- **Content-Signal already deployed** — verify `ai-input` intent if team wants explicit `ai-input=yes`
- **Google-Extended Disallow** — limits Gemini training/index extension; GEO team may want Allow
- robots Disallow ≠ HTTP 403 — probe with `ai_ua_probe.py` returns 200 even for Disallow bots

**Recommended target** (if team opts into broader GEO):

```
Content-Signal: search=yes, ai-input=yes, ai-train=no
User-agent: Google-Extended
Allow: /
```

---

## Key Routes Reference

### T0 — Critical

`/`, `/pricing`, `/download`, `/about`, `/combostore`, `/marketplace`

### T1 — High-intent landing

`/alternatives`, `/alternatives/*`, `/use-cases`, `/use-cases/*`, `/floatim`, `/integrations`, `/models`, `/showcases`, `/ai-agent-workspace`, `/app`

**Removed / broken (do not treat as live)**:
- `/floatcup-2026` → 404
- `/workflowstore` → 404 (still wrongly listed in sitemap)
- `/combo-store` → 404 (correct path is `/combostore`)

### T2 — Blog clusters (priority samples)

| Cluster | Example slugs |
|---------|---------------|
| Calendar-Driven | `calendar-driven-ai-vs-chat-ai`, `ai-scheduling-agent`, `ai-meeting-preparation`, `ai-follow-up-automation`, `best-ai-scheduling-assistants` |
| Solopreneur | `ai-agent-solo-operators`, `ai-workflow-for-solo-founders`, `how-one-person-businesses-work-like-a-team-with-ai` |
| Claude Cowork alt | `claude-code-non-developers-solo-operators`, `what-are-claude-managed-agents` |
| FloatIM | `introducing-floatim` |

### Pricing facts (verify live — do not trust this table without curl)

Audit must confirm against live `/pricing` + FAQ. Record as-of date in findings.

---

## Measurement Integration

| System | Purpose in audit |
|--------|------------------|
| GSC | Index coverage, queries, pages — optional input bundle |
| GA4 | AI referrer channel regex (see `references/prompt-library.md` § GA4 AI Referrer Regex) |
| Bing Webmaster | Sitemap + AI Performance dashboard CSV |
| Manual prompt sampling | 35 prompts in `references/prompt-library.md` |

**Handoff to weekly report**: Findings formatted as `===AUDIT_OBSERVATIONS===` block (see `references/portable/output-template.md`).

---

## Sister Product — FloatIM

| Field | Value |
|-------|-------|
| Product | FloatIM — Agent-Native IM |
| App URL | https://im.floatboat.ai |
| Site landing | https://floatboat.ai/floatim |
| Relationship | Floatboat = local desktop workspace; FloatIM = network / collaboration layer |
| Category keywords | agent-native messaging, multi-agent collaboration, chat with AI agents |

See `references/floatim-cross-domain.md` for audit rules.

---

## Forbidden External Reads

Agent running this skill **must not** read files outside:

```
floatboat/site-seo-geo-audit/
floatboat/site-seo-geo-audit/floatboat-seo-geo-checklist.md   ← output target only
```

All domain knowledge is in this skill's `references/`.
