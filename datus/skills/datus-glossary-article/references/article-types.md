# Datus Glossary — 文章类型与 H2 模板

> Phase 0 / Phase 3 / Phase 4 按需加载。本 skill **仅** 产出以下 2 类。

---

## 1. 类型路由表

| 类型 | category | 路由信号 | 词数 | Datus 占比 | Slug 模式 | 样稿 slug |
|------|----------|---------|------|-----------|----------|-----------|
| **GlossaryTerm** | Glossary | `what is` / 单术语定义 | 2200–3200 | ≤15% | `what-is-{term}` | `what-is-text-to-sql` |
| **GlossaryComparison** | Glossary | `X vs Y` / `difference between` | 2400–3400 | ≤15% | `{a}-vs-{b}` | `semantic-layer-vs-ontology` |

**禁止产出**：`category: Data Engineering Agent`、`Semantic Layer` 榜单文、Tutorial、Comparison 榜单、Case Study、Tools List。

**自动路由**：

- 含 `vs` / `versus` / `difference between` + 两概念 → GlossaryComparison
- 含 `best` / `tools list` / `directory` / `complete list of` → **STOP**，改用 `datus-blog-article` / ToolsList（勿用本 skill 硬写）
- 其余 glossary 选题 → GlossaryTerm

---

## 2. 全类型通用模块

| 模块 | 要求 |
|------|------|
| **H1** | `# {Title}` — 含 primary keyword |
| **Excerpt** | H1 下方 1–2 句简短摘要（30–50 词）；含 primary keyword；概述文章覆盖范围 |
| **TL;DR** | `## TL;DR` — 5 bullets；第 1 条含 snippet-ready 定义 |
| **H2 编号** | `## 1.` … `## N.`；Conclusion / FAQ 不编号 |
| **Conclusion** | `## Conclusion` |
| **FAQ** | `## Frequently asked questions` — ≥3 个 `###` 问答 |
| **内链** | blog ≥2；glossary ≤3；锚文本语义化 |
| **外链** | 2–5 条；HTML `<a href="..." rel="nofollow noopener">` |
| **长段落** | ≥3 段，每段 4–8 句；避免 table+one-sentence 空壳 |

---

## 3. GlossaryTerm — H2 模板

**叙事弧线**：定义 → 边界/对比 → 动机 → AI/agent 连接 → 深度（实现/案例/检查清单）→ 结论。

| § | H2 模板 | Target words | Notes |
|---|---------|-------------|-------|
| Excerpt | `# {Term}: {Subtitle}` 后 1–2 句 | 30–50 | 含 primary keyword；概述文章内容 |
| TL;DR | 5 bullets | 120 | bullet 1 = 定义 |
| 1 | `{Term}: a working definition` | 400–500 | **canonical 节**；含 blockquote 定义 + 具体例子 |
| 2 | `{Term} vs {Related A} vs {Related B}` | 350 | 对比表 |
| 3 | Why organizations {build/use/care about} {term} | 350 | 失败模式 / 动机 |
| 4 | How {term} connects to {AI / data engineering agents} | 350 | 链 hub：`what-is-data-engineering-agent` |
| 5–7 | 深度节（按术语定制） | 300–400 each | 实现、pipeline、checklist、case walkthrough |
| — | Conclusion | 120 | 收束定义 + 可靠性要点 |
| FAQ | ≥3 题 | 400 | ≥1 边界/objection 题 |

**GlossaryTerm 深度节选题库**（按术语选 2–3 个）：

- Pipeline / architecture diagram（四阶段、多层模式）
- Evaluation checklist
- Case walkthrough（wrong answer → context fix）
- Common implementations（vendor 中立）
- When X is enough — and when it is not

**Datus 出现位置**：§5–7 或 FAQ 前「工具/生态」段，≤3 段；不在 §1–2。

---

## 4. GlossaryComparison — H2 模板

**叙事弧线**：两概念各自定义 → 对比表 → 决策框架 → agent 语境 → 误解澄清。

| § | H2 模板 | Target words | Notes |
|---|---------|-------------|-------|
| Excerpt | 简短摘要（1–2 句） | 30–50 | 概述两个概念 + 文章覆盖范围 |
| TL;DR | 5 bullets | 120 | 各概念一句 + 关系一句 |
| 1 | `{Term A}: a working definition` 或 quick recap | 350 | 若 A 有 canonical → 1–2 句 + link |
| 2 | `{Term B}: a working definition` | 350 | 同上 |
| 3 | Side-by-side comparison table | 200 | ≥6 行维度 |
| 4 | When to use A vs B | 350 | 决策框架 / 场景表 |
| 5 | How both relate to {data engineering / AI agents} | 350 | 链 relevant glossary blogs |
| 6 | Common misconceptions | 300 | FAQ 前置材料 |
| — | Conclusion | 120 | |
| FAQ | ≥3 题 | 400 | |

**Cannibalization 规则**：

- Term A/B 若已有 `what-is-*` canonical → §1/§2 仅 recap（≤150 词）+ link，不重写全文
- 对比文本身成为该对比 intent 的 canonical

---

## 5. Frontmatter Schema

```yaml
---
title: "What Is {Term}? Definition, {Scope} & {Hook}"
description: "120–160 chars: definition + intent + differentiation"
slug: "what-is-{term}"          # 常青，不含年份
date: 2026-06-XX            # 发布时间，永不改变
updated: 2026-06-XX         # 可选；最近一次实质性内容更新；无更新则省略
author: "Kostja"
category: "Glossary"
---
```

> **2026-08-11 起废弃**：`image` 字段不再写入 frontmatter（图片由 CMS/OG 单独管理）。

**GlossaryComparison title 公式**：`{A} vs {B}: {Decision Frame} & {Agent/DE Hook}`

> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅**实质性更新**时更新，错别字/样式不动它。页面**只显示一个日期**（有 `updated` 显示它）——勿同时显示两个日期（实证导致 CTR 下跌）。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。

---

## 6. Title 公式

| 类型 | 公式 | 示例 |
|------|------|------|
| GlossaryTerm | `What Is {Term}? Definition, {Scope} & {Differentiator}` | What Is Text-to-SQL? Definition, How It Works & Why Context Matters |
| GlossaryComparison | `{A} vs {B}: {Difference Frame} & {Why It Matters}` | Semantic Layer vs Ontology: What's the Difference and Why It Matters for AI Agents |
