# Tools 文章 10 节结构 × 组件 × JSON 字段映射

> **来源**：`content/templates/template-tools.md` §一、[technical/technical-content-import-architecture.md](../../technical/technical-content-import-architecture.md)
> **版本**：v2.0 · 2026-06-23

---

## 一、结构顺序（不可变）

| 序号 | 章节 | 组件 | JSON block type | 必需 |
|------|------|------|-----------------|------|
| 1 | 核心要点 | `Tldr` | `tldr` | ✅ |
| 2 | 什么是 XXX | `Section` (Generic) | `section` | ✅ |
| 3 | XXX 如何工作 | `HowItWorks` | `howItWorks` | ✅ |
| 4 | 各类型工具介绍 | `BestTools` | `bestTools` | ✅ |
| 5 | 工具对比表格 | `Table` | `comparisonSection` | 推荐 |
| 6 | 应用场景 | `UseCases` | `useCases` | ✅ |
| 7 | 如何选择 | `HowToChoose` | `howToChoose` | ✅ |
| 8 | 结论 | `Section` (Generic) | `section` | ✅ |
| 9 | FAQ | `FAQ` | `faq` | ✅（8 问） |
| 10 | 参考文献 | `References` | `references` | 推荐 |

**硬约束**：Conclusion（8）必须在 FAQ（9）之前。

---

## 二、各章节 JSON 字段结构

### 1. TL;DR（核心要点）

```json
{
  "type": "tldr",
  "id": "article-intro",
  "title": "核心要点",
  "introduction": "40-80字中文简介",
  "items": [
    "要点1：一句话核心发现",
    "要点2：关键数据或趋势",
    "要点3：选型建议方向",
    "要点4：与其他品类的区分",
    "要点5：下一步行动指引"
  ]
}
```

**规则**：items 4–5 条；中文 intro 40–80 字；英文 intro 30–60 词。

**内链（R-TLDR）**：
- TLDR（intro + items）≤ **2** distinct slug；**创建时默认 0–1 条**
- Hub 页 TLDR **禁止**枚举 3+ 子品类链；子品类链放在「什么是」第二段
- TLDR 中的 slug **不得**再出现在「什么是」/ section（R-TLDR-3）
- 相邻两链间距 ≥40 字符（R-TLDR-2）
- 详见 [`02c-internal-links-drafting.md`](../02c-internal-links-drafting.md)

### 2. 什么是 XXX（What Is）

```json
{
  "type": "section",
  "title": "什么是 {工具类型}",
  "paragraphs": ["段落1", "段落2", "段落3"],
  "children": []
}
```

**规则**：2–4 段；中文每段 60–120 字；可含 1–2 个内链。

### 3. 如何工作（How It Works）

```json
{
  "type": "howItWorks",
  "id": "how-xxx-work",
  "title": "{工具类型}是如何工作的",
  "technologyBase": "技术原理（220-420字）",
  "advantages": [
    {"name": "优势1", "description": "说明"},
    {"name": "优势2", "description": "说明"},
    {"name": "优势3", "description": "说明"}
  ],
  "architectureDifferences": "架构差异（可选）"
}
```

**规则**：advantages 3–5 项；中文 technologyBase 220–420 字。

### 4. 各类型工具介绍（Best Tools）

```json
{
  "type": "bestTools",
  "id": "best-{slug}-2026",
  "title": "2026 年最好的 {工具分类}",
  "introduction": "1–2 句介绍，说明工具来源与选择标准",
  "tools": [
    {
      "id": "product-slug",
      "name": "产品名",
      "shortDescription": "4–25 字简述",
      "imageSrc": "/blog/{slug}/{image}.jpg",
      "imageAlt": "图片替代文本",
      "linkUrl": "https://...",
      "youtubeUrl": "https://www.youtube.com/watch?v=xxx",
      "description": "100–400字详述（含核心定位 + 关键差异 + 最佳适用场景）"
    }
  ],
  "locale": "zh"
}
```

**规则**：
- `tools` 为扁平数组，**无 categories 嵌套**
- 每个 tool 必填：`id`, `name`, `shortDescription`, `linkUrl`, `description`
- shortDescription 硬底线 ZH 4–25 字 / EN 10–50 字符
- description 硬底线 ZH 100–400 字 / EN 280–800 字符；同页 max/min < 3×
- 图片三选一：`imageSrc`(推荐) / `image`（兼容） / `video`（兼容，自动生成 YT 缩略图）
- 按钮文案自动处理：中文「试试 {name}」/ 英文「Try {name}」

### 5. 对比表格（Comparison Table）

```json
{
  "type": "comparisonSection",
  "h2Id": "{slug}-comparison",
  "h2Text": "{工具类型}工具对比：选择最适合你的",
  "introHtml": "以下是主流{工具类型}工具的对比，帮助您快速了解各工具的特点、应用场景和适用性：",
  "table": {
    "toolType": "{工具类型}",
    "toolTypeEn": "{Tool Type}",
    "columns": ["工具名称", "核心特点", "主要应用场景", "定价模式"],
    "items": [
      {
        "toolName": "产品名",
        "coreFeatures": "特点1、特点2、特点3",
        "bestFor": "最适合场景",
        "pricing": "定价"
      }
    ]
  }
}
```

