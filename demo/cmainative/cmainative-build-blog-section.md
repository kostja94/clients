# 猎豹AI实战派 任务单 — 构建 Blog 板块（独立文章页 + SEO + 转化）

> **任务类型**：页面开发 / 信息架构 / 技术 SEO
> **目标域名**：cmainative.cmcm.com
> **状态**：待处理
> **优先级**：P0（blog 为获客主渠道；当前 4 篇文章无独立 blog URL，无法被 sitemap 收录为博文，结构化数据缺失）
> **提交**：2026-08-21

---

## 1. 任务目标

在 `cmainative.cmcm.com` 上完成 **可扩展、可索引、可转化** 的 Blog 板块建设。对方 agent 完成后应达到：

1. **每篇 blog 有独立 URL**（`/blog/{slug}.html`），不再复用 `research-*.html` 作为博文正文页。
2. **`blog.html` 索引页** 全部卡片 / 列表 / 分类筛选指向 blog 单篇 URL。
3. **4 篇已有博文** 迁移至 blog URL；原 `research-*.html` 做 **301 重定向** 至对应 blog 页（保留外链权重，避免重复内容）。
4. 每篇 blog 单篇具备 **canonical、meta description、Open Graph、BlogPosting + BreadcrumbList JSON-LD**（绝对 URL）。
5. **`sitemap.xml` 收录全部 blog 单篇**；补 **`robots.txt`** 并声明 sitemap。
6. 文末统一 **转化 CTA 组件**（企业 AI 诊断 + 报名下一场活动），与全站飞书表单一致。
7. 提供 **可复用博文模板**，后续按 [blog/README.md](./blog/README.md) 队列新增文章时无需改结构。

**判定完成**：以下验收标准（§6）全部勾选通过。

---

## 2. 问题证据（2026-08-21 实测）

### 2.1 索引页存在，但文章链向 research URL

`https://cmainative.cmcm.com/blog.html` 置顶卡片与列表均指向 research 路径，而非 blog 路径：

```html
<!-- blog.html Featured 区块（2026-08-21 实测） -->
<a class="blog-lead" href="research-jagged-frontier-knowledge-work.html">
  <p class="latin">POST / 001</p>
  <h3>AI 的能力边界为什么像一条锯齿线？</h3>
  ...
</a>
```

同页 4 篇文章链接汇总：

| 标题 | 当前 href | 问题 |
|------|-----------|------|
| AI 的能力边界为什么像一条锯齿线？ | `research-jagged-frontier-knowledge-work.html` | 应为 blog URL |
| 业务 Agent 上线前，先证明它能完成闭环 | `research-business-agent-evaluation.html` | 应为 blog URL |
| 一人加 AI，能否达到两人团队的水平？ | `research-ai-cross-functional-teams.html` | 应为 blog URL |
| 客服 AI 最先改变的，是新人的学习曲线 | `research-customer-support-learning-curve.html` | 应为 blog URL |

### 2.2 Blog 单篇 URL 不存在

探测以下路径均 **404**（2026-08-21）：

```
/blog/post-001.html
/blog/ai-capability-boundary-jagged-line.html
/blog/001-ai-capability-boundary.html
/post-001.html
/blog/post/001.html
```

### 2.3 sitemap 无 blog 单篇，仅有索引

`https://cmainative.cmcm.com/sitemap.xml`（2026-08-21 实测，HTTP 200）包含：

```xml
<url><loc>https://cmainative.cmcm.com/blog.html</loc></url>
<!-- 以下为 research 单篇，无 blog/{slug}.html -->
<url><loc>https://cmainative.cmcm.com/research-jagged-frontier-knowledge-work.html</loc><lastmod>2026-08-17</lastmod></url>
<url><loc>https://cmainative.cmcm.com/research-business-agent-evaluation.html</loc>...</url>
<url><loc>https://cmainative.cmcm.com/research-ai-cross-functional-teams.html</loc>...</url>
<url><loc>https://cmainative.cmcm.com/research-customer-support-learning-curve.html</loc>...</url>
```

