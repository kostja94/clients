# 页面搭建指南：以 MeDo 官网为例

面向内部同事（工程 / 内容 / 设计）与 AI agent，讲清楚我们如何用「共享骨架 + 每页定制的内容组件」的方式，快速搭一个新的 MeDo landing / builder / use-case / blog 页面，并保持整站结构、SEO 与内链一致。

---

## 速查卡

> 如果你只读 30 秒，看这里。

| 概念 | 一句话 |
|---|---|
| ✅ 共享组件 | 直接 import 同一个 `.tsx`，只传 props（`SiteNavbar`、`SiteFooter`、`FinalCTA`、`FormatCarousel`、`UseCasesSection`、`HowToStepsSection`）|
| 🔁 结构共享，文案定制 | 调用同一个共享组件，只传本页 props（Hero、FAQ、Compare、Steps 骨架）|
| 🧩 模式共享，组件独立 | 视觉/字段契约一致但目前是独立组件（`HealthFeatureCarousel` vs `FormatCarousel`；各 builder 页的 `Showcase` / `AppTypes` / `ExploreMoreBuilders`）|
| ❌ 本页专属 | 命名带页面前缀，不进复用池（`InteractiveDemo`、`EcommercePromptComposer`、`IPhoneFrame`）|
| 页面骨架 | `SiteNavbar → Breadcrumbs → Hero → …内容 blocks… → FAQ → FinalCTA → SiteFooter` |
| 每页必配 | `head()` 里的 `title` / `description` / `og:*` / `twitter:*` / `canonical` + FAQ + Breadcrumb JSON-LD |

### 我该从哪开始？

| 你是 | 先读 |
|---|---|
| 第一次看 | §1 核心理念 → §2 工作流 → §3 参考页面 |
| 要搭 builder 页 | §2 工作流 → §4 Builder 页模板 → §7 Checklist |
| 要写文案 | §5 文案规则 → §7 Checklist |
| 要判定复用等级 | §1 复用等级 → §6 组件目录 |

---

## 1. 核心理念

一个 MeDo 页面 = **共享骨架 block** + **若干内容 block**。

- **共享骨架**（所有页面必须存在，顺序固定）
  `SiteNavbar → Breadcrumbs → Hero → …内容 blocks… → FAQ → FinalCTA → SiteFooter`
- **内容 block**（可复用、结构固定、**文案按页定制**）
  当前武器库：`FormatCarousel` / `HealthFeatureCarousel`（feature 轮播）、`Showcase`（案例卡片）、`AppTypes`（能构建的 app 类型网格）、`UseCasesSection`（场景卡片）、`HowToStepsSection`（步骤说明）、`Compare`（对比表）、`ExploreMoreBuilders`（跳转其他同类 builder）、`FAQ`。

同一个 block 在不同页面里：

- **组件结构完全一致**（栅格、动画、卡片视觉、字段契约）
- **文案完全不同**（针对当前品类挑选最相关的叙事）
- 描述中用自然锚文本内链，把权重回流到 `/ai-mobile-app-builder`、`/features`、其他 builder 子页与 blog

### 复用等级

| 等级 | 含义 | MeDo 现有例子 |
|---|---|---|
| ✅ 共享组件 | 一份代码，多页 import，只传 props | `SiteNavbar`、`SiteFooter`、`FinalCTA`、`Logo`、`FormatCarousel`、`UseCasesSection`、`HowToStepsSection` |
| 🔁 结构共享，文案定制 | 同一组件的不同实例，只换 props | 每个 builder 页里的 `FAQ` / `Compare` / `Steps` 骨架 |
| 🧩 模式共享，组件独立 | 契约相同但当前是独立组件，未来可收敛 | `HealthFeatureCarousel` ↔ `FormatCarousel`；各页 `Showcase` / `AppTypes` |
| ❌ 本页专属 | 命名带页面前缀，不进复用池 | `InteractiveDemo`（`/ai-mobile-app-builder`）、`EcommercePromptComposer`、`IPhoneFrame` / `PixelFrame` |

