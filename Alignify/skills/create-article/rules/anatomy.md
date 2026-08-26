# 文章结构 × Inline Markdown 映射

> **版本**：v2.1 · 2026-08-27  
> **格式**：`content/{channel}/{locale}/{slug}.md` 正文 + JSON 侧车（TL;DR / FAQ / References **线上只读 JSON**）。

---

## 〇、内容优先原则（必读）

**文章架构由内容本身决定，本目录与 `templates/` 提供的是参考菜单，不是必填清单。**

| 层级 | 含义 | 示例 |
|------|------|------|
| **A 硬底线** | 违反即结构/SEO 错误，必须修复 | md 以 `#conclusion` 收束；禁止 frontmatter `howTo:`；Brief 采用 FAQ 则 JSON 7 问且无内链 |
| **B 类型惯例** | 某 `articleType` 的常见做法，可因题材调整 | Best-ranking 通常有产品 H3 榜单；SEO 文通常有操作步骤节 |
| **C 参考模板** | 新建页时的起点，可增删改顺序 | 下文「参考菜单」10 节；`templates/best-ranking.md` 等 |

**决策流程**（Step 01 / 05 前）：

1. 读知识块 + Research，列出读者必须带走的信息（定义？对比？选型？场景？）
2. 对照 [`article-types.md`](./article-types.md) 与 [`templates/`](./templates/) 看**常见结构**
3. 画出本篇 H2 大纲：**只保留服务读者的节**；可合并（如「如何工作」并入「什么是」）、可省略（如无对比价值则去掉对比表）
4. 写完后用 [`quality-checklist.md`](./quality-checklist.md) 核对 **A 层**；B/C 层不足时说明理由即可

**中英 parity**：ZH/EN 的 **section 类型与顺序应对齐**（锚点 id 一致），但两边不必机械复制「是否凑满 10 节」——对齐的是**实际采用的架构**，不是模板行数。

**Flagship 质量**（Alignify 每篇固定）：架构可灵活，但 **Moat、Answer Blocks、Research、BLUF、SelfCheck、终审** 不可省略。见 [`gates.md`](./gates.md) · [`article-brief.md`](./article-brief.md)。

---

## 一、参考菜单（Tools 类常见，非强制顺序）

以下为 **best-ranking 新建页的高频结构**，其它类型见 [article-types.md](./article-types.md)。**可调整顺序、合并或省略**，只要 A 层底线满足。

| 序号 | 章节 | Markdown | 常见度 |
|------|------|----------|--------|
| 1 | 核心要点 / Key Takeaways | `tldr-data.json`（**不写 md**） | 常用；可省略（Brief 写理由） |
| 2 | 什么是 XXX | md section | 几乎总是 |
| 3 | 如何工作 / 概念 | md section | 常出现在 Tools |
| 4 | 主体（Best 榜单 / 策略节 / 分析节） | md section + H3 | **主体节几乎总是** |
| 5 | 对比表格 | html block 或 section 内 table | 有 2+ 同质产品时常用 |
| 6 | 应用场景 | md section + H3 | 视题材 |
| 7 | 如何选择 | md section + H3 步骤 | 选型类常用；纯概念文可省 |
| 8 | 结论 | `## 结论 {#conclusion}` | 几乎总是 |
| 9 | 常见问题 | `faq-data.json`（**不写 md**；页底全局组件） | 常用；可省略（Brief 写理由） |
| 10 | 参考文献 | `references-data.json`（**不写 md**） | 有外部引用时建议 |

**A 层硬底线**（与是否采用上表每一行无关）：

