# Oginify Blog

本目录存放 **与 oginify.com 公开博客对齐** 的 Markdown 终稿（`*.md` + YAML frontmatter），以及完整的博客文章创作 Skill 系统。英文正文与现网 [oginify 博客](https://oginify.com/blog/) 一致时可对接 CMS 或同一内容仓库。

---

## 目录结构总览

```
oginify/
├── skills/
│   └── oginify-blog-article/       ← 博客文章创作 Skill（v1.0.0，自包含）
│       ├── SKILL.md                ← 主 Skill 文件（9 Phase + 5 Gate 工作流）
│       ├── references/             ← 按需加载的参考规则（渐进式加载，一次 ≤2 个）
│       ├── references/portable/    ← 自包含便携参考（12 个）
│       ├── tools/                  ← Phase 5 机器检查脚本（3 个 Python + README）
│       └── evals/                  ← 回归测试套件（20 个 Eval + 6 个 golden-brief）
└── blog/
    ├── README.md                   ← 本文件
    └── 01-best-ai-og-image-generators.md  ← 已发布稿
```

---

## 创作 Skill 与工作流

**Skill 入口**：[skills/oginify-blog-article/SKILL.md](./skills/oginify-blog-article/SKILL.md)（v1.0.0 · 渐进式加载 · 自包含）

**触发语**：

```
按 oginify-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Ranking|Comparison|HowTo|Glossary|SizeGuide|MetaGuide|Alternative|ToolGuide|DeveloperGuide|UseCase|TrendAnalysis|OpenSourceGuide|Announcement} 文章。
Track：{S|T|auto}。发布目的：{SEO|品牌|转化|趋势}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

**工作流**（9 Phase + 5 Gate + 六角色换帽）：

```
Phase 0 — Intake & Gate A      (Strategist)
Phase 0R — Research 三角       (Researcher)
Phase 1 — Article Brief        (Strategist + SME)
Phase 2 — Slug & Gate B        (Strategist + SME)
Phase 3 — Outline              (Strategist + SME)
Phase 3.5 — Outline 交叉检查   (同批 ≥2 篇强制)
Phase 4 — Draft                (Writer)
Phase 5 — SelfCheck & Gate C   (Editor / Auditor)
Phase 5.5 — Cross-Article Audit(同批 ≥2 篇强制)
Phase 6 — Delivery             (Editor / Auditor)
```

**机器检查**：Gate C 前执行 `tools/` 下三个 Python 脚本（frontmatter / 字数 / 链接）。

新文章文件序号：当前下一号为 **02**（见 `references/content-graph.md`）。成稿后请更新下方「博客文章」表。

---

## 博客文章

| 序号 | 文件 | Slug | 类型 | 词数 | 状态 | 说明 |
|:---:|------|------|------|------|:---:|------|
| 01 | [01-best-ai-og-image-generators.md](./01-best-ai-og-image-generators.md) | `best-ai-og-image-generators` | Ranking | ~3.5k | ✅ | 三分类框架（URL-first / 通用生图 / 代码驱动）+ Oginify #1 + 每竞品优势 |

---

## 主题簇

### Open Graph Image 系列（Hub-Spoke）

```
                    ┌──────────────────────────────────────────┐
                    │  02 what-is-open-graph-image (Hub)       │
                    │  Glossary — category definition          │
                    └────────────────────┬─────────────────────┘
                                         │
        ┌────────────────────────────────┼───────────────────────────────┐
        │                    │                    │             │
  ┌─────▼──────┐   ┌─────────▼───────┐   ┌────────▼───────┐   ┌─────▼──────────┐
  │ 01 Ranking │   │ 03 HowTo        │   │ 04 SizeGuide   │   │ 05 MetaGuide   │
  │ best AI    │   │ how to create   │   │ og image size  │   │ og:image tags  │
  │ OG gens    │   │ OG image        │   │ (Track T)      │   │ + validator    │
  └────────────┘   └─────────────────┘   └────────────────┘   └────────────────┘
```

**P0 关键词覆盖**：best AI open graph image generator · open graph image size · what is open graph image · og image generator。

**发布节奏**：01（08-15）→ 02 Hub → 03 HowTo → 04 SizeGuide（Track T）→ 05 MetaGuide。

---

## 命名与 Frontmatter

| 约定 | 说明 |
|------|------|
| 文件 | `NN-{slug-kebab}.md`，常青 slug 不含年份；与现网 `slug` 一致 |
| `slug` | 不含年份、不含禁词（framework/strategy/guide/diagnosis/complete），search-intent-first |
| 语言 | 主站/博客为英文，上线稿为英文 |
| `date` | 每自然日 ≤1 篇，错开分配 |
| `articleFormat` | Ranking 文必填 `Ranking` |

```yaml
---
title: "Title Case — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword for SERP"
slug: "kebab-case-slug"
date: 2026-08-XX
author: "Oginify"          # Oginify | Kostja | {具体成员}
category: "Tutorial | Guide | Case Study | Reference | Product"
secondary_category: "Open Graph"
articleFormat: "Ranking | —"
---
```

> **2026-08-15 起**：frontmatter 不含 `image` / `keywords` / `related`（图片由 CMS/OG 单独管理）。正文不设 `## Related articles` 区块；内链全部为上下文内链。

---

## 写作标准

来自加权 12 维模板体系，所有文章统一遵循：

| 维度 | 约束 |
|------|------|
| **产品提及比例** | Glossary ≤20% · Ranking ≤40% · HowTo ≤40% · UseCase ≤50% |
| **竞品公平性** | 每竞品 ≥1 优势；禁用 "just a" / "merely" / "only does X"；每文 ≥1「何时不选 Oginify」 |
| **声调** | Practitioner-grade，Calm but opinionated；禁 AI hype / vendor puffery / generic SaaS / fake neutrality |
| **首段** | 1–3 句说清主题和对谁有用；不埋导语 |
| **列表比例** | Glossary ≤25% · Ranking/HowTo ≤35% · Track T ≤40% |
| **长段落** | ≥3 个长段落（4–8 句）；段落长度标准差 ≥1.5 |
| **FAQ** | 固定 6 题，覆盖反对意见 |
| **内链** | body 内 ≥2 个 blog 互链；Spoke 链回 Hub；禁用 "click here" |
| **CTA** | 每篇单一主行动，≤2 次 |
| **禁止模式** | "table + one sentence" 反模式；连续 3+ 短段落簇；"Imagine…" 开头 |
| **模块顺序** | YAML → TL;DR → H2 body → Conclusion → FAQ |
| **合规** | 不声称"全球首个"；不称竞品 dead/failed；产品数字 as-of；1200×630 规格有来源 |

---

## 跨文章一致性（Open Graph Image 系列）

| 概念 | Canonical 文章 | 引用文章 |
|------|---------------|---------|
| Open Graph image 定义 | 02 (Hub) — H2 "What Open Graph Image Actually Is" | 01, 03, 04, 05 |
| 1200×630 规格 | 02 (Hub) H2 + ogp.me | 01, 04, 05 |
| URL-first vs 通用生图 vs 代码驱动 | 01 — H2 "How This Ranking Works" | 03, 05 |
| OG 尺寸指南 | 04 — H2 "Platform-by-platform breakdown" | 05 |
| meta tags 设置 | 05 — H2 "The meta tags that control your preview" | 03 |

---

## 外部关联文档

| 文档 | 用途 |
|------|------|
| [oginify.com](https://oginify.com/) | 产品官网（机制、定价、工具页） |
| [oginify.com/pricing](https://oginify.com/pricing) | 定价 as-of 来源 |
| [social-cards-skills (GitHub)](https://github.com/kostja94/social-cards-skills) | 开源版事实来源 |
| [ogp.me](https://ogp.me/) | Open Graph 协议规格来源 |
