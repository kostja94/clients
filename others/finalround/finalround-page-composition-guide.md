# 页面搭建指南：以 Coding Interview Copilot 为例

面向内部同事，讲清楚我们如何用"共享 block + 每页定制的内容组件"的方式，快速搭一个新的 landing page，并保持整站的结构、SEO、内链一致性。

---

## 1. 核心理念

一个 landing page = **共享骨架 block** + **若干内容 block**。

- **共享骨架**（7 个，所有页面必须存在，顺序固定）  
  `Navbar → PageBreadcrumb → Hero → …内容 blocks… → SectionFAQ → SectionCTA → Footer`
- **内容 block**（可复用、结构固定、**文案按页定制**）  
  例如 `UseCases / HowItWorks / FeatureCarousel / Comparison / OtherFeatures / Testimonials`。

同一个"内容 block"在不同产品页里：
- **组件结构完全一致**（栅格、动画、卡片视觉、字段契约）
- **文案完全不同**（针对当前产品挑选最相关的场景）
- 通过描述里的**上下文内链**（自然锚文本 `<Link>`），把权重回流到 `/use-cases` hub 或其他产品页

> **复用等级说明**（贯穿全文）
> - ✅ **共享组件**：直接 import 同一个 `.tsx`，只传 props。例：`PageHero`、`SectionCTA`、`SectionFAQ`、`PageBreadcrumb`。
> - 🔁 **结构共享，文案定制**：包一层 `<Product>*.tsx`，内部渲染共享组件，只是把该页专属文案传进去。例：所有 `*CTA.tsx` / `*HeroSection.tsx` / `*FAQ.tsx`。
> - 🧩 **模式共享，组件独立**：视觉/契约一致但目前是三个独立组件，未来可抽成通用组件。例：`*UseCases.tsx`、`*OtherFeatures.tsx`。
> - ❌ **本页专属**：不进复用池。例：`CodingSafety`、`PhoneToolkit`、`MockComparison`。

> **模板 + 单页独有组件**  
> 同类产品页（如所有 XXX Interview Copilot 页）共享同一份 section 模板；但当某个页面有**其他页面不需要**的独特叙事时（例：Coding 需要 "undetectable safety"、Phone 需要 "phone toolkit"、Mock 需要 "vs traditional tools" 对比），可以在模板中插入本页专属组件。这类组件属于 ❌ 等级，命名带产品前缀（`<Product><FeatureName>.tsx`），不进复用池，也不需要在其他产品页里补齐同名占位。

---

## 2. 设计新页面的工作流（先规划，再动手）

**不要**上来就复制某个产品页开始改文案 —— 那是 vibe coding，会遗漏本页真正需要的独特组件，也会把模板里用不上的 section 顺手留下。正确顺序：

### 2.1 三步规划

1. **定位页面类型**：属于产品页 / use-case 页 / hub 页 / 文章页 / 落地页 中的哪一类？找出 1–2 个最接近的现有页面作为参考
2. **列 section 清单**：写下本页要讲的**叙事顺序**（不是 section 名，而是"用户滚到这里应该获得什么信息"），再把每条叙事映射到组件
3. **对每个组件判定复用等级**（✅ / 🔁 / 🧩 / ❌），并标注：
   - 属于 ✅ / 🔁：直接列共享组件名 + 需要传的 props
   - 属于 🧩：列出参考的镜像组件（如新 use-case 页的 Products 参考 `SoftwareEngineersOtherTools`）
   - 属于 ❌：说明为什么其它页面不需要 → 证明它确实是本页专属

### 2.2 用 ASCII 线框图落地规划

在 PR 描述或 `docs/` 下新建一个 `.md` 文档，用 ASCII tree 画出页面骨架，例如新增 `/use-cases/big-tech` 时：

