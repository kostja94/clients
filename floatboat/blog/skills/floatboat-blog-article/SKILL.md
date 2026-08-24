---
name: floatboat-blog-article
description: >
  Create Floatboat blog articles (floatboat.ai/blog) from brief to draft.
  Self-contained skill for client delivery — 9 Phase workflow, Mode, Investment
  Score, Phase 0R, Ranking vs Comparison routing, Topic Scope, cluster folders
  (claude/deepseek/openai/worldcup/Updates), tools/ validators, portable/ audit.
metadata:
  version: 5.1.0
  project: floatboat.ai
  locale: en
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 580
  complements: ~
  forbidden-reads:
    - ../../floatboat-keywords.md
    - ../../floatboat-features.md
    - blog/README.md
    - blog/blog-live-articles.md
---

# Floatboat Blog Article Creation

为 **https://floatboat.ai/blog/** 从选题到英文成稿。

**硬性规则：Agent 只读本 skill 文件夹内文件**（含 `references/`、`references/portable/`、`tools/`），禁止读取 skill 文件夹外的仓库文档（见 `forbidden-reads`）。发布前终审用 `references/portable/final-audit.md`。

**本文件夹自包含**：项目配置、G1–G7、6 类路由 + Ranking、Topic Scope、cluster-folders 路径、Proof Library、9 Phase 工作流、12 维自检、portable/ 通用 bundle、tools/ 均可独立分发给客户。

**渐进式加载**：Agent 默认只读本文件。Phase 需要细节时，按指针读取 `references/{file}.md`（一次最多 2 个）。禁止一次性加载全部 references。

**六角色换帽**（Phase 4 与 Phase 5 **分轮**，禁止 Draft 同轮自我放行 Gate C）：

| Phase | 角色 |
|-------|------|
| 0 / 0R | Strategist / Researcher |
| 1–3 | Strategist + SME |
| 4 | Writer |
| 5 / audit | Editor / Auditor |

---

## §0 如何使用

### 触发语

