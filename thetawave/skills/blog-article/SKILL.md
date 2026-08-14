---
name: thetawave-blog-article
description: Create English ThetaWave blog articles (thetawave.ai/blog) from brief to draft. Fully self-contained skill folder; final audit via references/portable/final-audit.md.
metadata:
  version: 2.2.3
  project: thetawave.ai
  locale: en
  self-contained: true
  complements: thetawave-meta-title-description
  components_spec: ../archive/thetawave-blog-components-spec.md
---

# ThetaWave Blog Article Creation

为 **https://thetawave.ai/blog/** 从选题到英文成稿。**Frontmatter 与正文模块以本 Skill §2 为准**（v2.2.3 起：`## Key takeaways` = TL;DR（正文第一块）→ `## Introduction`（开篇 H2）→ 正文 H2；含 `category`；FAQ 仅正文；YAML 不含 `keywords` / `faq` / `final_cta` / `related` / Disclosure 段）。作者页见 `/blog/author/{slug}`。发布前终审用 `references/portable/final-audit.md`。

**范围**：仅英文 `blog/`（`/blog/{slug}`）。**不含** `blog-kr/`、`localization/`。

**本文件自包含**：项目配置、G1–G7 阻断规则、双核心词、内容图谱、五类文章模板、引用分级、碎片化防护、漏斗透明度、7 Phase 工作流、12 维扩展创作自检、Mini Example 均内联。

---

## §0 如何使用

### 触发语

```
按 thetawave-blog-article skill，为关键词 "{primary keyword}" 创建一篇 {Commercial|Alternative|StudyMethodHub|StudyMethodSpoke|HowTo} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
```

批量示例：

