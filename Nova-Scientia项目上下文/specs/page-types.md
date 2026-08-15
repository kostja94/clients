# Nova Scientia — 页面类型定义

本文档定义 Nova Scientia 所有页面类型的**结构模板、必需区块、渲染组件**。新增页面时必须选择对应类型，按模板填写内容。

## 页面类型总览

| 类型 | URL 模式 | 数据源 | 核心组件 |
|------|----------|--------|----------|
| **A — 产品详情** | `/products/{slug}` | `content/products/{slug}.json` | `ProductLayout` > `ProductHeroSection`, `ProductFeaturesSection`... |
| **B — 主题指南** | `/{slug}` | `content/topics/{slug}.json` | `TopicPage` > `TopicHero`, `TopicTldr`, `TopicEditorialSection`... |
| **C — 公司档案** | `/company/{slug}` | `content/companies/{slug}.json` | `CompanyLayout` > `CompanyHero`, `CompanyPortfolio`... |
| **D — 词汇表** | `/glossary` | `content/glossary.json` | `GlossaryPageContent` |
| **E — 分类中心** | `/{segment}` | `category-hub.ts` 路由 | `ProductCategoryHubPage` |

---

## 类型 A：产品详情页 (`/products/{slug}`)

### 数据结构

JSON schema 见 `src/lib/content/product-adapter.ts` 中的 `ApiProduct` 接口。通过 `apiProductToDisplayData()` 映射为 `ProductDisplayData`。

### 区块顺序（DOM 渲染顺序）

| 序号 | 区块 | 组件 | 说明 |
|------|------|------|------|
| 1 | Breadcrumb | `BreadcrumbNav` | Início > Produtos > {产品名} |
| 2 | Hero | `ProductHeroSection` | h1, tags, description, stats, CTA 按钮, screenshot |
| 3 | TOC | `ProductTableOfContents` | 水平索引，锚点链接到各区块 id |
| 4 | About | `ProductAboutSection` | "O que é" — 产品介绍 |
| 5 | Features | `ProductFeaturesSection` | 功能列表（title + desc） |
| 6 | Pros/Cons | `ProductProsConsSection` | 优点 + 缺点两栏 |
| 7 | Pricing | `ProductPricingSection` | 套餐表格（plan/monthly/credits/features） |
| 8 | Use Cases | `ProductUseCasesSection` | 用例 + 目标受众 |
| 9 | Alternatives | `ProductAlternativesSection` | 竞品对比表格 |
| 10 | Conclusion | `ProductConclusionSection` | 总结 + CTA + 可选 items 列表 |
| 11 | News | `ProductNewsSection` | （可选）近期新闻 |
| 12 | Related Products | `ProductRelatedSection` | （可选）相关产品链接 |
| 13 | FAQ | `ProductFAQSection` | Accordion 式问答（内部用 `FaqSection`），使用 `FAQPage` schema |

### TOC 映射

API 中的 toc id 通过 `API_TOC_ID_MAP` 映射到页面 section id：

| API toc.id | 页面 section id |
|------------|----------------|
| `o-que-e` | `o-que-e` |
| `funcionalidades` | `recursos` |
| `pros-e-contras` | `pros-contras` |
| `precos` | `precos` |
| `casos-de-uso` | `casos-de-uso` |
| `alternativas` | `alternativas` |
| `conclusao` | `conclusao` |
| `faq` | `faq` |
| `noticias` | `noticias` |

### Schema 生成

- `SoftwareApplication` schema：基于产品属性（名称、描述、评分、价格等）
- `FAQPage` schema：基于 `content.faqs[]`
- `ItemList` schema：基于 alternatives 或 features

---

## 类型 B：主题指南页 (`/{slug}`)

### 数据结构

JSON schema 见 `src/types/topics.ts` 中的 `ApiTopic` 接口。字段通过 `TopicContent` 定义。

### 区块顺序

