# Clink — Gates 细则

> 加载时机：Phase 0 · Phase 2 · Phase 0R · Phase 5
> 主文件：SKILL.md §3 各 Phase 指针

---

## 1. Phase 0 — 六必问

| # | 问题 |
|---|------|
| 1 | 目标 SEO 关键词 + search intent？ |
| 2 | 目标读者？（全球 SaaS / AI-native / 支付工程师 / FinOps） |
| 3 | 发布目的？SEO / 品牌 / 转化 |
| 4 | SERP Top 3 竞品 URL？ |
| 5 | 与已有 blog / pipeline 关系？（hub-spoke） |
| 6 | category：Product / Comparison / Opinion / Glossary？ |

---

## 2. Gate A — KEEP/MERGE

**三条件满足 ≥2 → KEEP**；否则 MERGE 或 STOP。

| 条件 | 判断 |
|------|------|
| 搜索意图独立 | 与 content-graph 关键词重叠 ≤50% |
| 读者阶段不同 | Awareness / Consideration / Evaluation / Activation |
| 深度不可压缩 | 核心论证 >800 词 |

**信息增量**（KEEP 后）：相对 SERP Top 3 至少 **2 项**独有，否则 STOP：

- 决策框架 / 选型表
- 混合 MoR+PSP 架构视角
- 客户案例 + 量化区间（有 as-of）
- Agent 支付 / routing 交叉维度
- Glossary 额外：指标公式 + 计算工作示例 / 术语边界表（voluntary vs involuntary 等）

**GlossaryTerm 专属 Gate（D1–D4）**：

| # | 阻断条件 | 说明 |
|---|---------|------|
| D1 | Cannibalization | 已有 blog canon 术语不得重写完整定义，仅 1–2 句 + link |
| D2 | Link budget | blog 互链 ≥2；本簇 glossary ≤3；0 forbidden URL |
| D3 | Product ratio | Clink 正文占比 ≤15%；FAQ 前 ≤3 段 |
| D4 | Category lock | frontmatter `category` 必须为 `Glossary` |

**Investment Score <3.0 → STOP 或降级 Mode**

---

## 3. Gate 0R — Research 完整性

| # | 检查项 |
|---|--------|
| G0R-1 | project-config + product-competitors + content-graph 已读 |
| G0R-2 | R2 SERP Top 5 + PAA |
| G0R-3 | R3 clinkbill.com/docs + SERP Top 3 Fetch |
| G0R-4 | Synthesis 三要素完整 |
| G0R-5 | IG 三问成立 |
| G0R-6 | 无未验证 P0 claim（Degraded 除外） |

---

## 4. Gate B — Slug

见 `slug-gate.md` — 6 问全 Pass + 0 反模式 + publishDate 避让。

---

## 5. Gate C — SelfCheck

**H0–H4 + C1–C4 + 12 维全 Pass → audit-ready**

| Hard Gate | 说明 |
|-----------|------|
| H0 | Gate 0R 完整 |
| H1 | G1–G7 零触发 |
| H2 | Gate B Pass |
| H3 | 词数达类型下限 |
| H4 | Clink-Specific：C1–C4 + 产品占比 + Conclusion→FAQ |

---

## 6. Gate 失败回溯

| 结果 | 回退 |
|------|------|
| Gate A STOP | 改选题 |
| Gate 0R Fail | 补 R2/R3 |
| Gate B Fail | Phase 2 重选 slug |
| Gate C 写作类 | Phase 4 |
| Gate C 结构类 | Phase 3 |

---

*gates · v1.0.0 · 2026-07-21*
