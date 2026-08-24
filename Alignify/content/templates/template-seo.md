# SEO 页面模板

本文档为 Alignify SEO 类页面的标准模板，用于创建或优化 SEO 指南页面（如 Schema、链接建设、Landing Page、搜索引擎、SERP 等）。

**参考**：content-rules、[section 文档](../section/README.md)、[template-bloglayout](./template-bloglayout.md)、[section-consistency](../section/section-consistency.md)（字数与表达一致性）· **SEO 关键词与 slug 意图**：[alignify-keywords-seo.md](../keywords/alignify-keywords-seo.md)

---

## 〇、一致性规范（必读）

**目标**：同一类型（SEO）页面之间 **H2 格式、信息顺序、语气** 一致；正文篇幅见 [section-consistency §〇–§二](../section/section-consistency.md)。

- **跨页面**：结构、标题格式与表达习惯对齐；**不**强制各章总字数逐页相等
- **章节间**：避免极短与极长章节相邻
- **章节内**：并列块不宜约 3 倍以上长短差

**统一篇幅**：见 [section-consistency](../section/section-consistency.md)（含 §〇 字数层级）；正文以建议区间与自然分段为准；meta/H1/excerpt 仍宜遵守专项文档。

---

## 一、页面结构

```
1. 核心要点（TL;DR，40–80字 intro + 4–5 条 items）← [section-tldr](../section/section-tldr.md)
2. 什么是 XXX（建议篇幅见 section-consistency）← section-what-is
3. XXX 如何工作 / 核心原理
4. ... 正文内容（按主题展开，使用 Section 组件）...
5. How To（可选，如「如何优化面包屑」）← section-how-to
6. Conclusion（总结）← [alignify-conclusion](../alignify-conclusion.md)
7. FAQ（常见问题）← section-faq
8. References（引用，如有）← section-references
```

**标准顺序**：How To → Conclusion → FAQ → References

---

## 二、Metadata 与 BlogLayout 配置

> **字数与文案模板**：Meta title、meta description、H1、excerpt 的统一字数规范、文案模板、按页面类型差异，以 [section-meta-copy](../section/section-meta-copy.md) 为**唯一来源**。本节仅列 SEO 类型特有约束（如不含「指南」、不含年份等），通用规则不在此重复。

**meta 配置详见**：[section-meta-copy](../section/section-meta-copy.md) §一–二（字数、模板、CTA）、[section-seo](../section/section-seo.md)（像素值、截断机制）。

**SEO 特有约束**：
- 中文不含「指南」，英文不含 "Guide"
- 常青内容不含年份
- 主动语态：探索/掌握…比较…立即学习/开始实践

```tsx
export const metadata = {
  title: "[主题]：[核心价值/卖点] | Alignify",
  description: "60-80字/120-158字符，主动语态：探索/掌握XXX，比较核心方法，引导行动（如「立即学习」）",
  publishDate: "2026年X月X日",
  modifiedDate: "2026年X月X日",
};

<BlogLayout
  title="[主题]：副标题"
  excerpt="100-150字，说明页面价值"
  publishDate="2026年X月X日"
  modifiedDate="2026年X月X日"
  readTime="XX 分钟阅读"
  pageUrl="https://alignify.co/zh/seo/[page-slug]"
  heroContent={<div></div>}
/>
```

**H1 与 excerpt 文案构建形式**：须符合 [section-meta-copy](../section/section-meta-copy.md) §三–四 和 [section-heading-best-practices](../section/section-heading-best-practices.md) § 2.3、§ 3.3（跨类型统一）。

### 2.1 中英文页面差异

| 项目 | 中文 | 英文 |
|------|------|------|
| pageUrl | `/zh/seo/[slug]` | `/seo/[slug]` |
| readTime | `XX 分钟阅读` | `XX min read` |
| 日期格式 | `2026年1月15日` | `January 15, 2026` |
| 核心要点标题 | 核心要点 | Key Takeaways |
| Conclusion 标题 | 结论 | Conclusion |
| FAQ 数量 | **7 问** | **7 问** |

---

## 三、正文章节

- **核心要点**：参见 [section-tldr](../section/section-tldr.md)
- **什么是 XXX**：参见 [section-what-is](../section/section-what-is.md)
- **Generic Section（普通段落）**：参见 [section-generic](../section/section-generic.md)、[section-content-import](../section/section-content-import.md)
- **How To**：参见 [section-how-to](../section/section-how-to.md)（SEO 可含内链）
- **Conclusion**：参见 [alignify-conclusion](../alignify-conclusion.md)
- **FAQ**：参见 [section-faq](../section/section-faq.md)
- **References**：参见 [section-references](../section/section-references.md)

---

## 四、SEO 页面特点

- **无 HowItWorks**：技术说明用 Section 编写，标题如「XXX 如何工作」
- **无 BestTools / UseCases**：多为纯文字指南
- **可含 References**：引用 Google、Schema.org 等权威来源
- **可含如何选择 section**：如「如何优化 URL」→ 正文 `## 如何选择…` + H3 步骤
- **内链**：可自然融入内链到其他 SEO 页面；**专册**（Hub/Spoke、§1.5 分布、跨频道节制）见 [seo-articles-internal-links.md](../internal-links/seo-articles-internal-links.md)

---

## 五、SEO 各章节特有规则

以下规则为 **SEO 页面专有**，与 section 通用规范配合使用。

### 5.1 核心要点（Tldr）

- **统一使用 Tldr 组件**：参见 [section-tldr](../section/section-tldr.md) § 4.3 SEO 页面
- **introduction**：40–80 字，含 [主题]、[核心要点]、[目标]；直答式
- **items**：4–5 条，每条 25–40 字，同组长度相近
- **内容方向**：概念+作用、类型/格式、扩展类型、实施要点

### 5.2 How To（如何实施/如何选择）

- **可包含**：内链到相关 SEO 页面（如适用）
- **标题示例**：如何优化面包屑、如何实施 GEO 策略

### 5.3 正文章节

- **主要使用 Section 组件**：纯文字章节用 [section-generic](../section/section-generic.md)
- **HowItWorks 不适用**：技术说明用 Section，标题如「XXX 如何工作」

---

## 六、导入清单

**必需**：

```tsx
import BlogLayout from "@/components/BlogLayout";
import Tldr from "@/components/Tldr";
import FAQ from "@/components/FAQ";
import Section from "@/components/Section";
```

**按需**：

```tsx
<!-- 如何选择：正文 section，见 section-how-to.md；HowToChoose 组件已删除 -->
import References from "@/components/References";  // 有引用时
import YouTubeThumbnail from "@/components/YouTubeThumbnail";  // 有视频时
import { addUtmToExternalLink, getExternalLinkRel } from "@/lib/utils";  // 有外链时
import Link from "next/link";  // 有内链时
```

---

## 七、page.tsx 要求

```tsx
export const metadata: Metadata = LearnSEO.metadata;

export default function LearnSEOPage() {
  return <LearnSEO />;
}
```

- **直接返回 MDX 组件**：不需要额外布局包装
- **metadata 导出**：从 MDX 的 metadata 导出

---

## 八、示例页面

- LearnSEO、SchemaGuide、URLOptimization、InternalLinks、LandingPage、SearchEngine 等

---

## 九、页面专用组件

| 页面 | 组件 | 说明 |
|------|------|------|
| **SearchEngine** | StatCounterEmbed | 嵌入 StatCounter 搜索引擎市场份额图表 |
| 其他 | 按需 | YouTubeThumbnail、Section、Table 等，参见 [section](../section/README.md) |