> **模板 + 单页独有组件**
> 同类 builder 子页（`/ai-mobile-app-builder/health-and-fitness`、未来的 `/gaming`、`/kids` 等）共享同一份 section 模板。当某页有独特叙事（例：`/ai-mobile-app-builder` 需要 `InteractiveDemo` 演示双端生成；`/ai-website-builder/ecommerce` 需要 `EcommercePromptComposer`），插入 ❌ 等级的本页专属组件即可，不需要在其他页面补齐同名占位。

---

## 2. 设计新页面的工作流（先规划，再动手）

**不要**直接 copy 某个 route 就开始改文案 —— 会遗漏本页独特组件，也会留下模板里用不上的 section。

### 2.1 三步规划

1. **定位页面类型**：landing / builder hub / builder 子页（垂直品类）/ use-case / blog / compare。找 1–2 个最接近的现有页面做参考。
   - Builder hub → `/ai-mobile-app-builder`
   - Builder 垂直子页 → `/ai-mobile-app-builder/health-and-fitness`
   - 电商类 landing → `/ai-website-builder/ecommerce`
   - Feature hub → `/features`
   - 对比页 → `/explore/vs/lovable`
2. **写 Blueprint**：一页 markdown 列清楚
   - `route path` + `canonical` URL
   - `<title>`（≤ 60 字符，含主关键词）+ `meta description`（≤ 160 字符）
   - H1 + 每个 section 的 H2（关键词友好，例如 `Why Choose MeDo AI Health & Fitness App Builder`）
   - 复用的 block（标注等级 ✅🔁🧩）与本页独有的 ❌ 组件
   - 内链目标（哪些锚文本指向哪些站内页面）
   - JSON-LD：FAQ + Breadcrumb 必配；有产品/软件属性时加 `SoftwareApplication`
3. **确认后再编码**。

### 2.2 编码顺序

1. 建 `src/routes/<path>.tsx`，先把骨架 + `head()` + JSON-LD 打通（跑 `tsgo` / `bun run build` 保证类型和路由树无红）。
2. 从上到下填 sections：Hero → 内容 blocks → FAQ → FinalCTA。
3. 每个新增的 ❌ 组件放同文件内直到需要跨页复用时再抽到 `src/components/features/`。
4. 图片走 `src/assets/*.jpg`（1200×630 或 1280×672 横向为默认社交/展示比例）。

---

## 3. 参考页面速览

| 路由 | 类型 | 参考价值 |
|---|---|---|
| `/features` | Feature hub | `FormatCarousel` 用法 + TabStrip + Compare + FAQ 全套 |
| `/ai-mobile-app-builder` | Builder hub | `InteractiveDemo` 独家演示 + PlatformSection + Steps + Compare + FAQ |
| `/ai-mobile-app-builder/health-and-fitness` | Builder 垂直子页 | Showcase + `HealthFeatureCarousel` + `AppTypes` + `UseCasesSection` + `HowToStepsSection` + `ExploreMoreBuilders` + FAQ，**新垂直子页的标准范本** |
| `/ai-website-builder/ecommerce` | Website builder 子页 | `EcommercePromptComposer` + Features + Steps + Templates + Compare + Testimonials + FAQ |
| `/explore/vs/lovable` | 对比页 | Compare 表格叙事结构 |
| `/blog/how-to-build-mobile-app-with-ai` | Blog 文章 | 长文正文与 JSON-LD |

---

## 4. Builder 垂直子页模板（以 `/ai-mobile-app-builder/health-and-fitness` 为准）

以此为**新增品类**（gaming / kids / entertainment / social / education / finance …）的标准起点：

```
SiteNavbar
Breadcrumbs                              // Home › AI Mobile App Builder › <Category>
Hero                                     // H1 含 "AI <Category> App Builder"；副标题 + 2 个 CTA
Showcase (H2)                            // "<Category> App Showcase — Built with MeDo"，指向 marketplace
HealthFeatureCarousel (H2)               // "Why Choose MeDo AI <Category> App Builder"（🧩 每品类一份内容，组件可复用）
AppTypes (H2)                            // "What You Can Build With MeDo <Category> App Builder"
UseCasesSection (H2)                     // "<Category> App Use Cases — Powered by MeDo"（✅ 通用组件，每品类定制内容）
HowToStepsSection (H2)                   // "How to Build a <Category> App With MeDo"（✅ 通用组件，每品类定制内容）
ExploreMoreBuilders (H2)                 // "Explore More AI Mobile App Builders"，卡片跳其他品类
FAQ (H2)                                 // "<Category> App Builder FAQ" + FAQPage JSON-LD
FinalCTA
SiteFooter
```

