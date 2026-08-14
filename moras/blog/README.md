# Moras Blog

Markdown 格式文章，可直接导入支持 Markdown 的 CMS（Hugo、Jekyll、Next.js MDX、Astro 等）。

**线上 URL 模式**：`https://moras.ai{slug}`（slug 已含 `/blog/` 前缀）

写作与 Gate：用 skill [`moras-blog-article`](../skills/blog-article/SKILL.md)；内容图谱 / Cluster B 发布看板见 [`content-graph.md`](../skills/blog-article/references/content-graph.md)。页面渲染实现在产品仓 `docs/blog-article-spec.md`（本目录不存）。

## 文件结构

- `{NN}-{slug}.md`：单篇文章，NN 为两位数序号，含 YAML frontmatter
- 每篇 frontmatter 包含：`slug`、`title`、`description`、`date`、`isoDate`、`updated`、`author`
- **发布日期**：`isoDate` 全库唯一，**一天一篇**；按文件序号 `#01` 起逐日递增（见下表）；新稿 = 当前最晚 `isoDate` +1 天
- TL;DR、Conclusion、FAQ 均为正文内容，写在 Markdown body 中（不在 frontmatter 里）
- **本目录文档**：仅本 `README.md`（文章索引）；写作规范在 skill

## Frontmatter 示例

```yaml
---
title: "How to Make Money on TikTok in 2026 — Every Monetization Lane, Ranked"
slug: "/blog/how-to-make-money-on-tiktok"
description: "Meta description..."
date: "June 5, 2026"
isoDate: "2026-06-05"
updated: "2026-06-05"
author: "Kostja"
---
```

## 正文规范

- **TL;DR**：frontmatter 后**正文第一块**；`## TL;DR` 含长描述（60–110 词，兼 hook）+ 3–6 bullet；后接 `---` 再进正文 H2
- 正文主体以第一个非 TL;DR 的 `## Heading`（h2）开始；`title` 字段是文章唯一的 h1
- **Conclusion**：正文倒数第二节，使用 `## Conclusion`（FAQ 之上）
- **FAQ**：正文最后一节，使用 `## Frequently asked questions`，每个 Q 为 `### 问题文本`，A 为紧跟的段落
- 站内 Blog 互链：`{slug}`（slug 来自 frontmatter，已含 `/blog/` 前缀，不含 `NN-` 前缀）

## 文章列表

