# Alignify Skills 索引

> **部署仓**：`E:\自有部署项目\alignify production` · **上下文仓**：`E:\clients\Alignify`

---

## 顶层 Skills

| Skill | 用途 |
|-------|------|
| [`create-article/`](./create-article/SKILL.md) | 新建/重写文章（12 步 flagship 流程） |
| [`audit-article/`](./audit-article/SKILL.md) | audit-ready → publish-ready 终审 |
| [`optimize-internal-links/`](./optimize-internal-links/SKILL.md) | 存量内链优化 + [**全站快照**](./optimize-internal-links/references/site-structure-internal-links.md) |
| [`ops/`](./ops/README.md) | 发布后 SEO / 索引 / OG |

> **已合并**：`create-blog-article`、`create-tools-article`、`localize-content-zh` → 均使用 `create-article`。

---

## 关键约定（2026-08-28）

| 主题 | 规则 |
|------|------|
| **新文路由** | 任意类型 → `content/blog/` + `/blog/{slug}`（中文 `/zh/blog/{slug}`） |
| **存量** | `/marketing/`、`/tools/`、`/seo/`、`/insights/` **不重迁**，仅维护 |
| **内链** | 点击意图优先；**无硬性条数**；同 URL 全页 1 次 |
| **结论内链** | 全类型允许 **0–2** 条（非清单式）— [`conclusion.md`](./create-article/rules/conclusion.md) |

---

## 规范 Hub（按需加载，勿一次全读）

| 主题 | SSOT |
|------|------|
| 结构原则 | [`anatomy.md`](./create-article/rules/anatomy.md) |
| 类型 / 路径 | [`article-types.md`](./create-article/rules/article-types.md) |
| 内链（全站） | [`internal-links.md`](./create-article/rules/internal-links.md) Part 1–2 |
| 内链（Marketing） | [`marketing-internal-links.md`](./create-article/rules/marketing-internal-links.md) |
| **全站快照** | [`optimize-internal-links/references/site-structure-internal-links.md`](./optimize-internal-links/references/site-structure-internal-links.md) |
| 结论 | [`conclusion.md`](./create-article/rules/conclusion.md) |
| Meta | [`meta.md`](./create-article/rules/meta.md) |
| 质检地图 | [`rules/README.md`](./create-article/rules/README.md) |

---

*skills README · 2026-08-27*
