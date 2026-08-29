# ThetaWave blog

English Markdown articles for **thetawave.ai** live in this folder (`*.md` with YAML frontmatter), aligned with the public URL pattern **`/blog/{slug}`**（见 [thetawave.md](../thetawave.md) §5）。**韩文 Naver 等渠道成稿** 放在 [`../localization/`](../localization/readme.md)，**不要**与自站 `blog/` 混放。Markdown 可导入支持 YAML 的 CMS。

**Keywords, feature mapping, and topic ideas**: [thetawave-keywords.md](../keywords/thetawave-keywords.md) · **Feature landing URLs**: [thetawave-features.md](../thetawave-features.md).

**Internal & external linking（中文规范）**: [internal-external-links-checklist.md](./internal-external-links-checklist.md)（与 Nori / Lessie 同一思路，站点路径已替换为 ThetaWave）。

**Blog 组件与迁移规范（作者页 / FAQ / Final CTA / 上下文内链）**: [thetawave-blog-components-spec.md](../archive/thetawave-blog-components-spec.md) — UI 组件与构建管道参考；**Blog 结构与 frontmatter 以 [blog-article SKILL](../skills/blog-article/SKILL.md) v2.2.3 为准**（`## Key takeaways` → `## Introduction` → 正文 H2；FAQ 仅正文；YAML 不含 `faq` / `keywords` / `final_cta` / `related`）。

---

## 创作 Skill 与质量审核

| 阶段 | 工具 | 路径 |
|------|------|------|
| **选题 → 成稿（英文 blog/）** | ThetaWave 博客文章创作 Skill | [../skills/blog-article/SKILL.md](../skills/blog-article/SKILL.md) |
| **title / description 专项** | Meta Title & Description Skill | [../skills/meta-title-description/SKILL.md](../skills/meta-title-description/SKILL.md) |
| **发布前终审** | 十维内容质量审核 | [`blog-audit/README.md`](../../skills%20for%20clients/blog-audit/README.md) |

**工作流**：先用 **blog-article** Skill 走 Phase 0–7（Brief → Outline → Draft → SelfCheck），成稿 **audit-ready** 后按 [`blog-audit/README.md`](../../skills%20for%20clients/blog-audit/README.md) 做 P0 Gate + **十维评分**。仅需优化 SERP metadata 时用 **meta-title-description**。

**Agent 用法**：

```
按 thetawave-blog-article skill，为关键词 "{primary keyword}" 创建一篇 {Commercial|Alternative|StudyMethodSpoke|HowTo} 文章。
```

创作 Skill **完全自包含**（v1.0.0，locale: en）——Agent 只需读 `../skills/blog-article/SKILL.md`。**不含** `blog-kr/`（韩文另建 Skill）。

新文章文件序号：当前下一号为 **15**（见 Skill §4.1）。成稿后请更新下方「Published drafts」表与 [internal-external-links-checklist.md](./internal-external-links-checklist.md)。

---

## 目录结构

| 路径 | 说明 |
|------|------|
| [`*.md`](./) | 单篇草稿与已发布镜像（除本说明与检查清单） |
| [readme.md](./readme.md) | 本文件：维护说明、Frontmatter 参考、已发布登记表 |
| [internal-external-links-checklist.md](./internal-external-links-checklist.md) | 内外链分层、竞品 nofollow、E-E-A-T |
| [blog-kr/](./blog-kr/readme.md) | 韩文站内博客（`/ko/blog/{slug}`），与英文 `blog/` 及外部 Naver 分目录 |

---

## Frontmatter 示例（v2.2.3 — 见 [blog-article SKILL](../skills/blog-article/SKILL.md) §2.9）

```yaml
---
title: "How to Turn Notes Into a Podcast for Studying"
description: "Meta description for SERP; 150–160 characters where possible."
slug: "turn-notes-into-podcast"   # 不含年份，常青 URL → /blog/turn-notes-into-podcast
date: 2026-06-16
author: "Thetawave Team"
author_slug: "thetawave-team"   # kostja | thetawave-team → /blog/author/{slug}
image: "/blog/images/turn-notes-into-podcast-2026.jpg"
category: "Product"             # Research | Comparison | Product | Reference
---
```

**字段说明**

- `title` / `description`：SEO 标题与 meta description。
- `slug`：与线上 **`/blog/{slug}`** 一致。
- `category`：**必填**；与文章类型路由见 Skill §2.9。
- `author` + `author_slug`：byline 可点击链至 `/blog/author/{author_slug}`。
- **Key takeaways**：`## Key takeaways` = TL;DR，正文**第一块**；≥3 bullet。
- **Introduction**：`## Introduction` 必填，Key takeaways 之后；BLUF + 路线图；Introduction 首段 ≥1 内链。
- **FAQ**：只写在正文 `## Frequently Asked Questions`（≥3 题），**不要**放入 YAML。
- **禁止**：`keywords`、`related`、`faq`、`final_cta`、`faq_subtitle`、文首 Disclosure 段。

