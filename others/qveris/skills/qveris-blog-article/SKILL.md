---
name: qveris-blog-article
description: >
  Create QVeris blog articles for qveris.ai/blog — English only — any topic
  (capability routing, financial data APIs, agent tooling, MCP, product
  stories, market analysis, field tests). Also load for blog-only
  title/description optimization (references/meta-title-description.md).
  Do NOT load for non-blog landing pages or glossary/site metadata.
metadata:
  version: 1.0.0
  project: qveris.ai
  locale: en
  load-rule: progressive-disclosure
  max-primary-lines: 500
  self-contained: true
---

# QVeris Blog Article Creation

为 **https://qveris.ai/blog/** 从选题到英文成稿。**本 skill 文件夹可单独分发**：通用 Research / 终审在 `references/portable/`。**范围**：仅英文 `/blog/{slug}`。与用户沟通可用中文；**正文必须为英文**。

## 渐进式加载规则（硬性）

```
Agent 默认只读本文件（SKILL.md）。
Phase 需要细节时，按指针读取 references/{file}.md（一次最多 2 个）。
禁止一次性加载全部 references。
读完用完即弃——不跨 Phase 保留 reference 上下文。
```

---

## §0 如何使用

### 触发语

```
按 qveris-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{TechnicalDeepDive|FieldTest|WorkflowGuide|MarketAnalysis|Comparison|ProductStory} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主题 / 主关键词 | ✅ | 决定 search intent 与 §2 类型路由 |
| 文章类型 | 可选 | 未给则按 §2 路由规则推断 |
| 竞品参考 URL | 推荐 | Phase 0R 信息增量判断 |
| 实测数据 / 数据集 | 可选 | Field Test 类必填；其余可补强 |

### 输出（Phase 6 交付物）

1. **Article Brief**（Phase 1 最终版）
2. **Research Log**（R1–R3 + Synthesis，Phase 0R）
3. **完整稿** `qveris/blog/NN-{slug}.md`（NN 两位递增，见 `references/content-graph.md`）
4. **SelfCheck 表**（Hard Gates + 10 维健康分）
5. **Source Map** + **SERP Fit** + **OG Image Prompt**（1200×630）
6. **提示人类**更新 `blog/README.md` 文件表

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化已有文章的 title/description | 本 skill → `references/meta-title-description.md` |
| 已发稿回溯审计 | `references/portable/retro-audit.md` |
| 非 qveris.ai 博客 | 对应项目的 blog skill |
| 中文博客内容 | 另建 ZH skill（本期未实现） |

---

## §1 项目配置与 Gate 清单

> **完整配置 + G1–G7 + F1–F4 + URL 白名单 → `references/project-config.md`**

**Phase 0 / Phase 5 前加载。** 核心阻断项速查：

| Gate | 项数 | 阻断条件 |
|------|:---:|------|
| **G1–G7** | 7 | 事实错误 / 死链 / 无来源数字 / 竞品状态错误 / 产品夸大 / 内链未上线 / 品牌风险 |
| **F1–F4** | 4 | 投资建议违规 / 数据时效缺失 / 实测标注缺失 / API 价格无来源（金融博客特有） |

G1–G7 + F1–F4 全部 Pass 方可进入健康分评估。任一 Fail = 不得交付。

---

## §2 文章类型路由

> **6 类路由表 + H2 模板 + Voice/合规 + Who/How/Why → `references/article-types.md`**

**Phase 0 / Phase 3 前加载。** 速查：

| 类型 | intent | 词数 | 产品提及上限 | 参考 slug |
|------|--------|------|:---:|-----------|
| **Technical Deep Dive** | 技术原理 / 架构解析 | 2500–4000 | ≤25% | `mcp-qveris` |
| **Field Test & Audit** | 实测 / 计费审计 | 2500–3800 | ≤35% | `ai-finance-agent-cost-audit` |
| **Workflow Guide** | 教程 / 集成步骤 | 2200–3500 | ≤40% | `qveris-in-cursor` |
| **Market Analysis** | 市场 / 事件点评 | 2000–3000 | ≤20% | `a-share-realtime-quotes-agent` |
| **Comparison** | 对比 / 替代选型 | 2500–3500 | ≤45% | `openclaw-vs-hermes` |
| **Product Story** | 产品 / 生态叙事 | 2000–3200 | ≤45% | `qveris-fmp-60` |

**路由规则**：`how it works` / 架构 / 原理 → TechnicalDeepDive；`field test` / `audit` / 计费实测 → FieldTest；`how to` / `guide` / 集成 → WorkflowGuide；`market` / `stock` / 点评 → MarketAnalysis；`vs` / `alternative` / 对比 → Comparison；`product update` / 生态 / 案例 → ProductStory。

**搜索量数据**：所有搜索量/难度字段标注「⚠️ 待验证」，需 Semrush/Ahrefs 回填——禁止凭推断填入。

---

## §3 创作工作流（7 Phase + 4 Gate）

### 流程总览

```
Phase 0  ─ Intake & Gate A ─── 不通过 → STOP/MERGE
Phase 0R ─ Research 三角 & Gate 0R ─── 不通过 → 回溯 Phase 0R
Phase 1  ─ Article Brief
Phase 2  ─ Slug、Date & Gate B ─── 不通过 → 重选 slug
Phase 3  ─ Outline
Phase 4  ─ Draft
Phase 5  ─ SelfCheck & Gate C ─── 不通过 → 修复
Phase 6  ─ Delivery
```

---

### Phase 0 — Intake & Gate A（选题门禁）

#### 0.0 首行强制输出

```
## Topic Scope: {keyword} · {article type} · publish goal {SEO|品牌|转化}
## InvestmentScore: {1.0–5.0} — {五因子摘要}
## Gate A: KEEP | MERGE → {target slug} | STOP
```

#### 0.1 快速 Gate：独立成文 + 信息增量

**KEEP/MERGE（3 条件满足 ≥2 → KEEP）**：

| 条件 | 判断 |
|------|------|
| 搜索意图独立 | 与已有文章关键词重叠 ≤50%（对照 `references/content-graph.md` 冲突表 + 官网 120 篇） |
| 读者阶段不同 | Awareness / Evaluation / Setup / Production / Optimization |
| 深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

**信息增量 Gate（KEEP 后强制）**：相对 SERP Top 3，本篇须至少提供 **2 项** 以下之一，否则 **STOP**：

- 独有分析框架（如调用成本归因、多 Provider 路由决策树）
- 可执行决策表（用例 × Provider × 成本区间）
- 带方法论的内部实测（n + 时间窗 + 限定语，Field Test 类）
- 跨篇 canonical 引用 + 新边界声明

#### 0.2 五必问

| # | 问题 | 用途 |
|---|------|------|
| 1 | 目标 SEO 关键词 + search intent？ | 类型路由确认 |
| 2 | 目标读者？（Agent 开发者 / 量化工程师 / 投资分析师 / 产品团队） | 深度与 persona |
| 3 | 发布目的？SEO / 品牌 / 转化 | 产品提及容忍度 |
| 4 | 同主题竞品内容 2–3 链接？ | 信息增量交叉验证 |
| 5 | 是否有实测数据/内部观察？ | Field Test 与引用强度 |

---

### Phase 0R — Research 三角 & Gate 0R

> **→ `references/portable/research-triangle.md` · `references/portable/serp-fit-template.md`**

```
R1 — 读 references/project-config.md + product-competitors.md + content-graph.md
R2 — Web 搜索 primary keyword → SERP Top 5 + PAA
R3 — Fetch qveris.ai 相关页 + SERP Top 3–5（竞品/官方文档）
Synthesis + Candidate Examples
→ Research Log + SERP Fit → Gate 0R
```

**Degraded**：R2/R3 缺失时标注 `⚠️ 联网信息不足`；正文不得写未验证的 P0 claim。

---

### Phase 1 — Article Brief

> **完整模板 → `references/article-types.md` 末尾 / `references/mini-example.md`**

```markdown
## Article Brief
**Working title**:
**Primary keyword**:
**Search intent**: [ ] Informational  [ ] Commercial  [ ] Transactional
**Article type**: {from §2 route}
**Reader stage**: Awareness / Evaluation / Setup / Production / Optimization
**Publish goal**: SEO / Brand / Conversion
**Target audience**:
**Word count target**:
**Cluster role**: Pillar / Spoke / Standalone
**Canonical concept links**: (link only, do not redefine)
**Differentiation angle** (vs SERP top 3):
**Information Gain Statement** (from Phase 0):
**Primary product link(s)**:
**KEEP/MERGE**: KEEP | MERGE → {target slug}
**Compliance notes**: {financial blog → F1–F4 checklist; comparison → fair-treatment; field test → data provenance}
```

---

### Phase 2 — Slug、Date & Gate B

> **7 原则 + 12 反模式 → `references/slug-gate.md`**

1. 生成 2–3 个 slug 候选（无 `/blog/` 前缀，如 `stock-api-free-comparison`）+ 推荐项
2. 跑 slug-gate 6 问 + 对照 12 项反模式
3. 竞品基准检查（搜 Google → 对比前 5 竞品 slug）
4. 确定 `publishedAt`：避让 `references/content-graph.md` 已占用日期；本地 blog 一天一篇（参考其他项目惯例），新稿 = 当前最晚 `publishedAt` +1 天

**Gate B**：全部 6 问通过 + 0 项反模式命中 → 定 slug。任一项不通过 → 重选。**禁止 Flag 过关。**

同步：SERP Fit 快速对照 + 完整 frontmatter（slug、metaTitle、description、author、publishedAt、updatedAt、readTime）+ 正文 `# H1` title、excerpt 段、`## TL;DR` 区块——按 `references/frontmatter-schema.md`。title/description 计字符与自检 → `references/meta-title-description.md`。

