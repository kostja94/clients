---
name: moras-blog-article
description: >
  Create Moras blog articles (moras.ai/blog) from brief to draft. Self-contained
  skill for client delivery — 9 Phase workflow, Mode, Investment Score, Phase 0R,
  I1–I5 Income Claim Gate, 8 TikTok Shop article types, tools/ validators,
  portable/ audit bundle. Also handles title/description-only tasks via
  meta-title-description.md.
metadata:
  version: 2.1.0
  project: moras.ai
  locale: en
  market: US TikTok Shop (default; overridable per article topic)
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 580
  complements: ~
  forbidden-reads:
    - ../../moras-*.md
    - blog/README.md
---

# Moras Blog Article Creation

为 **https://moras.ai/blog/** 从选题到英文成稿。

**硬性规则：Agent 只读本 skill 文件夹内文件**（含 `references/`、`references/portable/`、`tools/`、`evals/`），禁止读取 skill 文件夹外的仓库文档（见 `forbidden-reads`）。发布前终审用 `references/portable/final-audit.md`。

**本文件夹自包含**：项目配置、G1–G7 + I1–I5、8 类路由、Topic Scope、内容图谱、引用分级、表现形式、9 Phase 工作流、12 维创作自检、portable/ 通用 bundle、tools/ 验证脚本均可独立分发给客户。

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
按 moras-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Pillar|Setup|Production|Research|Framework|Strategy|SideHustle|Diagnosis|PlatformOps} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
Topic Scope：{tiktok-shop-affiliate|moras-product|ecommerce-industry|other}
Intent lane：{Video|Research|Both}
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主关键词 | ✅ | 决定 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Mode | 可选 | Pillar/Framework/Research→flagship；Platform Ops→lite |
| Topic Scope | 推荐 | 决定 I1–I5 哪些 Gate 生效 |
| Intent lane | 推荐 | Video / Research / Both |
| 竞品参考 URL | 推荐 | Phase 0R |

### 输出（Phase 6 交付物，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief | ✅ | ✅ | ✅ |
| 2 | Research Log（R1–R3 + Synthesis） | 简 | ✅ | ✅ |
| 3 | 成稿 `moras/blog/{folder}/NN-{working-slug}.md`（NN **69**） | ✅ | ✅ | ✅ |
| 4 | SelfCheck（H0–H4 + I1–I5 + 12 维） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | Internal Link Plan | — | ✅ | ✅ |
| 8 | Cannibalization Check（blog + TVG） | ✅ | ✅ | ✅ |
| 9 | 终审指令（`references/portable/final-audit.md`） | ✅ | ✅ | ✅ |
| 10 | Post-publish Metric Spec | — | ✅ | ✅ |
| 11 | 提示人类更新 `blog/README.md` | ✅ | ✅ | ✅ |

与用户沟通可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化 title/description | **`references/meta-title-description.md`**（禁止改正文） |
| 已有完整稿，仅需发布前终审 | `references/portable/final-audit.md` |
| TVG 落地页（`/tiktok-video-generator/*`） | TVG 模板体系 |
| 非 moras.ai 博客 | 其他项目 blog skill |

### 仅优化 title / description

加载本 skill 后 **只读** `references/meta-title-description.md`；**禁止**改 H2 / TL;DR / FAQ / 正文；**禁止**跑完整 Phase 0–6。

---

## §1 项目配置速查

> **完整配置 + G1–G7 + I1–I5 → `references/project-config.md`**
> **产品事实 + TVG 白名单 → `references/product-competitors.md`**
> **Cluster 文件夹路由 → `references/topic-cluster-layout.md`**

| 配置项 | Moras 值 |
|--------|----------|
| **blogLayout** | cluster-folders（`moras/blog/{folder}/NN-{slug}.md`；Cluster D 在根目录） |
| **博客前缀** | `/blog/`（**frontmatter `slug` 已含此前缀**） |
| **Pillar Hub** | `/blog/how-to-make-money-on-tiktok` |
| **下一序号 NN** | **69**（见 `content-graph.md` §4.1） |
| **Primary ICP** | US TikTok Shop affiliate creators |
| **作者默认** | `Kostja` |
| **日期策略** | `isoDate` 全库唯一；一天一篇；新稿 = 最晚 date +1 天 |
| **禁止内链** | `/use-cases/*` `/app/*` 等 + forthcoming（G6） |
| **内链 SSOT** | `references/internal-links.md`（R1–R7 + 分布均质 + 审计） |

### G1–G7 + I1–I5 阻断速查

| Gate | 项数 | 说明 |
|------|:---:|------|
| **G1–G7** | 7 | 事实 / 死链 / 无来源数字 / 竞品状态 / 夸大 / 内链 / 品牌 |
| **I1–I5** | 5 | 收入承诺 / 证言 / 政策时效 / Who-How-Why / 复述 SERP |