- md 正文以 **`## 结论 {#conclusion}`** 收束；FAQ 由页底 `FAQ.tsx` 全局渲染（**不在 md 流内**）
- Brief **采用** FAQ → `faq-data.json` 中英文各 **7 问**，答案 plain text、无内链
- Brief **省略** TL;DR/FAQ/Refs → 三 JSON **不得**留对应 pathname 键（否则页面上仍会显示）
- **禁止** frontmatter `howTo:` / `heroHtml:` / `heroContent:`（E44）；Hero 导语写在首段 BLUF
- **禁止** 在 md 写 `#article-intro` / `#faq` / `#references` 指望线上渲染（408 篇 md **均无**此写法；写了也不显示）
- **禁止** 使用已删 JSON block 类型（`howToChoose` / `howItWorks` / `useCases`）及 `BestTools.tsx` 等组件

---

## 二、Frontmatter

```yaml
---
title: "H1：不写年份，推荐「类型：核心价值」"
description: "三段式摘要，中文 80–150 字"
slug: "{slug}"
date: "2026年6月23日"
updated: "2026年6月23日"
readingMinutes: "18 分钟阅读"
pageUrl: "https://alignify.co/zh/blog/{slug}"
locale: "zh"
category: "coding-dev"
categorySecondary: ""
heroImage: "/blog/{slug}/hero.jpg"
heroImageAlt: "…"
---
```

**允许键（仅此）**：`title` · `description` · `slug` · `date` · `updated` · `readingMinutes` · `pageUrl` · `locale` · `category` · `categorySecondary` · `heroImage` · `heroImageAlt`

**禁止键（E44）**：`heroHtml` · `howTo` · `heroContent` — 全站 md **不得**出现在 frontmatter；HTML 误入 YAML 区同样 Fail（E45）。区内首尾空行 Fail（E48）。送审跑 `scripts/audit/audit-frontmatter.py`；批量 normalize 跑 `scripts/ops/normalize-frontmatter.py`。

### 二·一 TL;DR / FAQ / References（JSON 侧车 · 线上 SSOT · 2026-08）

| 层 | SSOT | 说明 |
|----|------|------|
| **线上渲染** | JSON 侧车 | `src/data/tldr-data.json` · `faq-data.json` · `references-data.json` |
| **创作流程** | Brief + Step 08 | Brief 决定采用/省略；**采用 → Step 08 注册 JSON**；内容规范见 `sections/tldr.md` · `faq.md` · `references.md` |

**键格式**（= frontmatter `pageUrl` 去域路径）：

| 频道 | EN 键 | ZH 键 |
|------|-------|-------|
| blog 新文 | `/blog/{slug}` | `/zh/blog/{slug}` |
| tools 存量 | `/tools/{slug}` | `/zh/tools/{slug}` |
| marketing 存量 | `/marketing/{slug}` | `/zh/marketing/{slug}` |
| seo 存量 | `/seo/{slug}` | `/zh/seo/{slug}` |
| insights 存量 | `/insights/{slug}` | `/zh/insights/{slug}` |

**渲染链（部署仓）**：

- `markdown-doc.ts` → 解析 md 为 blocks；`block:tldr|faq|references` **跳过**
- `ArticleFromJson.tsx` → TL;DR / References 从 JSON 注入（`Tldr.tsx` · `References.tsx` **活跃**）
- `FAQ.tsx`（`ConditionalChrome`）→ 按 pathname 读 `faq-data.json`，渲染在**正文之后**

**Step 08 规则（E10）**：Brief 采用 TL;DR/FAQ/Refs → 注册对应 JSON（中英 pathname 键）；Brief 省略 → JSON **不得**留键。**勿**在 md 写这三节正文。

md 内可留 `<!-- references injected from references-data.json -->` 占位（editorial 提示），**不能**代替 JSON 注册。
- `category` → Hub 归属（经 `ARTICLE_CATEGORY_MAP` 推导）

### H2/H3 锚点语法

```markdown
## 章节标题 {#kebab-case-id}
### 步骤标题 {#step-1}
```

| 规则 | 说明 |
|------|------|
| **格式** | 标题末尾空格 + `{#id}`；`markdown-doc.ts` 解析后 **id 不进可见标题** |
| **禁止** | 空锚点 `{#}` — 会泄漏字面量 `{#}` 到线上（E27） |
| **id 命名** | kebab-case、语义化；与 EN/ZH 同 slug 的 section 用**相同 id** |

