## §2 文章类型路由

收到任务后**先匹配类型**，再跳转对应 H2 模板。

### 2.1 路由表

| 类型 | 典型 intent | 词数 | 产品提及上限 | 默认 Mode | 参考 slug |
|------|------------|------|-------------|:---:|-----------|
| **Pillar** | 变现全景 / 收入地图 | 3500–5000 | ≤20% | flagship | `how-to-make-money-on-tiktok` |
| **Setup** | 入驻路径对比 | 2500–3500 | ≤25% | standard | `tiktok-shop-setup` |
| **Production** | 不出镜 / 成片路径 | 2800–3800 | ≤35% | standard | `faceless-tiktok-shop-videos` |
| **Research** | AI 选品框架 | 2800–3500 | ≤30% | flagship | `tiktok-product-research` |
| **Framework** | 钩子/机制框架（非清单） | 2500–3200 | ≤25% | flagship | `tiktok-video-hooks` |
| **Strategy** | 文案/标签/描述策略 | 2500–3200 | ≤30% | standard | `tiktok-captions-hashtags` |
| **Side Hustle** | 副业时间线/收入预期 | 2200–3000 | ≤30% | standard | `tiktok-affiliate-side-hustle` |
| **Diagnosis** | 零销量/低转化排查 | 2500–3200 | ≤25% | standard | `tiktok-shop-no-sales` |
| **Platform Ops** | TikTok 平台操作/工具 | 1800–2500 | ≤15% | lite | `tiktok-shop-toolkit` |

**路由规则**：

- `how to make money` / 多 lane 排名 / monetization map → **Pillar**
- `setup` / 两条路径 / seller vs affiliate 入驻 → **Setup**
- `without filming` / `no camera` / faceless → **Production**
- `product research` / `winning products` / AI 选品 → **Research**
- `hooks` + framework / 心理机制 / 非列表 → **Framework**
- `captions` / `hashtags` / descriptions → **Strategy**
- `side hustle` / part-time / 90-day timeline → **Side Hustle**
- `no sales` / not converting / diagnosis → **Diagnosis**

### 2.2 全类型通用模块（Moras 成稿惯例）

| 模块 | 要求 |
|------|------|
| **TL;DR** | frontmatter 关闭 `---` 后**正文第一块**（无前置段落）；`## TL;DR` 含**一段长描述**（60–110 词，兼承担 Lead 的 hook + BLUF）+ **3–6 条 bullet**；后接 `---` 再进正文 H2 |
| **发布日期** | `date` / `isoDate` **全库唯一**；同一 `isoDate` 不得出现两篇；新稿 = 当前 portfolio 最晚日期 +1 天（见 `moras/blog/README.md` 日期表） |
| **H2** | 英文描述性 `##` 标题；**不强制编号**（与 floatboat/vofy 不同） |
| **Conclusion** | `## Conclusion`（FAQ 之上） |
| **FAQ** | `## Frequently asked questions`；每题 `### 问题` + 段落回答；≥3 题 |
| **内链** | 正文 ≥2 其他 blog slug；Pillar/Spoke 互链；**自然优先**——语境不通不强链；同 slug 同篇 ≤2 次；TL;DR/FAQ 无内链；H2 均匀分布 · 详见 `internal-links.md`；禁 G6 |
| **外链** | 权威 2–8；竞品/TikTok 政策 `rel="nofollow noopener"` HTML |
| **列表比例** | Pillar/Setup ≤25%；Framework/Research ≤30%；Production/Strategy ≤35% |
| **长段落** | ≥3 段 4–8 句（80–200 words）；避免连续 3+ 短段簇 |
| **CTA** | 单一主行动（Download Moras / TVG）；全文 ≤2 次；正文内链承担导流 |
| **美区限定** | 涉及 TikTok Shop 须明示 **US** 或等价语义 |
| **联盟客优先** | 默认面向 affiliate；seller 仅作对比或次要 persona |
| **无 Related** | Moras 博客**不用** `## Related articles` 模块（内链分布在正文） |

**结构顺序（全类型）**：`## TL;DR`（长描述 + bullets）→ `---` → 正文 H2… → `## Conclusion` → `## Frequently asked questions`

### 2.3 Pillar — H2 模板

**叙事弧线**：行业变化 → 收入地图（表格）→ 按 persona 分节 → 常见错误 → 工具注记（克制）→ 结论。