```
按 floatboat-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Research|Comparison|Ranking|Alternative|Product|Announcement} 文章。
发布目的：{SEO|品牌|转化|社区}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
Topic Scope：{scheduling-agent|floatim|combo-skills}
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主关键词 | ✅ | 决定 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Mode | 可选 | Announcement→lite；Research/Comparison/Ranking→flagship |
| Topic Scope | 推荐 | scheduling-agent / floatim / combo-skills |
| 竞品参考 URL | 推荐 | Phase 0R |
| 署名作者 | 推荐 | Kostja / Floatboat Team / 具体成员 |

### 输出（Phase 6 交付物，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief | ✅ | ✅ | ✅ |
| 2 | Research Log（R1–R3 + Synthesis） | 简 | ✅ | ✅ |
| 3 | 成稿 `floatboat/blog/[{cluster}/]NN-{slug}.md`（NN **58**） | ✅ | ✅ | ✅ |
| 4 | SelfCheck（H0–H4 + 12 维） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | Internal Link Plan | — | ✅ | ✅ |
| 8 | 终审指令（`references/portable/final-audit.md`） | ✅ | ✅ | ✅ |
| 9 | Post-publish Metric Spec | — | ✅ | ✅ |
| 10 | 提示人类更新 `blog/README.md` | ✅ | ✅ | ✅ |

**禁止单独生成**：`blog/schema/*.json` · `blog/images/` · ItemList JSON-LD 文件。

与用户沟通可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化 title/description | 未来 `floatboat-meta-title-description` |
| 已有完整稿，仅需终审 | `references/portable/final-audit.md` |
| 非 floatboat.ai 博客 | 其他项目 blog skill |

---

## §1 项目配置速查

> **完整配置 → `references/project-config.md`**
> **Topic Scope → project-config §3 · G1–G7 → §4**

| 配置项 | Floatboat 值 |
|--------|-------------|
| **blogLayout** | **cluster-folders**（见 §4 + `content-graph.md` §1B） |
| **博客前缀** | `/blog/`（slug kebab-case，**不含**子目录前缀） |
| **Pillar Hub** | `what-is-agentic-calendar` |
| **下一序号 NN** | **58**（见 `content-graph.md` §1） |
| **品类表述** | *The Proactive Agent OS that Runs Work from the Calendar* |
| **受众** | solopreneur / solo founder |
| **署名默认** | `Floatboat`；Research 优先 `Tan Shaoqing` |
| **日期策略** | 每自然日 ≤1 篇；从锚点日往前错开 |
| **禁止内链** | 404 / forthcoming 路径（G6） |

---

## §1B Mode 系统

| Mode | 适用 | Phase 深度 |
|------|------|-----------|
| **lite** | Announcement、短帖 | 最小 Research + BLUF |
| **standard** | Alternative / Product / 多数 Spoke | 完整 0R + Extractability |
| **flagship** | Research / Comparison / Ranking / Glossary | 全流程 + Moat + Excellence 必须 Yes |

默认：未指定 → **standard**。§2 路由表指定各类型默认 Mode。

---

## §2 文章类型路由

> **完整路由 + H2 模板 + Frontmatter → `references/article-types.md`**

| 类型 | 词数目标 | 产品上限 | 默认 Mode | `--intent` / `--min` |
|------|----------|:---:|:---:|------|
| Research / Glossary | 2400–3500 | ≤15% | flagship | `research` / `--min 2400` |
| Comparison | 2800–3500 | ≤40% | flagship | `comparison` / `--min 2800` |
| **Ranking / Listing** | 2400–3200 | ≤40% | flagship | `comparison` / `--min 2400` |
| Alternative | 2200–3000 | ≤35% | standard | `comparison` / `--min 2200` |
| Product / Scenario | 2000–2700 | ≤50% | standard | `product_tutorial` / `--min 2000` |
| Announcement | 1500–2000 | 不限 | lite | `announcement` / `--min 1500` |

**路由规则**：

- `best`/`top` + **≥3 具名竞品** → **Ranking**（`articleFormat: Ranking`）
- `vs` + 2 产品 → **Comparison**
- `alternative` + 单竞品 → **Alternative**
- `what is` / 范式 → **Research**
- pipeline / workflow → **Product**
- 新品发布 → **Announcement**（常放 `Updates/`）

**信息增量**：相对 SERP Top3 须 **≥2 项**独有增量。

### 增长职能（Brief 必填 SuccessMetric）

| 职能 | 适用类型 |
|------|----------|
| CategoryPOV | Research / Glossary |
| SearchCapture | Ranking / Alternative |
| EvaluationComparison | Comparison |
| ActivationTutorial | Product / Scenario |
| OpinionNarrative | Announcement |

---

## §3 创作工作流（9 Phase + 5 Gate）

```
Phase 0  ─ Intake & Gate A         (Mode + Topic Scope + Investment Score + 六必问)
    ↓ PASS
Phase 0R ─ Research 三角 & Gate 0R  (R1→R2→R3→Synthesis；Proof Library)
    ↓ PASS / ❌ → §3.G 回溯
Phase 1  ─ Article Brief           (+ ProofLibraryRefs, Cluster, category)
Phase 2  ─ Slug、Date、Path & Gate B (+ cluster-folders 路径)
    ↓ PASS / ❌ → §3.G 回溯
Phase 3  ─ Outline                 (+ internal-links 矩阵)
Phase 3.5─ Outline 交叉检查        (同批 ≥2 篇强制)
    ↓ PASS / ❌ → §3.G 回溯
Phase 4  ─ Draft                   (+ writing-constraints, BLUF 三处)
Phase 5  ─ SelfCheck & Gate C      (tools/ + references/selfcheck.md)
    ↓ PASS / ❌ → §3.G 回溯
Phase 5.5─ Cross-Article Audit     (同批 ≥2 篇强制)
Phase 6  ─ Delivery
```

---

### Phase 0 — Intake & Gate A

> **Investment Score → `references/portable/investment-score.md`**
> **Gate 细则 → `references/portable/gates-master.md` · `references/gates.md`**

#### 0.0 六必问

| # | 问题 |
|---|------|
| 1 | 目标 SEO 关键词 + 受众？ |
| 2 | 发布目的（SEO / 品牌 / 转化 / 社区）？ |
| 3 | 竞品 URL（2–3 个）？ |
| 4 | 内链目标页是否已上线？ |
| 5 | **署名作者**？ |
| 6 | **category**（Research / Comparison / Product / Claude / DeepSeek / OpenAI / World Cup 等）？ |

**Phase 0 首行强制输出**：

```
## Mode: lite | standard | flagship
## ArticleType: CategoryPOV | SearchCapture | …
## InvestmentScore: {1.0–5.0}
## Topic Scope: scheduling-agent | floatim | combo-skills
## Cluster: {cluster-id | standalone}
## File path: floatboat/blog/[{folder}/]NN-{slug}.md
## Category: {frontmatter category}
## Author: {author}
## Gate A: KEEP | MERGE → {slug} | STOP
```

#### 0.1 Investment Score

五因子各 1–5，算术平均。≥4.0 KEEP；3.0–3.9 降级 Mode；<3.0 MERGE/STOP。

#### 0.2 Gate A — KEEP/MERGE

三条件满足 ≥2 → KEEP（对照 `content-graph.md`）。

#### 0.3 信息增量 Gate

KEEP 后：相对 SERP Top3 **≥2 项** Floatboat 可提供的独有增量。

---

### Phase 0R — Research 三角 & Gate 0R

> **完整流程 → `references/portable/research-triangle.md`**
> **SERP Fit → `references/portable/serp-fit-template.md`**

**R1 第一步**：加载 `references/proof-library.md`；Brief 填 `ProofLibraryRefs: [PFL-xxx, …]`。

```
R1 — project-config + product-competitors + content-graph + proof-library
    ↓
R2 — Web 搜索（SERP Top 5 + PAA）
    ↓
R3 — Fetch URL（floatboat.ai 官方 + SERP Top 3–5）
    ↓
Synthesis + Research Log + SERP Fit → Gate 0R Pass
```

**Degraded**：WebSearch 不可用时标注；P0 claim 不得未验证。

---

### Phase 1 — Article Brief

> **范例 → `references/mini-example.md`**

Brief 必含：Mode · ArticleType · SuccessMetric · ProofLibraryRefs · Category · Topic Scope / Cluster · Pillar link · Information increment（≥2 项）· `articleFormat: Ranking`（Ranking 类）· PostPublishReviewDates（standard/flagship）。

---

### Phase 2 — Slug、Date、Path & Gate B

> **Slug → `references/gates.md` §5 + `article-types.md` §9**
> **Cluster 路径 → `references/topic-cluster-layout.md` + `content-graph.md` §1B**

1. Slug 候选（kebab-case，**无** `/blog/` 前缀于 slug 字段；公开 URL 为 `/blog/{slug}`）
2. Gate B：6 问 + 反模式零触发
3. **publishDate**：`content-graph.md` 日期表，一天一篇
4. **文件路径**：

```
读 content-graph §1B
  → folder 有值 → floatboat/blog/{folder}NN-{slug}.md
  → standalone → floatboat/blog/NN-{slug}.md
```

5. Frontmatter：Ranking 加 `articleFormat: Ranking`；簇内文见 §4 双分类

---

### Phase 3 — Outline

- H2 模板 → `article-types.md`
- Phase 3.5 对照 `references/internal-links.md` 集群矩阵
- Reader mental state 必填（禁空泛 "Interested"）

---

### Phase 3.5 — Outline 交叉检查

**触发**：同批 ≥2 篇。**详见** `references/portable/outline-cross-check.md` + `internal-links.md`。

单篇：标注 `N/A — single article`。

---

### Phase 4 — Draft

**加载顺序**（≤2 文件/轮）：

1. `references/writing-constraints.md`
2. `references/product-competitors.md`
3. `references/project-config.md`

flagship 额外 → `references/portable/extractability-checklist.md`

**BLUF 三处**：TL;DR bullet 1（40–60 词定义句）· 每 major H2 首段先答 · FAQ 首句即答

---

### Phase 5 — SelfCheck & Gate C

> **完整 checklist → `references/selfcheck.md`**

#### 工具先跑（从 `floatboat/` 根目录）

```bash
python blog/skills/floatboat-blog-article/tools/frontmatter_validator.py blog/{path} --keyword "{kw}" --categories "Research,Comparison,Product,Reference,Claude,DeepSeek,OpenAI,World Cup"
python blog/skills/floatboat-blog-article/tools/word_count_narrative.py blog/{path} --intent {intent} --min {threshold}
python blog/skills/floatboat-blog-article/tools/link_checker.py blog/{path} --forbidden ""
```

**Gate C**：H0–H4 + 12 维全 Pass → **audit-ready**。终审 → `references/portable/final-audit.md`。

---

### Phase 5.5 — Cross-Article Audit

同批 ≥2 篇：叙事雷同 · 互链完整性 · Intro/Conclusion 互换测试 · Canonical 越界（见 selfcheck 维 12）。

---

### Phase 6 — Delivery

1. 写入 `floatboat/blog/[{cluster}/]NN-{slug}.md`
2. Brief + SelfCheck + Source Map + SERP Fit + Internal Link Plan
3. **终审指令**：

```
按 references/portable/final-audit.md 执行发布前终审：
- 文件：floatboat/blog/{path}
- 项目：floatboat.ai / Floatboat
- 类型：{Article type}
- 主关键词：{primary keyword}
```

4. 提示人类更新 `blog/README.md`

---

### §3.G Gate 回溯表

| Fail 于 | 回退至 | 动作 |
|---------|--------|------|
| Gate A / Investment | Phase 0 | 改角度 / MERGE / STOP |
| Gate 0R | Phase 0R | 补 R2/R3 |
| Gate B | Phase 2 | 重选 slug / 修正 cluster 路径 |
| Gate C — H3 | Phase 4 | 扩写 |
| Gate C — H4 / 维 12 | Phase 4 | Floatboat 专属修复 |
| Phase 3.5 / 5.5 | Phase 3 / 4 | 改差异 |

---

## §4 集群与 frontmatter

> **Cluster 注册表 → `references/content-graph.md` §1B**
> **布局规则 → `references/topic-cluster-layout.md`**

| Cluster ID | folder | Hub slug | category 主分类 |
|------------|--------|----------|----------------|
| scheduling-agent | *(root)* | what-is-agentic-calendar | Research / Product / Comparison |
| updates | `Updates/` | introducing-floatim | Product / Features |
| floatim | `Updates/` | introducing-floatim | Product |
| claude | `claude/` | what-is-claude-cowork | **Claude** + secondaryCategory |
| deepseek | `deepseek/` | what-is-deepseek-agent | **DeepSeek** + secondaryCategory |
| openai | `openai/` | codex-harness-open-source | **OpenAI** + secondaryCategory |
| worldcup | `worldcup/` | world-cup-2026-guide | **World Cup** + secondaryCategory |
| model-singles | *(root)* | — | Research / Product |
| obsidian | *(root)* | what-is-obsidian-vault | Research / Product |

**双分类示例（claude/ 内）**：

```yaml
category: "Claude"
secondaryCategory: "Research"
articleFormat: "Ranking"   # Ranking 文必填
```

**内链**：永远 `/blog/{slug}`，禁止 `/blog/claude/{slug}`。

---

## §5 Reference 索引（均在 skill 文件夹内）

| 文件 | 加载时机 |
|------|----------|
| `references/project-config.md` | Phase 0R, 4, 5 |
| `references/article-types.md` | Phase 0, 2, 3, 4 |
| `references/gates.md` | Phase 0, 2 |
| `references/content-graph.md` | Phase 0, 2, 3.5, 5.5 |
| `references/topic-cluster-layout.md` | Phase 0, 2 |
| `references/internal-links.md` | Phase 3, 3.5 |
| `references/writing-constraints.md` | Phase 4 |
| `references/product-competitors.md` | Phase 0R, 4 |
| `references/proof-library.md` | Phase 0R |
| `references/selfcheck.md` | Phase 5 |
| `references/keywords.md` | Phase 0, 0R |
| `references/mini-example.md` | Phase 1, 3 |
| `references/portable/*` | 按 Phase 指针 |
| `references/floatboat-blog-schema.md` | **禁止加载**（归档） |
| `tools/` | Phase 5 |

---

## §6 Gotchas（Floatboat 精选）

- ❌ Ranking 文用 Comparison 双产品模板（应 numbered H3 + `articleFormat: Ranking`）
- ❌ 混用 Topic Scope 禁混词（Scheduling 文写 FloatIM P0 词）
- ❌ slug 含子目录前缀 · 内链写 `/blog/claude/...`
- ❌ FloatIM 与 Floatboat 桌面工作区混为一谈
- ❌ 生成 `blog/schema/*.json`
- ❌ Gate 未 Pass 交付 · 一次加载全部 references · 读 skill 文件夹外文档
- ❌ 旧触发语要求加载 blog-create L0

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **5.1.0** | 2026-08-24 | **客户交付自包含版**：`self-contained: true`；完整 9 Phase 内联；topic-cluster-layout 内置；终审用 portable/final-audit；NN→58；撤销 L0 外部依赖 |
| 5.0.0 | 2026-08-23 | 路线 A 试验（L0+L1，已废弃） |
| 4.0.0 | 2026-07-31 | SelfCheck 内联 |
| 3.0.0 | — | 9 Phase 自包含 monolith |

---

*floatboat-blog-article · v5.1.0 · 2026-08-24 · self-contained*
