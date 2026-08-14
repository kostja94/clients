# 页面搭建指南：以 Floatboat 产品页为例

面向内部同事与 agent，讲清楚我们如何用「共享 block + 每页定制的内容组件」的方式搭一个新的 Floatboat landing page，并保持整站的结构、SEO、内链与品牌一致性。

配套阅读：`docs/BRAND_GUIDELINES.md`（视觉/排版/间距的唯一真源）、`docs/blog-article-redesign.md`（博客文章迁移指南）。

---

## 1. 核心理念

一个 Floatboat landing page = **共享骨架 block** + **若干内容 block**。

- **共享骨架**（所有页面必须存在，顺序固定）
  `Header → Breadcrumbs → SiteHero/SiteSplitHero → …内容 blocks… → SiteFaq → SiteFinalCta → Footer`
- **内容 block**（可复用、结构固定、**文案按页定制**）
  当前武器库：`SplitSection`、`FeatureCarousel`、`UseCasesGrid`、`HowItWorksSteps`、`ComparisonTable`。

同一个内容 block 在不同产品页里：
- **组件结构完全一致**（栅格、动画、卡片视觉、字段契约）
- **文案完全不同**（针对当前产品挑最相关的场景）
- 描述里用 `inlineLinkClass` (`src/lib/link-styles.ts`) 做自然锚文本内链，把权重回流到 `/use-cases/for-*`、其他产品页、`/models/*` 等 hub

> **复用等级**（贯穿全文）
> - ✅ **共享组件**：直接 import 同一个 `.tsx`，只传 props。例：`Header`、`Footer`、`Breadcrumbs`、`SiteFaq`、`SiteFinalCta`、`UseCasesGrid`、`HowItWorksSteps`。
> - 🔁 **结构共享，文案定制**：调用同一个组件，仅传本页专属 props（title/description/items）。例：`SiteHero` / `SiteSplitHero` / `FeatureCarousel` 在每个产品路由的具体调用。
> - 🧩 **模式共享，组件独立**：视觉/契约一致但目前是多个独立组件，未来可继续收敛。例：`SplitSection` 变体、`WhyAgenticCalendar` / `CalendarToWork` 这类每页一次的深层机制块。
> - ❌ **本页专属**：不进复用池，命名带页面/产品前缀。例：`ComparisonTable`（coworker 专属）、`InteractiveDesktopDemo`、`ModelDemo`、`FloatcupDashboard`。

> **模板 + 单页独有组件**
> 同类产品页（`/coworker`、`/ai-file-organizer`、`/ai-scheduling-assistant`、`/floatim`、`/skills-marketplace`）共享同一份 section 模板；但当某页有其他页面不需要的独特叙事时（例：coworker 需要 "vs chat-only assistants" 对比表；skills-marketplace 需要 `SkillsRuntimeDemo`），可以在模板中插入本页专属组件。这类组件属于 ❌ 等级，不进复用池，也不需要在其他页面里补齐同名占位。

---

## 2. 设计新页面的工作流（先规划，再动手）

**不要**上来就复制某个产品页开始改文案 —— 那是 vibe coding，会遗漏本页真正需要的独特组件，也会把模板里用不上的 section 顺手留下。正确顺序：

### 2.1 三步规划

1. **定位页面类型**：产品页 / use-case 页 / hub 页 / 文章页 / 落地页。找出 1–2 个最接近的现有页面作为参考（大多数产品页应参考 `src/routes/coworker.tsx`）。
2. **列 section 清单**：写下叙事顺序（"用户滚到这里应该获得什么信息"），再把每条叙事映射到组件。
3. **对每个组件判定复用等级**（✅ / 🔁 / 🧩 / ❌），标注：
   - ✅ / 🔁：直接列共享组件名 + 需要传的 props
   - 🧩：列出镜像参考（如新 use-case 详情页参考现有 `UseCasePage`）
   - ❌：说明为什么其它页面不需要 → 证明它确实是本页专属

### 2.2 用 ASCII 线框图落地规划

