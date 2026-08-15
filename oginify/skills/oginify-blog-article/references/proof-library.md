# Oginify Proof Library — Product Fact Ledger

> 加载时机：Phase 0R（R1 第一步）/ Phase 4 / Phase 5
> 主文件：SKILL.md §9 指针 · 与 product-competitors.md 互补（此文件为可引用 claim 库）

---

## 1. 可引用 Fact（按 Proof ID）

| Proof ID | Claim | 表述模板 | 来源 |
|----------|-------|---------|------|
| OG-01 | URL-first 生成 4 变体 | "paste a URL and get four 1200×630 cards — one on-brand, three wildcards" | oginify.com |
| OG-02 | 30 秒生成 | "a run lands in about thirty seconds" | oginify.com |
| OG-03 | 免费 6 张/天 | "you can generate up to 6 images per day without an account or a card on file" | oginify.com + pricing |
| OG-04 | 按张付费无订阅 | "pay per card: $0.99 single, $7.90 for ten, $29 for fifty — credits never expire, no subscription" | oginify.com/pricing |
| OG-05 | 输出 1200×630 PNG + meta tags | "download a strict 1200×630 PNG and paste ready-made Open Graph and Twitter Card tags" | oginify.com |
| OG-06 | 开源 social-cards-skills | "the MIT-licensed Agent Skills distribution of the same engine" | github.com/kostja94/social-cards-skills |
| OG-07 | 三分类定位 | "The three tools solve adjacent problems, not the same one"（vs @vercel/og / Cloudinary） | oginify.com |

---

## 2. 竞品可引用 Fact（R3 验证后使用）

| 竞品 | Claim | 表述模板 | 来源 |
|------|-------|---------|------|
| Gemini 3.1 Flash Image | 1K 图约 $0.067 | "roughly $0.067 per 1K image via the Gemini API, no free tier for image output" | ai.google.dev pricing |
| GPT Image 2 | 2026-04-21 发布，native reasoning | "released April 2026 with native reasoning and legible text rendering" | openai.com + API docs |
| Midjourney V8.1 | $10–$120/月 订阅 | "Basic $10/mo, Standard $30/mo, Pro $60/mo, Mega $120/mo; annual billing saves 20%" | docs.midjourney.com |
| Vercel OG | 免费，JSX→PNG | "free on Vercel's free tier, renders JSX via Satori to PNG at the edge" | vercel.com docs |
| Placid | $19+/月 | "starts at $19/month for 500 credits" | placid.app pricing（as-of） |
| Bannerbear | $49+/月 | "starts at $49/month for 1,000 API credits" | bannerbear.com pricing |
| Canva | ~$13/月 | "paid plans run around $13/month" | canva.com（as-of） |
| Cloudinary | ~$99/月起 | "paid plans start around $99/month" | cloudinary.com（as-of） |

---

## 3. 使用规则

- P0 数字必须在正文出现时带 `[Source: URL]`（citations.md §1）
- 所有数字 claim 须带 `as of {month} {year}`（P1 Gate）
- 竞品定价以官方 pricing 页为准；第三方评测数据需交叉验证后使用
- 本库数字为 R3 基线；每次创作 Phase 0R 须重搜验证（价格可能变动）
