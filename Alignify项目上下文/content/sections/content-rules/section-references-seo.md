# SEO 文章 References 规则

> **关联**：[section-references.md](./section-references.md)（通用规范）· [section-faq.md](./section-faq.md) · [template-seo.md](../templates/template-seo.md)

**适用范围**：`content/seo/{en,zh}/*.json`（38 页 × 2 locale = 76 个 JSON）。

通用规范（字段结构、展示规则、日期格式）见 [section-references.md](./section-references.md)。本文仅补充 SEO 类目特有的引用策略。

---

## 一、引用定位

SEO 文章的 references 服务于**读者溯源与技术验证**——读者在理解搜索引擎机制后，应能通过引用直达 Google/Bing 官方文档、行业研究或工具实测数据，从而：

- 验证文中技术声明的准确性
- 深入阅读官方规范原文
- 了解行业数据来源与方法论

与 Tools 页面的 references 不同：SEO references 不涉及产品外链、论文引用，以**官方文档 + 行业数据 + 专业媒体**为主。

---

## 二、每页引用数量与结构

| 页面类型 | 最少引用条数 | 建议结构 |
|---------|------------|---------|
| 技术说明类（schema, robots-txt, sitemap 等） | 3 条 | L2 官方文档 ×2 + L4 行业工具/数据 ×1 |
| 指南类（learn-seo, keyword-research, link-building 等） | 3–5 条 | L2 官方 ×1 + L3 专业媒体 ×1–2 + L4 数据 ×1–2 |
| 工具/检查清单类（checklist, best-tools 等） | 3 条 | L2 官方 ×1 + L3 媒体 ×1 + L4 数据 ×1 |
| 学习/资源汇总类（glossary, example-article 等） | 2–3 条 | L2 官方 ×1 + L3/L4 ×1–2 |

**底线**：每条引用必须有 `title` 和 `url`；建议填写 `source` 和 `description`。

---

## 三、SEO 专属来源质量层级

| 层级 | 来源类型 | 适用场景 | 示例 |
|------|---------|---------|------|
| **L2 官方/平台文档** | Google Search Central, Bing Webmaster Guidelines, schema.org, W3C | 引用技术规范、官方指南 | Google 站点地图文档、schema.org 词汇表 |
| **L3 专业媒体** | Search Engine Journal, Search Engine Land, Moz, Ahrefs Blog, Backlinko | 引用行业分析、趋势、策略 | Moz 关键词研究指南、Ahrefs AI Overviews 研究 |
| **L4 行业数据/工具** | StatCounter, Statista, BuiltWith, W3Techs, HTTP Archive | 引用市场规模、份额、采用率 | StatCounter 搜索引擎份额、BuiltWith 技术采用率 |
| **L5 社区/开源** | Stack Overflow 趋势, GitHub SEO 工具, Web Almanac | 引用行业实践、工具实现 | Web Almanac SEO 章节、GitHub sitemap 生成工具 |

**不适用**：L1 学术论文（SEO 属实践学科，极少需要论文引用）。

---

## 四、每页引用方向速查

### 4.1 技术说明类（已有 references，质量较好）

| slug | 建议来源 | 当前状态 |
|------|---------|---------|
| `schema` | schema.org 词汇表、Google 结构化数据指南、Rich Results Test | ✅ 7 条 OK |
| `sitemap` | Google 站点地图文档、sitemaps.org 协议、Bing Webmaster | ✅ 3 条 OK |
| `crawler` | Google 爬虫文档、Cloudflare Radar 爬虫报告、Web Almanac | ✅ OK |
| `robots-txt` | Google robots.txt 规范、RFC 9309、Bing Webmaster | ✅ OK |
| `website-indexing` | Google 索引指南、Google Search Console 文档 | ✅ OK |
| `canonical-url` | Google 规范化指南、RFC 6596、Moz canonical 指南 | ✅ OK |
| `internal-links` | Google 内链最佳实践、Moz 内链指南、Ahrefs 内部链接研究 | ✅ OK |
| `external-links` | Google 外链指南、Moz 外链因素、Ahrefs 外链研究 | ✅ OK |
| `site-structure` | Google URL 结构指南、Moz 网站架构、Web Almanac | ✅ OK |
| `serp` | Google SERP 功能文档、Ahrefs SERP 研究、Moz SERP 分析 | ✅ OK |
| `search-engine` | StatCounter 份额、Statista 趋势、SEJ 行业概览 | ✅ 13 条 OK |
| `local-search-engines` | 各引擎官方页、StatCounter 区域数据、Similarweb | ✅ 8 条 OK |
| `domain` | ICANN、Google 域名指南、Moz 域名权威 | ✅ OK |
| `how-search-engine-works` | Google 搜索运作指南、Bing Webmaster 指南 | ❌ MISSING |
| `html-a-tag` | W3C HTML 规范、MDN `<a>` 文档、Google 链接最佳实践 | ⚠️ 仅 2 条 |
| `branded-queries-filter-google-search-console` | GSC 过滤文档、Search Engine Land 教程 | ❌ MISSING |
| `submit-website` | GSC URL 提交、Bing Webmaster URL 提交 | ❌ MISSING |
| `redirect-chain` | Google 重定向指南、MDN HTTP 重定向、Moz 重定向 SEO | ❌ MISSING |