---

## 三、章节示例

各节**写法**见 `sections/`；**是否采用**见 §〇 与 Step 01 大纲。

### 1. 核心要点（JSON · 不写 md）

Brief 采用时，Step 08 注册 `tldr-data.json`：

```json
"/zh/blog/{slug}": {
  "id": "article-intro",
  "title": "核心要点",
  "introduction": "40–80 字 intro，直接回答页面核心问题…",
  "items": ["要点 1（25–60 字）", "要点 2", "要点 3", "要点 4"]
}
```

英文键 `/blog/{slug}`，`title`: `"Key Takeaways"`。规则见 [sections/tldr.md](./sections/tldr.md)。

### 2–7. 正文章节

```markdown
<!-- block:section -->
## 什么是 {工具类型} {#section-1}
…

<!-- block:section -->
## 2026 年最好的 {分类} {#best-{slug}-2026}
### 产品名 {#product-slug}
…
```

节名、数量、顺序 **按本篇大纲**，不必与参考菜单序号一一对应。

### 8. 结论

```markdown
<!-- block:section -->
## 结论 {#conclusion}
…
```

见 [conclusion.md](./conclusion.md)。

### 9. FAQ（JSON · 页底全局组件）

Brief 采用时，Step 08 注册 `faq-data.json`（**7 问**）：

```json
"/zh/blog/{slug}": {
  "items": [
    { "question": "问题 1", "answer": "答案（60–120 字，plain text，无内链）…" }
  ]
}
```

FAQ 由 `FAQ.tsx` 渲染在正文之后；md **不写** `#faq`。规则见 [sections/faq.md](./sections/faq.md)。

### 10. References（JSON · 不写 md）

Brief 采用时，Step 08 注册 `references-data.json`：

```json
"/zh/blog/{slug}": {
  "items": [
    { "title": "文章标题", "url": "https://…", "source": "出版方", "date": "2026", "description": "一句说明" }
  ]
}
```

规则见 [sections/references.md](./sections/references.md)。

---

## 四、按 articleType 的常见差异（建议，非清单）

| 节 | best-ranking | seo-guide | marketing-strategy | insights-analysis |
|----|-------------|-----------|-------------------|-------------------|
| 核心要点 | 常见 | 常见 | 常见 | 常见 |
| Best 榜单 H3 | 常见 | — | — | — |
| 策略/分析多节 | — | 常见 | 常见 | 常见 |
| 如何选择 | 选型类常见 | 可选 | 可选 | 可选 |
| FAQ 7 问 | 常见 | 常见 | 常见 | 常见 |

详情见 [article-types.md](./article-types.md) 与各 [templates/](./templates/)。

---

## 四·一、正文表格与列表（blog md）

**禁止** GFM 管道表格（`| col |`）——`markdownToHtml` 不解析，会渲染成一行纯文本（`|` 全部挤在同一行）。

**禁止** Markdown 无序/有序列表（`- item` / `1. item`）——同样不解析，会与相邻段落或表格行**合并成一行**。

**禁止** Markdown fenced code block（`` ```lang `` … `` ``` ``）——`markdown-doc.ts` 不解析；fence 行与内容会变成**多个裸 `<p>`**，页面上出现字面量 `` ```text ``（**E36**）。

**代码/流程展示**须用下列之一：

| 场景 | 写法 |
|------|------|
| 单行流程（箭头链） | 并入 Markdown **长段落** prose |
| 多行示例（commit、CLI） | `childrenHtml` + `<pre><code>…</code></pre>`（见下） |
| 行内命令/字段 | Markdown 内 `` `command` ``（渲染为普通文本，组件层可加样式） |

多行示例：

```markdown
<!-- childrenHtml:start -->
<div class="content-html"><pre><code>fix: refactor auth middleware

