# MeDo Blog

Markdown 格式文章，可直接导入支持 Markdown 的 CMS（Hugo、Jekyll、Next.js MDX、Astro、Lovable 等）。

**线上 URL 模式**：`https://medo.dev/blog/{slug}`（Lovable 预览：`medo-ai.lovable.app/blog/{slug}`）

## 文件结构

- `*.md`：单篇文章，含 YAML frontmatter；主题簇文章放在对应子文件夹（如 `components/`），全局序号 `NN` 不因归簇而改变
- 每篇包含：`title`、`description`、`slug`、`date`、`author`、`category`、`secondary_category`；可选 `updated`
- **`category`** 取值：`Tutorial`（教程/实操）| `Guide`（概念/选型）| `Case Study`（案例，待写）| `Product`（产品发布/更新）
- **`secondary_category`**：品类归属，默认 `Mobile App`；覆盖跨端功能（移动 + 网页）时可用 `Full-stack App`；**主题簇文章**使用簇名（如 `Components`）（替代原 cluster 字段）
- **废弃字段（2026-08-14 起）**：`image` / `keywords` / `related` / `disclosure` 不再写入 frontmatter（image 由 CMS/OG 管理；keywords 由正文与 CMS 配置承载；related 已取消——内链全部为上下文内链；disclosure 已取消——对比诚实性由正文内容承载）
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
secondary_category: "Mobile App"
---
```

## 正文规范

- 主节 H2 使用英文编号：`## 1.` … `## N.`
- `## TL;DR`：3–5 bullet；bullet 1 为 snippet 定义句
- `## Conclusion`、`## Frequently asked questions` **不加**序号；**不设 `## Related articles`**，内链全部为**上下文内链**（正文自然嵌入）
- **FAQ 固定 6 题**，全部内容相关（禁止通用模板题），≥1 题覆盖边界/异议
- **BLUF 三处**：TL;DR 下 / 每个 major H2 首段 / FAQ 每题首句直接回答
- 站外链接使用 HTML：`<a href="URL" rel="nofollow noopener">锚文本</a>`
- 站内 Blog 互链：`/blog/{slug}`；产品页：`/ai-mobile-app-builder`、`/features` 等
- 对比文：正文 as-of 引用块（`as of {month} {year}`，A2）

## 文章列表