| # | 文件 | slug | 发布 date | 主题 | 类型 | 状态 |
|---|------|------|-----------|------|------|------|
| 1 | [01-how-to-make-money-on-tiktok.md](./01-how-to-make-money-on-tiktok.md) | `/blog/how-to-make-money-on-tiktok` | 2026-06-05 | TikTok 全变现路径概览与排名 | Pillar | ✅ |
| 2 | [02-tiktok-shop-setup-two-paths.md](./02-tiktok-shop-setup-two-paths.md) | `/blog/tiktok-shop-setup` | 2026-06-06 | TikTok Shop 两条入驻路径对比 | Setup | ✅ |
| 3 | [03-tiktok-shop-videos-without-filming.md](./03-tiktok-shop-videos-without-filming.md) | `/blog/faceless-tiktok-shop-videos` | 2026-06-07 | 不出镜制作 TikTok Shop 带货视频 | Production | ✅ |
| 4 | [04-tiktok-shop-ai-product-research.md](./04-tiktok-shop-ai-product-research.md) | `/blog/tiktok-product-research` | 2026-06-08 | 使用 AI 工具进行 TikTok Shop 选品研究 | Research | ✅ |
| 5 | [05-tiktok-shop-hooks-framework.md](./05-tiktok-shop-hooks-framework.md) | `/blog/tiktok-video-hooks` | 2026-06-09 | TikTok Shop 钩子心理机制框架 | Hooks | ✅ |
| 6 | [06-tiktok-shop-captions-hashtags-strategy.md](./06-tiktok-shop-captions-hashtags-strategy.md) | `/blog/tiktok-captions-hashtags` | 2026-06-10 | TikTok Shop 文案与标签策略 | Captions | ✅ |
| 7 | [07-tiktok-shop-affiliate-side-hustle.md](./07-tiktok-shop-affiliate-side-hustle.md) | `/blog/tiktok-affiliate-side-hustle` | 2026-06-11 | TikTok Shop 联盟营销副业时间线与收入预期 | Side Hustle | ✅ |
| 8 | [08-tiktok-shop-no-sales-diagnosis.md](./08-tiktok-shop-no-sales-diagnosis.md) | `/blog/tiktok-shop-no-sales` | 2026-06-12 | TikTok Shop 零销量诊断框架 | Diagnosis | ✅ |
| 9 | [09-tiktok-shop-influencer-marketing.md](./09-tiktok-shop-influencer-marketing.md) | `/blog/tiktok-shop-influencer-marketing` | 2026-06-13 | 品牌向 TikTok Shop 达人营销（费用/品类/信任/发现） | Strategy（品牌 ICP） | ✅ planned |
| 10 | [10-tiktok-shop-customer-service.md](./10-tiktok-shop-customer-service.md) | `/blog/tiktok-shop-customer-service` | 2026-06-14 | TikTok Shop 客服联系指南 | Platform Ops | ✅ draft |
| 11 | [11-tiktok-live-manager.md](./11-tiktok-live-manager.md) | `/blog/tiktok-live-manager` | 2026-06-15 | TikTok Live Manager 直播控制台 | Platform Ops | ✅ draft |
| 12 | [12-tiktok-shop-toolkit.md](./12-tiktok-shop-toolkit.md) | `/blog/tiktok-shop-toolkit` | 2026-06-16 | 工具栈 + Seller Assistant（含原 #17） | Platform Ops Hub | ✅ draft |
| 13 | [13-tiktok-live-auction.md](./13-tiktok-live-auction.md) | `/blog/tiktok-live-auction` | 2026-06-17 | TikTok Shop 直播拍卖 Countdown Bidding | Platform Ops | ✅ draft |
| 14 | [14-tiktok-shop-performance-score.md](./14-tiktok-shop-performance-score.md) | `/blog/tiktok-shop-performance-score` | 2026-06-18 | SPS 店铺绩效评分 | Platform Ops Hub | ✅ draft |
| 16 | [16-tiktok-two-step-verification.md](./16-tiktok-two-step-verification.md) | `/blog/tiktok-two-step-verification` | 2026-06-19 | 两步验证 / 卖家强制要求 | Platform Ops | ✅ draft |
| 18 | [18-how-to-shop-on-tiktok-shop.md](./18-how-to-shop-on-tiktok-shop.md) | `/blog/how-to-shop-on-tiktok-shop` | 2026-06-20 | 买家指南 + Balance（含原 #15） | Platform Ops Hub | ✅ draft |
| 19 | [19-tiktok-shop-shipping-delay.md](./19-tiktok-shop-shipping-delay.md) | `/blog/tiktok-shop-shipping-delay` | 2026-06-21 | 物流延迟与 EDT 退款规则 | Platform Ops | ✅ draft |
| 20 | [20-tiktok-giveaway.md](./20-tiktok-giveaway.md) | `/blog/tiktok-giveaway` | 2026-06-22 | Giveaway 合规与增长 | Platform Ops | ✅ draft |
| 21 | [21-tiktok-shop-automation.md](./21-tiktok-shop-automation.md) | `/blog/tiktok-shop-automation` | 2026-06-23 | 店铺自动化边界 | Platform Ops | ✅ draft |
| 22 | [22-tiktok-shop-domestic-seller.md](./22-tiktok-shop-domestic-seller.md) | `/blog/tiktok-shop-domestic-seller` | 2026-06-24 | 本土卖家五大好处 | Platform Ops | ✅ draft |
| 25 | [25-tiktok-video-formats.md](./25-tiktok-video-formats.md) | `/blog/tiktok-video-formats` | 2026-06-25 | 带货视频格式匹配框架（商品类型×认知阶段×算法信号） | Framework（Cluster C） | ✅ planned |
| 26 | [26-how-the-tiktok-algorithm-works.md](./26-how-the-tiktok-algorithm-works.md) | `/blog/how-the-tiktok-algorithm-works` | 2026-06-26 | TikTok 算法四机制分发管线（带货向） | Framework（Cluster C） | ✅ planned |
| 27 | [27-tiktok-keyword-research.md](./27-tiktok-keyword-research.md) | `/blog/tiktok-keyword-research` | 2026-06-27 | TikTok 搜索关键词研究（三索引放置+关键词簇） | Strategy（Cluster C） | ✅ planned |
| 28 | [28-trending-tiktok-sounds.md](./28-trending-tiktok-sounds.md) | `/blog/trending-tiktok-sounds` | 2026-06-28 | 热音选择（velocity>popularity + 商用音乐合规） | Strategy（Cluster C） | ✅ planned |
| 29 | [29-tiktok-ai-content-rules.md](./29-tiktok-ai-content-rules.md) | `/blog/tiktok-ai-content-rules` | 2026-06-29 | AI 内容合规三分类（TikTok+FTC 双轨） | Strategy（Cluster C） | ✅ planned |
| 30 | [30-how-to-use-tiktok-trends.md](./30-how-to-use-tiktok-trends.md) | `/blog/how-to-use-tiktok-trends` | 2026-06-30 | 趋势生命周期与是否跟进的决策链 | Strategy（Cluster C） | ✅ planned |