在 `docs/blueprints/<page>.md` 里画 ASCII 骨架。例：新增 `/ai-meeting-notes`：

```text
AiMeetingNotesPage
├── Header                  ✅ 共享
├── Breadcrumbs             ✅ 共享     items: [{ label: "AI Meeting Notes" }]
├── SiteSplitHero           🔁 结构共享  H1: "AI Meeting Notes" + 1 CTA → /download + hero.jpg (1200×630)
├── FeatureCarousel         🔁 结构共享  4 张 "Why Choose Floatboat for Meeting Notes"（配 1200×800 图）
├── UseCasesGrid            ✅ 共享     4 列 audience: solopreneur (highlight) / creators / small-biz / studio
├── HowItWorksSteps         ✅ 共享     3 步 "How to Turn Meetings into Action with AI"
├── MeetingNotesLiveDemo    ❌ 本页专属  ← 唯一独有：会议转写→行动项的交互式演示
├── SiteFaq                 ✅ 共享     6 条，来自 src/lib/page-content.ts 的 MEETING_NOTES_FAQS
├── SiteFinalCta            ✅ 共享     单 CTA + 一行标题两行描述
└── Footer                  ✅ 共享
```

收益：
- **一眼看出哪些是新组件**（❌ 标记）→ 提前评估工作量
- **一眼看出复用来源** → 避免和现有页面文案重复
- **section 顺序是文档，不是代码** → 评审无需打开 IDE

### 2.3 规划文档模板

```markdown
# <PageName> Blueprint

## 页面定位
- 类型：产品页 / use-case 页 / hub 页 / …
- 参考页面：src/routes/<file>.tsx
- 目标关键词：<primary + 2–3 semantic variants>

## 叙事顺序
1. 用户滚到 X 时应该获得 Y 信息
2. …

## Section 骨架（ASCII）
```text
<在此画 ASCII tree>
```

## 新增组件清单
- ❌ `<Product><Feature>.tsx` — 用途 / 为什么其它页面不需要

## 复用组件清单
- ✅ / 🔁：<component> + 关键 props
```

**[Hard Rule]** blueprint 评审通过后再动手写 `.tsx`。省这一步 = 后期返工。

---

## 3. Case Study：`/coworker` 页面拆解

文件：`src/routes/coworker.tsx`。这是当前最完整、复用等级最丰富的产品页（含 ❌ 本页专属 `ComparisonTable`）。

| 顺序 | Section | 组件 | 复用等级 | 说明 |
|---|---|---|---|---|
| 1 | Header | `Header` | ✅ | 全站统一 |
| 2 | 面包屑 | `Breadcrumbs` | ✅ | 传 `items=[{ label: "AI Coworker" }]`，组件自动补 Home |
| 3 | Hero | `SiteSplitHero` | 🔁 | 图文分栏；H1 = "AI Coworker"，1 CTA → `/download`，image 1200×630 |
| 4 | 功能轮播 | `FeatureCarousel` | 🔁 | 4 张 "Why Choose Floatboat as Your AI Coworker"，每张配 1200×800 MediaImage |
| 5 | Use Cases | `UseCasesGrid` | ✅ | 4 列 audience，solopreneur 高亮，见 §4 |
| 6 | How It Works | `HowItWorksSteps` | ✅ | 3 步 "How to Hire an AI Coworker on Your Desktop" |
| 7 | 对比表 | `ComparisonTable` | ❌ | coworker 专属；vs cloud chat / browser agent / sandbox VM |
| 8 | FAQ | `SiteFaq` | ✅ | items 来自 `COWORKER_FAQS`（`src/lib/page-content.ts`），恰好 6 条 |
| 9 | 最终 CTA | `SiteFinalCta` | ✅ | 一行标题 "Hire Your First AI Coworker" + 两行描述 + 1 CTA |
| 10 | Footer | `Footer` | ✅ | 全站统一 |

`/ai-file-organizer`、`/ai-scheduling-assistant`、`/floatim`、`/skills-marketplace` 遵循同一 section 顺序，只是把 ❌ 段替换成各自独有块（或不加）。