---

### Phase 3 — Outline

按 `references/article-types.md` 对应类型的 H2 模板展开。每节标注：目标词数、关键词位置、内链占位（对照 `references/project-config.md` URL 白名单）、产品出现计划。生成 **OG Image Prompt**（1200×630）。

---

### Phase 4 — Draft

> **Voice 正向/禁止 → `references/article-types.md` · 引用分级 → `references/citations.md` · 表现形式 → `references/writing-constraints.md`**

**核心约束**：
- 英文正文；H2 用描述性标题，不编号（对齐官网既有文章风格）
- P0 数字有来源链接；P1 趋势有官方 docs + as of date
- 长段落 ≥3 段（≥4 句）；列表占比 ≤ 类型上限；无连续 3+ 短段集群
- BLUF 三处：正文 `## TL;DR` 首条 / 每个 major H2 首段 / FAQ 每问首句
- 金融博客（Field Test / Market Analysis / Comparison 涉及行情数据）：数据须带时间戳（`as of {date}`）+ 来源标注（F2/F3）
- 站外链接权威 2–8；竞品/数据源 `rel="nofollow noopener"` HTML
- CTA ≤2 次（`qveris.ai` 主链 / `/plugins` / `/cli` / `/docs`）

---

### Phase 5 — SelfCheck & Gate C

