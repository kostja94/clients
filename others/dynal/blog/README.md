# Dynal blog drafts

English Markdown articles for **dynal.ai** live in this folder (`*.md` with YAML frontmatter), aligned with live URL pattern **`/blog/{slug}`** (see [dynal-site-structure.md](../dynal-site-structure.md) — blog subtree and `/blog/sitemap.xml`).

**Topic backlog, LinkedIn generator cluster, and keyword notes**: [dynal-pg-topics.md](../linkedin-post-generator/dynal-pg-topics.md) §3 · [dynal-keywords.md](../dynal-keywords.md).

**Internal and external linking (distribution, `related`, maintenance table)**：见 **[INTERNAL-EXTERNAL-LINKS-CHECKLIST.md](./INTERNAL-EXTERNAL-LINKS-CHECKLIST.md)** — 以该清单为单一事实来源；下条为摘要。

**Body section headings (`##`):** Number main sections sequentially in English drafts—`## 1. …`, `## 2. …`, and so on—and leave **`## Conclusion`** and **`## Frequently asked questions`** **without** a leading numeral.

**When adding a new post**

1. Add `NN-{slug-kebab}-2026.md` (or agreed naming) here with frontmatter: `title`, `slug`, `excerpt`, `publishedAt`, `author`（标准 Markdown 稿用 `author: "Kostja"`；若导入 Sanity，作者引用 `author._ref: "kostja"`，展示名 **Kostja**）, `categories`, `related`（`related: ["other-slug"]` 与正文 `https://dynal.ai/blog/{slug}` 互链对齐；产品链按 **H2 分散**到首页 / solutions / vs / pricing，**避免**同一段塞满多条未解释的 URL）。**勿**在文稿 frontmatter 中加 `mainImage`。
2. Ensure **`slug`** matches the public path segment: `/blog/{slug}` (e.g. `types-of-linkedin-posts` → `/blog/types-of-linkedin-posts`).
3. After publish, confirm the URL appears in **https://dynal.ai/blog/sitemap.xml** and cross-link from Solutions / other posts as planned.

**Published drafts in this folder**

| File | slug | publish (`publishedAt` date) |
|------|------|-------------------------------|
| [01-types-of-linkedin-posts-2026.md](./01-types-of-linkedin-posts-2026.md) | `types-of-linkedin-posts` | 2026-04-16 |
| [02-how-to-get-clients-on-linkedin-2026.md](./02-how-to-get-clients-on-linkedin-2026.md) | `how-to-get-clients-on-linkedin` | 2026-04-17 |
| [03-linkedin-client-acquisition-playbook-2026.md](./03-linkedin-client-acquisition-playbook-2026.md) | `linkedin-client-acquisition-playbook` | 2026-04-18 |
| [04-linkedin-hooks-without-clickbait-2026.md](./04-linkedin-hooks-without-clickbait-2026.md) | `linkedin-hooks-without-clickbait` | 2026-04-19 |
| [05-linkedin-posts-from-notes-and-pdfs-2026.md](./05-linkedin-posts-from-notes-and-pdfs-2026.md) | `linkedin-posts-from-notes-and-pdfs` | 2026-04-20 |
| [06-linkedin-content-calendar-template-solo-2026.md](./06-linkedin-content-calendar-template-solo-2026.md) | `linkedin-content-calendar-template-solo` | 2026-04-21 |
| [07-linkedin-personal-profile-vs-company-page-2026.md](./07-linkedin-personal-profile-vs-company-page-2026.md) | `linkedin-personal-profile-vs-company-page` | 2026-04-22 |
| [08-linkedin-dms-b2b-without-spam-2026.md](./08-linkedin-dms-b2b-without-spam-2026.md) | `linkedin-dms-b2b-without-spam` | 2026-04-23 |
| [09-scheduling-linkedin-posts-time-zones-2026.md](./09-scheduling-linkedin-posts-time-zones-2026.md) | `scheduling-linkedin-posts-time-zones` | 2026-04-24 |
| [10-linkedin-brand-voice-guidelines-ai-2026.md](./10-linkedin-brand-voice-guidelines-ai-2026.md) | `linkedin-brand-voice-guidelines-ai` | 2026-04-25 |
| [11-linkedin-newsletter-vs-feed-posts-2026.md](./11-linkedin-newsletter-vs-feed-posts-2026.md) | `linkedin-newsletter-vs-feed-posts` | 2026-04-26 |
| [12-ai-for-linkedin-what-to-automate-2026.md](./12-ai-for-linkedin-what-to-automate-2026.md) | `ai-for-linkedin-what-to-automate` | 2026-04-27 |
| [13-best-linkedin-tools-2026.md](./13-best-linkedin-tools-2026.md) | `best-linkedin-tools` | 2026-04-28 |
| [14-how-to-create-linkedin-carousel-posts-2026.md](./14-how-to-create-linkedin-carousel-posts-2026.md) | `how-to-create-linkedin-carousel-posts` | 2026-05-07 |
| [15-linkedin-carousel-ads-complete-guide-2026.md](./15-linkedin-carousel-ads-complete-guide-2026.md) | `linkedin-carousel-ads-complete-guide` | 2026-05-07 |

---

*Folder created for blog-first drafts; registry table updates when each post is added.*