I1–I5 在 Topic Scope ≠ tiktok-shop-affiliate 时按 project-config 跳过规则。**全部 Pass 方可 Gate C**。

---

## §1B Mode 系统

| Mode | 适用 | Phase 深度 |
|------|------|-----------|
| **lite** | Platform Ops、短诊断 | 最小 Research；SERP Fit 简版 |
| **standard** | Setup / Production / Strategy / Side Hustle / Diagnosis | 完整 0R + Extractability |
| **flagship** | Pillar / Framework / Research | 全流程 + Moat + Excellence 必须 Yes |

默认：用户未指定 → **standard**。§2 路由表指定各类型默认 Mode。

---

## §2 文章类型路由

> **8 类路由 + H2 模板 + Voice/Who/How/Why → `references/article-types.md`**

| 类型 | 词数 | 产品上限 | 默认 Mode | `--intent` / `--min` |
|------|------|:---:|:---:|------|
| **Pillar** | 3500–5000 | ≤20% | flagship | `pillar` / `--min 3500` |
| **Setup** | 2500–3500 | ≤25% | standard | `howto` / `--min 2500` |
| **Production** | 2800–3800 | ≤35% | standard | `product` / `--min 2800` |
| **Research** | 2800–3500 | ≤30% | flagship | `research` / `--min 2800` |
| **Framework** | 2500–3200 | ≤25% | flagship | `framework` / `--min 2500` |
| **Strategy** | 2500–3200 | ≤30% | standard | `howto` / `--min 2500` |
| **Side Hustle** | 2200–3000 | ≤30% | standard | `howto` / `--min 2200` |
| **Diagnosis** | 2500–3200 | ≤25% | standard | `diagnosis` / `--min 2500` |
| **Platform Ops** | 1800–2500 | ≤15% | lite | `announcement` / `--min 1800` |

**路由规则**：`how to make money` → Pillar；`setup` → Setup；faceless → Production；`product research` → Research；hooks + framework → Framework；captions/hashtags → Strategy；`side hustle` → Side Hustle；`no sales` → Diagnosis；TikTok 平台操作 → Platform Ops。

**非 TikTok Shop 话题**：Phase 0 声明 Topic Scope；跳过不适用的 I Gate；保留 G1–G7 + Moras Voice。

**信息增量**：相对 SERP Top3 须 **≥2 项**独有增量（框架 / 决策表 / 内部观察 / 跨篇边界）。

---

## §3 创作工作流（9 Phase + 5 Gate）

```
Phase 0  ─ Intake & Gate A         (Mode + Topic Scope + Investment Score + 六必问)
    ↓ PASS
Phase 0R ─ Research 三角 & Gate 0R  (R1→R2→R3→Synthesis)
    ↓ PASS / ❌ → §3.G 回溯
Phase 1  ─ Article Brief
Phase 2  ─ Slug、Date & Gate B
    ↓ PASS / ❌ → §3.G 回溯
Phase 3  ─ Outline
Phase 3.5─ Outline 交叉检查（同批 ≥2 篇强制）
    ↓ PASS / ❌ → §3.G 回溯
Phase 4  ─ Draft
Phase 5  ─ SelfCheck & Gate C（H0–H4 + I1–I5 + 12 维）
    ↓ PASS / ❌ → §3.G 回溯
Phase 5.5─ Cross-Article Audit（同批 ≥2 篇强制）
Phase 6  ─ Delivery
```

---

### Phase 0 — Intake & Gate A

> **Investment Score → `references/portable/investment-score.md`**
> **Gate 细则 → `references/portable/gates-master.md`**

#### 0.0 话题范围判定（先于一切）

| 话题范围 | 判定信号 | Gate 调整 |
|---------|---------|-----------|
| **tiktok-shop-affiliate**（默认） | TikTok Shop / affiliate / 佣金 / 选品 | G1–G7 + I1–I5 全生效 |
| **moras-product** | Moras update / changelog / company | 跳过 I3/I5 |
| **ecommerce-industry** | e-commerce / AI trends | 跳过 I1–I3 |
| **other** | 不匹配以上 | 补问 ICP 与 market |

**Phase 0 首行强制输出**：

```
## Mode: lite | standard | flagship
## Topic Scope: tiktok-shop-affiliate | moras-product | ecommerce-industry | other
## ArticleType: Pillar | Setup | … | PlatformOps
## InvestmentScore: {1.0–5.0} — {五因子摘要}
## Intent lane: Video | Research | Both
## File path: moras/blog/{folder}/NN-{working-slug}.md
## Gate A: KEEP | MERGE → {slug} | STOP
```

#### 0.1 六必问

