# knowledgehub / seo · SEO 知识块分册

本目录存放**搜索引擎优化（SEO）**相关的非线性知识块：爬取、收录、SERP、on-page、技术实现与内容策略等**问题域笔记**。**文件名与站内 `slug` 对齐的速查**：[README.md](../../../README.md) §十一（命名规范）。

---

## 与 [`knowledgehub/tools/`](../tools/README.md)、与 Tools 的关系

| 位置 | 用途 |
|------|------|
| **`knowledge/tools/`** | 与 **`src/data/tools-pages-config.ts`** 中 **`slug` 同名**的 `*.md` 知识块，便于与 **`/tools/[slug]`**、`product/alignify-keywords-tools.md` 对照（如 [`tools/geo.md`](../tools/search-geo/geo.md)、[`tools/note-taker.md`](../tools/productivity/note-taker.md)）。 |
| **`knowledge/seo/`（本目录）** | **不绑定** Tools slug 的 SEO 专册；**已对应站上长文**的条目，文件名 **与 `content/seo/*/[slug].md` 的 `slug` 段同名**（kebab-case），便于与 **`/seo/[slug]`** 对照；尚无正式页的主题可暂用描述性文件名，上线后改为 slug 同名。**不要求**在 `tools-pages-config` 中存在对应项。 |
| **`skills/ops/`** | 发布后 SEO 运维（sitemap、IndexNow、GSC）；本目录为**网摘与概念整理**，二者互补。 |
| **`skills/create-article/rules/`** | 文章创作与 section 写作规范 SSOT。 |

**边界提示**：**GEO / AEO / LLMO** 等「生成式答案可见度」若需与 Tools 页 **`geo`** 对齐，知识块正文仍放在 [`tools/geo.md`](../tools/search-geo/geo.md)，避免同一主题在两条路径重复维护。本目录侧重**经典 Web 搜索**与站内 technical SEO 工作流相关的笔记。

**正式文章创作**：[`skills/create-article/SKILL.md`](../../skills/create-article/SKILL.md)

---

## 文档结构

新建 `*.md` 时，章节骨架与文首声明沿用 [`../README.md`](../README.md) 中「知识块文档结构」；若某篇**无** Tools 对照，可省略「站内对照」「Tools 关键词与 slug 映射」两行，改为：

- `**规范对照**：…`（链到 [`skills/create-article/rules/meta.md`](../../skills/create-article/rules/meta.md) 或 [`skills/ops/`](../../skills/ops/)，按需）

---

## 文件清单（38 个，按站内分类）

### 入门与学习

| 文档 | 状态 | 主题 |
|------|------|------|
| [learn-seo.md](./learn-seo.md) | ✅ 完整 | 如何学习 SEO：路径、信源分层与资源索引 |
| [how-search-engine-works.md](./how-search-engine-works.md) | ✅ 完整 | 搜索引擎三阶段工作原理：爬取、索引、结果呈现 |
| [search-engine.md](../tools/search-geo/search-engine.md) | 🔲 待补充 | 搜索引擎类型与市场份额 |
| [local-search-engines.md](./local-search-engines.md) | ✅ 完整 | 本地化与特色搜索引擎：区域引擎与垂直品类 |
| [glossary.md](./glossary.md) | 🔲 待补充 | SEO 术语表 |
| [checklist.md](./checklist.md) | ✅ 完整 | SEO Checklist（技术 + On-page + 发布前） |

### 网站架构与导航

| 文档 | 状态 | 主题 |
|------|------|------|
| [website-structure.md](./website-structure.md) | 🔲 待补充 | 网站结构与信息架构 |
| [url-optimization.md](./url-optimization.md) | 🔲 待补充 | URL 优化、规范化 |
| [breadcrumbs.md](./breadcrumbs.md) | 🔲 待补充 | 面包屑导航 |
| [navigation-menu.md](./navigation-menu.md) | 🔲 待补充 | 导航菜单 |
| [subdomain-vs-subfolder.md](./subdomain-vs-subfolder.md) | 🔲 待补充 | 子域 vs 子目录 |
| [domain.md](./domain.md) | ✅ 完整 | 域名 SEO 与 AI 产品域名策略：.ai vs .com vs .io 选型、精品域名市场、品牌保护 |
| [new-domains-tld.md](./new-domains-tld.md) | 🔲 待补充 | 新顶级域名 |

### 技术：抓取、索引与渲染

| 文档 | 状态 | 主题 |
|------|------|------|
| [crawler.md](./crawler.md) | ✅ 完整 | 爬虫全网摘：搜索引擎/AI/Agent/第三方/恶意，UA 表与治理 |
| [sitemap.md](./sitemap.md) | 🔲 待补充 | XML 站点地图 |
| [robots-txt.md](./robots-txt.md) | 🔲 待补充 | Robots.txt 爬虫规则 |
| [website-indexing.md](./website-indexing.md) | 🔲 待补充 | 网站索引 |
| [website-rendering.md](./website-rendering.md) | 🔲 待补充 | 网站渲染（SSR/CSR/JS SEO） |
| [redirect-chain.md](./redirect-chain.md) | 🔲 待补充 | 重定向链 |
| [submit-website.md](./submit-website.md) | 🔲 待补充 | 提交网站到搜索引擎 |

