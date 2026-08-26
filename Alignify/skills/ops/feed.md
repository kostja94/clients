# RSS Feed 生成说明

本文档说明 Alignify 站点的 RSS Feed 实现与业界最佳实践。

**实现位置**：`app/feed/route.ts`

**访问路径**：`/feed`

**参考**：[RSS 2.0 规范](https://www.rssboard.org/rss-specification)、[RSS Best Practices Profile](https://www.rssboard.org/rss-profile)、[Google Webmaster RSS/Atom 最佳实践](https://webmasters.googleblog.com/2014/10/best-practices-for-xml-sitemaps-rssatom.html)

---

## 一、功能说明

- **格式**：RSS 2.0 + Atom 自引用（`atom:link rel="self"`）
- **内容**：SEO、增长策略、AI 工具、活动、客户案例等文章
- **数量**：取前 50 篇
- **排序**：按 `modifiedDate` 降序

---

## 二、业界最佳实践（RSS 2.0）

### 2.1 Channel 必选元素

| 元素 | 说明 | 当前实现 |
|------|------|----------|
| title | 频道名称 | ✓ |
| link | 站点 URL（绝对） | ✓ |
| description | 频道描述 | ✓ |

### 2.2 推荐元素

| 元素 | 说明 | 当前实现 |
|------|------|----------|
| atom:link rel="self" | 自引用，便于聚合器识别 | ✓ |
| language | 语言代码（如 en-us） | ✓ |
| lastBuildDate | 最后构建时间，RFC 822 格式 | ✓ |
| docs | 指向 RSS 规范文档 | ✗ 建议添加 |
| ttl | 缓存提示（分钟），减少轮询 | ✗ 可选 |
| managingEditor / webMaster | 联系邮箱 | ✓ |

### 2.3 Item 必选/推荐

| 元素 | 说明 | 当前实现 |
|------|------|----------|
| title | 标题 | ✓ |
| description | 描述（至少 title 或 description 其一） | ✓ |
| link | 文章 URL（绝对） | ✓ |
| guid | 全局唯一标识，建议用 permalink | ✓ 使用完整 URL |
| pubDate | 发布时间，RFC 822 格式 | ✓ |

### 2.4 技术规范

| 项目 | 规范 |
|------|------|
| **字符编码** | UTF-8 |
| **URL** | 必须为绝对 URL（含 https://） |
| **日期格式** | RFC 822，如 `Mon, 15 Oct 2007 14:10:00 GMT` |
| **特殊字符** | title/description 中 `&`、`<` 需转义或使用 CDATA |
| **Cache-Control** | 建议设置，减少服务端压力 |

### 2.5 Google / 聚合器建议

- **Cache-Control**：合理设置 max-age，避免聚合器频繁请求
- **Conditional GET**：可选支持 If-Modified-Since、ETag 进一步节省带宽
- **gzip 压缩**：Next.js 通常自动处理

---

## 三、当前实现与数据结构

### 3.1 数据来源

文章列表在 `getArticles()` 内**硬编码**维护，分为：

- `seoArticles`：SEO 指南
- `growthArticles`：增长策略、Marketing、Insights
- `aiToolsArticles`：AI 工具
- `eventsArticles`：活动
- `customerStoriesArticles`：客户案例

**问题**：与 Sitemap、Explore、site-pages-config 存在数据重复，新增页面需多处手动维护。

### 3.2 每篇文章需包含

| 字段 | 说明 |
|------|------|
| title | 文章标题 |
| url | 相对路径（如 `/seo/sitemap`），输出时拼接 baseUrl |
| description | 简短描述 |
| modifiedDate | 修改日期，格式 `YYYY-MM-DD` |

---

## 四、输出格式

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Alignify - AI/SaaS Growth &amp; Marketing</title>
    <description>...</description>
    <link>https://alignify.co</link>
    <atom:link href="https://alignify.co/feed" rel="self" type="application/rss+xml" />
    <language>en-us</language>
    <lastBuildDate>...</lastBuildDate>
    <item>
      <title><![CDATA[...]]></title>
      <description><![CDATA[...]]></description>
      <link>https://alignify.co/seo/sitemap</link>
      <guid>https://alignify.co/seo/sitemap</guid>
      <pubDate>Mon, 11 Feb 2025 00:00:00 GMT</pubDate>
    </item>
  </channel>
</rss>
```

---

## 五、缓存与性能

- **Cache-Control**：`public, max-age=3600, s-maxage=3600`（1 小时）
- **动态生成**：每次请求时生成，无静态构建

---

## 六、新文章添加流程

1. 在 `app/feed/route.ts` 的 `getArticles()` 中对应分类数组添加文章
2. 确保 `url`、`title`、`description`、`modifiedDate` 正确

---

## 七、潜在优化

| 优化项 | 说明 | 优先级 |
|--------|------|--------|
| **docs 元素** | 添加 `<docs>https://www.rssboard.org/rss-specification</docs>` | 低 |
| **ttl 元素** | 添加 `<ttl>60</ttl>` 作为缓存提示 | 低 |
| **统一数据源** | 与 site-pages-config、TOOLS_PAGES 共用，自动生成 Feed | 高 |
| **中文 Feed** | 增加 `/zh/feed` 支持中文内容 | 中 |
| **分类标签** | `<category>` 按文章类型区分为 SEO/Marketing/Tools 等 | 低 |
