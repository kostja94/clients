# Nova Scientia — 数据模型速查

本文档提供所有内容 JSON 的数据结构参考。字段名与 API 输出保持一致（snake_case）。

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

文件位置：`content/topics/{slug}.json`
TypeScript 类型：`src/types/topics.ts` → `ApiTopic`

### 顶层字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `slug` | `string` | 是 | 唯一标识 |
| `name` | `string` | 是 | 导航栏显示名称 |
| `seo_title` | `string \| null` | 否 | 自定义 SEO 标题 |
| `seo_description` | `string \| null` | 否 | 自定义 SEO 描述 |
| `canonical_url` | `string \| null` | 否 | 自定义 canonical URL |
| `og_image` | `string \| null` | 否 | 自定义 OG 图片 |
| `content` | `TopicContent` | 是 | 见下方 |

### TopicContent 字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `badge` | `string` | 否 | Hero 区的标签文案 |
| `navLabel` | `string` | 否 | 导航栏短标题；未设则从 h1 截断 |
| `h1` | `string` | 是 | 页面 H1 标题 |
| `description` | `string` | 是 | 页面描述 |
| `tldr` | `object` | 否 | `{ title, summary, points: string[] }` — 核心要点 |
| `stats` | `array` | 否 | `{ value: string, label: string }[]` |
| `intro` | `object` | 是 | `{ title: string, paragraphs: string[] }` |
| `sections` | `TopicSection[]` | 是 | 主要章节列表 |
| `comparisonTable` | `object` | 否 | `{ title?, headers: string[], rows: { cells: string[] }[] }` |
| `featuredProducts` | `object` | 否 | `{ title, items: TopicFeaturedProduct[] }` |
| `faqs` | `array` | 是 | `{ q: string, a: string }[]` |
| `recommendedTopics` | `array` | 否 | `{ name: string, slug: string }[]` |

### TopicSection 子字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `id` | `string` | 是 | 锚点 id（用于 TOC 链接） |
| `title` | `string` | 是 | 章节标题（H2） |
| `paragraphs` | `string[]` | 是 | 段落内容（支持内联 HTML） |
| `highlights` | `string[]` | 否 | 高亮要点 |
| `productCards` | `TopicProductCard[]` | 否 | 内嵌产品卡片：`{ name, subtitle, image?, cta_url?, cta_text?, description }[]` |

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
