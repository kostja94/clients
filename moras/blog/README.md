# Moras Blog

Markdown 格式文章，可直接导入支持 Markdown 的 CMS（Hugo、Jekyll、Next.js MDX、Astro 等）。

**线上 URL 模式**：`https://moras.ai{slug}`（slug 已含 `/blog/` 前缀）

写作与 Gate：用自包含 skill [`moras-blog-article`](../skills/blog-article/SKILL.md)（v2.1.0 · 9 Phase + I1–I5 + tools/ + portable/）。页面渲染实现在产品仓 `docs/blog-article-spec.md`（本目录不存）。

**触发语**：

```
按 moras-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Pillar|Setup|Production|Research|Framework|Strategy|SideHustle|Diagnosis|PlatformOps} 文章。
Mode：{lite|standard|flagship}。Topic Scope：{tiktok-shop-affiliate|moras-product|ecommerce-industry|other}。
Intent lane：{Video|Research|Both}。
```

发布前终审：skill 内 `references/portable/final-audit.md`。

## 文件结构

- 路径：`{folder}/NN-{slug}.md` 或根目录 `NN-{slug}.md`（Cluster D 等）
- 每篇 frontmatter 包含：`slug`、`title`、`description`、`date`、`isoDate`、`updated`、`author`、`category`（+ 可选 `secondaryCategory`）
- **发布日期**：`isoDate` 全库唯一，**一天一篇**；新稿 = 当前最晚 `isoDate` +1 天
- TL;DR、Conclusion、FAQ 均为正文内容，写在 Markdown body 中（不在 frontmatter 里）
- **本目录文档**（各司其职，避免重复维护）：

| 文档 | 职责 |
|------|------|
| **README.md**（本文件） | 写作说明 + **成稿索引**（NN / slug / date / 状态） |
| [`blog-structure-internal-links.md`](./blog-structure-internal-links.md) | Cluster 树、内链矩阵、用户旅程（**结构与内链 SSOT**） |
| [`blog-article-backlog.md`](./blog-article-backlog.md) | **未写选题**与 #69+ 规划（成稿后从 backlog 移除，索引只留 README） |
| [`content-graph.md`](../skills/blog-article/references/content-graph.md) | Agent 用 NN 注册表、Canonical、下一序号 |

创作 Gate 在 skill；成稿后按 backlog 内 checklist 同步 README + content-graph + blog-structure。

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
category: "Creator & Affiliate"
secondaryCategory: "Guide"
---
```

## 正文规范

- **TL;DR**：frontmatter 后**正文第一块**；`## TL;DR` 含长描述（60–110 词，兼 hook）+ 3–6 bullet；后接 `---` 再进正文 H2
- 正文主体以第一个非 TL;DR 的 `## Heading`（h2）开始；`title` 字段是文章唯一的 h1
- **Conclusion**：正文倒数第二节，使用 `## Conclusion`（FAQ 之上）
- **FAQ**：正文最后一节，使用 `## Frequently asked questions`，每个 Q 为 `### 问题文本`，A 为紧跟的段落
- 站内 Blog 互链：`{slug}`（slug 来自 frontmatter，已含 `/blog/` 前缀，不含 `NN-` 前缀）

## 文章列表（64 篇）

