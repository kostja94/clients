# 文章结构 × Inline Markdown 映射

> **版本**：v2.0 · 2026-08-26  
> **格式**：`content/{channel}/{locale}/{slug}.md` — 全部章节 inline，无集中 JSON。

---

## 〇、内容优先原则（必读）

**文章架构由内容本身决定，本目录与 `templates/` 提供的是参考菜单，不是必填清单。**

| 层级 | 含义 | 示例 |
|------|------|------|
| **A 硬底线** | 违反即结构/SEO 错误，必须修复 | 结论在 FAQ 前；禁止 frontmatter `howTo:`；FAQ 若存在则 7 问且无内链 |
| **B 类型惯例** | 某 `articleType` 的常见做法，可因题材调整 | Best-ranking 通常有产品 H3 榜单；SEO 文通常有操作步骤节 |
| **C 参考模板** | 新建页时的起点，可增删改顺序 | 下文「参考菜单」10 节；`templates/best-ranking.md` 等 |

**决策流程**（Step 01 / 05 前）：

1. 读知识块 + Research，列出读者必须带走的信息（定义？对比？选型？场景？）
2. 对照 [`article-types.md`](./article-types.md) 与 [`templates/`](./templates/) 看**常见结构**
3. 画出本篇 H2 大纲：**只保留服务读者的节**；可合并（如「如何工作」并入「什么是」）、可省略（如无对比价值则去掉对比表）
4. 写完后用 [`quality-checklist.md`](./quality-checklist.md) 核对 **A 层**；B/C 层不足时说明理由即可

**中英 parity**：ZH/EN 的 **section 类型与顺序应对齐**（锚点 id 一致），但两边不必机械复制「是否凑满 10 节」——对齐的是**实际采用的架构**，不是模板行数。

**Flagship 质量**（Alignify 每篇固定）：架构可灵活，但 **Moat、Answer Blocks、Research、BLUF、SelfCheck、终审** 不可省略。见 [`gates.md`](./gates.md) · [`article-brief.md`](./article-brief.md)。

---

## 一、参考菜单（Tools 类常见，非强制顺序）

以下为 **best-ranking 新建页的高频结构**，其它类型见 [article-types.md](./article-types.md)。**可调整顺序、合并或省略**，只要 A 层底线满足。

| 序号 | 章节 | Markdown | 常见度 |
|------|------|----------|--------|
| 1 | 核心要点 / Key Takeaways | `## 核心要点 {#article-intro}` | 几乎总是 |
| 2 | 什么是 XXX | md section | 几乎总是 |
| 3 | 如何工作 / 概念 | md section | 常出现在 Tools |
| 4 | 主体（Best 榜单 / 策略节 / 分析节） | md section + H3 | **主体节几乎总是** |
| 5 | 对比表格 | html block 或 section 内 table | 有 2+ 同质产品时常用 |
| 6 | 应用场景 | md section + H3 | 视题材 |
| 7 | 如何选择 | md section + H3 步骤 | 选型类常用；纯概念文可省 |
| 8 | 结论 | `## 结论 {#conclusion}` | 几乎总是 |
| 9 | 常见问题 | `## 常见问题 {#faq}` + `###` 7 问 | 几乎总是 |
| 10 | 参考文献 | `## 参考文献 {#references}` | 有外部引用时建议 |

**A 层硬底线**（与是否采用上表每一行无关）：

- 若同时有 **结论** 与 **FAQ** → 结论必须在 FAQ **之前**
- 若有 **FAQ** → **7 问**，答案 plain text、无内链；中英文条数一致
- **禁止** frontmatter `howTo:`；HowTo 内容仅写在正文 `## 如何选择…` section
- **禁止** 独立 JSON / 全局组件注入 TL;DR、FAQ、References（须 inline 在 md）

---

## 二、Frontmatter

```yaml
---
title: "H1：不写年份，推荐「类型：核心价值」"
description: "三段式摘要，中文 80–150 字"
slug: "{slug}"
date: "2026年6月23日"
updated: "2026年6月23日"
readingMinutes: "18 分钟阅读"
pageUrl: "https://alignify.co/zh/blog/{slug}"
locale: "zh"
category: "coding-dev"
categorySecondary: ""
heroImage: "/blog/{slug}/hero.jpg"
heroImageAlt: "…"
---
```

