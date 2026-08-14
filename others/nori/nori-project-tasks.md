# Nori 项目任务

> 基于 [skills-task-progress.md](../../.cursor/templates/skills-task-progress.md) 模板；包含 Nori（heynori.com）SEO、产品、营销等当前待办。  
> 关联：[nori.md](./nori.md) | [nori-features.md](./nori-features.md) | [nori-keywords.md](./nori-keywords.md) | [nori-site-structure.md](./nori-site-structure.md) | [nori-competitors.md](./nori-competitors.md) | [nori-calendar-converter.md](./nori-calendar-converter.md) | [nori-schedules.md](./nori-schedules.md) | [nori-others.md](./nori-others.md)（proof/backlog 索引，按需）  
> **维护规范**：通用-多文件文档联动精炼与增量循环.md §5

**Last updated**: 2026-03-24 — 更新后请同步修改日期，并可在 [nori-others.md](./nori-others.md) §4 记一笔索引。

---

## 任务进度

| 状态 | 数量 | 占比 |
|------|------|------|
| **未完成**（Pending / In Progress） | 8 | 100% |
| **已完成**（Done） | 0 | 0% |
| **总计** | 8 | — |

**进度**：0 / 8 已完成

---

## Legend

| Status | Meaning |
|--------|---------|
| **Pending** | Not started; needs work |
| **In Progress** | Currently working on it |
| **Done** | Completed |

| Priority | Meaning |
|----------|---------|
| **P0** | Blocker — fix first |
| **P1** | High — do soon |
| **P2** | Medium — important but not urgent |

**任务分类**：Technical SEO（4）| On-page SEO（6、7）| 内容/结构（1、2、3、5、8）

---

## 未完成（Pending / In Progress）

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 1 | **功能页 URL 优化** — 添加新功能页、优化老功能页 URL（SEO 不友好且与全站结构不一致） | url-structure, website-structure | Pending | P1 | 新建 /photo-to-calendar、/email-to-calendar、/call-alert、/ai-trip-planning、/family-to-do-list；301 旧 URL→新 URL：/import-recipes-instantly→/recipe-manager、/ai-powered-meal-planning→/meal-planning、/add-anything-by-voice→/voice-to-do-list、/features/ai-generated-tasks→/ai-generated-tasks；统一 URL 模式（kebab-case、与功能名一致）；见 [nori-features.md](./nori-features.md) §一、§六 | |
| 2 | **Schedules Hub 页** — 体育赛程模块入口页 | programmatic-seo, template-page | Pending | P1 | 新建 /schedules 作为赛程 Hub；链出 /schedules/mlb、/schedules/nfl 等联赛入口；球队详情页 /schedules/{league}/{team-slug}；见 [nori-schedules.md](./nori-schedules.md) | |
| 3 | **Recipes Importer 程序化菜谱页** — 仅针对 recipe importer 做批量程序化菜谱页面 | programmatic-seo | Pending | P1 | 基于 recipe 数据批量生成程序化菜谱页（如 /recipes/[slug]）；模板与数据驱动；覆盖 recipe manager、import recipes 相关长尾；不扩展其他 recipe 功能；与 /recipe-manager 主功能页内链 | |
| 4 | **Technical SEO 优化** | canonical, schema-markup | Pending | P1 | Canonical、Schema（Organization、WebSite、Recipe、BreadcrumbList、SoftwareApplication）、Hreflang（若多语言）；按 Google Search Central / Schema.org 与站内模板执行，**不引用其他客户专案** | |
| 5 | **关键词调研** — 找到功能一致且最通用的长尾关键词（如 photo to calendar） | keyword-research | Pending | P1 | 按功能梳理「X to Y」式、工具选型式等通用长尾；功能一致=与 Nori 能力匹配；最通用=搜索意图宽、不限定 persona；输出至 [nori-keywords.md](./nori-keywords.md) 长尾表；参考竞品 GSC/排名词 | |
| 6 | **Metadata 优化** — Title、Description、OG、Twitter Cards | title-tag, description, open-graph, twitter-cards | Pending | P1 | **On-page SEO**；每页 title、meta description 含主关键词；OG/Twitter Cards 社交分享预览；图片 1200×630px、绝对 URL；见 [nori-features.md](./nori-features.md) 各功能页 Title/Meta | |
| 7 | **Heading 优化** — H 标签结构与层级 | heading-structure | Pending | P1 | **On-page SEO**；每页仅 1 个 H1；H1→H2→H3 不跳级；H2/H3 含关键词、描述性强；见 [nori-features.md](./nori-features.md) 内容边界 | |
| 8 | **Alternatives 页面** — 竞品替代与对比页 | alternatives-page | Pending | P2 | 新建 /comparison/{slug}（如 nori-vs-cozi、nori-vs-familywall、nori-vs-paprika）；覆盖 Cozi alternative、Paprika alternative、Nori vs Cozi 等竞品词；差异化见 [nori-competitors.md](./nori-competitors.md) | |

---

## 已完成（Done）

