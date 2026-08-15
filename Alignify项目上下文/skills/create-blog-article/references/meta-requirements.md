# Meta Requirements — 四种 Meta 规则组 × 注册方式

> **路径**：`skills/create-blog-article/references/meta-requirements.md`
> **用途**：定义 Tools / Marketing / SEO / Insights 四种类型的 Meta title/description/H1/Excerpt 格式模板、publishDate 双重位置规则、routeCategory 与 hubCategory 填写规范。
> **版本**：v1.0 · 2026-07-16

---

## 一、四种 Meta 规则组

### 1. Best 型（Tools 榜单/对比）

| 要素 | 中文约束 | 英文约束 |
|------|---------|---------|
| **Meta title** | 须含「最佳」、全角年份 `（2026）`、中文冒号 `：`副线、`\| Alignify` | 须含 `Best`、半角年份 `(2026)`、英文冒号 `:`副线、`\| Alignify` |
| **Meta description** | 列举 2–3 个代表产品，60–80 字 | 列举 2–3 个代表产品，120–160 字符 |
| **H1** | 不写年份；推荐「类型：核心价值」 | 不写年份，40–60 字符 |
| **Excerpt** | 三段式 80–150 字，禁用通用结尾 | 三段式 200–250 字符 |

**示例**：
- ZH title：`2026年最佳AI图片生成器：文字转图像工具精选 | Alignify`
- EN title：`Best AI Image Generators (2026): Top Text-to-Image Tools | Alignify`

### 2. 策略型（Marketing 策略/案例）

| 要素 | 中文约束 | 英文约束 |
|------|---------|---------|
| **Meta title** | 须含「指南」或「策略」、`（2026）`、`：`副线、`\| Alignify` | 须含 `Guide` 或 `Strategy`、`(2026)`、`:`副线、`\| Alignify` |
| **Meta description** | 点明价值主张 + 覆盖要点，50–70 字 | 点明价值主张 + 覆盖要点，100–140 字符 |
| **H1** | 含「指南」或「如何」，不写年份 | 40–60 字符 |
| **Excerpt** | 三段式 80–150 字 | 三段式 200–250 字符 |

**示例**：
- ZH title：`Affiliate营销完整指南（2026）：策略与工具 | Alignify`
- EN title：`Affiliate Marketing Guide (2026): Strategy & Tools | Alignify`

### 3. 指南型（SEO 指南/教程）

| 要素 | 中文约束 | 英文约束 |
|------|---------|---------|
| **Meta title** | 须含「如何」或「指南」、`（2026）`、`：`副线、`\| Alignify` | 须含 `How to` 或 `Guide`、`(2026)`、`:`副线、`\| Alignify` |
| **Meta description** | 明确解决的问题 + 学习方法，50–70 字 | 明确解决的问题 + 学习方法，100–140 字符 |
| **H1** | 以「如何」开头或含「指南」 | 以 `How to` 开头或含 `Guide` |
| **Excerpt** | 三段式 80–150 字 | 三段式 200–250 字符 |

**示例**：
- ZH title：`如何选择域名（2026）：完整SEO域名指南 | Alignify`
- EN title：`How to Choose a Domain Name (2026): SEO Guide | Alignify`

### 4. 分析型（Insights 行业分析）

| 要素 | 中文约束 | 英文约束 |
|------|---------|---------|
| **Meta title** | 须含「分析」或「全景」或「趋势」、`（2026）`、`：`副线、`\| Alignify` | 须含 `Analysis` 或 `Landscape` 或 `Trends`、`(2026)`、`:`副线、`\| Alignify` |
| **Meta description** | 核心洞察摘要，60–80 字 | 核心洞察摘要，120–160 字符 |
| **H1** | 含「分析」「全景」「深度解读」之一 | 40–60 字符 |
| **Excerpt** | 三段式 80–150 字 | 三段式 200–250 字符 |

**示例**：
- ZH title：`AI产品命名全景分析（2026）：策略、案例与趋势 | Alignify`
- EN title：`AI Product Naming Analysis (2026): Strategy, Cases & Trends | Alignify`

---

