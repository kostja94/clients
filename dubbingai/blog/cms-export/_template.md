---
title: "Article Title from CMS"
description: "Meta description from CMS og:description or meta name=description"
slug: "example-slug"
date: 2024-08-12
author: "Kostja"
category: "voice-changer-tips"
lang: "en"
status: "published"
source: "cms"
canonical: "https://dubbingai.io/blog/example-slug/"
migrated_at: 2026-06-15
superseded_by: ""
---

# Article Title from CMS

正文由 `scripts/fetch_and_convert.py` 从 CMS `.entry-content` 忠实转换。第一阶段不改动段落与链接。

**字段说明**

| 字段 | 必填 | 说明 |
|------|------|------|
| `slug` | 是 | 与 URL 一致，不含 `/blog/` |
| `date` | 是 | CMS 原始发布日 |
| `source` | 是 | 固定 `cms` |
| `canonical` | 是 | 线上 URL |
| `migrated_at` | 是 | 入库日期 |
| `superseded_by` | 否 | 若计划 301 到新 pillar，填新 slug |
| `category` | 否 | CMS 分类 slug |
| `lang` | 否 | 默认 `en`；葡语稿 `pt` |

> **2026-08-11 起废弃**：`image` / `keywords` / `related` 三个 frontmatter 字段不再使用（image 由 CMS 单独管理，keywords/related 由正文内链与 CMS 配置承载）。
