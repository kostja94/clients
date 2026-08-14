---
name: moras-meta-title-description
description: Write or optimize meta title and meta description for ANY moras.ai page. HARD RULE every title and description must strongly match that page's target keywords and theme (not generic copy). Self-contained; covers homepage, /tiktok-video-generator, verticals, /blog, tool pages, legal.
metadata:
  version: 1.2.1
  project: moras.ai
  self-contained: true
  primary-audience: TikTok Shop affiliates
  brand-suffix: "| Moras"
  scope: all page types — live, preview, and planned
  complements: moras-blog-article
---

# Moras Meta Title & Description

为 **https://moras.ai** 编写或优化 `<title>` 与 `<meta name="description">`。**硬性要求：每条 title 和 description 必须与该 URL 对应页面的目标关键词和页面主题强相关**——不可用泛化 SaaS 话术、不可套模板而不改品类/场景词、不可写与页面 H1/正文无关的 metadata。

**本文件自包含**：Agent 只需读取本 skill，无需访问仓库内其他文档。

**市场范围**：仅 **美区 TikTok Shop**、**英文（en）**；当前无多语言路径，勿写其他区域或平台为主词。

**主受众**：**带货联盟客（affiliate creators）**——高佣达人、副业联盟客、无样品/少实拍的内容创作者。**seller / merchant / brand** 仅作次要受众或 P2，**不可**在 title 中取代 affiliate 作为主称谓。

**品牌后缀（硬性）**：凡含品牌的 title，统一置尾为 **`| Moras`**（竖线 + 空格 + Moras）。**禁止** `— Moras`、`| K2 Lab`、`| K2LAB`。博客 editorial title 通常不加品牌；法务页可用 `Privacy Policy | Moras`。

---

## 如何使用（分发给他人）

1. 将本文件复制到 Agent 的 skills 目录，例如：
   - Cursor: `.cursor/skills/moras-meta-title-description/SKILL.md`
   - Claude Code: `.claude/skills/moras-meta-title-description/SKILL.md`
2. 对 Agent 说：「按 moras-meta-title-description skill，为 [URL 或页面类型] 写 title 和 description」
3. 批量任务示例：「按 skill 为 `/tiktok-video-generator/skincare` 和 `/blog/faceless-tiktok-shop-videos` 写 title + description」

**Agent 执行时**：直接输出 metadata 方案；首次可用 1 句说明范围，后续跳过前言。若 URL 不在清单中，走 §任意页面 Fallback。**输出前必须计字符**（§长度）；标注页面 §上线状态。

---

## 站点页面清单与上线状态（必读）

本 skill 覆盖 **moras.ai 全部现有 + 规划中的可索引页面**，并非所有 path 均已上线。写 metadata 时：

| 状态 | 含义 | Agent 做法 |
|------|------|------------|
| **live** | 已在 moras.ai 可访问 | 可对齐线上 H1/首屏；输出 Notes 标 `live` |
| **preview** | 仅在预览域（如 moras-navy.vercel.app） | 按模板写 metadata；Notes 标 `preview` |
| **planned** | 路径/栏目已规划，页面未建 | **仍须写 metadata**（上线即用）；从本章 P1/P2 表写；Notes 标 `planned` |
| **anchor** | 首页内锚点，无独立 URL | 通常不写独立 title；若未来拆页，用对应章节 |
| **noindex** | 应用内/后台 | 不写 SEO metadata |

### 当前状态快照（2026-06-15，上线后请更新）

| 路径 | 类型 | 状态 |
|------|------|------|
| `/` | 首页 | **live** |
| `/terms` | 法务 | **live** |
| `/privacy` | 法务 | **live** |
| `/blog/how-to-make-money-on-tiktok` 等 8 篇 | 博客 | **planned**（文稿已有，主站待部署） |
| `/blog` | 博客聚合 | **planned** |
| `/tiktok-video-generator` | TVG Hub | **preview** |
| `/tiktok-video-generator/mattress` | TVG Vertical | **preview** |
| `/tiktok-video-generator/{slug}`（除 mattress） | TVG Vertical ×19 | **planned** |
| `/product-research` | 工具 | **planned**（页脚入口，无独立页） |
| `/hashtag-generator` | 工具 | **planned** |
| `/caption-generator` | 工具 | **planned** |
| `/pricing` | 营销 | **anchor**（首页 `#pricing` 区块，无独立 URL） |
| `/download` | 营销 | **anchor**（首页 CTA / App Store，无独立 URL） |
| `/#features` `/#showcase` 等 | 首页锚点 | **anchor** |

**规则**：

1. **planned / preview 页面同样适用本 skill**——用清单 P1/P2 + 页面类型模板写 metadata，勿因「未上线」而写泛化文案。
2. 若用户给的是 **规划 path**，在 Output 的 **Notes** 标 `planned` 或 `preview`，**不要**假装已核对线上 DOM。
3. 若未来页面上线后 H1/正文与清单不一致，**以实际上线内容为准**更新 P1/P2，再写 metadata。
4. 新增 path（`/docs`、`/comparison` 等）→ 走 §任意页面 Fallback，并建议回写本章状态表。