---

## 4. 重点示范：UseCasesGrid 模式（跨模板复用）

这是本次要重点讲清楚的**唯一已收敛完毕**的内容 block —— 已经跨过"每产品一份 `*UseCases.tsx`"的阶段，全部产品页复用同一份 `src/components/site/UseCasesGrid.tsx`。

### 4.1 组件契约

```ts
interface UseCaseItem {
  title: string;          // 结果导向短句，≤ 40 char
  body: ReactNode;        // 1–2 句，20–35 词；允许内嵌 <Link> 做上下文内链
  to?: string;            // 站内绝对路径（通常指向 /use-cases/for-*）
  highlight?: boolean;    // 主受众（solopreneur）高亮
}

<UseCasesGrid
  title="..."
  subtitle="..."
  columns={3 | 4}
  items={UseCaseItem[]}
/>
```

- 栅格：`grid-cols-1 sm:grid-cols-2 lg:grid-cols-{columns}`
- 视觉：`tw-frame` 卡片 + 硬边 2px + 偏移阴影（editorial-utility 语言）
- **无 eyebrow 字段**（mem Core 已全站禁用 filler label）
- 主受众卡片视觉：`highlight: true` → `bg-brand/10`

### 4.2 现有五个实例对比

| 页面路由 | columns | 4/6 张卡片挑选的场景 | 内链回 |
|---|---|---|---|
| `/coworker` | 4 | Solopreneurs（highlight）/ Creators / Small business / Studios | `/use-cases/for-*` 四页 |
| `/ai-file-organizer` | 4 | 同上，文案聚焦"文件混乱"场景 | 同上 |
| `/ai-scheduling-assistant` | 4 | 同上，文案聚焦"排程/自动化"场景 | 同上 |
| `/floatim` | 4 | 同上，文案聚焦"agent 群聊"场景 | 同上 |
| `/skills-marketplace` | 4 | 同上，文案聚焦"skills 复用"场景 | 同上 |

**关键观察**：结构和视觉是同一个组件，但**没有一张卡片文案是重复的** —— 每个产品挑了对它自己最有说服力的场景切入，并把描述里的锚文本链回 `/use-cases/for-*` 对应受众页。

### 4.3 文案编写规则

1. **打开 `src/routes/use-cases.tsx`**，浏览当前 4 个受众 slug（`for-solopreneur` / `for-creators` / `for-small-business` / `for-studio`）
2. **每个 slug 都写一张卡片**（4 张覆盖完整）；如果本页 columns=3，则合并其中两类
3. **description 用自然锚文本 `<Link>` + `inlineLinkClass`**，不写 "Learn more →"
4. **[Convention]** title 是**结果导向**的短句（≤ 40 char），如 "Ship the quarterly report, not chase CSVs"
5. **[Recommended]** body 保持 20–35 词、1–2 句，太长破坏卡片视觉一致性
6. **[Hard Rule]** solopreneur 卡片始终 `highlight: true`（主 SEO 受众）

### 4.4 何时使用

- **UseCasesGrid**：任何需要"多受众覆盖"叙事的产品页（当前全部 5 个产品页都用了）
- **改用 FeatureCarousel**：当叙事是"产品能力矩阵 / 差异化机制"（4–8 张卡片，每张配图）
- **改用 HowItWorksSteps**：当叙事是"3 步上手"（严格 3 步，动词开头）

---

## 5. FeatureCarousel 的 SEO 定位

`FeatureCarousel`（`src/components/site/FeatureCarousel.tsx`）是页面里**唯一一个鼓励堆内容**的 block。原因：

- **形态是横向轮播**，视觉高度固定，加更多卡片不会撑高页面
- **每张卡片都是独立 DOM**，SEO 抓取时计入完整正文 → 等价于把 4–8 段产品叙事塞进一屏视觉里
- 用户只看前 1–2 张，爬虫看全部 —— "人看视觉、机器看内容"的最佳平衡

### 5.1 写作规则

