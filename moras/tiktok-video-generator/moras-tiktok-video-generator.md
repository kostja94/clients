# Moras — TikTok Video Generator（合并主文档）

> 本文合并原 **overview / data / keywords / template** 四份文档并去重，一份文件覆盖全部内容：
> 目的与信息架构 · 页面模板与 config · 生产流程与验收 · 20 品类 Vertical 数据 · 关键词登记与找词方法 · 关键词变体 · 合规与待办。
>
> 关联：[video-types](./moras-tiktok-video-generator-video-types.md)（带货视频类型）· [../moras-site-structure.md](../moras-site-structure.md) · [../moras-keywords.md](../moras-keywords.md)

**Last updated**: 2026-08-11

*预览站*：[moras-navy.vercel.app/tiktok-video-generator](https://moras-navy.vercel.app/tiktok-video-generator) · *正式域*：[moras.ai](https://moras.ai/)
Vertical 基准页：[mattress](https://moras-navy.vercel.app/tiktok-video-generator/mattress)

---

## 1. 文档职责

| 本文 | 合并来源 |
|------|----------|
| 目的、信息架构、页面模板、Schema、生产流程、合规 | 原 `moras-tiktok-video-generator.md`（overview） |
| Vertical 注册、目标词表、Mattress 基准页数据 | 原 `moras-tiktok-video-generator-data.md`（data） |
| 找词方法、意图变体、称谓变体、cannibalize 规避 | 原 `moras-tiktok-video-generator-keywords.md`（keywords） |
| 线框图、config 填空、开写前 5 问、发布验收 | 原 `moras-tiktok-video-generator-template.md`（template） |

**核心前提**：Moras 生成 **转化驱动（Conversion）** 的 TikTok 可购短视频；本栏目是 Moras 的核心 SEO 增长引擎——通过 20 个品类 Vertical 详情页，承接 TikTok Shop 卖家品类 long-tail 搜索，引导下载 App。

---

## 2. 目的

### 2.1 业务目标

| 目标 | 说明 |
|------|------|
| **捕获品类长尾检索** | 承接 Vertical 英文 long-tail（[§9 目标关键词登记表](#9-目标关键词登记表)） |
| **解释 Moras 在品类上的价值** | 「选品 → 成片 → 发布赚佣」落到具体 SKU 类型 |
| **转化 App 下载** | CTA → App Store；US-only、~3 min/条、3 cuts/brief |
| **与 Product research 互链** | Vertical § 选品 → `/product-research` |

### 2.2 SEO / 内容目标

| 目标 | 说明 |
|------|------|
| **Hub 吃 broad 词** | `/tiktok-video-generator`（Hub 词不在本文件维护） |
| **Vertical 吃 long-tail** | `/tiktok-video-generator/{slug}`；词表见 [§9](#9-目标关键词登记表) |
| **程序化扩展** | 同一模板 + vertical config（§4–§5） |
| **E-E-A-T 与合规** | 审查日期、可验证数字；Moras 非 TikTok 官方、仅美区 |

### 2.3 不做什么

- 不替代 TikTok Shop Seller Center
- 不承诺普适 GMV/佣金结果
- 不用 find-replace 跨品类复制而不改 Signal 与 KPI

---

## 3. 信息架构

### 3.1 URL

```
/tiktok-video-generator                    ← Hub
/tiktok-video-generator/{category-slug}    ← Vertical
```

### 3.2 面包屑

```
Home → TikTok video generator → {displayName}
```

### 3.3 站内关系

| 栏目 | 关系 |
|------|------|
| Product research | Vertical § 选品 内链 |
| Use cases | Vertical § Who it's for playbook |
| Hashtag / Caption generator | 页脚并列；Vertical 内嵌示例 |
| Pricing / Download | 全站 CTA |

---

## 4. 页面模板

### 4.1 区块顺序

| # | 区块 | Hub | Vertical | 定制深度 |
|---|------|-----|----------|----------|
| 1 | 面包屑 + 标签行 | — | ✓ | 低 |
| 2 | Hero（H1 + subcopy + 双 CTA） | ✓ | ✓ | 中 |
| 3 | TikTok 参考 embed | — | ✓ | **高** |
| 4 | 三步流程（Pick → Generate → Publish） | ✓ | ✓ | 低 |
| 5 | KPI 四卡 | 部分 | ✓ | **高** |
| 6 | § How Moras picks the {category} winner（3 Signals） | — | ✓ | **高** |
| 7 | § How Moras generates…（3 Steps + 6 能力卡） | 3 Steps | ✓ | 中 |
| 8 | § Captions and hashtags | — | ✓ | **高** |
| 9 | § Moras vs UGC vs CapCut | ✓ | ✓ | 低 |
| 10 | § Who it's for（3 卡） | ✓ | ✓ | 中 |
| 11 | § FAQ（6 问 + 答案） | ✓ | ✓ | 中–高 |
| 12 | 底部 CTA + Footer | ✓ | ✓ | 低 |

### 4.2 线框图（以 mattress 为范本）

> 每新建一个品类 Vertical 页面即按此布局填写。标注 ⓕ 的区块跨品类固定，无需修改；标注 ★ 的区块为品类专属，决定 SEO 区分度。线框图以 **mattress**（唯一 live 页）为范本绘制；实际落地内容对照见 [§11](#11-mattress-页面已落地内容对照)。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🌐 moras.ai/tiktok-video-generator/mattress                                │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  Home  ›  TikTok video generator  ›  Mattress                     ⓕ 面包屑  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │   AI TikTok video generator                                           │  │
│  │   for mattress sellers.                                               │  │
│  │                                                                       │  │
│  │   High-AOV category on TikTok Shop — mattress sellers earn            │  │
│  │   5–15% commission with Moras AI video automation.                    │  │
│  │                                                                       │  │
│  │   [ 🍎 Download ]    [ ▶ Start free ]                                 │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                              ↳ config hero                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────┐                                   │
│  │                                     │                                   │
│  │      TikTok mattress unboxing       │                                   │
│  │      [ ▶ video embed ]              │                                   │
│  │                                     │                                   │
│  └─────────────────────────────────────┘                                   │
│              ↳ config reference  ★高                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│      ① Pick             ② Generate          ③ Publish           ⓕ 三步流程  │
│   ┌──────────┐      ┌──────────┐        ┌──────────┐                      │
│   │ Discover  │  →   │ AI makes │   →    │ Post &   │                      │
│   │ trending  │      │ 3 video  │        │ earn $   │                      │
│   │ products  │      │ variants │        │          │                      │
│   └──────────┘      └──────────┘        └──────────┘                      │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐            │
│  │           │   │           │   │           │   │           │            │
│  │   $420+   │   │   5–15%   │   │  ~3 min   │   │  3 cuts   │   ★高      │
│  │   avg AOV │   │ affiliate │   │ per video │   │ per brief │            │
│  │           │   │ comm.     │   │           │   │           │            │
│  └───────────┘   └───────────┘   └───────────┘   └───────────┘            │
│                      ↳ config metrics                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  How Moras picks the mattress winner                          ★高     │  │
│  │                                                                       │  │
│  │  Mattress on TikTok Shop is a high-AOV category where the right       │  │
│  │  product selection directly impacts your affiliate earnings.          │  │
│  │  Moras evaluates three signals to pick winners:                       │  │
│  │                                                                       │  │
│  │  ┌──────────────────────────────────────────────────────────────┐    │  │
│  │  │  Signal 1 · Commission × GMV                                │    │  │
│  │  │  Mattress AOVs reach $420+ with 5–15% commission —           │    │  │
│  │  │  Moras filters for products with verified payout history.   │    │  │
│  │  └──────────────────────────────────────────────────────────────┘    │  │
│  │  ┌──────────────────────────────────────────────────────────────┐    │  │
│  │  │  Signal 2 · Return rate filter                               │    │  │
│  │  │  High-ticket items risk returns eating commission.           │    │  │
│  │  │  Moras flags products with <8% return rate to protect margin.│    │  │
│  │  └──────────────────────────────────────────────────────────────┘    │  │
│  │  ┌──────────────────────────────────────────────────────────────┐    │  │
│  │  │  Signal 3 · Supply gap                                      │    │  │
│  │  │  Only 12% of mattress listings have dedicated affiliate      │    │  │
│  │  │  video content — be the first to capture untapped demand.    │    │  │
│  │  └──────────────────────────────────────────────────────────────┘    │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                           ↳ config productResearch                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  How Moras generates your mattress videos                             │  │
│  │                                                                       │  │
│  │  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐                 │  │
│  │  │ ① Hook the  │   │ ② Build     │   │ ③ Publish   │                 │  │
│  │  │   viewer    │ → │   the video │ → │   & earn    │                 │  │
│  │  │             │   │             │   │             │                 │  │
│  │  │ Unboxing    │   │ Product URL │   │ Auto-post    │                 │  │
│  │  │ expansion,  │   │ → 3 cuts    │   │ to TikTok   │                 │  │
│  │  │ firmness    │   │ with voice- │   │ Shop with   │                 │  │
│  │  │ test, price │   │ over, cap-  │   │ affiliate   │                 │  │
│  │  │ comparison  │   │ tions       │   │ links       │                 │  │
│  │  └─────────────┘   └─────────────┘   └─────────────┘                 │  │
│  │                                                                       │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │  │  Hook    │ │  Native  │ │   Auto   │ │ Product- │ │  Multi-  │ │Affiliate │ │
│  │  │ engine   │ │ voiceover│ │ captions │ │  aware   │ │ variant  │ │   link   │ │
│  │  │          │ │          │ │          │ │  edits   │ │  render  │ │injection │ │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
│  │                                    ⓕ 6 能力卡                                    │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                   ↳ config videoGeneration (3 steps) + 固定块 (6 能力卡)       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  Captions and hashtags                                       ★高     │  │
│  │                                                                       │  │
│  │  Hook-led     │ "This mattress inflated in 60 seconds 😳💰"           │  │
│  │  Problem-led  │ "Tired of mattress returns killing your commission?"  │  │
│  │  Social proof │ "342 sellers already use this script — your turn"     │  │
│  │                                                                       │  │
│  │  #Moras #MattressTok #BedInABox #TikTokShop #TikTokMadeMeBuyIt        │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                  ↳ config captions + hashtags                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  Moras  vs  UGC creators  vs  CapCut                         ⓕ 对比   │  │
│  │  ─────────────────────────────────────────────────                    │  │
│  │       AI agents        │  $200–500/video  │  template-only            │  │
│  │       3 cuts/brief     │  5–7 day wait    │  no affiliate link        │  │
│  │  Last reviewed June 2026                                              │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  Who it's for                                                  ★中    │  │
│  │                                                                       │  │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐    │  │
│  │  │ TikTok Shop      │  │ Affiliate         │  │ Home & furniture │    │  │
│  │  │ sellers          │  │ creators          │  │ creators         │    │  │
│  │  │                  │  │                   │  │                  │    │  │
│  │  │ Scale video      │  │ Earn without      │  │ Large products   │    │  │
│  │  │ output without   │  │ filming — Moras   │  │ need visual      │    │  │
│  │  │ hiring creators  │  │ generates from    │  │ demos — Moras    │    │  │
│  │  │                  │  │ your links        │  │ handles it       │    │  │
│  │  └──────────────────┘  └──────────────────┘  └──────────────────┘    │  │
│  │         ⓕ 固定               ⓕ 固定               ★品类专属            │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                         ↳ config whoItsFor                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  FAQ                                                          ★中    │  │
│  │                                                                       │  │
│  │  Q: What is the best AI TikTok video generator for mattress sellers?  │  │
│  │  A: Moras generates 3 video variants per product link...              │  │
│  │                                                                       │  │
│  │  Q: Can I use Moras for TikTok Shop affiliate marketing?              │  │
│  │  A: Yes. Moras auto-injects your affiliate links... US TikTok Shop.   │  │
│  │                                                                       │  │
│  │  Q: Is Moras officially affiliated with TikTok?                       │  │
│  │  A: No. Moras is independently developed by K2 Lab...                 │  │
│  │                                                                       │  │
│  │  Q: Can mattress sellers outside the US use Moras?                    │  │
│  │  A: Currently US TikTok Shop only. Non-US sellers...                  │  │
│  │                                                                       │  │
│  │  Q: How much commission can mattress affiliates earn?                 │  │
│  │  A: Mattress affiliate rates on TikTok Shop range 5–15%...            │  │
│  │                                                                       │  │
│  │  Q: Does Moras use AI to generate TikTok videos?                      │  │
│  │  A: Yes. Eleven AI agents handle hook selection, voiceover...         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                            ↳ config faq                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                                                                       │  │
│  │         HIRE MORAS. GO VIRAL.                                         │  │
│  │                                                                       │  │
│  │         [ 🍎 Download for iOS ]                                       │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                              ⓕ 底部 CTA                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│  Product · Showcase · Pricing · Terms · Privacy                  ⓕ Footer   │
│  © 2026 K2LAB. Powered by K2 lab                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.3 Hub vs Vertical

| 维度 | Hub | Vertical |
|------|-----|----------|
| H1 | 通用 commission 叙事 | `{category} sellers`（§4.5） |
| 选品 | 无 3 Signals | **必须有** |
| Caption / Hashtag | 无 | **必须有** |
| KPI | ~3 min、3 cuts | 品类 AOV / 佣金 |

### 4.4 跨 Vertical verbatim 块

- 6 能力卡：Hook engine · Native voiceover · Auto captions · Product-aware edits · Multi-variant render · Affiliate link injection
- Moras vs UGC vs CapCut + `Last reviewed {month} {year}`
- 常量：Eleven agents · 3 cuts/brief · ~3 min · iOS · US-only

### 4.5 Vertical 页面文案（Title / H1 / Description 模板）

| 字段 | 模板 / 要点 |
|------|-------------|
| **Title** | `AI TikTok video generator for {category} sellers — Moras` |
| **H1 行 1** | `AI TikTok video generator` |
| **H1 行 2** | `for {category} sellers.` |
| **Description** | 品类 AOV/佣金区间 + 选品价值摘要 + US TikTok Shop + CTA；`{category}` 与 §4.5 主称谓一致 |

发布前：Title / H1 / slug 同一 `{category}`；Meta description 含品类 + US + Moras；与 sibling vertical 无 cannibalize（见 §14.4）。

---

## 5. Schema / 页面 config（填空）

> 字段类型与填空注释合一。★高 块决定 SEO 区分度，禁止敷衍。写完后对照 §4.1 区块顺序确认覆盖完整。

```yaml
# ═══════════════════════════════════════════════
# slug: ""   # kebab-case；须在 §8 已登记
# ═══════════════════════════════════════════════

slug: ""                       # kebab-case；须在 §8 已登记
displayName: ""
categoryTags: []               # string[]

# —— Hero ——
seo:
  title: ""                    # AI TikTok video generator for {category} sellers — Moras
  description: ""              # 品类 AOV/佣金 + 选品价值 + US TikTok Shop + CTA

hero:
  h1Line1: "AI TikTok video generator"        # 固定，不可改
  h1Line2: "for {category} sellers."          # {category} = displayName
  subcopy: ""

# —— KPI 四卡 ——
metrics:
  aov: ""                       # 品类专属
  affiliateRate: ""             # 品类专属
  timePerVideo: "~3 min"
  variantsPerBrief: "3 cuts"

# —— 3 Signals（★高，品类专属，禁止 find-replace；P0 草稿见 §12） ——
productResearch:
  categoryFraming: ""           # 品类一句话概述
  signals:
    - title: ""                 # Signal 1 标题
      body: ""
    - title: ""                 # Signal 2 标题
      body: ""
    - title: ""                 # Signal 3 标题
      body: ""

# —— 3 Steps（每步配品类 hook） ——
videoGeneration:
  stepHooks: []                 # 品类 hook 方向
  steps:
    - title: ""                 # Step 1
      body: ""
    - title: ""                 # Step 2
      body: ""
    - title: ""                 # Step 3
      body: ""

# —— Captions & Hashtags（★高） ——
captions:
  hookLed: ""
  problemLed: ""
  socialProof: ""

hashtags:
  core: []                      # #Moras, #AITikTokVideoGenerator
  category: []                  # 品类 TikTok 站内词
  conversion: []                # #TikTokShop, #TikTokMadeMeBuyIt

# —— Who it's for（卡 1–2 固定，卡 3 品类专属） ——
whoItsFor:
  - persona: ""                 # 卡 1（固定）
    headline: ""
    body: ""
    playbookUrl: ""
  - persona: ""                 # 卡 2（固定）
    headline: ""
    body: ""
    playbookUrl: ""
  - persona: ""                 # 卡 3（★品类专属）
    headline: ""
    body: ""
    playbookUrl: ""

# —— FAQ（×6，覆盖 AI 披露 + 区域 + 收益 + 平台政策） ——
faq:
  - question: ""
    answer: ""
  - question: ""
    answer: ""
  - question: ""
    answer: ""
  - question: ""
    answer: ""
  - question: ""
    answer: ""
  - question: ""
    answer: ""

# —— 参考 ——
reference:
  tiktokUrl: ""
  embedLabel: ""

# —— 元数据 ——
meta:
  lastReviewed: ""              # YYYY-MM
  status: "draft"               # draft → review → live
```

---

## 6. 生产流程

### 6.1 三步法

```
Step A — 定 config：§8 取 slug；补 KPI、参考视频、playbook、审查日期
Step B — 写品类块：Signals + hooks + captions + hashtags + faq + whoItsFor
Step C — 套模板：固定块 + 术语/内链；关键词已在 §9 登记
```

### 6.2 决策树（开写前 5 问）

> 有一项答「否」就不能标 live。

| # | 问题 | 不过时 |
|---|------|--------|
| Q1 | slug 已在 §8 + §9 登记？ | → 否 → 先登记 |
| Q2 | 有 TikTok 参考视频 URL？ | → 可 draft，不可 live |
| Q3 | KPI 有来源或审慎区间？ | → 标「待验证」 |
| Q4 | playbook 内链可访问？ | → 占位 |
| Q5 | 3 个 Signal 品类专属？ | → 重写，禁止 find-replace |

### 6.3 发布验收与发布后

**发布验收**

- [ ] 全文无其他品类 displayName 残留
- [ ] 3 Signal 品类专属（对照 §7、§12）
- [ ] Title / H1 / Description 与 §9 主称谓一致
- [ ] Caption / hashtag 含 TikTok 站内词（§13.3）
- [ ] FAQ 6 问有完整答案
- [ ] 与 Hub / sibling vertical 无大段重复
- [ ] 数字有来源或「区间 + Last reviewed」
- [ ] 合规通过（§15：仅 US、非 TikTok 官方、Moras 统一拼写、收益可验证、AI 披露、Last reviewed）
- [ ] §8 `status` 已更新

**发布后**

- [ ] GSC 提交：`https://moras.ai/tiktok-video-generator/{slug}`
- [ ] 3–7 天后复查索引状态
- [ ] SOP 记录日期 + slug
- [ ] §8 `status` → `live`

---

## 7. 策略对照（写作必读）

| 维度 | Mattress（live） | Toiletry bag（draft） |
|------|------------------|----------------------|
| AOV | 高（$420+） | 低–中（$15–45，待核实） |
| 核心风险 | 退货吃佣金 | 同质化、内容饱和 |
| Signal 重心 | 佣金×GMV、退货率、供给缺口 | 评增速×佣金、可演示卖点、hook 缺口 |
| Hook 示例 | 开箱膨胀、硬度测试、比价大牌 | Pack with me、容量、防水、TSA |
| 第三人群卡 | Home & furniture creators | Travel / beauty / organization |
| TTS 指南 | 高 AOV 例外 | 低 AOV、强视觉、易决策 |

---

## 8. Vertical 登记表（20 品类）

> 热度数据：2026-06-02 第三方检索（FastMoss、Dashboardly、Darkroom）。**非 Moras 内部数据**。  
> 关键词登记 → [§9](#9-目标关键词登记表)

| # | slug | displayName | 优先级 | 状态 | 热度依据（摘要） | 视频 hook 方向 |
|---|------|-------------|--------|------|------------------|----------------|
| 1 | `skincare` | Skincare | **P0** | planned | 美护 ~31% GMV；Korean skincare 高增速 | GRWM、before/after、glass skin |
| 2 | `supplements` | Supplements | **P0** | planned | Q1 Top10 补剂；Health 高 YoY | 睡眠/能量/镁 transformation |
| 3 | `cleaning-gadgets` | Cleaning gadgets | **P0** | planned | CleanTok；Home 清洁 QoQ 高增 | satisfying 清洁、前后对比 |
| 4 | `kitchen-gadgets` | Kitchen gadgets | **P0** | planned | Home & Kitchen ~19% GMV | 一道菜搞定、省时神器 |
| 5 | `lip-gloss` | Lip gloss | **P0** | planned | 唇妆 CVR 领跑 | 试色、一涂成片 |
| 6 | `toiletry-bag` | Toiletry bag | **P0** | draft | Travel × Beauty；低 AOV | Pack with me、容量、防水 |
| 7 | `collagen` | Collagen | P1 | planned | Q1 Top10 胶原 | 内服+外用、皮肤变化 |
| 8 | `teeth-whitening` | Teeth whitening | P1 | planned | Q1 Top10 美白条 | 使用前后、条带效果 |
| 9 | `phone-case` | Phone case | P1 | planned | 电子配件 ~11% GMV | 开箱、防摔、MagSafe |
| 10 | `shapewear` | Shapewear | P1 | planned | Q1 Top10 塑身衣 | 上身对比、occasion |
| 11 | `pet-products` | Pet products | P1 | planned | Pet GMV 高 YoY | 萌宠使用、反应 |
| 12 | `home-organization` | Home organization | P1 | planned | Home & Living 加速 | 小空间改造 |
| 13 | `vacuum` | Vacuum | P2 | planned | Q1 Top10 吸尘器 | 吸尘 satisfying |
| 14 | `led-face-mask` | LED face mask | P2 | planned | H1 护肤设备 | GRWM、光疗科普 |
| 15 | `hair-growth` | Hair growth | P2 | planned | Hair growth QoQ 高增 | 发缝 before/after |
| 16 | `perfume` | Perfume | P2 | planned | 长期 Top 搜索 | 试香、dupes |
| 17 | `protein-snacks` | Protein snacks | P2 | planned | Food 高 YoY | 宏量营养、试吃 |
| 18 | `makeup-tools` | Makeup tools | P2 | planned | Tools 搜索上升 | 上妆对比 |
| 19 | `sleep-products` | Sleep products | P2 | planned | 助眠内容稳定 | 睡前 routine |
| 20 | `mattress` | Mattress | P2 | **live** | 高 AOV；**模板基准** | 开箱膨胀、硬度测试 |

**暂不优先**：大件家具、精细尺码服饰、受限健康宣称补剂。

---

## 9. 目标关键词登记表

> **唯一词表**。路径：`/tiktok-video-generator/{slug}`。Volume 待 GSC/广告补全。

| slug | displayName | 主目标词 | 次级词 | 变体 / 备注 | Volume |
|------|-------------|----------|--------|-------------|--------|
| `mattress` | Mattress | `AI TikTok video generator for mattress sellers` | `mattress TikTok Shop affiliate` | `bed in a box TikTok video` | — |
| `skincare` | Skincare | `AI TikTok video generator for skincare sellers` | `Korean skincare TikTok Shop` | `skincare affiliate video`; 称谓待验：skin care | — |
| `supplements` | Supplements | `AI TikTok video generator for supplement sellers` | `magnesium TikTok Shop` | `wellness affiliate`; 称谓：supplements vs wellness supplements | — |
| `cleaning-gadgets` | Cleaning gadgets | `AI TikTok video generator for cleaning gadget sellers` | `CleanTok products` | `TikTok Shop cleaning`; 称谓：gadgets vs tools | — |
| `kitchen-gadgets` | Kitchen gadgets | `AI TikTok video generator for kitchen gadget sellers` | `kitchen hacks TikTok Shop` | `small kitchen tools affiliate` | — |
| `lip-gloss` | Lip gloss | `AI TikTok video generator for lip gloss sellers` | `lip gloss swatch TikTok` | `GRWM lip product` | — |
| `toiletry-bag` | Toiletry bag | `AI TikTok video generator for toiletry bag sellers` | `cosmetic bag TikTok Shop` | `travel organizer affiliate`; **称谓待验**：toiletry bag / cosmetic bag / travel organizer | — |
| `collagen` | Collagen | `AI TikTok video generator for collagen sellers` | `collagen peptides TikTok Shop` | — | — |
| `teeth-whitening` | Teeth whitening | `AI TikTok video generator for teeth whitening sellers` | `whitening strips TikTok` | — | — |
| `phone-case` | Phone case | `AI TikTok video generator for phone case sellers` | `MagSafe case TikTok Shop` | — | — |
| `shapewear` | Shapewear | `AI TikTok video generator for shapewear sellers` | `fajas TikTok Shop` | `shapewear try on` | — |
| `pet-products` | Pet products | `AI TikTok video generator for pet product sellers` | `TikTok Shop pet` | `dog product affiliate` | — |
| `home-organization` | Home organization | `AI TikTok video generator for home organization sellers` | `closet organization TikTok Shop` | — | — |
| `vacuum` | Vacuum | `AI TikTok video generator for vacuum sellers` | `cordless vacuum TikTok Shop` | — | — |
| `led-face-mask` | LED face mask | `AI TikTok video generator for LED face mask sellers` | `LED mask skincare TikTok` | — | — |
| `hair-growth` | Hair growth | `AI TikTok video generator for hair growth sellers` | `hair serum TikTok Shop` | — | — |
| `perfume` | Perfume | `AI TikTok video generator for perfume sellers` | `perfume TikTok Shop dupes` | — | — |
| `protein-snacks` | Protein snacks | `AI TikTok video generator for protein snack sellers` | `high protein snacks TikTok` | — | — |
| `makeup-tools` | Makeup tools | `AI TikTok video generator for makeup tool sellers` | `makeup brush TikTok Shop` | — | — |
| `sleep-products` | Sleep products | `AI TikTok video generator for sleep product sellers` | `sleep mask TikTok Shop` | — | — |

---

## 10. Mattress 基准页详细关键词

> 数据来源：top商品.xlsx（Moras Top + FastMoss Top，100 商品），归类到 Bedding & Bath 床品卫浴。  
> Mattress 为 tiktok-video-generator 模板基准页，本表提供写页面时可引用的品类级关键词、商品级长尾词和 TikTok 热搜信号。

### 10.1 品类概览

| 指标 | 数据 |
|------|------|
| 所属高热品类 | Bedding & Bath（床品卫浴） |
| 品类优先级 | 中 |
| 该品类商品总数（样本） | 5 |
| 最高销量单品 | Shilucheng Bamboo Sheet Set — 341,601 件 / $8.57M |
| 核心关键词方向 | cooling sheets, comforter set, bath mat, mattress topper, microfiber hair towel |
| SEO 页面建议 | 分类页 + 商品页 + 季节性内容 |

### 10.2 品类级目标词

| 类型 | 关键词 | 说明 |
|------|--------|------|
| **主目标词** | `AI TikTok video generator for mattress sellers` | pSEO 主攻词 |
| **联盟向** | `mattress TikTok Shop affiliate` | 联盟卖家意图 |
| **成片向** | `mattress TikTok Shop affiliate video` | 视频生成意图 |
| **工具向** | `AI mattress TikTok video generator` | 工具属性 |
| **品类+场景** | `bed in a box TikTok video` | 子品类变现 |
| **品类+平台** | `mattress TikTok Shop` | 平台搜索 |

### 10.3 商品级长尾词

> 从 FastMoss / Moras 爆款商品中提取，用于 caption、hashtag 和 FAQ long-tail。

| 来源 | 商品 | 热度参考 | 可提炼关键词 |
|------|------|----------|--------------|
| Fastmoss Top #17 | Shilucheng Bamboo Sheet Set — 4/6 Pc Bedding Set, 16'' Deep Pocket | 销量 341,601 / $8,566,940 | `bamboo sheet set`, `deep pocket sheets`, `cooling bed sheets TikTok` |
| Moras Top #40 | 12"14" Twin Full Queen King Size Mattress in a Box — Hybrid Pocket Spring Memory Foam | 销量 3,051 / GMV $6,144 | `mattress in a box`, `hybrid mattress`, `pocket spring memory foam`, `bed in a box TikTok Shop` |
| Moras Top #50 | BEDLORE Bamboo Mattress Topper — Thicken Pillow Top Pad, Cooling | 销量 2,486 / GMV $1,071 | `mattress topper`, `cooling mattress pad`, `bamboo mattress topper` |
| Moras Top #43 | Bedsure Boho Arch Tufted Comforter Set — Beige Boho Bedding, 3 Pieces | 销量 7,805 / GMV $1,877 | `comforter set`, `boho bedding`, `tufted comforter` |
| Moras Top #36 | Exclusivo Mezcla Ultrasonic Quilt Set — 2/3 Pieces, Lightweight Bedspread | 销量 10,581 / GMV $1,097 | `quilt set`, `lightweight bedspread`, `ultrasonic quilt` |

### 10.4 TikTok 站内词参考

| 关键词方向 | 示例 | 用途 |
|------------|------|------|
| **产品形态** | `bed in a box unboxing`, `mattress inflation`, `memory foam expansion` | hook 方向 |
| **对比测试** | `mattress firmness test`, `mattress vs mattress`, `box mattress review` | 视频叙事 |
| **使用场景** | `bedroom makeover TikTok`, `guest room setup`, `small space mattress` | whoItFor |
| **购买意图** | `best mattress TikTok Shop`, `affordable mattress`, `mattress deal` | CTA / caption |
| **内容形式** | `mattress unboxing TikTok`, `bed setup timelapse`, `sleep test` | 视频参考 |

### 10.5 扩展 long-tail（拆法）

在 broad 品类词上叠加属性：

```
broad:     mattress TikTok Shop
long-tail: bed in a box mattress TikTok Shop
           memory foam mattress unboxing
           hybrid mattress review TikTok
           cooling mattress for hot sleepers
           queen mattress in a box affordable
           guest room mattress setup ideas
```

常用叠加维度：`cooling / memory foam / hybrid / king / queen / affordable / unboxing / setup / review / for hot sleepers / small space`

---

## 11. Mattress 页面已落地内容对照

> 与线上 mattress 基准页对照，用于后续 vertical 复刻。

| 区块 | 内容要点 | 数据引用 |
|------|----------|----------|
| Hero | H1: AI TikTok video generator for mattress sellers | [§10.2](#102-品类级目标词) 主目标词 |
| KPI | AOV $420+、佣金区间、~3 min/条、3 cuts/brief | — |
| 3 Signals | 佣金×GMV、退货率、供给缺口 | [§12](#12-p0-signal-草稿) |
| Hook 示例 | 开箱膨胀、硬度测试、比价大牌 | [§10.4](#104-tiktok-站内词参考) |
| Caption / Hashtag | hook-led / problem-led / social-proof 三类 | [§10.3](#103-商品级长尾词) 商品词 |
| Who it's for (第 3 卡) | Home & furniture creators | — |
| 合规提示 | 仅 US TikTok Shop；非 TikTok 官方；Last reviewed | [§15](#15-合规与品牌) |

---

## 12. P0 Signal 草稿

开写前须用 TTS / Moras 数据核实。

**skincare** — Review velocity × commission · Demo-friendly actives · Creator saturation gap  
**supplements** — Commission × repeat · Claim-safe filter · Transformation content gap  
**cleaning-gadgets** — GMV × CleanTok tag · Before/after demonstrability · Video supply gap  
**kitchen-gadgets** — Commission × impulse AOV ($18–65) · One-shot demo · Seasonal hook gap  
**lip-gloss** — Shade-level winners · Swatch-on-camera · GRWM cluster gap  
**toiletry-bag** — Review velocity × commission · Differentiation filter · Hook-type gap  

各 Signal 正文展开见历史 config 或开写时在 Schema `productResearch.signals` 填写。

---

## 13. 找词方法

### 13.1 关键词来源（四类）

| 类型 | 平台 | 找词目的 | 典型产出 |
|------|------|----------|----------|
| **官网 pSEO** | Google / Bing | 决定是否开 Vertical、定主/次级英文词 | `AI TikTok video generator for skincare sellers` |
| **TikTok 站内** | TikTok App / Shop | caption/hashtag 示例、验证品类搜索需求 | `skincare TikTok Shop`, Content Gap 话题 |
| **Moras 内部** | App / 选品飞轮 / 用户行为 | 验证「哪些品类真有出单与成片需求」 | 高 GMV 品类、高视频量产品类 |
| **竞品页面** | 竞品官网 SERP 页 | 拆词、找空白、收变体 | 竞品 Title/URL/H2 中的 category 词 |

> §13.2–§13.3 为外部公开数据；§13.4–§13.5 为 **Moras 侧与竞品侧**，用于验证「该品类是否值得占词」并补充变体。登记表（[§9](#9-目标关键词登记表)）以 **pSEO 主/次级词** 为主；TikTok 站内词、内部验证结论写入「变体 / 备注」。

### 13.2 官网 pSEO（Google 长尾）

| 步骤 | 做法 |
|------|------|
| 1. 定品类称谓 | 用 §14.3 变体规则确定 `{category}` 主称谓（如 skincare vs skin care） |
| 2. 套意图模板 | 按 §14.1 生成主词 + 联盟/成片变体 |
| 3. 验证搜索量 | GSC、Ahrefs、Semrush、Google Ads Keyword Planner；补入 [§9](#9-目标关键词登记表) `Volume` |
| 4. 查 SERP | 搜主词，看排名页类型（工具首页 / use-case / 博客）→ 对照 §13.5 |
| 5. 扩 long-tail | 从 autocomplete / People Also Ask 拆更具体子意图（见 §14.2） |
| 6. 登记 | 在 [§9](#9-目标关键词登记表) 增行；同步 §8 登记 slug |

### 13.3 TikTok 站内（caption / 选品佐证）

| 工具 | 找什么 | 怎么用 |
|------|--------|--------|
| **TikTok 搜索 autocomplete** | 输入 `{category} TikTok Shop` 看补全 | 次级词、买家意图验证 |
| **Creator Search Insights** | Suggested、**Content Gap** | 高搜索、低供给话题 → 写入变体/备注 |
| **Seller Center → Product Opportunities** | Top Searched Keywords、Trending Hashtags | 品类级买家词；周一查新词 |
| **Seller Center → Product Ranking** | Bestsellers + Popular Shoppable Videos | 见 §13.3.1 |
| **TikTok Creative Center** | 品类爆款关联 hashtag | hook / hashtag 方向 |
| **[Kalodata → Shop](https://www.kalodata.com/shop)** | 热店/热品、品类 GMV、SKU 标题 | 见 §13.3.1 |
| **[FastMoss → Sales List](https://www.fastmoss.com/e-commerce/saleslist)** | 销量榜；按国家/品类/时间筛 GMV | 见 §13.3.1 |
| **EchoTik** | TikTok 品类搜索趋势 | 与 Kalodata/FastMoss 交叉验证；见 §13.5 B 类竞品 |

> **Product Opportunities vs Product Ranking**：前者偏**搜索词 / hashtag**（更接近关键词字面）；后者偏**已出单品类与爆款视频**（更接近「该不该占 Google 词」）。无 Seller Center 账号时，用 FastMoss Sales List / Kalodata Shop 作近似替代。

#### 13.3.1 选品 / 品类 benchmark 信源（意图与解释）

> 以下信源服务于 **「该不该为这个品类占 Google 词」**（§13.4 业务验证）与 **TikTok 次级词 / 变体**（[§9](#9-目标关键词登记表) 备注）。**不能**替代 §13.2 的 Volume/KD；**不能**直接当 [§9](#9-目标关键词登记表) 主目标词——主词仍按 §14.1 模板 + Google 验证生成。

| 信源 | 链接 | 对应 §13.1 | 调研意图 | 解释 | 典型产出 | 不能替代 |
|------|------|---------|----------|------|----------|----------|
| **TikTok Shop · Product Ranking** | [Seller Center 官方说明](https://seller-us.tiktok.com/university/essay?knowledge_id=8671803954595597&lang=en) | TikTok 站内 | **验证品类 TTS 闭环** | 卖家中心一手数据。**TikTok Bestsellers**：同品类内按 GMV、clicks、CTR 排行，可按 LIVE / Video / Product card / Creator 拆渠道，benchmark 自己 vs 头部。**Popular Shoppable Videos**：按 views 排带货爆款，附带品名、价格区间、评分——用于看「什么视频形态带什么品」。入口：Seller Center → Analytics → Product → TikTok bestsellers & Popular shoppable videos；时间范围：单日 / 近 7 天 / 近 30 天（视频榜仅单日 / 近 7 天）。 | [§9](#9-目标关键词登记表) 变体/备注；hook 方向；§13.4 开 vertical 决策 | Google 搜索量；[§9](#9-目标关键词登记表) 主目标词 |
| **FastMoss · Sales List** | [fastmoss.com/e-commerce/saleslist](https://www.fastmoss.com/e-commerce/saleslist) | TikTok 站内 · 竞品(B) | **批量发现候选品类** | 公开/订阅向的 TikTok Shop **销量榜**：按国家、品类、时间筛 GMV、销量、订单增速。适合**横向扫榜**——从热品标题批量发现 [§9](#9-目标关键词登记表) 尚未登记的 broad category，并从 SKU 级标题抽次级词（如 `magnesium` → supplements、`MagSafe case` → phone-case）。配合 §13.5 `site:fastmoss.com {category} tiktok shop`，可同时看竞品 blog 已占哪些 `{category} TikTok Shop` 词。 | 候选 slug 清单；次级词；pSEO gap 线索 | Moras 内部出单验证；主词 Volume |
| **Kalodata · Shop** | [kalodata.com/shop](https://www.kalodata.com/shop) | TikTok 站内 · 竞品(B) | **热 SKU → category 反推** | 店铺/商品维度的 TTS 分析：热店、热品、品类 GMV、SKU 标题与类目路径。比 Sales List 更偏**单品深挖**——把具体爆款归并到 broad category（如 fajas → shapewear、Korean skincare → skincare），并与 Moras App 选品（§13.4）交叉。Kalodata 同时是 §13.5 B 类竞品，其 blog 常占 `{category} TikTok Shop` 长尾，可一并做 gap 分析。 | `{category}` 归并；变体/备注；与内部选品对齐 | 无 Seller Center 时的官方 benchmark（→ Product Ranking）；Google 主词 |

**推荐串联**（§13.3 → §13.4 → §13.5）：

```
1. FastMoss Sales List / Kalodata Shop     → 扫热品类、热 SKU（候选 category）
2. Seller Center Product Ranking（若有账号）→ 同品类 GMV + 爆款视频（官方 benchmark）
3. §13.2 Google Volume + §13.4 Moras 内部   → 决定是否开 vertical；套 §14.1 主/次级词
4. §13.5 Kalodata/FastMoss blog            → 拆变体、找 pSEO gap
5. 登记 §9 + §8
```

**决策对照**（与 §13.4 / §13.5 矩阵一致）：

| 外部榜单 / Ranking 信号 | Moras 内部 | 对 [§9](#9-目标关键词登记表) 的含义 |
|-------------------------|------------|--------------|
| 热 | 有出单 / 成片 | **优先**登记主词，§8 提高优先级 |
| 热 | 无需求 | 可做 pSEO 试验；§8 优先级靠后 |
| 冷 | 内部热 | **抢先**占词，快开 vertical |
| 冷 | 无 + Google Volume 低 | 暂缓，或仅作 TikTok 站内词运营 |

### 13.4 Moras 内部数据

> Moras 非公开 SEO 工具；以下指 **产品内已有或可达成的数据**，用于「该不该为这个品类占 Google 词」的**业务验证**，不替代 §13.2 的 Volume/KD。  
> 能力边界见 [moras-features.md](../moras-features.md)；竞品对照见 [moras-competitors.md](../moras-competitors.md)。

#### 可用数据源

| 来源 | 可提取信号 | 对找词的用途 |
|------|------------|--------------|
| **AI 选品 / 趋势模块**（App） | 美区 TTS 品类 GMV 增速、热 SKU、佣金区间 | 优先为「App 内已跑出量」的品类开 Vertical；主词 `{category}` 与热子类对齐（如 Korean skincare → skincare 次级词） |
| **成片 → 表现回灌飞轮** | 某品类链接的成片量、发布量、后续 GMV/佣金（Pro/MCN 用户） | 内部已验证转化潜力的品类，优先占 pSEO 词；备注「Moras 内有出单样例」 |
| **App 数据追踪 / Analytics** | 视频 engagement、转化向推荐、批量 hook 测试结果 | 从**高表现 hook/caption** 反推 TikTok 站内词，写入 [§9](#9-目标关键词登记表) 变体/备注 |
| **Wall of Love / 共创案例** | 用户自述品类（TTS、高佣品类、日产条数） | 佐证该 `{category}` 有真实买家；作定性参考 |
| **MCN / 托管档运营** | 某品类集中量产、重复选品 | 运营侧「已在服务的品类」优先登记 [§9](#9-目标关键词登记表) |
| **moras.ai GSC**（待接） | 已有曝光/点击 query、`/tiktok-video-generator/*` 页面表现 | 用**实际展示词**校正 [§9](#9-目标关键词登记表) 主/次级词；mattress 等 live 页优先分析 |

#### 推荐流程

```
1. 从 App 选品/趋势查看 Top 品类 / Top SKU 所属 category
2. 交叉：该品类在 Moras 内是否有成片量 + 可引用的 GMV/佣金叙事（勿写进 §9 表体，仅作开词决策）
3. 若内部热但 §9 无对应 slug → 在 §8 + §9 同步新增
4. 若某 slug 已在 §9 但 App 内无需求信号 → 降级优先级或标注「仅 pSEO 试验」
5. 将验证结论写入 §9「变体/备注」，例：`Moras 内有出单样例` / `App 选品 Top10 品类`
```

#### 局限

- 目前**无**对外公开的分品类 SEO dashboard；Volume 仍靠 §13.2 第三方工具
- 内部 GMV/出单率为用户个案或测试报道，**不可**写入对外承诺
- 内部数据反映 **TTS 闭环**，与 Google 搜索量可能不同步——须与 §13.2 交叉验证

### 13.5 竞品页面

> 从**已排名的竞品 URL** 拆 `{category}` 用词、意图变体、空白品类；**不是**抄 Title/页面结构（结构见 §4 / §5）。

#### 竞品分层

| 层级 | 代表 | 与 Moras 关系 | 找词看什么 |
|------|------|---------------|------------|
| **A. AI 成片 / TTS 工具** | [UGC AdMaker](https://ugcadmaker.ai/ai-tiktok-video-generator)、[Designkit](https://www.designkit.com/ai-video-generator/viral-video)、[CreatOK](https://www.creatok.ai/)、[HighReach TikTok Shops](https://highreach.ai/use-cases/tiktok-shops) | 重叠「链接→短视频」；多按 use-case 拆页 | 是否已有 `{category}` 落地页；URL slug、Title、H2 中的品类词 |
| **B. TTS 数据 / 选品** | [Kalodata](https://www.kalodata.com/)（~28.5k US 流量）、[FastMoss](https://www.fastmoss.com/)（~21.8k） | 重叠「选品」；blog 常占 `{category} TikTok Shop` 词 | Blog 类目词、爆款清单标题、FAQ long-tail |
| **C. SERP 占位页** | 联盟教程站、TTS 服务商、测评站 | 间接竞品 | 主词排名前 10 的 Title + URL |

*流量估算*：[moras-competitors.md](../moras-competitors.md) §2.1（Similarweb，非官方）。

#### 操作步骤

| 步骤 | 做法 | 产出 |
|------|------|------|
| 1. 定竞品清单 | A 类扫 use-case / features / blog；B 类扫 blog 类目 | 竞品域名列表 |
| 2. 扒有机词 | Ahrefs / Semrush：Organic keywords，筛 `tiktok shop`、`affiliate`、`video generator`、`{category}` | 竞品已占词列表 |
| 3. 扒落地页 | `site:domain.com tiktok` 或 sitemap；记 **URL + Title + H1** | 品类 / 用例页矩阵 |
| 4. 对照 [§9](#9-目标关键词登记表) | 竞品有、Moras 无 → 候选新 slug；双方都有 → 按 §14.4 差异化 | gap 清单 |
| 5. 拆变体 | 从竞品 Title 抽 `{category}` 表述、修饰词（AI / UGC / shoppable / for sellers） | 补充 §14.1 / §14.2 |
| 6. 登记 | 主词进 [§9](#9-目标关键词登记表)；竞品 URL 仅作调研记录，不内链 | 更新 [§9](#9-目标关键词登记表) + §8 |

#### 示例检索式（Google）

```
AI TikTok video generator {category}
{category} TikTok Shop affiliate video
site:ugcadmaker.ai OR site:highreach.ai tiktok
site:kalodata.com blog {category}
site:fastmoss.com {category} tiktok shop
```

#### 从竞品页重点提取

- **URL slug**：`use-cases/tiktok-shops` vs `/tiktok-video-generator/skincare` → 评估 Moras slug 是否更贴意图
- **Title 中的 category 词**：sellers / affiliates / brands / creators → §14.1 意图变体
- **H2 / FAQ 问句**：PAA 式 long-tail → §14.2 或 TikTok 备注
- **未覆盖品类**：竞品 blog 热但无工具 vertical → Moras pSEO 机会
- **已红海品类**：多竞品同词且 DA 高 → 改打 long-tail 差异化

#### 与 §13.4 的配合

| 信号组合 | 决策 |
|----------|------|
| 竞品有词 + Moras 内部有出单 | **优先**开 vertical，[§9](#9-目标关键词登记表) 登记主词 |
| 竞品有词 + Moras 内部无需求 | 可做 pSEO 试验，§8 优先级靠后 |
| 竞品无词 + Moras 内部热 | **抢先**占词，快开 vertical |
| 竞品无词 + 外部 Volume 低 | 暂缓，或仅作 TikTok 站内词运营 |

---

## 14. 关键词变体

### 14.1 意图变体（同一 Vertical 共用 slug）

以 `{category}` = displayName 自然英语为准：

| 变体类型 | 模式 | 示例（skincare） |
|----------|------|------------------|
| **主目标** | `AI TikTok video generator for {category} sellers` | …for skincare sellers |
| **联盟** | `{category} TikTok Shop affiliate` | skincare TikTok Shop affiliate |
| **成片** | `{category} TikTok Shop affiliate video` | skincare TikTok Shop affiliate video |
| **工具向** | `AI {category} TikTok video generator` | AI skincare TikTok video generator |
| **卖家向** | `{category} TikTok video generator for sellers` | skincare TikTok video generator for sellers |

**原则**：[§9](#9-目标关键词登记表)「主目标词」选 1 条作主优化；其余记入次级词或变体/备注，不另建 URL。

### 14.2 Long-tail 拆法

在 broad 品类词上叠加场景/属性，用于次级词或 TikTok caption，例如：

```
broad:     kitchen gadgets TikTok Shop
long-tail: space saving kitchen gadgets TikTok Shop
           meal prep gadgets small kitchen affiliate
```

常用叠加维度：`Korean / budget / best / for {persona} / small space / before and after`

### 14.3 品类称谓变体（开词前必验）

| slug | 待验证称谓 | 建议验证方式 |
|------|------------|--------------|
| `toiletry-bag` | toiletry bag · cosmetic bag · travel organizer | Google + TikTok autocomplete 搜量对比 |
| `skincare` | skincare · skin care | SERP 与 TikTok 高频形 |
| `cleaning-gadgets` | cleaning gadgets · cleaning tools | 同上 |
| `supplements` | supplements · wellness supplements | 与 health 子类区分 |

确定主称谓后：同步更新 [§9](#9-目标关键词登记表) `displayName`、§8、页面 config。

### 14.4 Cannibalize 规避

- 一 `{slug}` 一主意图；`lip-gloss` 与 `skincare` 不共用同一主目标词
- 次级词可交叉（如 Korean skincare 可作 skincare 次级、collagen 次级），但主词不可重复
- 新词若与 [§9](#9-目标关键词登记表) 已有行语义重叠 → 合并进变体/备注，不新开 vertical

---

## 15. 合规与品牌

- 仅 **TikTok Shop US**；FAQ 写清不支持区域
- Moras **非** TikTok/字节官方
- 对外统一 **Moras**（非 Morris 等误拼）
- caption 收益数字须可验证或标注示例
- FAQ 覆盖 AI 披露与平台政策（真实感 AI 内容须标注；2024-05 起自动读 C2PA 元数据打标）
- 商业内容需同时「品牌内容披露 + AI 标签」；直播带货禁用 AI 语音/预录音频/静态图（平台政策，非 Moras 承诺）
- 页面统一 `Last reviewed {month} {year}` 审查日期

---

## 16. 待办

### 16.1 开写前查证清单（R1–R5）

| ID | 需查证 | 优先级 |
|----|--------|--------|
| R1 | TTS 美区该品类 AOV、佣金 | P0 |
| R2 | 真实可购 TikTok 参考视频 URL | P0 |
| R3 | Moras 内成片样例 | P1 |
| R4 | Playbook URL live | P1 |
| R5 | 主称谓 SEO（[§14.3](#143-品类称谓变体开词前必验)） | P1 |

`toiletry-bag`：R1–R5 均为待查。

### 16.2 全局待办

- [ ] GSC/广告：[§9](#9-目标关键词登记表) 各 slug 补 **Volume**
- [ ] P0 slug：Creator Search Insights + autocomplete 验证次级词与 §14.3 称谓
- [ ] **Moras 内部**：从 App 选品/Analytics 导出 P0 品类需求信号，回写 §9 备注（§13.4）
- [ ] **竞品页**：对 A 类工具 + Kalodata/FastMoss 跑 gap 分析（§13.5 步骤 2–4），更新 P0 gap 清单
- [ ] 新 vertical：§8 + §9 同步登记
- [ ] 发布 live：确认 §9 主/次级词与实际上线页一致
- [ ] mattress §10.3 商品级关键词：与 Moras App 选品交叉验证

---

## 17. 外部信源

| 类型 | 链接 |
|------|------|
| TikTok Shop · Product Ranking（官方说明） | [Seller Center 官方说明](https://seller-us.tiktok.com/university/essay?knowledge_id=8671803954595597&lang=en) |
| FastMoss Sales List | [fastmoss.com/e-commerce/saleslist](https://www.fastmoss.com/e-commerce/saleslist) |
| Kalodata Shop | [kalodata.com/shop](https://www.kalodata.com/shop) |
| FastMoss Q1 爆款报告 | [Top Selling Products TikTok Shop US Q1 2026](https://www.fastmoss.com/blog/top-selling-products-tiktok-shop-us-q1-2026/) |
| Dashboardly 品类统计 | [TikTok Shop Category Statistics](https://www.dashboardly.io/statistics/tiktok-shop-category-product-statistics) |
| Creator Search Insights | [TikTok Creator Academy](https://www.tiktok.com/creator-academy/en/article/Creator-Search-Insights) |
| Canopy TikTok Shop SEO | [TikTok Shop SEO Strategy](https://canopymanagement.com/tiktok-shop-seo-strategy-rank-products-higher/) |
| 预览站 | [moras-navy.vercel.app/tiktok-video-generator](https://moras-navy.vercel.app/tiktok-video-generator) |
| 正式域 | [moras.ai/tiktok-video-generator](https://moras.ai/) |

---

## 18. 站内关联

[带货视频类型（video-types）](./moras-tiktok-video-generator-video-types.md) · [全站信息架构](../moras-site-structure.md) · [全站品牌/通用词](../moras-keywords.md) · [README 运营手册](./README.md)

---

*Moras · TikTok Video Generator（合并主文档）· https://moras.ai/tiktok-video-generator*
