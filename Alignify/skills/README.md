# Alignify Skills 索引

> **部署仓**：`E:\自有部署项目\alignify production` · **上下文仓**：`E:\clients\Alignify`

---

## 顶层 Skills

| Skill | 用途 |
|-------|------|
| [`create-article/`](./create-article/SKILL.md) | 新建/重写文章（12 步 flagship 流程） |
| [`audit-article/`](./audit-article/SKILL.md) | audit-ready → publish-ready 终审 |
| [`optimize-internal-links/`](./optimize-internal-links/SKILL.md) | 存量内链：[`workflow.md`](./optimize-internal-links/workflow.md) + [**全站快照**](./optimize-internal-links/references/site-structure-internal-links.md) |
| [`ops/`](./ops/README.md) | 发布后 SEO / 索引 / OG |

> **已合并**：`create-blog-article`、`create-tools-article`、`localize-content-zh` → 均使用 `create-article`。

---

## 关键约定（2026-08-28）

| 主题 | 规则 |
|------|------|
| **新文路由** | 任意类型 → `content/blog/` + `/blog/{slug}`（中文 `/zh/blog/{slug}`） |
| **模板定位** | [`templates.md`](./create-article/rules/templates.md) **仅为建议**；Answer Blocks 驱动，禁止一比一复刻 |
| **Intake** | 对文章不清楚时在**聊天中问用户** — [`intake-questions.md`](./create-article/rules/intake-questions.md) |
| **存量** | `/marketing/`、`/tools/`、`/seo/`、`/insights/` **不重迁**，仅维护 |
| **内链** | 点击意图优先；**无硬性条数**；同 URL 全页 1 次 |
| **结论内链** | 全类型允许 **0–2** 条（非清单式）— [`sections.md`](./create-article/rules/sections.md) Part 4.4 |

---

## 规范 Hub（按需加载，勿一次全读）

| 主题 | SSOT |
|------|------|
| 结构原则 | [`anatomy.md`](./create-article/rules/anatomy.md) |
| Intake 问答 | [`intake-questions.md`](./create-article/rules/intake-questions.md) |
| 类型 / 路径 | [`article-types.md`](./create-article/rules/article-types.md) |
| 页面模板（建议） | [`templates.md`](./create-article/rules/templates.md) |
| 节写法 | [`sections.md`](./create-article/rules/sections.md) |
| 内链（全站） | [`internal-links.md`](./create-article/rules/internal-links.md) Part 1–2 |
| 内链（Marketing M1–M11） | [`internal-links.md` Part 4.5](./create-article/rules/internal-links.md#part-45-marketing-频道内链) |
| **全站快照** | [`optimize-internal-links/references/site-structure-internal-links.md`](./optimize-internal-links/references/site-structure-internal-links.md) |
| 结论 / Final CTA | [`sections.md`](./create-article/rules/sections.md) Part 4–5 |
| Meta | [`meta.md`](./create-article/rules/meta.md) |
| 质检地图 | [`rules/README.md`](./create-article/rules/README.md) |

---

*skills README · 2026-08-27 · templates SSOT 合并*