```text
BigTechUseCasePage
├── Navbar                          ✅ 共享
├── PageBreadcrumb                  ✅ 共享     items: Use Cases › Big Tech
├── PageHero                        🔁 结构共享  variant="centered"
│    ├── H1: Big Tech Interview Prep
│    └── subtitle + 1 CTA → /interview-copilot
├── BigTechStats                    ❌ 本页专属  ← FAANG offer rates / TC 数据
├── BigTechFeatureCarousel          🧩 模式共享  参考 CodingFeatureCarousel，8 张
├── BigTechProducts                 🧩 镜像组件  ← §7 镜像 CodingUseCases
│    └── 6 张：Copilot / Coding / Mock / Phone / Resume / LinkedIn
│                （每张 description 按 big-tech 场景改写）
├── BigTechLoopBreakdown            ❌ 本页专属  ← phone screen → onsite → team match
├── TestimonialsSection             ✅ 共享     filter: bigtech tag
├── SectionFAQ                      🔁 结构共享  10 条 big-tech 相关 QA
├── SectionCTA                      🔁 结构共享  "Ready to ace your Big Tech loop?"
└── FooterSection                   ✅ 共享
```

这样做的收益：

- **一眼看出哪些是新组件**（❌ 标记），可以提前评估工作量
- **一眼看出镜像关系**（🧩 标记），避免和现有页面文案重复
- **section 顺序是文档，不是代码**，讨论/评审时不用打开 IDE
- 未来读代码的人打开 `docs/<page>-blueprint.md` 就能理解设计意图

### 2.3 规划文档模板

新页面开工前，建议在 `docs/blueprints/<page-name>.md` 建一份 blueprint，包含：

```markdown
# <PageName> Blueprint

## 页面定位
- 类型：产品页 / use-case 页 / hub 页 / …
- 参考页面：<path/to/reference-page.tsx>
- 目标关键词：<seo keywords>

## 叙事顺序
1. 用户滚到 X 时应该获得 Y 信息
2. …

## Section 骨架（ASCII）
```text
<在这里画 ASCII tree>
```

## 新增组件清单
- ❌ `<Product><Feature>.tsx` — 用途 / 为什么其它页面不需要
- 🧩 `<Slug>Products.tsx` — 镜像自 <existing component>

## 复用组件清单
- ✅ / 🔁：<component> + 关键 props
```

**[Hard Rule]** blueprint 文档评审通过后，再开始写 `.tsx`。这一步不做，后面复用等级判定和镜像检查都会变成事后返工。

---

## 3. Case Study：Coding Interview Copilot 页面拆解



文件：`src/pages/CodingInterview.tsx`

| 顺序 | Section | 组件 | 复用等级 | 说明 |
|---|---|---|---|---|
| 1 | Nav | `Navbar` | ✅ 共享 | 全站统一 |
| 2 | 面包屑 | `PageBreadcrumb` | ✅ 共享 | 只传 `items`，3 级结构 |
| 3 | Hero | `CodingHeroSection` → `PageHero` | 🔁 结构共享 | 只使用 `centered` / `split` 两种 variant（`dual-cta` 已废弃）。**[Hard Rule]** 每页只保留 1 个 CTA |
| 4 | 功能轮播 | `CodingFeatureCarousel` | 🧩 模式共享 | 各产品页独立文件，卡片契约一致 |
| 5 | **Use Cases** | `CodingUseCases` | 🧩 模式共享 | 本文档重点，见 §4 |
| 6 | How It Works | `CodingHowItWorks` | 🧩 模式共享 | 3–4 步，结构一致 |
| 7 | Testimonials | `TestimonialsSection` | ✅ 共享 | 全站同一份 |
| 8 | Safety | `CodingSafety` | ❌ 本页专属 | 强调 undetectable |
| 9 | Other Features | `CodingOtherFeatures` | 🧩 模式共享 | 见 §6，可跨模板 |
| 10 | FAQ | `CodingFAQ` → `SectionFAQ` | 🔁 结构共享 | 只传不同 QA 数组 |
| 11 | 最终 CTA | `SectionCTA` | 🔁 结构共享 | 每页定制 `title/gradientWord/description/CTA`，模板 `Ready to ace your next … interview?` |
| 12 | Footer | `FooterSection` | ✅ 共享 | 全站统一 |


Mock Interview、Phone Interview 页面遵循同样的 section 顺序，只是把 `Coding*` 换成 `Mock*` / `Phone*`。

---

## 4. 重点示范：UseCases 组件模式

这是本次要重点讲清楚的**可跨模板复用**的内容 block。

### 4.1 组件契约

所有 `*UseCases.tsx` 都遵循同一份数据结构：

```ts
interface UseCase {
  eyebrow: string;        // 场景分类标签（如 "Behavioral Rounds"）
  title: string;          // 简短卡片标题（如 "STAR stories on demand"）
  description: ReactNode; // 1–2 句描述，允许内嵌 <Link> 做上下文内链
}
```

