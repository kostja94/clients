# 四种文章类型 × Markdown 结构

> **版本**：v2.0 · 2026-08-23
> **格式**：`.md` frontmatter + `<!-- block:section|html -->` + 集中 JSON

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

10 节顺序见 [`create-tools-article/references/tools-article-anatomy.md`](../create-tools-article/references/tools-article-anatomy.md)。

- Best 榜单：正文 section + 产品 H3（非 BestTools 组件）
- 如何选择：正文 `## 如何选择…` + `###` 步骤
- FAQ：**7 问**（`faq-data.json`）

---

## Marketing 型

```
TL;DR(JSON) → 概念 section → 策略 sections×N → 场景 → 结论 → FAQ(7) → References
```

- 可选 frontmatter `heroHtml`
- Meta：策略型规则组

---

## SEO 型

```
TL;DR(JSON) → 概念 → 操作 sections（H3）→ 场景 → 结论 → FAQ(7) → References
```

- 代码/表格：`<!-- block:html -->`
- Meta：指南型规则组

---

## Insights 型

```
TL;DR(JSON) → html 长文 block 或 sections → 结论 → FAQ(7) → References
```

- Meta：分析型规则组

---

## Meta 规则组

| 类型 | title 模式 |
|------|-----------|
| Tools Best | `Best … (2026): …` / `最佳…（2026）：…` |
| Marketing | 策略/案例型（见 `meta-requirements.md`） |
| SEO | 指南型 |
| Insights | 分析型 |

H1 / excerpt 始终在 md frontmatter `title` / `description`。

---

*article-types · v2.0 · 2026-08-23*