```
## TL;DR
{60–110 词 BLUF 长描述 — hook + 直接回答 primary intent}
- {可执行要点 1}
- {可执行要点 2}
- …

---

## What's actually changed since {year}
## The {year} income map          ← 对比表：lane / income / time / hardest part
## How much you'll actually earn — by persona
   ### If you have no audience yet
   ### If you're a small creator (under 10k)
   ### If you're a mid-tier creator
   ### If you already sell products
## {N} mistakes that quietly kill earnings
## A note on AI tools              ← Moras 可出现；tool-agnostic 为主
## Conclusion
## Frequently asked questions
```

**Pillar 专属**：须链向所有 Spoke；表格前须有分析段；persona 节各 ≥1 具体数字或区间。

### 2.4 Setup — H2 模板

**叙事弧线**：两条路径定义 → 逐步对比 → 决策树 → FAQ。

```
{Lead}
## {Path A} vs {Path B} — what each actually means
## Step-by-step: {Path A}
## Step-by-step: {Path B}
## Which path fits your starting conditions
## Common setup mistakes
## Conclusion
## Frequently asked questions
```

### 2.5 Production — H2 模板

**叙事弧线**：生产瓶颈 → 四条路径一览表 → 分路径深讲 → 选型决策 → Moras 在链路中的位置（后段）。

```
{Lead}
## The production bottleneck nobody talks about
## What "without filming" actually means
   ### The four paths at a glance    ← 表格
## Path 1: …
## Path 2: …
## Path 3: …
## Path 4: …
## How to pick the right path for your SKU count
## Conclusion
## Frequently asked questions
```

### 2.6 Research — H2 模板

**叙事弧线**：为何 shadowing 失效 → 四信号框架 → 工具层 → AI workflow → 避坑。

```
{Lead}
## Why "scroll and copy" does not work anymore
## The four signals that separate winners from traps
   ### Signal 1–4（各含 metric + 反例）
## Reading the data layer（含工具公平对比）
## An AI-assisted research workflow
## Products to avoid（red flags）
## Conclusion
## Frequently asked questions
```

### 2.7 Framework — H2 模板

**叙事弧线**：批判清单文 → 定义机制 → 分机制深讲 → 品类匹配表 → 测试方法。**禁止**写成 "50 hooks you can copy"。

```
{Lead — 清单文为何不是策略}
## Why {topic} lists are not a strategy
## The {N} {mechanisms} that drive conversion
   ### Mechanism 1: …
   ### Mechanism 2: …
   ### Mechanism 3: …
## Matching {mechanisms} to product categories   ← 表格
## How to test systematically（非猜测）
## Conclusion
## Frequently asked questions
```

### 2.8 Strategy — H2 模板

```
{Lead}
## Why most {captions/hashtags} advice fails
## The three layers of …（或等效框架）
## What to write for {scenario A/B/C}
## What to avoid
## Conclusion
## Frequently asked questions
```

### 2.9 Side Hustle — H2 模板

```
{Lead — 反驳 screenshot 文与 debunk 文}
## What the earnings screenshots do not show you
## The time budget: what 90 minutes a day produces
## The 90-day validation sequence
   ### Days 1–30 / 31–60 / 61–90
## When to quit vs when to double down
## Conclusion
## Frequently asked questions
```

### 2.10 Diagnosis — H2 模板

```
{Lead}
## Stop treating every failure as the same failure
## Bottleneck 1: …（metric + fix）
## Bottleneck 2: …
…
## Bottleneck 5: …
## The diagnostic decision tree（可选）
## Conclusion
## Frequently asked questions
```

### 2.11 Slug、Title、Description 规则

| 项 | Moras 执行 |
|----|-----------|
| **frontmatter slug** | `/blog/{kebab-case}`；常青；**路径已含 `/blog/`** |
| **文件名** | `NN-{working-slug}.md`；working-slug 可与 URL slug 不同 |
| **title** | editorial；45–65 chars；Pillar 可含 `(2026)`；通常 **不加** `\| Moras` |
| **description** | 140–160 chars；读者得到什么 + 主关键词 |
| **Pillar 年份** | title 可含年份；**slug 不含年份** |
| **完整 meta 规则** | 计字符、四条自检、独立优化工作流 → `meta-title-description.md` |

**Slug 反模式速查**：

| 反模式 | 错误 | 正确 |
|--------|------|------|
| slug 缺前缀 | `tiktok-video-hooks` | `/blog/tiktok-video-hooks` |
| slug 含年份 | `/blog/make-money-tiktok-2026` | `/blog/how-to-make-money-on-tiktok` |
| 连续重复词 | `/blog/tiktok-tiktok-shop-hooks` | `/blog/tiktok-video-hooks` |
| 内部文件名泄漏 | URL 用 `tiktok-shop-hooks-framework` | URL 用 `tiktok-video-hooks`（搜索意图优先） |

