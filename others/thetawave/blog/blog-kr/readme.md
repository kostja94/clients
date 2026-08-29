# ThetaWave blog-kr（韩文站内博客）

Korean Markdown articles for **thetawave.ai/ko/blog/{slug}** live in this folder（`*.md` with YAML frontmatter），与英文站内博客 [`../`](../readme.md)（→ `/blog/{slug}`）和外部 Naver 渠道 [`../../localization/`](../../localization/readme.md) 分目录存放。

**URL 区别**：

| 目录 | 线上 URL | 用途 |
|------|----------|------|
| `blog/` | `https://thetawave.ai/blog/{slug}` | 英文站内博客 |
| `blog/blog-kr/` | `https://thetawave.ai/ko/blog/{slug}` | 韩文站内博客（本目录） |
| `localization/` | Naver Blog 等外部渠道 | 韩文外部分发 |

---

## 目录结构

| 路径 | 说明 |
|------|------|
| [`*.md`](./) | 韩文博客 Markdown 稿 |
| [readme.md](./readme.md) | 本文件：维护说明、Frontmatter 参考、已发布登记表 |

---

## Frontmatter 示例

```yaml
---
title: "한국 학생을 위한 최고의 AI 노트 필기 앱 (2026)"
description: "Naver / Google 검색용 메타 설명; 150–160자 권장."
slug: "best-ai-note-taker-korean-students"       # 英文 kebab-case，常青 URL → /ko/blog/best-ai-note-taker-korean-students
date: 2026-05-18
author: "Kostja"
language: "ko"
locale: "ko-KR"
image: "/ko/blog/images/best-ai-note-taker-korean-students-2026.jpg"
keywords: ["AI 노트 필기", "한국 학생", "강의 노트"]
related: ["lecture-to-notes-ai", "ai-notes-generator-students"]   # 英文 slug，不带 /ko/ 前缀
---
```

**字段说明**

- `title` / `description`：韩文标题与 meta description。
- `slug`：**英文 kebab-case**，与线上 `/ko/blog/{slug}` 一致；`related` 填英文 slug 字符串（不带 `/ko/` 前缀或域名）。
- `language`：固定 `"ko"`，供 CMS / 路由匹配。
- `locale`：固定 `"ko-KR"`，供 `hreflang` / `og:locale` 使用。
- `image`：封面图路径，推荐 `/ko/blog/images/{slug}-{year}.jpg`，与韩文静态资源目录对齐。
- `keywords`：韩文关键词，Naver 优先；详细映射见 [`../../keywords/thetawave-keywords.md`](../../keywords/thetawave-keywords.md)。

---

## 命名规则

`NN-{slug}-{year}.md`，其中 `slug` 为英文 kebab-case，与 frontmatter `slug` 一致。

示例：
- `04-best-ai-note-taker-korean-2026.md` → `slug: "best-ai-note-taker-korean"`
- `05-ai-study-tools-korea-2026.md` → `slug: "ai-study-tools-korea"`

韩文独立从 01 开始计数，与英文 `blog/` 分开。

---

## 内外链规范

韩国站内博客沿用 [英文内外链规范](../internal-external-links-checklist.md) 思路，但 URL 前缀为 `/ko/`：

| 类型 | 路径 / URL | 说明 |
|------|------------|------|
| **Blog 互链** | `/ko/blog/{slug}` | 韩文博文互链；也链英文 `/blog/{slug}` 仅在双语补充时 |
| **核心转化** | `https://thetawave.ai/ko/auth/signup` | 韩文注册 / 试用 CTA |
| **AI Note Taker** | `https://thetawave.ai/ko/` | 韩文首页（实时记录 / 讲座捕获） |
| **Notes Generator** | `https://thetawave.ai/ko/feature/notes-generator` | 「从素材生成笔记」韩文落地 |
| **其他功能页** | `/ko/feature/{slug}` | 如 `/ko/feature/lecture-to-notes`、`/ko/feature/flashcard-maker` |
| **Use Cases** | `/ko/use-case/{slug}` | 如 `/ko/use-case/korean-civil-service-9-prep` |
| **韩文竞品** | 韩国本地竞品（공단기、해커스 等） | `rel="nofollow noopener"` |
| **权威来源** | 韩国政府 / 教育机构（인사혁신처、국사편찬위원회 等） | 可核对数据，锚文本描述性 |