视觉与交互也完全一致：

- 6 张卡片，`grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`
- `framer-motion` 依次淡入
- Section 标题模板：`Use cases for the <Product Name>`
- 副标题模板：`From X to Y — <Product> adapts to every …`

### 4.2 三个现有实例对比

| 页面 | 组件 | 6 张卡片挑选的 use case | 内链回 `/use-cases/*` |
|---|---|---|---|
| Coding Interview | `CodingUseCases.tsx` | Algorithms, Big Tech, Pair Programming, Virtual Onsite, Take-homes, Polyglot | `/use-cases/big-tech`、`/use-cases/virtual-onsite` |
| Mock Interview | `MockUseCases.tsx` | Behavioral, Technical Loops, FAANG, Consulting/Product, Recruiter Screens, Global Loops | `/use-cases/big-tech`、`/use-cases/remote-jobs` + 跨产品链 `/coding-interview`、`/phone-interview` |
| Phone Interview | `PhoneUseCases.tsx` | Recruiter Screens, Technical Screens, Hiring Manager, Behavioral, In-Person, Global Loops | `/use-cases/remote-jobs` + 跨产品链 `/coding-interview` |

**关键观察**：三个组件的**结构和视觉是同一个模板**，但没有一张卡片文案是重复的——每个产品挑了对它自己叙事最有说服力的场景，并且把描述里的锚文本自然地链到 `/use-cases/*` hub 的对应子页。

### 4.3 文案编写规则

搭一个新产品页的 UseCases block 时，按顺序做：

1. **打开 `/use-cases` hub** (`src/pages/UseCasesHub.tsx`)，浏览四个维度（role / company / round / format）下的所有 slug
2. **挑 3–6 个和本产品高度相关的 slug**（比如 Resume Builder 页可以挑 `software-engineers` / `career-changers` / `new-grads`）
3. **补足到 6 张卡片**，剩下的 2–3 张不必链回 use-cases hub，可以链到**其他产品页**（跨产品互链），也可以纯粹是场景描述
4. **在 description 句子中用自然锚文本 `<Link>`**——不是"Learn more →"这种按钮式链接
5. **[Convention]** eyebrow 使用短分类词（1–2 词），title 使用**结果导向**的短句（≤ 40 字符）
6. **[Recommended]** description 保持 1–2 句、20–35 词，太长影响卡片视觉一致性

### 4.4 什么时候用 UseCases 组件

**适合放**：任何需要"多场景覆盖 / 多角色覆盖"叙事的 landing page。  
包括与 coding interview **不同模板**的页面，例如：

- `AIResumeBuilder` → 挑 `/use-cases/software-engineers`、`/use-cases/career-changers` 等
- `AIJobHunter` → 挑 `/use-cases/remote-jobs`、`/use-cases/new-grads` 等
- `LinkedInProfileOptimizer` → 挑 role/format 相关 slug

**不适合放**：功能单一、只解决一个场景的工具页（例如某个单点小工具），此时用 `FeatureCarousel` 或 `HowItWorks` 更合适。

---

## 5. FeatureCarousel 的 SEO 定位

`*FeatureCarousel.tsx` 是页面里唯一一个**鼓励堆内容**的 block。原因很直接：

- **形态是横向轮播**，视觉高度固定，加更多幻灯片不会撑高页面、不会让用户觉得臃肿
- **每张幻灯片都是独立 DOM**，SEO 抓取时可以计入完整正文，等价于把 6–10 段产品叙事塞进一屏视觉里
- 用户只看轮播头 1–2 张，但爬虫看全部——这是"人看视觉、机器看内容"的最佳平衡点

### 5.1 写作规则

1. **每张幻灯片配一段 40–90 词的正文**，别只写 1 句话。展开产品能力、场景、结果指标
2. **在文案里自然埋关键词**：产品别名（Coding Copilot / Coding Interview Copilot / Real-time Coding AI）、平台名（LeetCode、HackerRank、CoderPad、Zoom）、场景词（virtual onsite、pair programming）
3. **正文里加 1–2 个上下文 `<Link>`**，指向 use-cases 子页或姐妹产品页 —— 每张幻灯片都是一个内链机会
4. **[Recommended]** 幻灯片数量：**6–10 张为最佳**。少于 5 张不值得做轮播，多于 10 张爬虫权重被稀释
5. 每张卡片保留统一字段：`title` / `subtitle` / `body`（长文）/ `image` / `bullets?[]`

