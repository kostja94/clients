# AgentBoard 项目任务

> 本文档专注**任务**：Phase 0–5、SEO 审查、Blog、策略细化。基于 [skills-task-progress.md](../../.cursor/templates/skills-task-progress.md) 模板。  
> **关联**：[agentboard.md](./agentboard.md)（需求与优先级、产品状态）| [文档索引表 §10](./agentboard.md#10-文档互引)

**Last updated**: 2026-03-30（文档优化：需求表合并至主文档）

---

## 项目需求与优先级

> **权威表格** → [agentboard.md](./agentboard.md)（**当前需求与优先级**、**项目定位**）。本节不重复粘贴，避免双处维护。

---

## 任务进度

| 状态 | 数量 | 占比 |
|------|------|------|
| **未完成**（Pending / In Progress） | 18 | 100% |
| **已完成**（Done） | 0 | 0% |
| **总计** | 18 | — |

**进度**：0 / 18 已完成

---

## Legend

| Status | Meaning |
|--------|---------|
| **Pending** | Not started; needs work |
| **In Progress** | Currently working on it |
| **Done** | Completed |

| Priority | Meaning |
|----------|---------|
| **P0** | Blocker — fix first（SEO 审查、Blog） |
| **P1** | High — do soon |
| **P2** | Medium — important but not urgent |

**Workflow order**：Phase 0 SEO 审查 → Phase 1 Blog 建设 → Phase 2 策略细化（Technical → On-Page → Content → Off-Page）

---

## Phase 0：完整 SEO 审查（P0）

> 先执行全站 SEO 审计，产出问题清单与优先级；再进入 Phase 1 / Phase 2。

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 0.1 | **Technical SEO 审查** | seo-audit, robots, sitemap, crawlability, indexing | Pending | P0 | robots.txt、sitemap.xml、爬取性、索引状态、重定向、孤儿页；输出审查报告 | |
| 0.2 | **On-Page SEO 审查** | title-tag, meta-description, schema, heading, image-optimization | Pending | P0 | Title、Meta、Schema、H 结构、图片 alt；输出问题清单 | |
| 0.3 | **索引与 GSC 审查** | indexing, google-search-console | Pending | P0 | GSC 索引覆盖、Crawled - not indexed、noindex 配置 | |

**产出**：SEO 审查报告、问题清单、优先级排序 → 供 Phase 2 策略细化使用。

---

## Phase 1：Blog 建设（P0）

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 1.1 | **Blog 页面结构** | blog-page-generator | Pending | P0 | 新建 /blog；规划 Blog 结构、列表页、文章页 URL 模式 | |
| 1.2 | **首批 Blog 文章** | article-content, content-strategy | Pending | P0 | 自写 2–3 篇；主题见 [agentboard-use-cases.md](./agentboard-use-cases.md)、[agentboard-keywords.md](./agentboard-keywords.md)；覆盖 AI coding stats、Claude Code、Cursor、Code Wrapped 等 | |
| 1.3 | **Blog 内链与导航** | internal-links, sidebar-generator | Pending | P1 | Blog 与首页、安装页内链；侧边栏/相关文章 | |

---

## Phase 2：Technical SEO（基于审查结果）

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 2.1 | robots.txt | robots-txt | Pending | P0 | 按审查结果修复 | |
| 2.2 | sitemap.xml | xml-sitemap | Pending | P0 | 包含首页、`/leaderboard`、`/blog`、`/methodology`、`/install` 等 | |
| 2.3 | Canonical URLs | canonical-tag | Pending | P1 | 每页绝对 URL | |
| 2.4 | Indexing / noindex | indexing | Pending | P1 | 按审查结果配置 | |
| 2.5 | Crawlability | site-crawlability | Pending | P0 | 重定向、内链、孤儿页 | |

---

## Phase 3：On-Page SEO

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 3.1 | Title tag | title-tag | Pending | P1 | AgentBoard、AI coding stats、agentboard.cc 在 title | |
| 3.2 | Meta description | meta-description | Pending | P1 | 含主关键词；见 [agentboard-keywords.md](./agentboard-keywords.md) | |
| 3.3 | Schema / structured data | schema-markup | Pending | P1 | Organization、WebSite、SoftwareApplication、BreadcrumbList | |
| 3.4 | Open Graph / Twitter Cards | open-graph, twitter-cards | Pending | P2 | 社交分享预览；Code Wrapped 卡片分享 | |
| 3.5 | Heading structure | heading-structure | Pending | P1 | 每页 1 个 H1；H2/H3 含关键词 | |
| 3.6 | Image optimization | image-optimization | Pending | P1 | alt、WebP、LCP | |

---

## Phase 4：Content & Pages

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 4.1 | 品牌词覆盖 | — | Pending | P1 | AgentBoard、agentboard.cc 在 title、meta、H1 | |
| 4.2 | 功能词落地 | — | Pending | P1 | AI coding stats、Claude Code stats 在首页文案 | |
| 4.3 | Alternatives 页（可选） | alternatives-page-generator | Pending | P2 | AgentBoard vs WakaTime、vs Code Insights；见 [agentboard-competitors.md](./agentboard-competitors.md) | |
| 4.4 | Use cases 页（可选） | use-cases-page-generator | Pending | P2 | 个人证明、社交竞争、DevRel；见 [agentboard-use-cases.md](./agentboard-use-cases.md) | |

---

## Phase 5：Components & Analytics

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 5.1 | Navigation / Footer | navigation-menu-generator, footer-generator | Pending | P1 | 含 Blog 入口、安装 CTA | |
| 5.2 | Hero / CTA | hero-generator, cta-generator | Pending | P1 | 首页「One command」、Sign in | |
| 5.3 | GA4 / GSC | analytics-tracking, google-search-console | Pending | P1 | 追踪安装、Sign in、分享 | |

---

## 已完成（Done）

| # | Task | Skill | Completed | Notes |
|---|------|-------|-----------|------|
| — | *暂无* | — | — | 完成时将任务从上方移入此处 |

---

## Quick Reference

| Phase | 内容 | 触发 |
|-------|------|------|
| **Phase 0** | SEO 审查 | 首先执行；产出问题清单 |
| **Phase 1** | Blog 建设 | P0；与 Phase 0 可并行规划 |
| **Phase 2** | Technical SEO | 基于审查结果落地 |
| **Phase 3** | On-Page SEO | 品牌词、功能词、Schema |
| **Phase 4** | Content & Pages | 长尾页、Alternatives、Use cases |
| **Phase 5** | Components & Analytics | 导航、CTA、追踪 |

**AI Agent 使用**：提及「SEO audit」「SEO 审查」时执行 Phase 0；提及「Blog」「blog page」时执行 Phase 1。

---

**文档索引**（全表）→ [agentboard.md §10 文档互引](./agentboard.md#10-文档互引)

---

*来源：[agentboard.md](./agentboard.md)、skills-task-progress.md 模板*
