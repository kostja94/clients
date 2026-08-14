# Hellyeah Blog

> **职责**：博客成稿文件表、hub-spoke 索引、下一序号。  
> **Skill**：创作时使用 `hellyeah/skills/hellyeah-blog-article/`（Agent 创作阶段不读本文件；Phase 6 提示人类更新）。

**Last updated**: 2026-06-15  
**Blog URL prefix**: `https://www.hellyeahai.com/blog/`  
**Blog status**: ⚠️ sitemap 未收录（2026-06-02）；成稿以 `status: draft` 标注直至上线。

---

## 文件表

| NN | 文件 | slug | 类型 | 文稿 | 主站 | 主关键词 |
|----|------|------|------|:---:|:---:|---------|
| 01 | 01-what-is-hellyeah-ai.md | `/blog/what-is-hellyeah-ai` | PlatformExplainer | ✅ | draft | Hellyeah AI |

**下一序号：02**

---

## Hub-Spoke 结构（规划）

```
                    ┌─────────────────────────────────────┐
                    │  01 What Is Hellyeah AI (Intro Hub)  │
                    │  Command layer + four-platform OS    │
                    └──────────────┬──────────────────────┘
                                   │
     ┌─────────────┬───────────────┼───────────────┬─────────────┐
     │             │               │               │             │
  (planned)    (planned)      (planned)      (planned)    (planned)
  programmatic continuous   ai-ads-        aima-vs-     enterprise
  geo pillar   experiments  manager        forge        security
```

**Canonical GEO 页**：`/capabilities/seo-geo` — 博客 GEO 话题须链回该页。

---

## P0 队列（待写）

| 优先级 | 类型 | 建议 slug | 主关键词 |
|--------|------|-----------|---------|
| P0 | Pillar | `programmatic-geo-vs-seo` | programmatic GEO |
| P0 | Framework | `continuous-growth-experiments` | continuous growth experiments |
| P1 | CommercialEducational | `what-is-ai-ads-manager` | AI ads manager |
| P1 | PlatformExplainer | `aima-vs-forge-vs-mutation` | AI growth platform architecture |
| P2 | Compliance | `enterprise-marketing-platform-security` | SOC 2 marketing platform |

---

## 命名约定

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{working-slug}.md` |
| NN | 两位递增；当前下一号为 **02** |
| frontmatter `slug` | `/blog/{url-slug}` |
| 作者默认 | Kostja |
