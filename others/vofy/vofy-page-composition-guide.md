# 页面搭建指南：以 Vofy `/apps/color-splash` 为例

面向内部同事（工程 / 内容 / 设计）与 AI agent，讲清楚我们如何用「共享骨架 + 每页定制的内容组件」的方式，快速搭一个新的 Vofy landing / app / use-case / models / blog 页面，并保持整站结构、SEO 与内链一致。

---

## 速查卡

> 如果你只读 30 秒，看这里。

| 概念 | 一句话 |
|---|---|
| ✅ 共享组件 | 直接 import 同一个 `.tsx`，只传 props（`TopNav`、`SiteFooter`、`PageBreadcrumb`、`PageFAQ`、`SecondaryCTA`、`PageHero`、`HowToSteps`、`SplitSection`、`SectionHeader`）|
| 🔁 结构共享，文案定制 | 同一组件的不同实例，只换 props（`HomeFAQ` / `EcommerceFAQ` 都调 `PageFAQ`；`HowTo` / 各 use-case 步骤都调 `HowToSteps`；`UseCases` / `SplitSection` 多次调用）|
| 🧩 模式共享，组件独立 | 视觉/契约相近但目前是独立组件（apps 页的 `AppHero` vs 内容页的 `PageHero`；`HeroShowcase` vs `CompareSlider`）|
| ❌ 本页专属 | 命名带页面前缀或写在同文件内，不进复用池（`ShowcaseGallery` / `ThreePresets` / `WhenToUse` / `MoreTools` 在 `color-splash.tsx`；`NodeGraphHero` 在首页）|
| 页面骨架 | `TopNav → PageBreadcrumb → PageHero(或 AppHero) → …内容 blocks… → PageFAQ → SecondaryCTA → SiteFooter` |
| 每页必配 | `head()` 里真实 `title` / `description` / `og:*` / `twitter:card` / `canonical` + FAQ / Breadcrumb JSON-LD（有分步流程再加 HowTo）|

### 我该从哪开始？

| 你是 | 先读 |
|---|---|
| 第一次看 | §1 核心理念 → §2 工作流 → §3 参考页面 |
| 要搭新 app（effect / builder） | §2 工作流 → §4 App 页模板 → §8 Checklist |
| 要搭 use-case / 内容页 | §2 工作流 → §5 内容页模板 → §8 Checklist |
| 要写文案 | §6 文案规则 → §8 Checklist |
| 要判定复用等级 | §1 复用等级 → §7 组件目录 |

---

## 1. 核心理念

一个 Vofy 页面 = **共享骨架 block** + **若干内容 block**。

- **共享骨架**（顺序固定，所有页面都必须有）
  `TopNav → PageBreadcrumb → PageHero(或 AppHero) → …内容 blocks… → PageFAQ → SecondaryCTA → SiteFooter`
- **内容 block**（可复用、结构固定、**文案按页定制**）
  当前武器库：`SplitSection`、`HowToSteps`、`PageFAQ`、`PromptBox`、`HeroShowcase`（apps）、`CompareSlider`、`CreatorTestimonials`（apps）、`AppsSection` / `ModelsSection` / `Community`（首页专用 hub 卡片）。

同一个 block 在不同页面里：

- **组件结构完全一致**（栅格、字段契约、间距）
- **文案完全不同**（针对当前品类挑最相关的叙事）
- 描述里用自然锚文本 `<Link>` 内链，把权重回流到 `/`、`/models`、`/use-cases`、相邻 app 页

### 复用等级

| 等级 | 含义 | Vofy 现有例子 |
|---|---|---|
| ✅ 共享 | 一份代码，多页 import，只传 props | `TopNav`、`SiteFooter`、`PageBreadcrumb`、`PageFAQ`、`SecondaryCTA`、`PageHero`、`HowToSteps`、`SplitSection`、`SectionHeader` |
| 🔁 结构共享，文案定制 | 同一组件的不同实例 | `HomeFAQ` / `use-cases/ecommerce` FAQ 都调 `PageFAQ`；`HowTo` / `ecommerce` 步骤都调 `HowToSteps`；`UseCases` / `SplitSection` 每 section 一次 |
| 🧩 模式共享，组件独立 | 契约相近但目前是独立组件 | `AppHero`（apps 交互式 hero）vs `PageHeroCentered`（内容页）；`HeroShowcase`（apps 画廊）vs `CompareSlider`（before/after） |
| ❌ 本页专属 | 不进复用池，命名带页面前缀或写在同文件内 | `ShowcaseGallery` / `ThreePresets` / `WhenToUse` / `MoreTools`（`color-splash.tsx`）；`NodeGraphHero`（首页）；`ecommerce` 的 pipeline 图 |