---

## 页面类型路由（任意 URL 第一步）

给定 URL 后，按 path 匹配：

| 路径匹配 | 类型 | 跳转章节 |
|----------|------|----------|
| `/` | 首页 | §首页 |
| `/tiktok-video-generator` | TVG Hub | §TikTok Video Generator Hub |
| `/tiktok-video-generator/{slug}` | TVG Vertical | §TikTok Video Generator Vertical |
| `/blog/{slug}` 或 slug 含 `/blog/` | 博客文章 | §博客 |
| `/blog` | 博客聚合 | §首页、聚合 |
| `/product-research` | 选品工具页 | §工具页 |
| `/hashtag-generator` | Hashtag 工具页 | §工具页 |
| `/caption-generator` | Caption 工具页 | §工具页 |
| `/pricing` | 定价 | §营销页 |
| `/download` | 下载 | §营销页 |
| `/terms` | 服务条款 | §法务页 |
| `/privacy` | 隐私政策 | §法务页 |
| 首页锚点 `#features` `#showcase` `#pricing` 等 | 单页区块 | §首页锚点（通常不改独立 metadata） |
| 其他可索引 path | 未知页 | §任意页面 Fallback |

**示例**：
- `https://moras.ai/tiktok-video-generator/mattress` → TVG Vertical（mattress 品类）
- `https://moras.ai/blog/faceless-tiktok-shop-videos` → 博客（不出镜带货视频）
- `https://moras.ai/` → 首页

---

## Scope

| 元素 | 职责 |
|------|------|
| **Title tag** | **页面主题 + P1 关键词** 前置；工具/Vertical 页用冒号或 em dash + 动作/受众句；每页唯一；品牌置尾 |
| **Meta description** | **页面主题下的 P2** + 该页独有场景/品类/工作流 + CTA；不与 title 重复同一句 |
| **不覆盖** | 正文、H2 结构、Schema、og:*、hreflang、robots |

---

## 核心原则：页面主题与关键词强相关（最高优先级）

**每条 metadata 都是「这一页」的 SERP 承诺，不是全站通用广告语。**

| 规则 | 说明 | 反例 |
|------|------|------|
| **一页一词一组** | title/description 的 P1、P2 必须来自 **该 URL 所在章节清单** 或 **该页 H1/首屏主题** | 所有 Vertical 都写 `Best AI Video Generator` |
| **主题词入 title** | 页面核心主题（品类/persona/文章题/工具名）必须在 title 中 **显性出现** | `/tiktok-video-generator/skincare` 写 `AI Video Generator for Sellers`（缺 skincare；且 sellers 非主受众） |
| **description 展开主题** | description 写 **该页独有的品类信号、佣金区间、工作流、输出**，不是换说法重复 title | skincare 页只写 generic `product videos` 而不提 Korean skincare / GRWM |
| **禁止套娃** | 不可把 A 页推荐 title 改几个词用于 B 页；批量任务时 **逐 URL 核对 P1/P2 表** | mattress 与 toiletry-bag 用同一句 description |
| **与 H1 同主题** | 用户点进 SERP 后，H1 与 title 应感觉在讲 **同一件事**；可更短，不可更偏 | title 讲 mattress affiliate，H1 却是 generic video tool |
| **美区限定** | 涉及 TikTok Shop 的页，description 宜含 **US TikTok Shop** 或等价语义（勿写全球/多市场） | 写 `TikTok Shop affiliates worldwide` |
| **联盟客优先** | title/description 默认面向 **affiliate**（commission、showcase、link-to-video）；seller 仅当页面明确讲开店/上架 | 全站 title 写 `for sellers` 而丢 affiliate |

**自检问句（输出前必答）**：

1. 若去掉品牌名，title 能否让人猜出 **这是哪一页**？（不能 → 重写）
2. description 是否至少包含 **1 个该页专属主题词**（非全站共用词）？（没有 → 重写）
3. 该页清单中的 P1 是否在 title 中出现？P2 是否在 description 中出现？（缺 → 补）
4. **title 是否在 50–60 字符内？description 是否在 150–160 字符内？**（超 → 按 §长度 缩短后重计）

---

## 产品上下文（内嵌，勿外查）

**Moras** 是面向 **美区 TikTok Shop 带货联盟客** 的 **AI 内容电商 Agent OS**（B2B2C / 订阅 + 分成）。

