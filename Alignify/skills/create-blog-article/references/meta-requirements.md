# Blog Meta 规则

> **版本**：v2.0 · 2026-08-23
> **SSOT**：`content/sections/content-rules/section-meta-copy.md`

---

## 四要素

| 要素 | 位置 |
|------|------|
| Meta title / description | `*-meta.ts` en/zh |
| H1 / excerpt | md frontmatter `title` / `description` |

---

## Blog 新文（Tools Best 型）

- Meta title：含 `Best`/「最佳」、`(2026)`/`（2026）`、冒号副线
- H1：不写年份
- publishDate：meta ISO + md 展示格式双源同步

---

## Hub 配置（Blog 新文）

`blog-pages-config.ts`：**无 `routeCategory`**。填 `toolsHubCategory` 或 `marketingHubCategory` + hub 关键词；频道由 `category` 推导。

---

## 日期

| 位置 | 格式 |
|------|------|
| `*-meta.ts` | ISO `2026-07-16T00:00:00+08:00` |
| md frontmatter | `"2026年7月16日"` / `"July 16, 2026"` |

---

*meta-requirements · v2.0 · 2026-08-23*