### 5.2 为什么其它 block 不能这样堆

- Hero / CTA / FAQ / UseCases / OtherFeatures 都是**纵向 stack**，堆内容 = 页面变长 = 跳出率上升
- FeatureCarousel 是唯一"内容量与视觉高度解耦"的组件，因此是产品页承载长尾 SEO 词的主力

---

## 6. Other Features / Other Tools 模式



和 UseCases 同属"🧩 模式共享"级别，视觉一致但目前是多个独立组件：

| 页面 | 组件 | 页面角色 | 卡片用途 |
|---|---|---|---|
| Coding Interview | `CodingOtherFeatures.tsx` | 产品详情页 | 推其他产品 |
| Mock Interview | `MockOtherFeatures.tsx` | 产品详情页 | 推其他产品 |
| Use Case (SWE) | `SoftwareEngineersOtherTools.tsx` | use-case 子页 | 推适用于该场景的产品 |
| Company Layoff | `LayoffProductsBlock.tsx` | 公司裁员子页 | 推产品 |
| Layoffs Tracker | `LayoffsProducts.tsx` | hub 聚合页 | 展示分类子页列表 |

> **两类用途，同一套视觉**：详情页（产品页 / use-case 子页 / 公司裁员子页）用卡片**推产品**；hub 聚合页（`/tech-layoffs`、`/internships` 等）用卡片**展示分类子页列表**。两者 `items[]` 契约和视觉完全一致，差别仅在于 `href` 指向目标不同。

**共同契约**：`items[] = { image, title, description, href }`，栅格 `grid-cols-2 sm:grid-cols-3`，卡片带图 + 标题 + 1–2 句描述 + "Learn more →"。

### 6.1 什么时候用

任何非工具页 / 非文章页，只要页面底部想引导用户去试其他产品，都可以放。**跨模板同样适用**：

- Resume Builder → 推 Copilot / Mock / LinkedIn Optimizer
- Internship 页 → 推 Resume / Mock / Job Hunter
- Layoffs 页 → 推 Resume / Job Hunter / Copilot
- Use Cases 子页 → 推该场景相关的 2–3 个产品

### 6.2 文案规则

1. **[Recommended]** 6 张卡片是当前视觉最稳的数量（2×3 / 3×2）
2. **[Convention]** `title` 用**产品名**，不用行动短语
3. `description` 1 句、把该产品**对当前页面上下文的价值**说出来（例：Coding 页的 Resume 卡片会强调 "the source for personalized coding warm-ups"）
4. **[Hard Rule]** 不重复跨页文案 —— 每个页面都要针对自己上下文改写 description
5. 保持 6 个 href 都是站内绝对路径，方便 SEO 抓取

### 6.3 未来抽象

与 §7.2 的 `CardGrid` 收敛方向一致：将上述 5 个组件降级为 data-only 定义，共用同一个渲染组件。详见 §7.2。

---

## 7. 双向内链：产品 ↔ Use Case 的镜像组件

这是本项目组件复用的**核心理念**——同一套「卡片契约 + 视觉模板」可以两个方向使用，主语和宾语互换：

| 方向 | 所在页面 | 组件示例 | 主语（固定） | 宾语（挑选 + 改写） |
|---|---|---|---|---|
| 产品页 → Use Case | `/coding-interview` | `CodingUseCases.tsx` | Coding Interview Copilot | 从 `/use-cases/*` 池挑 6 个场景 |
| Use Case 页 → 产品 | `/use-cases/software-engineers` | `SoftwareEngineersOtherTools.tsx` | Software Engineers 场景 | 从产品池挑 N 个产品 |

两者是**镜像关系**：coding 页说"我这个产品能覆盖 big-tech / virtual-onsite 等场景"，software-engineers 页反过来说"作为 SWE，你可以用 Copilot / Mock / Resume 等产品"。

### 7.1 每一类页面都应有自己的 Products 组件

Use Case 子页不该只有共享的 `RelatedFeatures`，而应该像产品页有 `*UseCases.tsx` 一样，**各自有一份 `<UseCaseSlug>Products.tsx`**：

