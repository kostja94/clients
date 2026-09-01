## Article Brief — submit-website

**SSOT（双源 · 不拆文）**:
- `E:\个人知识库\数据分析-Analytics\GSC\网站提交与验证-GSC-Submit-Website.md`
- `E:\个人知识库\数据分析-Analytics\GSC\社媒平台属性-GSC-Platform-Properties.md`

**QualityTier**: flagship  
**ArticleType**: seo-guide（**存量** `/seo/submit-website` · `content/seo/` · **不重迁 URL**）  
**Gate A**: KEEP（2026-09-01 知识块驱动 **完整重构**）  
**Copy mode**: M1  
**BatchCount**: 1 — submit-website（Outline 3.5 / Cross 5.5 → N/A）

**User confirmed**（2026-09-01）:
- Website + Platform **合并单篇**，不另开 `gsc-platform-properties`
- 存量 URL 保留；publishDate `2025-02-13` 不改
- 允许完整重构正文结构
- **2026-09-01 构建完成**：ZH/EN 正文 + tldr/faq/references/seo-meta 已写入部署仓

**Primary keyword**:
- ZH: 提交网站到 Google / Google Search Console 验证 / GSC 社媒平台属性
- EN: submit website to Google Search Console / GSC platform properties / add property GSC

**Search intent**: Tutorial（Website 验证 + Platform OAuth）+ Definition（三种 property 辨析）

**One-line thesis**: GSC 提交 = 按资产类型选对 **Domain、URL-prefix 或 Platform** property 并完成对应验证（DNS/HTML 或 OAuth）——只开监控与发现通道、**不保证收录**；Website 验证后提交 sitemap 并 5 分钟内 Bing Import；Platform 仅度量内容在 Google Search/Discover/News 的表现，与 Website 并行、数据独立。

**Moat Asset**:
1. GSC property **三分法**总览（Website Domain / URL-prefix / Platform OAuth）
2. Website：粒度表 + token 不可复用 + 两串 meta 示例 + Bing Import
3. Platform（2026）：四平台表 + 测量边界 + vs Search profile
4. 删减全球引擎 encyclopedia 与三阶段重复，单篇覆盖「网站 + 社媒账号」完整 setup

**Differentiation angle**（vs 当前 alignify.co 稿 + SERP）:
- 唯一把 **2026 Platform properties** 与 Website 验证写入同一篇 GSC setup 指南
- Domain/URL-prefix 决策树 + Platform 无 sitemap 边界 — SERP 泛教程少见组合深度

**Answer Blocks**:
1. `#submit-vs-index`
2. `#gsc-property-overview` — 三分法
3. `#website-property-types` + `#choose-website-property`
4. `#verify-website-ownership`
5. `#after-website-verification`
6. `#platform-properties` — OAuth 四平台
7. `#platform-reports-and-limits`
8. `#property-boundaries`
9. `#bing-parallel`
10. `#anti-patterns`
11. `#conclusion`

**Removed（相对存量稿）**:
- 三阶段长节 → BLUF + 内链 `how-search-engine-works`
- 全球站长工具列表 → 内链 `search-engine`
- 加速索引杂烩（结构/频率/技术排查）→ 内链 `website-indexing` 等
- IndexNow/API 教程 → 1 句 + ops 链

**Sibling dedupe**: `how-search-engine-works` · `website-indexing` · `search-engine` · `sitemap`

**Planned internal links（出）**: `how-search-engine-works`, `search-engine`, `website-indexing`, `sitemap`, `checklist`, `internal-links`

**FAQ 7 问（锁定）**:
1. Domain 和 URL-prefix 怎么选？
2. 多个子域要几个 verification code？
3. Platform property 和 Website property 有何不同？
4. Platform 数据包含 TikTok 站内播放吗？
5. 提交后 Google 多久收录？
6. 如何从 GSC 导入 Bing？
7. 提交后仍不收录怎么办？

**Optional sections**: TL;DR ✅ · FAQ ✅ · References ✅ · How To ❌ · `#author-take` ❌

**Final CTA**（TBD Step 08）:
- ZH: GSC Website + Platform 并行 setup 或索引排查 → 开始合作
- EN: Work with us on GSC setup for sites and social accounts

**Skills**: [`seo-slug-notes/submit-website.md`](../../skills/create-article/rules/seo-slug-notes/submit-website.md)

**Build status**（2026-09-01）:
- [x] 单篇合并 Brief + Skills
- [x] ZH + EN 正文完整重构（部署仓 `content/seo/`）
- [x] tldr / faq / references JSON + seo-meta 同步
- [ ] OG brief 复核（可选增 Platform 副视觉）
- [ ] 入链回写（checklist · search-engine · learn-seo）
- [ ] audit-article Final ≥80
- [ ] npm run build 验证