| 项 | 内容 |
|----|------|
| **一句话** | 帮联盟客从选品到可购短视频成片，Moras 用多代理编排（A2A）驱动 TikTok Shop 佣金增长 |
| **两项核心能力** | ① **AI 选品**（美区 TTS 数据驱动高佣/趋势商品）；② **TT 商品视频生成**（商品链接/卖点 → 竖屏可购短视频，批量/多版本） |
| **ICP（主）** | **TikTok Shop 联盟客**、高佣带货达人、副业 side-hustle affiliate、无样品/少实拍 KOC |
| **ICP（次）** | 美区卖家/品牌、MCN/机构（套餐含 MCN 档，metadata 仍以 affiliate 工作流为主轴） |
| **定位** | 比通用 AI 视频工具更专于 **联盟客带货闭环**（选品→成片→挂链→佣金）；比纯数据分析工具多 **成片 + 飞轮** |
| **技术叙事** | Orchestrator + 11 专精代理 + A2A 协议；选品→成片→数据回灌飞轮 |
| **定价（以官网为准）** | **Pro** ~$1000/mo（600 条/月）；**Agency Partner** ~$20/mo + 50% commission；**Managed Service** $0 base + 70% commission |
| **站点** | https://moras.ai |
| **公司背书** | K2 Lab / K2LAB（页脚 `Powered by K2 lab`） |
| **语言/市场** | 英文；**仅美区 TikTok Shop** |
| **Voice** | 直接、结果导向、**联盟客/创作者**友好；优先用 affiliates, commission, showcase, product link, shoppable, viral, hook；seller 次之 |
| **Avoid** | 企业 jargon 堆砌、未验证 GMV 承诺、暗示 TikTok 官方合作 |

**可引用的 Proof points**（description 可选用，勿夸大）：

- Wall of Love 用户证言（个案 GMV/佣金，**须标注为 testimonial 语境，非保证**）
- ~3 min per video、3 cuts per brief、600 videos/mo（Pro 档，以官网为准）
- iOS App「Moras: Create & Earn with AI」
- Eleven specialized agents（官网叙事）

**禁止写入 metadata**（除非用户明确提供已核实数据）：

- 普适 GMV/收入保证（如「月入 $10k」作承诺）
- 「TikTok 官方合作 / 认证工具」
- SOC 2、端到端加密等未证实合规 claim
- 非美区市场覆盖（UK/EU/SEA 等）
- 具体竞品准确率对比数字
- 用户证言中的品牌误拼 **Morris**（对外统一 **Moras**）

**合规句**（Vertical / 工具页 description 可选用）：

- Moras is not affiliated with TikTok or ByteDance.
- US TikTok Shop only.
- Results vary; testimonial figures are not typical guarantees.

---

## 双核心词策略（全站 SEO 基石）

| 意图 | 核心词 | 主承接 URL |
|------|--------|------------|
| **成片** | AI TikTok video generator, TikTok Shop video generator, shoppable video AI | `/`、`/tiktok-video-generator`、`/tiktok-video-generator/{slug}` |
| **选品** | TikTok Shop product research, AI product research TikTok Shop, winning products AI | `/product-research`、`/blog/tiktok-product-research` |

**规则**：两意图不可混为一谈。Hub / Vertical 页不以「product research」为主词；选品工具页不以「video generator」为主词（可作 P2）。

**第三意图（品牌/定位）**：`AI commerce producer`, `TikTok Shop affiliate tools`, `TikTok Shop side hustle` → 首页、定价、下载。

---

## 长度（硬性，输出前必计字符）

Google 按像素截断；下表为 **英文字符** 近似上限。Agent **必须在 Output 中标注实际字符数**；超限视为未完成。

| 元素 | 目标范围 | 硬上限 | 超出时处理顺序 |
|------|----------|--------|----------------|
| **Title**（含 `\| Moras`） | **50–60** | 60 | ① 缩短 em dash 后修饰语 ② 用 §紧凑 Title ③ 不可删 P1/品类/affiliate |
| **Meta description** | **150–160** | 160 | ① 删冗余形容词 ② 缩短 CTA 前从句 ③ 不可删 P2/品类专属词 |
| **博客 title** | 45–60 | 65 | editorial 可略长，但仍避免 SERP 截断 |
| **博客 description** | 140–160 | 160 | 同 meta description |
| **法务 description** | 50–120 | 120 | 无 CTA |

### Title 紧凑模式（品类名较长时，>58 chars 触发）

默认模式超长时，改用：

```
{Category} TikTok Videos for Affiliates — AI Generator | Moras
```

或再短：

```
AI TikTok Generator for {Category} Affiliates | Moras
```

**禁止**：为凑字数删掉 `{Category}`、`Affiliates`、`| Moras`。

### Description 紧凑公式（控制在 150–160）

```
{P2 短语，≤12 词}. Shoppable {category} videos from affiliate links on US TikTok Shop. Download Moras.
```

CTA 统一用 `Download Moras.`（17 chars，含句号）——预留进 160 上限。

### 字符计数示例（合规）

| 页面 | Title | chars | Description | chars |
|------|-------|-------|-------------|-------|
| 首页 | `TikTok Shop Affiliate Videos — AI Commerce Producer \| Moras` | 58 | `Automate shoppable TikTok videos for US affiliates—from AI product picks to link-to-video edits, no filming. Hooks, captions, commission tags. Download Moras.` | 155 |
| Hub | `AI TikTok Video Generator for TikTok Shop Affiliates \| Moras` | 55 | `Turn affiliate product links into shoppable US TikTok Shop videos—hooks, voiceover, captions, and commission tags in minutes. Download Moras.` | 138 |
| skincare | `AI TikTok Generator for Skincare Affiliates \| Moras` | 50 | `Korean skincare hooks and GRWM angles from affiliate product links—shoppable videos for US TikTok Shop in minutes. Download Moras.` | 125 |