> **模板 + 单页独有组件**
> 同类 app 子页（`/apps/color-splash`、`/apps/ghibli`、`/apps/image-extender`）共享同一份 section 模板。当某页有独特叙事时（例：color-splash 需要 `ThreePresets` 讲三个经典配色 recipes），插入 ❌ 等级的本页专属组件即可 —— 命名不含跨页含义，也不需要在其他 app 页补齐同名占位。

---

## 2. 设计新页面的工作流（先规划，再动手）

**不要**直接 copy 某个 route 就开始改文案 —— 会遗漏本页独特组件，也会留下模板里用不上的 section。

### 2.1 三步规划

1. **定位页面类型**：landing / app（effect / builder）/ use-case / models hub / blog 中的哪一类？找 1–2 个最接近的现有页面做参考（见 §3）。
2. **写 Blueprint**：一页 markdown 列清楚
   - `route path`（TanStack Start 文件命名，见下）+ `canonical` URL
   - `<title>`（≤ 60 字符，含主关键词）+ `meta description`（≤ 160 字符）
   - H1（Title Case，≤ 6 词 / ~40 字符，不加 "The / A / Vofy" 前缀）+ 每个 section 的 H2（sentence case）
   - 复用的 block（标注等级 ✅🔁🧩）与本页独有的 ❌ 组件
   - 内链目标（哪些锚文本指向哪些站内 route）
   - JSON-LD：FAQ + Breadcrumb 必配；有分步流程加 `HowTo`
3. **确认后再编码**。

### 2.2 编码顺序

1. 建 `src/routes/<path>.tsx`（TanStack Start 文件路由）：
   - 页面级 route：`src/routes/pricing.tsx` → `/pricing`
   - 子层级独立布局：**用下划线拆层**，例如 `src/routes/use-cases_.ecommerce.tsx` → `/use-cases/ecommerce`（与 hub 页解耦）
   - 动态段：`src/routes/apps.$slug.tsx` + 在 `src/data/apps-pages.ts` 注册 slug（当前 apps 走这条路径）
   - **禁止** 建 `src/pages/`、`src/routes/_app/`、`src/routes/pages/` —— 会与 `index.tsx` 冲突
2. 先把骨架 + `head()` + JSON-LD 打通，跑 `bun run build` 保证类型和路由树无红。
3. 从上到下填 sections：`PageBreadcrumb → Hero → 内容 blocks → PageFAQ → SecondaryCTA`。
4. 新增的 ❌ 组件放在同文件内直到需要跨页复用时再抽到 `src/components/vofy/` 或 `src/components/apps/`。
5. 图片走 `src/assets/*.jpg`（1280×720 或 1200×630 横向为默认社交/展示比例），import 时写完整 `alt`。

---

## 3. 参考页面速览

| 路由 | 类型 | 参考价值 |
|---|---|---|
| `/` | Landing | `NodeGraphHero` + `AppsSection` + `ModelsSection` + `UseCases` + `HowTo` + `Community` + `HomeFAQ` + `SecondaryCTA` |
| `/apps/color-splash` | Effect app 页 | **新增 app 页的标准范本**（本文主范例，见 §4） |
| `/apps/ghibli`、`/apps/image-extender` | Effect app 页 | 与 color-splash 同模板，文案换品类 |
| `/use-cases/ecommerce` | Use-case 子页 | `PageHeroCentered` + `PromptBox` + `SplitSection`×4（左右交替）+ `HowToSteps` + `PageFAQ` + `SecondaryCTA`（见 §5） |
| `/models` / `/models/rankings` | Models hub + 子页 | Hub → 子页的层级拆分方式 |
| `/blog/[slug]` | 长文 | 正文版式与 JSON-LD |

---

## 4. App 页模板（以 `/apps/color-splash` 为准）

以此作为**新增 effect / builder app 页**的标准起点。文件实际实现在 `src/components/apps/pages/color-splash.tsx`，通过 `src/data/apps-pages.ts` 注册到 `/apps/$slug` 动态路由。

```text
AppsTheme                                   ✅ 共享（apps 品牌 token 包裹层）
 └─ TopNav                                  ✅ 共享
 └─ PageBreadcrumb                          ✅ 共享  Effects › Color Splash
 └─ AppHero                                 🧩 apps 专用 hero（H1 + description + controls + samples）
 └─ ShowcaseGallery (H2)                    ❌ 本页专属，内部用 HeroShowcase 🧩
 └─ WhatIs (H2)                             🔁 结构共享（居中 H2 + 一段 lead）
 └─ ThreePresets (H2)                       ❌ 本页专属（三个 recipes 卡片 + field notes）
 └─ WhenToUse (H2)                          ❌ 本页专属（4 个左侧描边小卡）
 └─ HowToSplash (H2)                        🔁 结构与 HowToSteps 一致；配 HowTo JSON-LD
 └─ Testimonials (H2)                       🔁 用 CreatorTestimonials（apps 通用）
 └─ MoreTools (H3)                          ❌ 本页专属（3 个相邻 app 跳转卡片）
 └─ PageFAQ (H2 "Questions")                ✅ 共享，配 FAQPage JSON-LD
 └─ SecondaryCTA                            ✅ 共享（title / description / primaryLabel / primaryTo）
 └─ SiteFooter                              ✅ 共享
```