1. **每张卡片配一段 40–90 词的 body**，别只写 1 句。展开机制、场景、结果指标
2. **在文案里自然埋关键词**：产品名（AI Coworker / AI Scheduling Assistant / FloatIM / AI File Organizer）、机制词（Selfware、IACT、Combo Skills、Tacit Engine）、平台词（macOS / Windows 10/11 / Apple Silicon）
3. **title 的一半词用 `tw-gradient-text` 高亮**（现为纯色 amber，非渐变；见 mem Core），另一半保留正文色 —— 形成视觉节奏
4. **每张 body 埋 1–2 个 `inlineLinkClass` 内链**，指向 `/use-cases/for-*` 或姐妹产品页
5. **[Recommended]** 卡片数：**4–8 张为最佳**。少于 4 不值得做轮播，多于 8 爬虫权重被稀释
6. **配图**：每张 `MediaImage` 用 1200×800 写实摄影 jpg，`badge` 是短机制标签（如 `Local-first · 0 uploads`、`Auto Mode · 4+ models`）

### 5.2 为什么其它 block 不能这样堆

- Hero / SiteFaq / SiteFinalCta / UseCasesGrid / SplitSection 都是**纵向 stack**，堆内容 = 页面变长 = 跳出率上升
- FeatureCarousel 是唯一"内容量与视觉高度解耦"的组件 —— 因此是产品页承载长尾 SEO 的主力

---

## 6. 交叉引流：产品间互推的当前状态

Floatboat 目前**没有** `*OtherFeatures` / `*OtherTools` 等价的共享组件。产品间引流依赖：

- **Footer 四大列**（Product / Solutions / Models / Resources）—— 每个产品/受众/模型页都出现在这里
- **正文 inline prose 链接** —— 在 FeatureCarousel body / SplitSection 段落里用 `inlineLinkClass` 自然锚文本引流
- **`/use-cases/for-*` 详情页底部的 cross-audience mono strip**（一行内链，非卡片，见 mem Core §Use Cases）

**下一步演进**：抽出 `<ProductSpotlight context="..." />`，见 §11。当前阶段不做，避免过早抽象。

---

## 7. 双向内链：产品页 ↔ `/use-cases/for-*` 镜像

Floatboat 组件复用的**核心理念**：同一套「卡片契约 + 视觉模板」两个方向使用，主语和宾语互换。

| 方向 | 所在页面 | 组件 | 主语（固定） | 宾语（挑选 + 改写） |
|---|---|---|---|---|
| 产品页 → 受众 | `/coworker` | `UseCasesGrid` | AI Coworker | 4 个受众场景 |
| 受众页 → 产品 | `/use-cases/for-solopreneur` | 目前是正文 `WhatYouRun`（3 行 combo）+ mono strip | Solopreneur 场景 | 从产品池挑 N 个产品 |

### 7.1 每一类受众页应有自己的 Products 组件

当前 `/use-cases/for-*` 详情页由 `<UseCasePage copy={...} />` 渲染，尚未有独立的 "Products for this scenario" 卡片组件。**建议演进**：

- 复用 `UseCasesGrid` 的契约（`items[]: { title, body, to }`），新增一个 `<ProductsForScenario />` 薄壳
- 每个受众页在 `UseCaseCopy` 里配置 4 张产品卡片（Coworker / File Organizer / Scheduling Assistant / FloatIM），description 按受众场景改写
- 例：`/use-cases/for-solopreneur` 的 AI Coworker 卡片描述 = "One coworker per client project — reconciles CSVs and drafts the invoice email"

**关键点**：同一个产品在不同受众页里 `title/href` 完全一样，但 `body` **必须按当前场景改写**。这正好和产品页 `UseCasesGrid` "同一场景在不同产品页改写"是镜像的。

### 7.2 收敛方向

`UseCasesGrid` 已经是通用组件；下一步让 use-case 详情页复用同一 items 契约，只是数据源换成 `UseCaseCopy.productsForScenario`。

### 7.3 类比拓展

