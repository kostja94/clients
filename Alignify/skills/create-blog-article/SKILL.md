# Create Blog Article — Alignify 通用文章创建 Skill

> **版本**：v1.3 · 2026-08-23
> **正文**：`content/{blog|seo|marketing|insights}/{locale}/{slug}.md`
> **集中 JSON**：`tldr-data.json` / `faq-data.json` / `references-data.json`
> **HowTo**：正文 section only；**禁止** frontmatter `howTo:`

---

## 与 create-tools-article 的分工

| 场景 | Skill |
|------|-------|
| Tools 榜单/对比（新文 → `/blog/`） | [`create-tools-article`](../create-tools-article/SKILL.md) |
| Marketing / SEO / Insights 长文 | **本 Skill** |
| 存量 `/tools/` 页维护 | `create-tools-article` Step 7 |

---

## 路由与内容路径

| 类型 | 路由 | 正文 | Meta / Config |
|------|------|------|---------------|
| Blog 新文（Tools 型） | `/blog/{slug}` | `content/blog/` | `blog-meta.ts` / `blog-pages-config.ts` |
| SEO | `/seo/{slug}` | `content/seo/` | `seo-meta.ts` / `seo-pages-config.ts` |
| Marketing | `/marketing/{slug}` | `content/marketing/` | `marketing-meta.ts` / `marketing-pages-config.ts` |
| Insights | `/insights/{slug}` | `content/insights/` | `insights-meta.ts` / `insights-pages-config.ts` |
| 存量 Tools | `/tools/{slug}` | `content/tools/` | `tools-meta.ts` / `tools-pages-config.ts` |

**Hub 归属**：Blog 新文由 frontmatter `category` 推导；`blog-pages-config.ts` **无** `routeCategory`。

---

## 流程总览

Step 1 Intake → Step 2 Research → Step 3 中文 md + JSON → Step 4 Meta → Step 5 英文 md → Step 6 质量门控 → Step 7 日期错开

各步文档见本目录 `01`–`07`。

---

## 质量检查

```bash
npm run verify:content-json
npm run build
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --locale both --violations-only
```

**Gate P0（2026-08-23）**：
- ✅ 无 frontmatter `howTo:`
- ✅ HowTo 正文 section（如适用）
- ✅ FAQ **7 问**
- ✅ 结论在 FAQ 之前
- ❌ ~~howToChoose JSON~~、~~HowTo JSON-LD~~、~~audit:howto-choose~~

---

*create-blog-article · v1.3 · 2026-08-23*
