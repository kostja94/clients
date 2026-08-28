---
name: datus-blog-article
description: >
  Create and structure datus.ai blog articles from brief to English draft.
  Self-contained unified skill — all article types (Glossary, ToolsList,
  Research, Comparison, Product, Tutorial, Pillar) routed by content intent,
  not by separate glossary vs blog skills. 9 Phase workflow, cluster-folders
  layout, portable audit bundle, validation tools. Complements datus-blog-audit.
metadata:
  version: 2.0.0
  project: datus.ai
  locale: en
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 560
  complements: datus-blog-audit
  forbidden-reads:
    - ../../datus.md
    - ../../datus-*.md
    - ../../blog/README.md
    - ../../blog/internal-external-links-checklist.md
---

# Datus Blog Article Creation

为 **https://datus.ai/blog/** 从选题到英文成稿。**单一 skill 覆盖全部体裁**——按 **内容意图** 路由 ArticleType，不再区分 glossary skill / blog skill。

**硬性规则**：Agent 只读本 skill 文件夹（`references/`、`references/portable/`、`tools/`、`evals/`）。禁止读取 `forbidden-reads` 列表中的仓库文档。发布前终审 → `references/portable/final-audit.md` 或 `datus-blog-audit` skill。

**渐进式加载**：默认只读本文件。Phase 需要细节时，按指针读 `references/{file}.md`（**一次最多 2 个**）。

**六角色换帽**：0/0R Strategist+Researcher · 1–3 Strategist+SME · 4 Writer · 5 Editor/Auditor

---

## §0 如何使用

### 触发语