### 4.2 指南/资源类（多数 MISSING）

| slug | 建议来源 | 当前状态 |
|------|---------|---------|
| `learn-seo` | Google SEO 入门指南、Moz 初学者 SEO 指南、Ahrefs SEO 教程 | ❌ MISSING |
| `keyword-research` | Moz 关键词研究指南、Ahrefs 关键词工具文档、Semrush 关键词类型 | 已指向 marketing 同名页 |
| `link-building` | Google 链接质量指南、Moz 链接建设、Ahrefs 外链研究 | ❌ MISSING |
| `checklist` | Google SEO 检查清单、Bing Webmaster 检查清单 | ❌ MISSING |
| `website-traffic` | Google Analytics 文档、Similarweb 流量数据、StatCounter | ❌ MISSING |
| `landing-page` | Google 着陆页指南、Unbounce 转化报告、HubSpot 着陆页研究 | ❌ MISSING |
| `create-blog` | Google 博客 SEO 指南、HubSpot 博客统计、WordPress SEO 指南 | ❌ MISSING |
| `glossary` | Moz SEO 术语表、Google SEO 词汇表、Search Engine Journal 术语 | ❌ MISSING |
| `new-domains-tld` | ICANN TLD 列表、Google TLD 处理文档 | ⚠️ 仅 2 条（EN） |
| `programmatic-seo` | Google 自动生成内容指南、案例研究（TripAdvisor/Zapier） | ⚠️ 仅 2 条 |
| `subdomain-vs-subfolder` | Google 子域 vs 子目录说明、Moz 案例研究 | ⚠️ 仅 1 条 |
| `best-tools` | G2/TrustRadius SEO 工具分类、Moz 工具推荐 | ❌ MISSING |
| `example-article` | —（示例页面，非正式内容） | ❌ MISSING |

---

## 五、数据字段填写约定（SEO 类目）

| 字段 | SEO 页面约定 |
|------|------------|
| `title` | 采用原文标题或与页面一致的译名。技术文档标题优先保持英文（如 "Learn about sitemaps"），中文页面可在标题中补充中文说明。 |
| `url` | 优先链接到稳定文档地址（Google Developers / schema.org），避免短链或跳转页。 |
| `source` | 填写发布机构的标准名称：`Google Search Central`（不写 "Google"）、`Moz`、`Ahrefs`、`Schema.org`、`Bing Webmaster`。 |
| `date` | 技术文档用 `持续更新`（中文）/ `Updated regularly`（英文）。行业报告/文章填写年份或具体日期。 |
| `description` | 一句话说明引用内容与页面主题的关联（如「Google 官方文档：站点地图格式与提交指南」），不超 60 字。 |

---

## 六、修复优先级

| 优先级 | 页面数 | 问题 | 方式 |
|--------|--------|------|------|
| **P0** | 21+17=38 | references block 完全缺失 | 逐页添加 3 条对口引用 |
| **P1** | 3+4=7 | 仅 1–2 条引用（thin） | 补充到 3+ 条 |
| **P2** | 14+17=31 | 质量可接受 | 逐页检查 URL 可访问性 |

---

## 七、与 Tools References 规则的差异

| 维度 | Tools | SEO |
|------|-------|-----|
| L1 学术论文 | 推荐（技术品类） | 不适用（实践学科） |
| 引用上限 | 无硬上限，建议 ≤8 | 建议 3–5 条 |
| 厂商官方 | L5，需标注来源 | Google/Bing 官方文档属 L2 高优先级 |
| 付费报告目录页 | 谨慎使用（≤1/3） | 一般不使用 |
| 字段要求 | title + url 底线 | 推荐 title + url + source + description |

---

## 八、审计与维护

- **审计脚本**：`D:\项目文档\Alignify项目上下文\scripts\audit-seo-references.py`
- **频率**：新页面发布前检查；存量页面每季度检查 URL 可访问性
- **新增页面**：创建 SEO JSON 时必须包含 `references` block，≥3 条对口引用
