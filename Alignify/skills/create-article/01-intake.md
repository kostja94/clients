# Step 1 — Intake & Gate A

> **产出**：Gate A 判定 + 大纲草案 + Investment Score  
> **下一步必过**：Step 02 Research（**全类型**，含 best-ranking）

---

## Phase 0 首行输出（强制）

```
## QualityTier: flagship
## ArticleType: {type}
## InvestmentScore: {X.X} — {五因子摘要}
## Gate A: KEEP | MERGE → {target slug} | STOP
```

---

## 素材源（SSOT）

满足其一即可进入 Gate A；**不要求**把外部文档迁入 `knowledge/`。

| 类型 | 路径示例 | Brief 登记 |
|------|----------|------------|
| Alignify 知识块 | `knowledge/marketing/{slug}.md` | `SSOT: knowledge/…` |
| **外部个人知识库** | `E:\个人知识库\…\{主题}.md` | `SSOT: {绝对路径}` |

外部 SSOT 仍须：主题完整、可检索来源、与 slug 意图对齐。**禁止**为「对齐目录」而整份复制到 `knowledge/`。

---

## Gate A 检查清单

- [ ] 素材 SSOT 存在（Alignify 知识块 **或** 外部路径已登记）
- [ ] slug 未在 `*-pages-config.ts` 注册
- [ ] 部署仓无 cannibalization
- [ ] Investment Score **≥3.0**（<3.0 → MERGE 或 STOP，**无急稿例外**）
- [ ] 主关键词 + 搜索意图已明确（未给则必问）
- [ ] 与已有文章关系已确认（Hub / Spoke / 新 cluster）
- [ ] 竞品 SERP Top 3 URL 已收集（供 Step 02）

---

## Gate A — KEEP / MERGE / STOP

**三条件满足 ≥2 → KEEP**；否则 MERGE 或 STOP。

| 条件 | 判断 |
|------|------|
| 搜索意图独立 | 与已有 slug 关键词重叠 ≤50% |
| 读者旅程阶段不同 | 认知 / 评估 / 选型 / 激活 等 |
| 深度不可压缩 | 核心论证无法压入他文 ≤3 段 |

| Investment 均分 | 动作 |
|-----------------|------|
| **≥4.0** | KEEP |
| **3.0–3.9** | KEEP 但须在 Brief 中写清 **改角度** 策略 |
| **<3.0** | MERGE / STOP |

---

## 类型判定

| 知识块目录 | articleType | 路由 |
|-----------|-------------|------|
| `knowledge/tools/` | `best-ranking` | `/blog/{slug}` |
| `knowledge/seo/` | `seo-guide` | `/seo/{slug}` |
| `knowledge/marketing/` | `marketing-strategy` | `/marketing/{slug}` |
| `knowledge/insights/` | `insights-analysis` | `/insights/{slug}` |

存量 `/tools/` → `best-ranking-legacy`，见 Step 12。

---

## 内容大纲草案

1. **读者任务**：读完能做什么决策？  
2. **主体形态**：榜单 / 策略 / 指南 / 分析  
3. **Planned H2**（可选节注明省略理由）：

| 计划 | 采用？ | Answer block # | 备注 |
|------|--------|----------------|------|
| 核心要点 | ☐ | | |
| 什么是… | ☐ | | |
| 如何工作 | ☐ | | |
| 主体节 | ☐ | **几乎总是** | |
| 对比表 | ☐ | | |
| 应用场景 | ☐ | | |
| 如何选择 | ☐ | | |
| 结论 | ☐ | | |
| FAQ | ☐ | | |
| References | ☐ | | |

参考：[`rules/anatomy.md`](./rules/anatomy.md) · [`rules/article-brief.md`](./rules/article-brief.md)

---

## Investment Score（五因子 1–5，均值）

搜索需求 · 商业相关性 · 差异化能力 · 证据可得性 · 内容生命周期

细则：[`rules/research-triangle.md`](./rules/research-triangle.md) 同 blog-create investment-score 逻辑。

---

## 输出

- [ ] Gate A：KEEP / MERGE / STOP  
- [ ] articleType · Hub/category  
- [ ] 大纲草案  
- [ ] SERP Top 3 URL 列表（供 Step 02）

**Gate A = KEEP** → 下一步：[02-research.md](./02-research.md)（**所有类型**）
