# Article Schema（structured data）最佳实践

本文档定义 **Article Schema**（Article 结构化数据）的规范，适用于 Tools、SEO、Marketing、Insights 等所有文章页面。

**参考**：content-rules、[section-seo](./section-seo.md)、[template-bloglayout](../templates/template-bloglayout.md)、[technical](../technical/README.md)

---

## 一、定位与作用

**Article Schema** 是文章类页面的核心结构化数据，用于：

- **富媒体搜索结果**：触发文章富结果、新闻轮播、知识卡片
- **AI Overview 可见性**：结构完整、质量高的 Schema 有助于被 Google AI Overviews 引用
- **搜索引擎理解**：明确页面类型、作者、发布时间、修改时间

**与 BlogLayout 的关系**：BlogLayout 提供 title、excerpt、publishDate、modifiedDate、author 等，Article Schema 应由 BlogLayout 或页面组件统一生成，确保与页面可见内容一致。

---

## 二、类型选择

| 类型 | 适用场景 | 说明 |
|------|----------|------|
| **Article** | 通用文章 | 博客、工具推荐、指南类内容 |
| **BlogPosting** | 博客文章 | Article 的子类型，更具体 |
| **NewsArticle** | 新闻 | 时效性强的新闻内容 |

**Alignify 建议**：Tools、SEO、Marketing 页面使用 **Article** 或 **BlogPosting**；新闻类内容使用 **NewsArticle**。

---

## 三、必需与推荐属性

### 3.1 Google 必需属性

| 属性 | 类型 | 说明 |
|------|------|------|
| **headline** | string | 标题，建议 ≤110 字符 |
| **image** | ImageObject 或 URL | 至少一张图片，建议 ≥1200px 宽，多比例（16:9、4:3、1:1） |
| **datePublished** | ISO 8601 | 发布日期 |
| **author** | Person 或 Organization | 必须包含 name |
| **publisher** | Organization | 必须包含 name 和 logo |

### 3.2 推荐属性

| 属性 | 类型 | 说明 |
|------|------|------|
| **dateModified** | ISO 8601 | 修改日期，内容更新时需同步 |
| **description** | string | 摘要，与 excerpt 对应 |
| **mainEntityOfPage** | URL | 页面 canonical URL |

### 3.3 可选增强属性

| 属性 | 说明 |
|------|------|
| **wordCount** | 字数，有助于 AI 理解内容深度 |
| **timeRequired** | 阅读时间（ISO 8601 如 PT8M） |
| **articleSection** | 文章分类 |
| **keywords** | 关键词（可选） |

---

## 四、最佳实践（网络研究汇总）

### 4.1 Search Engine Land 研究（2025）

**实验**：三页对比（完整 Schema、残缺 Schema、无 Schema）

**结论**：
- 仅**完整 Schema** 页面出现在 AI Overview 且有机排名最佳（最高 rank 3）
- 残缺 Schema 页面排名但未出现在 AI Overview
- 无 Schema 页面未被索引

**完整 Schema 应包含**：完整 Article、FAQ、BreadcrumbList、正确日期格式、author、publisher、教育级别、相关主题、字数、阅读时间。

**参考**：[Schema and AI Overviews: Does structured data improve visibility?](https://searchengineland.com/schema-ai-overviews-structured-data-visibility-462353)

### 4.2 日期格式

- 使用 **ISO 8601**：`2026-02-11` 或 `2026-02-11T08:00:00Z`
- 错误格式（如 `2026年2月11日`）会导致 Schema 无效

### 4.3 图片要求

- 至少一张图片，属于文章内容
- 建议 ≥1200px 宽
- 可提供多尺寸（16:9、4:3、1:1）以适配不同展示场景

### 4.4 Publisher 与 Author

- **publisher**：Organization 类型，包含 `name`、`logo`（ImageObject，含 url、width、height）
- **author**：Person 或 Organization，含 `name`；可用 `@id` 引用全局 Organization/Person 避免重复

### 4.5 Schema 一致性

- **Schema 内容必须与页面可见内容一致**
- headline 与 H1 对应；description 与 excerpt 对应；datePublished/dateModified 与页面显示日期一致

---

## 五、实现规范

### 5.1 生成位置

- **推荐**：在 BlogLayout 中根据 props（title、excerpt、publishDate、modifiedDate、author、pageUrl）自动生成 Article Schema
- 

### 5.2 与 BlogLayout 字段对应

| BlogLayout props | Article Schema 属性 |
|------------------|---------------------|
| title | headline |
| excerpt | description |
| publishDate | datePublished |
| modifiedDate | dateModified |
| author | author.name |
| pageUrl | mainEntityOfPage、url |
| readTime | timeRequired（需转换为 PTxM 格式） |

### 5.3 图片

- 若页面无特色图，可使用站点默认 og-image 或首张 BestTools 图片
- 图片 URL 需为绝对路径

### 5.4 与 FAQ、HowTo、Breadcrumb 的配合

- 同一页面可同时包含 Article、FAQPage、HowTo、BreadcrumbList
- 避免重复声明相同字段（如 headline 仅在 Article 中）

---

## 六、检查清单

- [ ] headline 与 H1 一致
- [ ] datePublished、dateModified 格式正确（ISO 8601）
- [ ] author 含 name
- [ ] publisher 含 name 与 logo
- [ ] image 至少一张，URL 可访问
- [ ] description 与 excerpt 一致
- [ ] mainEntityOfPage 或 url 为 canonical URL
- [ ] 使用 [Google Rich Results Test](https://search.google.com/test/rich-results) 验证
- [ ] 内容修改需同步更新 dateModified

---

## 七、参考文档

| 文档 | 说明 |
|------|------|
| [Google Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article) | 官方规范 |
| [Schema.org Article](https://schema.org/Article) | 类型定义 |
| [Search Engine Land: Schema and AI Overviews](https://searchengineland.com/schema-ai-overviews-structured-data-visibility-462353) | 实验研究 |
| [technical-optimization-plan](../technical/technical-optimization-plan.md) | 技术优化方案：Sitemap/Feed/IndexNow 数据统一 |
