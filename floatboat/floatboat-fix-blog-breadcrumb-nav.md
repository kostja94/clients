# Floatboat 任务单 — 全站 Blog 文章页「Back to Blog」替换为面包屑导航

> **任务类型**：页面结构改造（导航 UI + BreadcrumbList 结构化数据）
> **目标域名**：floatboat.ai
> **状态**：待处理
> **优先级**：P1（全站博客文章页共用头部组件；单点改动即全覆盖，兼改善导航与面包屑富结果）
> **提交**：2026-09-03

---

## 1. 任务目标

将 floatboat.ai 全部 Blog 文章页（`https://floatboat.ai/blog/{slug}`）文章标题上方的单一返回链接 **"Back to Blog"** 替换为**面包屑导航（breadcrumb navigation）**，并输出配套的 `BreadcrumbList` 结构化数据。

完成判定标准：

- 全站任一文章页不再渲染 "Back to Blog" 文本链接；
- 文章标题上方显示面包屑 `Home › Blog › {当前文章标题}`，层级链接可点且无死链；
- 页面输出 `application/ld+json` 的 `BreadcrumbList`（3 级、绝对 URL、末级含 `item`），通过 [Rich Results Test](https://search.google.com/test/rich-results)。

---

## 2. 问题证据（2026-09-03 实测）

### 2.1 示例页面 DOM 快照（提交方 2026-09-03 实测）

对 `https://floatboat.ai/blog/gemini-3-8-flash` 的渲染后页面 DOM 抓取，文章正文区顶部（站点头部导航之后、文章标签/日期行之前）当前输出为单一返回链接：

```
floatboat  floatboat            ← 站点头部导航（Pricing / About / Download）
─────────────────────────────────
Back to Blog                     ← 【待替换项】单一文字链接，指向 /blog
Label                            ← 文章分类标签（如 Research / Product 等）
Sep 3, 2026 · 21 min read        ← 日期 · 阅读时长
─────────────────────────────────
# Gemini 3.8 Flash — Google's New Coding & Agent Workhorse   ← H1
```

同一页面用文本抓取器得到的输出为（可见头部导航与 "Back to Blog" 所在容器整体位于被提取的正文区之前）：

```
floatboatfloatboat
PricingAbout
Download
Back to Blog
Label
Sep 3, 2026 · 21 min read
```

### 2.2 同区域在其他文章页的表现（抽验，2026-09-03）

对以下文章页分别抓取：`/blog/grok-4-6`、`/blog/claude-code-vs-cowork-vs-tag`、`/blog/gemini-3-7-flash`、`/blog/minimax-h3-max-infinite-ai-livestream`。文本层输出均**从文章元信息行（日期 · 阅读时长）开始**，未捕获任何位于其上的返回链接/面包屑文本——与 2.1 属同一「正文区上方头部容器」。即：文本抓取器对该站头部容器整体不透明，**无法据此判定元素缺失**；"Back to Blog" 应位于文章页共用模板的头部容器中（同模板渲染）。请对方 agent 以浏览器 DOM / 源码为准，全站扫描一次确认覆盖（见 §6 验收第 1 项）。

### 2.3 列表页

`https://floatboat.ai/blog`（Blog 列表页）当前无 "Back to Blog"（该链接只存在于文章页），列表页非本任务主范围（可选处理见 §5.5）。

---

## 3. 根因分析

- 文章页模板（blog post template）在文章标题上方只放置了**单一返回链接**（"Back to Blog"，指向 `/blog`），未提供**层级路径（breadcrumb）**：从搜索引擎或社交流量直接进入某篇文章的用户，只能「回列表」，无法一眼获知自己在站点层级中的位置（首页 → Blog → 该文章），也无法就地跳回上级分类语境。
- 面包屑同时是 Google 认可的导航模式与富结果类型：Google 的 [Breadcrumb 富结果文档](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) 建议页面既展示面包屑 UI，也输出对应的 `BreadcrumbList` 结构化数据（`position` 升序、每个 `ListItem.item` 为**完整绝对 URL**）。当前页面若未输出该 schema（请对方 agent 在源码中确认；如已有请按下文 §5.3 校正，如无则新增），则站点无法获得面包屑富结果资格。
- 该项改造是**全站共用模板级改动**：文章页共用同一 post template，替换一处组件即可覆盖全部文章页（与列表页/首页模板互不影响）。

---

## 4. 影响范围

| 页面 | 受影响位置 | 处理 |
|------|-----------|------|
| `/blog/{slug}`（全部已发布文章页） | 文章标题上方的头部容器，现为 "Back to Blog" 返回链接 | 替换为面包屑组件（本任务主范围） |
| `/blog`（Blog 列表页） | 无 "Back to Blog" | 不做改动；可选见 §5.5 |
| 首页 `/`、产品页等非文章页 | 无该组件 | 不涉及 |

**组件性质**：文章页共用模板的单点组件（推断，基于 2.2 同容器抓取一致性）——请对方 agent 定位到该模板组件后一次改全。

---

## 5. 修复要求

### 5.1 修复位置

定位文章页模板（blog post / article page template）中渲染 `Back to Blog` 的组件——站点源码内搜索关键词：**"Back to Blog"**、**"back-to-blog"**、`href="/blog"`（文章头部区）。面包屑组件应替换在同一位置（文章标题上方、标签/日期行之前）。

### 5.2 规则（必须满足）

1. **面包屑层级固定为 3 级**：`Home › Blog › {当前文章标题}`；不包含分类层（站点无 `/blog/{category}/…` 或 `/blog?category=` 的分类落地页证据，不得链接到 404 分类路径）。
2. **绝对 URL**：Home → `https://floatboat.ai/`；Blog → `https://floatboat.ai/blog`；末级为当前文章页 `https://floatboat.ai/blog/{slug}`（末级为当前页，可渲染为不可点文本并加 `aria-current="page"`；若渲染为链接则必须是该绝对 URL）。
3. **JSON-LD 对齐**：页面输出的 `BreadcrumbList` 结构化数据与可见面包屑层级一致；所有 `ListItem.item` 为绝对 URL；末级（position 3）也必须带完整 `item`。
4. **标题一致性**：末级名称取文章 H1/`title` 的正文标题（如 "Gemini 3.8 Flash — Google's New Coding & Agent Workhorse"）；超长标题可截断展示但 schema 中保留全名。
5. **替换而非叠加**：删除原 "Back to Blog" 返回链接；不得同时保留两套导航。
6. **全站生效**：一处组件改动覆盖所有文章页；标签/日期行、H1 等其他元素保持不动。

### 5.3 修复后的期望输出

`/blog/gemini-3-8-flash` 面包屑 UI（示意）：

```
Home › Blog › Gemini 3.8 Flash — Google's New Coding & Agent Workhorse   ← 面包屑（原 Back to Blog 位置）
Label · Sep 3, 2026 · 21 min read
```

对应 `BreadcrumbList` 结构化数据（示意，`application/ld+json`）：

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://floatboat.ai/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://floatboat.ai/blog" },
    { "@type": "ListItem", "position": 3, "name": "Gemini 3.8 Flash — Google's New Coding & Agent Workhorse", "item": "https://floatboat.ai/blog/gemini-3-8-flash" }
  ]
}
```

对任意文章页 `{slug}`，position 3 的 `name` 与 `item` 均替换为该页的标题与 `https://floatboat.ai/blog/{slug}`。

