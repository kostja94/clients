# Nova Scientia — 网站总规范

本文档定义 Nova Scientia 全站的**内容规则、SEO 规则、视觉规则、命名规则**。所有页面类型（产品、主题、公司、词汇表、分类中心）均以此为基准。编码时若偏离本文档，必须同步更新。

**适用人员**：内容编辑、开发者、AI 助手。修改本文档需注明日期和原因。

**Last updated**: 2026-08-29

---

## 一、语言与地区

| 项目 | 设定 |
|------|------|
| 默认语言 | pt-BR（巴西葡萄牙语），URL **无前缀** |
| 其他语言 | `pt-pt`、`es-mx`、`es-es`、`en` — URL 带 `/{locale}/` 前缀 |
| HTML lang | 按 locale 动态设置（如 `pt-BR`、`es-MX`、`en-US`） |
| Schema inLanguage | 与当前页面 locale 一致 |
| 主目标市场 | 巴西（pt-BR 内容最完整） |
| OpenGraph locale | 按 locale 映射（见 `src/lib/i18n.ts`） |

**规则**：
- **pt-BR 内容**（`content/products/`、`content/topics/`、`content/companies/`）均为葡萄牙语；URL slug 使用 kebab-case，不翻译 slug 本身。
- **多语言架构已上线**：路由与数据层支持 5 个 locale；翻译内容放 `content/locales/{locale}/`。未翻译页面在对应语言下 **404**，不回落 pt-BR 原文。
- **UI 文案**（导航/按钮/页脚）尚未国际化，仍为 pt-BR 硬编码。

详见 [i18n-route-plan.md](i18n-route-plan.md)、[i18n-content-workflow.md](i18n-content-workflow.md)。

## 二、URL 规范

### 2.1 页面路由

| 页面类型 | URL 模式 | 示例 |
|----------|----------|------|
| 首页 | `/` | `/` |
| 产品列表 | `/products` | `/products` |
| 产品详情 | `/products/{slug}` | `/products/chatgpt` |
| 主题列表 | `/topic` | `/topic` |
| 主题详情 | `/{slug}` | `/inteligencia-artificial-no-brasil` |
| 公司列表 | `/company` | `/company` |
| 公司详情 | `/company/{slug}` | `/company/a16z` |
| 词汇表 | `/glossary` | `/glossary` |
| 分类中心 | `/{segment}` | `/image`、`/video`、`/design` |
| 关于 | `/about` | `/about` |

### 2.2 重定向规则

旧路径通过 `next.config.js` 中的 301 重定向指向新 URL：

- `/tools/{segment}` → `/{segment}`（旧 Tools 路径）
- `/products/categoria/{category}` → `/{segment}`（旧分类路径）
- `/{path}/` → `/{path}`（去除尾部斜杠）

详见 `next.config.js` 中的 `legacyPathRedirects` 和 `productRootRedirects`。

### 2.3 Canonical URL

所有页面必须通过 `generateMetadata()` 设置 canonical URL：
- 产品页：优先使用 `canonical_url` 字段（JSON），fallback 为 `https://novascientia.com.br/products/{slug}`
- 主题页：优先使用 `canonical_url` 字段，fallback 为 `https://novascientia.com.br/{slug}`
- 公司页：同上模式
- 静态页：使用 `export const metadata` 固定值

### 2.4 Slug 命名规则

详见 **[slug-breadcrumb.md](slug-breadcrumb.md)**。核心约束：
- Slug 必须与 JSON 文件名一致
- 禁止使用 ISO 639-1 两字母语言代码作为 slug（如 `en`、`pt`、`ai`）
- 禁止与站点路径冲突的词（`home`、`admin`、`login`、`categoria`、`search` 等）
- 产品 slug 优先使用品牌名的 kebab-case 形式

## 三、内容规则

### 3.1 内容来源

| 页面类型 | 文件 | 格式 |
|----------|------|------|
| 产品页 | `content/products/{slug}.json` | JSON |
| 主题页 | `content/topics/{slug}.md` | Markdown + YAML frontmatter |
| 公司页 | `content/companies/{slug}.json` | JSON |
| 词汇表 | `content/glossary.json` | JSON（由 merge 脚本生成） |
| 多语言覆盖 | `content/locales/{locale}/...` | 与源类型相同（topics 为 MD） |

编辑后直接 git 提交。构建时 `src/lib/content/*.ts` 读取本地文件（主题经 `topic-md.ts` 解析）。

### 3.2 必需字段

完整字段表见 **[content-model.md](content-model.md)**。以下为最低门禁摘要：

- **产品页**：`slug`、`name`、`content.hero`（h1/description/cta_url）、`content.about`、`content.faqs`
- **主题页**：frontmatter 中 `h1`、`description`、intro section（`#intro`）
- **公司页**：`slug`、`name`、`content.description`、`content.type`（`company` 或 `investor`）

### 3.3 禁止的内容模式

- FAQ 区块中不得包含站内链接（会稀释 FAQPage schema 的信号）
- Conclusão 必须位于 FAQ 之前
- TL;DR（主题页）的 points 不得重复 intro 的原文
- 产品页的 `alternatives` 必须为实际竞品，不得填无关工具凑数

### 3.4 图片与 Alt 文本

