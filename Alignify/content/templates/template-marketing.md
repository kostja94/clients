# Marketing 页面模板

本文档为 Alignify Marketing 类页面的标准模板，用于创建或优化营销策略指南、方法论指南（如关键词调研、竞品调研、联盟营销、红人营销、GEO、外链建设等）。

**参考**：content-rules、[section 文档](../section/README.md)、[section-content-import](../section/section-content-import.md)、[template-tools](./template-tools.md)、[template-bloglayout](./template-bloglayout.md)、[section-consistency](../section/section-consistency.md)（字数与表达一致性）

**内容格式（2026-08）**：`content/marketing/{locale}/{slug}.md` + 集中 JSON（TL;DR/FAQ/References）。正文用 `<!-- block:section -->` / `Section.tsx`；如何选择 = 正文 H2 + H3 步骤（**无** HowToChoose 组件）。

**首篇落地**：关键词调研（`content/marketing/zh/keyword-research.md`）

---

## 〇、一致性规范（必读）

**目标**：同一类型（Marketing）页面之间 **H2 格式、方法论结构、语气** 一致；正文篇幅见 [section-consistency §〇–§二](../section/section-consistency.md#〇字数层级硬底线-vs-建议必读)。

- **跨页面**：结构、标题格式与表达习惯对齐；**不**强制各章总字数逐页相等
- **章节间**：避免极短与极长章节相邻
- **章节内**：并列块不宜约 3 倍以上长短差

**统一篇幅**：见 [section-consistency](../section/section-consistency.md) + 下文「Marketing 页面字数速查」。

**EN/ZH 结构同步（必读）**：创建或优化任一语言版本的页面后，**必须**同步另一语言版本的块结构（类型和顺序一致）。不允许 EN 和 ZH 出现不同的 block type 序列。内容语言不同，但 JSON 结构须一一对应。

**语言硬约束**：EN md 文件中所有面向用户的文本（H2、H3、段落）**必须**是英文。FAQ 在 `faq-data.json`。**7 问**。

---

## 一、页面结构

```
1. 核心要点（TL;DR，40–80字 intro + 4–5 条 items）← [section-tldr](../section/section-tldr.md)
2. 什么是 XXX（建议篇幅见 section-consistency）← section-what-is
3. 核心方法论 / 步骤 / 框架（按主题展开，可含表格、列表）
4. 如何实施（How To）← 正文 section，[section-how-to](../sections/section-how-to.md)
5. 结论 ← [alignify-conclusion](../alignify-conclusion.md)
6. FAQ ← section-faq
7. References（可选）← section-references
```

**标准顺序**：Conclusion 必须在 FAQ 之前。FAQ 禁止内链、禁止手动 H2（FAQ 组件自动渲染 H2）。

**硬底线章节（所有 Marketing 页面必含）**：以下五类章节为所有 Marketing 页面必须包含，不可省略：
- 核心要点（Tldr）
- 什么是 XXX（What Is）
- 如何实施（正文 `## 如何实施…` + 3–5 个 H3 步骤）
- 结论（Conclusion）
- FAQ（**7 问**，`faq-data.json`）

例外：`marketing-types` 等 Hub 索引页可不含如何选择/如何实施 section。

**Marketing 页面三种结构模式**：不同主题的 Marketing 页面正文结构不同，可分为三类：

| 类型 | 代表页面 | 正文特征 |
|------|----------|----------|
| **A 类 — 策略框架型** | affiliate、keyword-research、competitive-analysis、pricing-strategy | 方法论驱动，章节以步骤/框架/分析维度为主 |
| **B 类 — 平台战术型** | reddit、x-formerly-twitter、geo、email-marketing | 围绕特定平台展开，含平台机制解析 + 操作指南 |
| **C 类 — 项目运营型** | creator-program、influencer、referral-program、lifetime-deal、localization-strategy | 以「如何搭建/运营一个项目」为主线，含激励机制、招募、平台分析 |

创建新页面时，先判断类型再确定正文 H2 结构。首尾章节（TL;DR、What Is、如何实施 section、Conclusion、FAQ）跨类型一致。

**与 Tools 的差异**：Marketing 无 BestTools、UseCases、对比表格等产品展示；正文以方法论、步骤、框架为主，可含工具参考表（加 UTM 外链）。

**Marketing 页面字数速查**：

| 章节 | 中文 | 英文 | 导向 |
|------|------|------|------|
| **meta title** | 25-32 字 | 50-60 字符 | SEO |
| **meta description** | 60-80 字 | 120-158 字符 | SEO |
| **H1 (title)** | 14-22 字 | 40-60 字符 | 用户可读性 |
| **excerpt** | 100-150 字 | 200-250 字符 | 用户可读性 |
| 核心要点 intro | 40–80 字 | 40–70 词 | GEO |
| 核心要点 items | 4–5 条，每条 25–40 字，同组长度相近 | 4–5 条，每条 18–28 词，同组长度相近 | GEO |
| 什么是 | 约 **180–380 字** | 约 **150–280 词** | 与 section-what-is 一致 |
| How To 每步骤 | 约 **60–140 字** | 约 **50–120 词** | 步骤间不宜悬殊 |
| 结论 | 见 [alignify-conclusion.md §2.3](../alignify-conclusion.md) | 见 [alignify-conclusion.md §2.3](../alignify-conclusion.md) | - |
| FAQ 答案 | 约 **60–120 字** | 约 **40–80 词** | - |

---

## 二、Metadata 与 Frontmatter

> Meta title/description → `marketing-meta.ts`；H1/excerpt → md frontmatter `title`/`description`。

### 2.2 SEO 导向（meta title、meta description）

**详见**：[section-meta-copy](../section/section-meta-copy.md) §一–二（字数、模板、CTA）、[section-seo](../section/section-seo.md)（像素值、截断机制）。

**Marketing 特有约束**：
- 中文不含「指南」，英文不含 "Guide"
- 常青内容不含年份
- 主动语态：探索/掌握…比较…立即学习/开始实践

### 2.3 用户可读性导向（H1、excerpt）

**完整规范**：见 [section-meta-copy](../section/section-meta-copy.md) §三–四（字数、三段式结构）、[section-heading-best-practices](../section/section-heading-best-practices.md)（H1-H6 层级与可访问性）。H1 与 excerpt 的**文案构建形式**须符合跨类型统一格式（`[策略]：[价值]`；excerpt 三段式首句→中段→收尾）。

### 2.4 heroContent 两种形式

**形式 A：无工具卡片**（适用于无对应 /tools 页面的策略）

```tsx
heroContent={<div></div>}
```

**形式 B：工具推荐卡片**（适用于有对应 /tools 页面时）

```tsx
heroContent={
  <div className="bg-card/95 backdrop-blur-sm border border-border rounded-lg p-6 shadow-sm">
    <div className="flex flex-col items-center justify-center space-y-4 w-full">
      <h3 className="text-lg font-semibold text-foreground text-center mb-2">
        [策略名称]工具推荐
      </h3>
      <p className="text-sm md:text-base text-muted-foreground text-center max-w-3xl mb-4 px-4">
        [简短描述]
      </p>
      <div className="w-full max-w-md">
        <img src="/[路径]/[图片].jpg" alt="[描述]" className="w-full rounded-lg shadow-lg" loading="lazy" />
      </div>
      <div className="text-center mt-4">
        <Link href="/zh/tools/[tool-slug]" className="inline-flex items-center gap-2 text-primary hover:text-primary/80 font-medium text-sm">
          查看X款最佳[策略名称]工具 →
        </Link>
      </div>
    </div>
  </div>
}
```

### 2.5 中英文页面差异

| 项目 | 中文 | 英文 |
|------|------|------|
| pageUrl | `/zh/marketing/[slug]` | `/marketing/[slug]` |
| readTime | `XX 分钟阅读` | `XX min read` |
| 日期格式 | `2026年1月15日` | `January 15, 2026` |
| Introduction 标题 | 文章简介 | Introduction |
| Conclusion 标题 | 结论 | Conclusion |
| FAQ 数量 | **7 问** | **7 问** |

---

## 三、内容导入方式（专用组件 + Generic Section）

**要求**：正文章节使用**专用组件**或 **Generic Section**（Section 组件），禁止裸 `<div>` + `<h2>` + `<p>` 混用。详见 [section-content-import](../section/section-content-import.md)。

| 章节 | 导入方式 | 组件/用法 | 规范文档 |
|------|----------|-----------|----------|
| 核心要点 | Tldr 组件 | Tldr + introduction + items | [section-tldr](../section/section-tldr.md) |
| 什么是 XXX | Generic Section | Section + paragraphs | [section-what-is](../section/section-what-is.md) |
| 方法论/步骤 | Generic Section | Section + subSections、children | [section-generic](../section/section-generic.md) |
| 如何实施 | 正文 section | `## 如何实施…` + H3 | [section-how-to](../sections/section-how-to.md) |
| 结论 | Generic Section | Section + paragraphs | [alignify-conclusion](../alignify-conclusion.md) |
| FAQ | 专用组件 | FAQ | [section-faq](../section/section-faq.md) |
| References | 专用组件 | References | [section-references](../section/section-references.md) |

**Generic Section** = Section 组件用于普通段落（标题+段落），支持 paragraphs、subSections、children。详见 [section-generic](../section/section-generic.md)。

**H2 章节间距**：Marketing 正文 H2 章节之间**不使用** Section 的 `showDivider`，统一由容器 `space-y-12` 控制间距，保持简洁视觉节奏。

---

## 四、Marketing 各章节特有规则

### 4.1 核心要点（Tldr）

- **统一使用 Tldr 组件**：参见 [section-tldr](../section/section-tldr.md) § 4.2 Marketing 页面
- **introduction**：40–80 字，含 [策略名称]、[方法关键词]、[受众]；直答式
- **items**：4–5 条，每条 25–40 字，同组长度相近
- **内容方向**：核心价值+数据、完整方法论、工具+案例、适用受众

### 4.2 什么是 XXX

- **结构**：常见 **2–4 段**；首段定义+价值+适用人群；后续段可写边界与分流；内链按 [section-what-is](../section/section-what-is.md)
- **篇幅**：见 [section-consistency §二](../section/section-consistency.md#二通用字数与篇幅建议区间)
- **内链**：与主题有强功能/工作流关联

### 4.3 正文章节（方法论、步骤、框架）

- **结构**：按主题分 H2/H3，每节聚焦一个子问题
- **可含**：表格、列表、工具参考表
- **外链**：使用 `addUtmToExternalLink()` 添加 UTM
- **内容分块**：每块可独立回答一个子查询，利于 AI 提取与 Featured Snippets

### 4.4 How To（如何实施）

- **禁止**：链接、具体产品名、工具名、平台名
- **使用通用表述**：如「趋势类工具」「问题汇总工具」「关键词挖掘工具」
- **步骤数**：3–5 步（按主题复杂度，见 [section-how-to](../section/section-how-to.md) Part 2）
- **每步骤**：动词开头 + 分叉短语；内容优先，字数仅质检参考（建议约 **60–140 字**，见 [section-how-to](../section/section-how-to.md) Part 3）

### 4.5 结论

- **禁止**：内链、外链、产品名
- **篇幅**：见 [alignify-conclusion](../alignify-conclusion.md)

### 4.6 FAQ

- **数量**：**7 问**（`faq-data.json`）
- **禁止**：内链、手动 H2
- **答案**：见 [section-faq](../section/section-faq.md) 与 [section-consistency §二](../section/section-consistency.md#二通用字数与篇幅建议区间)

### 4.7 References

- **可选**：置于 FAQ 之后
- **适用**：有引用来源的页面（Affiliate、GEO、InfluencerMarketing 等）

---

## 五、内容最佳实践（参考 SEO / AI 搜索）

| 实践 | 说明 |
|------|------|
| **意图映射** | 先诊断搜索意图：informational vs transactional；内容与意图匹配 |
| **E-E-A-T** | 展示 Expertise、Experience、Authoritativeness、Trust；数据和引用可增强可信度 |
| **内容分块** | 每 H2 为独立可回答块；短段落、列表、表格；便于 AI 提取与 Featured Snippets |
| **TOC** | 长文可加目录（Table of Contents） |
| **关键词布局** | 自然融入，避免堆砌；Title、H1、intro、H2 含核心词 |
| **Topic Cluster** | 方法论类可考虑 Hub & Spoke：主文 + 衍生专题 |
| **内链** | 相关策略内链（工作流/场景关联） |
| **更新** | 定期更新 modifiedDate 与内容 |

---

## 六、导入清单

**常用**：

```tsx
import BlogLayout from "@/components/BlogLayout";
import Tldr from "@/components/Tldr";
import FAQ from "@/components/FAQ";
<!-- 如何实施：正文 section，见 section-how-to.md -->
import Section from "@/components/Section";
import Link from "next/link";
import { addUtmToExternalLink, getExternalLinkRel } from "@/lib/utils";
```

**按需**：

```tsx
import References from "@/components/References";  // 有引用时
import YouTubeVideo from "@/components/YouTubeVideo";  // 有视频时
```

---

## 七、标准 H2 标题格式与示例

| 章节 | H2 标题格式 | 示例 |
|------|-------------|------|
| 核心要点 | 核心要点（Tldr 组件 title） | 固定 |
| 介绍 | 什么是 [策略名称] | 什么是关键词调研 |
| 方法论 | [主题] 的 [方法] 步骤 / [主题] 框架 | 关键词调研与 Topical Map 的四步法 |
| 实施 | 如何实施 [策略名称] | 如何实施关键词调研 |
| 结论 | 结论 | 固定 |
| FAQ | 常见问题 | 固定 |

---

## 八、page.tsx 要求

```tsx
export const metadata: Metadata = KeywordResearch.metadata;

export default function KeywordResearchPage() {
  return <KeywordResearch />;
}
```

---

## 九、质量检查清单

- [ ] **H1 与 excerpt**：符合 [section-heading-best-practices](../section/section-heading-best-practices.md)
- [ ] 章节完整（核心要点、What Is、正文方法论、如何实施 section、Conclusion、FAQ）
- [ ] 正文使用 `<!-- block:section -->` / `Section.tsx`
- [ ] 如何实施 3–5 个 H3 步骤（见 [section-how-to](../sections/section-how-to.md)）
- [ ] How To 步骤中禁止链接、产品名、工具名
- [ ] Conclusion 在 FAQ 之前
- [ ] FAQ 数量为 **7 问**
- [ ] FAQ 无内链
- [ ] EN md 所有用户面文本为英文
- [ ] EN 与 ZH section 顺序与锚点一致

---

## 十、关键词调研页面示例（首篇落地）

**结构**：

1. 核心要点（Tldr，含「关键词调研」关键词）
2. 什么是关键词调研
3. 关键词调研与 Topical Map 的四步法
4. 如何寻找增量信息
5. 关键词扩展参考（功能词、多语言、有人搜）
6. 如何实施关键词调研（正文 section）
7. 结论
8. FAQ（**7 问**）

**工具参考表**：在正文中可含表格，外链加 UTM。

---

## 十一、常见错误与日期更新

### 11.1 常见错误

- ❌ BlogLayout 缺失
- ❌ heroContent 内放 H1
- ❌ 正文使用 HTML 裸块（`"type": "html"`）→ 必须用 Section 组件
- ❌ Section 块带 `showDivider: true`
- ❌ 结论位置错误（必须在 FAQ 之前）
- ❌ FAQ 重复 H2
- ❌ 如何实施步骤数 < 3
- ❌ 如何实施步骤中含产品名、链接
- ❌ 外链未加 UTM
- ❌ EN 文件出现中文标题或段落
- ❌ EN 与 ZH 的 block type 序列不一致
- ❌ EN 文件有中文 H2 但 H1 是英文（半翻译状态）

### 11.2 日期更新规则

**创建**：publishDate 与 modifiedDate 使用当前日期；publishDate 永不更改。

**更新**：modifiedDate 更新为本次更新日期；