| # | 文件 | slug | 发布 date | 主题 | 类型 | 状态 |
|---|------|------|-----------|------|------|------|
| 1 | [creator-affiliate/01-how-to-make-money-on-tiktok.md](./creator-affiliate/01-how-to-make-money-on-tiktok.md) | `/blog/how-to-make-money-on-tiktok` | 2026-06-05 | TikTok 全变现路径概览与排名 | Pillar | ✅ |
| 2 | [creator-affiliate/02-tiktok-shop-setup-two-paths.md](./creator-affiliate/02-tiktok-shop-setup-two-paths.md) | `/blog/tiktok-shop-setup` | 2026-06-06 | TikTok Shop 两条入驻路径对比 | Setup | ✅ |
| 3 | [tiktok-video/03-tiktok-shop-videos-without-filming.md](./tiktok-video/03-tiktok-shop-videos-without-filming.md) | `/blog/faceless-tiktok-shop-videos` | 2026-06-07 | 不出镜制作 TikTok Shop 带货视频 | Production | ✅ |
| 4 | [creator-affiliate/04-tiktok-shop-ai-product-research.md](./creator-affiliate/04-tiktok-shop-ai-product-research.md) | `/blog/tiktok-product-research` | 2026-06-08 | 使用 AI 工具进行 TikTok Shop 选品研究 | Research | ✅ |
| 5 | [tiktok-video/05-tiktok-shop-hooks-framework.md](./tiktok-video/05-tiktok-shop-hooks-framework.md) | `/blog/tiktok-video-hooks` | 2026-06-09 | TikTok Shop 钩子心理机制框架 | Hooks | ✅ |
| 6 | [creator-affiliate/06-tiktok-shop-captions-hashtags-strategy.md](./creator-affiliate/06-tiktok-shop-captions-hashtags-strategy.md) | `/blog/tiktok-captions-hashtags` | 2026-06-10 | TikTok Shop 文案与标签策略 | Captions | ✅ |
| 7 | [creator-affiliate/07-tiktok-shop-affiliate-side-hustle.md](./creator-affiliate/07-tiktok-shop-affiliate-side-hustle.md) | `/blog/tiktok-affiliate-side-hustle` | 2026-06-11 | TikTok Shop 联盟营销副业时间线与收入预期 | Side Hustle | ✅ |
| 8 | [creator-affiliate/08-tiktok-shop-no-sales-diagnosis.md](./creator-affiliate/08-tiktok-shop-no-sales-diagnosis.md) | `/blog/tiktok-shop-no-sales` | 2026-06-12 | TikTok Shop 零销量诊断框架 | Diagnosis | ✅ |
| 9 | [creator-affiliate/09-tiktok-shop-influencer-marketing.md](./creator-affiliate/09-tiktok-shop-influencer-marketing.md) | `/blog/tiktok-shop-influencer-marketing` | 2026-06-13 | 品牌向 TikTok Shop 达人营销 | Strategy（品牌 ICP） | ✅ planned |
| 10 | [platform-ops/10-tiktok-shop-customer-service.md](./platform-ops/10-tiktok-shop-customer-service.md) | `/blog/tiktok-shop-customer-service` | 2026-06-14 | TikTok Shop 客服联系指南 | Platform Ops | ✅ draft |
| 11 | [platform-ops/11-tiktok-live-manager.md](./platform-ops/11-tiktok-live-manager.md) | `/blog/tiktok-live-manager` | 2026-06-15 | TikTok Live Manager 直播控制台 | Platform Ops | ✅ draft |
| 12 | [platform-ops/12-tiktok-shop-toolkit.md](./platform-ops/12-tiktok-shop-toolkit.md) | `/blog/tiktok-shop-toolkit` | 2026-06-16 | 工具栈 + Seller Assistant | Platform Ops Hub | ✅ draft |
| 13 | [platform-ops/13-tiktok-live-auction.md](./platform-ops/13-tiktok-live-auction.md) | `/blog/tiktok-live-auction` | 2026-06-17 | TikTok Shop 直播拍卖 | Platform Ops | ✅ draft |
| 14 | [platform-ops/14-tiktok-shop-performance-score.md](./platform-ops/14-tiktok-shop-performance-score.md) | `/blog/tiktok-shop-performance-score` | 2026-06-18 | SPS 店铺绩效评分 | Platform Ops Hub | ✅ draft |
| 16 | [platform-ops/16-tiktok-two-step-verification.md](./platform-ops/16-tiktok-two-step-verification.md) | `/blog/tiktok-two-step-verification` | 2026-06-19 | 两步验证 / 卖家强制要求 | Platform Ops | ✅ draft |
| 18 | [platform-ops/18-how-to-shop-on-tiktok-shop.md](./platform-ops/18-how-to-shop-on-tiktok-shop.md) | `/blog/how-to-shop-on-tiktok-shop` | 2026-06-20 | 买家指南 + Balance | Platform Ops Hub | ✅ draft |
| 19 | [platform-ops/19-tiktok-shop-shipping-delay.md](./platform-ops/19-tiktok-shop-shipping-delay.md) | `/blog/tiktok-shop-shipping-delay` | 2026-06-21 | 物流延迟与 EDT 退款规则 | Platform Ops | ✅ draft |
| 20 | [platform-ops/20-tiktok-giveaway.md](./platform-ops/20-tiktok-giveaway.md) | `/blog/tiktok-giveaway` | 2026-06-22 | Giveaway 合规与增长 | Platform Ops | ✅ draft |
| 21 | [platform-ops/21-tiktok-shop-automation.md](./platform-ops/21-tiktok-shop-automation.md) | `/blog/tiktok-shop-automation` | 2026-06-23 | 店铺自动化边界 | Platform Ops | ✅ draft |
| 22 | [platform-ops/22-tiktok-shop-domestic-seller.md](./platform-ops/22-tiktok-shop-domestic-seller.md) | `/blog/tiktok-shop-domestic-seller` | 2026-06-24 | 本土卖家五大好处 | Platform Ops | ✅ draft |
| 25 | [tiktok-video/25-tiktok-video-formats.md](./tiktok-video/25-tiktok-video-formats.md) | `/blog/tiktok-video-formats` | 2026-06-25 | 带货视频格式匹配框架 | Framework Hub | ✅ planned |
| 26 | [content-discovery/26-how-the-tiktok-algorithm-works.md](./content-discovery/26-how-the-tiktok-algorithm-works.md) | `/blog/how-the-tiktok-algorithm-works` | 2026-06-26 | TikTok 算法四机制分发管线 | Framework | ✅ planned |
| 27 | [content-discovery/27-tiktok-keyword-research.md](./content-discovery/27-tiktok-keyword-research.md) | `/blog/tiktok-keyword-research` | 2026-06-27 | TikTok 搜索关键词研究 | Strategy | ✅ planned |
| 28 | [content-discovery/28-trending-tiktok-sounds.md](./content-discovery/28-trending-tiktok-sounds.md) | `/blog/trending-tiktok-sounds` | 2026-06-28 | 热音选择与商用合规 | Strategy | ✅ planned |
| 29 | [content-discovery/29-tiktok-ai-content-rules.md](./content-discovery/29-tiktok-ai-content-rules.md) | `/blog/tiktok-ai-content-rules` | 2026-06-29 | AI 内容合规三分类 | Strategy | ✅ planned |
| 30 | [content-discovery/30-how-to-use-tiktok-trends.md](./content-discovery/30-how-to-use-tiktok-trends.md) | `/blog/how-to-use-tiktok-trends` | 2026-06-30 | 趋势生命周期决策链 | Strategy | ✅ planned |
| 31 | [31-ai-commerce-agent-ecommerce.md](./31-ai-commerce-agent-ecommerce.md) | `/blog/ai-commerce-agent-ecommerce` | 2026-08-23 | AI commerce agent 六阶段编排 | Research（Cluster D） | ✅ planned |
| 32 | [32-ai-ugc-content-creator.md](./32-ai-ugc-content-creator.md) | `/blog/ai-ugc-content-creator` | 2026-08-24 | AI UGC 三档生产 | Production（Cluster D） | ✅ planned |
| 33 | [33-ai-custom-avatar-videos.md](./33-ai-custom-avatar-videos.md) | `/blog/ai-custom-avatar-videos` | 2026-08-25 | AI 定制 avatar 决策 | Production（Cluster D） | ✅ planned |
| 34 | [34-ai-ecommerce-video-workflow.md](./34-ai-ecommerce-video-workflow.md) | `/blog/ai-ecommerce-video-workflow` | 2026-08-26 | 六阶段 ecommerce video workflow | Framework（Cluster D） | ✅ planned |
| 35 | [tiktok-video/35-tiktok-photo-posts.md](./tiktok-video/35-tiktok-photo-posts.md) | `/blog/tiktok-photo-posts` | 2026-07-01 | Photo Mode / Carousel 带货 | Production | ✅ planned |
| 36 | [tiktok-video/36-tiktok-storytime-sells.md](./tiktok-video/36-tiktok-storytime-sells.md) | `/blog/tiktok-storytime-sells` | 2026-07-02 | Storytime 叙事带货 | Production | ✅ planned |
| 37 | [tiktok-video/37-tiktok-pov-marketing.md](./tiktok-video/37-tiktok-pov-marketing.md) | `/blog/tiktok-pov-marketing` | 2026-07-03 | POV 视角营销 | Production | ✅ planned |
| 38 | [tiktok-video/38-satisfying-product-videos.md](./tiktok-video/38-satisfying-product-videos.md) | `/blog/satisfying-product-videos` | 2026-07-04 | Satisfying 解压产品视频 | Production | ✅ planned |
| 39 | [tiktok-video/39-tiktok-before-after.md](./tiktok-video/39-tiktok-before-after.md) | `/blog/tiktok-before-after` | 2026-07-05 | Before/After 对比展示 | Production | ✅ planned |
| 40 | [tiktok-video/40-tiktok-duet-stitch.md](./tiktok-video/40-tiktok-duet-stitch.md) | `/blog/tiktok-duet-stitch` | 2026-07-06 | Duet / Stitch 借势 | Production | ✅ planned |
| 41 | [tiktok-video/41-tiktok-video-classification.md](./tiktok-video/41-tiktok-video-classification.md) | `/blog/tiktok-video-classification` | 2026-07-07 | 视频格式分类框架 | Framework | ✅ planned |
| 42 | [tiktok-video/42-tiktok-green-screen.md](./tiktok-video/42-tiktok-green-screen.md) | `/blog/tiktok-green-screen` | 2026-07-08 | Green Screen 产品演示 | Production | ✅ planned |
| 43 | [platform-ops/43-is-tiktok-shop-legit.md](./platform-ops/43-is-tiktok-shop-legit.md) | `/blog/is-tiktok-shop-legit` | 2026-08-17 | TikTok Shop 是否靠谱（买家向） | Platform Ops | ✅ planned |
| 44 | [creator-affiliate/44-tiktok-shop-dropshipping.md](./creator-affiliate/44-tiktok-shop-dropshipping.md) | `/blog/tiktok-shop-dropshipping` | 2026-08-18 | Dropshipping 2026 现实 | Strategy | ✅ planned |
| 45 | [platform-ops/45-tiktok-shop-fees.md](./platform-ops/45-tiktok-shop-fees.md) | `/blog/tiktok-shop-fees` | 2026-08-19 | TikTok Shop 费用结构 | Platform Ops | ✅ planned |
| 46 | [platform-ops/46-tiktok-shop-account-health-rating.md](./platform-ops/46-tiktok-shop-account-health-rating.md) | `/blog/tiktok-shop-account-health-rating` | 2026-08-20 | Account Health Rating | Platform Ops | ✅ planned |
| 47 | [content-discovery/47-tiktok-shop-algorithm.md](./content-discovery/47-tiktok-shop-algorithm.md) | `/blog/tiktok-shop-algorithm` | 2026-08-21 | TikTok Shop 算法（Shop 向） | Framework | ✅ planned |
| 48 | [platform-ops/48-tiktok-shop-promo-codes.md](./platform-ops/48-tiktok-shop-promo-codes.md) | `/blog/tiktok-shop-promo-codes` | 2026-08-22 | Promo codes 使用指南 | Platform Ops | ✅ planned |
| 49 | [creator-affiliate/49-tiktok-shop-niche-selection.md](./creator-affiliate/49-tiktok-shop-niche-selection.md) | `/blog/tiktok-shop-niche-selection` | 2026-08-27 | TikTok Shop 垂直 niche 选型 | Strategy | ✅ planned |
| 50 | [tiktok-video/50-tiktok-shop-video-script.md](./tiktok-video/50-tiktok-shop-video-script.md) | `/blog/tiktok-shop-video-script` | 2026-08-28 | 带货视频脚本框架 | Framework | ✅ planned |
| 51 | [platform-ops/51-tiktok-shop-violation-appeal.md](./platform-ops/51-tiktok-shop-violation-appeal.md) | `/blog/tiktok-shop-violation-appeal` | 2026-08-29 | 违规申诉与账号恢复 | Platform Ops | ✅ planned |
| 52 | [creator-affiliate/52-tiktok-shop-free-samples.md](./creator-affiliate/52-tiktok-shop-free-samples.md) | `/blog/tiktok-shop-free-samples` | 2026-08-30 | 免费样品工作流 | Strategy | ✅ planned |
| 53 | [53-ai-ugc-tiktok-shop-conversion.md](./53-ai-ugc-tiktok-shop-conversion.md) | `/blog/ai-ugc-tiktok-shop-conversion` | 2026-08-31 | AI UGC TikTok Shop 转化验证 | Research（Cluster D） | ✅ planned |
| 54 | [creator-affiliate/54-tiktok-creator-rewards-guide.md](./creator-affiliate/54-tiktok-creator-rewards-guide.md) | `/blog/tiktok-creator-rewards-guide` | 2026-09-01 | Creator Rewards / RPM / 提现 | Strategy | ✅ planned |
| 55 | [tiktok-video/55-tiktok-shop-slideshow-compliance.md](./tiktok-video/55-tiktok-shop-slideshow-compliance.md) | `/blog/tiktok-shop-slideshow-compliance` | 2026-09-02 | Slideshow 合规与违规风险 | Strategy | ✅ planned |
| 56 | [creator-affiliate/56-faceless-vs-face-tiktok-shop.md](./creator-affiliate/56-faceless-vs-face-tiktok-shop.md) | `/blog/faceless-vs-face-tiktok-shop` | 2026-09-03 | Faceless vs 露脸决策 | Strategy | ✅ planned |
| 57 | [creator-affiliate/57-tiktok-shop-affiliate-disclosure.md](./creator-affiliate/57-tiktok-shop-affiliate-disclosure.md) | `/blog/tiktok-shop-affiliate-disclosure` | 2026-09-04 | Affiliate FTC 披露 | Strategy | ✅ planned |
| 58 | [creator-affiliate/58-tiktok-shop-affiliate-commissions.md](./creator-affiliate/58-tiktok-shop-affiliate-commissions.md) | `/blog/tiktok-shop-affiliate-commissions` | 2026-09-05 | 创作者佣金怎么算 | Strategy | ✅ planned |
| 59 | [seasonal-campaign/59-tiktok-shop-sales-calendar.md](./seasonal-campaign/59-tiktok-shop-sales-calendar.md) | `/blog/tiktok-shop-sales-calendar` | 2026-09-06 | US 大促日历（Affiliate Hub · 每年更新） | Guide | ✅ planned |
| 60 | [seasonal-campaign/60-tiktok-shop-labor-day.md](./seasonal-campaign/60-tiktok-shop-labor-day.md) | `/blog/tiktok-shop-labor-day` | 2026-09-07 | Labor Day affiliate playbook | Strategy | ✅ planned |
| 61 | [seasonal-campaign/61-tiktok-shop-september-restock.md](./seasonal-campaign/61-tiktok-shop-september-restock.md) | `/blog/tiktok-shop-september-restock` | 2026-09-08 | September Restock 三波策略 | Strategy | ✅ planned |
| 62 | [seasonal-campaign/62-tiktok-shop-back-to-school.md](./seasonal-campaign/62-tiktok-shop-back-to-school.md) | `/blog/tiktok-shop-back-to-school` | 2026-09-09 | Back to School dorm/desk 指南 | Strategy | ✅ planned |
| 63 | [seasonal-campaign/63-tiktok-shop-black-friday.md](./seasonal-campaign/63-tiktok-shop-black-friday.md) | `/blog/tiktok-shop-black-friday` | 2026-09-10 | BFCM affiliate 旗舰 playbook | Strategy | ✅ planned |
| 64 | [seasonal-campaign/64-tiktok-shop-holiday-gifts.md](./seasonal-campaign/64-tiktok-shop-holiday-gifts.md) | `/blog/tiktok-shop-holiday-gifts` | 2026-09-11 | 十二月礼品 guide（affiliate） | Strategy | ✅ planned |
| 65 | [seasonal-campaign/65-tiktok-shop-halloween.md](./seasonal-campaign/65-tiktok-shop-halloween.md) | `/blog/tiktok-shop-halloween` | 2026-09-12 | Halloween 十月饱和日历 | Strategy | ✅ planned |
| 66 | [seasonal-campaign/66-tiktok-shop-fall-deals.md](./seasonal-campaign/66-tiktok-shop-fall-deals.md) | `/blog/tiktok-shop-fall-deals` | 2026-09-13 | Fall Deals 垂类矩阵 | Strategy | ✅ planned |
| 67 | [seasonal-campaign/67-tiktok-shop-jumpstart.md](./seasonal-campaign/67-tiktok-shop-jumpstart.md) | `/blog/tiktok-shop-jumpstart` | 2026-09-14 | Jumpstart 一月 sprint | Strategy | ✅ planned |
| 68 | [seasonal-campaign/68-tiktok-shop-summer-sale.md](./seasonal-campaign/68-tiktok-shop-summer-sale.md) | `/blog/tiktok-shop-summer-sale` | 2026-09-15 | Summer Sale + BTS pivot | Strategy | ✅ planned |