- SEO title/description → `*-meta.ts`（与 frontmatter 主题一致、不必同文）
- `category` → Hub 归属（经 `ARTICLE_CATEGORY_MAP` 推导）

### H2/H3 锚点语法

```markdown
## 章节标题 {#kebab-case-id}
### 步骤标题 {#step-1}
```

| 规则 | 说明 |
|------|------|
| **格式** | 标题末尾空格 + `{#id}`；`markdown-doc.ts` 解析后 **id 不进可见标题** |
| **禁止** | 空锚点 `{#}` — 会泄漏字面量 `{#}` 到线上（E27） |
| **id 命名** | kebab-case、语义化；与 EN/ZH 同 slug 的 section 用**相同 id** |

---

## 三、Inline 章节示例

各节**写法**见 `sections/`；**是否采用**见 §〇 与 Step 01 大纲。

### 1. 核心要点

```markdown
<!-- block:section -->
## 核心要点 {#article-intro}

40–80 字 intro，直接回答页面核心问题…

- 要点 1（25–60 字）
- 要点 2
- 要点 3
- 要点 4
```

英文：`## Key Takeaways {#article-intro}`。规则见 [sections/tldr.md](./sections/tldr.md)。

### 2–7. 正文章节

```markdown
<!-- block:section -->
## 什么是 {工具类型} {#section-1}
…

<!-- block:section -->
## 2026 年最好的 {分类} {#best-{slug}-2026}
### 产品名 {#product-slug}
…
```

节名、数量、顺序 **按本篇大纲**，不必与参考菜单序号一一对应。

### 8. 结论

```markdown
<!-- block:section -->
## 结论 {#conclusion}
…
```

见 [conclusion.md](./conclusion.md)。

### 9. FAQ（7 问）

```markdown
<!-- block:section -->
## 常见问题 {#faq}

### 问题 1 {#faq-1}
答案（60–120 字，plain text，无内链）…

### 问题 2 {#faq-2}
…
```

英文：`## FAQ {#faq}` / `## Frequently Asked Questions {#faq}`。规则见 [sections/faq.md](./sections/faq.md)。

### 10. References

```markdown
<!-- block:section -->
## 参考文献 {#references}

- [Title](https://…) — 描述
```

规则见 [sections/references.md](./sections/references.md)。

---

## 四、按 articleType 的常见差异（建议，非清单）

| 节 | best-ranking | seo-guide | marketing-strategy | insights-analysis |
|----|-------------|-----------|-------------------|-------------------|
| 核心要点 | 常见 | 常见 | 常见 | 常见 |
| Best 榜单 H3 | 常见 | — | — | — |
| 策略/分析多节 | — | 常见 | 常见 | 常见 |
| 如何选择 | 选型类常见 | 可选 | 可选 | 可选 |
| FAQ 7 问 | 常见 | 常见 | 常见 | 常见 |

详情见 [article-types.md](./article-types.md) 与各 [templates/](./templates/)。

---

## 四·一、正文表格（blog md）

**禁止** GFM 管道表格（`| col |`）——`markdownToHtml` 不解析，会渲染成一行纯文本。

**必须** 使用 `<!-- childrenHtml:start -->` + HTML：

```markdown
<!-- childrenHtml:start -->
<div class="content-html"><table><thead>…</thead><tbody>…</tbody></table></div>
<!-- childrenHtml:end -->
```

或独立 `<!-- block:section -->` 内单行 `<div class="content-html">…</div>`（见 `web-fetch` 对比表）。

---

## 五、已废弃

- 独立 `tldr-data.json` / `faq-data.json` 注入（目标：md inline）
- `<!-- block:tldr -->` / `<!-- block:faq -->` / `<!-- block:references -->`
- frontmatter `howTo:`
- JSON block：`howItWorks` / `bestTools` / `useCases` / `howToChoose`
- React 组件：`BestTools.tsx` / `HowToChoose.tsx` 等已删组件

---

*anatomy · v2.0 · 2026-08-26*