- `/use-cases/software-engineers` → `SoftwareEngineersOtherTools.tsx` ✅ 已存在
- `/use-cases/big-tech` → 建议新增 `BigTechProducts.tsx`（例：Coding Copilot 描述改成 "handle FAANG-style algorithm rounds under real interviewer pressure"）
- `/use-cases/remote-jobs` → 建议新增 `RemoteJobsProducts.tsx`（例：Phone Copilot 描述改成 "invisible support on async recruiter screens across time zones"）
- `/use-cases/virtual-onsite` → 建议新增 `VirtualOnsiteProducts.tsx`

**关键点**：同一个产品（如 Interview Copilot）在不同 use-case 页里，`title/image/href` 完全一样，但 `description` **必须按当前场景改写**。这正好和产品页里 UseCases 组件"同一个场景在不同产品页改写"是镜像的。

### 7.2 抽象后的通用组件

`OtherToolsGrid` 和产品页里 `*UseCases.tsx` 底层其实是**同一个组件**（都是 6 张 image-optional 卡片 + 描述内嵌 `<Link>`），只是数据源不同：

```
<CardGrid
  title=...            // "Use cases for X"  |  "Tools for Y scenario"
  description=...
  items={[
    { eyebrow?, title, description(含 <Link>), image?, href? },
    ...
  ]}
/>
```

未来收敛方向：`CodingUseCases` / `MockUseCases` / `PhoneUseCases` / `*OtherFeatures` / `<UseCaseSlug>Products` 全部降级为 data-only 文件，共用同一个渲染组件。

### 7.3 类比拓展

这条镜像原则不止于「产品 ↔ use-case」，站内所有 hub ↔ 详情关系都适用：

| Hub 页 | 详情页 | 镜像组件对 |
|---|---|---|
| `/use-cases` hub | `/use-cases/<slug>` | UseCase 卡片 ↔ Products 卡片 |
| `/compare` hub | `/compare/<slug>` | Alternative 卡片 ↔ ComparisonHighlights 卡片 |
| `/tech-layoffs` hub | `/tech-layoffs/<company>` | CompanyCard ↔ RelatedCompanies |
| `/explore` hub | 各产品页 | ProductCard ↔ OtherFeatures |

每一对都遵循「主语固定、宾语挑选并按上下文改写描述」的同一套写作规范。



---

## 8. 新页面搭建 checklist

1. **先写 blueprint**：按 §2.3 模板在 `docs/blueprints/<page>.md` 画 ASCII 骨架，标注每个 section 的复用等级，评审通过再动手
2. 确定产品/场景在 `/explore` 或 `/use-cases` 中的定位，找参考页面
3. 复制最接近的目录作为骨架（产品页从 `src/components/coding-interview/` 复制；use-case 页从现有 UseCasePage 模板复制）；对 blueprint 里 ❌ 标记的组件新建文件，对 🧩 标记的组件参考对应镜像组件写

4. 逐个 section 决定复用等级：✅ 直接用 / 🔁 包壳传 props / 🧩 新建同模式组件 / ❌ 本页专属
5. UseCases block 按 §4.3 规则挑 slug、写文案、加内链
6. Other Features / Products block 按 §6.2 + §7 规则挑对象、按上下文改写 description
7. 写 Hero 时用 `PageHero` 的 variant 之一，不要自己起 layout
8. 写 FAQ / CTA 时套用 `SectionFAQ` / `SectionCTA` 壳，CTA 标题遵循 `Ready to ace your next … interview?` 模板
9. 校对：
   - **[Hard Rule]** Hero 只留 1 个 CTA
   - **[Hard Rule]** `text-gradient-primary` 每页仅 1 处（H1）
   - **[Hard Rule]** 面包屑 3 级
   - **[Hard Rule]** 内链的 `/use-cases/<slug>` 都真实存在于 Supabase `use_cases` 表
   - **[Recommended]** section 背景色遵循 `bg-secondary/30` 交替规则

### 8.2 页面健康指标

搭好页面后，用以下指标判断页面是否有效——避免只忙于搭页面而不知道页面是否有效：

| 指标 | 健康线 | 说明 |
|------|--------|------|
| 索引速度 | < 7 天 | 发布后被搜索引擎收录的耗时 |
| 跳出率 | < 55% | 用户进来只看一页就离开的比例 |
| CTA 点击率 | > 3% | CTA 按钮点击 / 页面 UV |
| 内链 404 数 | 0 | 自动化检查，不允许存在断链 |
| 转化率 | > 1% | 完成注册/付费等目标行为的比例 |

