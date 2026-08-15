# Sovi.AI — 杂项归档

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[mysovi-site-structure.md](./mysovi-site-structure.md) | [mysovi.md](./mysovi.md)

**Last updated**: 2026-06-24

---

## 1. Sitemap 明细

### 1.1 索引结构

```
https://mysovi.ai/sitemap.xml
├── sitemap-main.xml          (lastmod: 2026-05-25)
├── resources/sitemap.xml     (lastmod: 2026-05-25)
└── blog-sitemap.xml          (lastmod: 2026-05-25)
```

### 1.2 sitemap-main.xml（17 URL）

| URL | lastmod |
|-----|---------|
| https://mysovi.ai/ | 2026-04-03 |
| https://mysovi.ai/chat | 2026-04-03 |
| https://mysovi.ai/study | 2026-04-03 |
| https://mysovi.ai/apexam | 2026-04-03 |
| https://mysovi.ai/app | 2026-04-03 |
| https://mysovi.ai/about | 2026-04-03 |
| https://mysovi.ai/faq | 2026-04-03 |
| https://mysovi.ai/resources | 2026-04-03 |
| https://mysovi.ai/blog | 2026-04-03 |
| https://mysovi.ai/search | 2026-04-17 |
| https://mysovi.ai/privacy-policy | 2026-04-03 |
| https://mysovi.ai/terms-of-service | 2026-04-03 |
| https://mysovi.ai/apps/assignment-helper | 2026-05-14 |
| https://mysovi.ai/apps/cheatsheet | 2026-05-14 |
| https://mysovi.ai/apps/ai-notes | 2026-05-14 |
| https://mysovi.ai/apps/smart-writing | 2026-05-14 |
| https://mysovi.ai/apps/live-recording | 2026-05-14 |

### 1.3 resources/sitemap.xml（12 学科子 sitemap）

| 子 sitemap | 学科 |
|-----------|------|
| resource/sitemap-math-page-1.xml | math |
| resource/sitemap-statistics-page-1.xml | statistics |
| resource/sitemap-calculus-page-1.xml | calculus |
| resource/sitemap-physics-page-1.xml | physics |
| resource/sitemap-chemistry-page-1.xml | chemistry |
| resource/sitemap-biology-page-1.xml | biology |
| resource/sitemap-economics-page-1.xml | economics |
| resource/sitemap-literature-page-1.xml | literature |
| resource/sitemap-business-page-1.xml | business |
| resource/sitemap-social_science-page-1.xml | social_science |
| resource/sitemap-writing-page-1.xml | writing |
| resource/sitemap-others-page-1.xml | others |

**量级说明**：`sitemap-math-page-1.xml` 单文件含 **≥500** 条 URL；`/resources/category/math/` 分页观测至 **949+**，总题库规模预估 **数万～十万级**（**待验证** 全量爬取）。

### 1.4 blog-sitemap.xml（19 URL，节选）

| URL | lastmod |
|-----|---------|
| https://mysovi.ai/blog | — |
| https://mysovi.ai/blog/basic-knowledge/how-to-write-a-strong-argumentative-essay-in-5-simple-steps | 2026-04-13 |
| https://mysovi.ai/blog/basic-knowledge/how-to-write-a-strong-thesis-statement-in-5-simple-steps | 2026-04-13 |
| https://mysovi.ai/blog/basic-knowledge/how-to-write-a-professional-email-in-5-simple-steps-with-examples | 2026-04-13 |
| https://mysovi.ai/blog/basic-knowledge/understanding-transition-words-for-essays-types-examples-and-tips | 2026-04-13 |
| …（共 18 篇 basic-knowledge 文章） | 2026-04-13 |

完整列表见 [blog-sitemap.xml](https://mysovi.ai/blog-sitemap.xml)。

### 1.5 robots.txt 要点（2026-03-11）

- 策略：**OPEN ACCESS**，欢迎搜索引擎与 AI 爬虫索引公开内容
- Disallow：`/api/`、`/question-banks/`
- 显式 Allow：Googlebot、GPTBot、ChatGPT-User、ClaudeBot、PerplexityBot、Applebot 等

---

## 2. 内链原始聚合（首页 2026-06-24）

| anchorText | URL |
|------------|-----|
| Ask Sovi | /chat |
| Study Tools | /study |
| AP Test Prep | /apexam |
| Video Explanation | /video |
| Expert Help | /expert |
| Assignment Helper | /chat、/apps/assignment-helper |
| Cheatsheet | /study?tab=cheatsheet、/apps/cheatsheet |
| AI Notes | /study?tab=notes |
| Smart Writing | /study?tab=writing |
| Live Recording | /study?tab=recording |
| Resources | /resources |
| Blog | /blog |
| Search | /search |
| About Us / App | /about |
| FAQ | /faq |
| Careers | /apps/career/ |
| Get the App | App Store id6740720452 |
| 社交 | TikTok @sovi_ai0 · Reddit r/Sovi_ai · Instagram sovi_ai_official |

---

## 3. 数据引用

| 数据点 | 数值 | 来源 | 日期 |
|--------|------|------|------|
| 用户数 | 2M+ students, parents, teachers | [mysovi.ai](https://mysovi.ai/) 首页 | 2026-06-24 |
| 解题量 | 45M+ problems solved | 同上 | 2026-06-24 |
| 准确率 | 95% overall（站点）；首页另称 vs GPT/Gemini 对比 | 同上 | 2026-06-24 |
| App 评分 | 4.8（4.7K ratings） | [App Store US](https://apps.apple.com/us/app/sovi-ai-ai-study-companion/id6740720452) | 2026-06-24 |
| IAP 定价 | Weekly $3.99–$6.99 · Monthly $12.99 · Annual $89.99 | App Store US | 2026-06-24 |
| 开发商 | Edgewise Limited | App Store | 2026-06-24 |

---

## 4. 调研 Backlog

| ID | 需查证 | 优先级 |
|----|--------|--------|
| R1 | Semrush/Similarweb 流量与 Top 关键词 | P0 |
| R2 | Google Play 是否存在及下载量 | P1 |
| R3 | `/app` vs `/about` 关系与 canonical | P1 |
| R4 | question-banks.mysovi.ai 与主域 Resources 迁移状态 | P1 |
| R5 | AP 覆盖科目完整列表与「Real AP Questions」授权说明 | P1 |
| R6 | Web 端订阅价是否与 App IAP 一致 | P2 |
