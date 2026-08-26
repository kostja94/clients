# 正文章节写法（Markdown）

> **新文（2026-08+）**：一律 `content/blog/` 或 `content/tools/` 的 md + `<!-- block:section -->` + Markdown `##` / `###` + `{#anchor}`。详见 [`anatomy.md`](../anatomy.md) §四·一。

---

## 一、基本结构

```markdown
<!-- block:section -->
## 章节标题 {#kebab-case-id}

首段 BLUF ≥3 句（策略/marketing 文）。

第二段展开…

### 子节标题 {#sub-id}

…
```

- 列表 / 表格 → `childrenHtml`（`content-html` + 语义 class，E35）
- 段落 → 裸 Markdown，**禁止** inline Tailwind（E35）

---

## 二、H1 / H2 / excerpt

| 元素 | 来源 | 规范 |
|------|------|------|
| H1 | frontmatter `title` | [meta.md](../meta.md) §三 · [generic 层级](#三h1h6-层级) |
| excerpt | frontmatter `description` | [meta.md](../meta.md) §四 |
| H2/H3 | 正文 `##` / `###` | kebab-case `{#id}`；ZH/EN 同 slug 用相同 id |

---

## 三、H1–H6 层级

完整可访问性与字数规范见下文及 [meta.md](../meta.md)、[consistency.md](../consistency.md)。

**H1**：`[主题]：[价值]`；不写年份。

**H2 间距**：容器 `space-y-12`；正文 H2 之间**不加** divider（E36）。

---

## 四、与专用章节的关系

| 章节 | 写法 | 文档 |
|------|------|------|
| 核心要点 | `tldr-data.json`（Step 08） | [tldr.md](./tldr.md) |
| 产品展示 | `###` 产品 H3 + 段落 | [best-tools.md](./best-tools.md) |
| 如何选择 | `## 如何选择…` + H3 步骤 | [how-to.md](./how-to.md) |
| FAQ | `faq-data.json`（Step 08 · 页底） | [faq.md](./faq.md) |
| References | `references-data.json`（Step 08） | [references.md](./references.md) |

---

*generic · v2.0 · 2026-08-27*