> **完整 12 维 → `references/selfcheck.md` · 机器预检 → `tools/README.md`**

#### 5.1 机器预检（先跑脚本）

```bash
cd qveris/skills/qveris-blog-article
python tools/frontmatter_validator.py ../../blog/NN-{slug}.md --keyword "{primary kw}"
python tools/word_count_narrative.py ../../blog/NN-{slug}.md --intent {type}
python tools/link_checker.py ../../blog/NN-{slug}.md
```

任一 FAIL → 修复后重跑，再进人工自检。

#### 5.2 Hard Gates（全部 Pass 方可交付）

| Gate | 项 | 任一 Fail → STOP |
|------|----|------|
| **G1–G7** | 事实 / 死链 / 无来源数字 / 竞品状态 / 产品夸大 / 内链未上线 / 品牌风险 | 修复后重检 |
| **F1–F4** | 禁止投资建议 / 数据时效 / 实测标注 / API 价格来源 | 修复后重检 |
| **Slug** | §13 全部 6 问 + 0 项反模式 | 重选 slug |

#### 5.3 轻量健康分（1–5，Gate 全部 Pass 后评估）

| # | 维度 | 快速判据 |
|---|------|---------|
| 1 | Fact / E-E-A-T | P0 数字全有来源？数据有时效？竞品 ≥1 优势？ |
| 2 | Differentiation | 独有框架/表格 ≥1？句级重复 <30%？信息增量 2 项已验证？ |
| 3 | Presentation | 长段落 ≥3？列表占比 ≤上限？0 碎片化集群？表格前后有分析？ |
| 4 | Writing / Voice | 禁词 0？空泛句 ≤2？≥1 具体 scenario？ |
| 5 | Objectivity | 漏斗符合类型标准？产品 ≤上限？无贬低措辞？Who/How/Why 齐备？ |
| 6 | Structure / Links | H1 title + excerpt 置顶？Conclusion+FAQ 收尾？blog 互链 ≥2？锚文本语义化？ |
| 7 | SEO | 正文 H1 含主关键词？description 120–160？metaTitle 含 `| QVeris`？ |
| 8 | Depth | 词数在区间？每 ~500 词 ≥1 例子？FAQ 固定 6 题且 ≥1 题独立？ |
| 9 | QVeris + Compliance | 品牌正确？协议叙事准确（Discover→Inspect→Probe→Call）？无投资建议暗示？ |
| 10 | Conversion | CTA ≤2？匹配读者阶段？CTA 前有独立价值？ |

