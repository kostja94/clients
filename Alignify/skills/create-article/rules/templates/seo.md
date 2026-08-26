# SEO 页面模板

本文档为 Alignify SEO 类页面的标准模板，用于创建或优化 SEO 指南页面（如 Schema、链接建设、Landing Page、搜索引擎、SERP 等）。

**参考**：content-rules、[section 文档](../README.md)、[bloglayout](./bloglayout.md)、[section-consistency](../consistency.md)（字数与表达一致性）· **SEO 关键词与 slug 意图**：`alignify-keywords-seo.md`

---

## 〇、一致性规范（必读）

**目标**：同一类型（SEO）页面之间 **H2 格式、信息顺序、语气** 一致；正文篇幅见 [section-consistency §〇–§二](../consistency.md)。

- **跨页面**：结构、标题格式与表达习惯对齐；**不**强制各章总字数逐页相等
- **章节间**：避免极短与极长章节相邻
- **章节内**：并列块不宜约 3 倍以上长短差

**统一篇幅**：见 [section-consistency](../consistency.md)（含 §〇 字数层级）；正文以建议区间与自然分段为准；meta/H1/excerpt 仍宜遵守专项文档。

---

## 一、页面结构

```
1. 核心要点（TL;DR，40–80字 intro + 4–5 条 items）← [tldr.md](../sections/tldr.md)
2. 什么是 XXX（建议篇幅见 [consistency.md](../consistency.md)）← [what-is.md](../sections/what-is.md)
3. XXX 如何工作 / 核心原理
4. ... 正文内容（按主题展开，`<!-- block:section -->` + Markdown）...
5. How To（可选，如「如何优化面包屑」）← [how-to.md](../sections/how-to.md)
6. Conclusion（总结）← [conclusion.md](../conclusion.md)
7. FAQ（常见问题）← [faq.md](../sections/faq.md)
8. References（引用，如有）← [references.md](../sections/references.md)
```

**标准顺序**：How To → Conclusion → FAQ → References

---

## 二、Metadata 与 frontmatter

> Meta title/description：[meta.md](../meta.md) §一–二。H1/excerpt：md frontmatter `title` / `description`。

**SEO 特有约束**：中文 meta 不含「指南」，英文不含 `Guide`；常青内容 meta 不含年份。

**新文路径**：`content/blog/{locale}/{slug}.md` + `blog-meta.ts`（见 §六）。

| 项目 | 中文 | 英文 |
|------|------|------|
| pageUrl | `/zh/blog/[slug]` | `/blog/[slug]` |
| readTime | `XX 分钟阅读` | `XX min read` |
| 日期格式 | `2026年1月15日` | `January 15, 2026` |
| 核心要点标题 | 核心要点 | Key Takeaways |
| Conclusion 标题 | 结论 | Conclusion |
| FAQ 数量 | **7 问** | **7 问** |

---

## 三、正文章节

- **核心要点**：参见 [tldr.md](../sections/tldr.md)
- **什么是 XXX**：参见 [what-is.md](../sections/what-is.md)
- **Generic Section（普通段落）**：参见 [sections/generic.md](../sections/generic.md)、[README.md](../README.md)
- **How To**：参见 [sections/how-to.md](../sections/how-to.md)（SEO 可含内链）
- **Conclusion**：参见 [conclusion.md](../conclusion.md)
- **FAQ**：参见 [faq.md](../sections/faq.md)
- **References**：参见 [references.md](../sections/references.md)

---

## 四、SEO 页面特点

- **正文**：`<!-- block:section -->` + Markdown `##`/`###`；列表/表格 → `childrenHtml`
- **无产品 H3 榜单**：多为纯文字指南
- **TL;DR / FAQ / References**：**仅 JSON 侧车**（E10）；Brief 采用 → Step 08 注册
- **内链**：见 [internal-links.md Part 4](../internal-links.md#part-4-seo-频道内链)

---

## 五、SEO 各章节特有规则

以下规则为 **SEO 页面专有**，与 section 通用规范配合使用。

### 5.1 核心要点（Tldr）

- **JSON 注册**：`tldr-data.json` 键 `/seo/{slug}` · `/zh/seo/{slug}`；参见 [tldr.md](../sections/tldr.md) §3.3
- **introduction**：40–80 字，含 [主题]、[核心要点]、[目标]；直答式
- **items**：4–5 条，每条 25–40 字，同组长度相近
- **内容方向**：概念+作用、类型/格式、扩展类型、实施要点

### 5.2 How To（如何实施/如何选择）

- **可包含**：内链到相关 SEO 页面（如适用）
- **标题示例**：如何优化面包屑、如何实施 GEO 策略

### 5.3 正文章节

`<!-- block:section -->` + Markdown（[`anatomy.md`](../anatomy.md) §四·一）；见 [generic.md](../sections/generic.md)。

---

## 六、Meta 注册

**生产现状（2026-08）**：38 篇 SEO 均在 `content/seo/{locale}/{slug}.md` + `seo-meta.ts` + `/seo/{slug}`。

**新 slug 政策**（尚未有落地范例）：`content/blog/` + `blog-meta.ts` + `/blog/{slug}`。

---

## 七、路由与渲染

| 项 | 存量（生产） | 新文（政策） |
|----|-------------|-------------|
| 正文 | `content/seo/{locale}/{slug}.md` | `content/blog/{locale}/{slug}.md` |
| Meta | `seo-meta.ts` | `blog-meta.ts` |
| URL | `/seo/{slug}` · `/zh/seo/{slug}` | `/blog/{slug}` · `/zh/blog/{slug}` |
| JSON 键 | `/seo/{slug}` · `/zh/seo/{slug}` | `/blog/{slug}` · `/zh/blog/{slug}` |

---

## 八、示例 slug

`learn-seo` · `schema-guide` · `url-optimization` · `internal-links` 等（**均在 `/seo/`**，非 blog）。