```
按 datus-blog-article skill，为关键词 "{primary keyword}" 创建一篇博客文章。
ArticleType：{可选；未给则按内容推断}
Mode：{lite|standard|flagship，默认 standard}
Cluster：{data-agent|data-engineering-agent|semantic-layer|osi|features|standalone}
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主关键词 / 主题 | ✅ | 决定 ArticleType + SERP |
| ArticleType | 可选 | **未给则 Agent 按 §2 从内容推断并告知** |
| Mode | 可选 | 默认 standard；见 §1B |
| Cluster | 推荐 | 决定 `category` + 文件子目录 |
| 竞品 SERP URL | 推荐 | Phase 0R |

### 输出（Phase 6，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief | ✅ | ✅ | ✅ |
| 2 | Research Log | 简 | ✅ | ✅ |
| 3 | 成稿 `datus/blog/{cluster}/NN-{slug}.md` | ✅ | ✅ | ✅ |
| 4 | SelfCheck（H0–H4 + 12 维） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | Internal Link Plan | — | ✅ | ✅ |
| 8 | 终审指令（final-audit.md） | ✅ | ✅ | ✅ |
| 9 | 提示人类更新 blog/README | ✅ | ✅ | ✅ |

与用户沟通可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 已有成稿，仅终审 | `datus-blog-audit` 或 `portable/final-audit.md` |
| 仅改 title/description | 未来 meta skill；禁止改正文 |
| 非 datus.ai 博客 | 其他项目 skill |

---

## §1 项目配置速查

> **完整配置 → `references/project-config.md`**
> **产品事实 → `references/product-competitors.md`**
> **Cluster 路径 → `references/topic-cluster-layout.md` + `content-graph.md`**

| 配置项 | 值 |
|--------|-----|
| **blogLayout** | cluster-folders |
| **下一序号 NN** | **55** |
| **默认作者** | Kostja |
| **URL** | `/blog/{slug}`（无子目录前缀） |

**G1–G7** 全类型阻断；体裁专属 Gate 见 `project-config.md` §3–§6。

---

## §1B Mode 系统

| Mode | 适用 ArticleType | Phase 深度 |
|------|------------------|-----------|
| **lite** | Product 短讯 | 最小 0R |
| **standard** | ToolsList, Comparison, Tutorial | 完整 0R + Extractability |
| **flagship** | Glossary*, Research, Pillar | 全流程 + Moat + Excellence |

\*GlossaryTerm / GlossaryComparison 默认 flagship。

用户未指定 Mode → **standard**（Glossary 类默认 flagship）。

---

## §2 文章类型路由（基于内容）

> **完整路由表 + H2 模板 → `references/article-types.md`**

**Phase 0 必须先输出**：

```
## Mode: {lite|standard|flagship}
## ArticleType: {type}          ← 由内容意图推断或用户指定
## category: {cluster enum}
## secondaryCategory: {Glossary|Research|Comparison|ToolsList|Product}
## Cluster: {cluster-id | standalone}
## File path: blog/{cluster}/NN-{slug}.md
## Gate A: KEEP | MERGE → {slug} | STOP
```

### 路由优先级（摘要）

1. Product → `introducing` / 产品发布
2. ToolsList → `best` / tools list / directory
3. GlossaryComparison → 两**概念**对比
4. Comparison → 产品/平台对比
5. GlossaryTerm → `what is` / 术语
6. Tutorial → step-by-step / build your first
7. Research → 深度指南 / vendor 深潜
8. Pillar → 品类 Hub + 多产品框架

**禁止**：因「是 glossary 词」就固定走旧 skill；**一律**在本 skill 内按 ArticleType 选模板与 Gate。

---

## §3 创作工作流（9 Phase + 5 Gate）

```
Phase 0  — Intake & Gate A
Phase 0R — Research 三角 & Gate 0R
Phase 1  — Article Brief
Phase 2  — Slug, Path, Date & Gate B
Phase 3  — Outline
Phase 3.5— Outline 交叉检查（同批 ≥2 篇）
Phase 4  — Draft
Phase 5  — SelfCheck & Gate C
Phase 5.5— Cross-Article Audit（同批 ≥2 篇）
Phase 6  — Delivery
```

> Investment Score → `references/portable/investment-score.md`
> Research 三角 → `references/portable/research-triangle.md`
> Gate 细则 → `references/portable/gates-master.md`

### Phase 0 — Intake & Gate A

**加载**：`content-graph.md` + `glossary-terms.md`（若 Glossary 相关）

**必问**：主关键词 · 与已有文关系（Hub/Spoke）· SERP Top 3 · Cluster

**Gate A**：三条件满足 ≥2 → KEEP；术语已有 canonical → MERGE（输出 slug 并 STOP）

**信息增量**：相对 SERP ≥1 项（standard/flagship ≥2）

### Phase 0R — Research

R1 项目文档 → R2 Web SERP → R3 Fetch Top3–5 → Synthesis + SERP Fit（`serp-fit-template.md`）

### Phase 1 — Brief

须含：ArticleType、category、secondaryCategory、Moat、Internal links、KEEP/MERGE。范例 → `mini-example.md`

### Phase 2 — Slug & Path

**加载**：`slug-gate.md` + `article-types.md` + `topic-cluster-layout.md`

- slug 常青、无年份
- 路径与 Cluster 注册表一致
- NN = content-graph 下一序号（当前 **49**）

### Phase 3 — Outline

按 **ArticleType** 选 H2 模板（`article-types.md` §4）。须含 TL;DR、编号 H2、Conclusion、FAQ。

### Phase 4 — Draft

**加载**：`presentation.md` + `product-competitors.md`（≤2 文件/轮）

flagship 额外：`extractability-checklist.md` + `perfect-article-checklist.md`

BLUF：TL;DR + 每 major H2 首段 + FAQ 首句。段落优先 → `presentation-rhythm.md`

### Phase 5 — SelfCheck

> **`references/selfcheck.md`** + `tools/` 三脚本

Gate C 全 Pass → **audit-ready**

### Phase 6 — Delivery

1. 写入成稿
2. Brief + SelfCheck + Source Map
3. 复制终审指令：

```markdown
请按 datus-blog-audit skill（或 references/portable/final-audit.md）终审：
- 文件：{path}
- ArticleType：{type}
- 主关键词：{kw}
- SelfCheck：{Pass}/12
```

4. 提示人类更新 `blog/README.md`

---

## §4 文档索引

| 文件 | 加载时机 |
|------|----------|
| `references/project-config.md` | 0, 5 |
| `references/article-types.md` | 0, 2, 3, 4 |
| `references/content-graph.md` | 0, 2, 3 |
| `references/glossary-terms.md` | 0（Glossary 体裁） |
| `references/product-competitors.md` | 0R, 4, 5 |
| `references/presentation.md` | 4 |
| `references/presentation-rhythm.md` | 4, 5 |
| `references/selfcheck.md` | 5 |
| `references/slug-gate.md` | 2 |
| `references/citations.md` | 4, 5 |
| `references/eeat-framework.md` | 4, 5 |
| `references/topic-cluster-layout.md` | 0, 2 |
| `references/portable/*` | 按 Phase 指针 |
| `tools/README.md` | 5 |

---

## Gotchas

**流程**：❌ Gate 未 Pass 交付 · ❌ 一次加载全部 references · ❌ 读 forbidden-reads

**路由**：❌ 因文件夹名假设 ArticleType · ❌ ToolsList 写 `category: Glossary` · ❌ Glossary 体裁忽略 D1

**结构**：❌ FAQ 复制正文 · ❌ slug 含年份 · ❌ 内链 `/blog/{cluster}/{slug}`

**写作**：❌ P0 数字无来源 · ❌ POC 写 GA · ❌ 贬低竞品

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **2.0.0** | 2026-08-28 | 合并 `datus-glossary-article` + 旧 `datus-blog-article`；对齐 blog-create/blog-audit 通用架构；内容意图路由 ArticleType；cluster-folders；portable/ + tools/ + selfcheck |
| 0.1.0 | 2026-07-20 | 旧 blog skill：仅 ToolsList MVP |
| 2.0.0 | 2026-06-15 | 旧 glossary skill（已废弃） |

---

*datus-blog-article · v2.0.0 · 2026-08-28 · unified · self-contained*
