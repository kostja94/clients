# Final Round AI 项目任务

> 基于 [skills-task-progress.md](../../.cursor/templates/skills-task-progress.md) 模板；包含 Final Round AI（finalroundai.com / finalround.lovable.app）SEO、内容、产品、内链等当前待办。  
> 关联：[finalround.md](./finalround.md) | [finalround-schema.md](./technical/finalround-schema.md) | [finalround-blog.md](./blog/finalround-blog.md) | [finalround-keywords.md](./finalround-keywords.md) | [finalround-features.md](./finalround-features.md) | [finalround-production-routing.md](./technical/finalround-production-routing.md)

**Last updated**: 2026-06-04 — 更新后请同步修改日期。

---

## 需求概要

| # | 需求 | 说明 |
|---|------|------|
| 1 | **多语种** | Hreflang、多语言内容 |
| 2 | **站内 Forum** | 基于 Discourse 开源 forum |
| 3 | **Email Followup 生成器** | 小工具类型 |
| 4 | **资源性内容** | 如 [tech-layoffs](https://finalround.lovable.app/tech-layoffs) |
| 5 | **内链优化** | 聚合页、Navbar、Footer（见下方拆解） |
| 6 | **博客文章自动化** | 模板化内容批量生成、自动化流程 |

---

## Legend

| Status | Meaning |
|--------|---------|
| **Pending** | Not started |
| **In Progress** | Working on it |
| **Done** | Completed |

| Priority | Meaning |
|----------|---------|
| **P0** | Blocker — fix first |
| **P1** | High — do soon |
| **P2** | Medium — important but not urgent |

---

## 1. 多语种

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 1.1 | Hreflang 配置 | page-metadata, localization | Pending | P1 | 多语言 URL、hreflang 标签、x-default | |
| 1.2 | 内容翻译 | translation, localization | Pending | P2 | 重要页面翻译为英文（若当前非英）；与主站语言策略一致 | |

---

## 2. 站内 Forum

选型与替代方案详见 [finalround-community-forum.md](./community/finalround-community-forum.md)；**运营 Pipeline** 见 [community-ops-playbook.md](./community/community-ops-playbook.md)。

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 2.1 | Forum 选型与部署 | community-forum | Done | P2 | Discourse 已上线：`www.finalroundai.com/community/`；见 forum 文档 §1 | 2026-06-04 |
| 2.2 | Forum 与主站集成 | internal-links | In Progress | P1 | `/explore` 已有；待 Footer、canonical、sitemap、Blog 互链；见 forum §4.1 | 2026-06-04 |
| 2.3 | Community 运营 Pipeline | community-ops | Pending | P1 | 按 [community-ops-playbook.md](./community/community-ops-playbook.md) 执行；90 天目标 150–200 主题 | 2026-06-04 |

---

## 3. 小工具：Email Followup 生成器

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 3.1 | 工具页规划 | tools-page-generator | Pending | P2 | 新建 Email Followup 生成器工具页；URL 如 /tools/email-followup-generator | |
| 3.2 | 功能与文案 | copywriting | Pending | P2 | 输入场景、输出 followup 邮件模板；与求职/面试场景关联 | |

---

## 4. 资源性内容

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 4.1 | 资源页扩展 | resources-page-generator, programmatic-seo | Pending | P1 | 参考 [tech-layoffs](https://www.finalroundai.com/tech-layoffs) 模式；数据源见 [tech-layoffs/reference/resources.md](./tech-layoffs/reference/resources.md)；新增同类资源页（数据驱动、定期更新、与产品 CTA 关联） | |
| 4.2 | 资源页聚合 | internal-links | Pending | P1 | 资源页加入 /explore 聚合；内链至产品页 | |

---

## 5. 内链优化

### 5.1 聚合页面（Explore）

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 5.1.1 | **Explore 聚合页完善** | internal-links, website-structure | Pending | P0 | 参考 [finalround.lovable.app/explore](https://finalround.lovable.app/explore)；从 sitemap 选出最重要页面加入；**每次上新页面优先在此加链接** | |
| 5.1.2 | **内容英文化** | translation | Pending | P1 | 聚合页及重要页面内容翻译为英文；与主站语言一致 | |
| 5.1.3 | **定期优化流程** | — | Pending | P1 | 基于 Explore 内容**定期优化 Navbar 和 Footer**；两目的：(a) 聚合页方便爬虫爬取和用户跳转；(b) 帮助团队了解站内有哪些内容（类似 /blog 聚合） | |

**参考**：/explore 用纯文本 `<a href>` 列出所有页面，是最可靠的爬虫入口。

---

### 5.2 Navbar 与 Footer

**当前问题（侧边栏 Navbar）**：

| 问题 | 说明 |
|------|------|
| 侧边栏默认收起 | 60px 宽，只显示图标，无可见文字链接；爬虫对「视觉隐藏」内容权重降低 |
| 移动端完全隐藏 | `dt:block hidden`，需点击汉堡菜单展开；Google mobile-first indexing 下权重更低 |
| 链接可能动态加载 | 60px 内容区可能为空 div，hover/click 后 JS 加载；对爬虫不友好 |

**可被爬取**：顶部导航栏（桌面端）标准 `<a href>`；页面内容中的链接。

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 5.2.1 | **Footer 关键链接** | footer-generator | Pending | P0 | 在所有页面 Footer 放置关键链接；Footer 全站可见，SEO 权重稳定 | |
| 5.2.2 | **sitemap.xml** | xml-sitemap | Pending | P0 | 确保 sitemap 包含所有重要页面；作为 Explore 补充 | |
| 5.2.3 | **营销/SEO 页顶部导航** | navigation-menu-generator | Pending | P1 | 除首页和重要转化页外，在**营销页、SEO 页**使用**另一套顶部导航栏**（非侧边栏）；详细拆解链接、便于爬虫 | |

**原则**：侧边栏图标导航是好的 UX，但**不应依赖它传递 SEO 链接权重**。Explore 页 + Footer 链接才是 SEO 主力。

---

### 5.3 内链结构总览

```
/explore（核心聚合页）
├── 纯文本 <a href> 链接
├── 从 sitemap 选最重要页面
├── 上新页面优先加入
└── 定期驱动 Navbar/Footer 优化

Footer（全站可见）
├── 关键产品/资源链接
└── SEO 权重稳定

sitemap.xml
└── 补充爬虫发现

营销/SEO 页
└── 顶部导航栏（非侧边栏）— 详细链接
```

---

## 6. Technical SEO（基础）

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 6.1 | robots.txt | robots-txt | Pending | P0 | 按需配置 | |
| 6.2 | sitemap.xml | xml-sitemap | Pending | P0 | 与 5.2.2 合并 | |
| 6.3 | Canonical | canonical-tag | Pending | P1 | 每页绝对 URL | |
| 6.4 | Crawlability | site-crawlability | Pending | P0 | 重定向、孤儿页、内链 | |

---

## 7. On-Page SEO

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 7.1 | Title / Meta | title-tag, meta-description | Pending | P1 | 主关键词布局 | |
| 7.2 | Schema（全站基座） | schema-markup | Pending | P1 | 首页/全站：**Organization**、**WebSite**、`@graph` 拆分等（见 [finalround-schema.md](./technical/finalround-schema.md) §三、§六）。与 **7.5** 博客详情页区分：7.2 不含单篇 BlogPosting 模板。 | |
| 7.3 | OG / Twitter Cards | open-graph, twitter-cards | Pending | P2 | 社交分享预览 | |
| 7.4 | **博客面包屑（UI）** | breadcrumb-generator, schema-markup | Pending | P1 | **缺失/问题**：(1) 常见仅三级、**末级停在分类**——应为四级 **Home → Blog → Category → 文章标题**（无分类时可三级到标题）；(2) 分隔符 **`>` 被包在指向首页的 `<a>`**，应改为非链接装饰（无障碍）。**BreadcrumbList** JSON-LD 见 **7.5** 与 [finalround-schema.md](./technical/finalround-schema.md) §七 · 7.2。**样例**：[cybersecurity-engineers-cover-letter](https://www.finalroundai.com/blog/cybersecurity-engineers-cover-letter)。 | 2026-03-31 |
| 7.5 | **博客详情页 Schema 补全** | schema-markup | Pending | P1 | **当前**：详情页往往仅有 **FAQPage**（文末 FAQ）。**待补**：(1) **BlogPosting** 或 **Article**——`headline`、`image`（建议 ≥1200px，与 og:image 一致）、`author`→Person、`datePublished`/`dateModified`、`publisher`→Organization；(2) **BreadcrumbList**——与可见面包屑一致，**item 绝对 URL**，与 **7.4** 同步上线；(3) **FAQPage**——与页面 **可见问答逐条一致**，禁止仅 JSON-LD 存在而 DOM 无对应内容。字段级见 [finalround-schema.md](./technical/finalround-schema.md) §七 · 7.1。发布后 Rich Results / Validator 抽测。 | 2026-03-31 |

---

## 8. 博客文章自动化

> 策略与主题见 [finalround-blog.md](./blog/finalround-blog.md)

**背景**：薪资换算、简历同义词等高流量类型为可模板化内容；产品核心词（AI interview assistant、interview copilot）待加强。

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 8.1 | **自动化流程搭建** | programmatic-seo, content-strategy | Pending | P1 | 建立模板 + 数据驱动的文章生成流程；新文章自动加入 /blog 聚合、sitemap、Explore | |
| 8.2 | **薪资换算类批量生成** | programmatic-seo | Pending | P1 | 基于现有高流量页（如 $25/hour↔year、60k/year↔hour）扩展变体；模板化、批量产出 | |
| 8.3 | **简历同义词类批量生成** | programmatic-seo | Pending | P1 | 基于 another-word-for-X 模式扩展；覆盖 resume synonym 长尾 | |
| 8.4 | **自动化文章 CTA 与内链** | internal-links, content-optimization | Pending | P1 | 每篇自动化文章嵌入产品 CTA、链至 /interview-copilot、/ai-mock-interview；提升转化 | |

---

## 已完成（Done）

| # | Task | Skill | Completed | Notes |
|---|------|-------|-----------|------|
| — | *暂无* | — | — | 完成时移入此处 |

---

## Quick Reference

| 模块 | 优先级 | 核心动作 |
|------|--------|----------|
| **5.1 聚合页** | P0 | Explore 完善、上新优先加链、定期驱动 Navbar/Footer |
| **5.2 Navbar/Footer** | P0 | Footer 关键链接、sitemap；营销页用顶部导航 |
| **4 资源内容** | P1 | tech-layoffs 模式扩展 |
| **7.4 面包屑 UI** | P1 | 四级到文章标题；分隔符勿链首页 |
| **7.5 博客详情 Schema** | P1 | BlogPosting + BreadcrumbList + FAQPage 与可见一致 |
| **8 博客自动化** | P1 | 薪资换算、简历同义词批量生成；自动化流程 |
| **1 多语种** | P1 | Hreflang、翻译 |
| **2 Forum** | P2 | Discourse 部署 |
| **3 Email Followup** | P2 | 工具页 |

---

## 文档导航

| 文档 | 用途 | 何时查阅 |
|------|------|----------|
| [finalround.md](./finalround.md) | 主文档、产品概览 | 了解产品全貌 |
| [finalround-schema.md](./technical/finalround-schema.md) | Schema.org / JSON-LD | 博客详情、面包屑、自检 |
| [finalround-project-tasks.md](./finalround-project-tasks.md) | 项目任务 | 本文档 |
| [finalround-blog.md](./blog/finalround-blog.md) | Blog 内容策略、自动化 | 文章主题 |
| [finalround-keywords.md](./finalround-keywords.md) | 关键词映射 | 写文案、SEO |
| [finalround-features.md](./finalround-features.md) | 功能、定价 | 产品详情 |
| [finalround-use-cases.md](./finalround-use-cases.md) | 使用场景 | 场景页 |
| [finalround-site-structure.md](./finalround-site-structure.md) | 网站 URL、内链、sitemap 规划 | 建站与 SEO |
| [finalround-production-routing.md](./technical/finalround-production-routing.md) | 前端实施：转发、模式 A/B、`/_next` | 主域与子站联调 |
| [finalround-competitors.md](./finalround-competitors.md) | 竞品分析 | 对比页 |
| [tech-layoffs/reference/resources.md](./tech-layoffs/reference/resources.md) | 资源参考、数据源 | 资源页扩展、裁员/求职内容 |
| [finalround-brand-visual.md](./finalround-brand-visual.md) | 品牌色彩 | 落地页 |
| [finalround-blog-article skill](./skills/finalround-blog-article/SKILL.md) | Blog 创作规范 + Review 程序化（`references/review-programmatic.md`） | 批量生成 Review |

---

*来源：finalround.md、skills-task-progress.md、/tech-layoffs、[tech-layoffs/reference/resources.md](./tech-layoffs/reference/resources.md)*
