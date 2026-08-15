# Technical SEO 文档

本目录存放 **Technical SEO** 相关实现：爬取、索引、Sitemap、robots、canonical、IndexNow 等。

**项目总索引**：参见 [README.md](../README.md)。

---

## Technical SEO 文档列表

| 文件 | 说明 | 适用场景 |
|------|------|----------|
| [technical-seo-fundamentals.md](./technical-seo-fundamentals.md) | 爬取、规范化与索引全链路 | robots、Canonical、站点结构、内链 |
| [technical-sitemap.md](./technical-sitemap.md) | Sitemap 生成与优化 | 多 Sitemap 结构、lastmod |
| [technical-robots.md](./technical-robots.md) | robots.txt 配置 | 爬虫规则、AI bot 策略、Sitemap 引用 |
| [technical-google-indexing.md](./technical-google-indexing.md) | Google Indexing API 集成 | 自签名 JWT、200 URL/天配额、GitHub Actions |
| [technical-indexnow.md](./technical-indexnow.md) | IndexNow 协议集成 | 部署后提交、批量提交 |
| [technical-ai-search-analytics.md](./technical-ai-search-analytics.md) | AI Search 流量收集 | GA4 追踪 AI 来源、AI Overviews、GSC 过滤 |
| [technical-gsc-api.md](./technical-gsc-api.md) | Search Console API 集成 | 搜索绩效、URL 检查、Sitemap 管理 |
| [technical-gsc-optimization-plan.md](./technical-gsc-optimization-plan.md) | GSC + Bing 双引擎 SEO 监控方案 | 数据存档、CTR 审计、位置滑坡、索引健康、看板 |

---

## 其他技术文档

| 文件 | 说明 | 适用场景 |
|------|------|----------|
| [technical-config-files.md](./technical-config-files.md) | 项目配置文件说明 | 开发环境、配置 |
| [technical-feed.md](./technical-feed.md) | RSS Feed 生成（locale-aware） | Feed 结构、多语言 |
| [technical-component-inventory.md](./technical-component-inventory.md) | 部署仓组件全量清单 | 46 组件的路径/Props/引用关系 |
| [content-json-block-keys.md](./content-json-block-keys.md) | Content JSON Block Key 规范 | ArticleFromJson 渲染要求 |
| [technical-breadcrumb-nav.md](./technical-breadcrumb-nav.md) | 面包屑与 `TOOLS_PAGES` | 新增 Tools slug 时避免重复维护标签 |
| [utm-and-nofollow-rules.md](./utm-and-nofollow-rules.md) | 外链 UTM / nofollow | `src/lib/utils.ts` |
| [code-comment-standards.md](./code-comment-standards.md) | 代码注释规范 | 开发约定 |
| [technical-content-import-architecture.md](./technical-content-import-architecture.md) | 页面内容导入架构 | ArticleFromJson 数据流、category 路由、类型系统 |
| [tldr-quality-enforcement.md](./tldr-quality-enforcement.md) | TL;DR 质量审计 | 内容修复计划 |
| [technical-glossary.md](./technical-glossary.md) | 中文术语对照表（可读版） | 创作中文内容时的术语统一 |
| [technical-glossary.json](./technical-glossary.json) | 中文术语对照表（脚本版） | 脚本批量检查术语一致性 |

---

## 与 docs 其他目录

- **内容规范**：见 [sections](../content/sections/)、[templates](../content/templates/)
- **速查入口**：[section-seo](../content/sections/section-seo.md) 链接至 technical
