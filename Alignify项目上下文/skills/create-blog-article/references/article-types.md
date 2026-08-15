# Article Types — 四种文章类型完整结构 × JSON 字段映射

> **路径**：`skills/create-blog-article/references/article-types.md`
> **用途**：定义 Tools / Marketing / SEO / Insights 四种文章类型的完整 JSON block 结构、字段约定、字数硬底线、与知识块目录的对应关系。
> **版本**：v1.0 · 2026-07-16

---

## 类型目录 ⇄ 路由 ⇄ Meta 规则

| 知识块目录 | routeCategory | Meta 规则组 | 关键词表 | 典型 slug 示例 |
|-----------|---------------|------------|---------|--------------|
| `knowledge/tools/` | `"tools"` | Best 型 | `alignify-keywords-tools.md` | `image-generator`, `multi-agent` |
| `knowledge/marketing/` | `"marketing"` | 策略型 / 指南型 | `alignify-keywords-marketing.md` | `affiliate`, `github-for-marketing` |
| `knowledge/seo/` | `"tools"` 或 `"marketing"` | 指南型 | `alignify-keywords-seo.md` | `domain`, `keyword-research` |
| `knowledge/insights/` | `"tools"` 或 `"marketing"` | 分析型 | `alignify-keywords-insights.md` | `ai-product-naming`, `openai` |

---

## 一、Tools 榜单/对比型

### 章节结构顺序（不可变）

```
TL;DR → 什么是XXX（section）→ 如何工作（howItWorks）→ 各类型工具详细介绍（bestTools）
→ 工具对比表格（comparisonSection）→ 应用场景（useCases）→ 如何选择（howToChoose）
→ 结论（section）→ FAQ → References
```

### JSON block 结构

```jsonc
{
  "version": 1,
  "category": "tools",
  "categoryZh": "工具",
  "blogLayout": {
    "title": "H1 标题（不写年份）",
    "excerpt": "三段式 80–150 字",
    "publishDate": "2026年7月16日",
    "modifiedDate": "2026年7月16日",
    "readTime": "12分钟",
    "pageUrl": "/blog/image-generator",
    "locale": "zh",
    "heroImage": "/blog/image-generator/hero.jpg",
    "heroImageAlt": "hero 图 alt 文本"
  },
  "blocks": [
    { "type": "tldr", "introduction": "...", "items": ["要点1", "要点2", "要点3"] },
    { "type": "section", "title": "什么是XXX", "paragraphs": ["<p>...</p>"] },
    { "type": "howItWorks", "technologyBase": "...", "advantages": [...] },
    { "type": "bestTools", "introduction": "...", "tools": [
      { "id": "tool-1", "name": "产品名", "shortDescription": "核心定位一句话",
        "imageSrc": "/tools/xxx.jpg", "linkUrl": "https://...", "description": "zh ≥100字" }
    ]},
    { "type": "comparisonSection", "introduction": "...", "table": {...} },
    { "type": "useCases", "introduction": "...", "useCases": [...] },
    { "type": "howToChoose", "introduction": "...", "steps": [
      { "id": "step-1", "title": "步骤标题", "description": "..." }  // 禁止 name 字段！
    ]},
    { "type": "section", "title": "结论", "paragraphs": ["<p>...</p>"] },
    { "type": "faq", "items": [{ "question": "...", "answer": "..." }] },  // ≥8 问
    { "type": "references", "items": [{ "title": "...", "url": "...", "source": "...", "date": "...", "description": "..." }] }
  ]
}
```

### 关键约束

| 约束项 | 标准 |
|--------|------|
| `bestTools` 每产品 `description` | ZH ≥100 字，EN ≥280 字符；三段式（核心定位+关键差异+最佳适用场景） |
| `howToChoose.steps[].title` | 必须用 `title`，**禁止 `name` 字段**；完整规范见 [section-how-to](../../content/sections/section-how-to.md) |
| `faq.items` 数量 | ≥8 问，答案不复制正文 |
| `references.items` 数量 | ≥10 条，含 URL |
| 内链 | 全文 ≥5 distinct slug，TLDR 0–1 slug，同 slug 仅 1 个 `<a>` |
| H1 | 不写年份；推荐「类型：核心价值」（如「AI 图片生成器：将文字转为惊艳视觉」） |

