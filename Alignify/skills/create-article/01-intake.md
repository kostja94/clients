# Step 1 — Intake & Gate A

> **产出**：Gate A 判定 + 大纲草案 + Investment Score  
> **不确定时**：在聊天中问用户，勿静默假设 — 见本文件 §「Intake 问答」  
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

## Intake 问答（不确定就问用户）

> 对文章有任何**不确定**之处，在**聊天中直接问用户**；禁止静默假设、禁止用「合理默认值」顶替用户未说的决策。
> （本节 2026-09-09 由原独立文档并入）

### 硬规则

1. **不确定就问** — 主叙事、中文主称、slug、是否写 Author POV、与姊妹篇关系、结构取舍等，**用户未说清且 SSOT/Brief 无法唯一推断时**，先在聊天提问，再继续 Gate A / 动笔。
2. **已明确的不重复问** — 用户在本轮或 Brief 里已确认的项，记入 `_briefs/{slug}.md`，不再追问。
3. **SSOT 文件名 ≠ 文章角度** — 知识库文件名（如 `Pay-to-Remove-Watermark-付费去水印.md`）只是素材路径；**文章写什么角度**若不清楚，必须先问（例：增长 vs 变现 vs 合规）。
4. **冲突须暂停** — 执行中发现 SSOT 与用户已定方向矛盾，说明冲突并等用户选择。
5. **确认回写 Brief** — 用户答复写入 `knowledge/{dir}/_briefs/{slug}.md`；可选附 `User confirmed (YYYY-MM-DD)` 摘要。

### 什么时候该问（示例，非固定问卷）

| 场景 | 问什么 |
|------|--------|
| 用户只给 SSOT 路径 | 主叙事、中文主称、slug、与已有文 MERGE/KEEP |
| SSOT 标题与讨论角度不一致 | 以哪个为主线 |
| Marketing 文是否写 `#author-take` | **独立 H2** 写 / 省略（与 Brief **Author POV** 分离：有 POV ≠ 要 `#author-take`） |
| 架构/Insights 文结构 | 从 SSOT 列 H2；**默认不要** go/no-go 表 + `#author-take` 双收束 |
| 未发布 skills / runbook | 正文 **禁止** 预告「细节进 skills」；skills 上线后 **再加内链** |
| 结构不明 | TL;DR / FAQ / How To 采用或省略 |
| 内链 / 回链 / 发布 | 链哪些已上线 slug、是否 commit/push、publishDate |
| commit / push | **未明确要求不执行**（沿用 git 用户规则） |

**不必**每篇机械过完一张问题表；**只要有一项不清楚，就问那一项**。

### 禁止行为

- ❌ 按 SSOT 文件名直译当 H1 或主叙事
- ❌ 用户说「给方案」却未经确认直接写正文
- ❌ 用户明确不要的内容仍写进文（如指定不写某产品）
- ❌ 把**其他 slug** 的对话确认套用到当前篇
- ❌ 能推断的唯一答案仍反复追问
- ❌ Author POV = 是 → 默认加 `#author-take` H2（须 User 单独确认是否独立成节）
- ❌ 「落地一带而过」→ 正文写「细节在 future skills」（应压缩概念进本文，E49）

### Brief 回写

用户确认过的决策，写入 Brief 对应字段即可（见 [`article-brief.md`](article-brief.md)）。无固定字段清单——**记用户实际确认过的内容**。

---

## Gate A 检查清单

- [ ] 素材 SSOT 存在（Alignify 知识块 **或** 外部路径已登记）
- [ ] slug 未在 `*-pages-config.ts` 注册
- [ ] 部署仓无 cannibalization
- [ ] Investment Score **≥3.0**（<3.0 → MERGE 或 STOP，**无急稿例外**）
- [ ] 主关键词 + 搜索意图已明确（不清楚则在聊天中问用户）
- [ ] 与已有文章关系已确认（Hub / Spoke / 新 cluster）
- [ ] **best-ranking**：拟选 **Product roster**（默认 **3 款**）与站级 canonical **无冲突**（粗查 → [`product-coverage.md`](product-coverage.md)）
- [ ] 竞品 SERP Top 3 URL 已收集（供 Step 02）
- [ ] **同批篇数**已登记：`BatchCount: 1` 或 `N≥2` + slug 列表（决定 Step 05 Outline 3.5 / Step 10 Cross 5.5 是否 `N/A`）

### 条件步骤速查

| BatchCount | Outline 3.5（Step 05 前） | Cross-Article 5.5（Step 10） | Step 04 截图 |
|------------|---------------------------|------------------------------|--------------|
| **1** | 输出 `N/A — single article` | 输出 `N/A — single article` | 仅 `best-ranking` / `legacy` |
| **≥2** | 过 [`cross-article-audit.md`](cross-article-audit.md) | 过 [`cross-article-audit.md`](cross-article-audit.md) | 同上 |

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

存量 `/tools/` → `best-ranking-legacy`；`modifiedDate` 规则见 [`08-meta-config.md`](08-meta-config.md) §发布日期。

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

参考：[`anatomy.md`](anatomy.md) · [`article-brief.md`](article-brief.md)

---

## Investment Score（五因子 1–5，均值）

搜索需求 · 商业相关性 · 差异化能力 · 证据可得性 · 内容生命周期

细则：[`02-research.md`](02-research.md) 同 blog-create investment-score 逻辑。

---

## 输出

- [ ] Gate A：KEEP / MERGE / STOP  
- [ ] articleType · Hub/category · **Copy mode**（M1/M2/M3 · 见 [`copy-quality.md`](copy-quality.md) Part 0）
- [ ] **BatchCount** + slug 列表（写入 Brief）  
- [ ] 大纲草案  
- [ ] SERP Top 3 URL 列表（供 Step 02）

**Gate A = KEEP** → 下一步：[02-research.md](02-research.md)（**所有类型**）