*上表 description 偏短时可补 P2 至 150–160，但不可超 160。*

---

## Title 结构原则

### TikTok Video Generator Vertical（默认：for {category} affiliates）

面向 **Transactional 意图**——联盟客搜具体品类 + 视频工具。**Title ≤60 chars**。

```
AI TikTok Generator for {category} Affiliates | Moras
```

品类名较长时（§长度 紧凑模式）：

```
{Category} TikTok Videos for Affiliates — AI Generator | Moras
```

| 原则 | 说明 | 反例 |
|------|------|------|
| 品类前置 | `{category}` 必须在 title 前半 | `AI Video Tool for E-commerce` |
| 受众明确 | **默认** `for {category} affiliates`；可用 `affiliate creators` | 写 `for sellers` / `for merchants` 作主称谓 |
| 品牌 | **统一** `\| Moras` 置尾 | `— Moras`、`\| K2 Lab`、混用多种后缀 |
| Title ≠ Description | Title = P1 + 品类 + affiliate | Description = P2 + 佣金/hook/工作流 |

### TVG Hub（broad 词）

```
AI TikTok Video Generator for TikTok Shop Affiliates | Moras
```

### 首页（em dash + 定位，≤60 chars）

```
{Primary Keyword} — {Value Prop for Affiliates} | Moras
```

示例 (58)：`TikTok Shop Affiliate Videos — AI Commerce Producer | Moras`

### 工具页（≤60 chars）

```
TikTok Shop {Tool} for Affiliates — AI | Moras
```

### 博客（editorial，通常不加品牌后缀）

```
{Topic Title}: {What reader gets} ({Year})
```

或 how-to / guide 句式。若加品牌，仍用 `{Title} | Moras`。

### 法务页

```
{Privacy Policy | Terms of Service} | Moras
```

---

## Title vs Description 分工

| 元素 | 写什么 | 不写什么 |
|------|--------|----------|
| **Title** | **该页 P1 + 该页主题词** + 受众/动作 | 其他页面的 P1/P2；泛类目标签 |
| **Description** | **该页 P2 + 该页场景/品类信号/工作流** + CTA | 与 title 同句；其他页主题词 |

两者都必须 **强相关于同一页面主题**——title 锁定「搜什么进来」，description 锁定「这一页具体解决什么」。

### Title / Description 关键词变体分工（推荐）

| 位置 | 推荐句式 | 示例 |
|------|----------|------|
| **Title** | `AI TikTok video generator for {category} affiliates` | 名词/工具标签 + 品类 + affiliate |
| **Description** | `generate shoppable TikTok videos from affiliate product links` / `turn {category} showcase picks into commission videos` | 动词短语变体 |

**规则**：

1. Title 用 generator / producer / research 等 **名词标签**。
2. Description 用 generate / turn / automate / discover 等 **动词变体**，勿整句重复 title。
3. **变体须对应该页主题**：skincare → `Korean skincare`, `GRWM`；mattress → `bed in a box`, high AOV。
4. CTA 末尾：`Download Moras.` 或 `Get started with Moras.`（**勿写** `Free to try` 除非该页确有免费档且已核实）。

**成对示例**：

| 页面 | Title | Description |
|------|-------|-------------|
| /tiktok-video-generator/skincare | `AI TikTok Generator for Skincare Affiliates \| Moras` (50) | `Korean skincare hooks and GRWM angles from affiliate links—shoppable videos for US TikTok Shop in minutes. Download Moras.` (125) |
| /product-research | `TikTok Shop Product Research for Affiliates — AI \| Moras` (52) | `Find high-commission US TikTok Shop products—trend signals, commission fit, and content gaps before you post affiliate videos. Download Moras.` (130) |
| / | `TikTok Shop Affiliate Videos — AI Commerce Producer \| Moras` (58) | `Automate shoppable TikTok videos for US affiliates—from AI product picks to link-to-video edits, no filming. Hooks, captions, commission tags. Download Moras.` (155) |

---

## 全站 URL 模式

| 类型 | 模式 | 规模 | 典型状态 |
|------|------|------|----------|
| 首页 | `/` | 1 | live |
| TVG Hub | `/tiktok-video-generator` | 1 | preview |
| TVG Vertical | `/tiktok-video-generator/{slug}` | 20（可扩展） | 1 preview + 19 planned |
| 博客 | `/blog/{slug}` | 8+（动态扩展） | planned |
| 工具页 | `/product-research`, `/hashtag-generator`, `/caption-generator` | 3 | planned |
| 营销独立页 | `/pricing`, `/download` | 0–2 | anchor（当前为首页区块） |
| 法务 | `/terms`, `/privacy` | 2 | live |
| 首页锚点 | `/#features`, `/#pricing` 等 | — | anchor，无独立 metadata |

**勿为以下路径写 SEO metadata**（若存在且 noindex）：`/app/*`, `/auth/*`, `/admin/*`, 预览域内部页

