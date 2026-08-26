# Article Brief 模板（Flagship 必填）

> **锁定时机**：Step 02 Gate 0R Pass 后定稿；Step 05 动笔前不得偏离 Brief 中的 One-line thesis 与 Moat。  
> **用户确认**：Brief 中与用户决策相关的字段，须来自用户明示或聊天确认；角度、禁忌、结构等**不清楚时先问**（见 [`intake-questions.md`](./intake-questions.md)）。
> **存放**：创作过程写入 `knowledge/{dir}/_briefs/{slug}.md` 或对话输出（不发布）。**外部 SSOT**（如个人知识库）时在 Brief 顶部写 `**SSOT**: {绝对路径}`，**不必**迁入 `knowledge/`。

---

## 模板

```markdown
## Article Brief — {slug}

**QualityTier**: flagship（Alignify 固定，不可降级）
**ArticleType**: {best-ranking | seo-guide | …}
**InvestmentScore**: {1.0–5.0} — {五因子一行摘要}
**Gate A**: KEEP | MERGE → {target}

**User confirmed**（可选摘要，YYYY-MM-DD）:
- …

**Primary keyword**（ZH / EN）:
**Search intent**: Definition | Comparison | Tutorial | Alternative | Commercial | …
**SuccessMetric**（发布后 90 天可量化）:
**Target reader**:
**Hub / category**:

**One-line thesis**（Top SERP **找不到同句**）:
**Differentiation angle**（vs SERP Top 3）:
**Moat Asset**（≥1，Alignify 独有增量）:
  1. …

**Author POV**（Marketing/Blog 必填，1–3 条可证伪判断；正文须第一人称兑现）:
  1. …
  **Voice**: Kostja 第一人称 | 编辑部（Insights 可选）

**Answer Blocks**（3–5，各对应一个 major H2）:
  1. {block-id} — …
  2. …

**Planned H2 architecture**（**内容驱动**；可选节采用/省略及理由）:
| H2 / 锚点 | 目标 | Answer block |
|-----------|------|--------------|
| **Optional sections** | TL;DR: ☐ 采用 ☐ 省略 — 理由：… · FAQ: ☐ 采用 ☐ 省略 — 理由：… · How To: ☐ 采用 ☐ 省略 |

**Word count target**（叙事正文，见 word-counts.md）:
**Planned internal links**（点击意图；无硬性条数，记录目标 slug + 段落 + 理由）:
**Synthesis Statement**（链 Step 02）:
**SERP Fit 摘要**（链 Step 02）:

**Excellence type**（择一标注）: Depth | Objectivity | Freshness | Workflow | Proof
**Post-publish metric**（T+7 / T+30 / T+90）:

**Final CTA**（Step 08 写入 `cta-config.json` · 见 [`final-cta.md`](./final-cta.md)）:
- ZH title:
- ZH description:
- EN title:（Step 09 定稿；Step 02 可留 TBD）
- EN description:
- cta 按钮: zh「开始合作」/ en「Work with us」（或 `final-cta.md` 备选表）
```

---

## Brief 硬要求（Flagship）

| 字段 | 要求 |
|------|------|
| Moat Asset | ≥1 项；正文必须兑现（Step 10 / audit 复核） |
| Author POV | Marketing/Blog ≥1 条；正文第一人称显式写出（见 `presentation.md`） |
| Answer Blocks | 3–5 个；Outline 中每个有对应 H2 |
| One-line thesis | 通过「SERP 同句测试」 |
| SuccessMetric | 可量化（排名、CTR、内链点击、转化路径之一） |
| Planned H2 | 主体节不可省略；TL;DR/FAQ/How To 若省略须在 Brief 写理由 |
| Final CTA | ZH title + description **Step 02 必填**；EN Step 09 定稿；Step 08 写入 deploy 仓 |

---

*article-brief · v1.1 · 2026-08-27*