> 这些指标不是硬性规范，而是帮助团队判断页面是否"活着"。超出健康线时优先排查内容质量和内链。

---

## 9. 反例 / 常见错误

- ❌ 把 UseCases / OtherFeatures 卡片写成 "Learn more →" 按钮式布局 —— 失去自然内链的 SEO 价值
- ❌ **文案交叉复制**：两个产品页之间复制 UseCases / OtherFeatures 文案，或在 use-case 页复用产品页的 OtherFeatures 描述 —— 违反镜像原则（§7），description 必须按当前场景改写，否则相关性和独特性归零
- ❌ Hero 自己写 layout 而不用 `PageHero` variant —— 破坏全站视觉一致
- ❌ Hero 放 2 个 CTA —— 违反本项目"单 CTA"约定
- ❌ 一页出现多个 `text-gradient-primary` —— 违反 color discipline
- ❌ 在描述里内链到根本不存在的 `/use-cases/<slug>` —— 会产生 404
- ❌ 为图省事把 `CodingUseCases` / `CodingOtherFeatures` 直接 import 到 Resume 页面 —— 应该新建 `Resume*.tsx`，文案独立


---

## 10. 内容与组件分离：用数据库存文案

组件里 hardcode 文案是当前的过渡状态。**长期方向**：把每个组件对应的字段（title / description / items / links / images…）存进数据库（Supabase JSONB），组件只负责渲染。这样做把三件事彻底分开管理：

| 维度 | 归属 | 改动影响 |
|---|---|---|
| **设计**（视觉、栅格、动画、颜色） | `.tsx` 组件 + Tailwind token | 改一次，所有引用该组件的页面同步变 |
| **技术**（数据契约、路由、SEO 结构） | TypeScript interface + Supabase 表结构 | schema 变更走 migration，字段和组件强绑定 |
| **内容**（每页文案、内链锚文本、卡片顺序） | Supabase JSONB 行 | 改文案不动代码，运营/内容团队可直接编辑 |

### 10.1 当前已经这样做的例子

- `use_cases` 表 → `UseCasePage.tsx` 渲染
- `company_layoffs` 表 → `CompanyLayoffPage.tsx` 渲染
- `company_internships` 表 → `CompanyInternshipPage.tsx` 渲染
- `compare_alternatives` 表 → `CompareDetail.tsx` 渲染

这些页面新增一个 slug 完全不用改代码，只 insert 一行 JSONB。

### 10.2 建议下沉到数据库的组件

优先把「🧩 模式共享 + 文案定制」这一类下沉，因为它们最容易踩"字段和组件对不上"的坑：

- `*UseCases.tsx` 的 6 张卡片 → `product_use_cases` 表 或 挂在产品表 JSONB 的 `useCases[]`
- `*OtherFeatures.tsx` / `<Slug>Products.tsx` → 同一张 `product_cross_links` 表，用 `(source_slug, target_slug)` 做键，`description` 按当前源页面改写
- `*FAQ.tsx` 的 QA 数组 → `page_faqs` 表，可按 `page_slug` 查询
- `*FeatureCarousel.tsx` 的 6–10 张幻灯片 → `page_carousels` 表

产品 Hero、CTA 这类每页仅 1 条数据的，可以直接和 `pages` 主表合并成一行。

> **示例：一行 JSONB 怎么驱动一个 UseCases 组件**
> ```json
> {
>   "product_slug": "coding-interview",
>   "use_cases": [
>     {
>       "eyebrow": "Big Tech",
>       "title": "FAANG-ready algorithm rounds",
>       "description": "Live coding support tuned for <a href='/use-cases/big-tech'>Big Tech loops</a> — from phone screen to onsite.",
>       "image": "/images/use-cases/big-tech.svg"
>     }
>   ]
> }
> ```
> 组件渲染时只需 `select use_cases from product_use_cases where product_slug = $slug`，不改 `.tsx`。新增场景 = 追加一行 JSON 数组元素。

### 10.3 好处