镜像原则不止于「产品 ↔ 受众」，站内所有 hub ↔ 详情关系都适用：

| Hub 页 | 详情页 | 镜像组件对 |
|---|---|---|
| `/use-cases` | `/use-cases/for-<audience>` | UseCasesGrid 卡片 ↔ ProductsForScenario 卡片（TODO） |
| `/models` | `/models/$slug` | ModelLineup 卡片 ↔ NotJustChat / WhyFloatboat 卡片 |
| `/combo-store` | `/combo-store/$author/$slug` | ComboCard ↔ RelatedCombos（TODO） |
| `/blog` | `/blog/$slug` | 文章卡片 ↔ 文章正文内链 |

每一对都遵循「主语固定、宾语挑选并按上下文改写描述」的同一套写作规范。

---

## 8. 新页面 checklist + 页面健康指标

### 8.1 校对项（对齐 mem Core Hard Rules & `docs/BRAND_GUIDELINES.md`）

- **[Hard Rule]** Hero 只留 1 个 CTA（无副按钮、无 footnote 里的第二链接）
- **[Hard Rule]** 页面里 `tw-gradient-text` 仅出现在 FeatureCarousel title 的高亮短语（每页 ≤ 4 处），H1 不用
- **[Hard Rule]** `<Breadcrumbs>` 必带（组件自动补 Home，只传尾部 items）
- **[Hard Rule]** `SiteFaq` items 恰好 **6 条**，来自 `src/lib/page-content.ts` 命名导出
- **[Hard Rule]** `SiteFinalCta` = 一行短标题 + 两行描述 + 1 CTA
- **[Hard Rule]** 所有 H2 使用 `text-2xl sm:text-3xl md:text-4xl`（Site* 组件已内置，route 不覆盖）
- **[Hard Rule]** 内链 `/use-cases/for-*` / `/models/*` / `/combo-store/*` 必真实存在
- **[Hard Rule]** 全站禁用 eyebrow filler label（如 `More than an organizer`、`Live demo · click around`）
- **[Hard Rule]** 全站禁用 sign in / sign up / register（Floatboat 是桌面 app，CTA 永远是 Download）
- **[Hard Rule]** 不引用任何外部产品名（对比表用通用能力描述，如 "Cloud chat assistant"）
- **[Hard Rule]** `head()` 必须设 title/description/og:title/og:description；产品页 leaf 设 og:image（1200×630 绝对 URL）
- **[Recommended]** H2 尽量包含核心关键词（如 "How to Organize Local Files with AI"）
- **[Recommended]** H1 直接是关键词本身（`AI Coworker` / `AI File Organizer`），不加装饰词

### 8.2 页面健康指标

| 指标 | 健康线 | 说明 |
|---|---|---|
| 索引速度 | < 7 天 | 发布后被搜索引擎收录的耗时 |
| 跳出率 | < 55% | 只看一页就离开的比例 |
| CTA 点击率 | > 3% | Download 按钮点击 / 页面 UV |
| 内链 404 数 | 0 | CI 检查，不允许断链 |
| 转化率 | > 1% | 完成下载/激活等目标行为的比例 |

超出健康线时优先排查内容质量和内链，不是先动视觉。

---

## 9. 反例 / 常见错误

- ❌ 把 `/coworker` 的 `UseCasesGrid` items 原样 import 到 `/skills-marketplace` —— 违反镜像原则，body 必须按当前产品改写
- ❌ Hero 用 `SiteHero` + 自定义 layout 而不用 `SiteSplitHero` variant —— 破坏全站视觉一致
- ❌ Hero 放 2 个 CTA + footnote 里再塞 "Free · No signup · macOS/Windows" —— 违反单 CTA 约定
- ❌ H1 用 `tw-gradient-text` —— 每页高亮预算已经花在 FeatureCarousel title
- ❌ 在 route 文件里内联 `<Accordion>` 或 hardcode FAQ 数组 —— FAQ 必须走 `SiteFaq` + `page-content.ts`
- ❌ 加 `eyebrow="More than an organizer"` / `Schedule & Automation` 之类填充标签
- ❌ 把 `model_pages` 表的字段硬编码进 `models.$slug.tsx` —— 破坏 DB-driven 契约
- ❌ 对比表点名外部产品（Claude / ChatGPT / Notion 等）—— 用 "Cloud chat assistant" / "Browser-only agent" 通用描述
- ❌ 加 `<SiteNewsletter />` 到 route —— Newsletter 只在 Footer，重复 = 两次 ask
- ❌ 手写 `inline-flex … rounded-full …` 的 CTA —— 必须用 `<CtaButton />`

