# FinalRound Research Triangle（Skill reference · portable）

> **Phase 0R Research 三角流程。** Gate A KEEP 之后、Brief 之前强制执行。

---

## 1. 目的

**不依赖模型记忆写事实**——在写作前收集外部证据。

## 2. 流程

```
R1 — 读 allow-extra-reads 项目文档（finalround.md + product-competitors + content-graph）
    ↓
R2 — Web 搜索（primary keyword → SERP Top 5 + PAA）
    ↓
R3 — Fetch URL（finalroundai.com 相关页 + SERP Top 3–5 原文提取）
    ↓
Synthesis Statement（洞察合成）+ Candidate Examples（≥1）
    ↓
输出 Research Log + SERP Fit 表
    ↓
Gate 0R Pass → Phase 1 Brief
```

## 3. Mode 差异

| R 步骤 | lite | standard | flagship |
|--------|------|----------|----------|
| R2 Top5 | 可选 | ✅ | ✅ |
| R3 Top3–5 | 可选 | Top3 | Top5 + 官方页 |
| Synthesis | 简版（1–2 句） | 完整 | 完整 + Moat 验证 |
| Candidate Examples | 0–1 | ≥1 | ≥2 |

## 4. Degraded 模式

R2/R3 缺失时标注 `Research mode: Degraded — {reason}`。Degraded 下正文**不得**写 P0 级未验证 claim。

## 5. 输出

### Research Log

```markdown
## Research Log
- R1: {读到的项目事实摘要}
- R2: {SERP Top 5 + PAA 摘要}
- R3: {Fetch 的官方页 + Top3–5 关键发现}
- Synthesis: {1–3 句洞察合成}
- Candidate Examples: {≥1 个可在正文使用的具体例子}
```

### SERP Fit 表

```markdown
## SERP Fit
Primary keyword:
Search intent: [ ] Informational  [ ] Commercial  [ ] Transactional  [ ] Navigational
Top 3–5 ranking pages:
Common coverage:
What they miss:
Our unique contribution:
```

---

*research-triangle · portable · 可跨项目复用*