## 二、Meta 注册规范

### blog-meta.ts 注册格式

```typescript
// src/data/blog-meta.ts
export const BLOG_META: Record<string, PageMeta> = {
  "your-slug": {
    en: {
      title: "English Meta Title | Alignify",
      description: "English meta description (120–160 chars)"
    },
    zh: {
      title: "中文 Meta Title | Alignify",
      description: "中文 meta description (60–80 字)"
    },
    publishDate: "2026-07-16",  // YYYY-MM-DD 格式
    modifiedDate: "2026-07-16", // YYYY-MM-DD 格式
  }
};
```

### blog-pages-config.ts 注册格式

```typescript
// src/data/blog-pages-config.ts
export const BLOG_PAGES_CONFIG: BlogPageItem[] = [
  {
    slug: "your-slug",
    shortTitleEn: "Short English Title",
    shortTitleZh: "短中文标题",
    routeCategory: "tools",  // "tools" | "marketing"
    toolsHubCategory: "image",  // 仅 routeCategory="tools" 时必填
    // 或
    // marketingHubCategory: "affiliate",  // 仅 routeCategory="marketing" 时必填
    hubKeywordEn: "keyword",
    hubKeywordZh: "关键词",
  }
];
```

### routeCategory 决策

| 知识块目录 | routeCategory | 需额外填空的字段 |
|-----------|---------------|-----------------|
| `knowledge/tools/` | `"tools"` | `toolsHubCategory`（必须在 `tools-pages-config.ts` 中已有定义的分组名） |
| `knowledge/marketing/` | `"marketing"` | `marketingHubCategory`（必须在 `marketing-pages-config.ts` 中已有定义的分组名） |
| `knowledge/seo/` | 视内容而定 | `toolsHubCategory` 或 `marketingHubCategory` |
| `knowledge/insights/` | 视内容而定 | `toolsHubCategory` 或 `marketingHubCategory` |

### toolsHubCategory 可用值（参考部署仓 `tools-pages-config.ts`）

常用的分组名示例：`image`, `video`, `audio`, `design`, `3d`, `dev`, `search`, `llm`, `productivity`, `marketing`, `vertical`。**以部署仓文件实时内容为准**。

### marketingHubCategory 可用值（参考部署仓 `marketing-pages-config.ts`）

常用的分组名示例：`affiliate`, `creator`, `influencer`, `pricing`, `content-seo`, `localization`, `social`, `referral`。**以部署仓文件实时内容为准**。

---

## 三、publishDate 双重位置

| 位置 | 格式 | 用途 |
|------|------|------|
| `blog-meta.ts` 的 `publishDate` | `"2026-07-16"`（ISO 日期） | SEO（`<meta>` 标签、sitemap `<lastmod>`） |
| JSON `blogLayout.publishDate` | 中文 `"2026年7月16日"` / 英文 `"July 16, 2026"` | 页面 Hero 区域展示 |

两处必须**内容一致**（日期相同，仅格式不同）。

### modifiedDate

- 新文章创建时 `modifiedDate` = `publishDate`
- 后续更新文章时**仅当有实质内容更新**才修改 `modifiedDate`
- `modifiedDate` 同样有两处同步要求

---

## 四、常见 Meta 错误

| 错误 | 正确做法 |
|------|---------|
| H1 写了年份 | H1 不写年份，年份只在 Meta title 和 URL slug 中体现 |
| Meta title 缺 `| Alignify` | 末尾必须加 `| Alignify` |
| 中文 Meta title 用半角 `:` | 中文用全角 `：`，英文用半角 `:` |
| 中文年份用半角括号 `(2026)` | 中文用全角 `（2026）` |
| routeCategory 与知识块目录不匹配 | `knowledge/marketing/` → routeCategory 必须是 `"marketing"` |
| toolsHubCategory 填了不存在的分组名 | 必须从 `tools-pages-config.ts` 中读取可用的分组名 |
| 两个 locale 的 Meta title 是逐字翻译 | 中英文各有各的 SEO 关键词策略，意译即可 |

---

*meta-requirements.md · v1.0 · 2026-07-16*
