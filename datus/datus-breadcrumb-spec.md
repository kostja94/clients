# Datus — 面包屑规范

> **本文档职责**：面包屑 UI 层级、标签约定、BreadcrumbList JSON-LD；供实现者与 Agent 在新建/编辑页面时统一引用。  
> **引用**：[datus-site-structure.md](./datus-site-structure.md)（URL 架构） | [datus.md](./datus.md)（概览）

**最近更新**：2026-06-21

---

## 一、总则

| 规则 | 说明 |
|------|------|
| **首页例外** | **`/` 不展示面包屑**（无上级页面） |
| **其余页面** | 所有 sitemap 内页面及 `/blog/{slug}/` 独立内容页 **必须** 有可见面包屑 + 匹配的 JSON-LD |
| **语言** | 面包屑 **标签用英文**（与线上一致）；本文档说明用中文 |
| **末级** | 当前页标签 = 页面 H1 或 frontmatter `title`（过长时可截断至 ~60 字符，但 JSON-LD 用完整 title） |
| **分隔符** | UI 推荐 `>` 或 `/`；Schema 不依赖分隔符 |
| **可访问性** | 使用 `<nav aria-label="Breadcrumb">` + 有序列表；末级 `aria-current="page"` |

---

## 二、层级规则（按页面类型）

站点 URL 模型见 [datus-site-structure.md](./datus-site-structure.md)。以下为 **推荐层级**（`/` = 首页）。

### 2.1 顶层营销页

| 路径模式 | 面包屑层级 | 中间节点 URL |
|----------|------------|--------------|
| `/pricing/` | Home > Pricing | — |
| `/integrations/` | Home > Integrations | — |
| `/faq/` | Home > FAQ | — |
| `/glossary/` | Home > Glossary | — |

### 2.2 产品页 `/products/{product}/`

| 路径 | 面包屑层级 | 末级标签 |
|------|------------|----------|
| `/products/cli/` | Home > Products > Datus CLI | Datus CLI |
| `/products/vscode/` | Home > Products > VS Code Extension | VS Code Extension |
| `/products/studio/` | Home > Products > Datus Studio | Datus Studio |
| `/products/enterprise/` | Home > Products > Enterprise | Enterprise |

**Products 中间层**：

- 当前 sitemap **无** `/products/` 聚合页。
- **UI**：显示 `Products` 为不可点击文本（避免链向任意单品页）。
- **JSON-LD**：仅包含有 canonical URL 的节点——暂用 **两级** `Home > {Product}`，待 `/products/` 上线后改为三级并更新 `@id`。

### 2.3 Blog 索引 `/blog/`

| 面包屑 |
|--------|
| Home > Blog |

### 2.4 Blog 独立内容（扁平 slug）`/blog/{slug}/`

| 类型 | 面包屑层级 |
|------|------------|
| 普通文章 / Glossary 术语 / DE Agent 文 | Home > Blog > {Article Title} |
| 对比 / 列表文 | 同上（不因 Glossary 而插入 Glossary 层——术语 canonical 在 `/blog/`，非 `/glossary/{term}`） |

**Glossary 术语页**（如 `/blog/what-is-semantic-layer/`）：**不要** 写 `Home > Glossary > …`；索引页 `/glossary/` 与术语正文是不同 URL 角色。

### 2.5 Blog 专题 Hub `/blog/{hub}/`

| 路径 | 面包屑 |
|------|--------|
| `/blog/data-engineering-agent/` | Home > Blog > Data Engineering Agent |

Hub 页 `title` 来自页面 H1；slug 目录名 `data-engineering-agent` → 标签 **Data Engineering Agent**（Title Case，非 slug 字面量）。

### 2.6 Blog 嵌套路径 `/blog/{hub}/{slug}/`

| 路径 | 面包屑 |
|------|--------|
| `/blog/data-engineering-agent/data-engineering-agent-layered-subagent/` | Home > Blog > Data Engineering Agent > {Article Title} |

Hub 节点链向 hub URL；末级为当前文标题。

