---
name: vofy-blog-article
description: Create Vofy blog articles (vofy.art/blog) from brief to draft. Fully self-contained skill folder; load references/portable/ for Phase 0R and final audit.
metadata:
  version: 2.0.0
  project: vofy.art
  locale: en
  self-contained: true
---

# Vofy Blog Article Creation

为 **https://www.vofy.art/blog/** 从选题到英文成稿。**硬性规则：Agent 只读本 SKILL + `references/`（含 `references/portable/`），禁止读 skill 文件夹外文档。** 发布前终审用 `references/portable/final-audit.md`。

**本文件自包含**：项目配置、G1–G7 阻断规则、7 类路由、内容图谱、引用分级、碎片化防护、漏斗透明度、7 Phase 工作流、14 维创作自检、Mini Example 均内联。

---

## §0 如何使用

### 触发语

```
按 vofy-blog-article skill，为关键词 "{primary keyword}" 创建一篇 {ModelGuide|PromptGuide|AppHowTo|Comparison|StyleGuide|Campaign|Announcement} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
```

批量示例：

```
按 vofy-blog-article skill，为 Grok Imagine Image 簇补一篇 ModelGuide + 一篇 PromptGuide。
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主题 / 主关键词 | ✅ | 决定 intent 与 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| 系列 / 簇 | 可选 | hub-spoke 定位；如 `gpt-image-2`、`kling-3-0` |
| 竞品参考 URL | 推荐 | Phase 0 信息增量判断 |
| `app_slug` | AppHowTo 必填 | 对应 `/apps/{slug}` |

### 输出（Phase 7 交付物）

1. **Article Brief**（Markdown 摘要）
2. **完整稿** `vofy/blog/53-{slug}.md`（NN = §4 下一序号，当前为 **53**）
3. **SelfCheck 表**（§3 Phase 6，14 维 Pass/Fail + Notes）
4. **templates 审核指令**（复制即用，§3 Phase 7）
5. **提示人类**更新 `blog/README.md` 文件表

### Agent 执行顺序

```
§2 类型路由 → §3 Phase 0–7 顺序执行 → 缺信息时先问 Phase 0 四必问
```

与用户沟通策略说明可用中文；**正文必须为英文**（上线稿）。

---

## §1 项目配置

审核/创作时将下表作为 Vofy 固定上下文。

| 配置项 | Vofy 值 |
|--------|---------|
| **品牌/产品名** | Vofy、VOFY |
| **产品名大小写** | 正文用 **Vofy**；大写 VOFY 仅 logo/横幅语境 |
| **主域名** | vofy.art |
| **博客路径前缀** | /blog/ |
| **品类 one-liner** | Your All-in-One AI Creative Studio |
| **Hero 问句** | What do you want to create? |
| **消费单位** | **Credits**（例：AI Image ~2.5 Credits — **随模型/分辨率变化，须标注以现网为准**） |
| **语言** | 英文正文；中文仅用于与用户沟通 |
| **Primary ICP** | 日常内容创作者、搜索驱动型工具访客 |
| **Secondary ICP** | 电商卖家、模型猎人/AI 爱好者 |
| **Pillar Hub（按簇）** | 见 §4.2；全局品类 Hub 待建：`what-is-vofy-ai-creative-studio`（缺口） |
| **关键词策略** | 内联 §5（本文件） |
| **内容规范** | 内联 §2–§3（本文件） |
| **未上线页面前缀（禁止内链）** | 404 的 `/studio?model=*`、`/models/*`、`/apps/*`；内链前假设需可访问 |
| **署名默认** | 从 persona 池选用（§1.2）；Campaign 可用 `Vofy Team` |
| **竞品（对比文）** | Leonardo.ai、Runway、Pika、Luma、fal playground、官方 model playground |
| **Blog 站面定位** | Learn how to use AI-generated video and images to grow your brand |

### 1.1 可链接 URL 白名单（内链优先）

| 类型 | 路径示例 |
|------|---------|
| 博客 | `/blog/{slug}` — 见 §4 |
| **Canvas** | `/canvas` |
| 首页 | `/` |
| Apps 目录 | `/apps` |
| 单 App | `/apps/{app-slug}` |
| 图像 Studio | `/studio/create/image?mode=create&model={model-id}` |
| 视频 Studio | `/studio/create/video?mode=create&model={model-id}` |
| Motion Control | `/studio/create/video?mode=motion-control` |
| Inpaint | `/studio/create/image?mode=inpaint`（以现网为准） |
| 模型页 | `/models/{vendor}/{version}` |
| 风格工作台 | `/studio/create/image?mode=create&model=gemini-3.1-flash-image-preview&workspace=styles` |

**G6 规则**：不链未上线路径；forthcoming ≤1 且仅 Related 脚注；正文核心流程不用 forthcoming 链接。

### 1.2 作者 Persona 池（与现网一致）

| 作者 | 适合主题 |
|------|---------|
| Ryan Mitchell | 通用教程、GPT Image 2、LinkedIn/职业向 |
| Sofia Rodriguez | 人像、滤镜、美颜、绿幕 |
| Yuki Tanaka | 模型深度、Seedance/Kling、艺术向 |
| Emma Clarke | 风格化、South Park/Ghibli、宠物视频 |
| Alex Harper | 电商、节日营销、Kling 设置 |
| Marcus Chen | 对比文、多语言营销 |
| Priya Sharma | 工具 HowTo、发型/LinkedIn |
| Lucas Andersson | 创意实验、April Fools、线稿 |
| Vofy Team | 公告、敏感/官方口吻 |

### 1.3 敏感类目合规模板

以下类目正文须含 **用途与授权声明**（FAQ 或开篇后独立段）：

| 类目 | 示例 slug / 主题 | 必写要点 |
|------|-----------------|----------|
| 亲密互动视频 | `ai-kissing-video-generator`、`ai-hugging-video-generator` | 仅用于本人或已授权素材；禁止冒充他人 |
| 名人换脸 | `ai-celebrity-selfie-generator` | 娱乐用途；禁止误导性「真实合影」传播 |
| 身体/肤色/泳装预览 | `ai-tankini-swimsuit-try-on`、`ai-skin-color-changer` | 尊重肖像权；非医疗/非身份验证用途 |
| IP 风格模仿 | Ghibli、Rick & Morty、South Park | 风格参考表述；非官方联名 |
| 政治人物生成 | `nanobanana-2-trump-image-generation-guide` | 标注 satire/editorial；遵守平台政策 |

**模板句**（按场景改写）：

> Use only photos you own or have permission to edit. Do not create misleading content that impersonates real people or violates platform policies.

### 1.4 G1–G7 一票否决阻断规则

以下 7 项为发布前硬性阻断——**任一项触发则文章不得发布**，修复后重新过 Gate。Phase 6 SelfCheck 首维即逐项对照此表。

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 模型能力、Credits、studio 参数与 vofy.art 现网矛盾 | 逐 claim 对照 §6.1–§6.4 产品事实表。功能不在当前版本 → 不能声称"已发布"。Credits 数值→标注"as of [date]"并提示以现网为准。 |
| **G2** | 死链 | 内链 404；`/studio?model=` 参数错误 | 逐个检查所有内链是否可访问（对照 §1.1 白名单）。外链可有 1–2 失效（外部不可控），但不能全挂。 |
| **G3** | 无来源数字 | 「2M+ users」、benchmark 分数、竞品定价无 attribution | P0 级数字必须可追溯到原始来源或标注内部数据基础。单案例不能写成复数趋势。竞品定价须有时效标注。 |
| **G4** | 竞品/模型状态错误 | GA/Beta/Deprecated 与官方公告矛盾 | 打开竞品官网/docs 验证。特别注意已 Deprecated 模型不能标为 "active competitor"。 |
| **G5** | 产品能力夸大 | 禁「唯一支持」「全球首个」；Credits 勿写死；禁未验证的「fastest/cheapest」 | 定位语言（"designed to"、"aims to"）≠ 已实现功能。Credits 标注 "rates vary by model and resolution"。 |
| **G6** | 内链指向未上线页面 | 对照 §1.1 白名单 | 只链白名单内路径；forthcoming >1 → Fail。正文核心流程不得使用 forthcoming 链接。 |
| **G7** | 品牌/合规风险 | 敏感类目缺声明；贬低竞品；未标注 AI 生成示例 | 对照 §1.3 五类敏感内容逐项核查。竞品措辞检查："just"、"merely"、"only does X" 均为贬低性措辞触发词。 |

---

## §2 文章类型路由

收到任务后**先匹配类型**，再跳转对应 H2 模板与约束。

### 2.1 路由表

| 类型 | 典型 intent | 词数 | 产品提及上限 | templates category | disclosure | 参考 slug |
|------|------------|------|-------------|-------------------|------------|-----------|
| **ModelGuide** | what is X / features | 1800–2800 | ≤25% | Model | 推荐 | `gpt-image-2-guide` |
| **PromptGuide** | how to write prompts | 2000–3200 | ≤30% | Tutorial | 推荐 | `gpt-image-2-prompts-guide` |
| **AppHowTo** | how to use {tool} | 1500–2500 | ≤50% | HowTo | 必填 | `how-to-change-eye-color-ai` |
| **Comparison** | X vs Y / best for Z | 2200–3200 | ≤40% | Comparison | 必填 | `gpt-image-2-vs-midjourney-comparison` |
| **StyleGuide** | {style} generator | 1500–2200 | ≤45% | Style | 必填 | `ghibli-style-image-generator-guide` |
| **Campaign** | 节日 / 营销场景 | 1200–2000 | ≤50% | Campaign | 必填 | `mothers-day-ai-image-generator` |
| **Announcement** | 新模型上线 Vofy | 1000–1800 | 不限 | Product | 视情况 | `nano-banana-2-gemini-3-1-flash-image-generation` |

**templates category 映射**：以上 7 类在交付 templates 审核时对应 Model / Tutorial / HowTo / Comparison / Style / Campaign / Product。Brief 阶段填入以备用。

**路由规则**：

- `{model} guide` / `what is` / `complete guide` → **ModelGuide**
- `prompts` / `how to write` / `prompt guide` → **PromptGuide**
- `how to` + 单 App/滤镜/特效 → **AppHowTo**
- `vs` / `compare` / `best` + 多模型或工具 → **Comparison**
- `{style} filter/generator/style guide` → **StyleGuide**
- 节日名 / Mother's Day / Easter / campaign → **Campaign**（`seasonal: true`）
- What's New 模型首发 → **Announcement**

### 2.2 全类型通用模块

| 模块 | 要求 |
|------|------|
| **TL;DR** | 3–5 bullet；独立传达 ~80% 价值（与现网 59 篇命名一致；templates 审核中此模块对应 TL;DR 维度，不扣分） |
| **H2 编号** | 英文编号 `## 1.` `## 2.`；FAQ 不编号 |
| **Conclusion** | `## N. Conclusion` 或 *Bottom line*；用多样的收束方式（预测/未解问题/具体警告），避免跨篇模板化 |
| **FAQ** | **固定 6 题**（2026-08-11 定标）；≥1 题覆盖边界/objection；**全部内容相关**（禁止通用模板题） |
| **Related Reading** | 2–3 条；2026-08-11 起 frontmatter 不再含 `related`，以正文互链为准 |
| **内链** | 正文 ≥2 其他 blog slug；同 cluster ≥1 |
| **Studio/Apps 链** | ModelGuide/PromptGuide 必链 studio + `/models/`；AppHowTo 必链 `/apps/{slug}` |
| **外链** | 2–5 条；HTML `<a href="..." rel="nofollow noopener">` |
| **列表比例** | ModelGuide/PromptGuide ≤30%；Comparison ≤35%；AppHowTo ≤40% |
| **长段落** | ≥3 段，每段 4–8 句（80–200 words）；段长标准差 ≥1.5 |
| **时效标注** | 模型类：`model_version_note` + 正文 `as of {month} {year}` |
| **CTA** | 单一主行动（Open in Studio / Try the App）；Related 即自然 CTA |
| **利益声明** | Comparison / StyleGuide / Campaign / AppHowTo 文开篇后须含 "Disclosure: Vofy is..." 1–2 句声明段（见 §5.5） |
| **敏感类目声明** | 如涉及 §1.3 五类敏感内容：开篇或 FAQ 中放置用途与授权声明段 |

### 2.3 ModelGuide — H2 模板

**叙事弧线**：读者为什么关心 → 模型定义 → 核心能力 → 适用场景 → 在 Vofy 上怎么用 → 局限。

```
## TL;DR

## 1. Why {Model} Matters for {Audience}
## 2. What {Model} Is — Key Features
   ### 2.1 What's New vs Prior Generation
   ### 2.2 Strengths and Trade-offs
## 3. Best Use Cases on Vofy
   ### 3.1 {Use case A}
   ### 3.2 {Use case B}
## 4. Quick Start on Vofy Studio
   （链 studio_url + /models/ 页）
## 5. Limitations and When to Pick Another Model

## N. Conclusion
## FAQ（固定 6 题）
## Related Reading
```

### 2.4 PromptGuide — H2 模板

**叙事弧线**：常见 prompt 失败 → 可复用框架 → 分场景模板 → 调试技巧。

```
## TL;DR

## 1. Why Most {Model} Prompts Underdeliver
## 2. A Reusable Prompt Framework for {Model}
   ### 2.1 Subject + Medium + Lighting + Camera
   ### 2.2 Negative / Constraint Language
## 3. Prompt Templates by Use Case
   ### 3.1 {Social / Product / Portrait / Video}
## 4. Copy-Ready Examples（带预期输出描述）
## 5. Troubleshooting: When Output Looks Wrong

## FAQ（固定 6 题，PromptGuide 推荐）
## Related Reading
```

### 2.5 AppHowTo — H2 模板

**对齐 Vofy HowTo 三步框架**（Upload → Configure → Generate → Download）。

```
## TL;DR

## 1. What You'll Get（结果预览 + 对谁有用）
## 2. Before You Start（素材要求 + 合规声明，§1.3）
## 3. How to {Outcome} with Vofy in 3 Steps
   ### 3.1 Upload your photo
   ### 3.2 Choose {preset / style / settings}
   ### 3.3 Generate and download
## 4. Tips for Better Results
## 5. Common Mistakes to Avoid

## FAQ（固定 6 题）
## Related Reading
```

**硬性要求**：frontmatter `app_slug` 必填；正文至少 1 次链 `/apps/{app_slug}`。

### 2.6 Comparison — H2 模板

**叙事弧线**：决策场景 → 对比维度 → 分场景推荐 → **不导向单一赢家**。

```
## TL;DR

## 1. The Decision You're Actually Making
## 2. Comparison at a Glance（表格 + 前后分析段）
## 3. {Model A} — Strengths and Limits
## 4. {Model B} — Strengths and Limits
## 5. Which One Fits Your Workflow
   ### 5.1 For speed / For quality / For cost
## 6. Running the Same Prompt on Vofy（可选实操段）

## FAQ（固定 6 题）
## Related Reading
```

**Vofy 出现方式**：Comparison 表一行 + studio 链；不做「Vofy 唯一推荐」。

### 2.7 StyleGuide / Campaign / Announcement

**StyleGuide**：Why this aesthetic → Picking source photos → Prompt/preset patterns → Before/after tips → IP/compliance note。

**Campaign**：Campaign goal → Asset types needed → Step-by-step creation → Localization/variations → Posting checklist。`seasonal: true`；Related 链 evergreen 工具文。

**Announcement**：What's launching → Why it matters → Key specs → Try on Vofy（studio CTA）→ FAQ。

### 2.8 Slug 与 Title 规则

| 原则 | Vofy 执行 |
|------|----------|
| P1 常青 | 新稿 slug **不含年份** |
| P2 关键词 | 含 primary keyword 核心词 |
| P3 可读 | kebab-case |
| P4 长度 | 4–8 词，≤60 字符 |
| P5 集群一致 | 同簇命名模式一致；Nano Banana 新稿用 `nano-banana-2-*` |
| P6 搜索意图 | 像读者会搜的语言 |

**新稿 slug 禁词**（internal 标签）：`complete` · `ultimate` · `definitive` · 年份

**Slug 反模式速查（创作阶段必检）**：

| 反模式 | 错误示例 | 正确示例 |
|--------|---------|---------|
| 含年份 | `ai-image-prompts-2026` | `ai-image-prompts` |
| 含数量 | `top-5-ai-models` | `best-ai-models-compared` |
| 连续重复词 | `nano-banana-2-guide-guide` | `nano-banana-2-prompts-guide` |
| 内部架构词泄漏 | `kling-3-0-complete-guide` | `kling-3-0-overview` |
| 前缀命名沉积 | 全簇 `nanobanana-2-*` | 各篇以搜索词开头，统一 nano-banana-2-* |

**Slug "大声读"测试**：去掉连字符大声读出来 → 通顺 → 通过；不通顺或含重复词 → 改。

**Title 公式**（<60 chars）：

- ModelGuide：`{Model}: What It Is and When to Use It on Vofy`
- PromptGuide：`How to Write Better {Model} Prompts — {Hook}`
- AppHowTo：`How to {Outcome} with AI — {Benefit}`
- Comparison：`{A} vs {B} for {Use Case} — {Frame}`

**Meta description**（120–160 chars）：benefit + 主 intent 词 + 差异化一句。

### 2.9 Frontmatter Schema

```yaml
---
title: "Title Case — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword for SERP"
slug: "kebab-case-slug"
date: 2026-06-XX
author: "Ryan Mitchell"
category: "Model | Tutorial | HowTo | Comparison | Style | Campaign | Product"
cluster: "gpt-image-2"
model: "gpt-image-2"
app_slug: ""
studio_url: "/studio/create/image?mode=create&model=gpt-image-2"
disclosure: "Vofy is an all-in-one AI creative studio. This article uses Vofy workflows as examples."
seasonal: false
model_version_note: "Based on {model} as available on Vofy, June 2026."
---
```

> **2026-08-11 起废弃**：`image` / `keywords` / `related` 不再写入 frontmatter（image 由 CMS 单独管理；keywords/related 由正文内链与 CMS 配置承载）。

---

## §3 创作工作流（7 Phase）

### Phase 0 — Intake（四必问）

| # | 问题 | 用途 |
|---|------|------|
| 1 | 目标 SEO 关键词 + search intent？ | 类型路由 |
| 2 | 目标受众 + 技术水平？ | 深度及格线 |
| 3 | 发布目的？SEO / 品牌 / 转化 | 产品提及容忍度 |
| 4 | 同主题竞品内容 2–3 链接？ | 信息增量 |

**选问**：`app_slug`（AppHowTo）；studio/model 页是否存在；cluster hub 是哪篇；是否 seasonal。

---

### Phase 1 — 独立成文 Gate

**三条件满足 ≥2 → KEEP**；否则 **MERGE**。

| 条件 | 判断 |
|------|------|
| 搜索意图独立 | 与 §4 已有 slug 关键词重叠 ≤50% |
| 读者阶段不同 | Discovery / Tutorial / Evaluation / Activation |
| 深度不可压缩 | 核心内容 >600 词，无法压入他文 ≤3 段 |

**高冲突边界**：

| slug 主题 | 与谁边界 |
|-----------|---------|
| `gpt-image-2-guide` | vs `gpt-image-2-prompts-guide`：定义 vs prompt 框架 |
| `kling-3-0-complete-guide` | vs `best-kling-3-0-prompts`：功能 vs prompt 列表 |
| App HowTo vs StyleGuide | 同一 App 只保留一篇 canonical HowTo |

---

### Phase 2 — Article Brief

```markdown
## Article Brief

**Working title**:
**Primary keyword**:
**Article type**: ModelGuide | PromptGuide | AppHowTo | Comparison | StyleGuide | Campaign | Announcement
**Templates category**: Model | Tutorial | HowTo | Comparison | Style | Campaign | Product
**Search intent**: Informational | Commercial | Transactional | Navigational
**Reader stage**: Discovery | Tutorial | Evaluation | Activation
**Publish goal**: SEO | Brand | Conversion
**Target audience**:
**Word count target**:
**Cluster role**: Hub / Spoke / Standalone
**Cluster ID**:
**Pillar link**:
**app_slug** / **studio_url** / **model**:
**Differentiation angle** (vs SERP top 3):
**Competitor gap**:
**Canonical concepts to reference** (link only, do not redefine):
**KEEP/MERGE**: KEEP | MERGE → {target slug}
**Compliance notes**（§1.3）:
**Disclosure needed**: Required | Recommended | Optional
```
**变更说明（v2.0）**：原 "Search intent" 字段枚举值实际是文章类型，已改为 "Article type"。新增 "Templates category" 映射字段和标准 SEO "Search intent" 四分类。

---

### Phase 3 — Slug + SERP + Frontmatter

1. 2–3 slug 候选 + 推荐（§2.8；检查反模式表 + "大声读"测试）
2. title + description（计字符）
3. 完整 frontmatter
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

编号 H2 骨架（§2.3–2.7），每节标注目标词数、内链占位、studio/apps 链。

```markdown
## Outline — {slug}

| § | H2 | Target words | Links / Notes |
|---|-----|-------------|---------------|
| Open | … | 150 | link: /blog/... + disclosure (if applicable) |
| TL;DR | … | 120 | primary keyword |
...
**Estimated total**: N words
```

---

### Phase 5 — Draft 写作约束

#### 5.1 Voice（Vofy）

| 正向 | 要求 |
|------|------|
| Creator-first | 具体场景：Reels cover、product flat lay、TikTok hook |
| Practical | 可复制的 prompt / 步骤 / 设置名 |
| Honest about limits | 承认某模型在 text-in-image、时长等方面的 trade-off |
| Fast-paced but not hype | 可用「fast」「cinematic」；禁 revolutionary/game-changing |
| Credits-transparent | 提及 Credits 时加「rates vary by model and resolution」 |

| 禁止 | 触发 |
|------|------|
| Vendor puffery | only platform, unbeatable |
| Fake benchmarks | 无来源的「beats Midjourney every time」 |
| Misleading UGC claims | 虚构 before/after |
| IP overreach | 「official Ghibli partnership」 |

#### 5.2 事实、合规与引用分级

##### 引用分级（P0/P1/P2）

Vofy 文章涉及大量量化数据：Credits 消耗、模型 benchmark、竞品定价、"2M+ users"。以下分级决定引用深度：

| 级别 | 触发条件 | 要求 | 示例 |
|------|---------|------|------|
| **P0 — 必须引用链接** | 竞品定价、benchmark 分数、市场份额、Credits 具体数值 | 链接到原始来源（官方 pricing 页、benchmark 报告、官方 docs）。同一数字跨篇出现时每篇都要链。 | "Midjourney Pro $60/mo"、"Kling 3.0 T2V-500 benchmark"、"GPT Image 2 4K upscale" |
| **P1 — 应当引用** | 行业趋势、竞品状态（GA/Beta）、"fastest/cheapest" 类声明 | 链接到官方 docs / Changelog / 行业报告。如无法链接则加限定词（"as of [date]"、"typically"）。 | "AI video generation typically 2–5 minutes per clip as of June 2026" |
| **P2 — 可不引用** | 原创 prompt 框架、作者自己测试的效果对比、从已引用数据衍生的分析 | 注明方法论基础或标注 "based on internal testing, n=X"。 | "Based on testing 20 prompt variations across 4 models..." |

##### 内部数据声明标准格式

当引用 Vofy 内部数据（如注册用户数、平台统计数据）或作者观察时，格式为：

> Based on internal analysis of [N] [data type] across [time period], [finding].

示例：
- "Based on internal testing of 50 prompt variations across GPT Image 2 and Midjourney in Q2 2026, GPT Image 2 produced more accurate text-in-image results in 68% of test cases."
- 禁止裸数字 "2M+ users choose Vofy" → 应有来源标注或时间窗口

##### 事实与合规速查

| 规则 | 执行 |
|------|------|
| 量化 claim | P0 级：`[Source: URL]` 链接；P1 级：链接或限定词 |
| 竞品定价/状态 | 标注 "as of [date]"；基于官网（非二手博客） |
| Credits | 标注 "rates vary by model, resolution, and duration" |
| 模型能力 | 标注 "as of {month} {year}"；禁写死「永远最便宜/最快」 |
| Benchmark 分数 | P0 级引用；说明测试条件（分辨率、prompt、评估方法） |
| 政策/准入门槛 | 有时效标注（如涉及 pricing / model availability） |

#### 5.3 漏斗透明度自检

在正式起草前，检查叙事弧是否过于透明：

**检测方法**：提取文章的叙事弧——开头（教育/问题陈述）→ 中部（中立概述）→ 转折点（"but" / "however" / "this is where"）→ Vofy 作为答案。

| 文章类型 | 漏斗透明度接受标准 |
|---------|-------------------|
| **Comparison / ModelGuide** | 可接受透明漏斗——读者知道这是产品对比/评测文。disclosure 在开篇标注。 |
| **PromptGuide** | 漏斗应适度。Prompt 框架教学 >70%；Vofy studio 实操在全文后 30%。 |
| **AppHowTo / StyleGuide** | 漏斗可明显——读者意图就是使用工具。产品占比允许较高（≤50%/≤45%）。 |
| **Campaign / Announcement** | 漏斗可透明——读者知道是品牌/营销内容。 |

**自检问题**：如果 PromptGuide 类文章在全文前 30% 就能被识别为 vendor blog → 漏斗过于明显，需重新平衡教学深度与产品出现时机。

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
| 相邻 H2 section | 不连续出现 2 个 "H2 → 列表 → 无分析 → 下一 H2" 模式（列表轰炸） |
| 列表项不超过 7 条 | 超过则考虑拆分为子标题 + 段落 |

##### 段间衔接

- 相邻段落之间至少有 1 种衔接手段：过渡词（"however"/"specifically"）/ 句子桥 / 关键词重复 / 指代词回指
- 目标：任意连续 10 段中 ≥7 对有衔接手段
- 避免 H2 后直接跟列表（H2 → 1–2 句过渡段 → 列表）

#### 5.5 利益声明（创作阶段必含）

| 文章类型 | 需要利益声明？ | 位置与模板 |
|---------|:---:|------|
| **Comparison** | ✅ 必须 | 开篇后紧跟：`Disclosure: Vofy is an all-in-one AI creative studio. This article compares multiple tools, including Vofy workflows, to help you choose.` |
| **StyleGuide** | ✅ 必须 | 同 Comparison |
| **Campaign** | ✅ 必须 | 开篇后或文末 |
| **AppHowTo** | ✅ 必须 | 开篇后：`Disclosure: This tutorial uses Vofy, an all-in-one AI creative studio, as the demonstration tool.` |
| **ModelGuide** | ⚠️ 推荐 | 开篇后自然声明 Vofy 平台关系 |
| **PromptGuide** | ⚠️ 推荐 | 文末或 AI workflow 段落中自然声明 |
| **Announcement** | 视情况 | 品牌内容不言自明；如提及竞品则加 |

**禁止**：利益声明写成营销语 → 保持简洁中立的 1–2 句。

#### 5.6 内链规则

- Model 文：≥1 `/models/` + ≥1 studio_url
- App 文：≥1 `/apps/{app_slug}` + ≥1 同品类 blog
- Comparison：≥2 被对比模型的 ModelGuide/PromptGuide
- 锚文本描述性（"our GPT Image 2 guide"），禁 "click here"、"learn more"
- 内链用 Markdown；外链/竞品用 HTML `<a href="..." rel="nofollow noopener">`

#### 5.7 竞品公平描述

| 规则 | 执行 |
|------|------|
| 每竞品 ≥1 明确优势（非敷衍） | 从竞品官方 docs/pricing 取优势 + 限制 |
| 禁贬低性措辞 | "just" / "merely" / "only does X" / "basically just" / "simplistic" |
| 对比表无二元化 | 不把需要 nuance 的能力简化为 "Yes/No"；如有简化需加脚注 |
| ≥1 场景推荐非 Vofy 方案 | 写在正文，非脚注（如 "If you need local/offline generation, {competitor}'s desktop app is a better fit."） |

#### 5.8 模块顺序

```
YAML frontmatter
→ {Disclosure paragraph}（如适用）
→ Opening hook（≤200 words）
→ ## TL;DR
→ 正文 H2
→ ## N. Conclusion
→ ## FAQ
→ ## Related Reading
```

---

### Phase 6 — 创作自检（14 维 Pass/Fail + Notes）

以下 14 维逐项自检。每项标注 Pass / Fail + 具体 Notes。Overall FAIL 则标注修复动作后重新过 Phase 6。

#### 1. Publishability G1–G7

| 检查项 | 对照 | Fail 条件 |
|--------|------|----------|
| G1 事实错误 | §1.4 G1 | 任何 claim 与 §6.1–§6.4 产品事实表矛盾；Credits 未标注浮动 |
| G2 死链 | §1.4 G2 | 内部链接 404；外链全挂 |
| G3 无来源数字 | §1.4 G3；§5.2 引用分级 | P0 级数字无链接或内部数据无 n= 标注 |
| G4 竞品/模型状态错误 | §1.4 G4 | 竞品/模型状态与官方矛盾 |
| G5 产品夸大 | §1.4 G5 | 定位语言当作已实现功能写；Credits 写死 |
| G6 未上线内链 | §1.4 G6；§1.1 白名单 | 链接不在白名单；forthcoming >1 |
| G7 品牌/合规风险 | §1.4 G7 | 敏感类目缺声明；贬低竞品 |

#### 2. Fact/E-E-A-T

- [ ] 所有 P0 级量化 claim 有 `[Source: URL]` 或内部数据标注（"based on internal testing, n=X"）
- [ ] 竞品描述基于官方资料（非二手博客）；pricing 有时效标注
- [ ] 每竞品 ≥1 优势；无贬低性措辞
- [ ] ≥1 场景推荐非 Vofy 方案（EEAT 信号）
- [ ] 基准测试/benchmark 有测试条件说明（分辨率、prompt、评估方法）
- [ ] 对比表无二元化简化；如有简化有脚注

#### 3. Differentiation

- [ ] 与 §4 已有文章 H2 标题重叠 <30%
- [ ] 核心论点/框架在 SERP 前 3 竞品中找不到等效替代
- [ ] 独有框架/prompt 模板/对比维度至少 1 项
- [ ] Canonical Concept（§4.3）：引用方式为 1–2 句 + link（不重复完整定义）
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

- [ ] §5.1 正向 5 维全满足（Creator-first / Practical / Honest / Fast-paced / Credits-transparent）
- [ ] 禁词（revolutionary / game-changing / unlock / seamless / magic / best-in-class / only solution）0 次命中
- [ ] 空泛句 ≤2 处（"In today's world…" / "Let's dive in…" / "It is important to note that…" 等）
- [ ] 每 300–500 词出现 1 个具体对象（具名工具/数字/workflow/场景）
- [ ] 无虚构 UGC / before-after 案例
- [ ] 无 IP overreach（"official partnership"）

#### 7. Objectivity & Transparency

- [ ] 文章 type 对应漏斗接受标准（§5.3）
- [ ] 产品提及比例 ≤ §2.1 类型上限
- [ ] 竞品描述无贬低性措辞；定位语言与功能事实区分明确
- [ ] Comparison / StyleGuide / Campaign / AppHowTo 文含 disclosure 段（开篇后）
- [ ] PromptGuide 文产品出现时机在全文 ≥30% 位置
- [ ] 署名从 persona 池正确选用；Campaign 可用 Vofy Team

#### 8. Structure/Links

- [ ] 必备模块完整：TL;DR + FAQ（固定 6 题）+ Related（2–3）
- [ ] 首段 ≥1 blog 或 studio/apps 内链；Body blog 1–4 互链
- [ ] 内链锚文本描述性（无 "click here"）；内链用 Markdown，外链/竞品用 HTML nofollow
- [ ] Related 与正文互链一致（frontmatter 不再含 `related`）
- [ ] Forthcoming ≤1（仅限 Related 脚注）
- [ ] 所有内链可访问（对照 §1.1 白名单）

#### 9. SEO/SERP

- [ ] title 含 primary keyword（45–65 字符）
- [ ] description 120–160 字符；含 keyword + value prop；与正文首段一致
- [ ] keywords 规划 ≥5、覆盖长尾（仅用于 SEO 规划，不入 frontmatter）
- [ ] FAQ 覆盖 Google People Also Ask 常见问题
- [ ] 有 snippet-ready 定义：40–60 词直接回答
- [ ] slug 常青、无年份/数量/内部架构词；通过"大声读"测试；通过反模式表检查

#### 10. Conversion

- [ ] CTA 与读者阶段匹配（Discovery → 内链；Tutorial → studio CTA；Evaluation → Comparison）
- [ ] studio + signup CTA 分散在不同 H2，全文 ≤2 次
- [ ] CTA 前已给足价值（读者主要疑问已回答）
- [ ] 无空泛 CTA（"Start your journey" / "Unlock your potential"）
- [ ] 无虚假承诺（"generate in seconds" 必须可达成）

#### 11. Slug & Evergreen Design

- [ ] 无年份
- [ ] 无数量/序数（top-5 / 7-ways）
- [ ] 无连续重复词（guide-guide / ai-ai）
- [ ] 无内部架构词（complete / ultimate / definitive / framework / strategy）
- [ ] 全小写 + 连字符（无下划线/大写/空格）
- [ ] ≤60 字符；人可读（"大声读"测试通过）
- [ ] 与 §2.8 反模式表对照：0 命中
- [ ] Nano Banana 新稿统一 `nano-banana-2-*` 前缀
- [ ] 30% 内容变化后 slug 仍然合适（语义余量原则）

#### 12. Cross-Article Consistency

- [ ] Canonical Concept Registry（§4.3）对照通过：每个引用概念用 canonical slug
- [ ] Hub-spoke 链接完整性：spoke 回链 hub；hub 链向所有 spoke
- [ ] 同 cluster 内无矛盾：文章 A 和文章 B 对同一模型能力的描述一致
- [ ] 跨篇产品描述一致性：Credits 表述统一、模型能力声明口径一致
- [ ] Cannibalization 检查：新文 targeting 的关键词不与现有文章 SERP 意图重叠 >50%

#### 13. Sensitive Content Compliance（Vofy 独有）

- [ ] 文章是否涉及 §1.3 五类敏感内容？
- [ ] 如涉及：FAQ 或开篇后是否有用途与授权声明？
- [ ] 是否使用了模板句（"Use only photos you own…"）？
- [ ] celebrity/政治类：是否标注 satire/editorial？
- [ ] IP 风格模仿类：是否声明 "非官方联名"、"风格参考"？
- [ ] 亲密/身体类：是否禁止 "冒充他人" 或 "医疗/身份验证用途"？

#### 14. Model Freshness（Vofy 独有）

- [ ] frontmatter `model_version_note` 已填且日期为审计当月
- [ ] 正文所有 Credits / 模型能力声明标注 "as of {month} {year}"
- [ ] 无写死的 "fastest / cheapest / always" 等时效敏感声明
- [ ] studio_url 参数在 vofy.art 现网已验证可用
- [ ] model id（§6.2）已在 Vofy 验证；未从本表硬编码到集成代码
- [ ] 如模型有已知的即将更新/弃用，正文提及 "check Vofy for latest version"

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
| 12. Cross-Article Consistency | Pass/Fail | |
| 13. Sensitive Content | Pass/Fail | |
| 14. Model Freshness | Pass/Fail | |
**Overall**: PASS | FAIL → {具体修复动作}
```

14 维全部 Pass → 进入 Phase 7 交付。任一维度 Fail → 标注具体修复动作，修复后重新过 Phase 6。

---

### Phase 7 — 交付

1. 写入 `vofy/blog/53-{slug}.md`
2. Article Brief 摘要 + SelfCheck 表（14 维全 Pass）
3. **templates 审核指令**（复制即用）：

```
请按 references/portable/final-audit.md 审核 vofy/blog/53-{slug}.md

项目配置：
- 品牌：Vofy
- 主域名：vofy.art
- 博客前缀：/blog/
- Pillar：按 cluster（如 gpt-image-2-guide）
- 受众：creators / marketers / tool-search visitors
- 禁止内链：404 studio/model/app 路径

要求：
1. 先过 01-publishability.md：独立成文 + P0 Gate (G1–G7)
2. 按 A–J 十维评分（参考 02–10 维度文档）
3. 输出 Source Map + SERP Fit
4. 如有多篇文章，检查跨篇一致性
5. 标记 P1/P2
```
4. 提示人类更新 `blog/README.md`

---

## §4 已有内容图谱

### 4.1 现网 slug 登记表（CMS · 本地无镜像）

**下一本地序号：53**

#### 本地稿（1）

| NN | 文件 | slug | 类型 | cluster | 状态 |
|----|------|------|------|---------|------|
| 52 | 52-introducing-vofy-ai-canvas.md | `introducing-vofy-ai-canvas` | Announcement | vofy-canvas | 草稿 |

#### 现网 CMS（约 59 篇 · 摘要见下）

#### nanobanana-2 簇（10）

| slug | 类型 | cluster |
|------|------|---------|
| `nano-banana-2-gemini-3-1-flash-image-generation` | Announcement | nanobanana-2 |
| `nanobanana-2-prompts-complete-guide` | PromptGuide | nanobanana-2 |
| `nano-banana-2-prompt-social-media-viral-guide` | PromptGuide | nanobanana-2 |
| `nano-banana-2-ecommerce-product-images` | PromptGuide | nanobanana-2 |
| `nano-banana-2-education-storytelling-prompts` | PromptGuide | nanobanana-2 |
| `nano-banana-2-photorealistic-image-generation` | PromptGuide | nanobanana-2 |
| `nano-banana-2-prompts-brand-marketing` | PromptGuide | nanobanana-2 |
| `nanobanana-2-creative-experimental-prompts` | PromptGuide | nanobanana-2 |
| `nanobanana-2-trump-image-generation-guide` | PromptGuide | nanobanana-2 |
| `nano-banana-2-vs-seedream-5-comparison` | Comparison | nanobanana-2 |

#### gpt-image-2 簇（5）

| slug | 类型 | cluster |
|------|------|---------|
| `gpt-image-2-guide` | ModelGuide | gpt-image-2 |
| `gpt-image-2-prompts-guide` | PromptGuide | gpt-image-2 |
| `gpt-image-2-vs-midjourney-comparison` | Comparison | gpt-image-2 |
| `gpt-image-2-vs-nano-banana` | Comparison | gpt-image-2 |
| `edit-images-with-gpt-image-2` | PromptGuide | gpt-image-2 |

#### kling-3-0 簇（4）

| slug | 类型 | cluster |
|------|------|---------|
| `best-kling-3-0-prompts` | PromptGuide | kling-3-0 |
| `best-kling-3-0-settings` | PromptGuide | kling-3-0 |
| `kling-3-0-image-to-video-guide` | AppHowTo | kling-3-0 |
| `kling-3-0-complete-guide` | ModelGuide | kling-3-0 |

#### seedance-2 簇（3）

| slug | 类型 | cluster |
|------|------|---------|
| `seedance-2-character-stability-basics` | PromptGuide | seedance-2 |
| `seedance-2-consistent-character-advanced-guide` | PromptGuide | seedance-2 |
| `seedance-2-prompt-guide-playbook` | PromptGuide | seedance-2 |

#### AppHowTo / 工具类（20）

| slug | 类型 |
|------|------|
| `ai-celebrity-selfie-generator` | AppHowTo |
| `ai-skin-enhancer-portrait-retouching-guide` | AppHowTo |
| `ai-haircut-virtual-try-on` | AppHowTo |
| `how-to-change-face-expression-with-ai` | AppHowTo |
| `how-to-change-eye-color-ai` | AppHowTo |
| `no-beard-filter-ai-guide` | AppHowTo |
| `ai-skin-color-changer` | AppHowTo |
| `ai-tankini-swimsuit-try-on` | AppHowTo |
| `piercing-filter-virtual-try-on-guide` | AppHowTo |
| `selfie-to-linkedin-headshot` | AppHowTo |
| `barbie-filter-pink-aesthetic-guide` | StyleGuide |
| `ai-baby-face-photo-generator` | AppHowTo |
| `ai-ninja-outfit-generator` | AppHowTo |
| `ai-green-screen-remover-guide` | AppHowTo |
| `remove-color-from-image` | AppHowTo |
| `how-to-remove-shadows-from-photos` | AppHowTo |
| `photo-to-line-drawing` | AppHowTo |
| `old-camera-filter-vintage-photo-generator` | AppHowTo |
| `cartoon-to-realistic-ai-transformation-guide` | AppHowTo |
| `warm-sunset-glow-photography-ai` | AppHowTo |

#### Style / 流行文化（4）

| slug | 类型 |
|------|------|
| `ghibli-style-image-generator-guide` | StyleGuide |
| `rick-morty-art-style-guide` | StyleGuide |
| `ai-south-park-character-creator-guide` | StyleGuide |
| `doodle-font-generator-spring-2026` | StyleGuide |

#### Campaign / 通用（11）

| slug | 类型 |
|------|------|
| `ai-couple-photoshoot-generator-romantic-photos` | Campaign |
| `10-best-prompts-photorealistic-ai-portraits` | PromptGuide |
| `how-to-create-photorealistic-product-images-nano-banana-2` | PromptGuide |
| `why-ai-images-look-fake-photorealistic-solutions` | PromptGuide |
| `april-fools-ai-prank-ideas-photos-videos` | Campaign |
| `easter-ai-image-prompts-bunnies-eggs-cards` | Campaign |
| `easter-church-graphics-holy-week` | Campaign |
| `mothers-day-ai-image-generator` | Campaign |
| `mothers-day-gpt-image-2-product-photos` | Campaign |
| `multilingual-mothers-day-campaign-ideas` | Campaign |
| `multilingual-mothers-day-marketing-assets` | Campaign |

#### Video / 动效（2 + 2026-05 新增 8）

| slug | 类型 | 备注 |
|------|------|------|
| `pet-fake-sleep-phone-video` | AppHowTo | |
| `vintage-pin-up-art-generator-guide` | StyleGuide | |
| `ai-kissing-video-generator` | AppHowTo | 2026-04-30 |
| `anime-live2d-video-generator` | AppHowTo | 2026-05-07 |
| `practical-guide-ai-art-styles` | PromptGuide | 2026-05-07 · slug 以 CMS 为准 |
| `live-photo-maker` | AppHowTo | 2026-05-08 |
| `memory-motion-video-generator` | AppHowTo | 2026-05-12 |
| `ai-hugging-video-generator` | AppHowTo | 2026-05-12 |
| `ai-money-rain-video-generator` | AppHowTo | 2026-05-12 |
| `ai-camera-movement-effect` | AppHowTo | 2026-05-12 · slug 以 CMS 为准 |

**现网合计约 59 篇**（51 来自 sitemap 2026-05-07 + 2026-05 增量）。

### 4.2 Hub-Spoke 结构

| cluster | Hub（canonical） | 优先补 spoke |
|---------|-----------------|--------------|
| `gpt-image-2` | `gpt-image-2-guide` | Credits 估算、更多 vs 对比 |
| `nanobanana-2` | `nano-banana-2-gemini-3-1-flash-image-generation` | 过时性修订、链 GPT Image 2 对比 |
| `kling-3-0` | `kling-3-0-complete-guide` | vs Seedance / vs Veo |
| `seedance-2` | `seedance-2-prompt-guide-playbook` | **三方对比**（缺口） |
| `grok-imagine` | *(缺失)* | ModelGuide + PromptGuide |
| `veo-3-1` | *(缺失)* | ModelGuide + Lite vs full |
| `vofy-brand` | *(缺失)* | what is Vofy / multi-model studio |
| `motion-control` | *(缺失)* | HowTo + Kling 2.6 专题 |
| `vofy-canvas` | `introducing-vofy-ai-canvas` | Canvas workflow 教程（spoke） |

### 4.3 Canonical Concept Registry

| 概念 | Canonical slug |
|------|-----------------|
| GPT Image 2 定义 | `gpt-image-2-guide` |
| GPT Image 2 Prompt 框架 | `gpt-image-2-prompts-guide` |
| Nano Banana 2 发布解读 | `nano-banana-2-gemini-3-1-flash-image-generation` |
| Seedance 2 角色一致性 | `seedance-2-consistent-character-advanced-guide` |
| Kling 3.0 完整指南 | `kling-3-0-complete-guide` |
| 伪真实感修复 | `why-ai-images-look-fake-photorealistic-solutions` |
| Vofy Canvas 定义 / 上线 | `introducing-vofy-ai-canvas` |

引用方式：1–2 句 + internal link，不在 spoke 完整重定义。

---

## §5 关键词速查

### 5.1 P0 — 必须主打

| 关键词 | intent | 建议类型 | 目标链 |
|--------|--------|---------|--------|
| Vofy / AI creative studio | 品牌 | Announcement/ModelGuide | `/` |
| GPT Image 2 | 模型 | ModelGuide + PromptGuide | studio + `/models/` |
| Nano Banana 2 / NanoBanana 2 | 模型 | 同上 | `/models/nanobanana/2` |
| Seedance 2 | 视频 | ModelGuide + PromptGuide | video studio |
| Kling 3.0 | 视频 | ModelGuide + PromptGuide | video studio |
| AI image generator online | 品类 | Comparison | `/studio/create/image` |
| AI video generator | 品类 | Comparison | `/studio/create/video` |

### 5.2 P1 — 模型与对比

| 关键词 | 建议类型 |
|--------|---------|
| GPT Image 2 vs Midjourney | Comparison |
| Seedance 2 vs Kling 3.0 | Comparison |
| Veo 3.1 Lite | ModelGuide |
| Grok Imagine Image | ModelGuide |
| Motion control AI video | AppHowTo |
| AI inpainting | AppHowTo |
| Which AI model should I use | Comparison（决策树） |

### 5.3 P2 — Apps 长尾（Sample）

| 关键词 | 建议类型 | app 方向 |
|--------|---------|---------|
| AI hair color filter | AppHowTo | hair-color |
| LinkedIn headshot AI | AppHowTo | linkedin-headshot |
| remove background product photo | AppHowTo | remove-bg |
| AI kissing video | AppHowTo | kissing-video |
| Ghibli style photo | StyleGuide | ghibli preset |
| memory motion old photo | AppHowTo | memory-motion |

### 5.4 竞品截流（Comparison 素材）

Leonardo.ai · Runway · Pika · Luma Dream Machine · fal · ChatGPT/DALL-E playground · Google AI Studio

对比须标注 **as of {date}**；定价/档位以各官方为准。

---

## §6 产品事实表

### 6.1 Studio 模块

| 模块 | studio 入口 | 说明 |
|------|------------|------|
| Create Image | `/studio/create/image?mode=create&model={id}` | 文生图/编辑 |
| Create Video | `/studio/create/video?mode=create&model={id}` | 短视频 |
| Motion Control | `/studio/create/video?mode=motion-control` | 参考视频驱动 |
| Inpaint | `/studio/create/image?mode=inpaint` | 局部重绘（以现网为准） |
| AI Style | `...&workspace=styles` | 风格预设 |

### 6.2 模型 → studio / models 映射（撰写内链用）

| 公开名称 | model id（studio） | models 路径（若存在） |
|---------|-------------------|---------------------|
| GPT Image 2 | `gpt-image-2` | `/models/openai/gpt-image-2` |
| Nano Banana 2 | `gemini-3.1-flash-image-preview` | `/models/nanobanana/2` |
| Seedance 2.0 | `seedance-2.0` | `/models/bytedance/seedance-2` |
| Kling 3.0 | `kling-3.0` | `/models/kling/3` |
| Veo 3.1 Lite | `veo-3.1-lite` | `/models/google/veo-3-1-lite` |
| Grok Imagine Image | `grok-imagine-image` | 以现网为准 |
| Seedream 5.0 Lite | `seedream-5.0-lite` | 以现网为准 |
| Sora 2 | `sora-2` | 以现网为准；写前确认是否仍上线 |

**规则**：发布前在 vofy.art 验证 model 参数；勿从本表硬编码到集成代码。

### 6.3 Credits 撰写规则

- 可引用首页示例「~2.5 Credits per AI Image」作**参考**，须加 **rates vary by model, resolution, and duration**
- 禁止「10 videos = exactly X credits」除非有官方计算器或文档
- Campaign 文可写「estimate workflow」定性描述
- 模型中提及 Credits 时标注 "as of {month} {year}"

### 6.4 禁止写入（除非官方更新）

- 未验证的「fastest / cheapest in the industry」
- 第三方模型独家 partnership（除非 What's New 明确）
- 具体 MAU/ARR unless sourced

---

## §7 README 维护提醒

成稿后人类更新：

1. `vofy/blog/README.md` — 「本目录文件」表
2. `vofy/vofy-blog-inventory-zh.md` — 新 slug / 缺口状态（可选）
3. Skill §4.1 — bump `metadata.version` 若登记表变更

---

## §8 Voice 与 Conclusion 规范

### 8.1 正向 Voice

| 维度 | 要求 |
|------|------|
| Creator-first | 具体场景：Reels cover、product flat lay、TikTok hook |
| Practical | 可复制的 prompt / 步骤 / 设置名 |
| Honest about limits | 承认某模型在 text-in-image、时长等方面的 trade-off |
| Fast-paced but not hype | 可用「fast」「cinematic」；禁 revolutionary/game-changing |
| Credits-transparent | 提及 Credits 时加「rates vary by model and resolution」 |

### 8.2 禁止

- revolutionary · game-changing · unlock · seamless · magic · best-in-class · only solution
- Vendor puffery：only platform / unbeatable
- Fake benchmarks：无来源的「beats Midjourney every time」
- Misleading UGC claims：虚构 before/after
- IP overreach：「official Ghibli partnership」
- 空泛句：In today's world / Let's dive in / It is important to note that / Without further ado / Here's the thing

### 8.3 漏斗透明度按类型

| 类型 | 标准 |
|------|------|
| Comparison / ModelGuide | 漏斗可透明（读者知道是产品对比/评测文）。disclosure 在开篇标注。 |
| PromptGuide | 漏斗应适度。Prompt 框架教学 >70%；Vofy studio 实操在全文后 30%。 |
| AppHowTo / StyleGuide | 漏斗可明显——读者意图就是使用工具。 |
| Campaign / Announcement | 漏斗可透明——读者知道是品牌/营销内容。 |

### 8.4 按类型产品策略

| 类型 | 产品策略 |
|------|---------|
| ModelGuide | studio 操作用法在 §4 "Quick Start" 出现；前 3 节建立独立价值 |
| PromptGuide | Prompt 框架教学 70%+；Vofy studio 实操在 "Copy-Ready Examples" |
| AppHowTo / StyleGuide | 三步框架为主；产品自然出现 |
| Comparison | Comparison 表一行 + studio 链；不做「Vofy 唯一推荐」 |
| Campaign | 产品作为创作工具自然出现 |

---

## §9 与 templates / README 分工

| 阶段 | 工具 |
|------|------|
| 选题 → Brief → Outline → Draft → SelfCheck（14 维） | **本 Skill** |
| 发布前终审、P0 Gate + 十维评分 + Source Map + SERP Fit | **`references/portable/final-audit.md`** + `source-map-template.md` + `serp-fit-template.md` |
| Phase 0R Research | **`references/portable/research-triangle.md`** |

Phase 3 已内联 title/description/slug 规则；无需读取 vofy-keywords.md 等外部文档。

---

## §10 Mini Example — PromptGuide Brief + 开篇样段

### 10.1 Brief 摘要

**以 `grok-imagine-image-prompts` 为参照**。

```markdown
## Article Brief
**Working title**: How to Write Better Grok Imagine Image Prompts — A Framework
**Primary keyword**: Grok Imagine Image prompts
**Article type**: PromptGuide
**Templates category**: Tutorial
**Search intent**: Informational
**Reader stage**: Tutorial
**Target audience**: Social creators testing new image models on Vofy
**Word count target**: 2200–2800
**Cluster role**: Spoke (hub: grok-imagine 待写 ModelGuide)
**Differentiation angle**: Copy-ready templates for portrait + product + text-in-image, tied to Vofy studio settings
**Competitor gap**: SERP contains mostly vibe-based prompt lists without structured framework
**Canonical concepts to reference**: gpt-image-2-prompts-guide (prompt framework, 1 sentence + link)
**KEEP/MERGE**: KEEP
**Disclosure needed**: Recommended
```

### 10.2 开篇样段（英文，勿直接当终稿）

> Most Grok Imagine Image prompts fail for the same reason: they describe a vibe, not a shot. If you are trying to turn a selfie into a cinematic portrait or a product label into a clean packshot, you need subject, medium, lighting, and constraint language in the same prompt — not just "make it look amazing."
>
> This guide gives you a reusable framework, copy-ready templates, and troubleshooting tips for Grok Imagine Image on Vofy **as of June 2026**. For model specs and when to pick Grok over GPT Image 2 or Nano Banana 2, see the related guides below.

### 10.3 Conclusion 多样结尾示例

每篇 conclusion 用不同的收束方式（避免跨篇模板化）：

- **预测**: "As text-in-image models improve, prompt frameworks will likely shift from describing what to see toward describing what NOT to see — making constraint language the real differentiator."
- **未解问题**: "Whether the same prompt framework transfers equally well to video generation models like Kling 3.0 and Seedance 2 remains an open question — we'll test that in a follow-up comparison."
- **具体警告**: "Don't confuse prompt length with prompt quality. A 50-word prompt that nails subject, medium, and lighting will outperform a 200-word prompt that describes a mood."

### 10.4 利益声明示例

**Comparison 文开篇后**：

> **Disclosure**: Vofy is an all-in-one AI creative studio. This article compares multiple AI image generation tools, including workflows available on Vofy, to help you choose the right one for your needs.

**AppHowTo 文开篇后**：

> **Disclosure**: This tutorial uses Vofy, an all-in-one AI creative studio, as the demonstration tool. The steps apply to the platform as of June 2026 — interfaces may evolve.

---

*vofy-blog-article · v2.1.0 · 2026-06-19 · fully self-contained · references/portable/*