---

## 首页 `/`（live）

- **P1**: AI commerce producer, TikTok Shop affiliate video, AI TikTok video generator
- **P2**: product picks to shoppable video, multi-agent workflow, no filming
- **Title** (58): `TikTok Shop Affiliate Videos — AI Commerce Producer | Moras`
- **Description** (155): `Automate shoppable TikTok videos for US affiliates—from AI product picks to link-to-video edits, no filming. Hooks, captions, commission tags. Download Moras.`

**备选 Title** (52)：`AI Commerce Producer for TikTok Shop Affiliates | Moras`

**首页 vs Hub cannibalization**：首页打 **品牌 + 双能力总览**；Hub 打 **TikTok video generator** 类目词。

---

## 首页锚点（§营销区块）

单页应用内锚点 **通常无独立 `<title>`**；若未来拆为独立 URL，按下列 P1/P2：

| 区块 | P1 | Description 角度 |
|------|-----|------------------|
| Features | TikTok Shop affiliate AI tools, agent OS | 选品 + 成片双能力（联盟客工作流） |
| Showcase | shoppable video examples | Made With Moras 联盟客案例 |
| Wall of Love | TikTok Shop affiliate reviews | 证言个案，非收益保证 |
| Pricing | Moras pricing, TikTok Shop affiliate plans | Pro / Agency / Managed 档摘要 |
| Download | Download Moras app | iOS + 联盟客成片入口 |

---

## 营销页

> **当前**：Pricing / Download 为首页 **anchor**，无独立 URL。下表供 **未来拆页** 或用户明确给 path 时使用。

| URL | 状态 | P1 | Title 示例 (chars) | Description 要点 (≤160) |
|-----|------|-----|-------------------|-------------------------|
| /pricing | anchor | Moras pricing, TikTok Shop affiliate plans | `Moras Pricing — TikTok Shop Affiliate Plans \| Moras` (48) | 三档摘要；价格以官网为准 |
| /download | anchor | Download Moras, Moras app | `Download Moras — TikTok Shop Affiliate Video App \| Moras` (52) | iOS；link-to-video；US affiliates |

---

## TikTok Video Generator Hub `/tiktok-video-generator`（preview）

- **P1**: AI TikTok video generator, TikTok Shop affiliate video generator
- **P2**: affiliate product link to shoppable video, hooks, voiceover, captions
- **Title** (55): `AI TikTok Video Generator for TikTok Shop Affiliates | Moras`
- **Description** (138): `Turn affiliate product links into shoppable US TikTok Shop videos—hooks, voiceover, captions, and commission tags in minutes. Download Moras.`

**Hub vs Vertical**：Hub 吃 broad affiliate 词；Vertical 吃 `{category} affiliates` long-tail。**禁止** Hub description 罗列具体品类替代 Vertical 页。

---

## TikTok Video Generator Vertical 完整清单（20 页，planned + preview）

URL 基准：`https://moras.ai/tiktok-video-generator/{slug}`

**Title 模式（默认，计字符 ≤60）**：

```
AI TikTok Generator for {displayName} Affiliates | Moras
```

品类名较长（如 Cleaning gadgets、Home organization、Teeth whitening）→ 用紧凑模式：

```
{Category} TikTok Videos for Affiliates — AI Generator | Moras
```

**Description 公式（150–160 chars）**：

```
{P2 短语}. Shoppable {category} videos from affiliate links on US TikTok Shop. Download Moras.
```