### 5.4 代码级参考（示意，按项目实际实现调整）

```tsx
// 文章页模板头部：以面包屑组件替换 "Back to Blog"
const SITE_URL = "https://floatboat.ai";

// 可见面包屑
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href={`${SITE_URL}/`}>Home</a></li>
    <li><a href={`${SITE_URL}/blog`}>Blog</a></li>
    <li aria-current="page">{title}</li>
  </ol>
</nav>

// BreadcrumbList JSON-LD（随页面输出，3 级，绝对 URL，末级带 item）
const breadcrumbSchema = {
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  itemListElement: [
    { "@type": "ListItem", position: 1, name: "Home", item: `${SITE_URL}/` },
    { "@type": "ListItem", position: 2, name: "Blog", item: `${SITE_URL}/blog` },
    { "@type": "ListItem", position: 3, name: title, item: `${SITE_URL}/blog/${slug}` }
  ],
};
```

### 5.5 可选项（不做不影响主验收）

- `/blog` 列表页若同样有头部容器，可补 `Home › Blog` 两级面包屑以保持一致（非必须，列表页无 "Back to Blog"）。
- 若站点未来提供分类落地页（如 `/blog/research/…`），可再讨论把分类插入 position 2/3 之间；本期不做。

---

## 6. 验收标准

- [ ] 全站文章页扫描（以源码/浏览器 DOM 为准）确认不再存在 "Back to Blog" 文本或同类单一返回链接；抽查 ≥4 篇不同类型文章（如 `/blog/gemini-3-8-flash`、`/blog/grok-4-6`、`/blog/claude-code-vs-cowork-vs-tag`、`/blog/glm-5-3`）头部均为面包屑
- [ ] 面包屑层级为 `Home › Blog › {当前文章标题}`；Home/Blog 链接分别指向 `https://floatboat.ai/` 与 `https://floatboat.ai/blog` 且可点可达（无死链）
- [ ] 末级当前页标记 `aria-current="page"`（或以不可点文本呈现），不产生指向自身的可重复链接（如有则必须为当前页绝对 URL）
- [ ] 页面源码含 `BreadcrumbList` JSON-LD：3 个 `ListItem`、`position` 1→2→3 升序、所有 `item` 为 `https://floatboat.ai/...` 绝对 URL、末级带 `item`
- [ ] 通过 [Rich Results Test](https://search.google.com/test/rich-results) 校验无错误（无关的提示性信息视为通过）
- [ ] 标签/日期/阅读时长行与 H1 等原内容无回归；移动端与桌面端面包屑均正常显示
- [ ] 部署后抽查 3–5 篇文章页确认全局生效（组件级改动，理论上一次覆盖）

---

*本任务单由外部 SEO/协作方提交，供 Floatboat 方 agent 直接执行。*
