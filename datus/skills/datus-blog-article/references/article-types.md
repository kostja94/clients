# Datus Blog Article — 文章类型与 H2 模板

> Phase 1–3 按需加载。本 skill **本期仅** 产出 ToolsList。

---

## 1. 类型路由表

| 类型 | category（按主题簇） | 路由信号 | 词数 | Datus 占比 | Slug 模式 | 样稿 |
|------|---------------------|---------|------|-----------|----------|------|
| **ToolsList** | `Semantic Layer` 或 `Data Engineering Agent` | `best` / `tools list` / `directory` / `complete list` | 2800–4000 | ≤25% | `{topic}-tools-list` / `best-{topic}` | `semantic-layer-tools-list-osi`；`best-data-engineering-agents` |

**禁止产出**：`category: Glossary`、Tutorial、Case Study、vs 竞品长文（backlog）。

**自动路由**：

- `what is` / 单术语 → **STOP**，改用 `datus-glossary-article`
- `X vs Y` 两概念 → **STOP**，改用 `datus-glossary-article`
- `best` / `tools list` / `directory` → ToolsList

---

## 2. 全类型通用模块

| 模块 | 要求 |
|------|------|
| **H1** | `# {Title}` — 含 primary keyword |
| **Excerpt** | H1 下方 1–2 句（30–50 词）；含 primary keyword；概述覆盖范围 |
| **TL;DR** | `## TL;DR` — 5 bullets；第 1 条含规模/分类摘要 |
| **H2 编号** | `## 1.` … `## N.`；Conclusion / FAQ 不编号 |
| **Conclusion** | `## Conclusion` |
| **FAQ** | `## Frequently asked questions` — ≥3 个 `###` 问答 |
| **内链** | blog ≥2（含相关 hub）；glossary 聚合页可选 ≤1 |
| **外链** | 2–5 条；HTML `<a href="..." rel="nofollow noopener">` |
| **长段落** | ≥3 段，每段 4–8 句 |

---

## 3. ToolsList — H2 模板

**叙事弧线**：市场分类（散文）→ 唯一主对比表 → 评估维度深潜 → 选型框架 → AI/agent 连接 → 结论。

**参考样板**：`04-best-data-engineering-agents`（分类用长段，产品用 1 主表 + 可选 per-tool prose）。

| § | H2 模板 | Target words | Notes |
|---|---------|-------------|-------|
| Excerpt | H1 后 1–2 句 | 30–50 | 含 primary keyword |
| TL;DR | 5 bullets | 120–160 | bullet 1 = 数量 + 分类 |
| 1 | The {N} architecture / market categories | 450–600 | **散文分类**；每类 ≥1 中/长段；工具名嵌段落；**禁止每类一张产品表** |
| 2 | The full list: features, pricing, and {eval dimension} | 400–700 | **唯一产品目录主表**；表后 ≥3 句读表分析；可加简短 legend |
| 3 | What "{eval dimension}" actually means | 400–550 | 分级说明；可选 **1 张小状态表**（如 converter）或有序列表；参与方用 prose |
| 4 | How to choose / decision framework | 350–450 | 决策问题用有序列表；可选 **1 张场景→选型表**；禁止再铺产品目录表 |
| 5 | Why this matters for AI agents | 300–400 | 链 hub：`what-is-data-engineering-agent`；Semantic Layer 文另链 `what-is-semantic-layer` / OSI |
| — | Conclusion | 120–160 | 收束建议；链相关阅读（非 glossary 空泛 CTA） |
| FAQ | ≥3 题 | 400+ | 覆盖 PAA；独立内容 |

深度节可按主题定制（OSI、pricing、open-source 等），但 **不得增加第二张产品目录表**。

---

## 4. 表格硬预算（ToolsList）

| 规则 | 标准 |
|------|------|
| 全文表格总数 | **≤3** |
| 产品目录 / 全量对比栅格 | **恰好 1** |
| 允许的额外表 | 状态小表（converter）≤1；场景 scorecard ≤1 |
| 禁止 | 按 architecture 拆多张产品表 + 再一张全量汇总 |
| 每张表节奏 | 表前完整导语；表后 ≥2–3 句分析（禁止裸表格） |

**反模式（曾见于早期稿）**：§1 三张分类产品表 + §2 全量表 + converter 表 + WG 表 + scorecard = 表格轰炸。

---

## 5. Frontmatter Schema

```yaml
---
title: "{Topic} Tools in 2026: A Complete List and {Hook}"
description: "120–160 chars: scope + differentiation (e.g. OSI status)"
slug: "{topic}-tools-list-{hook}"   # 常青，不含年份
date: 2026-XX-XX            # 发布时间，永不改变
updated: 2026-XX-XX         # 可选；最近一次实质性内容更新；无更新则省略
author: "Kostja"
category: "Semantic Layer"          # or "Data Engineering Agent"
---
```

**禁止**：`category: "Glossary"`。

> **2026-08-11 起废弃**：`image` 字段不再写入 frontmatter（图片由 CMS/OG 单独管理）。
>
> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅**实质性更新**（新增数据/章节/修正事实）时更新，错别字/样式不动它。页面**只显示一个日期**（有 `updated` 显示它）——勿同时显示两个日期（实证导致 CTR 下跌）。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。

---

## 6. Title 公式

| 模式 | 公式 | 示例 |
|------|------|------|
| Complete list | `{Topic} Tools in {Year}: A Complete List and {Differentiator}` | Semantic Layer Tools in 2026: A Complete List and Their OSI Support Status |
| Best / honest comparison | `Best {Topic} in {Year}: An Honest Comparison` | Best Data Engineering Agents in 2026: An Honest Comparison |

Title 可含年份；**slug 不含年份**。

---

*article-types · ToolsList MVP · v0.1.0 · 2026-07-20*