### 2.4 SEO 元数据与结构化数据缺失

**blog.html `<head>`**（2026-08-21）：

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="猎豹 AI Native 转型研究院博客：关于模型、Agent、组织与落地的观点、笔记和判断…">
<title>博客｜AI Native 转型研究院｜猎豹AI实战派</title>
<link rel="stylesheet" href="css/blog.css">
<!-- 无 canonical、无 og:*、无 application/ld+json -->
```

**research-jagged-frontier-knowledge-work.html**（当前承载 blog 正文，2026-08-21）：

```html
<meta name="description" content="基于 BCG 758 名顾问实验，解释 AI 在知识工作中的锯齿状能力边界…">
<!-- 无 canonical、无 og:*、无 application/ld+json -->
<!-- 页头体裁标注为「研究简报」，与 blog 索引「POST / 001」不一致 -->
<!-- 页脚有「回到博客 → blog.html」链接 -->
```

### 2.5 robots.txt 缺失

`https://cmainative.cmcm.com/robots.txt` → **404**（2026-08-21）。

### 2.6 Blog 与 Research 栏目边界混乱

站内定位（blog.html 页脚原文）：

> 这里写的是**观点和笔记**…需要原创分析框架与自有数据图的重型内容，发布在**研究栏目**。

现状：4 篇「观点和笔记」正文放在 `research-*.html`，与 `research.html` 下 heavier Report / Case Study 混用同一 URL 命名空间，不利于 SEO 聚类与用户心智。

---

## 3. 根因分析

1. **信息架构未完成第二阶段**：blog 索引页（`blog.html` + `css/blog.css`）已上线，但单篇正文页未从 research 命名空间拆出，导致「有列表、无博文 URL」。
2. **Research 页模板被复用为 Blog 载体**：开发时为快速上线，将 4 篇短文挂载在 `research-*.html`；索引页直接链到这些 URL，形成 **栏目标签（POST）与 URL 路径（research）不一致**。
3. **SEO 基建未随内容发布补齐**：静态站点未注入 JSON-LD / canonical；sitemap 生成脚本只收录了 research 路径；robots.txt 未部署。
4. **对获客的影响**（见 [cmainative-growth-strategy.md](./cmainative-growth-strategy.md)）：blog 是 P0 获客渠道；单篇不可索引 = 信息型关键词（如「AI 能力边界」「业务 Agent 验收」）无法逐篇排名；文末 CTA 无法按文章做来源追踪。

**规范参考**：