**整体**: __/5.0（10 维平均）　🟢≥4.0 / 🟡3.0–3.9 / 🔴<3.0

**交付标准**：Hard Gates 全部 Pass + 无 🔴 维度。🟡 维度标注 P1 修复项。

#### 5.4 SelfCheck 输出格式

```markdown
## SelfCheck — {slug}
### Hard Gates
| Gate | Pass/Fail | Notes |
### Health Check
| # | Dimension | Score | Notes |
**Overall**: X.X/5.0 🟢
### Information Gain Statement
{3 sentences vs SERP Top3}
### Source Map (internal)
| Claim | § | Source | Checked | Confidence |
### Cannibalization Check
| vs | Boundary | Clear? |
**🟡 P1 fixes**: ...
```

---

### Phase 6 — Delivery

1. **写入文件** `qveris/blog/NN-{working-slug}.md`
2. **Article Brief 摘要**（Phase 1 最终版）
3. **Research Log**（Phase 0R）
4. **SelfCheck 自检表**（Phase 5 完整输出）
5. **OG Image Prompt** + **Internal Link Plan**
6. **Meta 复核**（可选）：按 `references/meta-title-description.md` 计字符并跑自检；只改 frontmatter `metaTitle`/`description` 与正文 `# H1`
7. **Human handoff**：提示更新 `qveris/blog/README.md` 文件表 + planned/live 标注

---

### §3.G — Gate 失败回溯表

| Gate / 结果 | 回退至 |
|-------------|--------|
| Gate A → STOP/MERGE | 流程结束或改选题 |
| Gate 0R ❌ | Phase 0R |
| Gate B ❌ | Phase 2 |
| Gate C 写作/事实 | Phase 4 |
| Gate C 结构 | Phase 3 |
| Gate C Slug/Meta | Phase 2 |

---

## §4 已有内容图谱

> **本地 blog 文件表 + 官网 120 篇索引 + Canonical Registry + 跨篇边界声明 → `references/content-graph.md`**

**Phase 0 / Phase 5 加载。** 速查：本地下一序号 **02**；本地 Pillar/首个已发稿 `stock-api-free-comparison`；官网博客 120 篇（slug 见 content-graph，避免 slug 冲突与主题重叠）。

---

