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

**BatchCount**: {1 | N≥2} — {slug 或同批 slug 列表}（1 → Outline 3.5 / Cross 5.5 标 N/A）

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

**Author POV**（Blog 默认有；**≠** 固定 `#author-take` H2）:
  - **Voice**：Kostja 第一人称 | 省略（Brief 写理由，如纯事件稿）
  - **判断条目**（1–3 条可证伪观点；正文**融入**相关分析节，见 `presentation.md` §Author voice）
  - **独立 H2**（如 `#author-take`）：仅当 User confirmed 或 intake 明确「要/不要」；**禁止**因 Author POV 有值就默认加节
  1. …

**Type Plan**（推荐；全新题材写「无参照」）:

| 字段 | 值 |
|------|-----|
| articleType | {best-ranking \| seo-guide \| marketing-strategy \| insights-analysis \| …} |
| 路由 | content/blog/（新文）· 存量维护则注明旧路径 |
| 参照篇（可选） | {slug} · **无（Answer Blocks 驱动）** |
| deliberate 省略 | 例：无 How To — 策略判断文 · 无对比表 — 仅 2 款产品 |
| Section Plan | 见 [`sections.md`](./sections.md) Part 0 · 模板仅建议 → [`templates.md`](./templates.md) Part 0 |

**Answer Blocks**（3–5，各对应一个 **内容问题** 的 major H2；**非**页面模板节名）:
  1. {block-id} — 读者要搞懂什么（例：`#what-is-x` · `#vs-y` · `#cases`）
  2. …
  - **禁止**无 SSOT/用户依据硬塞 `#should-you-do-this` / go-no-go / `#author-take`——选型已在其他 Block 讲清则不必另开

**Planned H2 architecture**（**内容驱动**；从 SSOT + Answer Blocks 推导，非 Marketing 五段式）:
| H2 / 锚点 | 目标 | Answer block |
|-----------|------|--------------|
| **Optional sections** | TL;DR: ☐ · FAQ: ☐ · How To: ☐ · `#author-take`: ☐ 采用 ☐ 省略 · go/no-go 矩阵: ☐ 采用 ☐ 省略（**仅** `marketing-strategy` + GTM 适用性题材，见 [`templates.md`](./templates.md#part-3-marketing) §3.2） · **Skills/runbook 预告**: ☐ 正文**禁止**（E49） · **若采用 TL;DR/FAQ/Refs → Step 08 注册三 JSON（E10）；省略 → JSON 不得留键** |

**Word count target**（叙事正文，见 word-counts.md）:
**Planned internal links**（点击意图；无硬性条数，记录目标 slug + 段落 + 理由）:
**Synthesis Statement**（链 Step 02）:
**SERP Fit 摘要**（链 Step 02）:

**Copy quality**（见 [`copy-quality.md`](./copy-quality.md) · 附录 A）:
- Mode: M1 | M2 | M3（默认 M1；同 Hub 簇状生产 → M2）
- Hero fault（本页独有故障/缺口）:
- Deliverable（本页交付物）:
- Uniqueness target: L2（flagship 默认）
- Cluster hub: {slug}（仅 M2）
- Swap neighbors: {slug-a}, {slug-b}（M2 必填 ≥2）

**Excellence type**（择一标注）: Depth | Objectivity | Freshness | Workflow | Proof
**Post-publish metric**（T+7 / T+30 / T+90）:

**Final CTA**（Step 08 写入 `cta-config.json` · 见 [`sections.md`](./sections.md) Part 5）:
- ZH title:
- ZH description:
- EN title:（Step 09 定稿；Step 02 可留 TBD）
- EN description:
- cta 按钮: zh「开始合作」/ en「Work with us」（或见 `sections.md` Part 5.2）
```

---

## Brief 硬要求（Flagship）

| 字段 | 要求 |
|------|------|
| Moat Asset | ≥1 项；正文必须兑现（Step 10 / audit 复核） |
| Author POV | Blog 默认 ≥1 条判断**写入正文**（任意相关 H2 内）；独立 `#author-take` 须 Brief/User 明示 |
| Answer Blocks | 3–5 个**内容问题**；每个有对应 H2；**非**模板节清单 |
| One-line thesis | 通过「SERP 同句测试」（见 [`copy-quality.md`](./copy-quality.md) Part 1） |
| Copy quality | M1 推荐 Hero fault；M2 必填 cluster + swap neighbors |
| SuccessMetric | 可量化（排名、CTR、内链点击、转化路径之一） |
| Planned H2 | 主体节不可省略；TL;DR/FAQ/How To 若省略须在 Brief 写理由 |
| Final CTA | ZH title + description **Step 02 必填**；EN Step 09 定稿；Step 08 写入 deploy 仓 |

---

*article-brief · v1.4 · 2026-08-27*