---

## 部署提示

将 `blog/` 配置为内容源，`slug` → `https://thetawave.ai/blog/{slug}`。图片与路由以生产站 [thetawave-production-routing.md](../tech-stack/thetawave-production-routing.md) 为准。

---

## 关联文档

| 文档 | 用途 |
|------|------|
| [thetawave.md](../thetawave.md) | 产品语境、核心页 URL |
| [thetawave-keywords.md](../keywords/thetawave-keywords.md) | 关键词与目标页 |
| [thetawave-features.md](../thetawave-features.md) | 10 个功能落地页路径 |
| [thetawave-use-cases.md](../thetawave-use-cases.md) | Use Cases 路径（博客可互链） |
| [thetawave-competitors.md](../thetawave-competitors.md) | 竞品与对比稿素材 |
| [thetawave-blog-components-spec.md](../archive/thetawave-blog-components-spec.md) | 作者页、SiteFAQ、FinalCTA、上下文内链（UI）；frontmatter 见 Skill |
| [../skills/blog-article/SKILL.md](../skills/blog-article/SKILL.md) | 英文博客创作 Skill（Brief → 成稿 → SelfCheck） |
| [../skills/meta-title-description/SKILL.md](../skills/meta-title-description/SKILL.md) | 全站 title / description 优化 |
| [`blog-audit/`](../../skills%20for%20clients/blog-audit/) | 十维内容质量审查（成稿后终审） |

---

## When adding a new post

1. Add `NN-{slug-kebab}-2026.md` with frontmatter per [blog-article SKILL](../skills/blog-article/SKILL.md) §2.9：`category` 必填；推荐 `author_slug`；FAQ 仅正文；**不要**使用 `keywords` / `related` / `faq` / `final_cta` / `faq_subtitle`。
2. Ensure **`slug`** matches the path segment: `/blog/{slug}`（常青 slug 一般**不含**年份，与 Nori 稿一致）。
3. After publish, confirm the URL appears in **`https://thetawave.ai/blog/sitemap.xml`**（若已配置）并在相关功能页 / Use Cases 互链；并按 [internal-external-links-checklist.md](./internal-external-links-checklist.md) 更新链接状态表。

---

## Published drafts in this folder

| File | slug | `date` (publish) |
|------|------|------------------|
| [01-best-ai-note-takers-2026.md](./01-best-ai-note-takers-2026.md) | `best-ai-note-takers` | 2026-04-16 |
| [02-quizlet-alternatives-2026.md](./02-quizlet-alternatives-2026.md) | `quizlet-alternatives` | 2026-04-20 |
| [03-chatgpt-alternatives-2026.md](./03-chatgpt-alternatives-2026.md) | `chatgpt-alternatives` | 2026-04-20 |
| [04-cornell-note-taking-method-2026.md](./04-cornell-note-taking-method-2026.md) | `cornell-note-taking-method` | 2026-05-18 |
| [05-how-to-take-notes-in-college-2026.md](./05-how-to-take-notes-in-college-2026.md) | `how-to-take-notes-in-college` | 2026-05-18 |
| [06-how-to-study-for-finals-2026.md](./06-how-to-study-for-finals-2026.md) | `how-to-study-for-finals` | 2026-05-18 |
| [07-study-methods-compared-2026.md](./07-study-methods-compared-2026.md) | `study-methods-compared` | 2026-05-18 |
| [08-mind-mapping-method-2026.md](./08-mind-mapping-method-2026.md) | `mind-mapping-method` | 2026-05-18 |
| [09-zettelkasten-method-2026.md](./09-zettelkasten-method-2026.md) | `zettelkasten-method` | 2026-05-18 |
| [10-feynman-technique-2026.md](./10-feynman-technique-2026.md) | `feynman-technique` | 2026-05-18 |
| [11-sq3r-method-2026.md](./11-sq3r-method-2026.md) | `sq3r-method` | 2026-05-18 |
| [12-leitner-system-2026.md](./12-leitner-system-2026.md) | `leitner-system` | 2026-05-18 |
| [13-turn-notes-into-podcast-2026.md](./13-turn-notes-into-podcast-2026.md) | `turn-notes-into-podcast` | 2026-06-16 |
| [14-obsidian-notes-explained-2026.md](./14-obsidian-notes-explained-2026.md) | `obsidian-notes-explained` | 2026-07-28 |

---

*Folder prepared for blog-first drafts; extend the table as each post is added.*
