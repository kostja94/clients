# Phase 0R — Research 三角 + 洞察合成

> **随 skill 分发，不依赖仓库外路径。** · portable v1.1 · 2026-07-06

---

## 流程

```
R1 项目 SSOT → R2 搜索 → R3 Fetch
→ Synthesis Statement（必填）
→ Candidate Examples（推荐）
→ Research Log + SERP Fit → Gate 0R → Brief
```

---

## R1 — 读项目文档

Agent 读取 skill 文件夹内项目事实来源：
- `references/project-config.md`（品牌、G1–G7、URL 白名单）
- `references/product-competitors.md`（产品事实 + 竞品矩阵）
- `references/content-graph.md`（已有文章 + Canonical Registry）

---

## R2 — Web 搜索

`WebSearch` primary keyword → 收集：
- SERP Top 5 URL + 标题
- People Also Ask 问题列表
- 搜索意图类型确认（Definition / Comparison / Tutorial / Alternative / Commercial）

---

## R3 — Fetch

`WebFetch` 提取原文：
- 竞品官方页面（≥1）
- SERP Top 3 文章全文
- Clink 官方页 https://clinkbill.com/

---

## Synthesis Statement（Gate 0R 必填）

1. **SERP 未说的**：Top 5 没有说清/说错的什么？  
2. **一句话论点**：Top 5 **找不到同句**？（能 → 重新合成或 STOP）  
3. **读者改变**：读完后想法/行为的**具体**改变？  

每条论断须指向 Log §Fetched 或 R2。

---

## Information Gain 三问（Synthesis 后）

| # | 问题 |
|---|------|
| IG-1 | 核心 claim 能否贴进另外 10 篇同类文？ |
| IG-2 | 删掉本篇，网上会少实质性信息吗？ |
| IG-3 | 前 30% 能否用 40–60 词独立成段？（→ `extractability-checklist.md`） |

---

## Candidate Examples

| 例子 | 来源 | 适合证明 | 具体性 OK? |

禁止模糊案例（「某社区…」）；优先 Log §Fetched 来源。

---

## Research Log 模板

```markdown
## Research Log

### R1 — Internal
- Project config loaded: ...
- Content graph: N articles, next NN = ...
- Product facts verified: ...

### R2 — SERP
| # | URL | Title | Covers | Note |
|---|-----|-------|--------|------|

### R3 — Fetched
| # | URL | Key extract | Date fetched |
|---|-----|------------|-------------|

### Synthesis
{三要素 + IG 三问}

### Candidate Examples
| Example | Source | Relevance |
|---------|--------|-----------|
```

---

## Degraded 模式

当 WebSearch 不可用时标注 `Research mode: Degraded — {reason}`。
- 不得写 P0 级未验证 claim
- 每个基于推理的断言须用限定词（"likely"、"emerging"、"in our observation"）
- 不确定事实标 `[internal observation]`

---

## Gate 0R

G0R-1–5：SSOT、SERP、Fetch、增量。 **G0R-6**：Synthesis + IG 三问。

---

*research-triangle · portable v1.1*
