# Alignify Skills 索引

> **部署仓**：`E:\自有部署项目\alignify production` · **上下文仓**：`E:\clients\Alignify`  
> **最后更新**：2026-09-03

---

## 顶层 Skills

| Skill | 用途 |
|-------|------|
| [`create-article/`](./create-article/SKILL.md) | **构建新文章**（flagship：01–10 成稿 + Step 11 新会话终审） |
| [`audit-optimize/`](./audit-optimize/SKILL.md) | **审核并优化老文章**：retro · 内链 · refresh · page-audit |
| [`knowledge-block/`](./knowledge-block/SKILL.md) | **知识块**维护：slug 分流、keyword 映射、**垂类产品池**、SSOT、站内相邻；**Tools 簇临时 brief 成稿后删除**（非成稿） |
| [`ops/`](./ops/README.md) | 发布后 SEO / 索引 / OG / RSS |

> **已合并进 create-article**：`create-blog-article` · `create-tools-article` · `localize-content-zh` · **`audit-article` 终审轨（→ Step 11）**  
> **已合并进 audit-optimize**：`audit-article` retro · `optimize-internal-links`

---

## create-article 步骤（当前）

| 步骤 | 文档 | 说明 |
|------|------|------|
| 01 | [`01-intake.md`](./create-article/01-intake.md) | Gate A |
| 02 | [`02-research.md`](./create-article/02-research.md) | Gate 0R + Brief |
| 03 | [`03-keywords.md`](./create-article/03-keywords.md) | 关键词 + README |
| 04 | [`04-screenshots.md`](./create-article/04-screenshots.md) | 截图（best-ranking / legacy） |
| 05–06 | [`content-locale.md`](./create-article/rules/content-locale.md) Part 2–3 | ZH 起草 + 地道化 |
| 07 | [`07-internal-links.md`](./create-article/07-internal-links.md) | 内链 + Link Plan |
| 08 | [`08-meta-config.md`](./create-article/08-meta-config.md) | Meta · JSON 侧车 · **publishDate/modifiedDate** · Final CTA |
| 09–09c | [`content-locale.md`](./create-article/rules/content-locale.md) Part 4–5 | EN 独立成稿 + 对等对比 |
| 10 | [`10-quality-gates.md`](./create-article/10-quality-gates.md) | Gate C → audit-ready |
| 11 | [`11-final-audit.md`](./create-article/11-final-audit.md) | **新会话**终审 → publish-ready |
| 发布 | — | 人类发布（复核 Step 08 日期） |

---

## audit-optimize 模式

| 模式 | 文档 | 说明 |
|------|------|------|
| retro | [`01-retro.md`](./audit-optimize/01-retro.md) | 已发稿健康检查 |
| links | [`02-links.md`](./audit-optimize/02-links.md) · [`workflow.md`](./audit-optimize/workflow.md) | 存量内链 |
| refresh | [`03-refresh.md`](./audit-optimize/03-refresh.md) | 事实 / SERP / Meta / 结构刷新 |
| 质检 | [`rules/page-audit.md`](./audit-optimize/rules/page-audit.md) | P0 + 十维（与新文终审阈值对齐） |
| 快照 | [`site-structure-internal-links.md`](./audit-optimize/references/site-structure-internal-links.md) | 全站内链快照 |

---

## 关键约定

| 主题 | 规则 |
|------|------|
| **新文路由** | 任意类型 → `content/blog/` + `/blog/{slug}` |
| **模板** | [`templates.md`](./create-article/rules/templates.md) **建议非施工图** |
| **章节** | [`sections.md`](./create-article/rules/sections.md) SSOT（Part 0–5，含结论与 Final CTA） |
| **双语** | 双轨 native 成稿 → [`content-locale.md`](./create-article/rules/content-locale.md) |
| **术语** | [`locale-glossary.md`](./create-article/rules/locale-glossary.md) + `.json` |
| **内链 + 外链** | [`internal-links.md`](./create-article/rules/internal-links.md) Part 1–8 |
| **Intake** | 不清楚时在聊天问用户 — [`intake-questions.md`](./create-article/rules/intake-questions.md) |
| **Tools 产品** | 垂类 spoke · 默认 **3 款** H3 · **一产品一 canonical** — [`product-coverage.md`](./create-article/rules/product-coverage.md) |
| **Tools 簇 brief** | 会话内 `knowledge/tools/{cluster}/_briefs/*.md` · **KB 正文完成后删除** — [`knowledge-block/references/tools-cluster-ephemeral-brief.md`](./knowledge-block/references/tools-cluster-ephemeral-brief.md) |
| **Work Agent 簇** | Hub `work-agent` + Spoke `workspace-agent` + `ai-employee` — [`knowledge-block/references/work-agent-cluster.md`](./knowledge-block/references/work-agent-cluster.md) · [`ai-employee-cluster.md`](./knowledge-block/references/ai-employee-cluster.md) |

---

## 规范 Hub（按需加载）

| 主题 | SSOT |
|------|------|
| 质检地图 | [`create-article/rules/README.md`](./create-article/rules/README.md) |
| 结构原则 | [`anatomy.md`](./create-article/rules/anatomy.md) |
| 类型 / 路径 | [`article-types.md`](./create-article/rules/article-types.md) |
| Meta | [`meta.md`](./create-article/rules/meta.md) |
| 内链 Marketing M1–M11 | [`internal-links.md` Part 4.5](./create-article/rules/internal-links.md#part-45-marketing-频道内链) |
| 外链 UTM/Nofollow | [`internal-links.md` Part 8](./create-article/rules/internal-links.md#part-8-外链utm-与-nofollow) |
| 全站内链快照 | [`site-structure-internal-links.md`](./audit-optimize/references/site-structure-internal-links.md) |

---

## 已删除 / 已合并（勿再引用）

| 旧路径 | 现 SSOT |
|--------|---------|
| `audit-article/` | 终审 → [`create-article/11-final-audit.md`](./create-article/11-final-audit.md)；retro → [`audit-optimize/01-retro.md`](./audit-optimize/01-retro.md) |
| `optimize-internal-links/` | [`audit-optimize/`](./audit-optimize/SKILL.md) |
| `05-zh-content.md` · `06-localize-zh.md` · `09-en-content.md` · `localization-quality.md` | [`content-locale.md`](./create-article/rules/content-locale.md) |
| `terminology.md` · `terminology-glossary.md` · `marketing-glossary.json` | [`locale-glossary.md`](./create-article/rules/locale-glossary.md) + `.json` |
| `11-publish-dates.md` · `12-legacy-tools-dates.md` | [`08-meta-config.md`](./create-article/08-meta-config.md) §发布日期 |
| `utm-nofollow.md` | [`internal-links.md`](./create-article/rules/internal-links.md) Part 8 |
| `rules/sections/` · `conclusion.md` · `final-cta.md` | [`sections.md`](./create-article/rules/sections.md) |
| `rules/templates/` 子目录 | [`templates.md`](./create-article/rules/templates.md) |
| `marketing-internal-links.md` | [`internal-links.md`](./create-article/rules/internal-links.md) Part 4.5 |
| `aesthetic-hero.md` | 个人知识库 `首屏与插图美学参考-Hero-Illustration.md`（`设计-Design/首屏与插图美学参考-Hero-Illustration.md`） |

---

*skills README · v3.0 · 2026-09-03*
