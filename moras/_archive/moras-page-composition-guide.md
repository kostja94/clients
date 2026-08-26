# 页面搭建指南：Moras 官网

> **状态**：已归档（2026-08-26）。不再作为现行文档维护。

面向内部同事（工程 / 内容 / 设计），讲清楚我们如何用「共享骨架 + 类型化 data 契约」的方式，快速搭一个新的 Moras landing / product / use-case / glossary / blog 页面，并保持整站结构与内链一致。

本文只讲**页面结构、组件复用等级、内链关系**。视觉规则、博客正文版式、SEO 关键词研究不在范围内。

---

## 速查卡

> 如果你只读 30 秒，从这里开始。

| 概念 | 一句话 |
|---|---|
| ✅ 共享组件 | 直接 import 同一个 `.tsx`，只传 props（Navbar、Breadcrumbs、Footer、SecondaryCTA、FaqSection、PageHero）|
| 🔁 结构共享，数据定制 | 模板组件读一份 typed data 契约（ProductPageTemplate、PersonaTemplate）|
| 🧩 模式共享，组件独立 | 视觉/字段契约一致但独立组件（AudienceGrid、ValueGrid、FeatureGrid、SkuShowcase、VideoGallery、StepsRow、CompareGrid、ProblemSolution、MetricsStrip）|
| ❌ 本页专属 | 不进复用池 |
| 页面骨架 | `Navbar → Breadcrumbs → PageHero → …内容 blocks… → FaqSection → SecondaryCTA → Footer` |
| 硬性规则全文 | 共 15 条 Hard Rule，完整索引见 [附录 C](#附录-char-rule-完整索引) |
| 最快路径 | Blueprint 规划 → 编码（按 Checklist B）→ 发布前自检（按 Checklist C，4 条 Hard Rule 必须绿灯）|

### 我该从哪开始？

| 你是 | 先读 |
|---|---|
| 第一次看这份文档 | §1 核心理念 → §2 工作流 → §3 Case Study |
| 要搭新页面 | §2 工作流 → §9 Checklist → §10 反例 |
| 要写文案 | §4 AudienceGrid 文案规则 → 附录 B 模板 → §10 反例 |
| 要判定复用等级 | §1 复用等级说明 → §3.1 字段填充差异 |
| 要查某个组件的规范 | 直接在目录里找对应 section（AudienceGrid / VideoGallery / ValueGrid / …）|

---

## 1. 核心理念

一个 Moras 页面 = **共享骨架 block** + **若干内容 block**。

- **共享骨架**（6 个，所有页面必须存在，顺序固定）
  `Navbar → Breadcrumbs → PageHero → …内容 blocks… → FaqSection → SecondaryCTA → Footer`
- **内容 block**（可复用、结构固定、**文案按页定制**）
  `ValueGrid / StepsRow / SkuShowcase / VideoGallery / FeatureGrid / MetricsStrip / AudienceGrid / CompareGrid / ProblemSolution`

同一个内容 block 在不同页面里：

- **组件结构完全一致**（栅格、动画、卡片视觉、字段契约）
- **文案完全不同**（针对当前产品/角色/术语挑选最相关的叙事）
- 通过描述里的**上下文内链**（自然锚文本 `<Link>`），把权重回流到 `/use-cases` / `/glossary` / 姐妹产品页

### 复用等级

每个页面 section 都需要明确复用等级。Moras 定义了 4 级：

| 等级 | 含义 | 例子 |
|---|---|---|
| ✅ 共享 | 直接 import 同一个 `.tsx`，只传 props | `Navbar`、`Breadcrumbs`、`Footer`、`SecondaryCTA`、`FaqSection`、`PageHero` |
| 🔁 结构共享，数据定制 | 模板组件读一份 typed data 契约，换数据 = 换页面 | `ProductPageTemplate` 读 `ProductPageData`；`PersonaTemplate` 读 `personas.ts` 里的一条 persona |
| 🧩 模式共享，组件独立 | 视觉/字段契约一致，但目前是独立组件 | `AudienceGrid` / `ValueGrid` / `FeatureGrid` / `SkuShowcase` / `VideoGallery` |
| ❌ 本页专属 | 不进复用池，仅此页使用 | `/models` 的模型卡网格、`/glossary` 的字母表锚点导航 |

### 模板 + 条件渲染

同类产品页（`/tiktok-shop-products-finder` / `/tiktok-video-generator` / `/tiktok-video-analyzer`）共享同一份 `ProductPageTemplate`。当某个页面有其它页面不需要的独特叙事时（如 Video Generator 需要 `VideoGallery` + `SkuShowcase`，Products Finder 只需要 `FinderPreview`），在 `ProductPageData` 里**只填对应字段**触发条件渲染，**而不是新建 `.tsx`**。

---

## 2. 设计新页面的工作流（先规划，再动手）

**不要**上来就复制某个页面开始改文案 —— 那是 vibe coding，会漏掉本页真正需要的独特 block，也会把模板里用不上的 section 顺手留下。

### 2.1 三步规划

1. **定位页面类型**：属于以下哪一类？找出 1–2 个最接近的现有页面作为参考。
   - **产品页**（3 个：finder / generator / analyzer）
   - **use-case 页**（`/use-cases/*`，共 5 个 persona）
   - **hub 页**（`/use-cases`、`/blog`、`/glossary`、`/models`）
   - **文章页**（`/blog/<slug>`，见 `docs/blog-article-spec.md`）
   - **落地页**（`/download`、`/pricing`、`/features`、`/about`）
2. **列叙事顺序**：写下用户滚到每一段应该获得的信息（不是 section 名，而是「用户在这里获得什么」），再把每条叙事映射到组件。
3. **对每个组件判定复用等级**（✅ / 🔁 / 🧩 / ❌），并标注：
   - ✅ / 🔁：列共享组件名 + 需要传的 data 字段
   - 🧩：列出参考的镜像组件（如新 use-case 页的 audience 参考 `video-generator.ts` 的 audience 段）
   - ❌：说明为什么其它页面不需要，证明它确实是本页专属

### 2.2 用 ASCII 骨架落地规划

在 PR 描述或 `docs/blueprints/<page>.md` 下画 ASCII tree。例：新增 `/use-cases/kol-agencies`：

```text
KolAgenciesUseCasePage
├── Navbar                       ✅ 共享
├── Breadcrumbs                  ✅ 共享     items: Home › Use Cases › KOL Agencies
├── PageHero                     ✅ 共享     centered, 1 CTA → App Store
├── ValueGrid                    🧩 模式共享  3 段：批量接单 / 达人分派 / 结算对账
├── StepsRow                     🧩 模式共享  3 步：Onboard → Assign → Report
├── AudienceGrid                 🧩 模式共享  3 卡片：Agency owner / Producer / Talent lead
├── CompareGrid                  🧩 模式共享  Moras vs 手工排期 vs 传统 MCN SaaS
├── FaqSection                   ✅ 共享     8 条 agency 相关 QA
├── SecondaryCTA                 ✅ 共享     "Run every KOL like one team"
└── Footer                       ✅ 共享
```

**收益**：一眼看出新组件（❌）/ 镜像组件（🧩）/ 工作量；section 顺序是文档不是代码；未来读代码的人打开 blueprint 就懂设计意图。

### 2.3 Blueprint 模板

Copy 以下结构作为 blueprint 模板：

---

# &lt;PageName&gt; Blueprint

## 页面定位
- 类型：产品页 / use-case 页 / hub 页 / …
- 参考页面：&lt;path/to/reference.tsx&gt;
- 目标关键词：&lt;seo keywords&gt;

## 叙事顺序
1. 用户滚到 X 时应该获得 Y 信息
2. …

## Section 骨架（ASCII）

    PageName
    ├── Navbar                       ✅ 共享
    ├── Breadcrumbs                  ✅ 共享
    ├── PageHero                     ✅ 共享
    ├── ...                          🧩 模式共享
    ├── FaqSection                   ✅ 共享
    ├── SecondaryCTA                 ✅ 共享
    └── Footer                       ✅ 共享

## 新增组件清单
- ❌ `&lt;PageName&gt;&lt;Feature&gt;.tsx` — 用途 / 为什么其它页面不需要
- 🧩 `&lt;Block&gt;.tsx` — 镜像自 &lt;existing&gt;

## 复用组件清单
- ✅ / 🔁：&lt;component&gt; + 关键字段

---

**[Hard Rule]** blueprint 评审通过后再写 `.tsx`。

---

## 3. Case Study：TikTok Video Generator 页面拆解

文件：`src/routes/tiktok-video-generator.index.tsx` → 渲染 `ProductPageTemplate` + `videoGeneratorData`（`src/content/product-pages/video-generator.ts`）。

| 顺序 | Section | 组件 | 数据字段 | 复用等级 | 说明 |
|---|---|---|---|---|---|
| 1 | Nav | `Navbar` | — | ✅ | 全站统一 |
| 2 | 面包屑 | `Breadcrumbs` | `breadcrumb` | ✅ | 3 级 |
| 3 | Hero | `ProductHero` | `hero` | 🔁 | H1 + 2–3 行描述 + 1 CTA |
| 4 | 视频轮播 | `VideoGallery` | `videoGallery` | 🧩 | 5 条真实 TikTok Shop 案例 |
| 5 | SKU 差异化 | `SkuShowcase` | `skuShowcase` | 🧩 | 4 品类切换（Mattress/Skincare/Kitchen/Perfume）|
| 6 | 能力叙事 | `ValueGrid` | `valueProps` | 🧩 | Clink 风格 6/6 交替，3 段 |
| 7 | 受众 | `AudienceGrid` | `audience` | 🧩 | 3 张 persona 玻璃卡 |
| 8 | 对比 | `CompareGrid` | `compare` | 🧩 | vs UGC creators vs CapCut |
| 9 | How it works | `StepsRow` | `steps` | 🧩 | 3 步，含 HowTo JSON-LD |
| 10 | FAQ | `FaqSection` | `faq` | ✅ | H2 + H3，FAQPage JSON-LD |
| 11 | 最终 CTA | `SecondaryCTA` | `finalCta` | ✅ | 单 CTA → App Store |
| 12 | Footer | `Footer` | — | ✅ | 全站统一 |

`products-finder` 与 `video-analyzer` 遵循同样的模板：**换一份 `ProductPageData` 就得到一个新页面**，不需要新建 `<Product>Hero.tsx` / `<Product>FAQ.tsx` 之类的薄壳。

### 3.1 三个产品页字段填充差异

同一份 `ProductPageData` 契约，不同产品**只填对应字段**触发条件渲染。下表用 ✅ = 填 / — = 留空 直观展示差异：

| 字段 | Products Finder | Video Generator | Video Analyzer |
|---|---|---|---|
| `hero` / `audience` / `compare` / `faq` / `finalCta` | ✅ | ✅ | ✅ |
| `steps` | ✅ | ✅ | ✅ |
| `previewSlot` | `finder-preview` | `flow-strip` | `analyzer-preview` |
| `videoGallery` | — | ✅ (5 条真实带货视频) | — |
| `skuShowcase` | — | ✅ (4 品类切换) | — |
| `valueProps` | ✅ | ✅ | ✅ |
| `features` | ✅ (10 卡) | — | ✅ (12 卡) |
| `metrics` | ✅ (GMV / rising) | — | ✅ (hook / retention) |
| `problem` | ✅ | — | ✅ |

**判定原则**：字段是「加分叙事」而非「必要 section」，能空就空 —— 页面短一屏，跳出率下一档。**[Hard Rule]** 不允许为了「填满模板」硬凑内容。

### 3.2 迷你 Case：/use-cases/affiliates 拆解

文件：`src/routes/use-cases.affiliates.tsx` → 渲染 `PersonaTemplate` + `personas.ts` 里 `slug === "affiliates"` 的那条。

| Section | 组件 | 数据来源 | 说明 |
|---|---|---|---|
| Hero | `PageHero` | `persona.hero` | 居中，1 CTA → App Store |
| Value grid | `ValueGrid` | `persona.capabilities` | 3 段图文交替（推爆品 / 一键出视频 / 追踪佣金）|
| Steps | `StepsRow` | `persona.steps` | 3 步 |
| Product spotlight | `AudienceGrid` 的镜像用法 | `persona.products` | 3 张产品卡（finder / generator / analyzer）—— 主语是 affiliates 场景 |
| Compare | `CompareGrid` | `persona.compare` | vs 手动选品 + 拍摄 |
| FAQ + SecondaryCTA + Footer | ✅ 共享 | — | 全站统一 |

**镜像验证**：`/tiktok-video-generator` 的 audience 卡片里也有一张「For Affiliates Chasing Daily Commission」；两处 `title` 相同，但 `/use-cases/affiliates` 里主语是 affiliate 场景（Video Generator 是宾语之一），`/tiktok-video-generator` 里主语是 Generator（affiliate 是三个宾语之一）。两处的 `description` **必须**根据主语不同重写。

---

## 4. 重点示范：AudienceGrid 组件模式

Moras 里最重要的**可跨模板复用**内容 block。

### 4.1 组件契约

所有 audience 段共用 `Persona` 类型（`src/content/product-pages/types.ts`）：

```ts
type Persona = {
  name: string;        // H3：For <role>（如 "Affiliates Chasing Daily Commission"）
  pain: string;        // 一句现状痛点
  out: string;         // 一句 Moras 给出的产出
  checks?: string[];   // 可选：3–4 条能力清单
  to?: RouteTo;        // 可选：回链到 /use-cases/<slug>
};
```

字段填法详解：

| 字段 | 必填 | 什么时候填 | 反例 |
|---|---|---|---|
| `name` | ✅ | 永远以 `For <role>` 或结果导向短句开头 | ❌ 用抽象名词 "Growth Team"（读者不知道谁）|
| `pain` | ✅ | 一句现状（≤ 15 词）陈述当前手工做法有多痛 | ❌ 写成产品广告 "Without Moras it's hard…" |
| `out` | ✅ | 一句 Moras 输出（20–30 词），主语是「你」或「Moras」 | ❌ 复制其它产品页的 out 文案 |
| `checks` | 可选 | AudienceGrid 目前不渲染 checks；仅 PersonaTemplate 详情页用 | — |
| `to` | 可选 | 该角色在 `/use-cases/*` 有独立详情页时填；无则留空、不加假链接 | ❌ 链到不存在的 `/use-cases/foo` |

视觉：3 列毛玻璃卡 + `framer-motion` 淡入 + 居中标题。

### 4.2 三个现有实例对比

| 页面 | Persona 挑选 | 跨页内链 |
|---|---|---|
| `/tiktok-shop-products-finder` | Affiliates / Sellers / Dropship | `/use-cases/affiliates` / `/use-cases/dropship` |
| `/tiktok-video-generator` | Affiliates chasing commission / Sellers testing creative / Creators pitching brand deals | `/use-cases/affiliates` / `/use-cases/tiktok-sellers` / `/use-cases/creators` |
| `/tiktok-video-analyzer` | Creative leads / Media buyers / Agencies | `/use-cases/agencies` |

**关键观察**：三个页面共用同一份视觉模板，但**没有一张卡片文案是重复的** —— 每个产品挑对自己叙事最有说服力的角色，并把 `out` 里的锚文本自然链到 `/use-cases/*`。

### 4.3 文案编写规则

搭新页面 audience 段时：

1. **打开 `src/components/site/use-cases/personas.ts`**，浏览已有 5 个 persona slug
2. **挑 3 个与本页高度相关的 persona**，`name` 用 `For <role>` 或结果导向短句
3. **`pain` 一句现状**（≤ 15 词），**`out` 一句 Moras 输出**（20–30 词）
4. **在 `out` 里用自然语言锚文本回链** `/use-cases/<slug>`，不用「Learn more →」按钮式
5. **[Hard Rule]** 不复制其它产品页的 `out` 文案；每页 audience 必须按当前产品叙事重写
6. **[Recommended]** 3 张卡片是当前视觉最稳的数量；4 张也可接受，5+ 会破 grid

### 4.3.1 示例：同一 persona 在两个产品页的正确与错误写法

同一个「Affiliates」角色，在两个不同产品页出现时的正确 vs 错误写法：

**❌ 坏例子（Products Finder 页直接复制 Video Generator 页 out）：**

```ts
{
  name: "For Affiliates Chasing Daily Commission",
  pain: "Manual scouting eats hours before a single video ships.",
  out: "Render five shoppable cuts before lunch — affiliate link, hook and CTA baked in.",
}
```

主语错了：Products Finder 不产出视频，`out` 承诺了它做不到的事。

**✅ 好例子（Products Finder 页按当前产品叙事重写 out）：**

```ts
{
  name: "For Affiliates Chasing Daily Commission",
  pain: "Manual scouting eats hours before a single video ships.",
  out: "Spot rising SKUs and 3× commission products in minutes, then pass the winners straight to your video queue.",
}
```

**✅ 好例子（Video Generator 页里保留原文，因为主语匹配）：**

```ts
{
  name: "For Affiliates Chasing Daily Commission",
  pain: "You know which SKU wins — but filming eats the whole afternoon.",
  out: "Render five shoppable cuts before lunch — affiliate link, hook and CTA baked in, ready to post from your phone.",
}
```

**验证方法**：把 `out` 里的动词拎出来，必须能被当前产品**真的做到**。Finder → spot / rank / export；Generator → render / script / caption；Analyzer → score / diagnose / benchmark。

### 4.4 什么时候用 AudienceGrid

**适合放**：任何需要「多角色覆盖」叙事的页面 —— 3 个产品页 + `/features` + `/pricing` + 未来的行业落地页。

**不适合放**：单场景工具页（如 `/tools/tiktok-caption-generator`），此时用 `StepsRow` 或直接落 CTA 更合适。

---

## 5. VideoGallery / SkuShowcase 的 SEO 定位

这是 Moras 页面里唯二**「视觉高度固定但可堆内容」**的 block。

- **VideoGallery**：横向 shadcn Carousel + TikTok embed，可放 5–10 条真实 TikTok Shop 视频。每条 `label` 里带品类关键词（Mattress · Bedroom / Skincare · Beauty …），爬虫全部计入正文，但用户只看头 1–2 张
- **SkuShowcase**：左图右文的品类切换 tab，每个品类一段 40–70 词的 H3 + 描述。适合承载长尾 SKU / 品类关键词

### 5.1 写作规则

1. **每张视频 / 品类 tab 都在 `label` / `body` 里自然埋关键词**（品类词 · 场景词 · 平台词）
2. **`body` 里加 1–2 个上下文 `<Link>`**，指向 `/glossary#<term>` 或姐妹产品页
3. **[Recommended]** VideoGallery 5–8 条最佳；SkuShowcase 3–5 个品类最佳
4. **图片契约锁死 1200×630**（防止 SkuShowcase 高度飘）

### 5.1.1 SkuShowcase 适用场景判定

SkuShowcase 只服务「同一产品能力落到多个明确品类」的场景。判定：

| 产品/页面 | 该用 SkuShowcase？ | 原因 |
|---|---|---|
| Video Generator | ✅ | 生成视频天然按品类分（Mattress / Skincare / Kitchen / Perfume），每个品类的痛点 + 出口都不同 |
| Products Finder | ❌ | 选品是单一工作流；品类差异应放到 `features` 或 blog 长尾页 |
| Video Analyzer | ❌ | 分析对象是「视频结构」不是「SKU」；差异应用 `features` 讲维度（hook / retention / CTA）|
| /use-cases/* | ❌ | 场景已经聚焦到一个 persona，再切品类会分散注意力 |

**[Hard Rule]** SkuShowcase 只允许在产品页出现，且当前产品必须自然能按品类切分。不要为了「页面多一段」硬造品类。

### 5.2 为什么其它 block 不能这样堆

Hero / CTA / FAQ / AudienceGrid / CompareGrid 都是**纵向 stack**，堆内容 = 页面变长 = 跳出率上升。VideoGallery / SkuShowcase 是唯二内容量与视觉高度解耦的组件，因此是长尾 SEO 主力。

---

## 6. ValueGrid / FeatureGrid：6/6 交替 vs 三列卡片

两个视觉相似的 block，但用途不同：

| 组件 | 用途 | 布局 | 条目数 |
|---|---|---|---|
| `ValueGrid` | 讲**能力叙事**（3–5 段长文，每段配 1200×630 图） | 6/6 交替，image left/right alternating | 3 段 |
| `FeatureGrid` | 讲**功能矩阵**（8–12 个卡片，短标题 + 1 句） | 3 列卡片 | 8–12 |

### 6.1 使用规则

- ValueGrid **图片必须 1200×630**（`aspect-[1200/630]` 已锁），否则高度飘、破节奏
- 每段 body 40–90 词，允许 `<Link>` 内链
- FeatureGrid 每条卡 `title` ≤ 5 词，`desc` ≤ 20 词，图标可选（视频生成器不用图标）

---

## 7. 双向内链：Product ↔ Use Case ↔ Glossary ↔ Blog

Moras 页面复用的**核心理念** —— 同一份卡片契约可以两个方向使用，主语 ↔ 宾语互换：

| 方向 | 所在页面 | 组件 | 主语（固定） | 宾语（挑选 + 改写） |
|---|---|---|---|---|
| Product → Use Case | `/tiktok-video-generator` | `AudienceGrid` | Video Generator | 挑 3 个 persona |
| Use Case → Product | `/use-cases/affiliates` | `PersonaTemplate` 内的 product spotlight | Affiliates 场景 | 挑 3 个产品 |
| Product → Glossary | product 页 `ValueGrid` / `SkuShowcase` 描述 | 内嵌 `<Link>` | 产品能力 | 链 `/glossary#spark-ads` |
| Blog → Product | `/blog/<slug>` 正文 | 内嵌 `<Link>` | 文章主题 | 链 `/tiktok-video-generator` |
| Glossary → Blog / Product | `/glossary` 术语描述 | 内嵌 `<Link>` | 术语 | 链解释该概念的文章 / 产品 |

**镜像原则**：同一个产品在不同 use-case 页 `title/image/href` 完全一致，但 `description` **必须按当前场景改写**；同一个 persona 在不同 product 页也是同样规则。

---

## 8. 骨架组件的统一规则

### 8.1 SecondaryCTA

- **每页 1 个**（`SecondaryCTA.tsx`），位置固定：Footer 上方
- 只包含：H2 + 1 段描述 + 1 个 CTA（默认 → App Store）
- 文案模板：`Ready to <action>?` / `<Verb> <object> today.`
- **[Hard Rule]** 不允许 2 个 CTA、不允许 email 表单
- **[Hard Rule]** 所有 SEO 落点页面（`/blog/*` / `/glossary` / `/models` / `/features` / `/pricing`）**统一使用 `SecondaryCTA`**；不允许「样式想调一下」就新起一个 `MyCTA.tsx`

### 8.2 FaqSection

- H2：本页主题 + `Answered.` / `FAQ`
- 每条问题是 `<h3>`；问题与答案统一字号
- **必须** emit `FAQPage` JSON-LD（`emitJsonLd` 默认 true）
- **[Recommended]** 6–10 条 QA；少于 4 条别单独起 section

### 8.3 PageHero

- **[Hard Rule]** 每页 1 个 CTA（App Store 下载）
- H1 只放核心关键词（如 `TikTok Video Generator`），其余叙事放描述里
- 描述 2–3 行，`max-w-3xl`

**Breadcrumb 层级示例**：

| 路由 | 面包屑 | 层级 |
|---|---|---|
| `/tiktok-video-generator` | Home › TikTok Video Generator | 2 |
| `/tiktok-video-generator/mattress` | Home › TikTok Video Generator › Mattress | 3 |
| `/use-cases/affiliates` | Home › Use Cases › Affiliates | 3 |
| `/blog/how-to-make-money-on-tiktok` | Home › Blog › How to Make Money on TikTok | 3 |
| `/glossary` | Home › Glossary | 2 |

**[Hard Rule]** 面包屑 ≤ 3 级；超过说明 URL 层级设计过深，应重新拍平路由。

---

## 9. 新页面搭建 Checklist

**A. Blueprint 阶段**（写代码前）

1. **[Hard]** 先写 blueprint（§2.3），评审通过再动手
2. **[Hard]** 定位页面类型，找 1–2 个参考页面
3. **[Recommended]** 列出每个 section 的复用等级（✅/🔁/🧩/❌），❌ 的组件必须说明为什么其它页不需要

**B. 编码阶段**（写代码时）

4. **[Hard]** 复制最接近的 route + data 文件作为骨架：
   - 产品页 → `video-generator.ts`
   - use-case 页 → `personas.ts` 里最相近的一条
   - blog 文章 → 见 `docs/blog-article-spec.md`
5. **[Hard]** AudienceGrid 按 §4.3 挑 persona + 重写 `out`，禁止复制其它产品页文案
6. **[Hard]** VideoGallery / SkuShowcase 按 §5.1 埋关键词，图片 1200×630
7. **[Recommended]** ValueGrid 3 段、FeatureGrid 8–12 条、FAQ 6–10 条

**C. 发布前自检**（合并前必过）

8. **[Hard]** Hero 只留 1 个 CTA
9. **[Hard]** 面包屑 2–3 级
10. **[Hard]** 所有内链（`/use-cases/*` / `/glossary` / 姐妹产品页）真实存在，无 404
11. **[Hard]** 仅提 TikTok Shop US
12. **[Recommended]** SecondaryCTA 位于 Footer 上方，单 CTA

**最短通过路径**：Hard Rule #8 / #9 / #10 / #11 四条必须绿灯，否则不允许合并。其余为质量线，允许 1–2 条 Recommended 未满足但需在 PR 里注明理由。

---

## 10. 反例 / 常见错误

每条 ❌ 后面标出「怎么改」及相关规范章节：

- ❌ 直接复制别的 product 页 data 文件不改 audience / valueProps 文案 —— 违反镜像原则（§7）
  - ✅ 按当前产品的动词重写 `out`（详见 §4.3.1 Before/After 示例）
- ❌ Hero 放 2 个 CTA（例：App Store + Notify me）—— 违反单 CTA 约定（§8.3）
  - ✅ 只留 App Store CTA，次级动作放到页面下方的 SecondaryCTA（§8.1）
- ❌ 提及 TikTok Shop UK / ID / DE —— 我们只做 US（§9-C HR-18）
  - ✅ 全站文案锁定 "TikTok Shop US"，路由 slug 也不留其它市场
- ❌ SkuShowcase 图片非 1200×630 —— 高度飘破节奏（§5.1）
  - ✅ 生成图时锁 1216×640 或 1200×630，`aspect-[1200/630]` 由组件已经约束
- ❌ 内链到不存在的 `/use-cases/<slug>` —— 404 会伤 SEO（§9-C HR-17）
  - ✅ PR CI 前 grep 一遍所有 `href="/use-cases/*"`，对齐 `personas.ts` 的 slug
- ❌ 为图省事把 `/tiktok-video-generator` 的 `AudienceGrid` items 直接 `import` 到 `/tiktok-shop-products-finder` —— 破坏镜像原则（§7）
  - ✅ 每个产品页在自己的 data 文件里独立写 audience（可以复制粘贴后重写 `out`，但不能 import）
  - **为什么**：一旦 import，两个页面的文案就绑死；未来只想改一个页面就得抽 `Omit`/`Pick` 特殊 case，长期腐蚀契约
- ❌ 在正文里出现「Learn more →」按钮式链接 —— 应用自然语言锚文本（§4.3 第 4 条）
  - ✅ `Pass the winners straight to your <Link>video queue</Link>`
- ❌ SkuShowcase tab 数量 > 5 —— 移动端 tab 会换行 / 桌面端 tab bar 撑满、切换成本上升（§5.1.1）
  - ✅ 3–5 个品类为最佳；超过就拆到独立子路由（如 `/tiktok-video-generator/mattress`）
- ❌ 新 use-case 页 audience 卡片文案是「Moras 的 3 个能力」而不是「这个角色的 3 个场景」—— 主宾颠倒（§7 镜像原则）
  - ✅ 主语始终是当前页面的角色 / 场景，产品只是宾语之一

---

## 11. 参考文件

- **模板**：`src/components/site/product-page/ProductPageTemplate.tsx`
- **数据契约**：`src/content/product-pages/types.ts`
- **现有 data**：`src/content/product-pages/{products-finder,video-generator,video-analyzer}.ts`
- **Use-case 模板**：`src/components/site/use-cases/PersonaTemplate.tsx` + `personas.ts`
- **共享 block**：`src/components/site/{Navbar,Breadcrumbs,PageHero,FaqSection,SecondaryCTA,Footer}.tsx`
- **模式共享 block**：`src/components/site/product-page/{AudienceGrid,ValueGrid,FeatureGrid,SkuShowcase,VideoGallery,StepsRow,CompareGrid,ProblemSolution,MetricsStrip}.tsx`
- **Glossary**：`src/content/glossary.ts` + `src/routes/glossary.tsx`
- **Blog**：`src/lib/blog/articles.tsx` + `docs/blog-article-spec.md`

---

## 附录 A：ProductPageData 完整字段清单

一份查表用的字段索引，避免每次去 `types.ts` 里翻。字段顺序 = 页面渲染顺序。

| 字段 | 必填 | 触发的组件 | 说明 / 何时用 |
|---|---|---|---|
| `slug` | ✅ | — | 用于 canonical / JSON-LD id |
| `canonical` | ✅ | `<head>` | 绝对 URL |
| `breadcrumb` | ✅ | `Breadcrumbs` | 最末级显示名 |
| `meta.title` / `description` / `keywords` | ✅ | `<head>` | ≤ 60 / ≤ 160 字符 |
| `jsonLd` | ✅ | `<script type="application/ld+json">` | SoftwareApplication；`extra` 里塞 HowTo |
| `hero` | ✅ | `ProductHero` | H1 一行 + 描述 2–3 行 + 1 CTA + 可选 `metaItems` |
| `problem` | 可选 | `ProblemSolution` | 左右对照现状痛点 vs Moras 方案；工作流复杂的产品才用 |
| `steps` | 可选 | `StepsRow` | 3 步；`emitSchema: true` 会输出 HowTo JSON-LD |
| `previewSlot` | 可选 | `PreviewSlot` | 挂接 `finder-preview` / `analyzer-preview` / `flow-strip` 三个独立组件之一 |
| `valueProps` | 可选 | `ValueGrid` | 3 段图文交替，图片 1200×630 |
| `skuShowcase` | 可选 | `SkuShowcase` | 仅在产品自然按品类切分时用（§5.1.1）|
| `videoGallery` | 可选 | `VideoGallery` | 5–8 条真实 TikTok Shop 视频 |
| `features` | 可选 | `FeatureGrid` | 8–12 卡；短标题 + 一句 desc |
| `metrics` | 可选 | `MetricsStrip` | 3–4 个可量化数字 |
| `audience` | ✅ | `AudienceGrid` | 3 张 persona；`out` 必须按当前产品重写（§4.3.1）|
| `compare` | ✅ | `CompareGrid` | 首列是能力名，其余列 = 竞品 / 手工方法 |
| `faq` | ✅ | `FaqSection` | 6–10 条；`emitJsonLd` 默认 true |
| `finalCta` | ✅ | `SecondaryCTA` | 单 CTA → App Store |

**判定 checklist**：新页面填这份表时，凡是标「可选」的字段，能空就空。详见 §3.1 判定原则及其 Hard Rule。

---

## 附录 B：常用文案模板

### B.1 Hero H1 命名公式

**关键词优先**（3 个产品页 + tool 页统一）：直接放核心 SEO 关键词。

- `TikTok Video Generator`
- `TikTok Shop Products Finder`
- `TikTok Video Analyzer`

**场景优先**（use-case 页 / blog 页）：以角色 / 场景为主语。

- `For TikTok Shop Affiliates`
- `For Dropshippers Testing New SKUs`
- `How to Make Money on TikTok Shop`

**[Hard Rule]** H1 一行不换行；剩余叙事全部放 hero 描述（2–3 行，`max-w-3xl`）。

### B.2 SecondaryCTA 文案模板

| 页面类型 | H2 模板 | 描述模板 | CTA 文案 |
|---|---|---|---|
| 产品页 | `Ready to <verb> <object>?` | 一句重复产品价值 + 一句降低进入门槛 | `Download on App Store` |
| use-case 页 | `Run every <role task> like one team.` | 承诺给这个角色的具体产出 | `Download on App Store` |
| blog 文章 | `Ready to test what you just read?` | 把文章观点一句话收敛到产品动作 | `Download on App Store` |
| glossary | `Turn the vocabulary into results.` | 把术语落到工作流 | `Download on App Store` |

### B.3 FAQ 起手式

问题一律 `<h3>`，起手式收敛到 4 种：

- `Does Moras <do X>?` —— 澄清功能边界
- `How do I <achieve Y>?` —— 讲操作路径
- `Can I <edge case>?` —— 处理常见顾虑（合规 / 导出 / 多账号）
- `What's the difference between <A> and <B>?` —— 对比姐妹产品 / 竞品

答案 40–80 词，最后可留一句自然锚文本回链姐妹产品或 glossary。

---

## 附录 C：Hard Rule 完整索引

以下为文档中所有 Hard Rule 的完整汇总，便于一站式查阅。

| # | Hard Rule | 章节 |
|---|---|---|
| HR-1 | blueprint 评审通过后再写 `.tsx` | §2.3 |
| HR-2 | 不允许为了「填满模板」硬凑内容；可选字段能空就空 | §3.1 |
| HR-3 | AudienceGrid `out` 文案必须按当前产品叙事重写，不可复制其它产品页 | §4.3 |
| HR-4 | SkuShowcase 只允许在产品页出现，且当前产品必须自然能按品类切分 | §5.1.1 |
| HR-5 | Hero 每页只留 1 个 CTA（App Store 下载）| §8.3 |
| HR-6 | 面包屑 ≤ 3 级 | §8.3 |
| HR-7 | H1 一行不换行；剩余叙事全部放 hero 描述 | 附录 B.1 |
| HR-8 | SecondaryCTA 不允许 2 个 CTA、不允许 email 表单 | §8.1 |
| HR-9 | 所有 SEO 落点页面统一使用 `SecondaryCTA`；不允许新起 `MyCTA.tsx` | §8.1 |
| HR-10 | 先写 blueprint，评审通过再动手 | §9-A |
| HR-11 | 定位页面类型，找 1–2 个参考页面 | §9-A |
| HR-12 | 复制最接近的 route + data 文件作为编码骨架 | §9-B |
| HR-13 | AudienceGrid 按 §4.3 挑 persona + 重写 `out` | §9-B |
| HR-14 | VideoGallery / SkuShowcase 按 §5.1 埋关键词，图片 1200×630 | §9-B |
| HR-15 | 发布前：Hero 只留 1 个 CTA | §9-C |
| HR-16 | 发布前：面包屑 2–3 级 | §9-C |
| HR-17 | 发布前：所有内链真实存在，无 404 | §9-C |
| HR-18 | 发布前：仅提 TikTok Shop US | §9-C |

**注意**：§9 Checklist 中的 Hard Rule 与正文中的规则语义相同，分属不同阶段（规划/编码/发布前），此处均予列出以便对照。

---

## 文档维护

本文档是一个"活的规范"。以下情况**必须**更新本文档：

| 触发条件 | 需要更新的内容 |
|---|---|
| 新增页面类型 | §2.1 页面类型列表、对应 blueprint 示例 |
| 新增内容 block 组件 | §1 内容 block 列表、对应组件的独立章节 + 附录 A 字段清单 |
| 废弃某个内容 block | 标记为 deprecated，标注替代方案 |
| 复用等级发生变化（如 🧩 → ✅）| 修改全文中该组件的复用等级标记，更新 §11 参考文件路径 |
| 新增 / 修改 / 删除 Hard Rule | 更新对应章节 + 附录 C |
| 文案模板不够用 | 更新 附录 B |

**维护责任人**：每次对页面体系的改动，请由改动者同步更新本文档。如在修改时发现文档与代码不一致，应优先修正文档。
