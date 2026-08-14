# MeDo Blog

Markdown 格式文章，可直接导入支持 Markdown 的 CMS（Hugo、Jekyll、Next.js MDX、Astro、Lovable 等）。

**线上 URL 模式**：`https://medo.dev/blog/{slug}`（Lovable 预览：`medo-ai.lovable.app/blog/{slug}`）

## 文件结构

- `*.md`：单篇文章，含 YAML frontmatter
- 每篇包含：`title`、`description`、`slug`、`date`、`author`、`category`、`secondary_category`；可选 `updated` / `disclosure`
- **`category`** 取值：`Tutorial`（教程/实操）| `Guide`（概念/选型）| `Case Study`（案例，待写）
- **`secondary_category`**：品类归属，默认 `mobile app`（替代原 cluster 字段）
- **废弃字段（2026-08-11 起）**：`image` / `keywords` / `related` 不再写入 frontmatter（image 由 CMS/OG 管理；keywords/related 由正文内链与 CMS 配置承载）
- **日期规范**：`date` = 发布时间，永不改变；`updated` 仅实质性更新时更新；页面只显示一个日期
- **本目录文档**：`README.md`（本说明）、`blog-structure-internal-links.md`（文章结构与内链）

## Frontmatter 示例

```yaml
---
title: "How to Build a Mobile App with AI: 2026 Non-Developer Guide"
description: "Build real iOS and Android apps with AI in 2026: validate your idea, pick a builder, test on your phone, and ship to TestFlight and the App Store."
slug: "how-to-build-mobile-app-with-ai"   # 不含年份，常青 URL
date: 2026-06-08
author: "Kostja"
category: "Tutorial"
secondary_category: "mobile app"
disclosure: "..."      # Comparison/Alternative 必填
---
```

## 正文规范

- 主节 H2 使用英文编号：`## 1.` … `## N.`
- `## TL;DR`：3–5 bullet；bullet 1 为 snippet 定义句
- `## Conclusion`、`## Frequently asked questions`、`## Related articles` **不加**序号
- **FAQ 固定 6 题**，全部内容相关（禁止通用模板题），≥1 题覆盖边界/异议
- **BLUF 三处**：TL;DR 下 / 每个 major H2 首段 / FAQ 每题首句直接回答
- 站外链接使用 HTML：`<a href="URL" rel="nofollow noopener">锚文本</a>`
- 站内 Blog 互链：`/blog/{slug}`；产品页：`/ai-mobile-app-builder`、`/features` 等
- 对比文：开篇后 Disclosure 段；政策文：正文 as-of 引用块（`as of {month} {year}`，A2）

## 文章列表

| # | 文件 | slug | 主题 | category | 状态 |
|---|------|------|------|----------|------|
| 1 | [01-how-to-build-mobile-app-with-ai.md](./01-how-to-build-mobile-app-with-ai.md) | `how-to-build-mobile-app-with-ai` | 非开发者用 AI 构建移动应用完整指南 | Tutorial | ✅ |
| 2 | [02-what-is-vibe-coding.md](./02-what-is-vibe-coding.md) | `what-is-vibe-coding` | Vibe coding 定义与 2026 现状 | Guide | ✅ |
| 3 | [03-best-ai-mobile-app-builders.md](./03-best-ai-mobile-app-builders.md) | `best-ai-mobile-app-builders` | AI 移动应用构建工具横向对比 | Guide | ✅ |
| 4 | [04-publish-ai-app-app-store.md](./04-publish-ai-app-app-store.md) | `publish-ai-app-app-store` | AI 应用上架 App Store / Play Store | Tutorial | ✅ |
| 5 | [05-medo-tanstack-frontend-migration.md](./05-medo-tanstack-frontend-migration.md) | `medo-tanstack-frontend-migration` | 平台前端从 Vite 迁移至 TanStack | Guide | ✅ |

## 部署

将 `blog/` 目录配置为内容源，设置 `slug` → `/blog/{slug}` URL 映射。图片由 CMS/OG 单独管理，不入 frontmatter。（导入 CMS 时可排除 `README.md`。）

## 内容策略

全站 Blog 的文章结构与文章间内链见 [blog-structure-internal-links.md](./blog-structure-internal-links.md)。关键词规划见 [medo-keywords.md](../medo-keywords.md)，排期见 skill 内 `references/content-graph.md`。

## 关联文档

- [medo.md](../medo.md) — 产品概览
- [medo-growth-strategy.md](../archive/medo-growth-strategy.md) — 内容策略
- [medo-keywords.md](../medo-keywords.md) — 关键词映射
- [medo-site-structure.md](../medo-site-structure.md) — URL 与导航规划
