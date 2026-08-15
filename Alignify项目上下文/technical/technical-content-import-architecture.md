# 页面内容导入架构

本文档定义 Tools、SEO、Marketing、Insights、Events、Blog 等**内容型页面**的统一数据流与渲染管线。

**来源**：`src/lib/page-data.ts` → `src/content/render/ArticleFromJson.tsx`（部署仓源码）。

---

## 一、数据流全景

```
content/{category}/{en,zh}/{slug}.json          ← 构建时 readFileSync + JSON.parse
        │
        ▼
  getPageData(category, slug, locale)            ← src/lib/page-data.ts
        │  返回 ArticleDocV1
        ▼
  ArticleFromJson({ doc, imageUrl, heroContent }) ← src/content/render/ArticleFromJson.tsx
        │
        ├─ renderBlock() 按 block.type 分发 ──→ Tldr / Section / HowItWorks / BestTools /
        │                                        UseCases / HowToChoose / FAQ / References /
        │                                        Table / comparisonSection / html / table
        │
        ▼
  BlogLayout                                      ← Hero + TOC + 内容区 + FAQ（底部全宽）
        │  layout="standard" | "article"
        ▼
  ConditionalChrome                               ← TopBanner → Header → BreadcrumbNav → Footer
```

### page.tsx 职责

所有内容页的 `page.tsx` 结构一致——仅负责导入、调用 `getPageData()` 和传递 `ArticleFromJson`：

```tsx
import { getPageData } from "@/lib/page-data";
import ArticleFromJson from "@/content/render/ArticleFromJson";

export default async function Page({ params }) {
  const { locale, slug } = await params;
  const doc = getPageData("blog", slug, locale as "en" | "zh");
  if (!doc) notFound();
  return <ArticleFromJson doc={doc} imageUrl={getXxxArticleImage(slug)} />;
}
```

**无需创建新的 page.tsx 文件**：每个 category 使用独立动态路由 `app/[locale]/{category}/[slug]/page.tsx`，由 `generateMetadata()` 从对应 Meta 注册表（如 `BLOG_META`）自动输出 title/description。

---

## 二、支持的 category 与文件位置

| Category | 路由 | 数据文件路径 | Meta 注册表 | 图片函数 |
|----------|------|-------------|-----------|---------|
| tools | `/tools/[slug]` | `content/tools/{en,zh}/{slug}.json` | `tools-meta.ts` | `getToolsArticleImage()` |
| blog | `/blog/[slug]` | `content/blog/{en,zh}/{slug}.json` | `blog-meta.ts` | `getBlogArticleImage()` |
| seo | `/seo/[slug]` | `content/seo/{en,zh}/{slug}.json` | `seo-meta.ts` | `getSeoArticleImage()` |
| marketing | `/marketing/[slug]` | `content/marketing/{en,zh}/{slug}.json` | `marketing-meta.ts` | `getMarketingArticleImage()` |
| insights | `/insights/[slug]` | `content/insights/{en,zh}/{slug}.json` | `insights-meta.ts` | `getInsightsArticleImage()` |
| events | `/events/[slug]` | `content/events/{en,zh}/{slug}.json` | `events-meta.ts` | `getEventsArticleImage()` |

**例外**：`/glossary/[slug]` 不经过 `getPageData()` → `ArticleFromJson` 管线，而是使用 `BlogLayout` + `GlossaryPageContent` 直接导入内容。

---

## 三、类型系统

所有 JSON 文件由 `src/content/types/article-doc.ts` 中的 `ArticleDocV1` / `ArticleBlock`（可辨识联合体）进行类型校验。JSON 顶层结构：

```typescript
{
  category: "coding-dev",         // 内部路由区分
  categorySecondary?: "ai-agents", // 可选第二品类标签
  blogLayout: {
    title: string,
    excerpt: string,
    readTime: string,
    publishDate: string,
    modifiedDate: string,
    pageUrl: string,
    locale: "zh" | "en",
    heroHtml?: string             // 可选：自定义 Hero 内容
  },
  blocks: ArticleBlock[]          // 11 种 block 类型
}
```

---

## 四、Block 类型 → 组件映射

`renderBlock()` 将每个 JSON block 的 `type` 字段分发到对应 React 组件：

| JSON type | 组件 | 说明 |
|-----------|------|------|
| `tldr` | Tldr | 核心要点，含 ItemList Schema |
| `section` | Section | 通用 H2/H3 + 段落（什么是 XXX、结论等） |
| `howItWorks` | HowItWorks | 技术原理（三段式） |
| `bestTools` | BestTools | 产品推荐卡片 |
| `useCases` | UseCases | 应用场景列表 |
| `howToChoose` | HowToChoose | 5 步选型指南，含 HowTo Schema |
| `faq` | FAQ | 手风琴问答，含 FAQ Schema |
| `references` | References | 编号引用列表 |
| `comparisonSection` | Table（+ H2） | 对比表格（常用） |
| `table` | Table（+ 可选 H2） | 通用表格 |
| `html` | 无（直接渲染） | 原始 HTML |

---

## 五、内容区容器

所有内容页面正文统一包裹：

```tsx
<div className="space-y-12 blog-post-content">
  {contentBlocks.map((b, i) => renderBlock(b, i, locale, enableArticleLayout))}
</div>
```

**全站统一**：Tools / Blog / SEO / Marketing / Insights / Events 均使用 `space-y-12 blog-post-content`。

---

## 六、Meta 与页面配置

- **Meta 唯一维护位置**：各 category 的 Meta 注册文件（如 `blog-meta.ts`、`tools-meta.ts`）
- **自动输出**：由 `generateMetadata()` 从注册表读取，无需在 page.tsx 中硬编码
- **H1 与 excerpt**：在 JSON `blogLayout` 中维护，即页面数据文件的权威来源
