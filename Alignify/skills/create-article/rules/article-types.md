# 四种文章类型 × Markdown 结构

> **版本**：v3.1 · 2026-08-26  
> **格式**：`.md` frontmatter + `<!-- block:section -->` — TL;DR / FAQ / References 均在正文内  
> **原则**：类型决定路径、Meta、Hub；**正文架构由内容决定**，下文为各类型**常见结构（建议）**。

---

## 类型速查

| 类型 | 知识块 | 内容路径 | 路由 | Hub 推导 |
|------|--------|---------|------|---------|
| Tools（新） | `knowledge/tools/` | `content/blog/` | `/blog/` | frontmatter `category` |
| Marketing | `knowledge/marketing/` | `content/marketing/` | `/marketing/` | 独立 Hub |
| SEO | `knowledge/seo/` | `content/seo/` | `/seo/` | 独立 Hub |
| Insights | `knowledge/insights/` | `content/insights/` | `/insights/` | 独立 Hub |

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

---

## SEO 型

**常见顺序**：

```
核心要点 → 概念 → 操作 sections（H3）→ [场景] → 结论 → FAQ(7) → [References]
```

- 代码/表格：`<!-- block:html -->`
- Meta：指南型规则组

---

## Insights 型

**常见顺序**：

```
核心要点 → html 长文 block 或 sections → 结论 → FAQ(7) → [References]
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

*article-types · v3.1 · 2026-08-26*
