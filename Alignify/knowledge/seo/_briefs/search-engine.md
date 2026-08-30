## Article Brief — search-engine

**SSOT**: `knowledge/seo/search-engine.md` · 规划 `search-engine.plan.md`

**QualityTier**: flagship  
**ArticleType**: seo-guide（**存量**路由 `/seo/search-engine` · 不重迁）  
**Gate A**: KEEP（2026-08-30 完整重构）  
**Copy mode**: M1  
**BatchCount**: 1 — search-engine（Outline 3.5 / Cross 5.5 → N/A）

**中文主称（锁定）**: **全球搜索引擎版图**  
**EN 主称**: Global Search Engine Landscape

**Search intent（2026-08-30 锁定）**:
1. **Landscape** — 有哪些入口、份额怎么读、七型类型学、AI/API 新层  
2. **Comparison** — Google/Bing/Yahoo/DDG 四引擎对照  
3. **Practitioner** — 读完地图后按市场叠加 GSC → Bing → 区域 → GEO（`#seo-stack-by-market`）  
4. **非本文主轴** — 消费者「日常用哪个搜索引擎」（不单独开五维 H2）

**One-line thesis**: 2026 年搜索入口是 **Google/Bing 通用索引 + 区域门户 + 隐私 syndication 链 + AI 三形态 + Web Search API** 的叠加；SEO 默认 GSC，按信号叠加 Bing 与区域站长工具。

**Moat Asset**:
1. 七型类型学主表（`#search-engine-taxonomy`）
2. 份额数据源偏差表（`#market-share-and-sources`）
3. `#industry-notes-2026` 独立 H2（AI Mode、GSC 分列、Bing API 退役、Agent 受众）
4. `#seo-stack-by-market` — 按信号叠加站长工具（替代 consumer how-to-choose）

**Answer Blocks**:
1. `#what-is-search-engine` — BLUF + 读者任务声明（SEO/增长，非 consumer picker）
2. `#terminology-layers` — 机制/产品/基础设施（H3 under taxonomy）
3. `#global-mainstream-search-engines` — Google/Bing/Yahoo/DDG
4. `#local-specialized-engines` — 区域 + 隐私 syndication（纯文本 defer 姊妹文）
5. `#search-engine-taxonomy` — 七型 SSOT 表
6. `#market-share-and-sources` — 数据源偏差
7. `#comparison-table` — 四引擎（对比型 intent，置于 AI 之前）
8. `#ai-search-overview` + `#ai-search-types` — AI SSOT → `/marketing/geo`
9. `#search-as-infrastructure` → `/tools/web-search-api`
10. `#seo-stack-by-market` — GSC/Bing/区域/GEO 四层（**无** consumer 五维 H3）
11. `#industry-notes-2026` — 2026 增量
12. `#conclusion`

**Removed（2026-08-30）**: `#how-to-choose-search-engine` 五 H3（与 landscape 重复、consumer 意图偏置）

**Sibling dedupe**: 不重复 local-search-engines 卡片 · 不重复 how-search-engine-works 流水线 · 不重复 tools/search-engine 产品深评 · 不重复 web-search-api 选型 · 不重复 geo 战术

**publishDate**: 2025-05-01（不改）  
**modifiedDate**: 2026-08-30

**Build status**（2026-08-30）:
- [x] ZH + EN 意图驱动重构（landscape + `#seo-stack-by-market`）
- [x] seo-meta.ts · tldr · faq 同步
- [x] `#industry-notes-2026` 独立 H2（段落体）
- [ ] audit-article Final ≥80（待终审）
- [ ] npm run build 验证（本轮）

**ZH Locale Pass**（2026-08-30）:
- [x] 标题改为「全球搜索引擎版图」
- [x] 新增 `#terminology-layers`
- [x] syndication / zero-click / 检索供应商 中文化
- [x] tldr · faq · seo-meta zh 同步