**每个 H2 关键词友好且 sentence case**（"What is color splash?"、"Classic recipes"、"How it works"、"Where to use it"），H1 保持 Title Case + ≤ 6 词（"AI Color Splash"）。

### 4.1 注册新 app（走动态路由）

1. 在 `src/components/apps/pages/<slug>.tsx` 写页面 + 导出 `default` 组件与 `head` 函数。
2. 在 `src/data/apps-pages.ts` 里 `import` 并加入 `appPages` map：
   ```ts
   "<slug>": { Page: <Slug>Page, head: <slug>Head },
   ```
3. `/apps/<slug>` 立即可用；`apps.$slug.tsx` 的 `head()` 会自动读你的 `head`。

---

## 5. Use-case / 内容页模板（以 `/use-cases/ecommerce` 为准）

以此作为**新增 use-case 子页 / 长内容页**的标准起点。文件：`src/routes/use-cases_.ecommerce.tsx`（下划线拆层写法）。

```text
TopNav                                      ✅ 共享
PageBreadcrumb                              ✅ 共享  Use Cases › E-commerce
PageHeroCentered                            ✅ 共享（H1 Title Case + lead）
PromptBox                                   🧩 交互演示（可选，主要给电商 / 转化页）
SplitSection "Why …"        mediaSide=right ✅ 共享，图右
SplitSection "The pipeline" mediaSide=left  ✅ 共享，图左（左右交替）
SplitSection "Why choose Vofy" mediaSide=right
SplitSection "Built for teams" mediaSide=left
HowToSteps (H2)                             ✅ 共享（3 步卡片）
PageFAQ (H2)                                ✅ 共享，配 FAQPage JSON-LD
SecondaryCTA                                ✅ 共享
SiteFooter                                  ✅ 共享
```

**关键写法**

- `SplitSection` 的 `mediaSide` 左右交替，避免整页 media 都堆在同一侧。
- 每个 `SplitSection` 的 `link` 是内链回相邻 hub / app 页的好机会（`{ to: "/use-cases", label: "See all use cases" }`）。
- 图片写 `src/assets/use-cases/<slug>-<section>.jpg`，`alt` 写全场景描述。

---

## 6. 文案规则

> 与项目 memory 里 core rule / typography-case / brand.md 保持一致，这里做简化落地版。

- **H1**：Title Case，≤ 6 词 / ~40 字符；**不加** "The / A / Vofy" 前缀；描述性修饰移到 lead 里。例：H1 写 `AI Color Splash`，"AI 选择性配色效果，无需 Photoshop" 移到 lead。
- **H2 / H3 / H4**：sentence case。问题式 heading 用正常措辞（"What is color splash?"），不写 `FAQ: xxx`。
- **禁用**：eyebrow / kicker（H 标签上方的小字标签）；装饰性 lucide 图标（只保留导航 chevron、carousel arrow、表单控件、社交、UI primitive 图标）；标题（H1–H4 + `title=` prop）用 italic —— italic 仅限 body（blockquote、drop-cap、`<p>` 里的 `<em>`）。
- **字体**：只用 Geist（`font-display-xl`，H1/H2 专用）+ Inter（`font-display` H3+ / body / UI）。`font-serif` 是 Inter 的 legacy alias，绝对不要改指真 serif。不加第三家族。
- **类名常量**：H1/H2/H3/lead 直接用 `src/components/vofy/PageHero.tsx` 导出的 `H1_CLS` / `H2_CLS` / `H3_CLS` / `LEAD_CLS`，不再手抄一遍长串 class。
- **CTA**：纯文字 + " →"（例 `Open color splash →`），不写 "Click here"。
- **卡片描述**：1–2 句写清楚 **对谁 / 做什么 / 输出什么**，避免 "AI-powered 一切" 空话。
- **图片**：`src/assets/*.jpg`，1280×720 或 1200×630 横向；写 `alt`；避免生成式插画代替真截图。

---

## 7. 组件目录