- 产品 hero 截图（LCP 候选）：alt 文本限 125 字符，格式为 `"Interface do [Nome], [descricao da categoria], exibindo funcionalidades"`
- 产品 logo：alt 文本格式为 `"Logo do [Nome]"`
- 所有 `<img>` 标签必须有 `alt` 属性（装饰性图片用 `alt=""`）
- 优先使用 Next.js `Image` 组件（自动优化），仅在 Header/Footer 等非关键位置使用原生 `<img>`

## 四、SEO 规则

### 4.1 Metadata

每个页面必须通过 `generateMetadata()`（动态页）或 `export const metadata`（静态页）设置：

| 字段 | 要求 |
|------|------|
| `title` | 优先使用 JSON 中的 `seo_title`；fallback 为 `"{name}: Analise Completa | Nova Scientia"`（产品）或 `"{h1} | Nova Scientia"`（主题） |
| `description` | 优先使用 `seo_description`；fallback 为 `content.description` 或 `content.hero.description` |
| `alternates.canonical` | 优先使用 `canonical_url`；fallback 为上述 2.3 规则 |
| `openGraph` | 必须包含 `title`、`description`、`url`、`type: "article"`、`locale: "pt_BR"`、`images`（如有 og_image） |
| `twitter` | `card: "summary_large_image"`，title 和 description 与 OG 一致 |

### 4.2 结构化数据

| Schema 类型 | 位置 | 页面 |
|-------------|------|------|
| Organization | `app/[locale]/layout.tsx` | 全站 |
| WebSite | `app/[locale]/layout.tsx` | 全站 |
| Person (author) | `app/[locale]/layout.tsx` | 全站 |
| SoftwareApplication + FAQPage + ItemList | 产品页组件内 | `/products/[slug]` |
| FAQPage + HowTo | `TopicJsonLd` 组件 | `/{slug}`（主题） |
| CollectionPage | 列表页 | `/products`、`/topic`、`/company` |

所有 schema 使用 `@id` 引用链接到根布局中的 Organization/Person，确保实体一致性。

### 4.3 Sitemap

`app/sitemap.ts` 自动从 `getAllProducts()`、`getAllTopics()`、`getAllCompanies()`、`getGlossaryData()`、`getCategoryHubSlugs()` 生成。产品页 `lastmod` 来自 `content.lastUpdated`；主题页无 `lastUpdated` 字段时不输出 `lastModified`。

### 4.4 IndexNow

`npm run indexnow:all` 通过部署仓 `scripts/permanent/indexnow-submit.ts` 向 Bing IndexNow 批量提交全站 URL。URL 列表来自 `src/lib/urls.ts` 中的 `getAllPageUrls()`——这是 sitemap 和 IndexNow 的单一数据源。

## 五、视觉规则

所有颜色、字体、按钮、链接、布局与禁止事项以 **[brand.md](brand.md)** 为唯一权威来源。实现位于部署仓 `src/index.css` 与 `tailwind.config.ts`。

核心约束：
- 组件使用 CSS 变量（`bg-background`、`text-foreground` 等），禁止硬编码色值
- CTA 使用 `btn-primary`；外链由 `getExternalLinkRel()` 处理 `rel`
- 亮色/暗色模式通过 CSS 变量与 `.dark` class 切换

## 六、命名规则

### 6.1 文件名

- 组件文件：PascalCase（`ProductHeroSection.tsx`、`TopicPage.tsx`）
- 工具/类型文件：kebab-case（`product-adapter.ts`、`category-hub.ts`）
- JSON 数据文件：kebab-case slug 匹配（`chatgpt.json`）
- 主题 Markdown：`{slug}.md` 与 frontmatter `slug` 一致
- 文档文件：kebab-case（`reference.md`、`page-types.md`）

### 6.2 组件命名

- 页面级组件：`{Domain}Layout` 或 `{Domain}Page`（`ProductLayout`、`TopicPage`、`CompanyLayout`）
- 页面子区块：`{Domain}{Section}`（`ProductHeroSection`、`TopicTldr`、`CompanyPortfolio`）
- 共享组件：描述性名称（`BreadcrumbNav`、`FeaturedCard`、`NotFoundContent`）

### 6.3 类型命名

- API 原始类型：`Api{Entity}`（`ApiProduct`、`ApiTopic`、`ApiCompany`）
- 展示用类型：`{Entity}DisplayData`（`ProductDisplayData`）
- 共享类型（客户端安全）：放在 `*-shared.ts` 文件中
- 接口属性使用 snake_case 以匹配 JSON 字段（与 API 输出保持一致）

## 七、性能规则

- 所有产品/主题/公司页面使用 SSG（`generateStaticParams`）
- 首屏图片使用 Next.js `Image` 组件 + `priority` 属性
- 图标统一使用 `lucide-react`
- `next.config.js` 中已配置 `optimizePackageImports` 用于 Radix 组件的 tree-shaking

## 八、内容更新流程

完整步骤见 **[content-workflow.md](content-workflow.md)**（编辑 JSON/MD → validate → build → deploy → IndexNow）。

## 九、参考来源

| 文档 | 路径 |
|------|------|
| 页面类型定义 | `specs/page-types.md` |
| 数据模型 | `specs/content-model.md` |
| 品牌视觉全规范 | `specs/brand.md` |
| Slug/面包屑规则 | `specs/slug-breadcrumb.md` |
| 内容编辑流程 | `specs/content-workflow.md` |
| 脚本使用说明 | `scripts/README.md` |
