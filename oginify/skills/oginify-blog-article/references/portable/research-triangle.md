# Research Triangle — Phase 0R 研究三角

> 便携参考 · Phase 0R 使用

---

## 1. 流程

```
R1 — 读项目文档（project-config + product-competitors + content-graph + proof-library）
    ↓
R2 — Web 搜索（primary keyword → SERP Top 5 + PAA）
    ↓
R3 — Fetch URL（官方页 oginify.com + SERP Top 3–5 原文提取）
    ↓
Synthesis Statement（洞察合成）+ Candidate Examples（≥1）
    ↓
输出 Research Log + SERP Fit 表
    ↓
Gate 0R Pass → Phase 1 Brief
```

---

## 2. Mode 差异

| R 步骤 | lite | standard | flagship |
|--------|------|----------|----------|
| R2 Top5 | 可选 | ✅ | ✅ |
| R3 Top3–5 | 可选 | Top3 | Top5 + 官方页 |
| Synthesis | 简版（1–2 句） | 完整 | 完整 + Moat 验证 |
| Candidate Examples | 0–1 | ≥1 | ≥2 |

---

## 3. Gate 0R

- **Gate 0R-6**：One-line thesis 不得在 SERP Top5 找到同句。
- **Degraded 模式**：WebSearch 不可用时标注 `Research mode: Degraded`；用竞品 URL + content-graph 推演 SERP Fit；政策/定价类 P0 claim 不得写未验证数字。
- **阻断**：R2 未搜 / R3 未 Fetch / 无 Synthesis / 事实不可验证且需写 P0 claim → 回退补 R2/R3 或 STOP。

---

## 4. Research Log 格式

```markdown
## Research Log — {slug}

### R1 — 项目文档
- product-competitors: {关键事实}
- content-graph: {定位}
- proof-library: {Proof IDs}

### R2 — Web 搜索
- Top 1: {URL}
- Top 2: {URL}
- Top 3: {URL}
- PAA: {3 items}

### R3 — Fetch 验证
- 官方页 oginify.com: {验证事实}
- 竞品页: {验证事实}

### Synthesis
{One-line thesis + 洞察}

### Candidate Examples
1. {example}
```

---

## 5. SERP Fit 表

见 `serp-fit-template.md`（SERP Fit 模板）。
