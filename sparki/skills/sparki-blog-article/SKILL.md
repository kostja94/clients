---
name: sparki-blog-article
description: >-
  Create Sparki blog articles (sparki.io/blog) from brief to draft. Sparki is
  the first AI editing agent — conversational, cloud video editing for
  creators. Skill covers creator-clone, workflow how-to, feature-guide,
  comparison, alternative/roundup, category-POV, and announcement article
  types, with Mode system, Investment Score, Phase 0R research triangle, 9-Phase
  workflow, G1-G7 gates, tools/ validators, and portable/ audit bundle.
metadata:
  version: 1.0.0
  project: sparki.io
  locale: en
  market: US creators (default; overridable per article topic)
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 480
  complements: ~
  forbidden-reads:
    - ../sparki.md
    - ../sparki-*.md
    - ../creators/**
    - ../video-types/**
    - ../ai-traffic-report/**
    - ../../demo/**
    - ../../luciusai/**
    - ../../moras/**
    - ../../floatboat/**
    - ../../Alignify/**
---

# Sparki Blog Article Creation

为 **https://sparki.io/blog/** 从选题到英文成稿（OpenBlog 部署，`E:\客户部署项目\sparki-blog`）。

**硬性规则：Agent 只读本 skill 文件夹内文件**（含 `references/`、`references/portable/`、`tools/`），禁止读取 skill 文件夹外的仓库文档（见 `forbidden-reads`）。发布前终审用 `references/portable/final-audit.md`。

**渐进式加载**：Agent 默认只读本文件。Phase 需要细节时，按指针读取 `references/{file}.md`（一次最多 2 个）。读完即弃，不跨 Phase 保留 reference 上下文。

**成稿落盘**：OpenBlog 部署仓 `E:\客户部署项目\sparki-blog\content\blog\{slug}.md`——**slug 必须等于文件名**（`validate:posts` 强校验）；无 NN 序号前缀（与 luciusai `NN-` 体系不同）。

**六角色换帽**（Phase 4 与 Phase 5 分轮，禁止 Draft 同轮自我放行 Gate C）：

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
按 sparki-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{CreatorClone|WorkflowHowTo|FeatureGuide|Comparison|AlternativeRoundup|CategoryPOV|Announcement} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主关键词 | ✅ | 决定 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Mode | 可选 | 未指定→**standard**；Announcement 自动 lite，CreatorClone/Comparison 自动 flagship |
| 竞品/参考 URL | 推荐 | Phase 0R 信息增量判断 |
| 红人素材链接 | CreatorClone 必填 | 该 creator 公开视频/账号 URL，Phase 0R 抓取验证 |

### 输出（交付物，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief（含 SuccessMetric、MoatAssetPlanned、AnswerBlocks） | ✅ | ✅ | ✅ |
| 2 | Research Log（R1–R3 + Synthesis） | 简 | ✅ | ✅ |
| 3 | 成稿 `content/blog/{slug}.md`（OpenBlog 部署仓） | ✅ | ✅ | ✅ |
| 4 | SelfCheck 表（H0–H4 + 12 维 Pass/Fail） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | OG/Cover Image Prompt | ✅ | ✅ | ✅ |
| 8 | Internal Link Plan | — | ✅ | ✅ |
| 9 | 终审指令（`references/portable/final-audit.md`） | ✅ | ✅ | ✅ |
| 10 | Post-publish Metric Spec | — | ✅ | ✅ |

与用户沟通可用中文；**正文必须为英文**（en-US）。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 非 sparki.io 博客 | 对应项目 blog skill |
| 仅改既有文章 frontmatter/meta | 直接编辑，不跑 Phase 0–6 |
| 既有文章内容大改/合稿 | 只跑 Phase 5 复核 + final-audit |
| 红人/行业/视频类型落地页（`/creators/*`、`/industries/*`、`/video-editor/*`） | 主站页面体系（非本 blog skill） |

---

## §1 项目配置速查

> **完整配置 + G1–G7 + URL 白名单 → `references/project-config.md`**
> **产品事实 + 竞品矩阵 → `references/product-competitors.md`**
> **61 篇既有文章 → `references/content-graph.md`**

| 配置项 | Sparki 值 |
|--------|-----------|
| **产品** | Sparki — the first AI editing agent（对话式 AI 剪辑） |
| **域名** | sparki.io |
| **博客前缀** | `/blog/`（frontmatter `slug` **不含** `/blog/` 前缀；线上 URL = `/blog/{slug}`） |
| **定位** | Chat-to-edit：上传素材 → 自然语言 → Agent 规划并执行 → 多轮修订；云端处理 |
| **核心功能** | Copy Style、Long to Short、AI Caption、AI Commentary、Video Resizer（另有 Highlight Reels 等 solutions） |
| **定价（as of）** | Free 300 credits + 3GB · Starter/Plus 月付或年付（年付约 −40%）· Enterprise（API/SLA/并发，enterprise@sparki.io） |
| **作者** | `Sparki Team`（Organization） |
| **日期** | `date` = 发布日（UTC `YYYY-MM-DD`），永不变；`updated` 仅实质性更新时出现 |
| **Category 枚举** | `Clone Edit Viral Videos` · `Video Editing Features` · `ai-video-editor` · `AI Video Editing` · `AI Tools` · `Editor-in-browser` |
| **语言** | en-US 正文；中文仅沟通 |
| **站内页面链接** | 一律**绝对 URL** `https://sparki.io/...`（blog 是独立 OpenBlog 部署，Rewrite 只覆盖 `/blog/*`）；blog 互链用 `/blog/{slug}` 相对 |
| **发布通道** | OpenBlog 部署仓：`npm run validate:posts` → build → 运维侧上线 |

### G1–G7 阻断速查

| # | 阻断条件 | 说明 |
|---|---------|------|
| G1 | 事实错误 | 产品能力/定价/数据与 sparki.io 官方矛盾 |
| G2 | 死链 | 站内/站外链接 404 |
| G3 | 无来源数字 | 量化 claim 无 attribution |
| G4 | 竞品状态错误 | 竞品定价/定位/是否 AI 原生与官方矛盾 |
| G5 | 产品能力夸大 | 定位语言 ≠ sparki.io 已实现功能 |
| G6 | 内链指向未上线页面 | 只链 project-config §2 白名单 |
| G7 | 品牌/合规风险 | 贬低竞品、误导性标题、创作者关联暗示 |

---

## §1B Mode 系统

| Mode | 适用 | Phase 深度 |
|------|------|-----------|
| **lite** | Announcement、平台速讯 | 最小 Research + BLUF；不追求 Excellence |
| **standard** | WorkflowHowTo / FeatureGuide / AlternativeRoundup | 完整 Research 三角 + Extractability |
| **flagship** | CreatorClone / Comparison / CategoryPOV | 全流程 + Moat + Excellence **必须 Yes** |

默认：用户未指定 → **standard**。§2 路由表指定各类型默认 Mode。

---

## §2 文章类型路由

> **7 类路由表 + H2 模板 + Voice/Who/How/Why → `references/article-types.md`**
> Phase 0 加载路由表。Phase 3/4 加载模板。

### 路由速查

| 类型 | intent | 词数 | 产品上限 | 默认 Mode | category（frontmatter） |
|------|--------|------|:---:|:---:|------|
| **CreatorClone** | 红人风格拆解/教学 "How to Edit Like X" | 2200–3200 | ≤20%（教育向） | flagship | `Clone Edit Viral Videos` |
| **WorkflowHowTo** | 功能/流程实操 | 2000–2800 | ≤35% | standard | `Video Editing Features` / `ai-video-editor` |
| **FeatureGuide** | 生成器/工具指南 | 1800–2600 | ≤35% | standard | `Video Editing Features` |
| **Comparison** | 横向对比（含 Sparki） | 2500–3500 | ≤40% | flagship | `ai-video-editor` / `AI Tools` |
| **AlternativeRoundup** | 替代/榜单 | 2000–3000 | ≤30% | standard | `ai-video-editor` / `Editor-in-browser` |
| **CategoryPOV** | 品类观点/范式/科普 | 2000–3000 | ≤25% | flagship | `ai-video-editor` / `AI Video Editing` |
| **Announcement** | 产品/功能/内容发布 | 1200–1800 | 不限（产品叙事） | lite | `AI Video Editing` / `Video Editing Features` |

**路由规则**：`edit like {creator}` → CreatorClone；`how to + 功能/工作流` → WorkflowHowTo；`{feature} generator/guide` → FeatureGuide；`X vs Y` → Comparison；`best/alternative` → AlternativeRoundup；`can AI/paradigm/what is` → CategoryPOV；新品/更新 → Announcement。

**信息增量**：相对 SERP Top3 须 **≥2 项** 独有增量（原创框架 / 决策表 / 一手工作流 / 素材级观察）。

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
Phase 5  ─ SelfCheck & Gate C（H0–H4 + 12 维）
    ↓ PASS / ❌ → §3.G 回溯
Phase 5.5─ Cross-Article Audit（同批 ≥2 篇强制）
Phase 6  ─ Delivery
```

---

### Phase 0 — Intake & Gate A

> **Investment Score → `references/portable/investment-score.md`**
> **Gate 细则 → `references/gates.md`**

**Phase 0 首行强制输出**：

```
## Mode: lite | standard | flagship
## ArticleType: CreatorClone | WorkflowHowTo | FeatureGuide | Comparison | AlternativeRoundup | CategoryPOV | Announcement
## InvestmentScore: {1.0–5.0} — {五因子摘要}
## Category (frontmatter): {见 §2}
## Author: Sparki Team
## Gate A: KEEP | MERGE → {slug} | STOP
```

#### 六必问（信息不足时先问用户）

| # | 问题 |
|---|------|
| 1 | 目标 SEO 关键词 + 受众？ |
| 2 | 发布目的（SEO / 品牌 / 转化）？ |
| 3 | 与既有 61 篇 / 竞品内容的竞争关系（2–3 个 URL）？ |
| 4 | 文中内链的站内页面是否已上线（见 project-config §2 白名单）？ |
| 5 | 文章类型（未给 → Agent 按 §2 推断）？ |
| 6 | CreatorClone：具体红人 + 公开素材 URL（≥2 个视频/频道）？ |

用户只给 topic 时：Agent 自行 R2 SERP Top3；竞品 URL 缺失 → Log 标注 `competitor:TBD`；必问无法推断 → **AskUserQuestion**。

#### Investment Score

五因子各 1–5，取算术平均：

| 因子 | 1 分 | 5 分 |
|------|------|------|
| 搜索需求 | 几乎无搜索量 | 稳定或上升 |
| 商业相关性 | 与 ICP/产品路径无关 | 靠近购买或使用路径 |
| 差异化能力 | 只能复述 SERP | 有 Moat / 一手观察可引用 |
| 证据可得性 | 无法验证强 claim | R3 可支撑（红人文=素材可抓） |
| 内容生命周期 | <3 月过时 | 2+ 年常青 |

| 均分 | 动作 |
|------|------|
| **≥4.0** | KEEP，按声明 Mode 执行 |
| **3.0–3.9** | KEEP 但**降级 Mode** 或改角度 |
| **<3.0** | MERGE / STOP / 降级短帖 |

#### KEEP / MERGE 判定

三条件满足**任意两个** → KEEP（对照 `content-graph.md` §主题簇）：

| 条件 | 判断方法 |
|------|---------|
| 搜索意图独立 | 与既有 61 篇 primary keyword 搜索池重叠 <50% |
| 读者阶段不同 | Awareness / Consideration / Evaluation / Activation 不重叠 |
| 内容深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

**Gate A 阻断**：MERGE / STOP / Investment <3.0 / 必问缺失无法推断 → STOP。

---

### Phase 0R — Research 三角 & Gate 0R

> **完整流程 → `references/portable/research-triangle.md`**
> **SERP Fit → `references/portable/serp-fit-template.md`**

```
R1 — 读 project-config + product-competitors + content-graph
    ↓
R2 — WebSearch（primary keyword → SERP Top 5 + PAA）
    ↓
R3 — Fetch（官方页 sparki.io/features 相关 + SERP Top 3–5；
         CreatorClone：必抓红人公开视频页/频道 ≥2）
    ↓
Synthesis Statement + Information Gain（≥2 项）
    ↓
Research Log + SERP Fit → Gate 0R Pass → Phase 1
```

**Mode 差异**：lite 可简版 R2/R3；flagship 须完整 R3 + ≥2 Candidate Examples（CreatorClone = 素材级切点/转场/字幕观察）。

**Degraded**（WebSearch/Fetch 不可用）：标注 `Research mode: Degraded`；CreatorClone 无素材验证 → 不写具体切点断言；政策/定价 P0 claim 不得写未验证数字。

---

### Phase 1 — Article Brief

> **模板 + 范例 → `references/mini-example.md` · `references/article-types.md`**

Brief 必含：Mode · ArticleType · InvestmentScore · SuccessMetric · MoatAssetPlanned · AnswerBlocks · Working title · Primary keyword · Category · Synthesis Statement · Information increment（≥2 项）· Candidate examples · Word count target · Internal link plan · Slug candidate · Author（Sparki Team）。

---

### Phase 2 — Slug、Date & Gate B

> **Slug 规则 → `references/slug-gate.md`**
> **Gate B 细则 → `references/gates.md`**

1. Slug 候选 = `{slug}.md` 文件名（**不含 `/blog/`、不含 NN**）；文件名必须 = frontmatter `slug`
2. Gate B：6 问 + 12 反模式零触发
3. `date`：目标发布日（UTC），避开 `content-graph.md` 日期占用表；每自然日 ≤1 篇
4. title 45–60 / description 120–160（validate 范围 80–320）
5. 复核 Phase 0R SERP Fit

---

### Phase 3 — Outline

> **H2 模板 → `references/article-types.md`**
> **内链规划 → `references/internal-links.md`**

按类型 H2 模板；每节标注目标词数、Reader mental state、内链占位、Answer block ID。

---

### Phase 3.5 — Outline 交叉检查（Draft 前）

**触发**：同批规划或并行创作 **≥2 篇**（同 creator 双篇、同 cluster、或同功能）。**详见** `references/portable/outline-cross-check.md`。单篇标注 `N/A — single article`。

检查 H2 重复、Synthesis 冲突、Spoke 是否回链 hub、同一 creator 双篇角度是否雷同。

---

### Phase 4 — Draft

> **加载顺序**（≤2 文件/轮）：
> 1. `references/article-types.md`（Voice 与 H2 模板）
> 2. `references/writing-constraints.md`（Voice + 引用分级 + 段落优先协议 + 漏斗）
> 3. `references/product-competitors.md`（产品事实 + 竞品对照）

flagship 额外 → `references/portable/extractability-checklist.md`

**核心约束**：先 prose 后结构 · 禁伪列表 · 长段 ≥3 · 列表占比 ≤ 类型上限 · CTA ≤2 · 站内非 blog 页面一律绝对 URL · 无 `## Related articles`

**BLUF 三处**：TL;DR 长描述 + bullets · 每 major H2 首段先答 · FAQ 首句即答

---

### Phase 5 — SelfCheck & Gate C

> **完整 12 维 + H0–H4 → `references/selfcheck.md`**
> **Gate 细则 → `references/gates.md`**

#### 工具先跑（对部署仓成稿执行）

```bash
python skills/sparki-blog-article/tools/frontmatter_validator.py "E:\客户部署项目\sparki-blog\content\blog\{slug}.md" --keyword "{primary keyword}"
python skills/sparki-blog-article/tools/word_count_narrative.py "E:\客户部署项目\sparki-blog\content\blog\{slug}.md" --intent {creator|workflow|feature|comparison|alternative|pov|announcement}
python skills/sparki-blog-article/tools/link_checker.py "E:\客户部署项目\sparki-blog\content\blog\{slug}.md" --forbidden "/features/not-live,/pricing-beta"
# 部署仓强校验（slug=文件名、category/author 必填、description 80–320）：
cd E:\客户部署项目\sparki-blog && npm run validate:posts
```

**Gate C**：H0–H4 + 12 维全 Pass → **audit-ready**。终审 → `references/portable/final-audit.md`。

---

### Phase 5.5 — Cross-Article Audit

同批 ≥2 篇：叙事雷同 · 互链完整性 · Intro/Conclusion 互换测试 · 与 61 篇既有 slug 无混淆。

---

### Phase 6 — Delivery

1. 写入 `E:\客户部署项目\sparki-blog\content\blog\{slug}.md`（`draft: true` 起步；终审通过后改 `false`）
2. Article Brief 最终版 + SelfCheck 表 + Source Map + SERP Fit + Internal Link Plan
3. **终审指令**：

```
按 sparki-blog-article references/portable/final-audit.md 执行发布前终审：
- 文件：E:\客户部署项目\sparki-blog\content\blog\{slug}.md
- 项目：sparki.io / Sparki
- 类型：{ArticleType}
- 主关键词：{primary keyword}
```

4. 提示人类：在部署仓 `npm run validate:posts` → build → 上线；更新 `content-graph.md` 登记表。

---

### §3.G Gate 回溯表

| Fail 于 | 回退至 | 动作 |
|---------|--------|------|
| Gate A / Investment | Phase 0 | 改角度 / MERGE / STOP |
| Gate 0R | Phase 0R | 补 R2/R3 / 降 Degraded claim |
| Gate B | Phase 2 | 重选 slug |
| Gate C — H3 | Phase 4 | 扩写至类型下限 |
| Gate C — G1/G3/G7 | Phase 4 | 改事实/合规表述 |
| Gate C — 12 维 | Phase 4 | 按维度修复 |
| Phase 3.5 / 5.5 | Phase 3 / 4 | 改 Outline 或正文差异 |

---

## §4 Reference 索引（均在 skill 文件夹内）

| 文件 | 加载时机 |
|------|----------|
| `references/project-config.md` | Phase 0, 5 |
| `references/article-types.md` | Phase 0, 2, 3, 4 |
| `references/content-graph.md` | Phase 0, 2, 3.5, 5.5 |
| `references/internal-links.md` | Phase 3, 3.5, 5 |
| `references/slug-gate.md` | Phase 2 |
| `references/product-competitors.md` | Phase 0R, 4, 5 |
| `references/writing-constraints.md` | Phase 4 |
| `references/gates.md` | Phase 0, 1, 2, 5 |
| `references/selfcheck.md` | Phase 5 |
| `references/mini-example.md` | Phase 1, 3 |
| `references/portable/*` | 按 Phase 指针 |
| `tools/` | Phase 5 |

---

## §5 Gotchas（sparki 高发）

**结构与命名**：文件名 = slug，**无 NN 前缀** · 禁年份/`ultimate`/`guide` 后缀 · CreatorClone 标题勿虚构 "official"

**链接**：站内 `/features/*`、`/creators/*` 等一律 `https://sparki.io/...` **绝对 URL**（Rewrite 只透传 `/blog/*`）· blog 互链 `/blog/{slug}` 相对 · 禁链未上线页面（G6）

**红人合规（CreatorClone）**：只描述公开素材中可验证的剪辑手法，不臆测创作意图 · 禁暗示代言/合作/affiliate · 素材引用于正文注明出处

**品牌与事实**：Sparki 非 "Sparksview"（contact 邮箱域名，勿混）· 无来源数字（G3）· pricing 加 "as of" · FeatureGuide 不写未上线能力（G5）

**流程**：Gate 未 Pass 不交付 · 渐进式加载 · 不读 skill 文件夹外文档

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.0.0** | 2026-09-04 | 首版：从 luciusai-blog-article v2.0 模板移植并全面定制为 Sparki（OpenBlog 部署仓 slug 命名、7 类路由含 CreatorClone、绝对 URL 站外规则、61 篇 content-graph 基线、category 枚举） |

---

*sparki-blog-article · v1.0.0 · 2026-09-04 · self-contained · US creators*
