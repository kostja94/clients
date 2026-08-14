# MeDo 结构化数据（Schema）实施指南

> **站点**：https://medo.dev  
> **适用对象**：工程 / SEO 负责人（人类）+ Cursor Agent  
> **范围**：全站 JSON-LD 类型选型、字段约定、页面矩阵、验收与排错  
> **外部规则**：[Schema Markup Skill v1.5](https://github.com/kostja94/marketing-skills/blob/main/skills/seo/on-page/schema/SKILL.md) | [FAQ Page Skill](https://github.com/kostja94/marketing-skills/blob/main/skills/pages/content/faq/SKILL.md)  
> **Last updated**：2026-06-22 · **版本**：2.0 · **线上复核**：2026-06-22 HTTP 抓取

---

## 文档结构

| 部分 | 读者 | 用途 |
|------|------|------|
| **Part I — 人类实施指南** | 工程 / SEO | 现状、修正项、分阶段任务、验收 |
| **Part II — Agent 执行手册** | Cursor Agent | 常量、页型矩阵、决策树、禁止项 |
| **附录 A–F** | 实施时复制 | JSON-LD 模板；**附录 F** 为完整 Blog 文章示例 |

**互链**：[medo-site-structure.md](../medo-site-structure.md) | [medo-indexing-diagnosis.md](./medo-indexing-diagnosis.md) | [blog/README.md](../blog/README.md)

---

# Part I — 人类实施指南

## 1. 为什么要做 Schema

结构化数据让 Google / Bing / AI 搜索（AI Overviews、Perplexity 等）**准确理解**页面实体：产品是什么、文章作者、FAQ 答案、活动日期等。

| 目标 | MeDo 相关类型 | Google 富结果预期（2026） |
|------|---------------|---------------------------|
| 品牌实体 | Organization、WebSite | Sitelinks searchbox（品牌词） |
| 内容收录 | BlogPosting、Article | Article 富结果（高概率） |
| 导航 | BreadcrumbList | 搜索结果路径展示（高概率） |
| 产品认知 | SoftwareApplication | **有限/情境依赖** — 不保证富摘要 |
| 定价 FAQ | FAQPage | **多数商业站已无 FAQ 下拉富结果**（2023 起收紧）；仍利于 GEO 与内容结构 |
| 活动 | Event | Event 富结果（活动页，日期须准确） |
| 教程步骤 | HowTo | **Google 已于 2023-09 全面废弃 HowTo 富结果**；仅 Bing / AI 可能消费 |

> **原则**（对齐 Schema Skill）：Schema.org 类型可以比 Google 富结果清单更宽；**标记须与可见内容一致**；无富结果 ≠ 不做 Schema（AI 可见度仍受益）。

---

## 2. 线上现状与缺口（2026-06-22）

| 页面类型 | 代表 URL | 可抓取 | 现有 Schema | 缺口 |
|----------|----------|--------|-------------|------|
| 首页 | `/` | ✅ ~9 KB | ❌ 无 JSON-LD | Organization、WebSite、SoftwareApplication |
| Blog 索引 | `/blog/` | ✅ Ghost SSR | Ghost 默认 `WebSite` | 应为 `CollectionPage`；Organization.url 误指 `/blog/` |
| Blog 文章 | `/blog/build-an-app-…/` | ✅ | `Article` + Person | 改 `BlogPosting`；补 Breadcrumb、FAQ（有区块时） |
| Ghost 模板页 | `/blog/*-template/` | ✅ | `@graph` 较完整 + 冗余 Ghost `Article` | 合并为单块 JSON-LD；清理 description HTML |
| Blog 视频 | `/blog/video/{slug}/` | ✅ | 仅 `Article` | 补 `VideoObject` |
| About | `/blog/about-us/` | ✅ | `Article` | 改 `AboutPage`（**不要**把 Organization 只放在 About 页） |
| App 详情 | `/apps/app-{id}` | ❌ SPA ~6.8 KB | ❌ | SSR 后 `SoftwareApplication` |
| 营销 SPA | `/pricing` 等 | ❌ 空壳 | ❌ | SSR 后按页型补全 |

**优先样本**：Ghost 模板页已有 `SoftwareApplication` + `BreadcrumbList` + `FAQPage` 的 `@graph`，可作为 `/apps/*` 目标实现，但须合并双 JSON-LD 块。

---

## 3. 相对 v1.0 / Schema Skill 的修正项

以下为对照 [Schema Markup Skill v1.5](https://github.com/kostja94/marketing-skills/blob/main/skills/seo/on-page/schema/SKILL.md) 与 Google 文档后，**v1.0 文档中的错误或过度承诺**：

| # | v1.0 问题 | 修正 |
|---|-----------|------|
| E1 | HowTo 列为 Blog P0 附加类型，表述像富结果目标 | HowTo **仅可选、GEO/Bing**；Google 无 HowTo 富结果；教程优先 FAQPage + 正文步骤 |
| E2 | 未说明 FAQPage 富结果对商业站极难获得 | 仍实施 FAQ（parity + GEO），**不**以 FAQ 下拉为 KPI |
| E3 | `/pricing` 用 `Product` 描述 SaaS 平台 | SaaS 定价页主产品实体用 **`SoftwareApplication` + `Offer`/`AggregateOffer`**；`Product` 留给实体商品 |
| E4 | `WebSite`「仅首页输出完整定义」但未说明 Organization 全局布局 | **最优**：根 layout 注入 Organization + WebSite 各 **一次**；各页 `@id` 引用，避免重复完整节点 |
| E5 | About 页未强调 Skill 规则 | About 用 **`AboutPage`**；Organization 是实体级，放首页/全局 layout，**不要**只写在 About |
| E6 | 缺 `inLanguage` | 英文站各页加 `"inLanguage": "en-US"` |
| E7 | 日期示例 `"2026-06-08"` 缺时区 | JSON-LD 用 **ISO 8601 含时区**，如 `2026-06-08T00:00:00Z` |
| E8 | 缺 `headline` ≤110 字符约束 | Google Article/BlogPosting 要求 headline **≤110 字符** |
| E9 | 缺可见日期 CTR 规则 | 页面**只展示一个日期**（有更新则展示 dateModified，否则 datePublished）；JSON-LD 可两者并存 |
| E10 | Phase 1 把首页 Schema 排在营销页之后 | Organization + WebSite 应 **Phase 0**（或根 layout 首屏） |
| E11 | `SearchAction` 未验证 | 首页无站内搜索则 **省略** `potentialAction`，避免无效 Sitelinks searchbox |
| E12 | `publisher.logo` 用 60×60 favicon | Google 要求 publisher logo；建议 **≥112×112**，优先专用 logo 非 favicon |
| E13 | Case Study 类 Blog 未映射 | `category: Case Study` 可用 Schema 类型 **`CaseStudy`**（Skill exclusive type） |

---

## 4. 全局实体（SSOT）

### 4.1 放置策略

| 位置 | Organization | WebSite | 说明 |
|------|:------------:|:-------:|------|
| **根 layout / 首页** | ✅ 完整定义 | ✅ 完整定义 | Skill 推荐全局一次；Google 取首次实例 |
| **About 页** | ❌ 不重复完整定义 | ❌ | 用 `AboutPage`，经 `about` / `@id` 指向 Organization |
| **Blog（Ghost）** | `@id` 引用 | `@id` 引用 | 修正 `publisher.url` → `https://medo.dev/` |
| **其他页面** | `@id` 引用 | `@id` 引用 | 页级 `@graph` 只放 WebPage/BlogPosting 等 |

### 4.2 Organization + WebSite

完整 JSON-LD 见 **附录 A**（Organization）、**附录 B**（WebSite）。

核对项：

- `legalName`、`sameAs` 与官方披露一致  
- Logo URL 可 200；尺寸建议 ≥112×112  
- 勿使用 `publisher.url: https://medo.dev/blog/`

---

## 5. 页面类型 → Schema（人类速查）

| 页面 | 路径 | 主类型 | 附加（按需） | 阶段 |
|------|------|--------|--------------|:----:|
| 首页 | `/` | WebSite | SoftwareApplication、FAQPage（0–4 题） | P0 |
| Blog 索引 | `/blog/` | CollectionPage | BreadcrumbList | P0 |
| Blog 文章 | `/blog/{slug}/` | **BlogPosting** | BreadcrumbList、FAQPage+ | P0 |
| Blog 视频 | `/blog/video/{slug}/` | BlogPosting | VideoObject、BreadcrumbList | P1 |
| Blog 案例 | category=Case Study | **CaseStudy** 或 BlogPosting | FAQPage+ | P1 |
| Ghost 模板 | `/blog/*-template/` | WebPage | SoftwareApplication、BreadcrumbList、FAQPage | P0 |
| About | `/blog/about-us/` | **AboutPage** | — | P1 |
| 定价 | `/pricing` | WebPage | **SoftwareApplication**、AggregateOffer、FAQPage | P1 |
| 联盟 | `/affiliate` | WebPage | FAQPage | P1 |
| Hackathon | `/hackathon` | WebPage | **Event**、FAQPage+ | P1 |
| FAQ  hub | `/faq` | FAQPage | BreadcrumbList | P1 |
| 对比 | `/vs/{x}` | WebPage | FAQPage、BreadcrumbList | P2 |
| App 详情 | `/apps/app-{id}` | SoftwareApplication | BreadcrumbList、FAQPage+ | P2 |
| 分类广场 | `/templates/{cat}` | CollectionPage | ItemList、BreadcrumbList | P2 |

**BlogPosting vs Article vs CaseStudy**（Skill：选最具体类型）：

| 类型 | 何时用 |
|------|--------|
| **BlogPosting** | 默认：Ghost posts、教程、指南 |
| **Article** | 正式常青枢纽（如未来 `/learn/{topic}` 非 blog 路径） |
| **CaseStudy** | 客户案例、成果叙事 |
| **NewsArticle** | 时效新闻稿（Product Hunt 快讯等） |

---

## 6. 分页面要点

### 6.1 Blog 文章

**必填**（Google Article 系）：`headline`（≤110 字符）、`image`（绝对 URL，宽 ≥1200px 推荐）、`datePublished`（ISO 8601）、`author`（Person）、`publisher`（Organization **含 logo**）。

**推荐**：`dateModified`、`description`、`mainEntityOfPage`、`inLanguage: "en-US"`、`articleSection`、`keywords`。

**OG 对齐**：`og:type=article`，配合 `article:published_time`、`article:modified_time`、`article:author`。

**FAQ**：正文有 `## Frequently asked questions` → 输出 `FAQPage`（附录 D）；问答与 DOM **逐字一致**。

**HowTo（可选）**：仅当正文有 ≥3 编号步骤且团队需要 Bing/AI 结构化步骤；**不**作为 Google 富结果目标。

模板见 **附录 C**；完整可粘贴示例见 **附录 F**（`how-to-build-mobile-app-with-ai`）。

### 6.2 Ghost 模板页

保留现有 `@graph` 思路，执行：

1. 合并为 **单一** `<script type="application/ld+json">`  
2. 移除 Ghost 默认冗余 `Article` 块  
3. `SoftwareApplication.name` 用短产品名  
4. 面包屑中间 URL 须 200（如 `marketplace/tools` 待 IA 确认）  
5. `description` strip HTML

### 6.3 定价 `/pricing`

- 主产品：**SoftwareApplication**（MeDo 平台）+ **AggregateOffer**（各档 credits）  
- **FAQPage** 6–8 题（credits、免费额、消耗、退款等）  
- 定价 FAQ **不与** `/faq` 聚合页重复（registry 去重）

### 6.4 App 详情 `/apps/app-{id}`

前置：SSR 独特 Title / Description / H1（见 [medo-indexing-diagnosis.md](./medo-indexing-diagnosis.md)）。

止血期 `noindex` 仍建议输出 Schema，便于去掉 noindex 后快速验证。

### 6.5 FAQ 内容规则

| 维度 | 要求 |
|------|------|
| 题量 | 页内 3–8；Blog ≥3；定价 6–8；FAQ hub 8–15 |
| 答案 | 40–80 英文词；首句直接回答 |
| Parity | 可见 HTML = FAQPage JSON-LD |
| 去重 | 同一问题只在一个 canonical URL |
| Blog | `## Frequently asked questions` + `###` 问题 |

---

## 7. 面包屑

| 规则 | 说明 |
|------|------|
| 首页 | 无面包屑、无 BreadcrumbList |
| 语言 | 英文标签 |
| Parity | UI 与 JSON-LD 一致 |
| 末级 | 推荐 **无 `item` URL**（Google 允许末级带 URL，全站择一统一） |

层级速查：

| 路径 | 面包屑 |
|------|--------|
| `/blog/` | Home > Blog |
| `/blog/{slug}/` | Home > Blog > {title} |
| `/blog/video/{slug}/` | Home > Blog > Video > {title} |
| `/pricing` | Home > Pricing |
| `/vs/lovable` | Home > Compare > MeDo vs Lovable |

---

## 8. 实施路线图

### Phase 0 — 可立即做（Ghost / 全局 layout）

| # | 任务 |
|---|------|
| 1 | 根 layout 或首页：附录 A + B（Organization + WebSite） |
| 2 | Ghost：`publisher.url` → `https://medo.dev/`；logo 尺寸升级 |
| 3 | Blog 索引 → `CollectionPage` + BreadcrumbList |
| 4 | 26 posts：`Article` → `BlogPosting` + `inLanguage` + ISO 日期 |
| 5 | 模板页：合并双 JSON-LD；禁用 Ghost 默认 Article |
| 6 | 有 FAQ 区块的文章 / 模板：补 FAQPage |

### Phase 1 — 营销页 SSR 后

| # | 任务 |
|---|------|
| 1 | `/pricing` — WebPage + SoftwareApplication + AggregateOffer + FAQPage |
| 2 | `/faq`、`/affiliate`、`/hackathon` |
| 3 | `/blog/about-us/` → AboutPage |
| 4 | 视频文补 VideoObject |

### Phase 2 — 广场 SSR 后

| # | 任务 |
|---|------|
| 1 | `/apps/*` — SoftwareApplication + BreadcrumbList |
| 2 | `/templates/{category}` — CollectionPage + ItemList |
| 3 | `/vs/*`、`/compare` |

---

## 9. 验收

### 9.1 工具

| 工具 | 用途 |
|------|------|
| [Rich Results Test](https://search.google.com/test/rich-results) | Google 富结果资格 |
| [Schema Markup Validator](https://validator.schema.org/) | Schema.org 语法 |
| GSC → Enhancements | 持续监控 Breadcrumb / FAQ 报告 |

### 9.2 发布前清单

- [ ] 单页一个 JSON-LD（或单一 `@graph`）
- [ ] Organization `@id` = `https://medo.dev/#organization`，`url` = 根域
- [ ] Blog 为 BlogPosting（不与 BlogPosting 并存 Article）
- [ ] `headline` ≤110 字符；与 H1 一致
- [ ] `image` 绝对 URL；publisher.logo 可用
- [ ] 日期 ISO 8601 含时区；可见日期只展示一个
- [ ] `inLanguage: "en-US"` 于英文页
- [ ] FAQ / 面包屑 parity
- [ ] 无虚构 `aggregateRating` / `Review`
- [ ] 无无效 SearchAction（无搜索则省略）

### 9.3 线上 URL 清单

**Ghost posts（26）**：`https://medo.dev/blog/sitemap-posts.xml`  
**Ghost pages（54）**：`https://medo.dev/blog/sitemap-pages.xml`

优先优化（高商业意图）：

- `/blog/build-an-app-without-coding-in-2026-the-honest-step-by-step-guide/`
- `/blog/best-lovable-alternative-in-2026-medo-vs-lovable-vs-bolt/`
- `/blog/how-to-build-a-micro-saas-without-coding-in-2026-a-practical-guide/`
- `/blog/medo-hackathon-2026-guide-launch-your-ai-app-win-50k/`
- `/blog/unlock-your-earnings-with-the-medo-affiliate-program/`

本地 [blog/](../blog/) 5 篇（如 `how-to-build-mobile-app-with-ai`）线上仍 404 — 部署时按附录 C 输出 Schema。

---

# Part II — Agent 执行手册

> 优化或新建页面 Schema 时加载 **Part II + 对应附录**。代码/注入以站点实际框架（Next layout、Ghost theme）为准；**JSON-LD 字符串从附录复制后替换占位符**。

---

## A. 项目常量

```yaml
site:
  base_url: "https://medo.dev"
  organization_id: "https://medo.dev/#organization"
  website_id: "https://medo.dev/#website"
  software_id: "https://medo.dev/#software"
  in_language: "en-US"

organization:
  name: "MeDo"
  legal_name: "Sailai Private Limited"
  email: "Admin@medo.dev"
  logo_url: "https://s3-us-east-2.amazonaws.com/miaoda-cms-ghost-resource/2026/03/favicon.png"  # 上线前换 ≥112px logo
  same_as:
    - "https://www.producthunt.com/products/medo"
    - "https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en"

google_rich_results_2026:
  high_impact: [Product, Article, VideoObject, BreadcrumbList, Event, WebSite_SearchAction]
  limited: [FAQPage, SoftwareApplication]
  deprecated_rich: [HowTo]  # Sep 2023 — no Google rich results

blog:
  index_url: "https://medo.dev/blog/"
  index_id: "https://medo.dev/blog/#webpage"
  frontmatter_map:
    title: headline
    description: description
    date: datePublished
    author: author.name
    category: articleSection
    image: image  # must be absolute URL at build time
    slug: url path

ghost:
  fix_publisher_url: "https://medo.dev/"  # NOT /blog/
  template_suffix: "-template"
  merge_dual_jsonld: true
  disable_default_article_on_templates: true

validation:
  rich_results: "https://search.google.com/test/rich-results"
  schema_org: "https://validator.schema.org/"
```

---

## B. 页型 → Schema 矩阵（Agent 查表）

| page_type | path_pattern | primary @type | additional @types | phase |
|-----------|--------------|---------------|-------------------|-------|
| homepage | `/` | WebSite | SoftwareApplication, FAQPage? | P0 |
| blog_index | `/blog/` | CollectionPage | BreadcrumbList | P0 |
| blog_post | `/blog/{slug}/` | BlogPosting | BreadcrumbList, FAQPage? | P0 |
| blog_video | `/blog/video/{slug}/` | BlogPosting | VideoObject, BreadcrumbList | P1 |
| blog_case_study | `/blog/{slug}/` + category=Case Study | CaseStudy | FAQPage?, BreadcrumbList | P1 |
| ghost_template | `/blog/*-template/` | WebPage | SoftwareApplication, BreadcrumbList, FAQPage | P0 |
| about | `/blog/about-us/` | AboutPage | — | P1 |
| pricing | `/pricing` | WebPage | SoftwareApplication, AggregateOffer, FAQPage, BreadcrumbList | P1 |
| affiliate | `/affiliate` | WebPage | FAQPage, BreadcrumbList | P1 |
| hackathon | `/hackathon` | WebPage | Event, FAQPage?, BreadcrumbList | P1 |
| faq_hub | `/faq` | FAQPage | BreadcrumbList | P1 |
| vs_page | `/vs/{competitor}` | WebPage | FAQPage, BreadcrumbList | P2 |
| app_detail | `/apps/app-{id}` | SoftwareApplication | BreadcrumbList, FAQPage? | P2 |
| template_category | `/templates/{cat}` | CollectionPage | ItemList, BreadcrumbList | P2 |

---

## C. 决策树

```
INPUT: page_url, page_type, has_faq_section, has_numbered_steps, category

LOAD global @ids: organization_id, website_id

IF page_url in ["/", ""]:
  EMIT @graph: [Organization full, WebSite full, SoftwareApplication]
  IF site_has_search:
    INCLUDE WebSite.potentialAction SearchAction
  ELSE:
    OMIT potentialAction
  breadcrumb: NONE
  STOP

IF page_type == about:
  EMIT AboutPage (headline, description, inLanguage)
  REFERENCE organization via about: {@id organization_id}
  DO NOT emit full Organization block on this page only
  STOP

IF page_type == blog_index:
  EMIT CollectionPage + BreadcrumbList[Home, Blog]
  REFERENCE publisher → organization_id, isPartOf → website_id
  STOP

IF page_type == blog_post:
  primary ← BlogPosting
  IF category == "Case Study":
    primary ← CaseStudy OR BlogPosting  # prefer CaseStudy if template supports
  EMIT primary + BreadcrumbList[Home, Blog, title]
  IF has_faq_section:
    EMIT FAQPage from visible FAQ DOM (appendix D)
  IF has_numbered_steps >= 3 AND user_wants_geo_only:
    OPTIONAL HowTo  # NOT for Google rich results
  ENFORCE: headline <= 110 chars, image absolute, dates ISO8601Z, inLanguage en-US
  FORBIDDEN: Article AND BlogPosting together
  STOP

IF page_type == ghost_template:
  EMIT single @graph: WebPage + SoftwareApplication + BreadcrumbList + FAQPage?
  REMOVE ghost default Article block
  STRIP HTML from descriptions
  STOP

IF page_type == pricing:
  EMIT WebPage + SoftwareApplication + AggregateOffer + FAQPage(6-8) + BreadcrumbList
  USE SoftwareApplication NOT Product for SaaS platform
  STOP

IF page_type == app_detail:
  REQUIRE ssr_unique_meta
  EMIT SoftwareApplication + BreadcrumbList
  EMIT even if noindex
  STOP

DEFAULT:
  EMIT WebPage + BreadcrumbList(if not homepage)
  ADD FAQPage if visible FAQ
  REFERENCE organization_id, website_id via @id

POST-EMIT:
  VALIDATE single script tag
  RUN parity check FAQ + breadcrumb
  RUN Rich Results Test URL
```

---

## D. 禁止项

```yaml
forbidden:
  - hidden_schema_not_in_dom
  - multiple_FAQPage_per_url
  - Article_and_BlogPosting_same_page
  - Event_on_non_event_pages
  - aggregateRating_without_real_reviews
  - SearchAction_without_site_search
  - Organization_only_on_about_page
  - publisher_url_https://medo.dev/blog/
  - FAQ_question_duplicated_across_urls
  - HowTo_as_google_rich_result_KPI
  - Product_type_for_saas_platform_pricing  # use SoftwareApplication
  - headline_over_110_chars
  - date_without_timezone_in_jsonld
```

---

## E. FAQ 题量与主题（Agent 生成 FAQ 时用）

| page_type | themes | count |
|-----------|--------|-------|
| homepage | what is MeDo, who is it for, free start | 0-4 |
| pricing | credits, free tier, usage, refund, enterprise | 6-8 |
| affiliate | commission, payout, tracking, limits | 5-6 |
| hackathon | enter, prizes, rules, deadline | 4-6 |
| faq_hub | general product (NOT pricing detail) | 8-15 |
| blog_tutorial | objections, limits, cost | 3-6 |
| blog_comparison | selection criteria, migration | 5-6 |
| app_template | free, customize, deploy, data | 4-6 |

答案：40–80 英文词；首句直接回答；与正文相似度 <30%。

---

## F. 与 Blog Skill 的衔接

| 文档 | 用途 |
|------|------|
| [blog/README.md](../blog/README.md) | frontmatter → BlogPosting 字段 |
| [extractability-checklist.md](../skills/medo-blog-article/references/portable/extractability-checklist.md) | Draft 阶段 Schema 检查 |
| [medo-indexing-api-indexnow-guide.md](./medo-indexing-api-indexnow-guide.md) | Schema 部署后 URL 通知 |

---

# 附录 A — Organization（全局 SSOT）

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://medo.dev/#organization",
  "name": "MeDo",
  "legalName": "Sailai Private Limited",
  "url": "https://medo.dev/",
  "inLanguage": "en-US",
  "logo": {
    "@type": "ImageObject",
    "url": "https://s3-us-east-2.amazonaws.com/miaoda-cms-ghost-resource/2026/03/favicon.png",
    "width": 512,
    "height": 512
  },
  "sameAs": [
    "https://www.producthunt.com/products/medo",
    "https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "Admin@medo.dev",
    "contactType": "customer support"
  }
}
```

---

# 附录 B — WebSite（首页或根 layout）

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://medo.dev/#website",
  "url": "https://medo.dev/",
  "name": "MeDo",
  "inLanguage": "en-US",
  "description": "Build full-stack apps with a no-code AI platform — frontend, backend, database, and integrations in minutes.",
  "publisher": { "@id": "https://medo.dev/#organization" }
}
```

有 verified 站内搜索时追加：

```json
"potentialAction": {
  "@type": "SearchAction",
  "target": {
    "@type": "EntryPoint",
    "urlTemplate": "https://medo.dev/search?q={search_term_string}"
  },
  "query-input": "required name=search_term_string"
}
```

---

# 附录 C — BlogPosting @graph 模板

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@id": "https://medo.dev/#organization" },
    {
      "@type": "BlogPosting",
      "@id": "https://medo.dev/blog/{slug}/#blogposting",
      "headline": "TITLE MAX 110 CHARS",
      "description": "META DESCRIPTION PLAIN TEXT",
      "url": "https://medo.dev/blog/{slug}/",
      "inLanguage": "en-US",
      "datePublished": "2026-06-08T00:00:00Z",
      "dateModified": "2026-06-08T00:00:00Z",
      "image": "https://medo.dev/blog/images/{slug}.jpg",
      "author": {
        "@type": "Person",
        "name": "Kostja",
        "url": "https://medo.dev/blog/author/kostja/"
      },
      "publisher": { "@id": "https://medo.dev/#organization" },
      "mainEntityOfPage": "https://medo.dev/blog/{slug}/",
      "articleSection": "Tutorial",
      "keywords": ["keyword one", "keyword two"],
      "isPartOf": { "@id": "https://medo.dev/blog/#webpage" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://medo.dev/blog/{slug}/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://medo.dev/" },
        { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://medo.dev/blog/" },
        { "@type": "ListItem", "position": 3, "name": "FULL ARTICLE TITLE" }
      ]
    }
  ]
}
```

---

# 附录 D — FAQPage 模板

```json
{
  "@type": "FAQPage",
  "@id": "https://medo.dev/PAGE-PATH/#faq",
  "inLanguage": "en-US",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "QUESTION TEXT EXACTLY AS ON PAGE",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Answer-first paragraph, 40-80 words, matches visible content.</p>"
      }
    }
  ]
}
```

---

# 附录 E — SoftwareApplication（平台 / App / 定价）

**首页 / 定价（SaaS 平台）**：

```json
{
  "@type": "SoftwareApplication",
  "@id": "https://medo.dev/#software",
  "name": "MeDo",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "inLanguage": "en-US",
  "description": "AI no-code platform to build and deploy full-stack web and mobile apps from natural language.",
  "url": "https://medo.dev/",
  "creator": { "@id": "https://medo.dev/#organization" },
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "USD",
    "lowPrice": "0",
    "offerCount": "3",
    "offers": [
      {
        "@type": "Offer",
        "name": "Free tier",
        "price": "0",
        "priceCurrency": "USD"
      }
    ]
  }
}
```

**UGC App 详情** — 将 `@id`、`name`、`description`、`url`、`applicationCategory` 换为 App 独特值；`creator` 仍指向 MeDo Organization。

---

# 附录 F — 完整示例：Blog 文章（含 FAQ）

> **来源**：[blog/01-how-to-build-mobile-app-with-ai.md](../blog/01-how-to-build-mobile-app-with-ai.md)  
> **URL**：`https://medo.dev/blog/how-to-build-mobile-app-with-ai/`  
> **说明**：单页一个 `<script type="application/ld+json">`；`Organization` 在此示例内写全节点便于本地校验——**生产环境** Organization / WebSite 应由根 layout 注入一次，正文页仅 `@id` 引用（见 §4.1）。FAQ 问答与正文 `## Frequently asked questions` **逐字一致**。

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://medo.dev/#organization",
      "name": "MeDo",
      "legalName": "Sailai Private Limited",
      "url": "https://medo.dev/",
      "inLanguage": "en-US",
      "logo": {
        "@type": "ImageObject",
        "url": "https://s3-us-east-2.amazonaws.com/miaoda-cms-ghost-resource/2026/03/favicon.png",
        "width": 512,
        "height": 512
      },
      "sameAs": [
        "https://www.producthunt.com/products/medo",
        "https://intl.cloud.baidu.com/en/doc/MIAODA/s/overview-en"
      ],
      "contactPoint": {
        "@type": "ContactPoint",
        "email": "Admin@medo.dev",
        "contactType": "customer support"
      }
    },
    {
      "@type": "BlogPosting",
      "@id": "https://medo.dev/blog/how-to-build-mobile-app-with-ai/#blogposting",
      "headline": "How to Build a Mobile App with AI — a Non-Developer's Guide for 2026",
      "description": "A non-developer's guide to building real iOS and Android apps with AI vibe coding in 2026: validate your idea, pick a builder, ship to TestFlight and the App Store.",
      "url": "https://medo.dev/blog/how-to-build-mobile-app-with-ai/",
      "inLanguage": "en-US",
      "datePublished": "2026-06-08T00:00:00Z",
      "dateModified": "2026-06-08T00:00:00Z",
      "image": "https://medo.dev/blog/images/build-mobile-app-with-ai.jpg",
      "author": {
        "@type": "Person",
        "name": "Kostja",
        "url": "https://medo.dev/blog/author/kostja/"
      },
      "publisher": { "@id": "https://medo.dev/#organization" },
      "mainEntityOfPage": "https://medo.dev/blog/how-to-build-mobile-app-with-ai/",
      "articleSection": "Tutorial",
      "keywords": [
        "how to build mobile app with AI",
        "build mobile app with AI",
        "AI mobile app builder",
        "vibe coding mobile app",
        "non-developer mobile app",
        "AI app builder 2026"
      ],
      "isPartOf": { "@id": "https://medo.dev/blog/#webpage" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://medo.dev/blog/how-to-build-mobile-app-with-ai/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://medo.dev/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Blog",
          "item": "https://medo.dev/blog/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "How to Build a Mobile App with AI — a Non-Developer's Guide for 2026"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://medo.dev/blog/how-to-build-mobile-app-with-ai/#faq",
      "inLanguage": "en-US",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Can I really build a mobile app without knowing how to code?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "<p>Yes. With AI vibe coding tools you describe what you want in plain English and the tool writes the underlying Swift or Kotlin. You still need to think carefully about what the app does, who it's for, and how data flows — but you don't need to memorize syntax or wrestle with Xcode and Gradle.</p>"
          }
        },
        {
          "@type": "Question",
          "name": "How long does it take to build a mobile app with AI?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "<p>A focused MVP — three to five screens, login, one database table — is realistic in a weekend. A polished v1 ready for the App Store usually takes two to four weekends, mostly spent on copy, edge cases, and store assets rather than code.</p>"
          }
        },
        {
          "@type": "Question",
          "name": "How much does it cost to build a mobile app with AI in 2026?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "<p>Expect roughly $20–$50/month for the AI builder, $99/year for an Apple Developer account, and $25 one-time for Google Play. Backend, push notifications and storage usually fit inside generous free tiers until you have real users.</p>"
          }
        },
        {
          "@type": "Question",
          "name": "Will Apple and Google approve an AI-generated app?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "<p>Yes — both stores review the finished binary, not how it was written. As long as your app does something useful, respects platform guidelines, and doesn't simply repackage a website, AI-generated apps pass review at the same rate as hand-written ones.</p>"
          }
        },
        {
          "@type": "Question",
          "name": "Do I own the code an AI generates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "<p>On reputable platforms, yes. The AI generates standard Swift, Kotlin or React Native code that you can export, read, and host anywhere. Avoid any tool that locks the source inside a proprietary runtime you can't escape.</p>"
          }
        }
      ]
    }
  ]
}
```

**验收**：部署后对该 URL 运行 [Rich Results Test](https://search.google.com/test/rich-results)；确认 BlogPosting、BreadcrumbList、FAQPage 无 error；`headline` 67 字符（≤110）。

---

*MeDo Schema 实施指南 v2.0 · https://medo.dev/ · Schema Skill v1.5 对齐*