| # | 文件 | slug | 主题 | category | 状态 |
|---|------|------|------|----------|------|
| 1 | [01-how-to-build-mobile-app-with-ai.md](./01-how-to-build-mobile-app-with-ai.md) | `how-to-build-mobile-app-with-ai` | 非开发者用 AI 构建移动应用完整指南 | Tutorial | ✅ |
| 2 | [02-what-is-vibe-coding.md](./02-what-is-vibe-coding.md) | `what-is-vibe-coding` | Vibe coding 定义与 2026 现状 | Guide | ✅ |
| 3 | [03-best-ai-mobile-app-builders.md](./03-best-ai-mobile-app-builders.md) | `best-ai-mobile-app-builders` | AI 移动应用构建工具横向对比 | Guide | ✅ |
| 4 | [04-publish-ai-app-app-store.md](./04-publish-ai-app-app-store.md) | `publish-ai-app-app-store` | AI 应用上架 App Store / Play Store | Tutorial | ✅ |
| 5 | [05-medo-tanstack-frontend-migration.md](./05-medo-tanstack-frontend-migration.md) | `medo-tanstack-frontend-migration` | 平台前端从 Vite 迁移至 TanStack | Guide | ✅ |
| 6 | [06-medo-components.md](./components/06-medo-components.md) | `medo-components` | MeDo Components 功能发布（Components 主题簇 Hub） | Product | ✅ |
| 7 | [07-best-react-component-libraries.md](./components/07-best-react-component-libraries.md) | `best-react-component-libraries` | React 组件库全对比（所有权 + 分层，含动效/目录/AI 专用库） | Guide | ✅ |
| 8 | [08-what-is-a-react-component-library.md](./components/08-what-is-a-react-component-library.md) | `what-is-a-react-component-library` | React 组件库定义（非开发者向） | Guide | ✅ |
| 9 | [09-how-to-create-tailwind-components.md](./components/09-how-to-create-tailwind-components.md) | `how-to-create-tailwind-components` | 创建 Tailwind 组件教程 | Tutorial | ✅ |
| 10 | [10-are-tailwind-components-free.md](./components/10-are-tailwind-components-free.md) | `are-tailwind-components-free` | Tailwind 组件是否免费（成本模型） | Guide | ✅ |
| 11 | [11-what-is-an-ai-ui-generator.md](./components/11-what-is-an-ai-ui-generator.md) | `what-is-an-ai-ui-generator` | AI UI 生成器定义（边界梳理） | Guide | ✅ |
| 20 | [20-best-21st-dev-alternatives.md](./components/20-best-21st-dev-alternatives.md) | `best-21st-dev-alternatives` | 21st.dev 替代品对比 | Guide | ✅ |
| 21 | [21-best-ai-component-generators.md](./components/21-best-ai-component-generators.md) | `best-ai-component-generators` | AI 组件生成器对比 | Guide | ✅ |
| 22 | [22-best-ai-design-skills.md](./design/22-best-ai-design-skills.md) | `best-ai-design-skills` | AI 设计 skills 对比（六层能力框架） | Guide | ✅ |
| 23 | [23-what-is-frontend-design-skill.md](./design/23-what-is-frontend-design-skill.md) | `what-is-frontend-design-skill` | Anthropic frontend-design skill 定义 | Guide | ✅ |
| 24 | [24-figma-design-tokens.md](./design/24-figma-design-tokens.md) | `figma-design-tokens` | Figma design tokens 定义（非开发者向） | Guide | ✅ |
| 25 | [25-what-is-design-md.md](./design/25-what-is-design-md.md) | `what-is-design-md` | Google DESIGN.md 格式定义 | Guide | ✅ |
| 26 | [26-design-tokens-vs-css-variables.md](./design/26-design-tokens-vs-css-variables.md) | `design-tokens-vs-css-variables` | Design tokens vs CSS variables 选型 | Guide | ✅ |
| 27 | [27-why-ai-websites-look-the-same.md](./design/27-why-ai-websites-look-the-same.md) | `why-ai-websites-look-the-same` | AI 网站千篇一律诊断与修复 | Guide | ✅ |
| 28 | [28-how-to-build-design-system-with-ai.md](./design/28-how-to-build-design-system-with-ai.md) | `how-to-build-design-system-with-ai` | 用 AI 构建设计系统教程（非开发者向） | Tutorial | ✅ |

## 主题簇

### Components 系列（`components/` 子目录）

围绕 MeDo Components（AI 生成 UI 积木块）的主题簇，`secondary_category: "Components"`。文章放在 [components/](./components/) 子目录，全局序号 `NN` 保持不变。

```
                    ┌──────────────────────────────┐
                    │  06 medo-components           │
                    │  功能发布 Hub（已发布）        │
                    └──────────────┬───────────────┘
                                  │
        ┌─────────────────────────┼──────────────────────────┐
        │                         │                          │
  ┌─────▼──────────┐   ┌──────────▼─────────┐   ┌───────────▼────────┐
  │ 07 best-react-  │   │ 08 what-is-a-      │   │ 09 how-to-create-  │
  │ component-lib   │   │ react-component-   │   │ tailwind-          │
  │ (库全对比)       │   │ library (定义)     │   │ components (教程)  │
  └─────────────────┘   └────────────────────┘   └────────────────────┘
        │                         │
  ┌─────▼──────────┐   ┌──────────▼─────────┐
  │ 10 are-tailwind│   │ 11 what-is-an-     │
  │ components-free│   │ ai-ui-generator    │
  └────────────────┘   └────────────────────┘
        │
  ┌─────▼──────────┐   ┌──────────▼─────────┐
  │ 20 best-21st-  │   │ 21 best-ai-        │
  │ dev-alternatives│  │ component-         │
  │ (替代品对比)    │   │ generators         │
  └────────────────┘   └────────────────────┘
```

