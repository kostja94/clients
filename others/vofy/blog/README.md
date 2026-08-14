# Vofy Blog

本目录存放 **与 [vofy.art/blog](https://www.vofy.art/blog) 对齐** 的 Markdown 草稿与终稿（`*.md` + YAML frontmatter），英文正文与现网一致时可对接 CMS 或同一内容仓库。

**策略语境**：[vofy.md](../vofy.md) · [vofy-features.md](../vofy-features.md) · [vofy-keywords.md](../vofy-keywords.md) · [vofy-site-structure.md](../vofy-site-structure.md) · [vofy-blog-inventory-zh.md](../vofy-blog-inventory-zh.md) · [apps/03-vofy-apps-howto-implementation-zh.md](../apps/03-vofy-apps-howto-implementation-zh.md)

---

## 创作 Skill 与质量审核

| 阶段 | 工具 | 路径 |
|------|------|------|
| **选题 → 成稿** | Vofy 博客文章创作 Skill | [skills/vofy-blog-article/SKILL.md](./skills/vofy-blog-article/SKILL.md) |
| **发布前终审** | 十维内容质量审核 | [`blog-audit/README.md`](../../skills%20for%20clients/blog-audit/README.md) |

**工作流**：先用创作 Skill 走 Phase 0–7（Brief → Outline → Draft → SelfCheck），成稿 **audit-ready** 后按 [`blog-audit/README.md`](../../skills%20for%20clients/blog-audit/README.md) 做 P0 Gate + **十维评分**。

**Agent 用法**：

```
按 vofy-blog-article skill，为关键词 "{primary keyword}" 创建一篇 {ModelGuide|PromptGuide|AppHowTo|Comparison|StyleGuide|Campaign|Announcement} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
```

创作 Skill **完全自包含**（v1.0.0）——Agent 只需读 `skills/vofy-blog-article/SKILL.md`，无需再打开 `../vofy-keywords.md` 等策略文档。策略变更时同步 bump Skill 的 `metadata.version`。

新文章文件序号：当前下一号为 **53**（见 Skill §4.1）。成稿后请更新下方「本目录文件」表。

---

## 主题簇概览

现网 blog 以 **模型簇 + Apps 长尾 + 节日营销** 为主，hub-spoke 结构见 Skill §4.2。

```
                    ┌─────────────────────────────┐
                    │  ModelGuide (Hub)            │
                    │  e.g. gpt-image-2-guide      │
                    └──────────────┬──────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         │                         │                         │
  PromptGuide               Comparison                 AppHowTo / Campaign
  gpt-image-2-prompts       vs Midjourney              mothers-day-*
                            vs Nano Banana
```

**高优先级缺口**（详见 [vofy-blog-inventory-zh.md](../vofy-blog-inventory-zh.md) §四）：

- Grok Imagine、Veo 3.1 模型簇（Hub + PromptGuide）
- Seedance 2 vs Kling 3.0 vs Veo 3.1 三方对比
- Motion Control、Inpaint 专题
- Vofy 品牌 / multi-model studio 品类文

---

## 本目录文件

| 文件 | Slug | 类型 | 状态 | 说明 |
|------|------|------|------|------|
| [52-introducing-vofy-ai-canvas.md](./52-introducing-vofy-ai-canvas.md) | `introducing-vofy-ai-canvas` | Announcement | 草稿 | Vofy Canvas 上线 · Skill v2.0 重写 · [vofy.art/canvas](https://www.vofy.art/canvas) |

> 完整现网 slug 登记表见 [skills/vofy-blog-article/SKILL.md §4.1](./skills/vofy-blog-article/SKILL.md)。

---

## 命名与 Frontmatter

| 约定 | 说明 |
|------|------|
| 文件 | `NN-{slug-kebab}.md`，NN 从 52 起；常青 slug **不含年份** |
| `slug` | 与现网 `/blog/{slug}` 一致；**新稿** Nano Banana 系列统一 `nanobanana-2-*`（对齐 `/models/nanobanana/2`） |
| 语言 | 主站/博客为**英文**；与用户沟通可用中文 |
| `cluster` | hub-spoke 聚类 ID（如 `gpt-image-2`、`kling-3-0`） |
| `model_version_note` | 模型类文章必填时效标注 |

> **2026-08-11 起废弃**：`image` / `keywords` / `related` 不再写入 frontmatter（image 由 CMS 单独管理；keywords/related 由正文内链与 CMS 配置承载）。`related` 互链以正文为准。

```yaml
---
title: "GPT Image 2 Prompts — A Practical Framework for Creators"
description: "120–160 chars, benefit + main intent keyword for SERP"
slug: "gpt-image-2-prompts-guide"
date: 2026-06-15
author: "Ryan Mitchell"
category: "Tutorial"
cluster: "gpt-image-2"
model: "gpt-image-2"
app_slug: ""
studio_url: "/studio/create/image?mode=create&model=gpt-image-2"
disclosure: "Vofy is an all-in-one AI creative studio. This article uses Vofy workflows as examples."
seasonal: false
model_version_note: "Based on GPT Image 2 as available on Vofy, June 2026."
---
```

**作者 persona 池**（与现网一致，按主题选用）：Ryan Mitchell · Sofia Rodriguez · Yuki Tanaka · Emma Clarke · Alex Harper · Marcus Chen · Priya Sharma · Lucas Andersson · Vofy Team

---

## 写作标准（Vofy 通用）

以下为 Vofy blog 统一约束，源自 12 维度模板体系 + 现网惯例：

| 维度 | 约束 |
|------|------|
| **产品提及比例** | ModelGuide ≤25%，PromptGuide ≤30%，Comparison ≤40%，AppHowTo/StyleGuide ≤45%，Campaign ≤50% |
| **模型时效** | 模型能力、Credits、studio 参数须标注 `as of {month} {year}`；禁写死「永远最便宜/最快」 |
| **内链** | ModelGuide/PromptGuide 必链 `/models/` 或 studio；AppHowTo 必链 `/apps/{slug}`；正文 blog 互链 ≥2 |
| **竞品公平性** | Leonardo / Runway / Pika / fal 等至少 1 个优势；禁 derogatory 措辞 |
| **Disclosure** | Comparison / 高产品占比文必填 `disclosure` |
| **敏感类目** | 亲密特效、名人换脸、身体塑形类须加用途/授权声明（见 Skill §1.3） |
| **Slug** | 新稿统一 `nanobanana-2-*`；禁 slug 内嵌年份 |
| **FAQ** | ≥3 题；≥1 题覆盖 objection 或边界 |
| **HowTo 结构** | AppHowTo 对齐 [apps/03-vofy-apps-howto-implementation-zh.md](../apps/03-vofy-apps-howto-implementation-zh.md) 三步/四步框架 |

---

## 跨文章一致性

| 概念 | Canonical 文章（现网） | 引用方式 |
|------|----------------------|---------|
| GPT Image 2 定义 | `gpt-image-2-guide` | 1–2 句 + link |
| GPT Image 2 Prompt 框架 | `gpt-image-2-prompts-guide` | 同上 |
| Nano Banana 2 入门 | `nano-banana-2-gemini-3-1-flash-image-generation` | 同上 |
| Seedance 2 角色一致性 | `seedance-2-consistent-character-advanced-guide` | 同上 |
| Kling 3.0 完整指南 | `kling-3-0-complete-guide` | 同上 |

---

## 关联

| 文档 | 用途 |
|------|------|
| [../vofy.md](../vofy.md) | 主产品定位、ICP |
| [../vofy-features.md](../vofy-features.md) | 模型矩阵、Credits、studio URL |
| [../vofy-keywords.md](../vofy-keywords.md) | P0–P2 关键词梯队 |
| [../vofy-competitors.md](../vofy-competitors.md) | 竞品格局、对比稿素材 |
| [../vofy-use-cases.md](../vofy-use-cases.md) | 5 层受众、场景语言 |
| [../vofy-brand-visual.md](../vofy-brand-visual.md) | Voice & Tone |
| [../vofy-blog-inventory-zh.md](../vofy-blog-inventory-zh.md) | 现网 51+ 篇审计与缺口 |
| [skills/vofy-blog-article/SKILL.md](./skills/vofy-blog-article/SKILL.md) | 博客文章创作 Skill |
| [`blog-audit/`](../../skills%20for%20clients/blog-audit/) | 十维内容质量审查（成稿后终审） |
