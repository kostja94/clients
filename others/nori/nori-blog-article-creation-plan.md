# Nori Blog 24 篇文章创建完整方案

> **依据 Skills**：article-page-generator | article-content | content-strategy | content-optimization | eeat-signals | competitor-research | keyword-research | url-slug | schema-markup | blog-page-generator  
> **关联**：[nori-blog.md](./nori-blog.md) | [nori-keywords.md](./nori-keywords.md) | [nori-features.md](./nori-features.md)  
> **21–24**：基于竞品已有 blog/页面创建（Cozi Chores、Sense/Carly、FamilyWall 替代、Cozi Back-to-School）

**Last updated**: 2026-03-12

---

## 一、方案总览

| 阶段 | 内容 | 对应 Skill |
|------|------|------------|
| **0. 前置准备** | 博客基础设施、共享资产、竞品 SERP 分析 | blog-page-generator, competitor-research |
| **1. 单篇创作流程** | 每篇文章的 Research → 创作 → 优化 → 发布 | article-page-generator, article-content |
| **2. 批量执行** | 24 篇顺序、内链规划、排期 | content-strategy |
| **3. 发布后** | 索引、监控、刷新 | article-page-generator |

---

## 二、前置准备（Phase 0）

### 2.1 博客基础设施

| 项目 | 要求 | 说明 |
|------|------|------|
| **URL** | heynori.com/blog | 子目录优于子域名（SEO 权重） |
| **内容源** | 本专案 [`blog/`](./blog/) 下 `*.md` | Markdown + YAML frontmatter；可导入 Hugo、Jekyll、Next.js MDX、Astro、Contentful 等 |
| **Blog Index** |  Featured/Recent、Categories、Editor's Picks | 见 blog-page-generator |
| **技术** | Core Web Vitals LCP <1s、WebP 图片、IndexNow | 新文章快速索引 |

### 2.2 共享资产

| 资产 | 规格 | 用途 |
|------|------|------|
| **Author Bio** | 姓名、credentials、照片、链接 | 每篇文末；E-E-A-T |
| **Author Page** | /blog/author/[name] | Person schema |
| **Featured Image 模板** | 1200px wide min、WebP、alt | 每篇 Hero |
| **Schema 模板** | Article/BlogPosting JSON-LD | 见 schema-markup |
| **CTA 组件** | 链接至 /app、/download、功能页 | 文末、侧边栏 |

### 2.3 竞品 SERP 基准（批量采集）

在正式写作前，对 **P0 文章**（1–5）做一次 SERP 分析：

| 文章 | 目标关键词 | 需采集 |
|------|------------|--------|
| 1 | best family calendar app 2026 | 2–3 篇 top 结果 URL、字数、H2 结构 |
| 2 | best AI family organizer | 同上 |
| 3 | family organizer app | 同上 |
| 4 | best meal planning app | 同上 |
| 5 | best recipe manager app | 同上 |

**方法**：competitor-research 的 Competitor Article Fetch Workflow；输出 length target、content gaps、keyword opportunities。

---

## 三、单篇文章创作流程（Phase 1）

每篇文章按以下顺序执行。**对应 Skills**：article-page-generator、article-content、content-optimization、eeat-signals。

### 3.1 Step 0：Research Phase（必做）

| 动作 | 输出 |
|------|------|
| **Keyword** | 主词、2–3 次词、opportunities（来自 SERP 或 PAA） |
| **Search Intent** | Informational / Commercial / Transactional / Navigational |
| **Competitor** | 2–3 篇 top 结果；字数、H2 结构、content gaps；length target |

**跳过条件**：仅当用户明确要求「skip search」时跳过。

### 3.2 Step 1：Intent Analysis

| 维度 | 输出 |
|------|------|
| **Orientation** | Guide / Listicle / Comparison |
| **Primary goal** | Brand、organic traffic、product adoption |
| **SEO vs non-SEO** | SEO-driven / Hybrid |
| **Evergreen vs timely** | Evergreen（多数） |

### 3.3 Step 2：Outline & Spec

| 元素 | 规范 |
|------|------|
| **URL Slug** | 3–5 词、<60 字符、主词含入、**不含年份与数字**（常青内容；每年更新正文即可，URL 不变） |
| **Title** | 55 字符内；主词靠前；power words |
| **Meta description** | 150–160 字符；CTA；主词 |
| **H1** | 与 Title 一致；唯一 |
| **H2 结构** | 4–8 个；QAE 模式；至少 1 个含主词或相关词 |
| **Word count** | 目标 ~2,000 字/篇；Listicle 1,200–2,000；How-to 1,000–1,500；Competitive 1,800–2,500 |

