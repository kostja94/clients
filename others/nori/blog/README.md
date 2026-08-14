# Nori Blog

Markdown 格式文章，可直接导入支持 Markdown 的 CMS（Hugo、Jekyll、Next.js MDX、Astro、Contentful 等）。

## 文件结构

- `*.md`：单篇文章，含 YAML frontmatter
- 每篇包含：title、description、slug、date、author、keywords、related
- **本目录文档**：`README.md`（本说明）、`INTERNAL-EXTERNAL-LINKS-CHECKLIST.md`（内链外链规范）

## Frontmatter 示例

```yaml
---
title: "Best Family Calendar App 2026"
description: "Meta description..."
slug: "best-family-calendar-app"   # 不含年份，常青 URL
date: 2026-03-12
author: "Kostja"
image: "/blog/images/xxx.jpg"
keywords: ["keyword1", "keyword2"]
related: ["slug1", "slug2"]
---
```

## 文章列表（20 篇）

| # | 文件 | 主题 |
|---|------|------|
| 1 | 01-best-family-calendar-app-2026.md | Best Family Calendar App 2026 |
| 2 | 02-best-ai-family-organizer-2026.md | Best AI Family Organizer 2026 |
| 3 | 03-best-family-organizer-app-2026.md | Best Family Organizer App 2026 |
| 4 | 04-best-meal-planning-app-families-2026.md | Best Meal Planning App for Families 2026 |
| 5 | 05-best-recipe-manager-app-2026.md | Best Recipe Manager App 2026 |
| 6 | 06-best-shared-todo-list-apps-families-2026.md | Best Shared To-Do List Apps for Families 2026 |
| 7 | 07-best-voice-todo-list-app-2026.md | Best Voice To-Do List App 2026 |
| 8 | 08-best-photo-to-calendar-app-2026.md | Best Photo to Calendar App 2026 |
| 9 | 09-how-to-organize-family-schedule.md | How to Organize Family Schedule |
| 10 | 10-how-to-add-school-flyers-to-calendar.md | How to Add School Flyers to Calendar |
| 11 | 11-how-to-reduce-mental-load-parent.md | How to Reduce Mental Load as a Parent |
| 12 | 12-ai-meal-planning-families-guide-2026.md | AI Meal Planning for Families: Complete Guide 2026 |
| 13 | 13-ai-meal-planning-families-allergies.md | AI Meal Planning for Families with Allergies |
| 14 | 14-hands-free-scheduling-busy-parents.md | Hands-Free Scheduling for Busy Parents |
| 15 | 15-best-adhd-family-organizer-apps-2026.md | Best ADHD Family Organizer Apps 2026 |
| 16 | 16-cozi-alternative-family-organizer-apps.md | Cozi Alternative: 7 Best Family Organizer Apps |
| 17 | 17-family-calendar-sports-parents.md | Family Calendar for Sports Parents |
| 18 | 18-best-family-shopping-list-app-2026.md | Best Family Shopping List App 2026 |
| 19 | 19-how-to-import-recipes-from-website.md | How to Import Recipes from Any Website |
| 20 | 20-best-family-trip-planner-apps-2026.md | Best Family Trip Planner Apps 2026 |

> 编号 21–27、**28–30（家庭管理主题簇）**、**31–34** 等同目录 `NN-*.md`；完整规划见 [nori-blog-article-creation-plan.md](../nori-blog-article-creation-plan.md)。其中 **28–30**：`28-shared-calendar-for-co-parents-2026.md`、`29-blended-family-calendar-guide-2026.md`、`30-multi-generational-family-calendar-2026.md`；**31**：`31-google-family-manager-2026.md`（Google Family manager 角色与家庭群组）；**32**：`32-manage-family-with-ai-workflows-2026.md`（Manage family with AI workflows）；**33**：`33-best-family-management-software-2026.md`（Best family management software — 家庭运营向 ranking）；**34**：`34-what-is-family-management-app-2026.md`（family management app 定义；含 **AI-assisted capture** 段落，不单独做通用「AI family manager」专文）。

## 部署

将 `blog/` 目录配置为内容源，设置 `slug` → `/blog/{slug}` URL 映射。图片路径 `image` 需对应实际 CDN 或静态资源路径。（导入 CMS 时可排除 `README.md`、INTERNAL-EXTERNAL-LINKS-CHECKLIST.md。）

## 关联文档

- [nori-blog.md](../nori-blog.md) — Blog 策略
- [nori-blog-article-creation-plan.md](../nori-blog-article-creation-plan.md) — 创作方案、CMS 部署说明
- [INTERNAL-EXTERNAL-LINKS-CHECKLIST.md](./INTERNAL-EXTERNAL-LINKS-CHECKLIST.md) — 内链外链规范