**韩国内链分布与英文一致**：首段 ≥1 条 + Body blog 互链 1–4 + Related 2–6；功能页与 signup 按主题穿插，忌重复堆叠。

---

## 部署提示

将 `blog-kr/` 配置为韩语内容源，`slug` → `https://thetawave.ai/ko/blog/{slug}`。路由与语言前缀匹配以 [`../../tech-stack/thetawave-production-routing-i18n.md`](../../tech-stack/thetawave-production-routing-i18n.md) 为准。

---

## 关联文档

| 文档 | 用途 |
|------|------|
| [../readme.md](../readme.md) | 英文博客维护说明、Frontmatter 示例 |
| [../internal-external-links-checklist.md](../internal-external-links-checklist.md) | 内外链分层、竞品 nofollow、E-E-A-T |
| [../../thetawave-features.md](../../thetawave-features.md) | 功能落地页路径 |
| [../../thetawave-use-cases.md](../../thetawave-use-cases.md) | Use Cases 路径 |
| [../../thetawave-competitors.md](../../thetawave-competitors.md) | 竞品与对比稿素材 |
| [../../localization/korea/by-exam-kr.md](../../localization/korea/by-exam-kr.md) | 韩国考试维度本地化文档 |
| [../../tech-stack/thetawave-production-routing-i18n.md](../../tech-stack/thetawave-production-routing-i18n.md) | `/ko/` 多语种路由配置 |

---

## When adding a new post

1. Add `NN-{slug}-{year}.md` with frontmatter: `title`, `description`, `slug`, `date`, `author: "Kostja"`, `language: "ko"`, `locale: "ko-KR"`, `image`, `keywords`, `related`。
2. Ensure **`slug`** 为英文 kebab-case，匹配路径段 `/ko/blog/{slug}`（常青 slug 不含年份）。
3. 韩文正文中所有站内链使用 `/ko/` 前缀；外部韩文竞品链使用 `rel="nofollow noopener"`。
4. 发布后，确认 URL 出现在 `https://thetawave.ai/ko/blog/sitemap.xml`（若已配置）并在相关韩文功能页 / Use Cases 互链。

---

## Published drafts in this folder

| File | slug | `date` (publish) |
|------|------|------------------|
| [01-ai-tools-for-college-students-2026.md](./01-ai-tools-for-college-students-2026.md) | `ai-tools-for-college-students` | 2026-05-08 |
| [02-study-motivation-2026.md](./02-study-motivation-2026.md) | `study-motivation` | 2026-05-08 |
| [03-cornell-note-2026.md](./03-cornell-note-2026.md) | `cornell-note` | 2026-05-08 |
| [04-chatgpt-free-vs-thetawave-2026.md](./04-chatgpt-free-vs-thetawave-2026.md) | `chatgpt-free-vs-thetawave` | 2026-05-18 |
| [05-how-to-memorize-better-2026.md](./05-how-to-memorize-better-2026.md) | `how-to-memorize-better` | 2026-05-18 |
| [06-english-words-memorize-fast-2026.md](./06-english-words-memorize-fast-2026.md) | `english-words-memorize-fast` | 2026-05-18 |
| [07-toeic-study-method-ai-2026.md](./07-toeic-study-method-ai-2026.md) | `toeic-study-method-ai` | 2026-05-18 |
| [08-cramming-exam-ai-2026.md](./08-cramming-exam-ai-2026.md) | `cramming-exam-ai` | 2026-05-18 |
| [09-korean-history-exam-ai-2026.md](./09-korean-history-exam-ai-2026.md) | `korean-history-exam-ai` | 2026-05-18 |
| [10-lilys-vs-thetawave-2026.md](./10-lilys-vs-thetawave-2026.md) | `lilys-vs-thetawave` | 2026-05-18 |
| [11-wrtn-vs-thetawave-2026.md](./11-wrtn-vs-thetawave-2026.md) | `wrtn-vs-thetawave` | 2026-05-18 |
| [12-opic-ih-ai-guide-2026.md](./12-opic-ih-ai-guide-2026.md) | `opic-ih-ai-guide` | 2026-05-18 |
| [13-civil-service-exam-ai-2026.md](./13-civil-service-exam-ai-2026.md) | `civil-service-exam-ai` | 2026-05-18 |

---

*Folder prepared for Korean on-site blog drafts; extend the table as each post is added.*