### 3.4 Step 3：Content Creation（article-content）

| 区块 | 规范 |
|------|------|
| **TL;DR / Key Takeaways** | 二选一；Intro 后；50–100 字或 5–7 条 bullet |
| **Intro** | 40–120 字；首句 hook（痛点/数据/问题）；首 100 字含主词 |
| **Body** | QAE：H2 问句 → 40–60 字直接回答 → 证据；段落 40–80 字 |
| **Conclusion** | 总结 + CTA；自然链接产品/功能页 |
| **Product connection** | 每篇至少 1 处自然提及 Nori 并链至功能页 |

### 3.5 Step 4：SEO & Technical

| 元素 | 规范 |
|------|------|
| **Keyword** | Title 1×；首 100 字 1×；Body 2–3×；至少 1 个 H2 |
| **Internal links** | Body 3–5 条 + Related 3–6 条；锚文本描述性 |
| **Outbound** | 2–5 条；引用数据/研究/权威来源 |

### 3.5.1 Internal Links 最佳实践（article-page-generator, internal-links）

| 要求 | 规范 |
|------|------|
| **总量** | Body 内 3–5 条 + Related 3–6 条 = 每篇 6–11 条 |
| **首段** | 至少 1 条链至 pillar 或相关文章 |
| **Body** | 每主要 section 1 条；链至相关 blog 或功能页（/app、/meal-planning 等） |
| **Related** | 文末 3–6 条同主题文章；锚文本用文章标题或描述性短语 |
| **锚文本** | 描述性（如 "how to organize family schedule"）；避免 "click here"、"learn more" |
| **锚文本变化** | 混合 exact-match、partial-match、branded；避免过度优化 |
| **Orphan 预防** | 每篇文章至少被 1 篇 hub/pillar 或 nav 链入 |

### 3.5.2 External Links 最佳实践（article-page-generator, eeat-signals）

| 要求 | 规范 |
|------|------|
| **总量** | 每篇 2–5 条外链 |
| **用途** | 统计数据、研究、定义、竞品/工具对比、专家引用 |
| **锚文本** | 描述性（如 "Pew Research survey"、"Google's guidelines"）；链至来源 |
| **同 URL** | 同一外链只计 1 次；无需重复 |
| **E-E-A-T** | 链至权威来源（Pew、APA、FDA、行业报告）；提升信任 |
| **nofollow noopener** | 站外链接使用 HTML：`<a href="URL" rel="nofollow noopener">锚文本</a>`；站内（heynori.com、/blog/）保持 Markdown |
| **Schema** | Article 或 BlogPosting；datePublished、dateModified、author |
| **Featured image** | 1200px wide、WebP、alt、og:image |
| **Share buttons** | Intro 后或文末；需 Open Graph、Twitter Cards |

### 3.6 Step 5：E-E-A-T（eeat-signals）

| 元素 | 说明 |
|------|------|
| **Author bio** | 文末；姓名、credentials、照片、链接 |
| **Citations** | 数据/统计引用来源；5+ 处时加 References 区 |
| **Experience** | 若适用：测试、案例、用户反馈 |

---

## 四、24 篇文章单篇规格表

每篇的 **URL slug**、**目标字数**、**主词**、**Nori 链接**、**Related 建议**。

