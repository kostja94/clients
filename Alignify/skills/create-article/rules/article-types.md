# 四种文章类型 × Markdown 结构

> **版本**：v3.2 · 2026-08-27  
> **格式**：`.md` frontmatter + `<!-- block:section -->` — TL;DR / FAQ / References 均在正文内  
> **原则**：类型决定 Meta、Hub、知识块目录；**正文架构由内容决定**，下文为各类型**常见结构（建议）**。

---

## 类型速查

| 类型 | 知识块 | **新文** 内容路径 | **新文** 路由 | **存量**（不重迁） | Hub 推导 |
|------|--------|------------------|--------------|-------------------|----------|
| Tools | `knowledge/tools/` | `content/blog/` | `/blog/{slug}` | `content/tools/` · `/tools/{slug}` | frontmatter `category` |
| Marketing | `knowledge/marketing/` | `content/blog/` | `/blog/{slug}` | `content/marketing/` · `/marketing/{slug}` | 独立 Hub |
| SEO | `knowledge/seo/` | `content/blog/` | `/blog/{slug}` | `content/seo/` · `/seo/{slug}` | 独立 Hub |
| Insights | `knowledge/insights/` | `content/blog/` | `/blog/{slug}` | `content/insights/` · `/insights/{slug}` | 独立 Hub |

> **路由约定（2026-08-28）**：**所有新文章**（任意类型）统一 **`content/blog/` + `/blog/{slug}`**（中文 `/zh/blog/{slug}`）。存量旧路径**仅维护更新，不重迁 URL**。  
> **已废弃**：JSON block 类型 `howToChoose` / `bestTools` / `howItWorks` / `useCases`；对应 React 组件已删除。

---

## Tools 型（Blog 新文）

**常见结构**见 [`anatomy.md`](./anatomy.md) §一参考菜单；完整写法参考 [`templates/best-ranking.md`](./templates/best-ranking.md)。

- 主体多为 Best 榜单：正文 section + 产品 H3
- 选型类常含：`## 如何选择…` + `###` 步骤
- FAQ：**7 问**（md 内 inline）— 若采用 FAQ 节

可省略：对比表、应用场景、如何工作等 — 见 Step 01 大纲说明。

---

## Marketing 型

**常见顺序**（可合并/调整）：

```
核心要点(md) → 概念 section → 策略 sections×N → [场景] → 结论 → FAQ(7, md) → [References(md)]
```

- 可选 frontmatter `heroHtml`
- Meta：策略型规则组
- 内链专规：[`marketing-internal-links.md`](./marketing-internal-links.md)

---

## SEO 型

**常见顺序**：

```
核心要点 → 概念 → 操作 sections（H3）→ [场景] → 结论 → FAQ(7) → [References]
```

- 列表/表格：`<!-- childrenHtml:start -->` + HTML（见 `anatomy.md` §四·一）
- Meta：指南型规则组

---

## Insights 型

**常见顺序**：

```
核心要点 → sections 或 html 长文 → 结论 → FAQ(7) → [References]
```

- Meta：分析型规则组

---

## Meta 规则组

| 类型 | title 模式 |
|------|-----------|
| Tools Best | `Best … (2026): …` / `最佳…（2026）：…` |
| Marketing | 策略/案例型（见 `meta.md`） |
| SEO | 指南型 |
| Insights | 分析型 |

H1 / excerpt 始终在 md frontmatter `title` / `description`。

---

## A 层硬底线（全类型）

- 结论与 FAQ 同时存在 → 结论在 FAQ 前
- FAQ 若存在 → 7 问、无内链、中英条数一致
- 禁止 frontmatter `howTo:`

---

*article-types · v3.2 · 2026-08-27*