| slug | displayName | 状态 | P1 | P2（description） | 推荐 Title |
|------|-------------|------|-----|-------------------|------------|
| mattress | Mattress | preview | AI TikTok generator for mattress affiliates | bed in a box unboxing, high AOV, high commission | `AI TikTok Generator for Mattress Affiliates \| Moras` |
| skincare | Skincare | planned | AI TikTok generator for skincare affiliates | Korean skincare, GRWM, glass skin | `AI TikTok Generator for Skincare Affiliates \| Moras` |
| supplements | Supplements | planned | AI TikTok generator for supplement affiliates | magnesium/wellness, claim-safe hooks | `AI TikTok Generator for Supplement Affiliates \| Moras` |
| cleaning-gadgets | Cleaning gadgets | planned | AI TikTok generator for cleaning gadget affiliates | CleanTok, before/after demos | `CleanTok TikTok Videos for Affiliates — AI Generator \| Moras` |
| kitchen-gadgets | Kitchen gadgets | planned | AI TikTok generator for kitchen gadget affiliates | one-shot demo, kitchen hacks | `Kitchen Gadget TikTok Videos for Affiliates — AI Generator \| Moras` |
| lip-gloss | Lip gloss | planned | AI TikTok generator for lip gloss affiliates | swatch on camera, GRWM lip | `AI TikTok Generator for Lip Gloss Affiliates \| Moras` |
| toiletry-bag | Toiletry bag | planned | AI TikTok generator for toiletry bag affiliates | pack with me, travel organizer | `Toiletry Bag TikTok Videos for Affiliates — AI Generator \| Moras` |
| collagen | Collagen | planned | AI TikTok generator for collagen affiliates | collagen peptides, skin transformation | `AI TikTok Generator for Collagen Affiliates \| Moras` |
| teeth-whitening | Teeth whitening | planned | AI TikTok generator for teeth whitening affiliates | whitening strips before/after | `Teeth Whitening TikTok Videos for Affiliates — AI Generator \| Moras` |
| phone-case | Phone case | planned | AI TikTok generator for phone case affiliates | MagSafe, drop-test unboxing | `AI TikTok Generator for Phone Case Affiliates \| Moras` |
| shapewear | Shapewear | planned | AI TikTok generator for shapewear affiliates | fajas try-on, occasion styling | `AI TikTok Generator for Shapewear Affiliates \| Moras` |
| pet-products | Pet products | planned | AI TikTok generator for pet product affiliates | pet reaction videos | `Pet Product TikTok Videos for Affiliates — AI Generator \| Moras` |
| home-organization | Home organization | planned | AI TikTok generator for home organization affiliates | closet makeover, small-space | `Home Organization TikTok Videos for Affiliates — AI Generator \| Moras` |
| vacuum | Vacuum | planned | AI TikTok generator for vacuum affiliates | cordless vacuum satisfying clean | `AI TikTok Generator for Vacuum Affiliates \| Moras` |
| led-face-mask | LED face mask | planned | AI TikTok generator for LED face mask affiliates | LED light therapy GRWM | `LED Face Mask TikTok Videos for Affiliates — AI Generator \| Moras` |
| hair-growth | Hair growth | planned | AI TikTok generator for hair growth affiliates | hair serum, before/after | `AI TikTok Generator for Hair Growth Affiliates \| Moras` |
| perfume | Perfume | planned | AI TikTok generator for perfume affiliates | perfume dupes, scent try-on | `AI TikTok Generator for Perfume Affiliates \| Moras` |
| protein-snacks | Protein snacks | planned | AI TikTok generator for protein snack affiliates | high-protein taste test | `Protein Snack TikTok Videos for Affiliates — AI Generator \| Moras` |
| makeup-tools | Makeup tools | planned | AI TikTok generator for makeup tool affiliates | brush/sponge comparison | `Makeup Tool TikTok Videos for Affiliates — AI Generator \| Moras` |
| sleep-products | Sleep products | planned | AI TikTok generator for sleep product affiliates | bedtime routine, sleep mask | `Sleep Product TikTok Videos for Affiliates — AI Generator \| Moras` |

**Mattress description 示例** (148 chars)：

> Bed-in-a-box unboxing and firmness-test hooks from affiliate product links—high-commission mattress videos for US TikTok Shop in minutes. Download Moras.

**Vertical 写作规则**：

1. Title / H1 / slug 使用 **同一 `{category}` 主称谓**（如 toiletry bag vs cosmetic bag 开词前选定主词）。
2. Description **必须**含品类专属 P2，不可 20 页共用同一段。
3. 数字（AOV、佣金）用区间或「待核实」；live 页可加 `Last reviewed {month} {year}` 于正文，metadata 保持简洁。
4. 与 sibling vertical **禁止**大段重复；仅共享「US TikTok Shop」「~3 min」等常量。

---

## 工具页（planned）

页脚 Product 入口；**页面尚未上线**，metadata 供上线直接使用。

| URL | P1 | P2 | 推荐 Title (chars) |
|-----|-----|-----|-------------------|
| /product-research | TikTok Shop product research for affiliates | commission signals, showcase picks, content gaps | `TikTok Shop Product Research for Affiliates — AI \| Moras` (52) |
| /hashtag-generator | TikTok Shop hashtag generator | category/niche/conversion hashtag layers | `TikTok Shop Hashtag Generator for Affiliates \| Moras` (50) |
| /caption-generator | TikTok Shop caption generator | hook-extension, search-driven captions | `TikTok Shop Caption Generator for Affiliates \| Moras` (50) |

**product-research description 示例** (130 chars)：

> Find high-commission US TikTok Shop products—trend signals, commission fit, and content gaps before you post affiliate videos. Download Moras.

**工具页 vs 博客 cannibalization**：

- `/product-research` = **工具落地页**，P1 为 product research tool
- `/blog/tiktok-product-research` = **教育文章**，P1 为 how-to / framework

---

## 博客 `/blog/{slug}`（planned，文稿已有）

**8 篇 slug**——主站待部署；新文章按同规则扩展：

| slug | 状态 | 建议 title 角度 | 主关键词（P1） |
|------|------|-----------------|----------------|
| /blog/how-to-make-money-on-tiktok | planned | Pillar / Year guide | how to make money on TikTok |
| /blog/tiktok-shop-setup | planned | Setup comparison | TikTok Shop setup |
| /blog/faceless-tiktok-shop-videos | planned | How-to / Production | TikTok Shop videos without filming |
| /blog/tiktok-product-research | planned | Research framework | TikTok Shop AI product research |
| /blog/tiktok-video-hooks | planned | Framework | TikTok Shop video hooks |
| /blog/tiktok-captions-hashtags | planned | Strategy guide | TikTok Shop captions and hashtags |
| /blog/tiktok-affiliate-side-hustle | planned | Timeline / Expectations | TikTok Shop affiliate side hustle |
| /blog/tiktok-shop-no-sales | planned | Diagnosis framework | TikTok Shop no sales |