**每个 H2 必须包含主关键词 + `MeDo` 或 `<Category> App Builder`**（对 SEO 与内部组件识别都友好）。

---

## 5. 文案规则

- **H1**：一句话说清"MeDo 是什么样的 builder + 输出什么"，包含核心关键词（例：`AI Health & Fitness App Builder`）。
- **H2**：见 §4，关键词友好、组件友好。禁止纯品牌口号型 H2（如 `One Prompt. Every Device.`），改为 `Why Choose MeDo AI <X> Builder`。
- **卡片描述**：1–2 句，避免"AI-powered 一切" 的空话；写清楚 **对谁 / 做什么 / 输出什么**。
- **内链**：在描述里以自然锚文本链回相邻 builder / features / blog；不做"点击这里"。
- **CTA**：主 CTA 统一"Start Building for Free"（或对应品类），副 CTA 指向 Marketplace / Docs。
- **图片**：写实产品截图 / mock，默认 1200×630 或 1280×672 横向；避免生成式插画风格。

---

## 6. 组件目录

**✅ 共享**
- `src/components/marketing/SiteNavbar.tsx`
- `src/components/marketing/SiteFooter.tsx`
- `src/components/marketing/FinalCTA.tsx`
- `src/components/marketing/Logo.tsx`
- `src/components/features/FormatCarousel.tsx`
- `src/components/features/UseCasesSection.tsx`（通用场景卡片网格，每品类通过 props 传入不同的 useCases）
- `src/components/features/HowToStepsSection.tsx`（通用步骤说明，每品类通过 props 传入不同的 steps）

**🧩 模式共享**
- `src/components/features/HealthFeatureCarousel.tsx`（未来可与 `FormatCarousel` 合并为通用 `FeatureCarousel`）
- 各 builder 子页中的 `Showcase` / `AppTypes` / `ExploreMoreBuilders`（当第二个品类页落地时抽公共组件到 `src/components/features/`）

**❌ 本页专属（示例，勿跨页 import）**
- `InteractiveDemo` / `IPhoneFrame` / `PixelFrame`（`/ai-mobile-app-builder`）
- `EcommercePromptComposer`（`/ai-website-builder/ecommerce`）

---

## 7. Checklist（发布前自检）

**Hard Rule（必须绿灯）**

1. `head()` 已设置真实 `title` / `description` / `og:*` / `twitter:card` / `canonical`，无 `Lovable App` / `Lovable Generated Project` 默认值。
2. 页面存在 **且只有一个** `<h1>`；每个 H2 含品类主关键词。
3. FAQ 与 Breadcrumb JSON-LD 均已注入 `<script type="application/ld+json">`。
4. 所有 `<Link to="...">` 指向真实存在的 route 文件；`bun run build` 无 "Failed to resolve import"。

**建议项**

- 图片使用 `src/assets/*.jpg`（1200×630 或 1280×672），并写 `alt`。
- 每个 section 的纵向间距使用 `py-14/16`，避免大片空白。
- 每个 builder 子页至少 1 条自然锚文本内链回 `/ai-mobile-app-builder` hub。
- `ExploreMoreBuilders` 里的品类卡片，尚未上线的加 `Coming soon` 徽标而非死链。

---

## 8. 反例

- ❌ 用 `#anchor` 把 Services / About / Contact 全部塞进 `/` —— 每个独立内容 section 应该拥有自己的 route（见现有 `/features`、`/ai-mobile-app-builder/*`）。
- ❌ 直接复制 `/ai-mobile-app-builder/health-and-fitness` 命名新品类，但把 `HealthFeatureCarousel` / Health 文案原样留下。命名与文案必须换成新品类。
- ❌ H2 写成 `Built With MeDo. Shipped by the Community.` 这种品牌口号 —— 换成 `<Category> App Showcase — Built with MeDo`。
- ❌ 在 `src/routes/` 下建 `_app/` 或 `pages/` 目录（不是 TanStack Start 约定，会与 `index.tsx` 冲突）。
- ❌ 把品类 role 卡片的图片直接用生成式插画代替产品截图。
