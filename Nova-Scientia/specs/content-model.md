# Nova Scientia — 数据模型速查

本文档提供所有内容文件的数据结构参考。产品/公司为 JSON（snake_case）；主题为 Markdown frontmatter + 正文块。

## 一、ApiProduct（产品）

文件位置：`content/products/{slug}.json`
TypeScript 类型：`src/lib/content/product-adapter.ts` → `ApiProduct`

### 顶层字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `slug` | `string` | 是 | 唯一标识，与文件名一致 |
| `name` | `string` | 是 | 产品名称 |
| `seo_title` | `string \| null` | 否 | 自定义 SEO 标题；null 时自动生成 |
| `seo_description` | `string \| null` | 否 | 自定义 SEO 描述 |
| `canonical_url` | `string \| null` | 否 | 自定义 canonical URL |
| `og_image` | `string \| null` | 否 | 自定义 OG 图片 URL |
| `content` | `object` | 是 | 见下方 content 字段 |

### content 字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `hero` | `object` | 是 | 见下方 hero 子字段 |
| `toc` | `array` | 是 | 目录项：`{ id: string, label: string }[]` |
| `about` | `object` | 是 | `{ title: string, paragraphs: string[] }` |
| `features` | `object` | 是 | `{ title: string, items: { title: string, desc: string }[] }` |
| `pros` | `string[]` | 是 | 优点列表 |
| `cons` | `string[]` | 是 | 缺点列表 |
| `pricing` | `object` | 是 | `{ title, note?, plans: { plan, monthly, credits?, features? }[] }` |
| `useCases` | `object` | 是 | `{ title, cases: { title, desc }[], audiences: { title, desc }[] }` |
| `alternatives` | `array` | 是 | `{ name: string, desc: string, slug?: string }[]` |
| `conclusion` | `object` | 是 | `{ title, text, cta_url, cta_text, items?: { label, text }[] }` |
| `faqs` | `array` | 是 | `{ q: string, a: string }[]` |
| `breadcrumbs` | `array` | 是 | `{ name: string, url: string }[]` |
| `lastUpdated` | `string` | 是 | 最后更新日期 |
| `news` | `array` | 否 | `{ title, summary, date, url?, source? }[]` |
| `schema` | `object` | 否 | 自定义 schema 覆盖 |

### hero 子字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `h1` | `string` | 是 | 页面 H1 标题 |
| `tags` | `string[]` | 是 | 标签列表（如 `["Geracao de Imagem", "Design"]`） |
| `stats` | `array` | 是 | `{ value: string, label: string }[]` — 评分、用户数等 |
| `cta_url` | `string` | 是 | CTA 按钮链接 |
| `cta_text` | `string` | 是 | CTA 按钮文案 |
| `description` | `string` | 是 | 产品简述 |
| `screenshot_url` | `string` | 否 | 产品截图 URL |

---

## 二、ApiTopic（主题）

文件位置：`content/topics/{slug}.md`（Markdown + YAML frontmatter）
解析器：部署仓 `src/lib/content/topic-md.ts` → 输出 `ApiTopic`
TypeScript 类型：`src/types/topics.ts` → `ApiTopic`

> 历史格式 `content/topics/{slug}.json` 已全部迁移为 MD。JSON 仅作解析器遗留回退，勿再新建。

### 文件结构

```markdown
---
slug: "llm"
name: "LLM (Large Language Models)"
seo_title: "..."
seo_description: "..."
canonical_url: null
og_image: null
updated: "2026-06-20"
readingMinutes: "5 min read"
author: "Kostja"
h1: "..."
description: "..."
tldr: {"title":"...","points":[...],"summary":"..."}
comparisonTable: {...}
featuredProducts: {...}
faqs: [{"q":"...","a":"..."}]
recommendedTopics: [{"name":"...","slug":"..."}]
---

<!-- block:section -->
## Introdução {#intro}
段落内容...

<!-- block:section -->
## 章节标题 {#anchor}
...
```

Frontmatter 值：字符串直接写；`null` 写 `null`；对象/数组写单行 JSON。

正文块：`<!-- block:section -->` 开启区块；`## Title {#id}` 定义标题与锚点；段落以空行分隔；可选 `<!-- highlights:start/end -->`、`<!-- childrenHtml:start/end -->`。

### 顶层字段（frontmatter）

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `slug` | `string` | 是 | 唯一标识，与文件名一致 |
| `name` | `string` | 是 | 导航栏显示名称 |
| `seo_title` | `string \| null` | 否 | 自定义 SEO 标题 |
| `seo_description` | `string \| null` | 否 | 自定义 SEO 描述 |
| `canonical_url` | `string \| null` | 否 | 自定义 canonical URL |
| `og_image` | `string \| null` | 否 | 自定义 OG 图片 |
| `updated` | `string` | 否 | 最后更新日期（如 `2026-06-20`） |
| `readingMinutes` | `string` | 否 | 阅读时长文案 |
| `author` | `string` | 否 | 作者名 |
| `h1` | `string` | 是 | 页面 H1 标题 |
| `description` | `string` | 是 | 页面描述 |
| `tldr` | `object` | 否 | `{ title, summary, points: string[] }` |
| `comparisonTable` | `object` | 否 | `{ title?, headers, rows: { cells: string[] }[] }` |
| `featuredProducts` | `object` | 否 | `{ title, items: TopicFeaturedProduct[] }` |
| `faqs` | `array` | 是 | `{ q: string, a: string }[]` |
| `recommendedTopics` | `array` | 否 | `{ name: string, slug: string }[]` |