**✅ 共享（`src/components/vofy/`）**
- `TopNav.tsx` — 全站顶部导航
- `SiteFooter.tsx` — 全站页脚（无 newsletter；如需 CTA 用 `SecondaryCTA`）
- `PageBreadcrumb.tsx` — 面包屑（`items={[{ label, to? }]}`）
- `PageHero.tsx` — 导出 `PageHeroCentered` / `PageHeroSplit` + `H1_CLS`/`H2_CLS`/`H3_CLS`/`LEAD_CLS` 常量
- `PageFAQ.tsx` — FAQ 折叠列表（`title` + `items=[{q,a}]`）
- `SecondaryCTA.tsx` — 深色底闭幕 CTA（`title` + `description` + `primaryLabel` + `primaryTo`），**只有这三段**
- `HowToSteps.tsx` — 3 步卡片网格
- `SplitSection.tsx` — 左右布局（图 + 文 + 可选 link），`mediaSide="left"|"right"`
- `SectionHeader.tsx` — H2 + description + align

**🔁 结构共享，文案定制（各页薄包装）**
- `HomeFAQ.tsx` — 首页对 `PageFAQ` 的文案封装
- `HowTo.tsx` / `UseCases.tsx` — 首页对 `HowToSteps` / `SplitSection` 的封装

**🧩 模式共享，组件独立**
- `src/components/apps/hero/AppHero.tsx` — apps 交互式 hero（控件 + samples + credits + eta）
- `src/components/apps/HeroShowcase.tsx` — apps 画廊
- `src/components/vofy/CompareSlider.tsx` — 通用 before/after 拖动
- `src/components/apps/CreatorTestimonials.tsx` — apps 通用证言
- `src/components/vofy/PromptBox.tsx` — 交互式 prompt 演示

**❌ 本页专属（示例，勿跨页 import）**
- `NodeGraphHero`（首页）
- `ShowcaseGallery` / `ThreePresets` / `WhenToUse` / `MoreTools`（`color-splash.tsx` 内部）
- `ecommerce` route 里的四个 `SplitSection` 具体文案

---

## 8. Checklist（发布前自检）

**Hard Rule（必须绿灯）**

1. `head()` 已设真实 `title` / `description` / `og:title` / `og:description` / `og:image`（leaf route，绝对 https URL 或 import 的 assets 常量）/ `twitter:card` / `canonical`，**无** `Lovable App` / `Lovable Generated Project` 默认值。
2. 页面存在 **且只有一个** `<h1>`；H1 Title Case ≤ 6 词、不含 "The / A / Vofy" 前缀；H2/H3/H4 sentence case。
3. FAQ + Breadcrumb JSON-LD 已注入 `<script type="application/ld+json">`（有分步流程再加 `HowTo`）。
4. 所有 `<Link to="...">` 指向真实 route 文件；`bun run build` 无 "Failed to resolve import" / 无重复 `/` 路由冲突。
5. **`SecondaryCTA` 必须在 `PageFAQ` 之后、`SiteFooter` 之前**（近期修复过 4 个页面漏了这条）。
6. 无 eyebrow / kicker；无装饰性 lucide 图标；H1–H4 无 italic。

**建议项**

- 每个 section 纵向节奏用 `mt-16` 或 `mt-20`。
- 每个 app 页至少一条自然锚文本内链回 `/` 或 `/use-cases` 或相邻 app。
- H1/H2/H3/lead 用 `H1_CLS` / `H2_CLS` / `H3_CLS` / `LEAD_CLS` 常量，不手抄。
- 图片写 `alt`；避免生成式插画代替真产品截图。

---

## 9. 反例

- ❌ 用 `#section` 把 Services / About / Pricing 全塞进 `/` —— 每个内容 section 都应有自己的 route（见现有 `/pricing`、`/models`、`/use-cases/*`）。Hash anchor 仅用于同页 TOC 滚动。
- ❌ 直接复制 `color-splash.tsx` 命名新 effect，但把 `ThreePresets` / `MoreTools` 里的 red-accent / ghibli 文案原样留下。命名换品类，文案也换。
- ❌ H1 写 `The Ultimate AI Studio for Everyone` —— 违反 Title Case + ≤ 6 词 + 无 "The" 前缀三条规则。改为 `AI Creative Studio`，"for everyone" 移到 lead。
- ❌ 在 `src/routes/` 下建 `_app/` / `pages/` / `layout.tsx` —— 不是 TanStack Start 约定，会与 `index.tsx` 冲突。
- ❌ 在 H2 上方加一行小字号 `EFFECTS · SELECTIVE COLOR` 或加装饰 `<Sparkles />` 图标 —— 违反"无 eyebrow / 无装饰 icon"规则。
- ❌ 给 `SecondaryCTA` 传 `secondaryLabel` / `trustItems` 以为会渲染 —— 组件已简化为只有 title / description / primary CTA，传了也是死代码。
- ❌ 用 `useEffect + fetch` 或 `useQuery + isLoading` 做首屏数据 —— TanStack 项目在 loader 里 `ensureQueryData`，组件里 `useSuspenseQuery`。