- [Google Article 结构化数据](https://developers.google.com/search/docs/appearance/structured-data/article)
- [Google Breadcrumb 结构化数据](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)（`item` 必须为绝对 URL）
- [Sitemap 协议](https://www.sitemaps.org/protocol.html)

---

## 4. 影响范围

| 页面 / 组件 | 受影响位置 | 抽验结果（2026-08-21） |
|-------------|-----------|------------------------|
| `blog.html` | Featured 卡片、Brief 卡片、文章索引表、分类锚点 | 4/4 链到 research URL |
| `research-jagged-frontier-knowledge-work.html` 等 4 页 | 被当作 blog 正文 | 需 301 → blog URL |
| `sitemap.xml` | URL 列表 | 含 4 research URL，缺 blog 单篇 |
| `robots.txt` | 全站 | 404 |
| 全站导航（`zone-nav`） | 已含 blog / research 入口 | 无需移除；blog 单篇需接入同一 header/footer |
| `research.html` 索引 | 是否仍列出上述 4 篇 | ⚠️ 待验证；迁移后应从 research 索引移除，避免 duplicate |

**范围界定**：本任务聚焦 **blog 板块**（索引 + 单篇 + 迁移 + SEO + CTA）。`research.html` 及其 Report/Case Study 单篇 **不在本任务改内容**，仅处理 4 篇已出现在 blog 索引的交叉内容。

---

## 5. 修复要求

### 5.1 修复位置

在站点静态文件目录中定位（搜索关键词）：

| 搜索关键词 | 预期文件 |
|-----------|---------|
| `blog-page`、`blog-featured`、`blog-lead` | `blog.html`、`css/blog.css` |
| `research-jagged-frontier` | 现有正文 HTML（迁移源） |
| `zone-header`、`zone-nav` | 全站 header 组件（blog 单篇需复用） |
| `sitemap` | sitemap 生成脚本或 `sitemap.xml` |
| `G-3RB89JCFVV` | `js/site-analytics.js`（可选 UTM） |

### 5.2 规则（必须满足）

#### A. URL 与信息架构

1. **Blog 单篇 URL 模式**：`https://cmainative.cmcm.com/blog/{slug}.html`（小写英文 kebab-case + 可选年份后缀）。
2. **Research 单篇 URL 模式保持不变**：`research-{slug}.html` 仅用于 research 栏目重型内容（Report / Case Study / Review）。
3. **4 篇迁移映射**（slug 可调整，但需 301 旧 URL）：

| 现 URL | 新 blog URL（建议） | 分类 |
|--------|-------------------|------|
| `research-jagged-frontier-knowledge-work.html` | `blog/jagged-frontier-knowledge-work.html` | 能力边界 |
| `research-business-agent-evaluation.html` | `blog/business-agent-evaluation.html` | 能力边界 |
| `research-ai-cross-functional-teams.html` | `blog/ai-cross-functional-teams.html` | 组织与岗位 |
| `research-customer-support-learning-curve.html` | `blog/customer-support-learning-curve.html` | 落地与踩坑 |

4. **301 重定向**：上述 4 个 `research-*.html` → 对应 `blog/*.html`（全站永久跳转）。
5. **`blog.html` 内所有内链** 必须指向 `blog/*.html`，禁止再链向已迁移的 research URL。

#### B. 页面模板（单篇）

每篇 blog 单篇必须包含：

| 区块 | 要求 |
|------|------|
| `<head>` | 唯一 `<title>`：`{文章标题}｜博客｜AI Native 转型研究院｜猎豹AI实战派` |
| | `<meta name="description">`：110–160 字中文摘要，每篇独立 |
| | `<link rel="canonical" href="https://cmainative.cmcm.com/blog/{slug}.html">` |
| | Open Graph：`og:title`、`og:description`、`og:url`、`og:type=article`、`og:locale=zh_CN` |
| Header | 复用 `zone-header` + 当前栏目高亮「博客」 |
| 文章头 | 栏目：博客 · {分类}；可选 `POST / {NNN}` 序号；发布日期 `YYYY.MM.DD`；阅读时长 |
| 正文 | 从现有 research 页迁移 Markdown/HTML 内容；保留「数据与资料来源」节 |
| 文末 CTA | 统一组件（见 5.3） |
| 相关阅读 | ≥2 条链到其他 blog 单篇或 research 单篇 |
| Footer | 全站 footer + 「返回博客索引」链到 `blog.html` |

#### C. 结构化数据

1. 每篇 blog 输出 **BlogPosting** JSON-LD。
2. 每篇 blog 输出 **BreadcrumbList** JSON-LD。
3. 所有 URL 字段必须为 **https 绝对 URL**（禁止 `/blog/...` 相对路径）。
4. `blog.html` 索引页输出 **CollectionPage** 或 **Blog** JSON-LD（二选一，推荐 `Blog`）。

#### D. Sitemap 与 robots

1. 新建 `robots.txt`：

```
User-agent: *
Allow: /

Sitemap: https://cmainative.cmcm.com/sitemap.xml
```

2. `sitemap.xml` 更新：
   - **新增** 4 条 `blog/{slug}.html` + 后续 blog 单篇
   - **移除** 已 301 的 4 条 `research-*.html`（避免重复提交）
   - 每条 blog URL 带 `<lastmod>`（ISO 8601 日期）

#### E. 分类筛选

`blog.html` 已有分类：**能力边界、组织与岗位、成本与账、落地与踩坑**。

- 每篇文章标注 `data-category` 或等价属性
- 筛选按钮点击后仅显示对应文章（无需 SPA；可用 CSS/轻量 JS）
- 分类名与 [blog/README.md](./blog/README.md) 队列保持一致

#### F. 转化 CTA（获客）

文末 CTA 固定文案（中文）：

```
若你已在尝试 AI 但卡在组织推进或业务落地，可先申请企业 AI 诊断，
或报名下一场实战派活动。
```

链接：

- 诊断：`https://cheetah-mobile.feishu.cn/share/base/form/shrcnbFta2YlqNHc9Hs07Xv5Ehd?hide_source_id=1&prefill_source_id=website`（与首页一致，2026-08-21 首页内链）
- 活动：首页活动区块当前场次链接（部署时读取最新 event URL；2026-08-21 为 `/events/shenzhen-20260904` 或首页 CTA）

**UTM 建议**（可选但推荐）：`?utm_source=blog&utm_medium=article&utm_campaign={slug}`

#### G. 边界（不要做）

- 不要修改 research 栏目中 **非上述 4 篇** 的内容页
- 不要删除 blog 索引页现有视觉风格（`css/blog.css` 为基准扩展）
- 不要在本任务中批量撰写 [blog/README.md](./blog/README.md) 队列里的 8 篇新文（仅搭模板 + 迁移 4 篇）

### 5.3 修复后的期望输出

#### Blog 单篇 JSON-LD 示例

以 `blog/jagged-frontier-knowledge-work.html` 为例：

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "AI 的能力边界为什么像一条锯齿线？",
  "description": "基于 BCG 与哈佛商学院对 758 名顾问的随机实验，解释 AI 能力边界的锯齿状分布，以及企业应如何分任务验收。",
  "datePublished": "2026-08-05",
  "dateModified": "2026-08-05",
  "inLanguage": "zh-CN",
  "author": {
    "@type": "Organization",
    "name": "猎豹AI实战派 · AI Native 转型研究院",
    "url": "https://cmainative.cmcm.com/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "猎豹移动",
    "url": "https://www.cmcm.com/"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://cmainative.cmcm.com/blog/jagged-frontier-knowledge-work.html"
  },
  "url": "https://cmainative.cmcm.com/blog/jagged-frontier-knowledge-work.html",
  "articleSection": "能力边界",
  "keywords": ["AI 能力边界", "企业 AI Native", "BCG 锯齿状前沿"]
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "首页",
      "item": "https://cmainative.cmcm.com/homepage-one-to-one.html"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "博客",
      "item": "https://cmainative.cmcm.com/blog.html"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "AI 的能力边界为什么像一条锯齿线？",
      "item": "https://cmainative.cmcm.com/blog/jagged-frontier-knowledge-work.html"
    }
  ]
}
```

#### blog.html 索引 JSON-LD 示例

```json
{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "AI Native 转型研究院 · 博客",
  "description": "关于模型、Agent、组织与落地的观点和笔记。",
  "url": "https://cmainative.cmcm.com/blog.html",
  "publisher": {
    "@type": "Organization",
    "name": "猎豹AI实战派",
    "url": "https://cmainative.cmcm.com/"
  },
  "blogPost": [
    {
      "@type": "BlogPosting",
      "headline": "AI 的能力边界为什么像一条锯齿线？",
      "url": "https://cmainative.cmcm.com/blog/jagged-frontier-knowledge-work.html",
      "datePublished": "2026-08-05"
    }
  ]
}
```

#### 301 重定向示例（按部署方式二选一）

**Apache `.htaccess`：**

```apache
Redirect 301 /research-jagged-frontier-knowledge-work.html /blog/jagged-frontier-knowledge-work.html
Redirect 301 /research-business-agent-evaluation.html /blog/business-agent-evaluation.html
Redirect 301 /research-ai-cross-functional-teams.html /blog/ai-cross-functional-teams.html
Redirect 301 /research-customer-support-learning-curve.html /blog/customer-support-learning-curve.html
```

**或静态托管跳转页**：在旧 research HTML 的 `<head>` 插入 `<meta http-equiv="refresh" content="0;url=...">` + `<link rel="canonical" href="新 blog URL">`（次选；优先 HTTP 301）。

#### 新博文模板文件（示意）

建议新增 `blog/_template.html` 或构建脚本模板，占位符：

```
{{SLUG}} {{TITLE}} {{DESCRIPTION}} {{DATE}} {{CATEGORY}} {{POST_NUMBER}} {{BODY_HTML}} {{CTA_DIAGNOSIS_URL}} {{CTA_EVENT_URL}}
```

后续文章按 [blog/README.md](./blog/README.md) 队列填入即可发布。

### 5.4 代码级参考（示意）

```html
<!-- blog/{slug}.html 正文页结构示意 — 按项目实际实现调整 -->
<body class="zone-page blog-article-page">
  <header class="zone-header">…<!-- 复用 blog.html header --></header>
  <main>
    <article class="blog-article" itemscope itemtype="https://schema.org/BlogPosting">
      <header class="blog-article__head">
        <p class="blog-article__eyebrow">博客 · 能力边界 · POST / 001</p>
        <h1 itemprop="headline">AI 的能力边界为什么像一条锯齿线？</h1>
        <p class="blog-article__meta"><time datetime="2026-08-05">2026.08.05</time> · 约 12 分钟</p>
      </header>
      <div class="blog-article__body" itemprop="articleBody">…</div>
      <aside class="blog-cta">…</aside>
    </article>
  </main>
  <footer>…</footer>
  <script type="application/ld+json">…BlogPosting + BreadcrumbList…</script>