Frontmatter 即 SERP metadata：

```yaml
---
title: "How to Make TikTok Shop Videos Without Filming in 2026"
description: "Four paths for TikTok Shop videos without filming—from AI voiceover to product-link automation, with cost and conversion benchmarks."
slug: "/blog/faceless-tiktok-shop-videos"
date: "2026-06-11"
---
```

| 项 | 规则 |
|----|------|
| title | editorial；45–60 chars；通常 **不加** `\| Moras` |
| description | 140–160 chars；读者将得到什么 + 主关键词 |
| slug | 常青 URL；路径已含 `/blog/` 前缀 |
| Moras 提及 | 主题相关时在 description 轻提；避免硬广；**不写收益保证** |
| 集群内链 | Pillar → Spoke 结构；metadata 不重复同一 P1 |

**博客 Title 示例**（与线上一致）：

- `How to Make Money on TikTok in 2026`（Pillar，年份可入 title）
- `How to Make TikTok Shop Videos Without Filming in 2026`
- `TikTok Shop Captions, Hashtags, and Descriptions: What Actually Drives Sales`

**新博客 Fallback**：从文章 H1/frontmatter title 提炼；description 写「读完能做什么」+ 1 个主关键词。

---

## 法务页（live）

| URL | Title (chars) | Description (chars) |
|-----|---------------|---------------------|
| /privacy | `Privacy Policy \| Moras` (22) | How Moras (K2LAB) collects, uses, and protects your data. US TikTok Shop affiliate platform. (95) |
| /terms | `Terms of Service \| Moras` (24) | Terms governing use of Moras AI commerce tools and subscription plans. (68) |

法务页 **不用** 冒号动作句；description 一句概括即可，50–120 chars；**无**营销 CTA。

---

## Cannibalization（站内竞争）

| 层级 | 规则 |
|------|------|
| **P1** | 类目词可跨页出现，但每页 P1 **侧重不同意图/品类** |
| **P2/P3** | **每页唯一**—Korean skincare → 仅 skincare vertical；CleanTok → 仅 cleaning-gadgets |
| **首页 vs Hub** | 首页 = 品牌 + 双能力；Hub = TikTok video generator broad |
| **Hub vs Vertical** | Hub 无具体品类；Vertical 必须有 `{category}` |
| **Vertical vs Vertical** | 品类词不可互换；toiletry-bag 不写 mattress hooks |
| **工具页 vs 博客** | 工具 = transactional tool 词；博客 = educational how-to |
| **TVG vs /blog/faceless-*** | Vertical 打品类+generator；博客打 without filming 教育意图 |
| **product-research vs tiktok-product-research blog** | 前者 tool P1；后者 framework/guide P1 |

---

## 任意页面 Fallback（URL 不在清单时）

适用于 **未来新增页面** 与 **状态表未列出的 path**。

1. **解析 URL** — 得基准 path；查 §站点页面清单 判 live / preview / planned
2. **若页面可访问** — 读 `<h1>`、首段、面包屑确定主题（**planned 页跳过此步**，用类型模板）
3. **推断类型** — §页面类型路由
4. **P1/P2 从页面或类型来** — live 以 H1 为准；planned 以章节清单 + slug 语义为准
5. **选 title 结构** — Vertical/工具 = 品类+affiliate；首页 = em dash；博客 = editorial
6. **Draft + 计字符** — title 50–60；description 150–160；超限按 §长度 重写
7. **Theme-keyword self-check** — §核心原则 四条自检
8. **Cannibalization** — 与同站相近 path 不重复 P2
9. **合规** — US-only；非 TikTok 官方；无 GMV 保证
10. **Notes** — 标注 `live` / `preview` / `planned`

**slug 人话化示例**：`led-face-mask` → 主题 `LED face mask affiliates`，P1 `AI TikTok video generator for LED face mask affiliates`，P2 `LED light therapy GRWM`

---

## Best Practices

| Item | Guideline |
|------|-----------|
| **Theme-keyword fit** | **最高优先级**：title/description 与该 URL 的 P1/P2 及页面主题强相关 |
| Front-load | 该页 P1 + 主题词在 title 最前 |
| Query mirror | Vertical title = 用户会搜的 `{category} + TikTok video generator` 句式 |
| Unique | 全站无 duplicate title/description |
| H1 alignment | Title 与 H1 **同主题**（Vertical：H1 常为 `AI TikTok video generator` + `for {category} affiliates.`） |
| Affiliate-first | 默认写 **affiliate / commission / showcase**；seller 不作 title 主称谓 |
| Brand suffix | 含品牌 title **统一** `\| Moras` 置尾 |
| Title ≠ Description | 不整句重复；title 名词标签，description 动词变体 |
| CTA | Description 末尾：`Download Moras.` 或 `Get started with Moras.` |
| US-only | 美区 TikTok Shop 语义入 description（工具/Vertical 页） |
| TikTok 写法 | 品牌写法 `TikTok`；`TikTok Shop` 首次出现写全 |
| 字符超限 | **输出前必计**；超 60/160 按 §长度 缩短；**不可删掉品类/主题词** |
| Testimonials | 证言 GMV 仅正文引用；metadata 不写具体数字作承诺 |