> **下一篇**：文件序号 **#31**，可用 `isoDate`：`2026-07-01`（#15/#17/#23/#24 已删/合并，NN 不重排）

### 已删除 / 合并（无独立 URL）

| 原 slug | 处置 |
|---------|------|
| `/blog/tiktok-shop-balance` (#15) | 合并 → `how-to-shop-on-tiktok-shop` |
| `/blog/tiktok-shop-seller-assistant` (#17) | 合并 → `tiktok-shop-toolkit` |
| `/blog/tiktok-deals-for-you-days` (#23) | 删除 |
| `/blog/tiktok-shop-seller-spotlight-brandon` (#24) | 删除 |

## 集群结构

### Cluster A — Creator / Affiliate（#01–#09）

```
01-how-to-make-money-on-tiktok          ← Pillar：全变现路径概览
  ├── 02-tiktok-shop-setup-two-paths    ← Spoke：入驻与账号设置
  ├── 03-tiktok-shop-videos-without-filming ← Spoke：视频制作（不出镜）
  ├── 04-tiktok-shop-ai-product-research    ← Spoke：AI 选品
  ├── 05-tiktok-shop-hooks-framework        ← Spoke：钩子框架
  ├── 06-tiktok-shop-captions-hashtags-strategy ← Spoke：文案与标签
  ├── 07-tiktok-shop-affiliate-side-hustle  ← Spoke：副业时间线
  ├── 08-tiktok-shop-no-sales-diagnosis     ← Spoke：故障诊断
  └── 09-tiktok-shop-influencer-marketing   ← Spoke：品牌向达人营销决策
```

### Cluster B — Platform Ops（#10–#22，11 篇存活）

```
                    ┌─────────────────────────────────────┐
                    │  12 Toolkit Hub (+ Seller Assistant) │
                    │  14 SPS Hub · 18 Buyer Hub           │
                    └──────────────┬──────────────────────┘
                                   │
     ┌─────────────┬───────────────┼───────────────┬─────────────┐
     │             │               │               │             │
  10 Support   11 Live Mgr    13 Auction     16 2SV      19 Shipping
     │             │               │               │             │
     └─────────────┴───────────────┴───────┬───────┴─────────────┘
                                           │
                              20 Giveaway · 21 Automation · 22 Domestic
```

### Cluster C — Content & Discovery（#25–#30，6 篇）

```
25-tiktok-video-formats                ← Spoke：格式匹配框架
  ├── 26-how-the-tiktok-algorithm-works ← Spoke：算法四机制分发
  ├── 27-tiktok-keyword-research        ← Spoke：关键词研究/放置
  ├── 28-trending-tiktok-sounds         ← Spoke：热音选择与合规
  ├── 29-tiktok-ai-content-rules        ← Spoke：AI 内容合规
  └── 30-how-to-use-tiktok-trends       ← Spoke：趋势决策链
```

Cluster C 内部已互链闭合（自然语境，同 slug ≤2 次）；C→A/B 弱桥接（#25→#01/#05/#06 等）。发布策略：isoDate 06-25 起一天一篇，与 Cluster B 现有档期衔接。

Cluster A ↔ B 弱桥接：seller/creator 文链 #08/#04；live 文链 #05。

编号逻辑（Cluster A）：Pillar → Setup → Production → Research → Hooks → Captions → Side Hustle → Diagnosis → Brand Influencer。

编号逻辑（Cluster B）：文件 NN 保留间隙（#15/#17/#23/#24 已删/合并），不重排。

**发布策略**：Tier 1（#10 #12 #14 #20）→ Tier 2（#11 #13 #16 #18 #19）→ Tier 3（#21 #22）；按 isoDate 一天一篇。Tier / SuccessMetric / T+30 清单见 skill [`content-graph.md` §4.2b](../skills/blog-article/references/content-graph.md)。

## 部署

将 `blog/` 目录配置为内容源，`slug` 字段已含 `/blog/` 前缀，直接作为 URL 路径使用。图片路径 `image` 需对应实际 CDN 或静态资源路径。（导入 CMS 时可排除本 `README.md`。）

## 关联文档

- [`moras-blog-article` skill](../skills/blog-article/SKILL.md) — 选题到成稿、Gate、正文规范
- [`content-graph.md`](../skills/blog-article/references/content-graph.md) — 内容图谱、Canonical、Cluster B 发布看板
- 产品仓 `docs/blog-article-spec.md` — Next.js `/blog/[slug]` 页面实现（若需复刻渲染层）