</body>
```

---

## 6. 验收标准

- [ ] 4 篇 blog 单篇可通过 `https://cmainative.cmcm.com/blog/{slug}.html` 直接访问，返回 HTTP 200
- [ ] `blog.html` 上 4 张卡片 + 索引表全部指向 `blog/*.html`，零条指向已迁移的 `research-*.html`
- [ ] 访问旧 URL（如 `research-jagged-frontier-knowledge-work.html`）返回 **301** 至对应 blog URL
- [ ] 每篇 blog 单篇 `<head>` 含 **唯一 canonical**（绝对 URL，指向自身）
- [ ] 每篇 blog 单篇含 **BlogPosting + BreadcrumbList** JSON-LD；Rich Results Test 无 error
- [ ] `blog.html` 含 **Blog**（或 CollectionPage）JSON-LD；Breadcrumb 绝对 URL
- [ ] `robots.txt` 可访问且声明 `Sitemap: https://cmainative.cmcm.com/sitemap.xml`
- [ ] `sitemap.xml` 含 4 条 blog 单篇 URL + `blog.html`；**不含** 已 301 的 4 条 research URL
- [ ] 每篇 blog 文末 CTA 含「企业 AI 诊断」+「报名活动」两链，链接可点击且与首页一致
- [ ] `research.html` 索引 **不再列出** 已迁移的 4 篇（避免与 blog 重复）
- [ ] 分类筛选在 `blog.html` 可切换 4 个分类并正确过滤
- [ ] 抽验 2 篇：移动端 viewport 正常、header 导航与 blog.html 一致
- [ ] 新增 `_template` 或文档说明：运营如何按 [blog/README.md](./blog/README.md) 发布第 5 篇文章

---

## 7. 关联文档（仓库内）

| 文档 | 用途 |
|------|------|
| [cmainative-site-structure.md](./cmainative-site-structure.md) | URL 层级与分阶段规划 |
| [cmainative-growth-strategy.md](./cmainative-growth-strategy.md) | 获客渠道与 blog 发布节奏 |
| [blog/README.md](./blog/README.md) | 待产博文队列与文章结构模板 |
| [cmainative-keywords.md](./cmainative-keywords.md) | 单篇目标关键词 |

---

*本任务单由外部 SEO / 增长协作方提交，供 cmainative.cmcm.com 方 agent 直接执行。*
