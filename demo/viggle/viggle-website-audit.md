# Viggle Website Audit

> 基于 seo-strategy 工作流、[Technical SEO Audit 2026](https://www.digitalapplied.com/blog/technical-seo-audit-2026-50-point-checklist) 及相关 skills（site-crawlability、robots、sitemap、canonical、indexing、schema、title、meta-description、heading、internal-links、image-optimization、open-graph、favicon）  
> 关联：[viggle.md](./viggle.md) | [viggle-keywords.md](./viggle-keywords.md) | [viggle-page-tools.md](./viggle-page-tools.md)

---

## 1. 审计范围

| 站点 | URL | 说明 |
|------|-----|------|
| **viggle.ai** | https://viggle.ai/ | 主站；Cloudflare 保护 |
| **Programmatic SEO 落地页** | 待建 /tools/、/vs/、/for/、/glossary/、/blog/ | 见 [viggle.md](./viggle.md) Section 10 |

**审计顺序**（遵循 seo-strategy）：Technical → On-Page → Content → Off-Page

---

## 2. Pillar 1：Crawlability（可抓取性）

> 参考 skill：**site-crawlability**、**robots-txt**、**xml-sitemap**

| # | Audit Item | 检查方法 | 状态 |
|---|------------|----------|------|
| 1 | robots.txt 语法正确，未阻止 CSS/JS/图片 | 直接访问 robots.txt；GSC robots.txt Tester | ⬜ |
| 2 | XML sitemap 已提交、有效、仅含可索引 URL | 访问 /sitemap.xml；GSC Sitemaps | ⬜ |
| 3 | sitemap lastmod 准确，反映实际内容变更 | 检查 lastmod 是否随内容更新 | ⬜ |
| 4 | 内链使用可抓取 `<a href>`，非 JS onclick | Screaming Frog JS 模式 | ⬜ |
| 5 | 无 crawl trap（faceted nav、session ID、日历） | Screaming Frog；robots Disallow 或 noindex | ⬜ |
| 6 | 重要页面 3 次点击内可达 | Screaming Frog 抓取深度 | ⬜ |
| 7 | 无 orphan 页（重要页有内链指向） | CMS 导出 vs Screaming Frog 抓取对比 | ⬜ |
| 8 | 服务器响应 <200ms（Googlebot） | GSC Crawl Stats；Server-Timing | ⬜ |
| 9 | 重定向链 ≤1 跳；无循环 | Screaming Frog Redirect 报告 | ⬜ |
| 10 | Crawl Stats 稳定或上升 | GSC > Settings > Crawl Stats | ⬜ |

**Viggle 注意**：viggle.ai/sitemap.xml 受 Cloudflare 保护，自动化工具可能无法访问；需浏览器或 GSC 验证。

---

## 3. Pillar 2：Indexing（索引）

> 参考 skill：**canonical-tag**、**indexing**、**page-metadata**

| # | Audit Item | 检查方法 | 状态 |
|---|------------|----------|------|
| 1 | Canonical 自引用或指向正确 canonical URL | Screaming Frog Canonical 报告 | ⬜ |
| 2 | 应索引页面无 noindex | Screaming Frog X-Robots-Tag、meta robots | ⬜ |
| 3 | Hreflang 存在、格式正确、完全互指 | Screaming Frog hreflang 报告 | ⬜ |
| 4 | 多语言站有 x-default | 检查 hreflang 配置 | ⬜ |
| 5 | 重复 URL 已合并（www/non-www、HTTP/HTTPS、尾斜杠） | 301 链、canonical 检查 | ⬜ |
| 6 | 分页处理正确（rel=next/prev 已弃用） | canonical 或 noindex 策略 | ⬜ |
| 7 | GSC Coverage 无 soft 404 | GSC Index Coverage | ⬜ |
| 8 | 无「Crawled but not indexed」超 90 天 | GSC Excluded | ⬜ |
| 9 | 内链统一使用 canonical URL 格式 | Screaming Frog 内链协议/格式 | ⬜ |
| 10 | URL 结构一致、小写、连字符 | 无 /Product 与 /product 混用 | ⬜ |

**Viggle 注意**：若未来做多语言，需配置 hreflang/x-default。

---

## 4. Pillar 3：Performance（性能）

> 参考 skill：**image-optimization**；工具：PageSpeed Insights、Chrome DevTools

| # | Audit Item | 检查方法 | 状态 |
|---|------------|----------|------|
| 1 | INP <200ms（75th 百分位） | PageSpeed Insights CrUX | ⬜ |
| 2 | LCP <2.5s（75th 百分位） | PageSpeed Insights CrUX | ⬜ |
| 3 | CLS <0.1（75th 百分位） | PageSpeed Insights CrUX | ⬜ |
| 4 | TTFB <800ms | PageSpeed Insights；GSC Crawl Stats | ⬜ |
| 5 | 图片压缩、WebP/AVIF、width/height | Lighthouse；Squoosh/Sharp | ⬜ |
| 6 | 无 render-blocking 脚本/样式 | Lighthouse | ⬜ |
| 7 | 首屏总重 <1MB（压缩后） | Chrome DevTools Network | ⬜ |
| 8 | 第三方脚本 async/defer，不阻塞 INP | Chrome DevTools Performance | ⬜ |
| 9 | 无 Long Tasks（>50ms 阻塞主线程） | Chrome DevTools Performance | ⬜ |
| 10 | 移动端性能与桌面相当 | PageSpeed 移动端；3G 节流测试 | ⬜ |

---

## 5. Pillar 4：Structured Data（结构化数据）

> 参考 skill：**schema-markup**

| # | Audit Item | 检查方法 | 状态 |
|---|------------|----------|------|
| 1 | 所有 schema 在 Rich Results Test 无错误 | richresults.google.com | ⬜ |
| 2 | Blog/新闻页有 Article/BlogPosting schema | 必填：headline、datePublished、dateModified、author、image、publisher | ⬜ |
| 3 | BreadcrumbList 与可见面包屑一致 | 顺序、position、name、item | ⬜ |
| 4 | Product schema 含必填属性（name、image、description、offers） | 产品页 | ⬜ |
| 5 | 首页有 Organization schema（name、url、logo、contactPoint、sameAs） | 首页 | ⬜ |
| 6 | 首页有 WebSite + SearchAction（Sitelinks Search Box） | 品牌搜索 | ⬜ |
| 7 | 教程类有 HowTo schema | 步骤、name、text | ⬜ |
| 8 | 无隐藏 schema（须与可见内容一致） | 人工检查 | ⬜ |
| 9 | 使用 JSON-LD，置于 head | View Source | ⬜ |
| 10 | GSC Enhancements 无错误 | GSC Rich Results | ⬜ |

**Viggle 适用**：首页 Organization、WebSite；/tools/ 页 WebPage/SoftwareApplication；/blog/ Article。

---

## 6. Pillar 5：JavaScript & Rendering（JS 渲染）

> 工具：GSC URL Inspection、Chrome DevTools

| # | Audit Item | 检查方法 | 状态 |
|---|------------|----------|------|
| 1 | 关键内容（H、正文、内链）在 raw HTML 中，不依赖 JS | 禁用 JS 后刷新 | ⬜ |
| 2 | Schema 在服务端响应中，非 JS 注入 | URL Inspection 渲染截图 | ⬜ |
| 3 | 导航链接为标准 `<a href>`，非 JS router | View Source 检查 | ⬜ |
| 4 | 无限滚动有分页 URL 或首屏内容在 HTML | 检查分页/SSR | ⬜ |
| 5 | 懒加载图片用 loading=lazy，src 在 HTML 中 | 非 data-src 动态替换 | ⬜ |
| 6 | CSR 页有 SSR/SSG/动态渲染 fallback | 检查渲染策略 | ⬜ |
| 7 | 无 hydration 错误 | 浏览器 Console | ⬜ |
| 8 | Meta（title、description、robots、canonical）在 raw HTML | View Source | ⬜ |
| 9 | JS bundle 优化（code splitting、tree shaking） | Bundle Analyzer；<150KB/路由 | ⬜ |
| 10 | URL Inspection 渲染截图与用户所见一致 | GSC URL Inspection | ⬜ |

---

## 7. On-Page 审计项

> 参考 skills：**title-tag**、**meta-description**、**heading-structure**、**internal-links**、**image-optimization**、**open-graph**、**favicon**

| 类别 | Audit Item | 参考 Skill | 状态 |
|------|------------|------------|------|
| **Title** | 每页唯一；50–60 字符；主关键词靠前 | title-tag | ⬜ |
| **Meta Description** | 每页唯一；150–160 字符；含 CTA | meta-description | ⬜ |
| **Heading** | 单 H1；H2–H6 层级正确；无跳级 | heading-structure | ⬜ |
| **Internal Links** | 描述性锚文本；无 orphan；hub-to-spoke | internal-links | ⬜ |
| **Image** | Alt 文本；WebP/AVIF；width/height；lazy loading | image-optimization | ⬜ |
| **Open Graph** | og:title、og:description、og:image、og:url | open-graph | ⬜ |
| **Twitter Cards** | twitter:card、twitter:title、twitter:image | twitter-cards | ⬜ |
| **Favicon** | 16、32、180、192、512 等尺寸；Apple Touch Icon | favicon | ⬜ |
| **Viewport** | width=device-width, initial-scale=1 | page-metadata | ⬜ |
| **Charset** | UTF-8 | page-metadata | ⬜ |

---

## 8. 其他审计项

| 类别 | Audit Item | 说明 | 状态 |
|------|------------|------|------|
| **安全** | HTTPS 全站 | 无混合内容 | ⬜ |
| **移动** | 移动友好 | GSC Mobile Usability | ⬜ |
| **404** | 自定义 404 页 | 用户友好、含内链 | ⬜ |
| **IndexNow** | 新/更新 URL 通知 | Bing 等快速索引 | ⬜ |
| **多语言** | 若做多语言 | canonical、hreflang | ⬜ |

---

## 9. 审计工具

| 工具 | 用途 |
|------|------|
| **Google Search Console** | Index Coverage、Crawl Stats、URL Inspection、Core Web Vitals、Enhancements |
| **Screaming Frog** | 全站抓取、robots、sitemap、canonical、hreflang、redirect |
| **PageSpeed Insights** | Core Web Vitals、Lighthouse、CrUX |
| **Chrome DevTools** | 禁用 JS、Performance、Coverage、Network |
| **Rich Results Test** | Schema 验证 |

---

## 10. 优先级矩阵

| 优先级 | 含义 | 示例 |
|--------|------|------|
| **P0** | 阻塞项，优先修复 | robots 阻止 CSS/JS、canonical 错误、索引失败 |
| **P1** | 核心项，尽快完成 | Title、meta、schema、sitemap、内链 |
| **P2** | 重要项，非紧急 | Open Graph、Twitter Cards、IndexNow |
| **P3** | 优化项 | Rich results、sitelinks |

---

## 11. 文档导航

| 文档 | 用途 |
|------|------|
| [viggle.md](./viggle.md) | 产品概览、SEO 落地页体系 |
| [viggle-keywords.md](./viggle-keywords.md) | 关键词、URL 模式 |
| [viggle-page-tools.md](./viggle-page-tools.md) | /tools/ 页规范（审计时对照） |