## §5 Frontmatter 与文件命名

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{working-slug}.md`（NN 两位递增） |
| frontmatter `slug` | 不含 `/blog/` 前缀，不含 NN 前缀；与官网 `/blog/{slug}` 对应 |
| frontmatter 必填字段 | `slug` `metaTitle` `description` `author` `publishedAt` `updatedAt`（`readTime` 推荐） |
| `title` | **正文 `# H1`**（45–90 字符，含主关键词）；不进 frontmatter |
| `excerpt` | **正文 H1 后首段**（斜体引言，≥40 字符）；不进 frontmatter |
| `TL;DR` | **正文 excerpt 后 `## TL;DR` 区块**（3–5 条 `- **label** — body`，首条 "Fast answer" BLUF ≥40 字符）；不进 frontmatter |
| 禁止字段 | `title` `excerpt` `tldr` `badge` `breadcrumb` `authorInitials` `heroImage` `heroAlt` `tocExtra` 及 `date` `isoDate` `category` `keywords` `related` `disclosure` |

> **完整 Schema + 正文 H1/excerpt 规范 → `references/frontmatter-schema.md`（基准：`blog/01-stock-api-free-comparison.md`）**

---

## §6 关键词速查

> **P0/P1/P2 + 话题簇 → `references/keywords.md`**

**Phase 0 加载。**

---

## §7 产品与竞品事实

> **产品事实 + 竞品公平摘要 + 合规红线 → `references/product-competitors.md`**

**Phase 4 / Phase 5 加载。**

---

## §8 创作 vs 审核 vs Meta（严格边界）

| | **qveris-blog-article** | **references/portable/final-audit.md** | **references/meta-title-description.md** |
|------|:---:|:---:|:---:|
| 做什么 | **生成**文章 | **审核**文章（打分+报告） | **生成/优化** title/description |
| 产出 | .md 成稿 + SelfCheck | 审核报告（S/A/B/C/D 等级） | frontmatter metadata |
| 时机 | 选题→成稿 | 成稿后，发布前 | Phase 2 或独立任务 |
| 评分 | 轻量健康分 (1–5, 🟢🟡🔴) | 加权评分 (0–100, S-D) | 计字符 + 四条自检 |

**硬规则**：
- Phase 5 SelfCheck = **创作质量自检**，健康分供人类快速判断，不等同审核等级
- `final-audit.md` 的加权评分（S/A/B/C/D）= **独立发布终审**，是最终质量判定
- 两者不可互相替代

---

## Gotchas — 禁止项清单（36 条）

创作时逐条对照。任一项触发 = 对应维 Fail。

**结构与格式**：
1. ❌ 不要在正文 `# H1` title 后省略 excerpt 引言段（H1 → excerpt → 正文 H2）
2. ❌ 不要用 `## TL;DR` 之外的结构承载 TL;DR（TL;DR 必须是正文 `## TL;DR` 区块 + 3–5 条 `- **label** — body` bullet）
3. ❌ 不要用 `## Related articles` 模块（内链分布在正文）
4. ❌ 不要两篇共用同一 `publishedAt`（一天一篇，新稿 = 最晚 date +1 天）
5. ❌ 不要连续 3+ 短段落（≤2 句）集群
6. ❌ 不要"表格+一句话然后跳下节"——表格后 ≥2 句分析
7. ❌ 不要 H2 后直接列表/表格——先写引导段

> 注：编号 H2（`## 1.`）在 01 已发稿中出现，可接受；描述性 H2 为首选（多数官网文）。Conclusion/FAQ 建议有但非强制。

**Slug 与链接**：
8. ❌ 不要 slug 含 `/blog/` 前缀（frontmatter `slug` 裸 slug，文件名才带 NN-）
9. ❌ 不要 slug 含年份（`stock-api-free-comparison` ✅；`stock-api-free-comparison-2026` ❌）
10. ❌ 不要 slug 含内部架构词（guide/how-to/analysis 等）
11. ❌ 不要链 `/auth/*` `/admin/*` `/dashboard/*` 及未上线路径（G6）
12. ❌ 不要锚文本 "click here" / "learn more" / "this article"
13. ❌ 不要同篇对同一 slug 链超过 2 次
14. ❌ 不要在正文 `## TL;DR` 区块或 FAQ 内放内链
15. ❌ 不要链向官网已下线栏目（`/use-cases/*` `/scenarios/*` `/alternative/*`）