Co-Authored-By: Cursor &lt;cursoragent@cursor.com&gt;</code></pre></div>
<!-- childrenHtml:end -->
```

**必须** 使用 `<!-- childrenHtml:start -->` + HTML（列表/表格/卡片网格）：

```markdown
<!-- childrenHtml:start -->
<div class="content-html"><table><thead>…</thead><tbody>…</tbody></table></div>
<!-- childrenHtml:end -->
```

列表示例（**禁止** Tailwind utility class）：

```markdown
<!-- childrenHtml:start -->
<div class="content-html"><ul><li>…</li></ul></div>
<!-- childrenHtml:end -->
```

产品卡片网格：

```markdown
<!-- childrenHtml:start -->
<div class="content-html"><div class="article-card-grid article-card-grid--3"><div class="article-card article-card--compact"><div class="article-card__media"><img src="…" alt="…" loading="lazy"/></div><div class="article-card__body"><div class="article-card__title">名称</div><p class="article-card__desc">描述</p><a class="article-card__link" href="…">链接 →</a></div></div></div></div>
<!-- childrenHtml:end -->
```

### 禁止 inline Tailwind（E35 · 2026-08 全站统一）

**禁止** 在 `childrenHtml` / `html-block` / section 内联 HTML 中写 Tailwind utility（`text-base md:text-lg`、`grid grid-cols-2`、`bg-card`、`list-disc pl-6` 等）。

| 元素 | 正确写法 |
|------|----------|
| H2 / H3 / H4 / 正文段落 | Markdown `##` / `###` / 段落；insights `html-block` 内可用裸 `<h2>`/`<p>`（样式由 `index.css` `.content-html` 统一） |
| 无序/有序列表 | `childrenHtml` + `<div class="content-html"><ul><li>…</li></ul></div>` |
| 表格 | `childrenHtml` + `<div class="content-html"><table>…</table></div>` 或 `<div class="article-scroll-wrap"><table>…</table></div>` |
| 代码块 | `<pre><code>…</code></pre>` 或 `.article-code-block` |
| 行内 code | `<code class="article-inline-code">…</code>` |
| 图片网格 / 案例卡 | `.article-card-grid` / `.article-figure-grid` / `.article-feature-grid` / `.article-image-grid` + 子元素 `.article-card__*` / `.article-figure__*` / `.article-image-cell` |
| Hero 策略卡片 | **禁止** frontmatter HTML（E44）；首节 BLUF + 正文内链 |

**允许的 class 前缀**：`content-html`、`article-*`（完整列表见部署仓 `src/index.css` §content-html 与 `scripts/ref/inventory-content-classes.py`）。

批量迁移遗留页：`python scripts/ref/migrate-content-html.py`；Hero 专项：`python scripts/ref/migrate-hero-html.py`；语义 grid 对齐：`python scripts/ref/fix-semantic-grids.py`；审计：`python scripts/ref/inventory-content-classes.py` + `python scripts/ref/audit-semantic-html.py`（均应输出 clean）。

---

## 五、已废弃

**frontmatter / 旧 block（禁止新写）**

- frontmatter `heroHtml:` / `heroContent:` / `howTo:`（E44）
- `<!-- block:howToChoose -->` / `howItWorks` / `useCases` 等已删 JSON block 类型
- React 组件：`BestTools.tsx` / `HowToChoose.tsx` 已删；`Tldr.tsx` / `References.tsx` **活跃**（读 JSON）

**TL;DR / FAQ / References（生产现实 · 勿误解）**

- ✅ **线上 SSOT = JSON 侧车**；Brief 采用 → Step 08 注册；Brief 省略 → JSON 不得留键
- ✅ `Tldr.tsx` · `References.tsx` · `FAQ.tsx` **均为活跃组件**，读三份 JSON
- ❌ **不是**「md `#article-intro` / `#faq` 会渲染」——408 篇 md **均无**此写法；写了也不显示
- ❌ `<!-- block:tldr|faq|references -->` 会被 parser **跳过**；内容须进 JSON

---

*anatomy · v2.1 · 2026-08-27*