---

## 10. 内容与组件分离：把文案下沉到 Lovable Cloud

组件里 hardcode 文案是当前的过渡状态。**长期方向**：把每个组件对应的字段（title / description / items / links / images）存进 Lovable Cloud (Supabase JSONB)，组件只负责渲染。

| 维度 | 归属 | 改动影响 |
|---|---|---|
| **设计**（视觉、栅格、动画、颜色） | `.tsx` 组件 + Tailwind token | 改一次，所有引用同步 |
| **技术**（数据契约、路由、SEO 结构） | TypeScript interface + Supabase 表结构 | schema 变更走 migration |
| **内容**（每页文案、内链锚文本） | Supabase JSONB 行 | 不动代码，内容团队直接编辑 |

### 10.1 当前唯一 DB-driven 案例

- `model_pages` 表 → `src/routes/models.$slug.tsx` 渲染，via `src/lib/model-pages.ts`
- 新增一个 model = insert 一行 JSONB（`hero` / `lineup` / `why` / `how` / `faqs` / `seo` 等字段），不改代码

### 10.2 下一批候选下沉

优先把「🧩 模式共享 + 文案定制」类下沉：

- `SiteFaq` 数组 → `page_faqs` 表（当前在 `src/lib/page-content.ts`，天然可迁移；键 = 路由 slug）
- `FeatureCarousel` 4–8 张卡片 → `page_carousels` 表
- `UseCasesGrid` 4 张卡片 → `page_use_cases` 表（或 `product_use_cases` 挂产品 JSONB）
- `SiteFinalCta` 每页 1 条 → 合并进 `pages` 主表

### 10.3 渐进式迁移四步

1. **契约先行**：新页面走 blueprint 时先写 TypeScript interface，即使先用常量数组喂数据
2. **两处触发**：当同一份 interface 出现在 ≥ 2 个页面 → 建表 + migration，两处数据同时迁进去
3. **老页面按流量优先级替换**：`/coworker` / `/floatim` 这类高流量页先切
4. **抽通用渲染器**：让 `UseCasesGrid` / `FeatureCarousel` / `SiteFaq` 都读同一张 pattern 表，`where` 条件不同

### 10.4 反例

- ❌ 组件既读 DB 又保留 hardcode fallback —— 两份真相
- ❌ 字段展开成一堆平铺 column —— JSONB 更适合"每页字段略有不同"
- ❌ schema 迁移和渲染代码不在同一个 PR —— 上线必出对不上

---

## 11. 跨团队复用：主产品是所有 SEO 页面的公共依赖

未来当团队里有多人分别负责不同类型的 SEO 页面（use-cases / models / combo-store / blog / floatcup / creator-program），**每类页面都需要"引导用户到主产品"的落点**。如果每类各写一遍产品卡片，会出现：

- 同一个产品有 N 份视觉不同的介绍卡片
- 主产品改 tagline 要改 N 个文件
- 命名漂移（`AI Coworker` vs `Coworker` vs `Floatboat Coworker`）

**解法**：主产品对应的 section 只做**一个组件 + 一份数据源**，所有 SEO 页面按需 import + 传当前上下文 props。

### 11.1 谁复用什么

