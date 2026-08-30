# Step 1 — Intake & Gate A

> **产出**：Gate A 判定 + 大纲草案 + Investment Score  
> **不确定时**：见 [`rules/intake-questions.md`](./rules/intake-questions.md) — 在聊天中问用户，勿静默假设  
> **下一步必过**：Step 02 Research（**全类型**，含 best-ranking）

---

## Phase 0 首行输出（强制）

```
## QualityTier: flagship
## ArticleType: {type}
## BatchCount: {1 | N≥2} — {slug 或同批 slug 列表}
## InvestmentScore: {X.X} — {五因子摘要}
## Gate A: KEEP | MERGE → {target slug} | STOP
```

---

## 素材源（SSOT）

满足其一即可进入 Gate A；**不要求**把外部文档迁入 `knowledge/`。

| 类型 | 路径示例 | Brief 登记 |
|------|----------|------------|
| Alignify 知识块 | `knowledge/marketing/{slug}.md` | `SSOT: knowledge/…` |
| **外部个人知识库** | `E:\个人知识库\增长策略-Growth\…`（增长策略类**唯一 SSOT**） | `SSOT: {绝对路径}` |

外部 SSOT 仍须：主题完整、可检索来源、与 slug 意图对齐。

**Hard rule（增长策略 / 营销专题）**：素材已在 `E:\个人知识库\增长策略-Growth` 维护时，**禁止**在 `knowledge/marketing/{slug}.md` 再建副本或同步粘贴；仅允许 `knowledge/marketing/_briefs/{slug}.md` 登记路径与 Moat（不复制 SSOT 正文）。

---

## Gate A 检查清单

- [ ] 素材 SSOT 存在（Alignify 知识块 **或** 外部路径已登记）
- [ ] slug 未在 `*-pages-config.ts` 注册
- [ ] 部署仓无 cannibalization
- [ ] Investment Score **≥3.0**（<3.0 → MERGE 或 STOP，**无急稿例外**）
- [ ] 主关键词 + 搜索意图已明确（不清楚则在聊天中问用户）
- [ ] 与已有文章关系已确认（Hub / Spoke / 新 cluster）
- [ ] **best-ranking**：拟选 **Product roster**（默认 **3 款**）与站级 canonical **无冲突**（粗查 → [`rules/product-coverage.md`](./rules/product-coverage.md)）
- [ ] 竞品 SERP Top 3 URL 已收集（供 Step 02）
- [ ] **同批篇数**已登记：`BatchCount: 1` 或 `N≥2` + slug 列表（决定 Step 05 Outline 3.5 / Step 10 Cross 5.5 是否 `N/A`）

### 条件步骤速查

| BatchCount | Outline 3.5（Step 05 前） | Cross-Article 5.5（Step 10） | Step 04 截图 |
|------------|---------------------------|------------------------------|--------------|
| **1** | 输出 `N/A — single article` | 输出 `N/A — single article` | 仅 `best-ranking` / `legacy` |
| **≥2** | 过 [`outline-cross-check.md`](./rules/outline-cross-check.md) | 过 [`cross-article-audit.md`](./rules/cross-article-audit.md) | 同上 |

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

| 知识块目录 | articleType | **新文** 路由 · 正文路径 | **存量**（不重迁） |
|-----------|-------------|------------------------|-------------------|
| `knowledge/tools/` | `best-ranking` | `/blog/{slug}` · `content/blog/` | `/tools/{slug}` · `content/tools/` |
| `knowledge/tools/`（存量维护） | `best-ranking-legacy` | — | `/tools/{slug}` · `content/tools/` |
| `knowledge/seo/` | `seo-guide` | `/blog/{slug}` · `content/blog/` | `/seo/{slug}` · `content/seo/` |
| `knowledge/marketing/` | `marketing-strategy` | `/blog/{slug}` · `content/blog/` | `/marketing/{slug}` · `content/marketing/` |
| `knowledge/insights/` | `insights-analysis` | `/blog/{slug}` · `content/blog/` | `/insights/{slug}` · `content/insights/` |

存量 `/tools/` → `best-ranking-legacy`；`modifiedDate` 规则见 [`08-meta-config.md`](./08-meta-config.md) §发布日期。

---

## 内容大纲草案

1. **读者任务**：读完能做什么决策？  
2. **主体形态**：榜单 / 策略 / 指南 / 分析  
3. **Planned H2**（**内容驱动**；TL;DR/FAQ/How To 采用或省略均须在 Brief 写理由）：

| 计划 | 采用？ | Answer block # | 备注 |
|------|--------|----------------|------|
| 核心要点 | 几乎总是 | `tldr-data.json` | 可省略；Brief 须写理由 |
| 什么是… | 几乎总是 | | |
| 如何工作 | ☐ | | |
| 主体节 | ☐ | **几乎总是** | |
| 对比表 | ☐ | | |
| 应用场景 | ☐ | | |
| 如何选择 | ☐ | | |
| 结论 | ☐ | | |
| FAQ | ☐ 采用 ☐ 省略 | | 省略须写理由；采用则 7 问 |
| References | ☐ | | |

参考：[`rules/anatomy.md`](./rules/anatomy.md) · [`rules/article-brief.md`](./rules/article-brief.md)

---

## Investment Score（五因子 1–5，均值）

搜索需求 · 商业相关性 · 差异化能力 · 证据可得性 · 内容生命周期

细则：[`rules/research-triangle.md`](./rules/research-triangle.md) 同 blog-create investment-score 逻辑。

---

## 输出

- [ ] Gate A：KEEP / MERGE / STOP  
- [ ] articleType · Hub/category · **Copy mode**（M1/M2/M3 · 见 [`copy-quality.md`](./rules/copy-quality.md) Part 0）
- [ ] **BatchCount** + slug 列表（写入 Brief）  
- [ ] 大纲草案  
- [ ] SERP Top 3 URL 列表（供 Step 02）

**Gate A = KEEP** → 下一步：[02-research.md](./02-research.md)（**所有类型**）
