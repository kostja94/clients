# Final Round AI — Schema.org / JSON-LD

> **职责**：全站 **JSON-LD** 落地策略与字段说明（单主题：结构化数据）。  
> **关联**：[finalround.md](../finalround.md) · [finalround-project-tasks.md](../finalround-project-tasks.md)（任务） · [finalround-blog-article skill](../skills/finalround-blog-article/SKILL.md)（Blog 创作 + 竞品 Review 程序化） · [finalround-community-forum.md](../community/finalround-community-forum.md)（Forum）  
> **规范**：[文档优化指导](../../../通用知识库/元文档-通用文档规范.md)（主题一致、去重、互链） · [Schema.org](https://schema.org/) · 验证 [Rich Results Test](https://search.google.com/test/rich-results)、[Schema Validator](https://validator.schema.org/)

**站点**：https://www.finalroundai.com/

**目录**：零 协作者读本 · 一 原则 · 二 图片 · 三 全站通用 · 四 页面一览 · 五 类型索引 · 六 首页示例 · 七 博客与 Review · 八 外部参考 · 九 自检 · [文档维护](#文档维护)

---

## 零、协作者读本（非工程）

业务侧结论见下；**实现规则以 §一 起为准**，避免与「仅 JSON-LD」可见性要求重复展开。

| 结论 | 详见 |
|------|------|
| 结构化数据须与页面**可见**内容一致（FAQ、价格、视频等） | §一 |
| Logo、文章图、视频封面 URL 与实资源一致 | §二 |
| 无独立「计算器」类型；工具页用 `WebApplication` 等 | §四 `/ai-salary-calculator`、§五 Occupation |
| `JobPosting` 仅用于本公司真实招聘岗位 | §五 · 5.2 |
| 改口径时同步改 JSON-LD | §一、§九 |

**不承诺**：排名；标记仅为辅助理解。

---

## 一、原则

1. **分节点**：`VideoObject`、`FAQPage`、`WebSite` 分开描述（或同一 `@graph` 多实体），勿把视频/FAQ 属性堆在一个 `WebSite` 上。  
2. **与 DOM 一致**：FAQ、价格、视频等须在页面**可见**；`sameAs` 用 URL **数组**。  
3. **实体复用**：`Organization` 设稳定 `@id`，供 `publisher`、`isPartOf`、`about` 引用。

---

## 二、图片与 ImageObject

| 场景 | 字段 | 要点 |
|------|------|------|
| 品牌 | `Organization.logo` | 绝对 URL；可与 `width`/`height` 同传 |
| 博客 | `BlogPosting` / `Article` 的 **`image`** | 建议 **≥1200px 宽**；与 `og:image`、正文首图一致 |
| 视频 | `VideoObject.thumbnailUrl` | 与播放器缩略图一致 |
| 应用 | `SoftwareApplication` / `WebApplication` 的 **`screenshot`** | 与落地页截图区对应 |
| 作者 | `Person.image` | 与署名头像一致 |

---

## 三、全站通用（模板注入）

| 类型 | 作用 |
|------|------|
| **Organization** | `name`、`url`、`logo`（ImageObject）、`sameAs`（与**页脚** Facebook / X / IG / TikTok / YouTube / PH 等**对齐**） |
| **WebSite** | 短 `description`、`publisher`、`inLanguage`（如 `en-US`）；有站内搜索时再考虑 `SearchAction` |
| **BreadcrumbList** | 与可见面包屑 **路径、锚文本、链接一致**；`item` **绝对 URL**；`position` 连续 · **常见错误与博客四级示例见 §七 · 7.2** |

---

## 四、页面一览：推荐类型 + 现状

「现状」基于历史审计，**以线上为准**。博客、Review、面包屑的字段细节 **不在此重复**，见 **§七**。

| 页面 | 推荐 Schema | 现状与优化方向 |
|------|-------------|----------------|
| **首页** | Organization, WebSite, WebPage, VideoObject, 可选 FAQPage | `@graph` 拆分；`sameAs` 补全；视频与 §二 对齐；首页若含 FAQ 标记规则见 §七 · 7.1 |
| **`/about`** | AboutPage；Organization（`address`、创始人→Person） | 1M/10M+、80+/100+ 口径统一；PR 占位清理；Trustpilot 与页面对齐再 `aggregateRating` |
| **`/contact`** | ContactPage, ContactPoint | 邮件勿长期对爬虫不可读 |
| **`/download`** | SoftwareApplication（`screenshot`、`operatingSystem`、可选 `downloadUrl`） | 有稳定安装包链可写入 |
| **`/ai-mock-interview`** | FAQPage, HowTo, WebPage | 证言模块重复渲染宜排查 |
| **`/ai-salary-calculator`** | WebApplication（内容就绪后） | 先 SSR/首屏文案；无独立 Calculator 类型 |
| **定价 /subscription** | 可选 Product + Offer | 与可见价格一致 |
| **博客** | BlogPosting/Article, BreadcrumbList；文末 FAQ→FAQPage | 占位与 **image** 见 §二；正文与标记见 **§七 · 7.1–7.2** |
| **竞品 Review** `/blog/{competitor}-review` | Review, FAQPage, 可选 BreadcrumbList | **§七 · 7.3** |
| **/faq 等** | FAQPage | 与可见问答逐条一致 |
| **法律页** | WebPage | — |
| **站内 Forum**（若上线） | 与主站 Organization、`sameAs`、导航一致 | [finalround-community-forum.md](../community/finalround-community-forum.md) §5；外部文档 **§八** |

---

## 五、Schema.org 类型索引（扩展）

词汇表见 [Schema.org](https://schema.org/)。下列与 [finalround.md](../finalround.md) 产品线相关；**≠** Google 均有富结果，以 [Google 搜索图库](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) 为准。

### 5.1 主站与产品（高频）

| 类型 | 链接 |
|------|------|
| Organization · WebSite · WebPage · AboutPage · ContactPage | [Organization](https://schema.org/Organization) [WebSite](https://schema.org/WebSite) [WebPage](https://schema.org/WebPage) [AboutPage](https://schema.org/AboutPage) [ContactPage](https://schema.org/ContactPage) |
| SoftwareApplication · WebApplication | [SoftwareApplication](https://schema.org/SoftwareApplication) [WebApplication](https://schema.org/WebApplication) |
| Product · Offer | [Product](https://schema.org/Product) [Offer](https://schema.org/Offer) |
| FAQPage · HowTo · BreadcrumbList | [FAQPage](https://schema.org/FAQPage) [HowTo](https://schema.org/HowTo) [BreadcrumbList](https://schema.org/BreadcrumbList) |
| Article · BlogPosting · VideoObject | [Article](https://schema.org/Article) [BlogPosting](https://schema.org/BlogPosting) [VideoObject](https://schema.org/VideoObject) |
| Person · ImageObject | [Person](https://schema.org/Person) [ImageObject](https://schema.org/ImageObject) |
| Review | [Review](https://schema.org/Review) |

### 5.2 JobPosting（易误解）

| 说明 |
|------|
| **[JobPosting](https://schema.org/JobPosting)** 表示**一则招聘启事**。仅适用于 **Final Round 公司自己**在 **Careers / Open Roles** 上发布的**真实岗位**（通常一岗一页或列表项）。 |
| **不适用于**：「帮求职者面试」「模拟面试」等 C 端产品描述。第三方职位是否可标见 [Google JobPosting](https://developers.google.com/search/docs/appearance/structured-data/job-posting) 政策。 |

### 5.3 选做（内容匹配时）

| 类型 | 链接 | 说明 |
|------|------|------|
| Course | [Course](https://schema.org/Course) | 独立课纲、多节课程页 |
| LearningResource · Quiz | [LearningResource](https://schema.org/LearningResource) [Quiz](https://schema.org/Quiz) | 题库 / 测验页结构清晰时 |
| Service | [Service](https://schema.org/Service) | 抽象为可订购服务时；勿与 Product 矛盾 |
| Review · AggregateRating | [Review](https://schema.org/Review) [AggregateRating](https://schema.org/AggregateRating) | 与 §5.1 中 `Review` 同型；此处强调与 **可核验评价 / 聚合评分** 同用场景 |
| Occupation | [Occupation](https://schema.org/Occupation) | 与 [Google Estimated salary](https://developers.google.com/search/docs/appearance/structured-data/estimated-salary) 一致时；非普通交互计算器 |
| Dataset | [Dataset](https://schema.org/Dataset) | 公开发布可下载数据时 |

### 5.4 不建议硬套

- **[EducationalOrganization](https://schema.org/EducationalOrganization)**：多为学校实体；你们是 **SaaS 公司**。  
- **JobPosting**：勿把「用户使用场景」写成职位帖。

---

## 六、首页 `@graph` 示例（节选）

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.finalroundai.com/#organization",
      "name": "Final Round AI",
      "url": "https://www.finalroundai.com/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://d12araoe7z5xxk.cloudfront.net/landing-page/images/full-logo.svg"
      },
      "sameAs": ["https://x.com/finalround_ai", "https://www.instagram.com/finalround_ai/", "https://www.youtube.com/@FinalRoundAI"]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.finalroundai.com/#website",
      "name": "Final Round AI",
      "url": "https://www.finalroundai.com/",
      "description": "与 meta description 一致",
      "publisher": { "@id": "https://www.finalroundai.com/#organization" },
      "inLanguage": "en-US"
    },
    {
      "@type": "WebPage",
      "@id": "https://www.finalroundai.com/#webpage",
      "url": "https://www.finalroundai.com/",
      "name": "与 H1 一致",
      "isPartOf": { "@id": "https://www.finalroundai.com/#website" },
      "about": { "@id": "https://www.finalroundai.com/#organization" },
      "inLanguage": "en-US"
    },
    {
      "@type": "VideoObject",
      "@id": "https://www.finalroundai.com/#video-example",
      "name": "与播放器标题一致",
      "thumbnailUrl": "https://img.youtube.com/vi/aDwIYt9vcvM/maxresdefault.jpg",
      "uploadDate": "2024-03-27T10:00:00+00:00",
      "duration": "PT5M5S",
      "contentUrl": "https://www.youtube.com/watch?v=aDwIYt9vcvM",
      "embedUrl": "https://www.youtube.com/embed/aDwIYt9vcvM",
      "publisher": { "@id": "https://www.finalroundai.com/#organization" }
    }
  ]
}
```

若首页另有可见 FAQ 区块，FAQPage 的 `mainEntity` 规则见 **§七 · 7.1**，勿与上方 `@graph` 混为单节点。

---

## 七、博客与 Review 页（字段级）

与 [finalround-project-tasks.md](../finalround-project-tasks.md) **§7.2**（全站 Schema 基座）、**§7.4**（博客面包屑 UI）、**§7.5**（博客详情页 Schema 补全）对应；任务细节以任务表为准，**字段与 JSON-LD 要求以本节为准**。

### 7.1 博客单篇（BlogPosting / Article）

| 要点 | 说明 |
|------|------|
| **主类型** | `BlogPosting` 或 `Article`；`headline` 与 H1、`name`/title 与 SEO title 对齐 |
| **image** | 见 §二；与 `og:image`、首图一致 |
| **作者** | `author` → `Person`（与署名一致）；可有 `reviewedBy` 等若页面展示 |
| **发布** | `datePublished` / `dateModified` 与页面展示一致 |
| **出版方** | `publisher` → 站点 `Organization`（`@id` 引用） |
| **文末 FAQ** | 可见 FAQ 区块可输出 **FAQPage**（独立 script 或 `@graph`）；`mainEntity` 与问答 **逐条一致**（同 §一） |

### 7.2 BreadcrumbList（博客推荐四级）

与 [breadcrumb-generator skill](../../.cursor/skills/components/navigation/breadcrumb/SKILL.md) 一致：**基于位置**、深度通常 **3–5**；博客推荐：

**Home** → **Blog**（`https://www.finalroundai.com/blog`）→ **分类名**（如 Cover Letters → `https://www.finalroundai.com/category/cover-letters`）→ **文章标题**（与 H1 一致）。

- **末级**：页面上一般为 **纯文本**，`aria-current="page"`；不虚构「Categories」一级（除非存在真实分类索引 URL；见 [finalround-project-tasks.md](../finalround-project-tasks.md) §7.4）。
- **JSON-LD**：每个 `ListItem` 含 `position`、`name`；`item` **绝对 URL**；末项 `name` 为文章标题；末项 `item` 是否指向当前文 URL 以实现为准，并以 Rich Results 测试为准。

**示例（四级）**：

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.finalroundai.com/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.finalroundai.com/blog" },
    { "@type": "ListItem", "position": 3, "name": "Cover Letters", "item": "https://www.finalroundai.com/category/cover-letters" },
    { "@type": "ListItem", "position": 4, "name": "Cybersecurity Engineers Cover Letters: Examples and Writing Tips", "item": "https://www.finalroundai.com/blog/cybersecurity-engineers-cover-letter" }
  ]
}
```

**已知线上问题（样例）**：分隔符误链首页；仅三级且末级停在分类；整页缺 BreadcrumbList——修 UI（**§7.4**）与 JSON-LD（**§7.5**）同步。

### 7.3 竞品 Review 文章（`/blog/{competitor}-review`）

正文结构与 SEO 模板见 [finalround-blog-article skill](../skills/finalround-blog-article/references/review-programmatic.md) §2/§5。

| 类型 | 用途 |
|------|------|
| **Review** | `itemReviewed` → 竞品 `SoftwareApplication`（等）；`reviewRating`、`author`；符合 [Google 评论类结构化数据](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| **FAQPage** | 3–5 组问答，与可见 FAQ **一致** |
| **BreadcrumbList** | 可选；若有可见面包屑则必须与 JSON-LD 一致 |
| **Pros/Cons** | 以 Google 当前图库是否支持为准 |

---

## 八、外部参考

| 用途 | URL |
|------|-----|
| 富结果测试 | [Rich Results Test](https://search.google.com/test/rich-results) |
| Schema 校验 | [Schema Markup Validator](https://validator.schema.org/) |
| Google 结构化数据总览 | [Structured data documentation](https://developers.google.com/search/docs/appearance/structured-data) |
| 富结果类型图库 | [Search Gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) |
| 论坛（通用） | [finalround-community-forum.md](../community/finalround-community-forum.md) §6 |

---

## 九、自检

| 检查项 | 说明 |
|--------|------|
| 与 DOM 一致 | 无「仅 JSON-LD」的 FAQ/价格（§一 · 原则 2） |
| 图片与实体 | 博客 **image**（§二）；Logo、缩略图、截图与页面对齐 |
| 结构干净 | 无单节点混装整段视频 + FAQ |
| 面包屑 | 若有 UI 面包屑，则 BreadcrumbList 与路径、绝对 URL、`position` 一致（§七 · 7.2） |
| Review 文 | `Review` / `FAQPage` 与正文、可见 FAQ 一致（§七 · 7.3） |
| 发布后 | 抽测 [Rich Results Test](https://search.google.com/test/rich-results) |

任务跟踪：[finalround-project-tasks.md](../finalround-project-tasks.md)

---

## 文档维护

增改本文时遵循 [文档优化指导](../../../通用知识库/元文档-通用文档规范.md)：**主题一致**（仅 Schema/JSON-LD）、**去重**（与 §四/§七 交叉处用「见 §×」替代重复段落）、**互链**（关联文档见文首）。协作者向导读物见 [finalround.md](../finalround.md) §文档互引，避免在本文重复粘贴非技术摘要。

---

*最后更新：2026-05-13（可信度核查：移除不存在的内容概览引用、修复 finalround.md 路径为 ../）*