### On-page 与标记

| 文档 | 状态 | 主题 |
|------|------|------|
| [meta-tag.md](./meta-tag.md) | 🔲 待补充 | Meta 标签（title/meta description） |
| [html-tag.md](./html-tag.md) | 🔲 待补充 | HTML 语义标签 |
| [html-a-tag.md](./html-a-tag.md) | 🔲 待补充 | HTML a 标签与链接属性 |
| [schema.md](./schema.md) | 🔲 待补充 | 结构化数据与 Schema 标记 |

### 链接：内链、外链与 SERP

| 文档 | 状态 | 主题 |
|------|------|------|
| [internal-links.md](./internal-links.md) | 🔲 待补充 | 站内链接策略 |
| [link-building.md](./link-building.md) | 🔲 待补充 | 外链建设 |
| [external-links.md](./external-links.md) | 🔲 待补充 | 出站链接 SEO |
| [serp.md](./serp.md) | 🔲 待补充 | SERP 特性与富结果 |

### 内容与规模化

| 文档 | 状态 | 主题 |
|------|------|------|
| [create-blog.md](./create-blog.md) | 🔲 待补充 | 创建博客 |
| [category-pages.md](./category-pages.md) | 🔲 待补充 | 分类页 SEO |
| [programmatic-seo.md](./programmatic-seo.md) | 🔲 待补充 | 程序化 SEO |
| [landing-page.md](./landing-page.md) | 🔲 待补充 | 着陆页 SEO |

### 流量、测量与诊断

| 文档 | 状态 | 主题 |
|------|------|------|
| [dark-traffic.md](./dark-traffic.md) | ✅ 完整 | 无法归因流量（暗流量）：Direct 桶成因与治理 |
| [search-and-traffic-definitions.md](./search-and-traffic-definitions.md) | ✅ 完整 | 搜索与流量定义：GA4/GSC 指标、仪器偏差 |
| [website-traffic.md](./website-traffic.md) | 🔲 待补充 | 网站流量分析与渠道归因 |
| [branded-queries-filter-google-search-console.md](./branded-queries-filter-google-search-console.md) | 🔲 待补充 | GSC 品牌词过滤 |
| [google-tag-manager.md](./google-tag-manager.md) | 🔲 待补充 | Google Tag Manager |

### 工具盘点

| 文档 | 状态 | 主题 |
|------|------|------|
| [best-tools.md](./best-tools.md) | ✅ 完整 | SEO 工具谱系与选型：类目心智模型、工具栈 |

---

共 38 个文件，其中 9 篇完整、29 篇待补充。

- 全站 SEO 规范入口：[section-seo.md](../../skills/create-article/rules/meta.md)
- Technical SEO 索引：[technical/README.md](../../skills/ops/README.md)
- 关键词总表：[alignify-keywords.md](../../keywords/alignify-keywords.md) · [alignify-keywords-seo.md](../../keywords/alignify-keywords-seo.md)
- 全站知识块总说明：[knowledgehub/README.md](../README.md)

---



---

## SEO 页面 References 审计（2026-05-20）

全站 76 个 SEO 页面（38 ZH + 38 EN）的 `references` 块审计结果：

| 状态 | 数量 | 说明 |
|------|------|------|
| ✅ 完整 | 4 | `search-engine` (ZH+EN, 各 13 条), `local-search-engines` (ZH+EN, 各 8 条) |
| ❌ 无 `references` 块 | 38 | ZH 19 篇 + EN 19 篇，包含 `best-tools`, `checklist`, `create-blog`, `domain`, `external-links`, `glossary`, `how-search-engine-works`, `internal-links`, `landing-page`, `learn-seo`, `link-building`, `redirect-chain`, `robots-txt`, `submit-website`, `website-indexing`, `website-structure`, `website-traffic`，及部分仅有单语的 `branded-queries-filter`, `new-domains-tld`, `serp` |
| ❌ 块存在但 items 全空 | 34 | ZH 15 篇 + EN 19 篇，包括 `crawler`(9空), `schema`(7空), `meta-tag`, `dark-traffic`, `website-rendering`, `sitemap`, `breadcrumbs`, `category-pages`, `google-tag-manager`, `html-a-tag`, `html-tag`, `navigation-menu`, `programmatic-seo`, `subdomain-vs-subfolder`, `url-optimization` 等 |

**优先级建议**：第一批（高流量）：`learn-seo`, `how-search-engine-works`, `website-structure`, `crawler`, `schema`, `sitemap`, `meta-tag`；第二批（中流量）：`internal-links`, `link-building`, `serp`, `robots-txt`, `url-optimization`, `breadcrumbs`, `programmatic-seo`；第三批：其余占位页/工具页。

暂缓补充，待知识块内容完成后统一处理。


---

*本 README 随 `knowledgehub/seo` 约定变更而更新。*