解析后映射为 `TopicContent`：`intro` 来自第一个 section；`sections[]` 来自后续 section 块。

### TopicSection 子字段（解析后）

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `id` | `string` | 是 | 锚点 id（`## Title {#id}` 或 intro 固定为 `intro`） |
| `title` | `string` | 是 | 章节标题（H2） |
| `paragraphs` | `string[]` | 是 | 段落内容（支持内联 HTML） |
| `highlights` | `string[]` | 否 | 高亮要点（`highlights` 围栏） |
| `childrenHtml` | `string` | 否 | 嵌套 HTML 块（`childrenHtml` 围栏） |
| `productCards` | `TopicProductCard[]` | 否 | 内嵌产品卡片（JSON 时代遗留；MD 中少用） |

### TopicFeaturedProduct 子字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `name` | `string` | 是 | 产品名称（可含副标题，如 `"Nome: Destaque"`） |
| `slug` | `string` | 否 | 产品 slug（有则链站内 `/products/{slug}`） |
| `description` | `string` | 是 | 产品描述 |
| `image` | `string` | 否 | 产品图片 URL |

---

## 三、ApiCompany（公司/投资机构）

文件位置：`content/companies/{slug}.json`
TypeScript 类型：`src/types/companies.ts` → `ApiCompany`

### 顶层字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `slug` | `string` | 是 | 唯一标识 |
| `name` | `string` | 是 | 公司名称 |
| `seo_title` | `string \| null` | 否 | 自定义 SEO 标题 |
| `seo_description` | `string \| null` | 否 | 自定义 SEO 描述 |
| `canonical_url` | `string \| null` | 否 | 自定义 canonical URL |
| `og_image` | `string \| null` | 否 | 自定义 OG 图片 |
| `content` | `object` | 是 | 见下方 |
| `indexed_products` | `CompanyIndexedProduct[]` | 是 | 在 Nova Scientia 有页面的产品：`{ slug, name }[]` |

### content 字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `type` | `"investor" \| "company"` | 否 | 公司类型；决定页面渲染变体 |
| `tags` | `string[]` | 是 | 标签列表 |
| `website` | `string` | 是 | 公司官网 URL |
| `logo_url` | `string` | 是 | Logo 图片 URL |
| `description` | `string` | 是 | 公司描述 |
| `founded` | `string` | 否 | 成立年份 |
| `headquarters` | `string` | 否 | 总部所在地 |
| `known_products` | `CompanyKnownProduct[]` | 是 | `{ name, description, category, url?, icon? }[]` |
| `news` | `CompanyNewsItem[]` | 是 | `{ title, summary, date, url?, source? }[]` |
| `faq` | `CompanyFAQItem[]` | 是 | `{ question, answer }[]` |

### VC 专属字段（type === "investor" 时）：

| 字段 | 类型 | 说明 |
|------|------|------|
| `investment_focus` | `string` | 投资聚焦领域 |
| `investment_terms` | `string` | 投资条款/阶段 |
| `advisors` | `CompanyAdvisor[]` | `{ name, title, url? }[]` |
| `portfolio_batches` | `PortfolioBatch[]` | 每批含 `name` + `companies: PortfolioCompany[]`（`{ name, description?, url?, indexed_slug? }`）|
| `perks` | `CompanyPerk[]` | `{ provider, amount, description?, url? }[]` |

---

## 四、GlossaryData（词汇表）

文件位置：`content/glossary.json`
TypeScript 类型：`src/types/glossary.ts` → `GlossaryData`

| 字段 | 类型 | 说明 |
|------|------|------|
| `heroTitle` | `string` | Hero 区标题 |
| `heroDescription` | `string` | Hero 区描述 |
| `introTitle` | `string` | 词汇表介绍标题 |
| `introBody` | `string` | 词汇表介绍正文 |
| `lastUpdated` | `string` | 最后更新日期 |
| `termCount` | `number` | 术语总数（由脚本计算） |
| `categories` | `GlossaryCategory[]` | 分类列表 |

### GlossaryCategory

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | `string` | 分类 ID |
| `title` | `string` | 分类标题 |
| `terms` | `GlossaryTerm[]` | 术语列表 |

### GlossaryTerm

| 字段 | 类型 | 说明 |
|------|------|------|
| `term` | `string` | 术语名称 |
| `definition` | `string` | 术语定义 |
| `relatedHref` | `string` | （可选）关联页面链接 |
| `relatedLabel` | `string` | （可选）关联链接文案 |