**品牌与受众**：
16. ❌ 不要写错品牌名（统一 **QVeris**；`QVeris AI` 仅指公司语境）
17. ❌ 不要声称 QVeris 与某交易所/数据源官方合作（除非官网声明）
18. ❌ 不要混淆 QVerisBot 与 QVeris Lab（QVerisBot 已并入 Lab beta）
19. ❌ 不要写 MCP 版本号未经 /ecosystem 或 /docs 核实（当前 v0.13.0）

**数据与引用**：
20. ❌ 不要裸引 10,000+ 能力 / 99.99% 上线率无来源（G3）
21. ❌ 不要 "studies show" / "industry reports indicate" 泛引
22. ❌ 不要用 Low confidence 来源支撑核心论证
23. ❌ 不要内部实测无 "based on internal analysis, n≈X" 或 "QVeris Data Test" 标注（F3）

**金融合规（QVeris 特有）**：
24. ❌ 不要给出买入/卖出建议（"buy Seres" ❌）——只陈述数据与事实（F1）
25. ❌ 不要行情/价格数据无时间戳（"as of {date}"）+ 来源（F2）
26. ❌ 不要 API 价格估算无来源或未注明"以官方为准"（F4）
27. ❌ 不要把单次实测结果写成普适结论（加限定语，F3）

**Cannibalization**：
28. ❌ 不要与官网已有博客主题高度重叠（对照 content-graph 官网 120 篇；重叠 >50% → MERGE 或改角度）
29. ❌ 不要重写官网 guides 已覆盖的完整定义（canonical 术语 1–2 句 + link）
30. ❌ 不要 Pillar 完整展开 Spoke 核心内容（引述 1–2 句 + link）

**流程与合规**：
31. ❌ 不要 G/F/Slug Gate 未全部 Pass 就交付
32. ❌ 不要为凑字数写偏离 ICP 的长篇
33. ❌ 不要 "Imagine you're…" 虚构开头
34. ❌ 不要一次加载全部 references（渐进式加载，一次 ≤2 个）
35. ❌ 不要混淆创作自检与独立审核——发布前终审用 `references/portable/final-audit.md`

---

## Reference Index

创作时按需加载（一次最多 2 个）：

| 文件 | 内容 | 加载时机 |
|------|------|----------|
| `references/project-config.md` | 项目配置 + G1–G7 + F1–F4 + URL 白名单 | Phase 0 / Phase 5 |
| `references/article-types.md` | 6 类路由 + H2 模板 + Voice + Who/How/Why | Phase 0 / Phase 3 / Phase 4 |
| `references/frontmatter-schema.md` | QVeris frontmatter Schema + 示例 | Phase 2 / Phase 5 |
| `references/content-graph.md` | 本地 blog 表 + 官网 120 篇 + Canonical | Phase 0 / Phase 5 |
| `references/keywords.md` | P0/P1/P2 关键词 + 话题簇 | Phase 0 |
| `references/product-competitors.md` | 产品事实 / 竞品 / 合规红线 | Phase 4 / Phase 5 |
| `references/writing-constraints.md` | 表现形式与表达节奏 | Phase 4 |
| `references/citations.md` | 引用分级 + Source Map 模板 | Phase 4 / Phase 5 |
| `references/slug-gate.md` | Slug 设计审查（7 原则 + 12 反模式） | Phase 2 |
| `references/meta-title-description.md` | title/description 长度、自检、独立优化工作流 | Phase 2 / title-only 任务 |
| `references/selfcheck.md` | 10 维健康分完整判据 | Phase 5 |
| `references/mini-example.md` | Brief + Outline 范例 | Phase 1 / Phase 3 |
| `references/portable/*` | 通用 Research / 终审件 | 按指针 |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.0.0** | 2026-08-06 | 初版：6 类路由 + 7 Phase + 4 Gate + F1–F4 金融合规 + QVeris frontmatter schema + tools/evals |

---

*qveris-blog-article · v1.0.0 · 2026-08-06 · qveris.ai/blog*