**选题方向**（参考 `medo/components/medo-ai-components-strategy.md` §6.1）：组件分类长尾词（navbar components、pricing table components 等）、21st.dev 对比、用组件拼接落地页实操、AI 组件生成器对比。已写 7 篇 Spoke（#07–#11、#20–#21；原 #22「AI 组件库」已并入 #07）。发布节奏：先 Hub 后 Spoke，一天一篇。序号 #12–#21 预留缓冲。

### AI Frontend Design 系列（`design/` 子目录）

围绕「让 AI 生成的界面不再千篇一律」的设计系统层主题簇，`secondary_category: "AI Frontend Design"`。文章放在 [design/](./design/) 子目录，全局序号 `NN` 保持不变。本簇承接设计系统层关键词（AI design skills、frontend-design skill、Figma design tokens、DESIGN.md），与 Components 簇（组件层）互补。**内链约定**：簇内文章互链 + 每篇链回 #22（选型 Hub）+ 每篇链回 Pillar。

```
                    ┌──────────────────────────────┐
                    │  22 best-ai-design-skills     │
                    │  选型 Hub（六层能力框架）      │
                    └──────────────┬───────────────┘
                                  │
        ┌─────────────────────────┼──────────────────────────┐
        │                         │                          │
  ┌─────▼──────────┐   ┌──────────▼─────────┐   ┌───────────▼────────┐
  │ 23 what-is-     │   │ 24 figma-design-   │   │ 25 what-is-         │
  │ frontend-design │   │ tokens (值层)      │   │ design-md (契约层)  │
  │ skill (美学skill)│  └────────────────────┘   └────────────────────┘
  └─────────────────┘
        │
  ┌─────▼──────────┐   ┌──────────▼─────────┐
  │ 26 design-      │   │ 27 why-ai-         │
  │ tokens-vs-css-  │   │ websites-look-     │
  │ variables       │   │ the-same           │
  │ (值层选型)      │   │ (诊断+修复)        │
  └────────────────┘   └──────────┬──────────┘
                                  │
                          ┌───────▼────────┐
                          │ 28 how-to-      │
                          │ build-design-   │
                          │ system-with-ai  │
                          │ (搭建教程)      │
                          └────────────────┘
```

**选题方向**：AI design skills 对比（#22，已写）、frontend-design skill 定义（#23，已写）、Figma design tokens 定义（#24，已写）、DESIGN.md 格式定义（#25，已写）、design tokens vs CSS variables 选型（#26，已写）、AI 网站为什么千篇一律诊断（#27，已写）、用 AI 构建设计系统教程（#28，已写）。后续可扩展：design skills vs design tokens 边界。发布节奏：一天一篇。序号 #29 起为移动簇缓冲。


## 部署

将 `blog/` 目录配置为内容源，设置 `slug` → `/blog/{slug}` URL 映射。图片由 CMS/OG 单独管理，不入 frontmatter。（导入 CMS 时可排除 `README.md`。）

## 内容策略

全站 Blog 的文章结构与文章间内链见 [blog-structure-internal-links.md](./blog-structure-internal-links.md)。关键词规划见 [medo-keywords.md](../medo-keywords.md)，排期见 skill 内 `references/content-graph.md`。

## 关联文档

- [medo.md](../medo.md) — 产品概览
- [medo-growth-strategy.md](../archive/medo-growth-strategy.md) — 内容策略
- [medo-keywords.md](../medo-keywords.md) — 关键词映射
- [medo-site-structure.md](../medo-site-structure.md) — URL 与导航规划