> **下一篇**：文件序号 **#69**，可用 `isoDate`：`2026-09-16`（#15/#17/#23/#24 已删/合并，NN 不重排）

### 已删除 / 合并（无独立 URL）

| 原 slug | 处置 |
|---------|------|
| `/blog/tiktok-shop-balance` (#15) | 合并 → `how-to-shop-on-tiktok-shop` |
| `/blog/tiktok-shop-seller-assistant` (#17) | 合并 → `tiktok-shop-toolkit` |
| `/blog/tiktok-deals-for-you-days` (#23) | 删除 |
| `/blog/tiktok-shop-seller-spotlight-brandon` (#24) | 删除 |

## 部署

将 `blog/` 目录配置为内容源，`slug` 字段已含 `/blog/` 前缀，直接作为 URL 路径使用。图片路径 `image` 需对应实际 CDN 或静态资源路径。（导入 CMS 时可排除本 `README.md`。）

## 关联文档

- [`blog-structure-internal-links.md`](./blog-structure-internal-links.md) — Cluster 树、内链矩阵、补链优先级（**结构与内链唯一 SSOT**）
- [`moras-blog-article` skill](../skills/blog-article/SKILL.md) — 选题到成稿、Gate、正文规范
- [`content-graph.md`](../skills/blog-article/references/content-graph.md) — Agent 用内容图谱、Canonical、Cluster B 发布看板
- 产品仓 `docs/blog-article-spec.md` — Next.js `/blog/[slug]` 页面实现（若需复刻渲染层）
