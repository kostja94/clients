# 四种文章类型 × Markdown 结构

> **版本**：v3.5 · 2026-08-27  
> **格式**：`.md` frontmatter + `<!-- block:section -->` 正文；TL;DR / FAQ / References **仅 JSON 侧车渲染**（见 [`anatomy.md`](./anatomy.md) §二·一）  
> **原则**：类型决定 Meta、Hub、知识块目录；**正文架构由内容决定**。**[`templates.md`](./templates.md) 与 `templates/` 仅为建议**，不要求与任一存量篇一比一复刻。  
> **新文**：统一 **`content/blog/` + `/blog/{slug}`** — 许多题材从未有过，**更不应硬套**旧频道骨架。

---

## 类型速查

| 类型 | 知识块 | **新文** 内容路径 | **新文** 路由 | **存量**（不重迁） | Hub 推导 |
|------|--------|------------------|--------------|-------------------|----------|
| Tools | `knowledge/tools/` | `content/blog/` | `/blog/{slug}` | `content/tools/` · `/tools/{slug}` | frontmatter `category` |
| Marketing | `knowledge/marketing/` | `content/blog/` | `/blog/{slug}` | `content/marketing/` · `/marketing/{slug}` | 独立 Hub |
| SEO | `knowledge/seo/` | `content/blog/`（政策） | `/blog/{slug}` | `content/seo/` · `/seo/{slug}` | 独立 Hub |
| Insights | `knowledge/insights/` | `content/blog/`（政策） | `/blog/{slug}` | `content/insights/` · `/insights/{slug}` | 独立 Hub |

> **路由约定（2026-08）**：**新 slug**（任意 articleType）统一 **`content/blog/` + `/blog/{slug}`**（中文 `/zh/blog/{slug}`）。存量旧路径**仅维护更新，不重迁 URL**。  
> **为何迁到 blog**：新文大量是**全新题材**，按频道拆模板无意义；类型由 Brief `articleType` + Answer Blocks 决定，非 URL 目录。  
> **生产现状（2026-08-27）**：blog **33** slug · tools **108** · marketing **16** · seo **38** · insights **7**（events 另计）。**SEO / Insights 尚无 blog 新文批量**——仍在存量路径 + 对应 `*-meta.ts`。  
> **已废弃**：JSON block 类型 `howToChoose` / `bestTools` / `howItWorks` / `useCases`；对应 React 组件已删除。

---

## Meta 注册（生产）

| 频道 | Meta | Config | 正文路径 | URL |
|------|------|--------|----------|-----|
| blog 新文 | `blog-meta.ts` | `blog-pages-config.ts` | `content/blog/` | `/blog/` |
| tools 存量 | `tools-meta.ts` | `tools-pages-config.ts` | `content/tools/` | `/tools/` |
| marketing 存量 | `marketing-meta.ts` | — | `content/marketing/` | `/marketing/` |
| seo 存量 | `seo-meta.ts` | — | `content/seo/` | `/seo/` |
| insights 存量 | `insights-meta.ts` | — | `content/insights/` | `/insights/` |

Marketing **双轨**：11 篇 blog 新文 + 16 篇 marketing 存量。blog-meta 有 slug 且 tools-meta 也有 → **redirect** 到 blog。

---

## Tools 型（Blog 新文）

**常见结构**见 [`templates.md`](./templates.md) Part 2 · [`sections.md`](./sections.md) Part 0。**勿**为对齐模板增删节。

- 主体多为 Best 榜单：正文 section + 产品 H3
- 选型类常含：`## 如何选择…` + `###` 步骤
- FAQ：**7 问**（`faq-data.json`）— Brief 采用时

可省略：对比表、应用场景、如何工作等 — 见 Step 01 大纲说明。

**Tools 存量**（108 slug）：仍走 `content/tools/` + `tools-meta.ts` + `/tools/{slug}`；TL;DR/FAQ/Refs JSON 键为 `/tools/{slug}` · `/zh/tools/{slug}`。

---

## Marketing 型

**常见顺序**（**参考 only**；节数与是否含 TL;DR/FAQ/How To **由内容决定**）见 [`templates.md`](./templates.md) Part 3 · [`sections.md`](./sections.md) Part 0：

```
[核心要点 JSON] → 概念 section → 策略/分析 sections×N → [场景] → [作者判断] → 结论 {#conclusion} → [FAQ JSON · 页底] → [References JSON]
```

- 内链专规：[`internal-links.md` Part 4.5](./internal-links.md#part-45-marketing-频道内链)
- **禁止** frontmatter `heroHtml` / `heroContent` / `howTo:`（E44）；导语写首节 BLUF
- **ZH/EN**：同等 flagship 深度；EN 独立重写

---

## SEO 型

**常见顺序**（**参考 only**；H2 因题而异）见 [`templates.md`](./templates.md) Part 4 · [`sections.md`](./sections.md) Part 0：

```
核心要点 JSON → 概念 → 操作 sections（H3）→ [场景] → 结论 → FAQ JSON(7) → [References JSON]
```

- 列表/表格：`<!-- childrenHtml:start -->` + HTML（见 `anatomy.md` §四·一）
- Meta：指南型规则组
- **生产路径**：38 篇均在 `content/seo/` + `seo-meta.ts` + `/seo/{slug}`（**非** blog）

---

## Insights 型

**常见顺序**（**参考**；H2 由 SSOT + Brief Answer Blocks 推导，**非** Marketing 收束模板）：

```
核心要点 JSON → 分析 sections×N → [案例/边界] → 结论 → FAQ JSON(7) → [References JSON]
```

- Meta：分析型规则组
- **新文**：`content/blog/` + `blog-meta.ts`（`articleType: insights-analysis`）
- **存量**：7 篇在 `content/insights/` + `insights-meta.ts`
- **默认不设**：`#author-take`、`#should-you-do-this` go/no-go、How To（见 [`templates.md`](./templates.md) Part 5）
- **E49**：正文禁止「细节进 future skills」meta 句

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

- md 正文以 `#conclusion` 收束；FAQ 由页底 `FAQ.tsx` 全局渲染（不在 md 流内）
- Brief 采用 FAQ → `faq-data.json` 中英文各 **7 问**、条数一致；内链若存在须 R4 全文 1 次
- Brief 省略 TL;DR/FAQ/Refs → 三 JSON **不得**留对应 pathname 键
- 禁止 frontmatter `howTo:` / `heroHtml:` / `heroContent:`（E44）；HTML 不得出现在 `---` 之间（E45）
- frontmatter 仅允许 `anatomy.md` §二 白名单；节内勿留首尾空行（E48）

---

*article-types · v3.5 · 2026-08-27*