1. **一次改设计，全站生效**：改 `CardGrid.tsx` 的 padding / 阴影 / 动画，所有引用它的页面立刻变，不会漏掉某个 hardcode 版本
2. **字段和组件强绑定**：新增字段先改 TS interface + migration，组件立刻编译报错提示，避免"组件读不到字段/字段没渲染"这种脱节
3. **内容独立版本化**：文案变更走 DB migration 或后台编辑记录，和代码 PR 解耦，不用为了改一句话开一个前端 PR
4. **易于导出 / 迁移**：整站内容就是几张表的 JSON dump，换 CMS、换框架、做多语言、做 A/B 都比翻代码里的字符串容易几个量级
5. **AI 生成 / 批量生产**：新加 50 个 use-case 子页只是 50 行 insert，不用 50 个 `.tsx`

### 10.4 迁移建议（渐进式）

不要一次全下沉。按 §2 blueprint 做新页面时，同时问一句"这些字段的下一个使用场景是不是也应该复用？"：

1. **第一步**：新页面走 blueprint 流程时，把每个组件的字段先写成 TypeScript interface，即使先用常量数组喂数据
2. **第二步**：当同一份 interface 出现在 ≥ 2 个页面时，建 Supabase 表 + migration，把两处数据同时迁进去
3. **第三步**：老页面按优先级（流量高、文案改动频繁的先）逐步替换 hardcode → DB fetch
4. **第四步**：抽出 §7.2 里说的通用 `CardGrid` 组件，让所有 UseCases / OtherFeatures / Products 类卡片都读同一张表，只 `where` 条件不同

### 10.5 反例

- ❌ 组件里既读 DB 又保留 hardcode fallback —— 两份真相，永远有一份是旧的
- ❌ 字段直接展开成一堆平铺 column —— JSONB 更适合我们这种"每页字段略有不同"的场景
- ❌ 内容和组件版本不同步就直接上线 —— schema 迁移必须和渲染代码在同一个 PR

---

## 11. 跨团队复用：主产品组件是所有 SEO 页面的公共依赖

当团队里有多个人分别负责不同类型的 SEO 页面（tech layoffs、company internships、free tools、compare、use cases…），**每个页面都需要"引导用户到主产品"的落点 section**。如果每个人各写一遍 Coding Interview / Mock / Copilot 的介绍卡片，就会出现：

- 同一个产品有 N 份视觉不同的介绍卡片
- 主产品改 tagline 要改 N 个文件、追 N 个 owner
- 有人写 "Coding Copilot"、有人写 "Coding Interview Copilot"、有人漏掉新产品

**解法**：主产品对应的 section 只做**一个组件 + 一份数据源**，所有 SEO 页面按需 import + 传当前上下文 props。

### 11.1 谁复用什么

| SEO 页面团队 | 需要的主产品 section | 复用同一个组件 |
|---|---|---|
| Tech Layoffs (`/tech-layoffs/*`) | Comeback toolkit：推 Copilot / Resume / Job Hunter | `<ProductSpotlight context="layoff" />` |
| Company Internships (`/internships/*`) | Interview prep toolkit：推 Coding / Mock / Phone | 同上，`context="internship"` |
| Free Tools (`/tools/*`) | Upgrade path：从工具引流到付费主产品 | 同上，`context="free-tool"` |
| Compare (`/compare/*`) | Our advantage：主产品能力矩阵 | 同上，`context="compare"` |
| Use Cases (`/use-cases/*`) | Products for this scenario | 同上，`context="use-case"` + `scenario` |
| Blog / Guide | Related products footer | 同上，`context="article"` |

现状是每个团队各写了一份（`LayoffProductsBlock` / `LayoffsProducts` / `SoftwareEngineersOtherTools` / `*OtherFeatures` …），职责重叠、维护分散。

### 11.2 目标结构

```text
src/components/shared/product-spotlight/
├── ProductSpotlight.tsx        ← 唯一渲染组件（栅格 / 动画 / 卡片视觉）
├── useProductSpotlight.ts       ← 按 context + scenario 从 DB / 数据源取卡片
└── types.ts                     ← ProductCard 契约

Supabase:
product_cards            ← 主产品清单（id / name / href / image / base_tagline）
product_context_copy     ← (product_id, context, scenario) → 改写后的 description
```

调用方（任意 SEO 页面）只写一行：

```tsx
<ProductSpotlight context="layoff" scenario="amazon-2026" limit={4} />
```