| # | 问题 |
|---|------|
| 1 | 目标 SEO 关键词 + search intent？ |
| 2 | 目标读者？（affiliate / 小达人 / 卖家） |
| 3 | 发布目的？SEO / 品牌 / 转化 |
| 4 | 竞品内容 2–3 URL？ |
| 5 | Intent lane：Video / Research / Both？ |
| 6 | Cluster role + Pillar link（Spoke 必填）？ |

#### 0.2 Investment Score

五因子各 1–5，算术平均。≥4.0 KEEP；3.0–3.9 降级 Mode；<3.0 MERGE/STOP。

#### 0.3 Gate A — KEEP/MERGE

三条件满足 ≥2 → KEEP（对照 `content-graph.md` §4.1）。

#### 0.4 信息增量 Gate

KEEP 后：相对 SERP Top3 须 **≥2 项** 独有增量，否则 STOP。

---

### Phase 0R — Research 三角 & Gate 0R

> **完整流程 → `references/portable/research-triangle.md`**
> **SERP Fit → `references/portable/serp-fit-template.md`**

```
R1 — project-config + product-competitors + content-graph (+ proof-library 可选)
    ↓
R2 — Web 搜索（primary keyword → SERP Top 5 + PAA）
    ↓
R3 — Fetch URL（TikTok Shop 文 ≥1 官方源 + SERP Top 3–5）
    ↓
Synthesis + Information Gain Statement（≥2 项）
    ↓
Research Log + SERP Fit → Gate 0R Pass → Phase 1
```

**Mode 差异**：lite 可简版 R2/R3；flagship 须完整 R3 Top5 + ≥2 Candidate Examples。

**Degraded**（WebSearch 不可用）：标注 `Research mode: Degraded`；政策/定价 P0 claim 不得写未验证数字。

---

### Phase 1 — Article Brief

> **模板 + 范例 → `references/mini-example.md` · `references/article-types.md` §2.12**

Brief 必含：Mode · Topic Scope · Article type · Intent lane · Cluster role · Pillar link · Information Gain Statement · KEEP/MERGE · Compliance notes · PostPublishReviewDates（standard/flagship）。

---

### Phase 2 — Slug、Date & Gate B

> **Slug 规则 → `references/slug-gate.md` §13**
> **Meta → `references/meta-title-description.md`**

1. Slug 候选 **`/blog/{url-slug}`**（frontmatter 含前缀；文件名不含 `/blog/`）
2. Gate B：6 问 + 12 反模式零触发
3. `isoDate`：一天一篇，取 portfolio 最晚 date +1 天
4. title 45–60 / description 140–160
5. 复核 Phase 0R SERP Fit

---

### Phase 3 — Outline

按 `article-types.md` H2 模板；每节标注词数、关键词、内链占位、Moras 出现计划。

---

### Phase 3.5 — Outline 交叉检查

**触发**：同批 ≥2 篇。**详见** `references/portable/outline-cross-check.md`。

检查 H2 重复、Synthesis 冲突、Spoke 是否链回 Pillar。单篇标注 `N/A — single article`。

---

### Phase 4 — Draft

**加载顺序**（≤2 文件/轮）：

1. `references/article-types.md`（Voice §8）
2. `references/citations.md`
3. `references/presentation.md`

flagship 额外 → `references/portable/extractability-checklist.md`

**核心约束**：affiliate-first · P0 数字有来源 · 长段落 ≥3 · 列表占比 ≤ 类型上限 · CTA ≤2 · US-only（TikTok Shop 文）· 无 `## Related articles`

**BLUF 三处**：TL;DR 长描述（60–110 词）+ bullets · 每 major H2 首段先答 · FAQ 首句即答

---

### Phase 5 — SelfCheck & Gate C

> **完整 checklist → `references/selfcheck.md`**
> **Gate 细则 → `references/portable/gates-master.md`**

#### 工具先跑（从 `moras/` 根目录）

```bash
python skills/blog-article/tools/frontmatter_validator.py blog/{NN-slug}.md --keyword "{kw}" --moras-slug
python skills/blog-article/tools/word_count_narrative.py blog/{NN-slug}.md --intent {intent} --min {threshold}
python skills/blog-article/tools/link_checker.py blog/{NN-slug}.md --forbidden "/use-cases/,/app/,/auth/,/admin/"
```

**Gate C**：H0–H4 + I1–I5 + 12 维全 Pass → **audit-ready**。终审 → `references/portable/final-audit.md`。

---

### Phase 5.5 — Cross-Article Audit

同批 ≥2 篇：叙事雷同 · 互链完整性 · Intro/Conclusion 互换测试 · TVG cannibalization（见 gotchas #29–#31）。

---

### Phase 6 — Delivery