---

## Workflow（Agent 逐步执行）

1. **Parse URL** — 得基准 path
2. **Check page status** — §站点页面清单（live / preview / planned / anchor）
3. **Route page type** — §页面类型路由
4. **Identify page theme** — live 可读 H1；planned 从清单 + slug 推断
5. **Lookup P1/P2** — 查对应章节；**禁止**用其他页的 P1/P2 顶替
6. **Pick title pattern** — 含 §紧凑 Title（若品类名长）
7. **Draft title** — 含 P1 + 主题词 + `| Moras`（博客除外）；**计字符，目标 50–60**
8. **Draft description** — 含 P2 + 专属场景 + `Download Moras.`；**计字符，目标 150–160**
9. **Length check** — 超限则重写；**不计字符 = 未完成**
10. **Theme-keyword self-check** — §核心原则 四条
11. **Compliance + Cannibalization**
12. **Output** — §Output Format（含 **Page status**）

---

## Output Format

```markdown
### {Page name} — `{URL}`

**Page status**: {live | preview | planned | anchor}

**Page theme**: {one-line page topic}

**Primary keyword (P1)**: {this page only}

**Secondary keyword (P2)**: {this page only — for description}

**Recommended title** ({n} chars) ← must be 50–60
> {title text}

**Recommended meta description** ({n} chars) ← must be 150–160
> {description text}

**Theme-keyword fit**: {1 sentence}

**Alternatives**（可选，也需标注 chars）
- Title B ({n} chars): …
- Description B ({n} chars): …

**H1 alignment**: {suggested H1}
**Notes**: {planned 页勿声称已核对线上 DOM / cannibalization / compliance}
```

**批量任务**：Markdown 表格，列：URL | Status | Title (chars) | Description (chars)

---

## Templates（复制即用，字数已校验）

### 首页 (live)

```
Title (58): TikTok Shop Affiliate Videos — AI Commerce Producer | Moras
Description (155): Automate shoppable TikTok videos for US affiliates—from AI product picks to link-to-video edits, no filming. Hooks, captions, commission tags. Download Moras.
```

### TVG Hub (preview)

```
Title (55): AI TikTok Video Generator for TikTok Shop Affiliates | Moras
Description (138): Turn affiliate product links into shoppable US TikTok Shop videos—hooks, voiceover, captions, and commission tags in minutes. Download Moras.
```

### TVG Vertical (planned/preview)

```
Title (50): AI TikTok Generator for {Category} Affiliates | Moras
Description (~150): {P2 phrase}. Shoppable {category} videos from affiliate links on US TikTok Shop. Download Moras.
```

### 工具页 (planned)

```
Title (52): TikTok Shop {Tool} for Affiliates — AI | Moras
Description (~140): {P2 for US TikTok Shop affiliates}. Download Moras.
```

### 博客 (planned)

```
title (≤60): "{Topic Title} ({Year})"
description (150–160): "{What reader learns}. {Main keyword}."
```

### 法务 (live)

```
Title (22): Privacy Policy | Moras
Description (95): How Moras (K2LAB) collects, uses, and protects your data. US TikTok Shop affiliate platform.
```

---

## GSC 优化（可选）

1. Google Search Console → 高展示、低 CTR 页面
2. 优先改 title/description（Vertical 页通常先改 title 中的 `{category}` 表述）
3. 改后 2–4 周再看 CTR；避免频繁改动
4. 用实际展示 query 校正 Vertical P1/P2（尤其 mattress 等 live 页）

---

## 版本与维护

| 字段 | 值 |
|------|-----|
| version | 1.2.1 |
| last-updated | 2026-06-15 |
| complements | moras-blog-article |
| site | moras.ai |
| covers | all page types — live, preview, planned |
| market | US TikTok Shop, English only |
| primary-audience | TikTok Shop affiliates (not sellers as default) |
| brand-suffix | `\| Moras` (mandatory when brand appears in title) |
| title-length | 50–60 chars (hard max 60) |
| description-length | 150–160 chars (hard max 160) |
| core-rule | **Every title & description must strongly match that page's keywords and theme** |

更新定价、页面上线状态、新增 slug 或博客时，同步修改 §站点页面清单 与对应章节。

**外部参考（可选，非必读）**：

- [Google: Create good titles and snippets](https://developers.google.com/search/docs/appearance/title-link)
- [title-tag skill](https://github.com/kostja94/marketing-skills/blob/main/skills/seo/on-page/title/SKILL.md)
- [meta-description skill](https://github.com/kostja94/marketing-skills/blob/main/skills/seo/on-page/description/SKILL.md)