**Slug "大声读"测试**：去掉连字符大声读 → 通顺 → 通过。

**Title 公式示例**：

- Pillar：`How to Make Money on TikTok in 2026`
- Production：`How to Make TikTok Shop Videos Without Filming in 2026`
- Framework：`TikTok Shop Hooks That Actually Convert: A Framework, Not a List`
- Diagnosis：`Why You Are Not Making Sales on TikTok Shop — A Diagnosis Framework`

### 2.12 Frontmatter Schema

```yaml
---
title: "Editorial Title — Subtitle After Em Dash (if needed)"
description: "140–160 chars, benefit + main intent keyword for SERP"
slug: "/blog/kebab-case-slug"
date: "June 15, 2026"       # 人类可读；与 isoDate 同一天
isoDate: "2026-06-15"        # YYYY-MM-DD；portfolio 内唯一，一天一篇
updated: "2026-06-15"        # 末次实质修订；无修订则与 date 相同
author: "Kostja"
category: "Creator & Affiliate"   # 必填；枚举见 §2.12b
secondaryCategory: "Guide"         # 可选；如 Guide / HowTo / Framework
---
```

### 2.12b category 枚举

| category | folder | 适用 NN |
|----------|--------|---------|
| Creator & Affiliate | `creator-affiliate/` | #01–02, #04, #06–09, #44 |
| TikTok Video | `tiktok-video/` | #03, #05, #25–#42 |
| Content & Discovery | `content-discovery/` | #26–#30, #47 |
| Platform Ops | `platform-ops/` | #10–#14, #16, #18–#22, #43, #45–#46, #48 |
| E-commerce AI | *(root)* | #31–#34 |

## §8 Voice 与合规

### 8.1 正向 Voice

| 维度 | 要求 |
|------|------|
| Clear | 非专业读者能复述核心框架 |
| Affiliate-first | 联盟客佣金语境；非企业采购文 |
| Evidence-led | Reuters、TikTok transparency、Oxford Economics 等可引用 |
| Framework-led | 机制/信号/瓶颈；禁空泛清单 |
| Honest ranges | 收入用区间 + 条件；禁保证 |

### 8.2 禁止

- revolutionary · game-changing · unlock · seamless · guaranteed income · official TikTok partner
- 把证言 GMV 写成典型结果
- 虚构 "I made $10k in 30 days" 案例（除非标注 testimonial + 来源）
- 空泛句：In today's world / Let's dive in / It is important to note that / Without further ado
- Framework 文退化为 hook 列表

### 8.3 按类型产品策略

| 类型 | Moras 策略 |
|------|-----------|
| Pillar | "A note on AI tools" 段；tool-agnostic 为主 |
| Setup | ≤25%；中立路径对比 |
| Production | 四路径后链 TVG/首页 |
| Research | 工具公平对比 + workflow 段 |
| Framework | 全文后 30%+ 可选工具；主体是机制 |
| Strategy | workflow 节轻提 Moras |
| Side Hustle | 时间线为主；产品 optional |
| Diagnosis | 排查框架为主；产品 optional |

---




## Who / How / Why 模块（Moras 博客强制）

按 Google [Who/How/Why](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) 框架，每篇新增以下模块：

| 模块 | 位置 | Pillar/Framework/Research | 其他类型 |
|------|------|:---:|:---:|
| **Who** | TL;DR 长描述或 Conclusion 前 | 必填 | 可选 |
| **How** | Research/Framework 文 Conclusion 前 | 必填 | 可选 |
| **Why** | TL;DR 长描述段 | 必填 | 建议 |

**Who 模板**：
> This article was written by Kostja, based on analysis of US TikTok Shop affiliate workflows and creator economics data as of {month} {year}.

**How 模板**（Research/Framework 文）：
> ## How we researched this
> Data sources include TikTok Shop Seller Center policies, Reuters reporting on TikTok Shop US GMV, [additional sources]. Internal observations are based on analysis of ~{N} shoppable videos across {categories} in {time period}. Frameworks in this article are original analysis, not aggregated from existing blog posts.

**Why 模板**（TL;DR 长描述段融入）：
> This article helps US TikTok Shop affiliates make {specific decision} — not to promote any single tool. Where Moras appears, we've noted it explicitly.

**AI 辅助披露**：若正文大量依赖 AI 生成的工作流示例，在 FAQ 中加 1 题：
> ### Was this article written by AI?
> The frameworks and analysis are human-designed. Some workflow examples were generated with AI assistance and reviewed for accuracy. See [How we researched this](#how-we-researched-this) for data sources.
