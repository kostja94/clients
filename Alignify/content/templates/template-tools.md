# Tools 页面模板

本文档为 Alignify Tools 类页面的标准模板，用于创建或优化工具推荐、产品对比、排名列举类页面（如 AI 图片工具、AI 视频工具、招聘工具等）。

**参考**：content-rules、[section 文档](../section/README.md)、[template-bloglayout](./template-bloglayout.md)、[section-consistency](../section/section-consistency.md)（字数与表达一致性）

---

## 〇、一致性规范（必读）

**目标**：同一类型（Tools）页面之间 **H2 格式、信息顺序、语气** 一致；正文篇幅以 **自然、说清** 为先，字数用 **建议区间** 质检（见 [section-consistency §〇](../section/section-consistency.md#〇字数层级硬底线-vs-建议必读)）。

- **跨页面**：与同类型已有页面对比结构、标题格式与表达习惯；**不**强制各章总字数逐页对齐
- **章节间**：避免极短与极长章节相邻；节奏可读
- **章节内**：并列块（场景、步骤、FAQ）**不宜**出现约 3 倍以上长短差；产品描述以讲清差异为准

**篇幅建议**：见 [section-consistency](../section/section-consistency.md) + 下文「Tools 页面字数速查」。

---

## 一、页面结构

```
1. 核心要点（TL;DR）← `tldr-data.json`，[section-tldr](../sections/section-tldr.md)
2. 什么是 XXX 工具 ← md `<!-- block:section -->`
3. XXX 技术如何工作 ← md section
4. 各类型工具详细介绍 ← md section + 产品 H3（[section-best-tools](../sections/section-best-tools.md)）
5. 工具对比表格（可选）← html block 或 section 内 table
6. 应用场景 ← md section + H3
7. 如何选择 ← md section + H3 步骤（[section-how-to](../sections/section-how-to.md)，**无** HowToChoose 组件）
8. 结论 ← md section
9. FAQ ← `faq-data.json`（**7 问**）
10. References ← `references-data.json`
```

**标准顺序**：Conclusion 必须在 FAQ 之前。FAQ 答案 **plain text，无内链**。

**不推荐**：以下 section 对选工具决策价值有限，易与 How to Choose 重复，不建议作为独立章节：
- Workflow（工作流程）
- Cost Analysis（成本分析）
- Getting Started（入门指南）
- Future Trends（未来趋势）

**Tools 页面字数速查**（**C 层建议**，meta/H1/excerpt 为 **B 层** 仍宜遵守窄区间）：

| 章节 | 中文 | 英文 | 导向 |
|------|------|------|------|
| **meta title** | 25-32 字 | 50-60 字符 | SEO |
| **meta description** | 60-80 字 | 120-158 字符 | SEO |
| **H1 (title)** | 14-22 字 | 40-60 字符 | 用户可读性；**不写年份**（见 §2.1.2） |
| **excerpt** | 100-150 字 | 200-250 字符 | 用户可读性 |
| 核心要点 intro | 40–80 字 | 40–70 词 | GEO |
| 核心要点 items | 4–5 条；每条宜扫读可收，**不必**条条等长 | 同上 | GEO |
| 什么是 | 约 **180–380 字**，常见 **2–4 段** | 约 **150–280 词** | 自然分段 |
| 如何工作 technologyBase | 约 **220–420 字** | 约 **140–280 词** | 原理讲清即可 |
| 如何工作 architectureDifferences | 约 **120–280 字** | 约 **90–200 词** | |
| 产品描述 | 硬底线 100–400 字，建议 180–260 字 | 硬底线 280–800 字符，建议 350–650 字符 | 差异优先；同页 max/min < 3x |
| FAQ 答案 | 约 **60–120 字** | 约 **40–80 词** | 首句直答 |
| 结论 | 见 [alignify-conclusion.md §2.3](../alignify-conclusion.md) | 见 [alignify-conclusion.md §2.3](../alignify-conclusion.md) | |

---

## 二、Metadata 与 Frontmatter

**单篇 Tools 长文**依赖：① `src/data/blog-meta.ts`（或 `tools-meta.ts`）的 **meta**；② `content/{blog|tools}/{zh,en}/{slug}.md` frontmatter 的 **`title`（H1）** 与 **`description`（excerpt）**。

> **字数与文案模板**：Meta title、meta description、H1、excerpt 的统一字数规范、文案模板、按页面类型差异，以 [section-meta-copy](../section/section-meta-copy.md) 为**唯一来源**。本节仅列出 **Tools 页面特有的硬约束**（如「最佳」/ `Best`、年份格式、冒号副线等），通用规则（字数区间、CTA 要求、OG/Twitter 三处同文等）不在此重复。

### 2.0 四要素速查：Tools 类型硬约束

| 要素 | Tools 特有约束 | 通用规则 |
|------|---------------|----------|
| **Meta title** | **必须含「最佳」/ `Best`**；中文 `（2026）` + `：` + 副线；英文 `(2026)` + `:` + 副线；**禁止** `（2026）\| Alignify` 无副线直连 | [section-meta-copy §一](../section/section-meta-copy.md#一meta-title) |
| **Meta description** | 列举 2–3 个代表产品；须由 TL;DR 与 Best 榜单支撑 | [section-meta-copy §二](../section/section-meta-copy.md#二meta-description) |
| **H1** | **不写年份**；推荐「类型：核心价值」格式；不强制含「最佳」 | [section-meta-copy §三](../section/section-meta-copy.md#三h1页面主标题) |
| **Excerpt** | 三段式；避免通用结尾 | [section-meta-copy §四](../section/section-meta-copy.md#四excerpthero-摘要) |

**工具中心首页**（`/zh/tools`、`/tools`）仅有 `page.tsx` 的 **meta**，无 `blogLayout` H1/ excerpt（页面结构为索引列表）。

**站内核检**（不替代人工通读）：

- `audit:tools-meta`：仅 **meta title** 硬规则（「最佳」/ `Best`、年份后冒号、禁止 `（2026）\|` 无副线）。脚本位于上下文仓 `scripts/ops/audit-tools-meta-titles.mjs`。
- `audit:tools-page-fields`：在上述基础上增加 **meta description 过短/过长**、**H1 / excerpt 长度** 与 **可解析性** 报表。脚本位于上下文仓 `scripts/ops/audit-tools-page-fields.mjs`。

部署仓 `package.json` 暂无对应 npm scripts。运行方式：`node ../../clients/Alignify/scripts/ops/{script}.mjs`（路径按实际调整）。

**Description 在代码中的单引号**：英文产品名如 `There's` 若写在 **双引号** 字符串内，**禁止**用错误正则去解析 `[^"']` 截断；合并与工具脚本以 **仅双引号** 的字段为准。

### 2.1 Meta 注册方式（blog-meta.ts / tools-meta.ts）

**架构说明**（2026-05-20 迁移后）：不存在每 slug 一个 `page.tsx`。路由使用单个动态路由文件，Meta 由 `generateMetadata()` 从 `BLOG_META[slug]`（或 `TOOLS_META[slug]`）读取。

```ts
// src/data/blog-meta.ts（新文章）或 src/data/tools-meta.ts（旧文章）
export const BLOG_META: Record<string, BlogPageMeta> = {
  "{slug}": {
    en: {
      title: "Best [Tool Type] (2026): [Subtitle] | Alignify",
      description: "Explore the best [tool type] in 2026: [Product A], [Product B], and more…",
      publishDate: "2026-06-23",
      modifiedDate: "2026-06-23",
    },
    zh: {
      title: "最佳[工具类型]（2026）：[副线] | Alignify",
      description: "探索2026年最佳[工具类型]：[产品A]、[产品B]等…",
      publishDate: "2026-06-23",
      modifiedDate: "2026-06-23",
    },
  },
};
```

**新文章默认走 `/blog/` 路由**，注册到 `blog-meta.ts` + `blog-pages-config.ts`。旧 `/tools/` 文章保持不变。详见 [`skills/create-tools-article/SKILL.md`](../../skills/create-tools-article/SKILL.md)。

### 2.1.1 SEO 导向（meta title、meta description）

**用途**：搜索结果展示、爬虫、点击率。面向搜索引擎与 SERP。

> **字数与模板**：以 [section-meta-copy](../section/section-meta-copy.md) §一–二为准。以下仅标注 Tools 特有约束。

**详见**：[section-seo](../section/section-seo.md)（像素值、截断机制）、[section-meta-copy](../section/section-meta-copy.md)（文案规范）。

**Next.js `metadata` 与社交预览**：`generateMetadata()` 自动从 `BLOG_META[slug]`（或 `TOOLS_META[slug]`）读取并输出到 `<meta>`、OG、Twitter 标签——**无需手写在 page.tsx 中**。Meta 的唯一维护位置为 `blog-meta.ts`（或 `tools-meta.ts`）。

#### 2.1.1.0 Meta 硬约束（与 JSON 内 H1 分离）

以下规则针对 `blog-meta.ts`（或 `tools-meta.ts`）中注册的 meta 字段——**不替代** JSON 里的 `blogLayout.title`（H1 仍按 §2.1.2）。

| 项目 | 中文（`/zh/tools/...`） | 英文（`/tools/...`） |
|------|-------------------------|----------------------|
| **Title 关键词** | **必须含「最佳」**，且尽量出现在**主题词前**（如 `最佳AI图片工具（2026）：…`、`最佳 LinkedIn AI 工具盘点（2026）：…`）。**工具中心** `/zh/tools`：`最佳AI工具分类索引（2026）：…` | **必须含 `Best`**（习惯上为 `Best … (2026): …`；索引页 `Best AI Tools Hub (2026): …`） |
| **年份 + 副线** | 使用全角 `（2026）`，之后**必须**有 **全角冒号 `：`** 与 **2–4 个短标签**（顿号、逗号连接均可），再视需要接 ` \| Alignify`。**禁止** `（2026）\| Alignify` 或 `（2026） \| Alignify` 这类**无副线**直连。 | 使用半角 `(2026)`，后接半角 `:` 与英文副线，再接 ` \| Alignify`（若保留品牌后缀）。**禁止** `(2026)\| Alignify` 无副线直连。 |
| **Description** | 目标 **60–80 字**（过短影响 SERP 点击率）。首句可用「探索/对比/厘清＋2026 年最佳…」点题；**列举 2–3 个**正文代表产品/场景即可，勿堆砌；**末句 CTA** 如「立即探索」「立即探索站内完整指南，免费阅读。」 | 目标 **120–158 字符**；`Discover` / `Compare` 点题＋2–3 个代表名＋一句 CTA（`Explore.` / `Free guide.` 等与 sitewide 英文语气一致） |
| **唯一性** | 全站各 slug 的 meta title、meta description 须**彼此不同**，勿复用同一句只改一个词。 | 同上 |
| **质检** | 合并前运行 `npm run audit:tools-meta`（见 `scripts/ops/audit-tools-meta-titles.mjs`）：校验 **「最佳」**、**年份后必有冒号副线**（含 `| Alignify` 时）、英文 **Best**。 | 同上 |

**与「盘点/索引」类 copy 的关系**：若 H1 为「LinkedIn AI 工具**盘点**」等叙事型标题，meta title 仍须在语义最前加 **「最佳」**，以与全站工具 SEO 词根一致；H1 与 meta 允许微差（H1 可更长、可含「选型」等），但主题与意图须同一。

**内容与文案一致性（Tools）**：
- **完整句与标点**：`description` 须为完整英文句（或规范中文），**禁止**因字数上限被截成半词（如 `Cura`、`Curate`、`Fre`、`gu`）。若超长，应改写缩短而非硬截断。
- **语气模板**：英文 meta description 宜统一为「Discover… Compare… + CTA（Curated. Free guide. / Step-by-step guide. Free. / Explore.）」一类节奏，避免一句缺句号、缺连词（如 `scaling Curated` 应改为 `scaling. Curated.`）。
- **与正文**：`blogLayout.excerpt` 应能由 TL;DR / 首段支撑，避免 meta 写 A 类产品而 H1/excerpt 只谈 B 类；产品名以正文 `bestTools` 为准时，meta 仅列 2–3 个代表即可。

### 2.1.2 用户可读性导向（H1、excerpt）

**用途**：页面可见内容，面向进入页面的用户。兼顾可读性与首屏信息架构。

> **字数与模板**：以 [section-meta-copy](../section/section-meta-copy.md) §三–四为准。以下仅标注 Tools 特有约束。

**导入方式**：使用硬编码字面量（`title="..."`、`excerpt="..."`），避免引用 pageConfig 导致构建失败。

**内容原则**：
- **H1**：格式「[工具类型]：核心价值/卖点」，含关键词；以用户可读性为首要考量。**H1 不写年份**；新鲜度用 **meta title** 中的 `(2026)` 以及 **publishDate / modifiedDate** 表达。
- **excerpt**：聚焦工具价值、适用场景、用户收益；**避免通用结尾**。

**文案构建形式**：H1 与 excerpt 的句式、结构须符合 [section-heading-best-practices](../section/section-heading-best-practices.md) § 2.3、§ 3.3（跨类型统一）和 [section-meta-copy](../section/section-meta-copy.md) §三–四。

```tsx
<BlogLayout
  title="[工具类型]：核心价值描述"
  excerpt="[100-150 字 / 200-250 字符的摘要]"
  heroContent={<div></div>}
  publishDate={pageConfig.meta.publishDate}
  modifiedDate={pageConfig.meta.modifiedDate}
  readTime={pageConfig.content.readTime}
  pageUrl="https://alignify.co/zh/tools/[page-slug]"
/>
```

### 2.1.3 H1 与 Excerpt 生成示例（供 AI 生成新页面参考）

**完整规范**：见 [section-heading-best-practices](../section/section-heading-best-practices.md) § 2.3（H1 文案构建形式）、§ 3.3（Excerpt 文案构建形式）。以下为 Tools 类型示例。

**H1 示例**：AI变声器：改变声音，创造无限可能 | AI Voice Changers: Transform Your Voice Experience

**Excerpt 示例（合规）**：
- **中文**：`让音乐创作变得人人可及。AI音乐生成工具能根据文字描述或风格偏好自动创作旋律，从背景音乐到主题曲，让每个人都能成为音乐创作者。`
- **英文**：`Unlock infinite potential in voices and create unique audio experiences. AI voice changer tools provide real-time voice transformation, effect layering, and personalization, suitable for entertainment, education, and professional recording.`

**避免**：excerpt 结尾使用「这将显著提升…」「这将帮助你更好地理解…」「这些方法帮助您…」等通用句；H1 含「Guide」「指南」、年份。

### 2.2 中英文页面差异

| 项目 | 中文 | 英文 |
|------|------|------|
| pageUrl | `/zh/tools/[slug]` | `/tools/[slug]` |
| readTime | `X 分钟阅读`（数字后有空格） | `X min read` |
| 日期格式 | `2026年1月15日` | `January 15, 2026` |
| 日期/readTime 导入 | `{pageConfig.meta.publishDate}` 等 | 与 pageConfig 同步，见 [section-hero](../section/section-hero.md) §5.1 |
| 产品描述 | 约 220 字 | 400-600 字符 |
| FAQ 数量 | **7 问** | **7 问** |

---

## 三、专用组件与 Section 规范

| 章节 | 组件 | 规范文档 |
|------|------|----------|
| 核心要点 | Tldr 组件 | [section-tldr](../section/section-tldr.md) |
| 什么是 XXX | Section 或 div | [section-what-is](../section/section-what-is.md) |
| 技术概述 | HowItWorks | [section-how-it-works](../section/section-how-it-works.md) |
| 产品展示 | BestTools | [section-best-tools](../section/section-best-tools.md) |
| 对比表格 | Table | [section-comparison-table](../section/section-comparison-table.md) |
| 应用场景 | UseCases | [section-use-cases](../section/section-use-cases.md) |
| 如何选择 | 正文 section | [section-how-to](../sections/section-how-to.md) |
| 结论 | Section 或 div | [alignify-conclusion](../alignify-conclusion.md) |
| FAQ | FAQ | [section-faq](../section/section-faq.md) |

---

## 四、Tools 页面特点

- **必须使用 BlogLayout**：中文页面必须有 Hero 区域
- **垂直大图布局**：产品展示图片在上、文字在下
- **禁止 Grid 左右布局**：遵守产品展示大图像布局标准
- **图片路径**：`/tools/[page-name]/[image].jpg`，文件必须存在于 `public/tools/`
- **按钮文案**：`试试 [产品名称]`（中文）或 `Try [产品名称]`（英文）

---

## 五、Tools 各章节特有规则

以下规则为 **Tools 页面专有**，与 section 通用规范配合使用。

### 5.0 「什么是」与「如何工作」章节优化

**篇幅（建议）与内容分工**：全文数字区间见 [section-consistency](../section/section-consistency.md) 与上文「Tools 页面字数速查」。

| 章节 | 中文（建议） | 英文（建议） | 内容聚焦 | 避免 |
|------|-------------|-------------|----------|------|
| 什么是 | 约 **180–380 字**，常见 **2–4 段** | 约 **130–320 词** | 定义、价值、适用人群、边界/分流、内链（按 section-what-is） | 技术细节堆在首章 |
| 如何工作 technologyBase | 约 **220–420 字** | 约 **140–280 词** | 技术原理、建模方式、生成流程 | 与「什么是」重复卖点 |
| 如何工作 architectureDifferences | 约 **120–280 字** | 约 **90–200 词** | 架构类型与技术差异 | 列举具体产品名 |

**质检**：以「是否说清、是否重复、单段是否过长」为主；**不**为贴旧数字删必要限定。字符统计：去 HTML、合并空格；中文按字，英文可按词看可读长度。若有自动化字数校验，英文按**完整句子**截断，禁止 mid-word 截断。

**英文内容原则**：与中文**信息深度**相当，意译优先。

**内链相关性**：内链目标必须与当前主题有强功能/工作流关联。✅ 音乐生成 → 视频编辑、MV 生成；❌ 音乐生成 → 文字转语音、声音克隆（虽同属音频但功能边界不同）。详见 [section-what-is](../section/section-what-is.md#34-内链相关性原则)、[section-links](../section/section-links.md#13-内链相关性原则)。

**Tools 内链拓扑、邻居矩阵、产品外链验证**：见 [alignify-internal-links.md](../alignify-internal-links.md)（附录 B、附录 C 与 §五）。

**文案描述**：首段定义+价值+适用人群；含内链段落按 [section-what-is 四](../section/section-what-is.md#四文案描述原则) 自然融入。

**生成时检查清单**（创建或翻译 Tools 页面时逐项核对）：

- [ ] 什么是：段数与内链符合 [section-what-is](../section/section-what-is.md)；篇幅落在 [section-consistency §二](../section/section-consistency.md#二通用字数与篇幅建议区间) 建议区间或能说明理由
- [ ] 如何工作 technologyBase / architectureDifferences：篇幅建议见 §二；advantages **3–5** 项，每项 name + description
- [ ] 内链目标与主题有强功能/工作流关联（参见 3.4）
- [ ] **均衡分布**：在 TLDR / 如何工作 / 场景 / 如何选择 / 对比 intro / 结论等区块中安排**多个不同** Tools 内链（全文每个 href 仍只出现一次）；细则见 [alignify-internal-links.md §3.1.5](../alignify-internal-links.md#135-tools-内链均衡分布阅读体验优先--锚文本规范--跨板块预留)
- [ ] 英文意译、与中文深度相当，禁止 mid-word 截断

**示例（音乐生成）**：见 [alignify-internal-links.md §附录 A](../alignify-internal-links.md#附录-a什么是--第二段内链示例音乐生成)。

### 5.1 How To（如何选择）

- **完整规范（唯一真相源）**：见 [section-how-to](../section/section-how-to.md)——含定位分工、步骤数量 3–5、去模板黑名单、决策分叉写法、组件与 Schema、验收审计。
- **可包含**：具体工具推荐和选择建议
- **标题示例**：如何选择 AI 图片工具、如何选择最适合的 XXX

### 5.2 应用场景（Use Cases）

**场景数量**（按工具类型）：

| 工具类型 | 场景数量 |
|----------|----------|
| 图片工具 | 4-5 个 |
| 视频工具 | 5-6 个 |
| 音频工具 | 4-5 个 |
| 文本工具 | 4-5 个 |
| 浏览器/搜索工具 | 5-6 个 |
| 编程工具 | 4-5 个 |
| 设计工具 | 4-5 个 |
| 生产力工具 | 4-5 个 |
| 其他专业工具 | 3-6 个 |

### 5.3 产品展示（Best Tools）

- **组件**：必须使用 BestTools 组件，禁止原始 HTML
- **图片路径**：`/tools/[page-name]/[image].jpg`，必须存在于 `public/tools/`
- **篇幅**：shortDescription 硬底线 EN 10–50 字符 / ZH 4–25 字，建议 EN 15–35 字符 / ZH 6–18 字；描述硬底线 EN 280–800 字符 / ZH 100–400 字，建议 EN 350–650 字符 / ZH 180–260 字；同页 max/min < 3x
- **内容质量**：每款描述需包含核心定位 + 关键差异 + 最佳适用场景；禁止空洞副词和万能结尾
- **迁移**：若仍用旧 HTML 格式，优先迁移到 BestTools 组件
- **完整规范**：参见 [section-best-tools](../section/section-best-tools.md)

### 5.4 对比表格

- **推荐使用**：Table
- **列结构**：标准 4 列（工具名称、核心特点、主要应用场景、定价模式），可选第 5 列（扩展列须语义明确）
- **内容规范**：bestFor 必填；pricing 必填（无则「待定」）；coreFeatures 2–4 个关键词，顿号分隔
- **文案规范**：H2 为「[工具类型]工具对比」（可加「选择最适合你的」）；intro 为「以下是主流[工具类型]工具的对比，帮助您快速了解各工具的特点、应用场景和适用性：」
- **详细规范**：参见 [section-comparison-table](../section/section-comparison-table.md)

---

## 六、导入清单

**常用**：

```tsx
import BlogLayout from "@/components/BlogLayout";
import Tldr from "@/components/Tldr";
import FAQ from "@/components/FAQ";
import HowItWorks from "@/components/HowItWorks";
import BestTools from "@/components/BestTools";
import UseCases from "@/components/UseCases";
<!-- 如何选择：正文 section -->
import Table from "@/components/Table";
import Link from "next/link";
import { addUtmToExternalLink, getExternalLinkRel } from "@/lib/utils";
```

---

## 七、标准 H2 标题格式与示例

| 章节 | H2 标题格式 | 示例 |
|------|-------------|------|
| 核心要点 | 核心要点 | 固定 |
| 介绍 | 什么是 [工具类型] | 什么是 AI 变声器 |
| 技术 | [工具类型] 是如何工作的 | 变声器是如何工作的 |
| 产品分类 | 2026 年最好的 [工具分类] | 2026 年最好的实时变声器 |
| 对比 | [工具类型] 工具对比：选择最适合你的 | 变声器工具对比：选择最适合你的 |
| 场景 | [工具类型] 都能做什么：[数量] 大实用场景 | 变声器都能做什么：8 大实用场景 |
| 选择 | 如何选择 [AI] [工具类型] | 如何选择 AI 变声器 |
| 结论 | 结论 | 固定 |
| FAQ | 常见问题 | 固定 |

**产品 H3 格式**：`[序号]. [产品名]：[核心优势]`，如 `1. Dubbing AI：游戏直播声音转换`。

---

## 八、优秀参考页面

| 页面 | 学习要点 |
|------|----------|
| **website-builder** | 唯一 meta 完全合规（title 31字、desc 74字）、2-3 个产品名 + 等 |
| **image-generator** | 9 个产品、垂直大图、YouTube 优先、5 个应用场景 |
| **headshot-generator** | 4 个产品、6 个应用场景、FAQ 80-100 字符 |
| **virtual-staging** | 垂直大图、Table、响应式 |
| **voice-changer** | 完整结构示例、多分类产品 |

---

## 九、优化流程

1. **合规检查**：运行英文内容验证脚本（上下文仓 `scripts/ops/check-tools-en-content.mjs`）验证 EN 页面「什么是」「如何工作」字数与结构；禁止 mid-word 截断
2. **状态检查**：获取当前日期，完整阅读文件，记录待优化项
3. **按顺序优化**：H1/excerpt → H2 → Best 榜单 section → 产品描述 → 应用场景 → 如何选择 section → 结论 → FAQ → 表格 → 日期
4. **日期规则**：内容修改需更新 `modifiedDate`；仅格式迁移不更新
5. **验证**：运行检查脚本、对照质量检查清单
6. **批量优化**：完成当前批次的全部编辑后再运行 `npm run build` 验证；不要中途插入构建检查
7. **容差原则**：字数 approximate 即可，±10% 可接受；英文禁止过度精简导致信息缺失，需与中文内容深度相当

---

## 十、硬约束汇总（不可协商）

以下规则为 Tools 页面的**硬底线**（A 层），违反将导致构建错误、SEO 降级或用户体验问题。B/C 层建议见各章节。

| # | 约束 | 后果 | 来源 |
|---|------|------|------|
| 1 | Meta title 必须含「最佳」/ `Best`，年份格式 `（2026）：` / `(2026):` 后接副线 | SEO 点击率下降 | §2.1.1 |
| 2 | H1 不写年份 | 与 meta title 冗余、降低可读性 | §2.1.2 |
| 3 | FAQ 数量 **7 问**（中英文各 7 问，与线上一致） | 非 7 问视为未对齐 | section-faq |
| 4 | FAQ 禁止内链（MDX），Tools JSON FAQ 内链按 §3.2 试点规则 | Schema/渲染冲突 | section-faq §3 |
| 5 | Conclusion 必须在 FAQ 之前 | 页面结构错误 | §一 |
| 6 | BestTools 描述硬底线：ZH 100–400 字 / EN 280–800 字符；同页 max/min < 3x | 内容质量不达标 | §5.3 |
| 7 | comparisonSection：bestFor/pricing 不得为空，coreFeatures 2–4 个关键词，items ≥ 2 条 | 对比表格不可用 | section-comparison-table §三 |
| 8 | page.tsx 中 metadata、OG、Twitter 标题/描述必须完全相同 | 社交预览漂移 | §2.1.1 |
| 9 | 必须使用 BlogLayout + 垂直大图布局，禁止 Grid 左右 | 设计一致性破坏 | §四 |
| 10 | 所有图片必须存在于 `public/tools/[slug]/` | 图片 404 | §四 |

---

## 十一、质量检查清单

- [ ] **H1 与 excerpt**：符合 [section-heading-best-practices](../section/section-heading-best-practices.md)；使用硬编码字面量防止构建失败
- [ ] 章节完整（核心要点、介绍、技术、产品、对比、场景、选择、结论、FAQ）
- [ ] 字数符合 section 规范（±10% 容差可接受；英文内容验证脚本位于上下文仓 `scripts/ops/check-tools-en-content.mjs`）
- [ ] 内链目标与主题有强功能/工作流关联（参见 5.0）
- [ ] Meta 符合 [section-seo](../section/section-seo.md)（中文 desc 60-80 字）
- [ ] Tools 四要素（§2.0、§2.1.1 / §2.1.2）：`npm run audit:tools-meta` 与 `npm run audit:tools-page-fields` 在默认模式下无 **error**（`--strict` 可按 CI 需约束 warning）
- [ ] 垂直大图布局、禁止 Grid 左右
- [ ] 组件正确导入、图片存在于 `public/tools/`
- [ ] Conclusion 在 FAQ 之前
- [ ] FAQ 数量为 **7 问**（中英文各 7 问）
- [ ] FAQ 内链符合专册 §1.5（Tools/Blog JSON：≤3 distinct slug，与正文去重；MDX FAQ 仍禁链）
- [ ] BlogLayout 与 page.tsx 符合 [template-bloglayout](./template-bloglayout.md)

### 图片存在性检查

- [ ] 所有图片实际存在于 `/public/tools/[page-name]/`
- [ ] 文件名与代码引用完全一致（含扩展名）
- [ ] 路径格式：`/tools/[page-name]/[image].jpg` 或 `.png`

### 表格内容检查

- [ ] 对比表格列数与同类型页面一致（4 列或 5 列）
- [ ] bestFor、pricing 无空值
- [ ] H2、intro 文案符合 [section-comparison-table](../section/section-comparison-table.md) 规范

---

## 十二、Meta 注册与架构说明

**Meta 注册方式**（2026-05-20 迁移后）：

```ts
// src/data/blog-meta.ts — 新文章（/blog/ 路由）
// src/data/tools-meta.ts — 旧文章（/tools/ 路由，保持不变）
export const BLOG_META: Record<string, BlogPageMeta> = {
  "{slug}": {
    en: { title: "...", description: "...", publishDate: "...", modifiedDate: "..." },
    zh: { title: "...", description: "...", publishDate: "...", modifiedDate: "..." },
  },
};
```

路由使用单个动态路由文件（`app/[locale]/blog/[slug]/page.tsx`），`generateMetadata()` 自动读取 Meta。**无需创建新的 page.tsx 文件**。正文由 `getPageData("blog"|"tools", slug, locale)` 加载 JSON。

### BestTools 迁移

若页面仍使用旧 HTML 格式，优先迁移到 BestTools 组件。参见 [section-best-tools](../section/section-best-tools.md)。

---

## 十三、常见错误与日期更新

### 13.1 常见错误预防

- ❌ BlogLayout 缺失
- ❌ 标题语法错误（如「如何变声器工作」→ ✅「变声器如何工作」）
- ❌ 结论位置错误（必须在 FAQ 之前）
- ❌ FAQ 重复 H2（不在 FAQ 组件前手动添加 H2）
- ❌ 日期遗漏（**例外**：格式迁移不更新）
- ❌ 组件导入缺失、图片文件不存在于 `public/tools/`

### 13.2 日期更新规则

**创建**：publishDate 与 modifiedDate 使用当前日期；**创建后 publishDate 永不更改**。

**更新**：modifiedDate 更新为本次更新日期；**例外**：格式迁移不更新日期。

---

## 十四、翻译为英文

### 14.0 中英流程（必读）

- **先中文**：新增页面时仅创建中文版，不提前创建英文
- **后英文**：中文创建完毕之后，一次性批量优化英文页面
- **非逐句对应**：英文页面不与中文完全一致；Tools 页可针对具体工具做**本地化优化**（如示例、定价、地区适用性、目标市场差异等）

### 14.1 核心翻译原则

- **意译**：理解中文含义后用自然英文表达，勿逐字翻译
- **字数**：按各章节绝对字符数执行（见 14.3 表）
- **结构**：保持相同章节数量和顺序

### 14.2 标题和文案

- **H2**：50-80 字符；描述性短语（What Are...、How...、Best...）；避免直译
- **H3**：使用 generator/editor/enhancer 等专业术语，避免 "XXX Tools"
- **CTA**：`Try [产品名称]`，勿用 "Visit XXX Website"

### 14.3 内容精简（从中文翻译时）

| 项目 | 英文（建议） |
|------|-------------|
| H1 (title) | 40-60 字符 |
| excerpt | 200-250 字符 |
| 什么是 | 约 **130–320 词**；段数自然 |
| 如何工作 technologyBase | 约 **140–280 词** |
| 如何工作 architectureDifferences | 约 **90–200 词** |
| 产品描述 | 硬底线 280–800 字符，建议 350–650 字符 |
| FAQ 答案 | 约 **40–80 词** |
| 应用场景 | 约 **100–260 词/场景** |
| 结论 | 见 [alignify-conclusion.md §2.3](../alignify-conclusion.md) |

**注意**：英文与中文**深度**相当即可，不必字符数机械对齐。

**英文 HowItWorks 示例**（篇幅随主题调整，以下为示意）：

```tsx
<HowItWorks
  id="how-xxx-work"
  title="How [Tool Type] Work"
  technologyBase="Modern [tool type] uses [core tech]. [Method A] and [Method B] enable [outcome]. Compared to traditional approaches, AI-based tools offer [key benefits]."
  advantages={[
    { name: "[Advantage 1]", description: "[20-50 chars]" },
    { name: "[Advantage 2]", description: "[20-50 chars]" },
    { name: "[Advantage 3]", description: "[20-50 chars]" },
  ]}
  architectureDifferences="Different tools use different architectures. [Type A] optimizes for [case]; [Type B] focuses on [case]. Choice depends on [criteria]."
  locale="en"
/>
```

### 14.4 英文页面 UI 差异

- **颜色方案**：`data-locale="en"`（深色背景、浅色文字）
- **H2 分割线**：英文仅 `pt-8`，无分割线
- **Hero**：左对齐；更新日期显示 "Updated on [日期]"
- 参见 [section-hero](../section/section-hero.md)、[section-nav](../section/section-nav.md)
