# Glossary 页面模板

本文档定义 Alignify 术语表（Glossary）页面的标准结构，用于 SEO Glossary、Marketing Glossary、AI Glossary 等。

**参考**：GlossaryViewer、GlossaryPageContent 组件、[section-consistency](../section/section-consistency.md)（表达一致性）

---

## 〇、一致性规范

**术语定义**：同一 Glossary 内，各术语定义长度与风格宜相近；定义格式（如「XXX 是指…」）保持一致，便于读者快速扫读。

**内容型页面**（Tools、SEO、Marketing）：一致性见 [section-consistency](../section/section-consistency.md) 及各对应 template。

---

## 一、适用范围

| 路径 | 文件位置 | 说明 |
|------|----------|------|
| `/glossary` | `app/glossary/page.tsx` | 术语表索引页 |
| `/glossary/seo` | `app/glossary/seo/page.tsx` + content/glossary/{en,zh}/seo.json | SEO 术语表 |
| `/glossary/marketing` | `app/glossary/marketing/page.tsx` + content/glossary/{en,zh}/marketing.json | 营销术语表 |
| `/glossary/ai` | `app/glossary/ai/page.tsx` + content/glossary/{en,zh}/ai.json | AI 术语表 |

---

## 二、Glossary 索引页结构

- **Hero Section**：H1「Glossary Index」+ 描述
- **分类列表**：SEO Glossary (180+)、Marketing Glossary (120+)、AI Glossary (140+)
- **Footer Stats**：术语表分类总数

**布局**：`grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4`

---

## 三、子术语表页面

- **数据源**：`content/glossary/{en,zh}/{slug}.json`
- **组件**：GlossaryViewer、GlossaryPageContent
- **结构**：按字母或主题分组的术语列表，每项含术语、定义、可选链接

---

## 四、Metadata 配置

```tsx
export const metadata = {
  title: "[类型] Glossary: 180+ Terms & Definitions | Alignify",
  description: "Comprehensive [类型] glossary: Detailed definitions of 180+ terms...",
  alternates: {
    canonical: "https://alignify.co/glossary/[type]",
    languages: {
      'zh': 'https://alignify.co/zh/glossary/[type]',
      'en': 'https://alignify.co/glossary/[type]',
      'x-default': 'https://alignify.co/glossary/[type]',
    },
  },
  openGraph: { ... },
  twitter: { ... },
};
```

---

## 五、与内容页面的区别

- **无 BlogLayout**：Glossary 页面通常使用专用布局
- **无文章简介、How To、Conclusion**：术语表为词条列表，非指南文章
- **无 FAQ**：术语表本身为定义型内容