### 2.7 未上线 / 站外

| 范围 | 规则 |
|------|------|
| `docs.datus.ai` | **不在** 本规范范围；文档站自有 nav |
| 规划路径（`/agent`、`/use-cases/*` 等） | 上线时在本文档追加一行；发布前不写面包屑 |

---

## 三、标签约定

| 节点 | 固定英文标签 | URL |
|------|--------------|-----|
| 首页 | Home | `https://datus.ai/` |
| 产品（中间层） | Products | 待 `/products/` 上线后补 `https://datus.ai/products/` |
| Blog 索引 | Blog | `https://datus.ai/blog/` |
| 定价 / 集成 / FAQ / 术语索引 | Pricing / Integrations / FAQ / Glossary | 各对应顶层 URL |
| 末级 | 页面 `title` 或 H1 | 当前页 canonical URL |

**命名**：产品名用官网品牌写法（Datus CLI、Datus Studio）；文章用 frontmatter `title` 的主标题部分，去掉 SEO 后缀（如 “Definition, Examples & …” 可省略，保留核心题头）。

---

## 四、BreadcrumbList JSON-LD

### 4.1 要求

- 每页 **一个** `BreadcrumbList`；与可见面包屑 **逐项一致**（名称 + URL 一一对应）。
- 使用 JSON-LD，`<script type="application/ld+json">` 置于页面 `<head>` 或 body 顶部。
- `@id`：建议 `{canonicalUrl}#breadcrumb`。
- `itemListElement`：按 `position` 从 1 递增。
- **除末级外**，每项必须有 `item`（完整 URL 字符串）。
- **末级**：必须有 `name`；`item` 可省略（Google 接受）或与 canonical 相同。
- 无 URL 的中间层（当前 Products）**不要** 写入 schema。

### 4.2 模板

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://datus.ai/PAGE-PATH/#breadcrumb",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://datus.ai/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "MIDDLE-LABEL",
      "item": "https://datus.ai/middle-path/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "CURRENT PAGE TITLE"
    }
  ]
}
```

### 4.3 校验

- [Google Rich Results Test](https://search.google.com/test/rich-results)
- 可见 crumb 数量 = `itemListElement` 数量
- 末级 `name` 与 H1 一致

---

## 五、完整示例

### 5.1 `/products/cli/`

**可见**：Home > Products > Datus CLI  

**JSON-LD**（当前无 `/products/` 索引，两级）：

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://datus.ai/products/cli/#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://datus.ai/" },
    { "@type": "ListItem", "position": 2, "name": "Datus CLI" }
  ]
}
```

### 5.2 `/pricing/`

**可见**：Home > Pricing  

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://datus.ai/pricing/#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://datus.ai/" },
    { "@type": "ListItem", "position": 2, "name": "Pricing" }
  ]
}
```

### 5.3 `/glossary/`

**可见**：Home > Glossary  

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://datus.ai/glossary/#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://datus.ai/" },
    { "@type": "ListItem", "position": 2, "name": "Glossary" }
  ]
}
```

### 5.4 `/blog/what-is-semantic-layer/`

**可见**：Home > Blog > What Is a Semantic Layer?  

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://datus.ai/blog/what-is-semantic-layer/#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://datus.ai/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://datus.ai/blog/" },
    { "@type": "ListItem", "position": 3, "name": "What Is a Semantic Layer?" }
  ]
}
```

### 5.5 `/blog/best-data-engineering-agents/`

**可见**：Home > Blog > Best Data Engineering Agents  

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://datus.ai/blog/best-data-engineering-agents/#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://datus.ai/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://datus.ai/blog/" },
    { "@type": "ListItem", "position": 3, "name": "Best Data Engineering Agents" }
  ]
}
```

### 5.6 `/blog/data-engineering-agent/`（Hub）

