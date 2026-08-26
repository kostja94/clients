# Technical SEO：爬取、规范化与索引

爬取（Crawlability）、Canonical（规范化）与索引（Indexing）是搜索引擎发现和理解站点内容的三连环节。本文档合并了原先三个独立文档，统一覆盖全链路。

**参考**：[Google 爬取与索引](https://developers.google.com/search/docs/crawling-indexing)、[Google Canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)、Google Search Console

---

## 一、爬取（Crawlability）

爬取确保搜索引擎能够发现和访问站点内容。

### 1.1 Robots.txt

- **位置**：`public/robots.txt`
- **作用**：指导爬虫哪些路径可抓取、哪些排除
- **要求**：不阻塞重要页面；声明 Sitemap
- 详见 [technical-robots](./robots.md)

### 1.2 X-Robots-Tag

- **位置**：`next.config.js` headers
- **已排除**：`/_next/static/*` 设置 `noindex, nofollow`
- **作用**：防止静态资源被索引

### 1.3 站点结构与内链

- **层级**：重要页面距首页不超过 3 次点击
- **孤儿页**：避免无内链指向的页面
- **内链**：参见内容规范中的内链文档

### 1.4 Middleware 与路由

- Sitemap、API、静态资源路径需排除 i18n 重定向
- 确保爬虫可访问 `/sitemap.xml`、`/robots.txt`
- `middleware.ts` 通过 `.*\\..*` 模式排除带扩展名的静态文件、robots.txt 等

### 1.5 常见问题

| 问题 | 检查 |
|------|------|
| 页面未被抓取 | robots.txt 是否阻塞、是否有内链 |
| 大量 404 | 检查链接、重定向 |
| 爬取预算浪费 | 减少低价值页面、优化 robots |

---

## 二、Canonical（规范化）

Canonical 标签声明页面的首选 URL，避免重复内容导致搜索引擎分散权重。与 hreflang 配合使用，在 `alternates.languages` 中配置 zh、en、x-default。

### 2.1 何时使用

- 多语言页面：每个语言版本有独立 canonical
- 同一内容多个 URL（如带参数、分页）
- 避免自引用错误：canonical 应指向自身或首选版本

### 2.2 Next.js 实现

在 `generateMetadata` 中配置：

```tsx
alternates: {
  canonical: isZh ? "https://alignify.co/zh/seo/page-slug" : "https://alignify.co/seo/page-slug",
  languages: {
    zh: "https://alignify.co/zh/seo/page-slug",
    en: "https://alignify.co/seo/page-slug",
    "x-default": "https://alignify.co/seo/page-slug",
  },
}
```

### 2.3 规则

- 使用绝对 URL（含 `https://`）
- 必须与当前页面 URL 一致，或指向明确的首选版本
- 避免链式 canonical（A→B→C）
- Sitemap 中的 URL 应与 canonical 一致
- IndexNow 提交的 URL 使用 canonical 版本

---

## 三、索引（Indexing）

索引确保页面被搜索引擎收录并出现在搜索结果中。

### 3.1 索引状态检查

- **工具**：Google Search Console「页面」报告
- **状态**：已编入索引、已发现未编入索引、已排除等
- **排查**：移除意外 noindex、检查 robots.txt、解决重复内容

### 3.2 IndexNow

- **作用**：主动通知 Bing 等搜索引擎新页面或更新，加快索引
- **实现**：`scripts/permanent/submit-all-pages-to-indexnow.ts`、`src/lib/indexnow.ts`
- 详见 [technical-indexnow](./indexnow.md)

### 3.3 Sitemap

- **作用**：帮助搜索引擎发现所有可索引 URL
- **提交**：在 Search Console 提交 sitemap URL
- 详见 [technical-sitemap](./sitemap.md)

### 3.4 Noindex 使用

- **场景**：登录页、后台、重复内容页、低价值页（如 `/search?q=...`）
- **实现**：`metadata.robots = { index: false }` 或 X-Robots-Tag
- **注意**：避免对重要页面误设 noindex

### 3.5 Crawled - currently not indexed

Google 已抓取但未编入索引的页面。常见原因与处理：

| 原因 | 处理 |
|------|------|
| 低质量、重复、与主题不符 | 提升内容质量、解决重复、确保 canonical 正确 |
| 静态资源（CSS/JS）被当作页面抓取 | 见 §3.5.1 |
| Feed、分享带参 URL | 通常可忽略；或 noindex、canonical 指向主 URL |
| 重要内容页 | 用 [URL Inspection](https://search.google.com/search-console?action=inspect) 检查，Request indexing |

#### 3.5.1 Next.js / Vercel：`/_next/static/css/*.css?dpl=*`

Vercel 每次部署为静态资源附加唯一 `dpl=` 参数，产生大量「已抓取但未索引」URL。

**结论：不宜在 robots.txt 中禁止 CSS**

- **不要** 整体禁止 `/_next/`，否则浏览器无法加载 CSS/JS，影响渲染和移动端适配
- **不要** 禁止 `/_next/static/css/` 或带 `?dpl=` 的请求：Google 需要抓取 CSS 才能渲染页面
- 静态资源出现在「Crawled - currently not indexed」是**预期且正常**的，对 SEO 无实质影响
- **建议**：保持 robots.txt 允许 `/_next/`，接受静态资源在 GSC 中显示为已抓取未索引

#### 3.5.2 GSC Coverage 常见 Issue 类型

| Issue | 含义 | 处理 |
|-------|------|------|
| Crawled - currently not indexed | 已抓取但未索引 | 见上文 |
| Excluded by «noindex» tag | 被 noindex 排除 | 若为预期则忽略 |
| Redirect / 404 | 重定向或不存在 | 修复 URL 或重定向 |
| Duplicate / Canonical | 重复内容 | 通常正常，保留 canonical 指向 |

### 3.6 Google Indexing API

**当前状态**：暂未通过 Indexing API 主动提交（网络需代理）。现有方案（IndexNow + Sitemap + Search Console）已足够。

适用场景：JobPosting、BroadcastEvent 等含结构化数据的页面。配额默认 200 URL/天，需服务账号 + Search Console 所有者验证。

实现指南参见 [technical-google-indexing](./google-indexing.md)。

---

## 四、参考文档

| 文档 | 说明 |
|------|------|
| [Page indexing report](https://support.google.com/webmasters/answer/7440203) | GSC 页面索引报告官方说明 |
| [Crawled – Currently not indexed 修复](https://searchengineland.com/fix-crawled-currently-not-indexed-error-google-search-console-445344) | Search Engine Land 修复指南 |
| [technical-robots](./robots.md) | 本站 robots 配置 |
| [technical-sitemap](./sitemap.md) | Sitemap 配置 |
| [technical-indexnow](./indexnow.md) | IndexNow 集成 |