---

## 二、Marketing 策略/案例型

### 章节结构（指南式编排）

```
TL;DR → 概念定义（section）→ 策略/方法论 ×N（section）→ 案例（useCases / section）
→ 结论（section）→ FAQ → References
```

可选块：`bestTools`（当需要推荐工具时）、`howItWorks`（当需要解释技术原理时）、`html`（当需要嵌入自定义内容时）。

### JSON block 结构差异

```jsonc
{
  "version": 1,
  "category": "marketing",
  "categoryZh": "营销",
  "categorySecondary": "affiliate",
  "categorySecondaryZh": "联盟营销",
  "blogLayout": {
    "title": "H1 标题",
    "excerpt": "三段式 80–150 字",
    "publishDate": "2026年7月16日",
    "pageUrl": "/blog/affiliate",
    "locale": "zh",
    "heroHtml": "<div class=\"...\">CTA Hero</div>"  // ← Marketing 特有：Hero CTA HTML
    // 注意：heroImage 与 heroHtml 互斥，勿同时使用
  },
  "blocks": [
    { "type": "tldr", "introduction": "...", "items": [...],
      "skillCta": { "skillId": "...", "label": "..." } },  // ← Marketing 可选 skillCta
    { "type": "section", "title": "什么是XXX", "paragraphs": [...],
      "childrenHtml": "<table>...</table>",  // ← 可嵌入复杂表格/图表
      "subSections": [...] },
    // ... 策略 sections
    { "type": "useCases", "introduction": "...", "useCases": [
      { "id": "case-1", "title": "案例名", "description": "..." }
    ]},
    { "type": "section", "title": "关键指标与数据", "childrenHtml": "<div class='stat-grid'>...</div>" },
    { "type": "section", "title": "总结", "paragraphs": [...] },
    { "type": "faq", "items": [...] },
    { "type": "references", "items": [...] }
  ]
}
```

### 关键约束

| 约束项 | 标准 |
|--------|------|
| `blogLayout.heroHtml` | 与 `heroImage` 互斥；用于 CTA Hero |
| `section.childrenHtml` | 可嵌入复杂表格、数据可视化 |
| `tldr.skillCta` | 可选，链接到对应的 Alignify Agent Skill |
| `useCases` 每个用例 | `description` ZH ≥80 字，含具体数据/结果 |
| FAQ | ≥3 问（非硬性 8 问，与 tools 型不同） |
| `category` + `categorySecondary` | 根级需同时填两个分类 |
| 内链 | 全文 ≥3 distinct slug，策略文中优先链到 tools 型工具页 |

---

## 三、SEO 指南/教程型

### 章节结构

```
TL;DR → 概念定义（section）→ 操作步骤 ×N（section，subSections 重使用）
→ 实际应用（useCases / section）→ 结论（section）→ FAQ → References
```

### JSON block 结构差异

```jsonc
{
  "version": "2.0",  // ← SEO 类型用 v2.0
  "category": "seo",
  "categoryZh": "SEO",
  "blogLayout": {
    "title": "H1 标题",
    "excerpt": "三段式 80–150 字",
    "publishDate": "2026年7月16日",
    "pageUrl": "/blog/keyword-research",
    "locale": "zh"
    // ← SEO 类型通常无 heroImage
  },
  "blocks": [
    { "type": "tldr", "introduction": "...", "items": [
      { "title": "核心要点", "content": "..." },  // ← SEO 用 {title, content} 对象格式
      { "title": "...", "content": "..." }
    ]},
    { "type": "section", "title": "什么是XXX", "paragraphs": [...],
      "subSections": [
        { "title": "关键概念", "paragraphs": [...], "childrenHtml": "<pre><code>...</code></pre>" }
        // ← childrenHtml 可嵌入代码示例
      ]
    },
    // ... 操作步骤 sections，每个步骤一个 section
    { "type": "useCases", "introduction": "...", "useCases": [...] },
    { "type": "section", "title": "常见误区与最佳实践", "paragraphs": [...] },
    { "type": "section", "title": "总结", "paragraphs": [...] },
    { "type": "faq", "items": [...] },
    { "type": "references", "items": [...] }
  ]
}
```