1. 写入 `moras/blog/{folder}/NN-{working-slug}.md`（Cluster D 在根目录；folder 见 `topic-cluster-layout.md`）
2. Article Brief 最终版 + SelfCheck 表
3. Source Map + SERP Fit + Cannibalization Check + Internal Link Plan（standard/flagship）
4. **终审指令**：

```
按 references/portable/final-audit.md 执行发布前终审：
- 文件：moras/blog/{folder}/NN-{slug}.md
- 项目：moras.ai / Moras
- 类型：{Article type}
- 主关键词：{primary keyword}
```

5. 提示人类更新 `blog/README.md`

---

### §3.G Gate 回溯表

| Fail 于 | 回退至 | 动作 |
|---------|--------|------|
| Gate A / Investment | Phase 0 | 改角度 / MERGE / STOP |
| Gate 0R | Phase 0R | 补 R2/R3 / 降 Degraded claim |
| Gate B | Phase 2 | 重选 slug |
| Gate C — H3 | Phase 4 | 扩写至类型下限 |
| Gate C — I1–I5 | Phase 4 | 改合规表述 |
| Gate C — 12 维 | Phase 4 | 按维度修复 |
| Phase 3.5 / 5.5 | Phase 3 / 4 | 改 Outline 或正文差异 |

---

## §4 创作 vs 审核 vs Meta

| | **moras-blog-article** | **portable/final-audit.md** | **meta-title-description.md** |
|------|:---:|:---:|:---:|
| 做什么 | **生成**文章 | **终审**（S/A/B/C/D） | **优化** title/description |
| 时机 | 选题→成稿 | SelfCheck Pass 后 | Phase 2 或独立任务 |
| 评分 | H0–H4 + 12 维 Pass/Fail | 加权 0–100 | 计字符 + 四条自检 |

**硬规则**：SelfCheck = audit-ready；终审 ≥70 + P0 Pass = publish-ready。不可互相替代。

---

## §5 Reference 索引（均在 skill 文件夹内）

| 文件 | 加载时机 |
|------|----------|
| `references/project-config.md` | Phase 0, 5 |
| `references/article-types.md` | Phase 0, 2, 3, 4 |
| `references/content-graph.md` | Phase 0, 2, 3.5, 5.5 |
| `references/topic-cluster-layout.md` | Phase 2, 6（文件路径） |
| `references/slug-gate.md` | Phase 2 |
| `references/product-competitors.md` | Phase 0R, 4, 5 |
| `references/presentation.md` | Phase 4 |
| `references/citations.md` | Phase 4, 5 |
| `references/keywords.md` | Phase 0, 0R |
| `references/meta-title-description.md` | Phase 2 / title-only |
| `references/mini-example.md` | Phase 1, 3 |
| `references/proof-library.md` | Phase 0R（可选） |
| `references/selfcheck.md` | Phase 5 |
| `references/portable/*` | 按 Phase 指针 |
| `tools/` | Phase 5 |
| `evals/` | skill 变更后回归 |

**维护者同步 SSOT**（内网维护用，客户包已内置副本）：

```powershell
Copy-Item "E:\Agent执行\blog-create\references\portable\*.md" `
  "references\portable\" -Force
```

---

## §6 Gotchas（37 条精选）

**结构与 slug**：TL;DR 须长描述+bullets · 无 Related 模块 · slug 须 `/blog/` 前缀 · 禁内部架构词 · Framework 非 hook 清单

**链接**：禁 `/use-cases/*` 等 · forthcoming ≤1 · TL;DR/FAQ 无内链 · 同 slug ≤2 · H2 均匀分布 · 详见 `references/internal-links.md`

**品牌与合规**：Moras 非 Morris · 无 TikTok 官方暗示 · 裸引 $15.8B（G3）· 收入承诺（I1）· 政策 as-of（I3）

**流程**：Gate 未 Pass 不交付 · 渐进式加载 · 不读 skill 文件夹外文档 · 混淆 SelfCheck 与终审

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **2.1.1** | 2026-08-24 | **`internal-links.md`**：R1–R7 + H2 分布均质 + `link_audit.py` 全库 Gate |
| **2.1.0** | 2026-08-24 | **客户交付自包含版**：`self-contained: true`；完整 9 Phase 内联；portable/ + tools/ + selfcheck 内置；终审用 portable/final-audit；撤销 L0 外部依赖 |
| 2.0.0 | 2026-08-24 | 路线 A 试验（L0+L1，已废弃） |
| 1.3.1 | 2026-08-04 | meta-title-description 并入 |
| 1.2.0 | 2026-06-15 | references/ 拆分 + I1–I5 + evals |

---

*moras-blog-article · v2.1.0 · 2026-08-24 · self-contained · US TikTok Shop*
