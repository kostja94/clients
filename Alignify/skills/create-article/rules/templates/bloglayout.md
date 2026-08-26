# BlogLayout 通用模板

本文档定义 BlogLayout 组件的通用使用规范，适用于 Tools、SEO、Marketing 等使用 BlogLayout 的页面。

**参考**：content-rules-common、[README.md](../README.md)（统一内容导入）、[section-consistency](../consistency.md)（字数与表达一致性）

---

## 〇、一致性规范

**布局层**：BlogLayout 的 title、excerpt、heroContent、readTime 等字段格式需与同类型页面对齐；H1/Excerpt 规范见 [sections/generic.md](../sections/generic.md)。**内容层**：正文章节字数与表达见 [section-consistency](../consistency.md) 及各 content template（tools、marketing、seo）。

---

## 一、适用范围

- Tools 页面（使用 pageConfig）
- SEO 页面（使用 metadata）
- Marketing 页面（使用 metadata）

---

## 二、页面配置结构

### 2.1 Tools 页面：pageConfig

```tsx
export const pageConfig = {
  meta: {
    title: "X款最佳XXX工具（年份）：XXX | Alignify",
    description: "探索年份最佳XXX工具：工具列表。比较核心功能，提升效率。",
    publishDate: "2026年1月6日",
    modifiedDate: "2026年1月6日",
  },
  content: {
    title: "XXX：核心价值描述",
    excerpt: "让...这将帮助你更好地理解和应用这些先进的技术工具，提升工作效率和创造力。",
    readTime: "12 分钟阅读",
  },
};
```

### 2.2 SEO / Marketing 页面：metadata

```tsx
export const metadata = {
  title: "SEO学习指南：资源、工具与最佳实践（2026）| Alignify",
  description: "从零开始学习SEO：涵盖搜索引擎工作原理、关键词研究、技术SEO、链接建设等核心技能。",
  publishDate: "2025年2月11日",
  modifiedDate: "2026年1月15日",
};
```

---

## 三、BlogLayout 使用格式

### 3.1 Tools 页面

**title、excerpt**：使用硬编码字面量，避免引用 pageConfig 导致构建失败。

**publishDate、modifiedDate、readTime**：使用 pageConfig 引用，与 meta/content 保持同步，避免漂移。

```tsx
<BlogLayout
  title="[工具类型]：核心价值描述"
  excerpt="[摘要内容]"
  heroContent={<div></div>}
  publishDate={pageConfig.meta.publishDate}
  modifiedDate={pageConfig.meta.modifiedDate}
  readTime={pageConfig.content.readTime}
  pageUrl="https://alignify.co/zh/tools/xxx"
>
  <section className="space-y-12 blog-post-content">
    {/* 页面内容 */}
  </section>
</BlogLayout>
```

**属性顺序建议**：title → excerpt → heroContent → publishDate → modifiedDate → readTime → pageUrl

### 3.2 SEO / Marketing 页面

```tsx
<BlogLayout
  title="SEO学习指南：从基础到高级"
  excerpt="系统性SEO的完整指南..."
  heroContent={<div></div>}
  publishDate={metadata.publishDate}
  modifiedDate={metadata.modifiedDate}
  readTime="15 分钟阅读"
  pageUrl="/zh/seo/learn-seo"
>
  <section className="space-y-6" id="introduction">
    {/* 页面内容 */}
  </section>
</BlogLayout>
```

### 3.3 格式差异

| 页面类型 | section className | section id |
|----------|-------------------|------------|
| Tools | `space-y-12 blog-post-content` | 通常无 |
| SEO / Marketing | `space-y-12 blog-post-content`（与 Tools 统一） | 可用 `id` 作锚点（如 `id="introduction"`） |

**统一**：新建 Marketing/SEO 页面使用 `space-y-12 blog-post-content`，与 Tools 保持一致。详见 [README.md](../README.md)。

---

## 四、heroContent 要求

- **可为空**：`heroContent={<div></div>}`
- **可为实际内容**：如图片、图表、工具推荐卡片等
- **[CRITICAL] 禁止 H1**：heroContent 中**不得**使用 `<h1>`，BlogLayout 已用 `title` prop 生成 H1
- **使用 div**：装饰性标题用 `<div>` 而非 `<h1>`

---

## 五、页面架构（2026-05-20 迁移后）

Tools 和 Blog 页面使用动态路由（`app/[locale]/tools/[slug]/page.tsx`、`app/[locale]/blog/[slug]/page.tsx`），Meta 注册到 `blog-meta.ts`（或 `tools-meta.ts`），由 `generateMetadata()` 统一输出。**无需创建新的 page.tsx 文件**。

```tsx
// 动态路由示例：app/[locale]/blog/[slug]/page.tsx
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const meta = BLOG_META[params.slug];
  // ... 自动输出 <meta>, OG, Twitter 标签
}
```

---

## 六、Hero 区域配置速查（供生成新页面）

| 项目 | 来源 | 说明 |
|------|------|------|
| 作者 | 默认 | 不传 `author`，BlogLayout 默认 "Kostja" |
| publishDate | pageConfig.meta / metadata | 发布日期 |
| modifiedDate | pageConfig.meta / metadata | 更新日期，Hero 优先显示 |
| readTime | pageConfig.content | 中文格式 `X 分钟阅读`（数字后有空格），英文 `X min read` |
| pageUrl | 硬编码 | 绝对 URL，用于分享按钮 |
| 分享按钮 | 自动 | 传入 pageUrl 即显示 |

---

## 七、实现检查清单

- [ ] BlogLayout 正确导入
- [ ] 页面配置完整（Tools 用 pageConfig，SEO/Marketing 用 metadata）
- [ ] publishDate、modifiedDate、readTime 与 pageConfig 一致，或使用引用
- [ ] pageUrl 正确
- [ ] heroContent 仅出现一次，为 `<div></div>` 或实际内容，**不含 H1**
- [ ] JSON 内容包裹在 `<section>` 中
- [ ] section 使用正确的 className 或 id

---

## 八、布局与全局组件

| 组件 | 适用 | 说明 |
|------|------|------|
| **PageLayout** | zh layout、部分 tools/seo layout | 包装 children，内含 TopBanner |
| **TopBanner** | 全局 | 顶部横幅，在 app/layout.tsx 或 PageLayout 中渲染 |

**PageLayout 用法**：`<PageLayout locale="zh">{children}</PageLayout>`
