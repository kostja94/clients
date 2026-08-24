# Project Task Tracker

> 营销与 SEO 任务追踪。**Last updated**: 2026-08-08

---

## Related Documents

| 文档 | 用途 |
|------|------|
| [README.md](../README.md) | 仓库入口与目录 |
| [project-context.md](../specs/project-context.md) | 产品、受众、关键词 |
| [reference.md](../specs/reference.md) | 内容与 SEO 规范 |
| [internal-links.md](../knowledge/internal-links.md) | 内链清单与策略 |

---

## Progress Summary

| Status | Count |
|--------|-------|
| **Pending / In Progress** | ~13 |
| **Done** | ~72 |

**Workflow order**: Technical SEO → On-Page → Content

| Priority | Meaning |
|----------|---------|
| **P0** | 阻塞项 |
| **P1** | 高 — 核心 SEO/营销 |
| **P2** | 中 |
| **P3** | 低 |

---

## 1. Technical SEO

| Task | Status | Priority | Notes |
|------|--------|----------|-------|
| sitemap.xml | Done | P0 | app/sitemap.ts |
| Canonical URLs | Done | P1 | alternates.canonical |
| robots.txt | Pending | P0 | 检查默认配置 |
| Indexing (GSC) | Pending | P1 | |
| IndexNow (Bing) | Done | P2 | INDEXNOW_KEY + public/{key}.txt |
| Crawlability | Pending | P0 | redirects, orphans |
| Content version accuracy | Done | P1 | Sora 移除、模型版本全局修正 2026-05 |

---

## 2. On-Page SEO

| Task | Status | Priority | Notes |
|------|--------|----------|-------|
| Title tag | In Progress | P1 | 50–60 字符 |
| Meta description | In Progress | P1 | 120–158 字符 |
| Open Graph / Twitter | In Progress | P2 | 与 meta 一致 |
| Schema | Done | P1 | WebSite, Organization, FAQ |
| Internal linking | Done | P1 | 35/35 已补全（2026-08-08），见 internal-links.md |
| Heading structure | In Progress | P1 | sections id 已统一 |
| Image optimization | Pending | P1 | Alt、LCP |

---

## 3. Content SEO

| Task | Status | Priority | Notes |
|------|--------|----------|-------|
| Products description 300–600 | Done | P1 | |
| Topics 正文与 Meta | In Progress | P1 | content/topics/*.json |
| Version sweep | Done | P1 | ~60 修正 2026-05 |
| Sora 全面移除 | Done | P0 | 2026-05 |

---

## 4. Products 优化（进行中）

| 目标 | 状态 |
|------|------|
| meta title 50–60 字符 | In Progress |
| meta description 120–158 字符 | In Progress |
| subtitle 40–80 字符 | Pending |

规范见 [reference.md](../specs/reference.md)、[content-model.md](../specs/content-model.md)。

---

## 5. Pending Next Steps

| Priority | Task | Notes |
|----------|------|-------|
| P0 | `python capture-screenshots.py --target products` | meta, questionai, talkie-ai |
| P2 | 32 SEO meta edge cases | 标题/描述过短，需人工扩写 |
| P2 | Company screenshots | `--target companies` |
| P3 | robots.txt / crawlability | §1 Pending |

---

## Quick Reference

| Section | When |
|---------|------|
| 1. Technical SEO | 优先 — robots、crawlability |
| 2. On-Page | Meta 逐页达标 |
| 3. Content | Topics 迭代；版本查 knowledge/topics/ |
| 5. Pending | P0 → P1 → P2 |