| 序号 | 区块 | 组件 | 说明 |
|------|------|------|------|
| 1 | Breadcrumb | `BreadcrumbNav` | Início > Temas > {主题名} |
| 2 | Hero | `TopicHero` | h1, badge, description, stats |
| 3 | TL;DR | `TopicTldr` | 直答式摘要 + 要点列表（3-5 条） |
| 4 | TOC | `TopicTableOfContents` | 自动从 sections + featuredProducts + comparisonTable + faq 生成 |
| 5 | Intro | `TopicHowToTabs` | （如有 tabs 数据）标签式介绍 |
| 6 | Intro Section | `TopicEditorialSection` | `content.intro` — 开篇章节 |
| 7 | Sections | `TopicEditorialSection` | `content.sections[]` — 主要章节，每节含 paragraphs + highlights + productCards |
| 8 | Featured Products | `TopicFeaturedProducts` | 精选产品卡片（仅链站内 `/products/{slug}`） |
| 9 | Comparison Table | `TopicComparisonTable` | 对比表格（headers + rows） |
| 10 | FAQ | `TopicFaq` | 问答列表 |
| 11 | Related Bar | `TopicRecommendedBar` | 推荐主题 + 工具分类链接 |

### TOC 生成逻辑

`buildTocItems()` 在 `TopicPage.tsx` 中按以下规则生成：
1. Intro section → `{ id: "intro", label: intro.title }`
2. 每个 content section → `{ id: section.id, label: section.title }`
3. 如有 featured products → `{ id: "destaques", label: featuredProducts.title }`
4. 如有 comparison table → `{ id: "comparacao", label: comparisonTable.title }`
5. 如有 FAQ → `{ id: "faq", label: "Perguntas Frequentes" }`

### Schema 生成

`TopicJsonLd` 组件生成：
- `FAQPage` schema（基于 `content.faqs[]`）
- `HowTo` schema（基于 sections 中的步骤内容，如有）

### 路由守卫

`/[slug]` 是动态路由，必须检查 `RESERVED_SLUGS` 防止与静态路由冲突。保留的 slug 包括：`about`、`products`、`topic`、`company`、`glossary`、`image`、`video`、`voice`、`3d`、`design`、`coding`、`productivity`。匹配时调用 `notFound()`。

---

## 类型 C：公司档案页 (`/company/{slug}`)

### 数据结构

JSON schema 见 `src/types/companies.ts` 中的 `ApiCompany` 接口。

### 两种变体

由 `content.type` 字段决定：

**`"company"` — 标准公司**：
| 区块 | 说明 |
|------|------|
| Hero | logo, name, description, website, founded, headquarters |
| Known Products | `content.known_products[]` — 产品卡片 |
| News | `content.news[]` — 新闻列表 |
| FAQ | `content.faq[]` — 问答 |

**`"investor"` — VC/投资机构**（额外区块）：
| 区块 | 说明 |
|------|------|
| Investment Focus | `content.investment_focus` |
| Investment Terms | `content.investment_terms` |
| Portfolio | `content.portfolio_batches[]` — 按批次展示被投公司 |
| Advisors | `content.advisors[]` — 顾问/合伙人 |
| Perks | `content.perks[]` — 被投公司福利 |

### 产品关联

- `content.known_products[]`：手动关联的已知产品（可含外链）
- `indexed_products[]`：在 Nova Scientia 有页面的产品（slug 匹配，自动生成站内链接）

---

## 类型 D：词汇表页 (`/glossary`)

### 数据结构

单一 `content/glossary.json`，schema 见 `src/types/glossary.ts` 中的 `GlossaryData`。

### 结构

- 14 个分类，147 个术语
- 每个术语含 `term`、`definition`、可选的 `relatedHref` 和 `relatedLabel`
- 分类间使用互斥手风琴（一次展开一个分类）
- 支持 URL hash 定位到具体术语（`/glossary#term-id`）

---

## 类型 E：分类中心页 (`/{segment}`)

### 路由映射

`SHORT_HUB_SEGMENT_TO_CATEGORY`（`src/lib/content/category-hub.ts`）：

| 短路径 | 产品分类 |
|--------|----------|
| `/image` | `image-generation` |
| `/video` | `video-generation` |
| `/voice` | `audio-generation` |
| `/3d` | `3d` |
| `/design` | `design-tools` |
| `/coding` | `code-generation` |
| `/productivity` | `productivity` |

### 结构

- 展示该分类下的产品列表
- 按评分/名称排序
- 含分类描述和子类别导航