| # | 主题 | URL Slug | 字数 | 主词 | Nori 链接 | Related 建议 |
|---|------|----------|------|------|-----------|--------------|
| 1 | Best Family Calendar App 2026 | best-family-calendar-app | 1,800–2,200 | best family calendar app 2026 | /app、/automatic-scheduling | 2, 3, 4, 9 |
| 2 | Best AI Family Organizer 2026 | best-ai-family-organizer | 1,800–2,200 | best AI family organizer | /app、首页 | 1, 3, 4, 9 |
| 3 | Best Family Organizer App 2026 | best-family-organizer-app | 1,800–2,200 | family organizer app | /app、首页 | 1, 2, 3, 4, 6 |
| 4 | Best Meal Planning App for Families 2026 | best-meal-planning-app-families | 1,800–2,200 | best meal planning app | /meal-planning | 5, 12, 13, 18 |
| 5 | Best Recipe Manager App 2026 | best-recipe-manager-app | 1,800–2,200 | best recipe manager app | /recipe-manager | 4, 19, 18 |
| 6 | Best Shared To-Do List Apps for Families 2026 | best-shared-todo-list-apps-families | 1,500–2,000 | shared to-do list families | /family-to-do-list | 3, 7, 9 |
| 7 | Best Voice To-Do List App 2026 | best-voice-todo-list-app | 1,200–1,800 | best voice to-do list app | /voice-to-do-list | 6, 14, 15 |
| 8 | Best Photo to Calendar App 2026 | best-photo-to-calendar-app | 1,200–1,800 | photo to calendar | /photo-to-calendar | 1, 10, 17 |
| 9 | How to Organize Family Schedule (Without Losing Your Mind) | how-to-organize-family-schedule | 1,200–1,800 | how to organize family schedule | /app、/automatic-scheduling | 1, 11, 14 |
| 10 | How to Add School Flyers to Calendar Automatically | how-to-add-school-flyers-to-calendar | 1,000–1,500 | school flyer to calendar | /photo-to-calendar | 8, 17 |
| 11 | How to Reduce Mental Load as a Parent | how-to-reduce-mental-load-parent | 1,200–1,800 | reduce mental load parents | /app、/use-cases/for-parents | 9, 14 |
| 12 | AI Meal Planning for Families: Complete Guide 2026 | ai-meal-planning-families-guide | 1,500–2,000 | AI meal planning for families | /meal-planning | 4, 13, 18 |
| 13 | AI Meal Planning for Families with Allergies | ai-meal-planning-families-allergies | 1,200–1,800 | AI meal planner allergy | /meal-planning | 4, 12 |
| 14 | Hands-Free Scheduling for Busy Parents | hands-free-scheduling-busy-parents | 1,200–1,800 | hands-free scheduling parents | /voice-to-calendar、/voice-to-do-list | 7, 9, 16 |
| 15 | Best ADHD Family Organizer Apps 2026 | best-adhd-family-organizer-apps | 1,200–1,800 | ADHD family organizer | /voice-to-do-list、/use-cases/for-parents | 7, 9, 11 |
| 16 | Cozi Alternative: 7 Best Family Organizer Apps Compared | cozi-alternative-family-organizer-apps | 1,800–2,500 | Cozi alternative | /app、待建 /comparison | 1, 2, 3 |
| 17 | Family Calendar for Sports Parents: Manage Kids' Activities | family-calendar-sports-parents | 1,200–1,800 | family calendar for sports parents | /photo-to-calendar、/use-cases/for-parents | 1, 8, 10 |
| 18 | Best Family Shopping List App 2026 | best-family-shopping-list-app | 1,200–1,800 | family shopping list app | /meal-planning | 4, 5, 6 |
| 19 | How to Import Recipes from Any Website (2026 Guide) | how-to-import-recipes-from-website | 1,200–1,800 | import recipes | /recipe-manager | 4, 5, 12 |
| 20 | Best Family Trip Planner Apps: AI Vacation Itinerary 2026 | best-family-trip-planner-apps | 1,200–1,800 | family trip planner | /ai-trip-planning | 1, 9 |
| 21 | Best Family Chore App 2026 | best-family-chore-app | 1,200–1,800 | family chore app, chore tracker for kids | /family-to-do-list | 6, 3, 9, 1 |
| 22 | How to Forward Email to Calendar Automatically | how-to-forward-email-to-calendar-automatically | 1,200–1,800 | forward email to calendar | /email-to-calendar | 1, 8, 9, 3 |
| 23 | FamilyWall Alternative: 7 Best Family Organizer Apps Compared | familywall-alternative-family-organizer-apps | 1,500–2,000 | FamilyWall alternative | /app | 16, 1, 3, 9 |
| 24 | Back-to-School: How to Organize Your Family Schedule | back-to-school-organize-family-schedule | 1,200–1,800 | back to school schedule | /photo-to-calendar、/app | 10, 9, 1, 17 |

---

## 五、内链规划（content-strategy）

### 5.1 Hub 与 Cluster

| Hub（概念） | Cluster 文章 |
|-------------|-------------|
| **家庭组织工具** | 1, 2, 3, 6, 7, 8, 15, 16, 21 |
| **餐食与食谱** | 4, 5, 12, 13, 18, 19 |
| **How-to / 场景** | 9, 10, 11, 14, 17, 22, 24 |
| **竞品** | 16, 23 |

### 5.2 内链规则

- 每篇 **Body**：3–5 条链至相关文章或功能页
- 每篇 **Related**：3–6 条同主题文章
- **Hub 文章**（1, 2, 3, 4, 5）：优先链入 cluster
- **避免**：纯 "click here"、"learn more" 锚文本

---

## 六、排期与执行顺序