**规则**：4 列标准结构；`toolName` 不得为空；`bestFor` 必填；`pricing` 必填（无则「待定」）；`coreFeatures` 2–4 个关键词；`items` 嵌套在 `table` 内而非顶层。

### 6. 应用场景（Use Cases）

```json
{
  "type": "useCases",
  "id": "use-cases",
  "title": "{工具类型}都能做什么：{N}大实用场景",
  "introduction": "1-2句引导段，概述场景覆盖范围",
  "useCases": [
    {
      "id": "content-creation",
      "title": "1. 场景名",
      "description": "100-260字场景描述"
    }
  ]
}
```

**规则**：图片工具 4–5 个、视频工具 5–6 个、其他 4–6 个。

### 7. 如何选择（How to Choose）

> **渲染组件**：`src/components/HowToChoose.tsx`（部署仓）只读 `steps[].title`，**禁止**使用 `steps[].name`。完整规范见 [section-how-to](../../content/sections/section-how-to.md)（唯一真相源）。

```json
{
  "type": "howToChoose",
  "id": "how-to-choose-{slug-kebab}",
  "title": "如何选择 {AI} {工具类型}",
  "introduction": "1–2 句引导段，说明选型框架；可含 1–2 个内链 HTML",
  "steps": [
    {
      "id": "step-slug-kebab",
      "title": "步骤标题（显示为 H3）",
      "description": "≥80 字（去 HTML 后）实操说明，含评估维度与可执行动作"
    }
  ],
  "wrapperClassName": ""
}
```

**规则**：
- block **`id`**、**`introduction`**、每步 **`id`** + **`title`** 必填（非 `name`）
- 标准 **5 步**；中文每步 description 硬底线 **≥80 字**；英文 **≥80 词/字符**（去 HTML）
- introduction 硬底线：中文 **≥40 字** / 英文 **≥40 词**
- block `id` 用 slug 级命名（如 `how-to-choose-web-fetch`），勿全站复用 `how-to-choose`
- 标杆：`content/tools/zh/web-search-api.json`、`content/tools/zh/web-scraping.json`

**验收（部署仓）**：
```bash
npm run verify:content-json    # error 级：name 误用、缺 block id、缺 step title
npm run audit:howto-choose     # 全量 warn：缺 step id、intro/描述过短
```

### 8. 结论（Conclusion）

```json
{
  "type": "section",
  "title": "结论",
  "paragraphs": ["段落1", "段落2"]
}
```

**规则**：2–3 段；**允许** 0–2 条内链（与专册 §1.5 一致，仍遵守全文 slug 唯一）；不含 CTA。

### 9. FAQ（常见问题）

```json
{
  "type": "faq",
  "items": [
    {"question": "问题1？", "answer": "答案1"},
    {"question": "问题2？", "answer": "答案2"}
  ]
}
```

**规则**：中英文各 8 问；**Tools/Blog JSON** 的 FAQ **允许**站内链（≤3 个不同 slug、与正文去重，见 [section-faq §3.2](../../content/sections/section-faq.md#32-tools--blog-json-的-faq-块)）；**MDX FAQ** 仍禁止内链。答案 40–80 词。

### 10. 参考文献（References）

```json
{
  "type": "references",
  "items": [
    {"title": "来源标题", "url": "https://..."}
  ]
}
```

---

## 三、blogLayout 配置（JSON 顶层）

```json
{
  "category": "coding-dev",
  "blogLayout": {
    "title": "H1 标题（不写年份）",
    "excerpt": "三段式摘要，避免通用结尾",
    "readTime": "XX 分钟阅读",
    "pageUrl": "https://alignify.co/zh/blog/{slug}"
  },
  "blocks": [...]
}
```

**说明**：
- `category`：JSON 顶层字段，用于内部路由区分。枚举与 `src/data/tools-pages-config.ts` 中的 `ToolsCategory` 一致（如 `"coding-dev"`、`"marketing"`——**以源文件为准**）。
- `heroImage`（封面图）：**不在 blogLayout 中**——Article Schema 的 `imageUrl` 由 ArticleFromJson 外部传入，OG 图在 `blog-article-images.ts` 中单独注册。

---

## 四、Meta 注册（blog-meta.ts 条目示例）

```ts
// src/data/blog-meta.ts — 注意 publishDate/modifiedDate 是 slug 级字段，不在 en/zh 内
export const BLOG_META: Record<string, PageMeta> = {
  "{slug}": {
    en: {
      title: "Best {Tool Type} (2026): {Subtitle} | Alignify",
      description: "Explore the best {tool type} in 2026: {Product A}, {Product B}, and more...",
    },
    zh: {
      title: "最佳{工具类型}（2026）：{副线} | Alignify",
      description: "探索2026年最佳{工具类型}：{产品A}、{产品B}等...",
    },
    publishDate: "2026-06-23",
    modifiedDate: "2026-06-23",
  },
};
```

**publishDate 创建后永不更改**；modifiedDate 每次更新时修改。Tools 成批错开见 Step 7 [`07-tools-modified-date.md`](../../07-tools-modified-date.md)。

---

*tools-article-anatomy · v2.0 · 2026-06-23*