| SEO 页面 | 需要的主产品 section | 复用组件 |
|---|---|---|
| `/use-cases/for-*` | Products for this scenario | `<ProductSpotlight context="use-case" scenario="solopreneur" />` |
| `/blog/$slug` | Related products footer | `<ProductSpotlight context="article" />` |
| `/combo-store/$author/$slug` | Products that use this skill | `<ProductSpotlight context="combo" />` |
| `/models/$slug` | Products that use this model | `<ProductSpotlight context="model" />` |
| `/floatcup-2026` | Get the desktop client | `<ProductSpotlight context="landing" />` |

### 11.2 目标结构

```text
src/components/site/product-spotlight/
├── ProductSpotlight.tsx       ← 唯一渲染组件（栅格 / 动画 / 卡片视觉）
├── useProductSpotlight.ts     ← 按 context + scenario 从 DB 取卡片
└── types.ts                   ← ProductCard 契约

Lovable Cloud:
product_cards          ← 主产品清单（id / name / href / image / base_tagline）
product_context_copy   ← (product_id, context, scenario) → 改写后 description
```

调用方（任意 SEO 页面）：

```tsx
<ProductSpotlight context="use-case" scenario="solopreneur" limit={4} />
```

主产品团队改 tagline / 新增产品 → 在 `product_cards` insert 一行 → **所有 SEO 页面下一次渲染立即同步**。

### 11.3 落地建议（渐进式）

1. **先统一契约**：把 `UseCasesGrid` items 契约扩展成 `ProductCard`（增 `image?`, `badge?`）
2. **抽出 `<ProductSpotlight items=[] />`**：先接受 items 直接渲染
3. **建两张 Lovable Cloud 表**：把当前 hardcode 数据迁进去，`context` 字段按现有页面填
4. **删薄壳**：SEO 页面直接调 `<ProductSpotlight context=... />`
5. **owner 落到 Platform 团队**：组件视觉变更走 Platform PR review

### 11.4 反例

- ❌ SEO 页面团队为了"这次样式想调一下"复制 `<ProductSpotlight>` 改名 `<MyProductSpotlight>` —— 破坏跨团队复用
- ❌ 主产品 tagline hardcode 在 SEO 页面而不是从 `product_cards.base_tagline` 读 —— 主产品改名时漏
- ❌ 每个 SEO 团队各自维护"当前有哪些主产品"的枚举 —— 主产品清单必须只有 Platform 一份

---

## 12. 参考文件

- **Site\* primitives**：`src/components/site/{Header,Footer,Breadcrumbs,SiteHero,SiteSplitHero,SiteFaq,SiteFinalCta,FeatureCarousel,UseCasesGrid,HowItWorksSteps,SplitSection,CtaButton}.tsx`
- **产品页参考实现**：`src/routes/{coworker,ai-file-organizer,ai-scheduling-assistant,floatim,skills-marketplace}.tsx`
- **Use-case 壳 + 4 个受众页**：`src/components/site/use-cases/UseCasePage.tsx` + `src/routes/use-cases.for-*.tsx`
- **Model DB-driven 页**：`src/routes/models.$slug.tsx` + `src/lib/model-pages.ts`
- **内容源**：`src/lib/page-content.ts`（FAQ 数组）+ `src/lib/faq-render.tsx`（渲染器）
- **Inline 链接样式**：`src/lib/link-styles.ts`（`inlineLinkClass`）
- **品牌/视觉规则单一来源**：`docs/BRAND_GUIDELINES.md`
- **博客文章迁移指南**：`docs/blog-article-redesign.md`

---

## 13. 未来演进方向

当团队规模扩展到 5+ engineers + 独立内容团队时，这套体系需要从文档升维到工具化：

- **Page Generator**：输入 page type / slug / keywords，自动生成 blueprint + 组件骨架
- **CMS Editor**：让内容团队在不碰代码的前提下编辑 `page_faqs` / `page_carousels` / `page_use_cases`
- **Internal Link Validator**：CI 中自动检查 `/use-cases/for-*` / `/models/*` / `/combo-store/*` 断链、孤页、弱锚文本
- **`<ProductSpotlight />` 抽象**：见 §11，先落契约再落 DB

当前阶段以本文档为 single source of truth 即可，上述工具在内容规模进入下一个数量级时启动。