```
按 thetawave-blog-article skill，为关键词 "NotebookLM alternative for students" 创建一篇 Alternative 文章。
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主题 / 主关键词 | ✅ | 决定 intent 与 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| 双核心词 lane | 推荐 | NoteTaker / NotesGenerator / Both（Phase 0 第五问） |
| 竞品参考 URL | 推荐 | Phase 0 信息增量判断 |

### 输出（Phase 7 交付物）

1. **Article Brief**（Markdown 摘要）
2. **完整稿** `thetawave/blog/NN-{slug}-2026.md`（NN = §4 下一序号，当前为 **15**）
3. **SelfCheck 表**（§3 Phase 6，Pass/Fail + 详细 Notes）
4. **templates 审核指令**（复制即用，§3 Phase 7）
5. **提示人类**更新 `blog/readme.md` 文件表（§7）

### Agent 执行顺序

```
§2 类型路由 → §3 Phase 0–7 顺序执行 → 缺信息时先问 Phase 0 五必问
```

与用户沟通策略说明可用中文；**正文必须为英文**（上线稿）。

---

## §1 项目配置与 G1–G7 阻断规则

### 1.1 项目配置

| 配置项 | ThetaWave 值 |
|--------|-------------|
| **品牌/产品名** | ThetaWave（正文与 frontmatter 统一 **ThetaWave**；域名 thetawave.ai 小写） |
| **主域名** | thetawave.ai |
| **博客路径前缀** | `/blog/` |
| **作者** | `Kostja` 或 `Thetawave Team`；**必填** `author_slug`: `kostja` \| `thetawave-team` |
| **Primary ICP** | college students（本科生、研究生） |
| **Secondary ICP** | 高中生、自学者 |
| **双核心词 A** | **AI note taker** — capture, record, transcribe（实时讲座） |
| **双核心词 B** | **AI notes generator** — generate, create, turn into（素材→笔记） |
| **品类 one-liner** | AI-powered note-taking platform for college students: real-time lecture capture → formatted notes, mind maps, quizzes, flashcards, podcasts |
| **Hero 叙事** | Learn 10x faster · Turn what you hate to learn into formats you'll enjoy |
| **定价** | 免费试用；Pro **$118.80/年**（约 $9.90/月）；学生首年 30% off → $83.16；**无月付**；7 天退款 |
| **Proof（可写）** | 300,000+ registered students；100,000+ MAU（2026-01）；TLS 1.3 传输加密；App Store 4.2★ |
| **Proof（禁写）** | SOC 2（待官方核实）、端到端加密、未验证 ARR/增长率当作硬数据 |
| **「10x faster」** | 方向性品牌表述，**不可**写成实验结论或保证 |
| **CTA 主链** | `https://thetawave.ai/auth/signup` |
| **Chrome Extension** | [Thetawave Quick Notes](https://chromewebstore.google.com/detail/thetawave-quick-notes/eihlofmfpienfpoldbfbdjbilfccgcjg) |
| **移动端** | [App Store](https://apps.apple.com/app/id6744060956) · [Google Play](https://play.google.com/store/apps/details?id=ai.thetawave.app) |
| **禁止内链** | 404 或 forthcoming 的 Use Case / 功能页 |

### 1.2 G1–G7 一票否决阻断规则

以下 7 项为发布前硬性阻断——**任一项触发则文章不得发布**，修复后重新过 Gate。Phase 6 SelfCheck 首维即逐项对照此表。

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、状态、数据与官方文档/官网矛盾 | 逐 claim 对照 §6.1 产品事实表。功能不在当前版本 → 不能声称"已发布"。 |
| **G2** | 死链 | 站内或站外链接 404/域名拼写错误 | 逐个检查所有内链是否可达（feature 页 + blog 互链）。外链可有 1–2 失效（外部不可控），但不能全挂。 |
| **G3** | 无来源数字 | 量化 claim（"15%→60%"、"30min→3min"）无 attribution | 每个数字必须可追溯到原始来源或标注内部数据基础（"based on internal analysis, n≈X"）。单案例不能写成复数趋势。 |
| **G4** | 竞品状态错误 | GA/Beta/Preview/Archived/被收购 与官方公告矛盾 | 打开竞品官网/docs 验证。特别注意：已 Archive 项目标为 "active competitor"。 |
| **G5** | 产品能力夸大 | 自有产品能力超出当前 GA 版本或已文档化 roadmap | 检查产品 docs / product page。定位语言（"designed to"、"aims to"）≠ 已实现功能。 |
| **G6** | 内链指向未上线页面 | 链到项目配置中 "禁止内链" 列表或未发布的路径 | 对照 §1.1 的「禁止内链」和 §6.2 十页白名单——只链白名单内路径。 |
| **G7** | 重大品牌风险 | 内容可能引发法律/合规/竞品纠纷 | 贬低性措辞（"just a prompt file"、"merely a chat window"）在技术社区可能被竞品用户放大为纠纷。 |

**G6 补充**：forthcoming 内链上限 ≤1 个，且仅限正文脚注。正文不得链未上线页。

**禁止**：`## Related Reading`、frontmatter `related` / `keywords` / `faq` / `final_cta` / `faq_subtitle`、文首 **Disclosure** 段。FAQ 只写在正文 `## Frequently Asked Questions`。内链见 §6.4。

### 1.3 双核心词 → 落地页（创作内链必查）

| 用户意图 | 动作词 | 主链目标 |
|---------|--------|---------|
| **Note Taker** | capture, record, transcribe, live lecture | `https://thetawave.ai/` 或 `/feature/lecture-to-notes` |
| **Notes Generator** | generate, create, turn into, upload | `https://thetawave.ai/feature/notes-generator` |

**策略**：Heavy semester 通常需 **Both**；Comparison 文按 input 类型分节链向对应 feature。

### 1.4 可链接 URL 白名单

| 类型 | 路径 |
|------|------|
| 博客 | `/blog/{slug}` — 见 §4 |
| 功能页 | `/feature/{slug}` — 见 §6 十页清单 |
| 转化 | `/auth/signup` |
| 对比页 | `/thetawave-vs-chatgpt`（若已上线） |
| Use Cases | `/use-case/for-{audience}` — **仅已上线页** |
| Study 页 | `/study/{slug}` — 按需，勿与 blog 抢同一 P1 |

**G6 规则**：不链未上线页；forthcoming ≤1 且仅正文脚注。

---

## §2 文章类型路由

收到任务后**先匹配类型**，再跳转对应 H2 模板。

### 2.1 路由表

| 类型 | 典型 intent | 词数 | 产品提及上限 | templates category | 参考 slug |
|------|------------|------|-------------|-------------------|-----------|
| **Commercial Roundup** | best X / tool selection | 2500–3500 | ≤45% | Comparison | `best-ai-note-takers` |
| **Alternative / VS** | X alternative(s) | 2000–3000 | ≤50% | Comparison | `quizlet-alternatives`, `chatgpt-alternatives` |
| **Study Method Hub** | compare N methods | 2500–3200 | ≤25% | Research | `study-methods-compared` |
| **Study Method Spoke** | single method deep dive | 1800–2500 | ≤30% | Research / Glossary | `cornell-note-taking-method`, `feynman-technique` |
| **How-To** | how to X | 2000–2800 | ≤35% | Product | `how-to-take-notes-in-college`, `how-to-study-for-finals` |

**路由规则**：

- `best` + 品类/工具 → **Commercial Roundup**
- `{competitor} alternative(s)` / `vs` + 单竞品 → **Alternative**
- 学习方法名 / technique / system / method → **Study Method Spoke**
- N 种方法对比 / at a glance 表 → **Study Method Hub**
- `how to` + 学生场景 → **How-To**

**templates category 映射**：以上 5 类在交付 templates 审核时对应 Comparison（Commercial + Alternative）、Research（Study Hub + most Spokes）、Product（How-To + some Spokes）、Glossary（short Spokes）。Brief 阶段填入以备用。

### 2.2 全类型通用模块

| 模块 | 要求 |
|------|------|
| **Key takeaways** | **= TL;DR**；`## Key takeaways` 为正文**第一块**（frontmatter 之后）；3–6 bullet；独立传达 ~80% 价值 |
| **Introduction** | **必填** `## Introduction`；Key takeaways 之后、第一个正文主题 H2 之前；≤200 words；BLUF（直接答 primary intent）+ 路线图（全文覆盖什么）；Introduction **首段** ≥1 内链 |
| **H1** | **禁止** Markdown `# H1` 重复 frontmatter `title`（页面 title 由 CMS 渲染）；开篇一律用 `## Introduction` |
| **H2** | 英文 `##` 标题；Study Method 可用描述性标题（非强制编号） |
| **FAQ** | **固定 6 题**（2026-08-11 定标）；正文 `## Frequently Asked Questions` + `###` 小题；**不写** frontmatter `faq`；**全部内容相关**（基于本文主题，禁止通用模板题）；≥1 覆盖边界/异议 |
| **内链** | Introduction 首段 ≥1；body blog 1–4；feature 0–2；**上下文分布** |
| **外链** | 权威 2–8；竞品 `rel="nofollow noopener"` |
| **列表比例** | Commercial/Alternative ≤30%；Study Method ≤25%；How-To ≤35% |
| **长段落** | ≥3 段 4–8 句（80–200 words）；避免连续 3+ 短段簇 |
| **CTA** | signup 或 feature 分散在不同 H2，各 ≤1 次；**不写**文末独立 FinalCTA 区块或 Conclusion 后单行 signup |
| **category** | frontmatter 必填：`Research` \| `Comparison` \| `Product` \| `Reference`（见 §2.9 路由） |

### 2.3 Commercial Roundup — H2 模板

**叙事弧线**：input-first 分类 → 评估标准 → 分工具 trade-off → 不导向单一产品。

```
## Key takeaways                       ← 正文第一块（TL;DR）
## Introduction                        ← BLUF + 路线图；首段 ≥1 内链
## A practical taxonomy: … by primary use case   ← 本篇独有框架 + 路由表
## What makes a great … (evaluation criteria)
## Why "best" depends on … (not hype)
## Top … (2026)                         ← 分 H3 每工具 trade-off
## Comparison table                     ← 表前后有分析段
## Frequently Asked Questions
```

**ThetaWave 出现**：分 input/output 场景写适用条件，非「唯一最佳」。

### 2.4 Alternative — H2 模板

**叙事弧线**：为何搜索 alternative → 竞品是什么 → 公平对比 → 按场景推荐。

```
## Key takeaways
## Introduction
## What {Competitor} is (and why people search alternatives)
## Comparison table (quick routing)
## {Tool N} — when it fits              ← 每竞品 ≥1 优势 + 限制
## Frequently Asked Questions
```

**竞品外链**：HTML `<a href="..." rel="nofollow noopener">`。

### 2.5 Study Method Hub — H2 模板

**叙事弧线**：为何方法比时长重要 → 全景表 → 各法简述 + 链 spoke → 组合建议。

```
## Key takeaways
## Introduction
## The N Methods at a Glance            ← 对比表（Type / Mechanism / Best For）
## Method 1: {Name}                    ← 简述 + link /blog/{spoke-slug}
## Method 2: …
…
## Which Methods Work Together
## Frequently Asked Questions
```

**禁止**：在 hub 完整展开各法（>800 词/法 → 应独立 spoke）。

### 2.6 Study Method Spoke — H2 模板

**叙事弧线**：定义 → 格式/步骤 → 科学/历史 → 适用边界 → **AI connection**（后半）。

```
## Key takeaways
## Introduction
## What Is the {Method}?
## The {Method} Format / How It Works
## Why {Method} Works — The Science Behind …
## How to … — Step by Step
## When to Use / When Not to
## Common Mistakes
## AI connection                         ← 必须；链 §6 feature 映射
## Frequently Asked Questions
```

**AI connection 规则**：

- 放在方法教学完成之后，**不**每段推产品
- 1 段：该方法 + 对应 ThetaWave feature 如何减少 manual 步骤
- 链 1 个最相关 `/feature/*`（见 §6.3 映射表）
- 可选第二链 signup 或 notes-generator

### 2.7 How-To — H2 模板

```
## Key takeaways
## Introduction
## Why {Topic} Matters More Than …
## Step 1–N: …                         ← 编号或描述性 H2/H3
## Tools and Workflows for …
## Common Mistakes
## Frequently Asked Questions
```

### 2.8 Slug、Title、Description（自包含规则）

| 项 | 规则 |
|----|------|
| **slug** | kebab-case；**不含年份**；常青 URL → `/blog/{slug}`；5–8 词，≤60 字符；不含内部架构词（framework/strategy/diagnosis/guide/complete） |
| **title** | editorial；how-to / guide / roundup / best；可含 `(2026)`；45–65 字符；**通常不加** `| Thetawave` |
| **description** | 150–160 chars；读者得到什么 + 主关键词；轻 CTA 可用「Free tools included」 |

**Title 公式示例**：

- Commercial：`Best {Category} in 2026: {Differentiator}`
- Alternative：`Best {Competitor} Alternatives in 2026: {Hook}`
- Study Method：`{Method Name} — Complete Guide with Templates (2026)`
- How-To：`How to {Action} in College (2026)`

**Slug 反模式速查（创作阶段必检）**：

| 反模式 | 错误示例 | 正确示例 |
|--------|---------|---------|
| 含年份 | `best-ai-note-takers-2026` | `best-ai-note-takers` |
| 含数量 | `top-5-study-methods` | `study-methods-compared` |
| 连续重复词 | `note-taking-app-app-store` | `note-taking-app-store` |
| 内部架构词泄漏 | `tiktok-shop-hooks-framework` | `tiktok-video-hooks` |
| 分类前缀沉积 | 七篇全以 `tiktok-shop-` 开头 | 各篇以搜索词开头 |

**Slug "大声读"测试**：去掉连字符大声读出来 → 通顺 → 通过；不通顺或含重复词 → 改。

### 2.9 Frontmatter Schema

```yaml
---
title: "Editorial Title (2026)"
description: "150–160 chars, benefit + main intent keyword for SERP"
slug: "kebab-case-no-year"
date: 2026-XX-XX          # 发布时间（首次发布，永不改变）
updated: 2026-XX-XX       # 可选；最近一次实质性内容更新；无更新则省略
author: "Kostja"
author_slug: "kostja"          # 推荐；与 /blog/author/{slug} 一致
image: "/blog/images/{slug}-2026.jpg"
category: "Research"           # Research | Comparison | Product | Reference
---
```

**必填**：`title`、`description`、`slug`、`date`、`author`、`image`、`category`。  
**推荐**：`author_slug`；`updated`（可选，最近一次**实质性**内容更新，仅实质变更时更新——新增数据/章节/修正事实；错别字、样式调整不更新）。  
**禁止**：`keywords`、`related`、`faq`、`final_cta`、`faq_subtitle`。

> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅实质更新时更新。页面**只显示一个日期**（有 `updated` 显示它）——**勿同时显示**两个日期（实证会导致 CTR 下跌）。JSON-LD 中保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致（无则用 `date`）。

#### category 路由（文章类型 → frontmatter）

| 文章类型 | `category` |
|---------|------------|
| Commercial Roundup | **Comparison** |
| Alternative / VS | **Comparison** |
| Study Method Hub | **Research** |
| Study Method Spoke | **Research** |
| How-To | **Product** |
| 纯参考/数据页（少见） | **Reference** |

Phase 0 确认 `category`；与 §2.1 类型不一致时以类型路由为准。

---

## §3 创作工作流（7 Phase）

### Phase 0 — Intake（五必问）

| # | 问题 | 用途 |
|---|------|------|
| 1 | 目标 SEO 关键词 + search intent？ | 类型路由 |
| 2 | 目标受众 + 课程类型（STEM/文科/考试）？ | 深度与例子 |
| 3 | 发布目的？SEO / 品牌 / 转化 | 产品提及容忍度 |
| 4 | 同主题竞品内容 2–3 链接？ | 信息增量 |
| 5 | **Core keyword lane**：NoteTaker / NotesGenerator / Both？ | 主链 feature 页 |

**额外可选问题**：是否链特定 Use Case；pricing 是否需在文中提及。

---

### Phase 1 — 独立成文 Gate

**三条件满足 ≥2 → KEEP**；否则 **MERGE**，停止创作。

| 条件 | 判断 |
|------|------|
| 搜索意图独立 | 与 §4 已有文关键词重叠 ≤50% |
| 读者阶段不同 | 选型 vs 学法 vs 操作指南 |
| 深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

**Study Method 特规**：单法 spoke 若 hub 已完整展开该法 → MERGE 到 hub 或加强 spoke 深度角度。

**关键词冲突快查**：

| slug | 主关键词 | 边界 |
|------|---------|------|
| `best-ai-note-takers` | best AI note takers | Commercial hub |
| `quizlet-alternatives` | Quizlet alternatives | Flashcard 替代；链 hub |
| `chatgpt-alternatives` | ChatGPT alternatives | 通用 AI 替代；非 note-specific |
| `study-methods-compared` | study methods compared | 8 法 hub；不重复 spoke 深度 |
| `cornell-note-taking-method` | Cornell note taking method | 单法 canonical |
| `mind-mapping-method` | mind mapping method | 单法 canonical |
| `zettelkasten-method` | Zettelkasten method | 单法 canonical |
| `feynman-technique` | Feynman technique | 单法 canonical |
| `sq3r-method` | SQ3R method | 单法 canonical |
| `leitner-system` | Leitner system | 单法 canonical |
| `how-to-take-notes-in-college` | how to take notes in college | How-To hub；不重复单法 |
| `how-to-study-for-finals` | how to study for finals | How-To hub；不重复单法 |

**NotebookLM alternative 示例**：KEEP — intent 为 document/audio study tool，与 chatgpt-alternatives（通用 AI）和 best-ai-note-takers（broad roundup）均不同。

---

### Phase 2 — Article Brief

```markdown
## Article Brief

**Working title**:
**Primary keyword**:
**Article type**: Commercial / Alternative / StudyMethodHub / StudyMethodSpoke / HowTo
**Templates category**: Comparison / Research / Product / Glossary
**Core keyword lane**: NoteTaker | NotesGenerator | Both
**Reader stage**: Awareness / Consideration / Evaluation
**Target audience**:
**Word count target**:
**Cluster role**: Commercial hub / Study hub / Study spoke / How-to / Standalone
**Differentiation angle** (vs SERP top 3):
**Competitor gap**:
**Canonical concepts to reference** (link only, do not redefine):
**Primary feature link(s)**:
**KEEP/MERGE**: KEEP | MERGE → {target slug}
**Category** (frontmatter): Research | Comparison | Product | Reference
```

---

### Phase 3 — Slug + SERP + Frontmatter

1. 2–3 slug 候选 + 推荐（§2.8；检查反模式表 + "大声读"测试）
2. title + description（计字符）
3. 完整 frontmatter YAML（含 `category` + 推荐 `author_slug`；禁止 §2.9 所列字段）
4. **SERP Fit mini-audit**：

```markdown
## SERP Fit
Primary keyword:
Search intent: [ ] Informational  [ ] Commercial  [ ] Transactional  [ ] Navigational
Top 3–5 ranking pages:
Common coverage:
What they miss:
Our unique contribution:
```
→ 进入 Phase 4 — Outline

---

### Phase 4 — Outline

用 §2.3–2.7 对应模板；每节标注目标词数、内链占位、feature 链（Study spoke 必含 AI connection）。

```markdown
## Outline — {slug}

| § | H2 | Target words | Links / Notes |
|---|-----|-------------|---------------|
| Key takeaways | … | 120 | primary keyword |
| Introduction | … | 150 | link: /blog/... or /feature/... |
...
**Estimated total**: N words
```

---

### Phase 5 — Draft 写作约束

#### 5.1 Voice（§8 摘要）

- Clear, student-friendly, evidence-led
- Wirecutter-style fair comparisons
- Category-building before product pitch
- 禁 revolutionary / game-changing / unlock / seamless / magic / best-in-class / only solution
- 禁虚构 lecture 场景开头（"Imagine you're in class…"）

#### 5.2 事实、合规与引用分级

##### 引用分级（P0/P1/P2）

| 级别 | 触发条件 | 要求 | 示例 |
|------|---------|------|------|
| **P0 — 必须引用链接** | 任何可在外部数据源验证的量化声明 | 链接到原始来源（官方报告、官方文档、一手数据页）。同一数字跨篇出现时每篇都要链。 | "$15.8B GMV"、"73% creators <$50/mo" |
| **P1 — 应当引用** | 行业趋势、产品能力描述、竞品状态 | 链接到官方 docs / GitHub / Changelog / 行业报告。如无法链接则加限定词（"based on"、"typically"）。 | "TikTok Shop affiliate 归因窗口 typically 7 days" |
| **P2 — 可不引用** | 作者自己测试/观察得出的 benchmark、原创框架、从已引用数据衍生的分析 | 注明方法论基础或标注 "internal observation, n=X"。框架性结论（如"三个心理机制"）是原创分析，不需要 citation。 | "CTR >3% good (based on internal analysis, n≈200)" |

##### 内部数据声明标准格式

当引用 ThetaWave 内部数据（如 300,000+ registered students）或团队观察时，格式为：

> Based on internal analysis of [N] [data type] across [time period], [finding].

示例：
- "Based on internal analysis of ~200 top-performing student workflows across STEM and humanities courses in Q1 2026, students using AI-formatted notes scored 23% higher on recall tests."
- 禁止裸数字 "300,000+ students use ThetaWave" → 应有来源标注或时间窗口

##### 事实与合规速查

| 规则 | 执行 |
|------|------|
| 量化 claim | P0 级：`[Source: URL]` 链接；P1 级：链接或限定词 |
| 定价 | $118.80/年；内链到 signup 页或在脚注标注 "pricing as of [date] — verify at thetawave.ai/pricing" |
| 竞品 | 每竞品 ≥1 优势；基于官网（非二手博客）；无贬低性措辞 |
| 10x faster | directional，非 guarantee |
| 无 SOC 2 / E2E encryption claim |
| 政策/准入门槛 | 有时效标注 "as of [date]"（如涉及 pricing / scholarships / app store ratings） |
| 行业趋势 ("studies show") | 替换为具体引用或删除 |

#### 5.3 漏斗透明度自检

在正式起草前，检查叙事弧是否过于透明：

**检测方法**：提取文章的叙事弧——开头（教育/问题陈述）→ 中部（中立概述）→ 转折点（"but" / "however" / "this is where"）→ 产品作为答案。

| 文章类型 | 漏斗透明度接受标准 |
|---------|-------------------|
| **Commercial / Alternative** | 可接受透明漏斗——读者知道这是产品对比文 |
| **Study Method Spoke** | 漏斗应不可见。产品仅在 AI connection 出现（全文后 30%）。 |
| **Study Method Hub** | 漏斗应不可见。方法对比完成后可选提一句 AI 辅助。 |
| **How-To** | 工具在 workflow 节出现；不每段推产品 |

**自检问题**：如果读者在全文前 30% 就能识别这是 vendor blog → 漏斗过于明显，需重新平衡产品出现时机。

#### 5.4 碎片化防护规则（创作阶段必检）

AI 生成 blog 最常见的缺陷是碎片化——bullet point 堆砌 + 段落节奏单一。以下规则在起草阶段即强制执行：

##### 段落节奏

| 检查项 | 健康标准 | 红线 |
|--------|---------|------|
| 长段落（≥4 句，80–200 词） | ≥3 个 | 0 个 |
| 连续短段落（≤2 句） | ≤2 个连续 | ≥4 个连续 |
| 段落长度标准差（句数） | 能目测长短交替 | 全文所有段落长度几乎相同 |
| 每节叙事重量 | 每 H2 section 至少 1 个 ≥3 句段落 | 3+ 节全是短段落 |

##### 列表使用

| 检查项 | 标准 |
|--------|------|
| 每个列表前 | 必须有完整前导句说明列表目的 |
| 每个列表后 | ≥2 句分析（"这意味着什么？"） |
| 无单一项列表 | 1 个 bullet 是段落，不是列表 |
| 相邻 H2 section | 不连续出现 2 个 "H2 → 列表 → 无分析 → 下一 H2" 模式 |
| 列表项不超过 5 条 | 超过则考虑拆分为子标题 + 段落 |

##### 段间衔接

- 相邻段落之间至少有 1 种衔接手段：过渡词（"however"/"specifically"）/ 句子桥 / 关键词重复 / 指代词回指
- 目标：任意连续 10 段中 ≥7 对有衔接手段
- 避免 H2 后直接跟列表（H2 → 1–2 句过渡段 → 列表）

#### 5.5 内链（§6 硬性）

- Introduction 首段 ≥1 blog 或 feature
- Body blog 1–4
- signup + feature 分散，各 H2 ≤1
- 双核心词：capture 节链 lecture-to-notes；generate 节链 notes-generator
- 内链锚文本描述性（"our comparison of AI note-taking tools"），禁 "click here"、"learn more"

#### 5.6 竞品公平描述

| 规则 | 执行 |
|------|------|
| 每竞品 ≥1 明确优势（非敷衍） | 从 §6.5 竞品公平摘要表取优势 + 限制 |
| 禁贬低性措辞 | "just" / "merely" / "only does X" / "basically just" / "simplistic" |
| 对比表无二元化 | 不把需要 nuance 的能力简化为 "Yes/No"；如有简化需加脚注 |
| ≥1 场景推荐非 ThetaWave 方案 | 写在正文，非脚注 |

#### 5.7 模块顺序

```
YAML frontmatter（含 category；推荐 author_slug）
→ ## Key takeaways（TL;DR；正文第一块）
→ ## Introduction（开篇；首段 ≥1 内链）
→ 正文 H2（上下文内链）
→ ## How ThetaWave fits… / ## AI connection（按类型）
→ ## Common mistakes（推荐）
→ ## Frequently Asked Questions
```

---

### Phase 6 — 创作自检（12 维 Pass/Fail + Notes）

以下 12 维逐项自检。每项标注 Pass / Fail + 具体 Notes。Overall FAIL 则标注修复动作后重新过 Phase 6。

#### 1. Publishability G1–G7

| 检查项 | 对照 | Fail 条件 |
|--------|------|----------|
| G1 事实错误 | §1.2 G1 | 任何 claim 与 §6.1 产品事实表矛盾 |
| G2 死链 | §1.2 G2 | 内部链接 404；外链全挂 |
| G3 无来源数字 | §1.2 G3；§5.2 引用分级 | P0 级数字无链接或内部数据无 n= 标注 |
| G4 竞品状态错误 | §1.2 G4 | 竞品状态（GA/Beta/Archived）与官网矛盾 |
| G5 产品夸大 | §1.2 G5 | 定位语言当作已实现功能写 |
| G6 未上线内链 | §1.2 G6；§1.4 白名单 | 链接不在白名单；forthcoming >1 |
| G7 品牌风险 | §1.2 G7 | 贬低性措辞或可能引发纠纷的描述 |

#### 2. Fact/E-E-A-T

- [ ] 所有 P0 级量化 claim 有 `[Source: URL]` 或内部数据标注（"based on internal analysis, n=X"）
- [ ] 竞品描述基于官方资料（非二手博客）；pricing 有时效标注
- [ ] 每竞品 ≥1 优势；无贬低性措辞
- [ ] ≥1 场景推荐非 ThetaWave 方案（EEAT E6）
- [ ] 行业趋势引用具体来源；无 "studies show" 泛引
- [ ] 对比表无二元化简化；如有简化有脚注

#### 3. Differentiation

- [ ] 与 §4 已有文章 H2 标题重叠 <30%（即 ≤3.6 个 H2 重叠）
- [ ] 核心论点/框架在 SERP 前 3 竞品中找不到等效替代
- [ ] 独有框架/分类体系/对比维度至少 1 项
- [ ] Canonical Concept：引用方式为 1–2 句 + link（不重复完整定义）
- [ ] 本篇独有 takeaway 可用 1 句话概括

#### 4. Depth

- [ ] 叙事词数达 §2.1 类型阈值（排除 frontmatter / 表格 / FAQ 问答对）
- [ ] "表格+一句话然后跳到下一节"模式 ≤2 处
- [ ] FAQ 固定 6 题；≥1 题覆盖正文未涉及角度（非正文重排）
- [ ] ≥3 个分析性段落达 4–8 句（80–200 词）
- [ ] 标题承诺的核心问题在最深的一节给出了实现层面的解释（非仅定义）
- [ ] 每 500 词 ≥1 个具体例子/表格/框架/决策点

#### 5. Presentation & Rhythm

- [ ] 列表占比 ≤ §2.2 类型上限
- [ ] ≥3 个长段落（≥4 句）；连续短段落（≤2 句）≤2 个连续
- [ ] 每个列表有完整前导句；列表后有 ≥2 句分析段落
- [ ] 无连续 2 个 H2 section 各含列表而中间无分析段落（列表轰炸）
- [ ] 表格/媒体元素前后各有 ≥2 句分析段落
- [ ] 抽样连续 10 段，≥7 对有衔接手段（过渡词/句子桥/关键词重复）
- [ ] H2 后首段是引导段落，非直接列表或表格
- [ ] 段落长度有显著差异（非全文段落长度相同）

#### 6. Writing/Voice

- [ ] §8 正向 5 维全满足（Clear / Student-friendly / Evidence-led / Wirecutter-style / Category-building）
- [ ] 禁词（revolutionary / game-changing / unlock / seamless / magic / best-in-class / only solution）0 次命中
- [ ] 空泛句 ≤2 处（"In today's world…" / "Let's dive in…" / "It is important to note that…" / "Without further ado…" 等）
- [ ] 每 300–500 词出现 1 个具体对象（具名工具/数字/workflow/场景）
- [ ] 自有产品首次出现前，文章已提供独立价值
- [ ] 无虚构 lecture 场景开头

#### 7. Objectivity & Transparency

- [ ] 文章 type 对应漏斗接受标准（§5.3）；Compare/Alternative 文漏斗不透明但可接受
- [ ] 产品提及比例 ≤ §2.1 类型上限
- [ ] 竞品描述无贬低性措辞；定位语言与功能事实区分明确
- [ ] **无** 文首 Disclosure 段；**无** frontmatter `keywords` / `faq` / `final_cta` / `related` / `faq_subtitle`
- [ ] Study Spoke 文 AI connection 在全文后 30% 位置
- [ ] 署名真实（Kostja 或 Thetawave Team）；`author_slug` 与 `/blog/author/{slug}` 一致

#### 8. Structure/Links

- [ ] 必备模块完整：`## Key takeaways`（TL;DR，正文第一块）+ `## Introduction` + ## Frequently Asked Questions（≥3）；frontmatter 含 `category`
- [ ] **无** Markdown `# H1` 重复 frontmatter `title`
- [ ] **无** `## Related Reading`、**无** frontmatter `related` / `keywords` / `faq` / `final_cta` / `faq_subtitle`
- [ ] Introduction 首段 ≥1 blog 或 feature 内链；Body blog 1–4 互链；feature 0–2
- [ ] 内链锚文本描述性（无 "click here"）；内链用 Markdown，外链/竞品用 HTML nofollow
- [ ] Forthcoming ≤1（仅限正文脚注）
- [ ] 所有内链可访问（对照 §1.4 白名单 + §6.2 十页清单）

#### 9. SEO/SERP

- [ ] title 含 primary keyword（45–65 字符）
- [ ] description 120–160 字符；含 keyword + value prop；与正文首段一致
- [ ] frontmatter `category` 与 §2.9 路由一致
- [ ] FAQ 覆盖 Google People Also Ask 常见问题
- [ ] 有 snippet-ready 定义：40–60 词直接回答
- [ ] slug 常青、无年份/数量/内部架构词；通过"大声读"测试

#### 10. Conversion

- [ ] CTA 与读者阶段匹配（Awareness → 内链；Consideration → demo/signup；Activation → tutorial）
- [ ] signup + feature CTA 分散在不同 H2，全文 ≤2 次
- [ ] CTA 前已给足价值（读者主要疑问已回答）
- [ ] 无空泛 CTA（"Start your journey" / "Unlock your potential"）
- [ ] 无虚假承诺（"in just 15 minutes" 必须可达成）

#### 11. Slug & Evergreen Design

- [ ] 无年份（除非 §2.8 合法例外）
- [ ] 无数量/序数（top-5 / 7-ways）
- [ ] 无连续重复词（app-app / ai-ai）
- [ ] 无内部架构词（framework / strategy / diagnosis / guide / complete）
- [ ] 全小写 + 连字符（无下划线/大写/空格）
- [ ] ≤60 字符；人可读（"大声读"测试通过）
- [ ] 与 §2.8 反模式表对照：0 命中
- [ ] 30% 内容变化后 slug 仍然合适（语义余量原则）

#### 12. Thetawave-Specific

- [ ] Dual-core lane：NoteTaker 内容链 lecture-to-notes 或首页；NotesGenerator 内容链 notes-generator
- [ ] Study hub-spoke：spoke 未完整重定义 hub 表格内容（hub 中该法 ≤1 段概述）
- [ ] Canonical Concept Registry（§4.3）对照通过：每个引用概念用 canonical slug

**SelfCheck 输出格式**：

```markdown
## SelfCheck — {slug}
| Dimension | Pass/Fail | Notes |
|-----------|-----------|-------|
| 1. Publishability G1–G7 | Pass/Fail | Gx triggered: ... |
| 2. Fact/E-E-A-T | Pass/Fail | |
| 3. Differentiation | Pass/Fail | |
| 4. Depth | Pass/Fail | |
| 5. Presentation & Rhythm | Pass/Fail | |
| 6. Writing/Voice | Pass/Fail | |
| 7. Objectivity | Pass/Fail | |
| 8. Structure/Links | Pass/Fail | |
| 9. SEO/SERP | Pass/Fail | |
| 10. Conversion | Pass/Fail | |
| 11. Slug Design | Pass/Fail | |
| 12. Thetawave-Specific | Pass/Fail | |
**Overall**: PASS | FAIL → {具体修复动作}
```

12 维全部 Pass → 进入 Phase 7 交付。任一维度 Fail → 标注具体修复动作，修复后重新过 Phase 6。

---

### Phase 7 — 交付

1. 写入 `thetawave/blog/NN-{slug}-2026.md`
2. 输出 Article Brief 最终版
3. 输出 SelfCheck 表（12 维全 Pass）
4. **templates 审核指令**（复制即用）：

```
请按 references/portable/final-audit.md 审核 thetawave/blog/NN-{slug}-2026.md

项目配置：
- 品牌：ThetaWave
- 主域名：thetawave.ai
- 博客前缀：/blog/
- 作者：Kostja
- 受众：college students
- 双核心词：AI note taker + AI notes generator
- CTA：https://thetawave.ai/auth/signup

要求：
1. 先过 01-publishability.md：独立成文 + P0 Gate (G1–G7)
2. 按 A–J 十维评分（参考 02–10 维度文档）
3. 输出 Source Map + SERP Fit
4. 如有多篇文章，执行 12-cross-article-consistency.md 跨篇审计
5. 按 `references/portable/final-audit.md` §六 格式输出审核报告
```
5. 提示人类更新 `blog/readme.md`（§7）


---

## §4 已有内容图谱（en blog/）

### 4.1 文件表与下一序号

| NN | 文件 | slug | 类型 | 日期 | 主关键词 |
|----|------|------|------|------|---------|
| 01 | 01-best-ai-note-takers-2026.md | best-ai-note-takers | Commercial | 2026-04-16 | best AI note takers |
| 02 | 02-quizlet-alternatives-2026.md | quizlet-alternatives | Alternative | 2026-04-20 | Quizlet alternatives |
| 03 | 03-chatgpt-alternatives-2026.md | chatgpt-alternatives | Alternative | 2026-04-20 | ChatGPT alternatives |
| 04 | 04-cornell-note-taking-method-2026.md | cornell-note-taking-method | Study Spoke | 2026-05-18 | Cornell note taking method |
| 05 | 05-how-to-take-notes-in-college-2026.md | how-to-take-notes-in-college | How-To | 2026-05-18 | how to take notes in college |
| 06 | 06-how-to-study-for-finals-2026.md | how-to-study-for-finals | How-To | 2026-05-18 | how to study for finals |
| 07 | 07-study-methods-compared-2026.md | study-methods-compared | Study Hub | 2026-05-18 | study methods compared |
| 08 | 08-mind-mapping-method-2026.md | mind-mapping-method | Study Spoke | 2026-05-18 | mind mapping method |
| 09 | 09-zettelkasten-method-2026.md | zettelkasten-method | Study Spoke | 2026-05-18 | Zettelkasten method |
| 10 | 10-feynman-technique-2026.md | feynman-technique | Study Spoke | 2026-05-18 | Feynman technique |
| 11 | 11-sq3r-method-2026.md | sq3r-method | Study Spoke | 2026-05-18 | SQ3R method |
| 12 | 12-leitner-system-2026.md | leitner-system | Study Spoke | 2026-05-18 | Leitner system |
| 13 | 13-turn-notes-into-podcast-2026.md | turn-notes-into-podcast | How-To | 2026-06-16 | turn notes into podcast |
| 14 | 14-obsidian-notes-explained-2026.md | obsidian-notes-explained | How-To | 2026-07-28 | obsidian notes |

**下一序号：15**

### 4.2 主题簇结构

```
Commercial: 01 best-ai-note-takers ←→ 02 quizlet-alternatives ←→ 03 chatgpt-alternatives

Study Hub: 07 study-methods-compared
    ├── 04 cornell-note-taking-method
    ├── 08 mind-mapping-method
    ├── 09 zettelkasten-method
    ├── 10 feynman-technique
    ├── 11 sq3r-method
    └── 12 leitner-system

How-To: 05 how-to-take-notes-in-college · 06 how-to-study-for-finals
    └── 互链 Commercial + Study 簇
```

### 4.3 Canonical Concept Registry

| 概念 | Canonical slug | 引用方式 |
|------|---------------|---------|
| 8 学习方法全景 | study-methods-compared | 对比表 + 1 句 + link |
| Cornell 方法 | cornell-note-taking-method | 1–2 句 + link；不在他文逐步展开 |
| Mind Mapping | mind-mapping-method | 同上 |
| Zettelkasten | zettelkasten-method | 同上 |
| Feynman Technique | feynman-technique | 同上 |
| SQ3R | sq3r-method | 同上 |
| Leitner System | leitner-system | 同上 |
| AI note taker 选型 | best-ai-note-takers | Commercial 入口 |
| Quizlet 替代 | quizlet-alternatives | Alternative |
| ChatGPT 替代 | chatgpt-alternatives | Alternative |
| 大学笔记总览 | how-to-take-notes-in-college | How-To hub |

---

## §5 关键词速查

### P0 — 双核心

| 关键词 | user intent | 建议类型 | 目标页 |
|--------|------------|---------|--------|
| AI note taker | capture lectures | Commercial / How-To | `/` · `/feature/lecture-to-notes` |
| AI notes generator | generate from files | Commercial / How-To | `/feature/notes-generator` |
| AI note taker for college students | student + tool | Commercial | 首页 + blog |
| best AI note taker for students | tool selection | Commercial Roundup | best-ai-note-takers |

### P1 — 输入/输出

| 关键词 | 建议类型 | feature |
|--------|---------|---------|
| lecture to notes / real-time note taking | Commercial / How-To | lecture-to-notes |
| YouTube to notes | Commercial / How-To | youtube-to-notes |
| PDF to notes | Study Spoke AI connection | pdf-to-notes |
| AI flashcard generator / notes to flashcards | Alternative / Commercial | flashcard-maker |
| AI quiz generator | How-To / Commercial | quiz-maker |
| AI mind map generator | Study Spoke | mind-map-maker |
| lecture to podcast / study podcast | Commercial | podcast-generator |
| AI infographics generator | How-To | infographics-generator |

### P1 — 竞品截流

| 关键词 | 建议类型 |
|--------|---------|
| Quizlet alternative | Alternative |
| Knowt alternative | Alternative |
| RemNote alternative | Alternative |
| Otter alternative for students | Alternative |
| NotebookLM alternative | Alternative |
| ChatGPT alternative for students | Alternative（已有 03） |
| ScholarAI alternative | Alternative |

### P2 — 场景/学科

| 关键词 | 建议类型 | Use Case（若上线） |
|--------|---------|-------------------|
| AI note taker for STEM students | Commercial | for-stem-students |
| exam prep AI | How-To | exam-prep |
| ADHD study app | How-To / Commercial | for-adhd-students |
| how to study for finals | How-To（已有 06） | exam-prep |

---

## §6 产品、功能页与内外链

### 6.1 产品事实（创作可用）

**One-line**：
> ThetaWave is an AI-powered note-taking platform for college students that captures lectures in real-time and transforms audio, text, files, and YouTube videos into formatted notes, mindmaps, quizzes, flashcards, and podcasts.

**输入**：live audio · uploads · YouTube · PDF · web (Chrome extension)

**输出**：formatted notes · mind maps · quizzes · flashcards · podcasts · infographics · exam prep

**差异化 vs 通用 AI**：学生专属 workflow；实时讲座；多格式 study stack；非仅 chat summary

### 6.2 十功能页白名单

| Feature | URL |
|---------|-----|
| Notes Generator | `/feature/notes-generator` |
| Lecture to Notes | `/feature/lecture-to-notes` |
| YouTube to Notes | `/feature/youtube-to-notes` |
| PDF to Notes | `/feature/pdf-to-notes` |
| Flashcard Maker | `/feature/flashcard-maker` |
| Quiz Maker | `/feature/quiz-maker` |
| Podcast Generator | `/feature/podcast-generator` |
| Mind Map Maker | `/feature/mind-map-maker` |
| Infographics Generator | `/feature/infographics-generator` |
| Exam Generator | `/feature/exam-generator` |

### 6.3 主题 → Feature 映射（AI connection 用）

| 文章主题 | 链向 |
|---------|------|
| 讲座/实时/课堂 | `/feature/lecture-to-notes` 或首页 |
| PDF/教材/阅读 | `/feature/pdf-to-notes` |
| YouTube/视频课 | `/feature/youtube-to-notes` |
| 闪卡/间隔重复/Leitner | `/feature/flashcard-maker` |
| 自测/测验/Feynman | `/feature/quiz-maker` |
| 思维导图/概念图 | `/feature/mind-map-maker` |
| 音频复习/通勤 | `/feature/podcast-generator` |
| 信息图/视觉总结 | `/feature/infographics-generator` |
| 期末/模拟考 | `/feature/exam-generator` |
| 通用上传→笔记 | `/feature/notes-generator` |

### 6.4 内外链规则

| 规则 | 标准 |
|------|------|
| Introduction 首段 | ≥1 `/blog/{slug}` 或 `/feature/*` |
| Body blog | 1–4 互链（上下文分布） |
| Body feature | 0–2（主题相关） |
| signup | `https://thetawave.ai/auth/signup`；正文 H2 分散 ≤2 次 |
| feature | 按主题；同一 feature 全文 ≤1 次（workflow 节除外可 +1） |
| 权威外链 | 2–8：NCES、Sage/journal、大学 LSC、认知科学 |
| 竞品 | `rel="nofollow noopener"` HTML；锚文本用公司名 |
| 内链锚文本 | 描述性；禁 "click here"、"learn more" |

### 6.5 竞品公平摘要

| 竞品 | 优势（写作必须承认） | 限制 |
|------|---------------------|------|
| **Quizlet** | 品牌认知；deck 生态；games | 付费墙；workflow 偏 terms |
| **Knowt** | 免费；Quizlet 替代叙事 | 深度因 plan 而异 |
| **RemNote** | 笔记+SRS+PDF | 学习曲线 |
| **Otter** | 实时转录成熟 | 偏会议；少 study stack |
| **NotebookLM** | 文档 grounded；Audio Overviews 免费 | 非 lecture capture 专用 |
| **ChatGPT** | 灵活通用 | 无实时讲座；无原生 flashcards |
| **ScholarAI** | 免费入门；slides→notes | 功能广度有限 |
| **Anki** | 开源 SRS 控制 | 设置成本高 |

---

## §7 Frontmatter 与文件命名

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{slug-kebab}-2026.md` |
| NN | 两位递增；下一号 **15** |
| slug | frontmatter 与 URL 一致；**不含年份**；通过 §2.8 反模式检查 |
| image | `/blog/images/{slug}-2026.jpg` |

成稿后提示人类更新 `blog/readme.md`。**Skill 不自动改 README**。

策略变更时 bump `metadata.version`。

---

## §8 Voice 与合规

### 8.1 正向 Voice

| 维度 | 要求 |
|------|------|
| Clear | 非专业读者能复述要点 |
| Student-friendly | 像学习伙伴，非企业采购文 |
| Evidence-led | 认知科学/教育统计有来源 |
| Wirecutter-style fair | 每工具 trade-off；≥1 场景竞品更合适 |
| Category-building | ThetaWave 首次出现前已有独立价值 |

### 8.2 禁止

- revolutionary · game-changing · unlock · seamless · magic · best-in-class · only solution
- 把 10x faster 写成 measured outcome
- SOC 2 · end-to-end encryption（未核实）
- 虚构 lecture 场景开头（"Imagine you're in class…"）
- 空泛句：In today's data-driven world / It is important to note that / Without further ado /
  Let's dive in / Here's the thing / Consider the following / As we all know / The reality is that /
  But that's not all

### 8.3 按类型产品策略

| 类型 | 产品策略 |
|------|---------|
| Commercial | input/output 分场景；ThetaWave 为一之选项非唯一 |
| Alternative | 公平列表；ThetaWave 按 fit 描述 |
| Study Spoke | 方法教学 70%+；AI connection 1 段（全文后 30%） |
| Study Hub | 表格+简述；AI 仅 optional 一句 |
| How-To | 步骤优先；工具在 workflow 节 |

### 8.4 漏斗透明度按类型

| 类型 | 标准 |
|------|------|
| Commercial / Alternative | 漏斗可透明（读者知道是产品对比文） |
| Study Method Spoke | 漏斗应不可见。转折点（产品出现）在全文 ≥70% 位置。 |
| Study Method Hub | 漏斗应不可见。方法对比完整后才可出现产品。 |
| How-To | 工具在 workflow 节出现。不每段推产品。 |

---

## §9 与 templates / meta skill 分工

| 阶段 | 工具 |
|------|------|
| 选题 → Brief → Outline → Draft → SelfCheck（12 维） | **本 Skill** |
| title/description 专项优化 | **thetawave-meta-title-description** |
| 发布前终审、P0 Gate + 十维评分 + Source Map + SERP Fit | **`references/portable/final-audit.md`** + portable 模板 |
| Phase 0R Research | **`references/portable/research-triangle.md`** |

Phase 3 已内联 title/description 规则；无需读取 meta skill 文件。

---

## §10 Mini Example — Brief + Outline 片段

以 `cornell-note-taking-method`（Study Method Spoke）为参照。

### Brief（节选）

```markdown
## Article Brief
**Working title**: Cornell Note Taking Method — Complete Guide with Templates (2026)
**Primary keyword**: Cornell note taking method
**Article type**: StudyMethodSpoke
**Templates category**: Research
**Core keyword lane**: NotesGenerator
**Reader stage**: Awareness / Consideration
**Target audience**: College students in lecture-heavy courses
**Word count target**: 2200–2500
**Cluster role**: Study spoke (hub: study-methods-compared)
**Differentiation angle**: Step-by-step + science + ASCII layout + AI Cornell formatting
**Competitor gap**: SERP 多为短 overview，缺 cue column workflow + testing effect citations
**Canonical concepts to reference**: study-methods-compared (1 table row + link)
**Primary feature link(s)**: /feature/pdf-to-notes
**KEEP/MERGE**: KEEP
**Category**: Research
```

### Outline（节选）

```markdown
## Outline — cornell-note-taking-method

| § | H2 | Target words | Notes |
|---|-----|-------------|-------|
| Open | What Is the Cornell Note Taking Method? | 250 | link: how-to-take-notes-in-college |
| | The Cornell Note Format — Three Sections | 400 | ASCII diagram |
| | Why Cornell Notes Work — The Science | 350 | Roediger & Karpicke source |
| | How to Take Cornell Notes — Step by Step | 500 | numbered sub-steps |
| | Common Mistakes | 200 | |
| | AI connection | 150 | link: /feature/pdf-to-notes |
| FAQ | FAQ | 200 | 固定 6 题；正文 ### 小题 |

**Estimated total**: ~2300 words
```

### AI connection 范例句

> Instead of manually formatting every lecture into Cornell layout, the **[AI PDF to Notes](https://thetawave.ai/feature/pdf-to-notes)** tool generates Cornell-formatted notes from uploaded PDFs and recordings—including Cue Column questions and summaries.

### Conclusion 多样结尾示例

每篇 conclusion 用不同的收束方式（避免跨篇模板化）：

- **预测**: "As lecture capture AI improves, Cornell notes may evolve from a manual technique into an automated study layer…"
- **未解问题**: "Whether the Cue Column format transfers equally well to lab-based STEM courses remains an open question…"
- **具体警告**: "Don't confuse transcribing with note-taking—the Cornell method's value is in the Cue Column, not the Note column…"

---

*thetawave-blog-article · v2.2.1 · 2026-07-28 · fully self-contained · references/portable/*
