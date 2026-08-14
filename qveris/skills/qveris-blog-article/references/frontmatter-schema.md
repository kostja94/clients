# §2.5 Frontmatter Schema（QVeris 精简版）

> **基准**：`qveris/blog/01-stock-api-free-comparison.md`。与 moras/clink 的 `date/isoDate`、`category` 不同——QVeris 用 `publishedAt/updatedAt`。

## 设计原则（v1.2）

- **`title` / `excerpt` / `tldr` 均不进 frontmatter**，全部放正文。
- **frontmatter 仅 7 个字段**：`slug` `metaTitle` `description` `author` `publishedAt` `updatedAt` `readTime`（readTime 推荐）。
- **已移除字段**（禁止出现在 frontmatter）：`title`、`excerpt`、`tldr`、`badge`、`breadcrumb`、`authorInitials`、`heroImage`、`heroAlt`、`tocExtra`。

## 完整 Schema（frontmatter 仅 7 字段）

```yaml
---
slug: stock-api-free-comparison          # 裸 slug，无 /blog/ 前缀，kebab-case，无年份
metaTitle: "Best Free Stock APIs 2026: Real-Time, Historical & Python | QVeris"
                                         # 含 "| QVeris" 品牌后缀，SEO title
description: "Compare 8 free stock data APIs — Alpaca, Twelve Data, … — on quota, feed freshness, credit card, commercial use and WebSocket access."
                                         # 120–160 字符优先
author: "QVeris Team"                     # 作者名（统一 QVeris Team）
publishedAt: "2026-07-24"                # YYYY-MM-DD，全库唯一
updatedAt: "2026-07-24"                  # 更新日期
readTime: "14 min read"                  # 阅读时长，格式 "N min read"（推荐）
---
```

## 正文结构（title / excerpt / TL;DR 落点）

```
# {Title}                                ← 第一个 H1 = 文章标题（45–90 字符，含主关键词）

*{excerpt}*                              ← H1 后第一段 = excerpt 引言（斜体，2–3 句，≥40 字符）

## TL;DR                                 ← TL;DR 区块（3–5 条 label — body bullet）

- **Fast answer** — {body ≥40 字符，直接回答 primary intent}
- **{label}** — {body}
- **{label}** — {body}

## {第一个正文 H2}
…
```

- `title`：正文 `# H1`，长度 45–90 字符，含 primary keyword；常青标题可带 `(year)` 展示，slug 不允许年份。
- `excerpt`：正文 `# H1` 后紧跟的段落（斜体 `*…*`），2–3 句、≥40 字符，可复用 `description` 扩充。
- **`TL;DR`**：正文 excerpt 后的 `## TL;DR` H2 区块，3–5 条 `- **label** — body` bullet；**第 1 条 label 用 "Fast answer" 作 BLUF**（≥40 字符，直接回答 primary intent）。TL;DR 内**不放内链**。

## 字段规则

| 字段 | 位置 | 必填 | 规则 |
|------|------|:---:|------|
| `slug` | frontmatter | ✅ | 裸 slug，kebab-case，不含年份，不含 `/blog/` |
| `metaTitle` | frontmatter | ✅ | 以 `\| QVeris` 结尾；≤70 字符更佳 |
| `description` | frontmatter | ✅ | 120–160 字符优先（100–280 可接受） |
| `author` | frontmatter | ✅ | `QVeris Team` |
| `publishedAt` | frontmatter | ✅ | ISO `YYYY-MM-DD`；全库唯一（一天一篇） |
| `updatedAt` | frontmatter | ✅ | 修订时更新 |
| `readTime` | frontmatter | 推荐 | 格式 `"{N} min read"` |
| `title` | 正文 `# H1` | ✅ | 45–90 字符；含主关键词 |
| `excerpt` | 正文 H1 后首段 | ✅ | 2–3 句；≥40 字符 |
| `TL;DR` | 正文 excerpt 后 `## TL;DR` | ✅ | 3–5 条 `- **label** — body`；首条 "Fast answer" BLUF ≥40 字符；无内链 |

## 禁止字段（frontmatter）

- ❌ `title` / `excerpt` / `tldr`（移到正文）
- ❌ `badge` / `breadcrumb` / `authorInitials` / `heroImage` / `heroAlt` / `tocExtra`（已移除）
- ❌ `date` / `isoDate`（QVeris 用 `publishedAt/updatedAt`）
- ❌ `category`（无此字段；类型仅路由内部判定）
- ❌ `keywords` / `related` / `disclosure`（schema 已废弃，见 tools 校验）

## 完整示例（已发稿 01，可直接作为模板）

```markdown
---
slug: stock-api-free-comparison
metaTitle: "Best Free Stock APIs 2026: Real-Time, Historical & Python | QVeris"
description: "Compare 8 free stock data APIs — Alpaca, Twelve Data, Alpha Vantage, Finnhub, FMP, Marketstack, Massive and Databento — on quota, feed freshness, credit card, commercial use and WebSocket access."
author: "QVeris Team"
publishedAt: "2026-07-24"
updatedAt: "2026-07-24"
readTime: "14 min read"
---

# Best Free Stock APIs for Real-Time, Historical & Python Use (2026)

*Compare eight free stock data APIs using the questions developers actually ask: Is the data real-time or delayed? Does the free plan work with Python or WebSocket? Is a credit card required? Can the data be used in a commercial product? Every plan detail below was rechecked against official provider pages on July 24, 2026.*

## TL;DR

- **Fast answer** — Alpaca is a strong no-cost starting point for real-time U.S. equity data through IEX. Twelve Data is attractive for broader market coverage and 800 daily API credits. Alpha Vantage and FMP fit low-frequency historical or fundamental research.
- **Important correction** — Polygon.io is now Massive and offers a free Stocks Basic plan. Databento provides $125 in time-limited credits, not a permanent message allowance.
- **Decision rule** — Choose by feed coverage, freshness, redistribution rights and request pattern — not by the word "free" alone.

## Which Free Stock API Offers Real-Time Data Without a Credit Card?
…
```