| 批次 | 文章编号 | 建议周期 | 说明 |
|------|----------|----------|------|
| **P0** | 1, 2, 3, 4, 5 | 第 1–2 周 | 高量词；先做 SERP 分析 |
| **P1** | 6, 7, 8, 9, 16 | 第 3–4 周 | 差异化、竞品替代 |
| **P2** | 10, 11, 12, 13, 14, 15 | 第 5–6 周 | How-to、场景 |
| **P3** | 17, 18, 19, 20 | 第 7–8 周 | 扩展场景 |

**节奏**：每篇 2–3 天（含 Research、写作、审核、发布）；可并行时优先 P0。

---

## 七、发布后检查清单

| 项目 | 动作 |
|------|------|
| **IndexNow** | 新文章提交 IndexNow |
| **Sitemap** | 博客 URL 纳入 sitemap |
| **Canonical** | 自引用 canonical |
| **GSC** | 提交 URL 检查、请求索引 |
| **监控** | 索引状态、排名、Core Web Vitals |
| **刷新** | 每 6–12 个月更新数据、统计、内链 |

---

## 八、单篇创作 Checklist（可打印）

每篇文章可据此勾选：

```
□ Research Phase
  □ 主词、次词、opportunities
  □ Search intent
  □ 2–3 竞品 URL、字数、H2、gaps、length target

□ Outline & Spec
  □ URL slug（3–5 词、<60 字符、不含年份与数字）
  □ Title（55 字符、主词靠前）
  □ Meta description（150–160 字符）
  □ H2 结构（4–8 个、QAE）

□ Content
  □ TL;DR 或 Key Takeaways
  □ Intro（hook、主词 100 字内）
  □ Body（QAE、40–80 字/段）
  □ Conclusion
  □ 至少 1 处 Nori 产品链接

□ SEO
  □ 主词：Title、首 100 字、1 H2、Body 2–3×
  □ 内链：Body 3–5 + Related 3–6
  □ 外链：2–5 条引用
  □ Schema：Article/BlogPosting

□ Technical
  □ Featured image 1200px、WebP、alt
  □ Share buttons
  □ Author bio
  □ Open Graph、Twitter Cards
```

---

## 九、Markdown 文件与 CMS 部署

### 9.1 文件位置

| 路径 | 说明 |
|------|------|
| `blog/`（本专案内） | 所有文章 Markdown 文件 |
| `01-best-family-calendar-app-2026.md` ~ `20-best-family-trip-planner-apps-2026.md` | 20 篇文章（按编号排序） |
| `README.md` | 博客说明、CMS 兼容性 |

### 9.2 Frontmatter 格式（YAML）

每篇文章含以下 frontmatter，兼容常见 Markdown CMS：

```yaml
---
title: "文章标题"
description: "Meta description 150-160 字符"
slug: "url-slug"   # 不含年份、数字；常青 URL，每年更新正文即可
date: 2026-03-12
author: "Kostja"
image: "/blog/images/xxx.jpg"
keywords: ["keyword1", "keyword2"]
related: ["slug1", "slug2", "slug3"]
---
```

**Slug 最佳实践**：不含年份（如 -2026）、不含数字；保持常青，每年更新 title/正文中的年份即可，URL 不变，避免 301 与 SEO 流失。

### 9.3 兼容 CMS

| CMS / 框架 | 说明 |
|------------|------|
| **Hugo** | 原生支持 YAML frontmatter；`content/blog/` |
| **Jekyll** | 原生支持；`_posts/` 或 `blog/` |
| **Next.js MDX** | `gray-matter` 解析 frontmatter |
| **Astro** | 原生支持 Markdown + frontmatter |
| **Contentful** | 可导入为 Markdown 字段 |
| **Strapi** | Markdown 块或富文本 |

### 9.4 部署步骤建议

1. 将 `blog/` 目录配置为内容源
2. 配置 `slug` → URL 映射（如 `/blog/{slug}`）
3. 添加 `image` 占位或实际图片至 `/blog/images/`
4. 配置 Schema、Open Graph、sitemap

---

## 十、文档导航

| 文档 | 职责 |
|------|------|
| [nori-blog.md](./nori-blog.md) | Blog 策略、24 篇主题、关键词 |
| [nori-blog-article-creation-plan.md](./nori-blog-article-creation-plan.md) | **本文档**：完整创作方案、Markdown 部署 |
| [nori-keywords.md](./nori-keywords.md) | 关键词映射、待办 |
| [nori-features.md](./nori-features.md) | 功能页、URL、内容摘要 |
| [blog/](./blog/) | **24 篇 Markdown 文章**；可直接导入 CMS |