不同页面拿到的是**同一个组件**、同一份视觉，但 description 已经按当前场景改写；主产品团队改 tagline / 新增产品，只在 `product_cards` insert 一行，**所有 SEO 页面下一次渲染立即同步**。

### 11.3 团队协作分工

这一层抽象让分工天然清晰：

| 角色 | 拥有 | 不碰 |
|---|---|---|
| **主产品团队**（Platform） | `ProductSpotlight.tsx` 组件设计 + `product_cards` 主表 | 各 SEO 页面的具体内容 |
| **SEO 页面团队**（Layoffs / Internships / Tools…） | 各自 `context` 的 `product_context_copy` 文案 + 页面骨架 | 卡片视觉、产品清单 |
| **内容 / 运营** | 直接在 DB 里编辑 `product_context_copy` | 代码 |

冲突域从"改同一份 `.tsx`"降到"insert 不同 `(context, scenario)` 行"，几乎不会互相踩脚。

### 11.4 好处（叠加 §10 的收益）

1. **主产品是所有 SEO 页面的单一依赖**：一次升级，全站同步
2. **命名 / 定位 / 视觉零漂移**：不会再出现 "Coding Copilot" vs "Coding Interview Copilot" 两种叫法并存
3. **新增 SEO 页面模板成本降到 0**：新起一类页面（比如 `/salary-negotiation/*`）不需要重造产品卡片
4. **新增主产品自动铺满全站**：主产品团队上新产品 → 补一条 default context copy → 所有 SEO 页面下一次渲染就带上新产品引流
5. **A/B 测试变得可能**：同一个 slot 的 description / 挑选逻辑可以按 context 独立实验，不影响其他团队

### 11.5 落地建议

1. **先统一契约，再统一实现**：把 `LayoffProductsBlock` / `LayoffsProducts` / `SoftwareEngineersOtherTools` / `*OtherFeatures` 的 props 对齐到同一份 `ProductCard` interface（仅 TS 层收敛，不改渲染）
2. **抽出 `ProductSpotlight.tsx`**：先让它接受 `items: ProductCard[]` 直接渲染，5 个老组件改成薄壳传数据
3. **建 Supabase 两张表**：把 5 个老组件里的 hardcode 数据迁进去，`context` 字段按现有页面填
4. **删薄壳**：SEO 页面直接调 `<ProductSpotlight context=... />`
5. **owner 落到 Platform 团队**：`ProductSpotlight` 的视觉变更从此走 Platform PR review，不再散落在各 SEO 页面

### 11.6 反例

- ❌ SEO 页面团队为了"这次样式想调一下"复制一份 `ProductSpotlight` 改名成 `MyProductSpotlight` —— 直接破坏跨团队复用
- ❌ 把主产品 tagline hardcode 在 SEO 页面文案里，而不是从 `product_cards.base_tagline` 读 —— 主产品改名时会漏
- ❌ 每个 SEO 团队自己维护"当前有哪些主产品"的枚举 —— 主产品清单必须只有 Platform 一份

---

## 12. 参考文件

- 共享 block：`src/components/shared/{PageHero,PageBreadcrumb,SectionCTA,SectionFAQ,HowToSection,RelatedFeatures}.tsx`
- Use cases 三个实例：`src/components/{coding-interview,mock-interview,phone-interview}/*UseCases.tsx`
- Other Features 现有实例：`src/components/{coding-interview,mock-interview}/*OtherFeatures.tsx` + `LayoffProductsBlock` / `LayoffsProducts` / `SoftwareEngineersOtherTools`
- 已数据库化的页面：`src/pages/{UseCasePage,CompanyLayoffPage,CompanyInternshipPage,CompareDetail}.tsx`
- 品牌/视觉规则单一来源：根目录 `BRAND_GUIDELINES.md`
- FAQ / CTA 规范：根目录 `FAQ_AND_CTA_GUIDELINES.md`

---

## 13. 未来演进方向

当团队规模扩展到 5+ engineers + 独立内容团队时，这套体系需要从文档升维到工具化：

- **Page Generator**：输入 page type / slug / keywords，自动生成 blueprint + 组件骨架
- **CMS Editor**：让内容团队在不碰代码的前提下编辑卡片文案和内链
- **Internal Link Validator**：CI 中自动检查断链、孤页、弱锚文本

当前阶段以本文档为 single source of truth 即可，上述工具在内容规模进入下一个数量级时启动。

