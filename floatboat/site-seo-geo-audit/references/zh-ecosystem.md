# Floatboat Chinese Site & Ecosystem Audit

> `/zh/` SEO rules and Chinese generative engine sampling.
> **Last updated**: 2026-08-20

---

## Language Split Strategy

| Dimension | English (`/`) | Chinese (`/zh/`) |
|-----------|---------------|------------------|
| Primary audience keyword | solopreneur, solo founder | 一人公司, 单人创始人 |
| Avoid | "one-person company" as EN head term | Machine-translated EN copy |
| Traffic note | Google Search primary | Baidu, Direct, social — Google Search contribution low |
| hreflang | Pair EN ↔ ZH where content equivalent | x-default → EN recommended |

---

## `/zh/` Audit Checks

| # | Check | Pass | P |
|---|-------|------|---|
| Z1 | `/zh/` or `/zh` resolves (200 or 301 to canonical) | Consistent | P0 |
| Z2 | Chinese homepage has unique title/description | Not duplicate EN | P1 |
| Z3 | Core value prop in Chinese | 日历驱动 / 主动式 Agent / 一人公司 | P1 |
| Z4 | hreflang en ↔ zh-CN on paired pages | Mutual reference | P1 |
| Z5 | x-default points to EN or strategic choice documented | | P1 |
| Z6 | Content quality | Native Chinese, not empty MT | P1 |
| Z7 | `/zh/pricing` if exists | 200 (live 2026-08-20 ✅) | P1 |
| Z8 | Pricing/credits match EN `/pricing` | Same numbers, as-of date | P0 |

---

## Recommended `/zh/` Routes (verify live)

| Path | Intent |
|------|--------|
| `/zh/` | Chinese home |
| `/zh/use-cases/one-person-company` | OPC 一人公司场景 |
| `/zh/pricing` | 中文定价（若存在） |
| `/zh/download` | 中文下载 |

Flag missing planned routes as Planned Gap — not automatic fail if product prioritizes EN.

---

## Chinese AI Platform Sampling

Run prompts from `prompt-library.md` Category F monthly:

| Platform | Sampling method |
|----------|-----------------|
| 豆包 (Doubao) | Web UI manual |
| Kimi | Web UI manual |
| 秘塔 (Metaso) | Web UI manual |
| 元宝 (Yuanbao) | Optional |
| 百度 AI 搜索 | Optional — if Baidu Webmaster verified |

Log: 品牌提及 / 链接到 floatboat.ai / 事实错误（定价、品类、公司名）

---

## Baidu Webmaster (optional)

| Check | P |
|-------|---|
| Site verified in 百度搜索资源平台 | P2 |
| Sitemap submitted | P2 |
| Mobile-friendly | P2 |

Not blocking for EN-primary GEO audit.

---

## GA4 Segmentation Note

When analyzing traffic, **do not** treat `/zh/` high PV with low Google clicks as SEO failure — segment:

```
Landing page starts with /zh/
Session source = google / organic  → low expected
Session source = baidu / direct / referral → may dominate
```

---

## Entity Names in Chinese

| EN | ZH (approved) |
|----|---------------|
| Floatboat | Floatboat（可保留英文品牌名） |
| Calendar-Driven AI | 日历驱动的 AI |
| Proactive Agent OS | 主动式 Agent 操作系统 |
| Combo Skills | Combo Skills（产品专有名词可保留） |
| Solopreneur | 单人创业者 / 个人创业者 — not 一人公司 in EN pages |
| One-person company | 一人公司 — ZH primary |

---

## hreflang Template

```html
<link rel="alternate" hreflang="en" href="https://floatboat.ai/pricing" />
<link rel="alternate" hreflang="zh-CN" href="https://floatboat.ai/zh/pricing" />
<link rel="alternate" hreflang="x-default" href="https://floatboat.ai/pricing" />
```

Audit: sitemap includes hreflang annotations if implemented sitewide.

---

## Fail Examples

| Finding | P |
|---------|---|
| `/zh/` 404 while linked from footer | P0 |
| Chinese page says Floatboat is "聊天 AI" only — wrong category | P1 |
| hreflang points to 404 EN counterpart | P0 |
| 一人公司 content only in EN without /zh/ counterpart | P2 (strategic) |