### 关键约束

| 约束项 | 标准 |
|--------|------|
| `version` | `"2.0"`（区别于 tools 的 `1`） |
| `tldr.items` 格式 | 用 `{title, content}` 对象，非纯字符串 |
| `subSections` | 重使用；每步操作一个 subSection |
| `childrenHtml` | 可嵌入代码块（`<pre><code>`）、配置示例 |
| 技术术语 | 首次出现时需解释或给出中英对照 |
| FAQ | ≥3 问，优先覆盖实操类问题 |

---

## 四、Insights 行业分析型

### 章节结构

```
TL;DR → 核心正文（html 长文块）→ 结论（section）→ FAQ → References
```

这是最特殊的类型：主体内容通过单个 `type: "html"` block 承载，所有排版完全由 HTML 控制。

### JSON block 结构差异

```jsonc
{
  "version": 1,
  "category": "insights",
  "categoryZh": "洞察",
  "blogLayout": {
    "title": "H1 标题",
    "excerpt": "三段式 80–150 字",
    "publishDate": "2026年7月16日",
    "pageUrl": "/blog/ai-product-naming",
    "locale": "zh"
    // ← 通常无 heroImage
  },
  "blocks": [
    { "type": "tldr", "introduction": "...", "items": [
      { "title": "...", "content": "..." }  // ← Insights 也偏向对象格式
    ]},
    { "type": "html", "className": "prose max-w-none", "html": "<h2>...</h2><p>...</p>..." },
    // ← 整个文章的主体走这一个 html block！
    // 其中可以包含任意 H2/H3/表格/图片/列表
    { "type": "section", "title": "关键洞察与展望", "paragraphs": [...] },
    { "type": "faq", "items": [...] },
    { "type": "references", "items": [...] }
  ]
}
```

### 关键约束

| 约束项 | 标准 |
|--------|------|
| `html` block 的 `className` | 通常为 `"prose max-w-none"`（Tailwind Typography） |
| `html` 内容完整性 | `html` 块内必须是一个完整文章的 HTML，从 H2 开始 |
| 内链 | 可在 HTML 块内使用 `<a href="/blog/...">` 硬编码内链 |
| FAQ | ≥3 问 |
| 引用与数据 | 所有事实性论断需在 `references` 里有对应出处 |

---

## 五、类型判定决策树

```
知识块在 knowledge/tools/ → routeCategory "tools" → Tools 榜单/对比型 → Best 型 Meta
知识块在 knowledge/marketing/ → routeCategory "marketing" → Marketing 策略/案例型 → 策略型 Meta
知识块在 knowledge/seo/：
  ├── 偏工具选型 → routeCategory "tools" → 指南型 Meta（含「如何」）
  └── 偏策略方法 → routeCategory "marketing" → 指南型 Meta
知识块在 knowledge/insights/：
  ├── 纯行业分析报告 → 分析型 Meta（含「分析」/「全景」）
  └── 含工具推荐 → Insights 的 html 型结构 + 分析型 Meta
```

---

## 六、各类型字数与格式底线速查

| 指标 | Tools | Marketing | SEO | Insights |
|------|-------|-----------|-----|----------|
| **H1 标题** | ≤30 字，不写年份 | ≤30 字 | ≤30 字 | ≤30 字 |
| **Excerpt** | 80–150 字 | 80–150 字 | 80–150 字 | 80–150 字 |
| **总字数（叙事）** | ≥2,000 字 | ≥2,500 字 | ≥2,000 字 | ≥2,500 字 |
| **bestTools 每产品 desc** | ZH ≥100 字 | EN ≥60 字（如有） | — | — |
| **useCases 每用例** | ZH ≥60 字 | ZH ≥80 字 | ZH ≥60 字 | — |
| **FAQ 数量** | ≥8 问 | ≥3 问 | ≥3 问 | ≥3 问 |
| **References 数量** | ≥10 条 | ≥5 条 | ≥5 条 | ≥5 条 |
| **内链 distinct slug** | ≥5 | ≥3 | ≥3 | ≥3 |
| **images** | heroImage + bestTools 图片 | heroHtml 或 heroImage | 通常无 | 通常无 |

---

*article-types.md · v1.0 · 2026-07-16*