| # | Task | Skill | Completed | Notes |
|---|------|-------|-----------|------|
| — | *暂无* | — | — | 完成时将任务从上方移入此处 |

---

## Task Details

### Task 1：功能页 URL 优化

**问题**：旧功能页 URL 对 SEO 不友好，且与全站 URL 结构不一致。

**目标 URL 模式**（见 [nori-features.md](./nori-features.md) §一、§六；[nori-keywords.md](./nori-keywords.md) §11）：
- 功能页：`/feature-name`（kebab-case，与主关键词一致）
- Use Cases：`/use-cases/{persona}`

**301 重定向**：
| 旧 URL | 新 URL |
|--------|--------|
| /import-recipes-instantly | /recipe-manager |
| /ai-powered-meal-planning | /meal-planning |
| /add-anything-by-voice | /voice-to-do-list |
| /features/ai-generated-tasks | /ai-generated-tasks |

**待新建页面**：/photo-to-calendar、/email-to-calendar、/voice-to-calendar、/call-alert、/ai-trip-planning、/family-to-do-list（统一 xxx-to-calendar URL 模式）

---

### Task 2：Recipes Importer 程序化菜谱页

**范围**：仅针对 recipe importer 做批量程序化菜谱页面，不扩展其他 recipe 功能。

**目标**：程序化生成菜谱详情页（如 /recipes/[slug]），覆盖 recipe manager、import recipes、save recipes from website 等长尾关键词。

**实现**：模板 + 菜谱数据；Schema Recipe；与 /recipe-manager 主功能页内链。

---

### Task 4：关键词调研

**目标**：找到功能一致且最通用的长尾关键词，供功能页、URL、内容优化使用。

**标准**：
- **功能一致**：与 Nori 核心能力匹配（photo to calendar、email to calendar、voice to schedule、recipe manager、meal planning 等）
- **最通用**：搜索意图宽、不限定 persona；如 photo to calendar 比 school flyer to calendar 更通用

**输出**：更新 [nori-keywords.md](./nori-keywords.md) 长尾表（§15、§16）；博客主题见 [nori-blog.md](./nori-blog.md)；按功能/目标页归类；标注搜索量、竞品排名

**方法**：GSC/GA4 现有词、竞品排名词、People Also Ask、工具选型词（best X app）、「X to Y」式动作词

---

### Task 3：Technical SEO

**类别**：Technical SEO（技术 SEO）

**核心项**：Canonical、Schema、Hreflang；实现说明以官方文档与本文档任务表为准。

- Canonical：每页绝对 URL
- Schema：Organization、WebSite、Recipe（菜谱页）、BreadcrumbList、SoftwareApplication
- Hreflang：若多语言，配置自引用、x-default

---

### Task 5：Metadata 优化

**类别**：**On-page SEO**（页面 SEO）

**范围**：title tag、meta description、Open Graph、Twitter Cards

**动作**：每页 title、meta description 含主关键词；OG/Twitter Cards 社交分享预览（og:title、og:description、og:image、og:url；1200×630px、绝对 URL）；见 [nori-features.md](./nori-features.md) 各功能页 Title/Meta 规范

---

### Task 6：Heading 优化

**类别**：**On-page SEO**（页面 SEO）

**范围**：H1–H6 标签结构与层级

**动作**：每页仅 1 个 H1；H1→H2→H3 不跳级；H2/H3 含关键词、描述性强；见 [nori-features.md](./nori-features.md) 内容边界与目标词

---

### Task 7：Alternatives 页面

**类别**：**内容/营销页**（竞品截流）

**范围**：竞品替代页（X alternative）、对比页（Nori vs X）

**目标关键词**（见 [nori-keywords.md](./nori-keywords.md) §6、§17；[nori-competitors.md](./nori-competitors.md) §5、§8）：
- 替代：Cozi alternative、FamilyWall alternative、Paprika alternative、Any.do alternative、Sense alternative、Kora alternative
- 对比：Nori vs Cozi、Nori vs FamilyWall、Nori vs Paprika、Cozi vs Nori

**URL 模式**：/comparison/nori-vs-cozi、/comparison/nori-vs-familywall 等

**动作**：每页突出 Nori 差异化（voice/photo/email 多模态、家庭共享、与 meal planning 一体化）；见 [nori-competitors.md](./nori-competitors.md) 对比矩阵与差异化

---

## Page Scope (Nori)

**站点**：https://heynori.com/

- **首页**：/
- **功能页**：/recipe-manager、/meal-planning、/automatic-scheduling、/photo-to-calendar、/email-to-calendar、/call-alert、/ai-trip-planning、/family-to-do-list、/voice-to-do-list、/ai-generated-tasks
- **Use Cases**：/use-cases/for-parents、/use-cases/for-grandparents、/use-cases/for-caregivers、/use-cases/for-families
- **对比页**：/comparison/{slug}（待建：nori-vs-cozi、nori-vs-familywall、nori-vs-paprika 等）
- **其他**：/app、/download、help.heynori.com