**可见**：Home > Blog > Data Engineering Agent  

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://datus.ai/blog/data-engineering-agent/#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://datus.ai/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://datus.ai/blog/" },
    { "@type": "ListItem", "position": 3, "name": "Data Engineering Agent" }
  ]
}
```

### 5.7 嵌套示例 `/blog/data-engineering-agent/data-engineering-agent-layered-subagent/`

**可见**：Home > Blog > Data Engineering Agent > {文标题}  

Hub 节点 `item`: `https://datus.ai/blog/data-engineering-agent/`

---

## 六、实现备注

| 项 | 建议 |
|----|------|
| **组件** | 全站单一 `Breadcrumb` 组件；传入 `items: { label, href? }[]` |
| **CMS / Blog** | frontmatter 可选 `breadcrumbLabel`（覆盖末级）；`parentHub` + `hubLabel` 用于嵌套路径 |
| **Blog 构建** | 由 `slug` 解析：`/blog/a/b/` → hub=`a`；查 hub 元数据得 hub 标签 |
| **与 FAQ 关系** | 面包屑在 hero 下、正文上；FAQ 区块不影响 breadcrumb 层级 |

### Frontmatter 扩展（Blog，可选）

```yaml
breadcrumbLabel: "What Is a Semantic Layer?"   # 覆盖末级显示
parentHub: "data-engineering-agent"              # 嵌套路径必填
hubLabel: "Data Engineering Agent"               # Hub 显示名
```

---

## 七、Agent 规则（机器可读）

### 7.1 决策树

```
INPUT: page_url, page_title, optional parent_hub

IF page_url == "/" OR page_url == "":
  → NO breadcrumb UI, NO BreadcrumbList schema
  → STOP

items = [{ label: "Home", href: "https://datus.ai/" }]

IF page_url matches ^/products/[^/]+/?$:
  → UI append { label: "Products", href: null }  # 直到 /products/ 存在
  → schema: skip Products node; append { label: product_title } only after Home
  → product_title from mapping: cli→Datus CLI, vscode→VS Code Extension, studio→Datus Studio, enterprise→Enterprise

ELIF page_url in ["/pricing/", "/integrations/", "/faq/", "/glossary/"]:
  → append single segment: Pricing | Integrations | FAQ | Glossary

ELIF page_url == "/blog/" OR page_url == "/blog":
  → append { label: "Blog", href: "https://datus.ai/blog/" }

ELIF page_url matches ^/blog/([^/]+)/([^/]+)/?$ AND segment2 is NOT empty slug file:
  → IF known_hub(segment1):
      append Blog
      append { label: hubLabel(segment1), href: https://datus.ai/blog/{hub}/ }
      append { label: page_title }
  → ELSE treat as flat /blog/{slug}/:
      append Blog
      append { label: page_title }

ELIF page_url matches ^/blog/[^/]+/?$:
  → append Blog
  → append { label: page_title }
  → DO NOT insert Glossary even if category==Glossary

OUTPUT: visible breadcrumb + BreadcrumbList JSON-LD with parity check
```

### 7.2 硬规则

```yaml
breadcrumb_rules:
  homepage_excluded: true
  label_language: en
  schema_type: BreadcrumbList
  schema_parity: required  # visible == JSON-LD names and URLs
  glossary_term_url: /blog/{slug}/  # never /glossary/{term}
  glossary_index_url: /glossary/    # separate crumb path
  max_depth: 4  # Home > Blog > Hub > Article
  forbidden:
    - breadcrumb on homepage
    - Glossary parent for /blog/what-is-* terms
    - schema item without URL for non-terminal items (except Products until index exists)
    - English doc labels on Chinese-only pages (N/A for datus.ai)
```

### 7.3 发布前检查清单

- [ ] 非首页页面有可见面包屑
- [ ] 末级与 H1/`title` 一致
- [ ] JSON-LD 项数与 UI 一致
- [ ] 所有非末级 `item` URL 可 200
- [ ] Hub 嵌套文含 hub 中间层
- [ ] Glossary **术语** 文走 Blog 路径，不插 Glossary 层

---

*面包屑规范 · Datus · https://datus.ai/ · 见 [datus-site-structure.md](./datus-site-structure.md)*
