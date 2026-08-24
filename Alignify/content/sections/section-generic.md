# Generic Section（普通段落）使用最佳实践

本文档定义 SEO、Marketing 等页面中纯文字章节的规范，使用 `Section` 组件作为 **Generic Section**（普通段落）统一管理标题+段落结构。

**参考**：Section 组件（`src/components/Section.tsx`）

---

## 一、定位与作用

**Generic Section** = 使用 Section 组件承载的普通段落章节，核心作用是：

- **减少重复**：替代重复的 `<div>` + `<h2/h3>` + `<p>` 模式
- **统一样式**：标题、段落样式由组件统一管理
- **支持富内容**：段落可包含链接、加粗、JSX 等

---

## 二、通用规范

### 2.1 组件 Props

- `id`：可选，章节锚点 ID
- `level`：`2 | 3`，H2 或 H3
- `title`：标题文本
- `paragraphs`：`(string | React.ReactNode)[]`，段落内容
- `subSections`：可选，H3 子章节数组
- `className`：可选
- `showDivider`：是否显示分割线（H2 之间）；**Marketing 正文章节默认不显示**，由容器 `space-y-12` 控制间距
- `children`：可选，在段落之间插入列表、表格等

### 2.2 样式

标题、段落、分割线样式遵循 [brand-visual.md §2.2 文本层级定义](../alignify-project-context/brand-visual.md#22-文本层级-l1l6)，由 Section 组件统一实现；本节**不重复声明**具体 Tailwind 类。

---

## 三、适用场景

- **SEO**：什么是 XXX、XXX 如何工作、实施指南等纯文字章节
- **Marketing**：什么是红人营销、联盟计划组成部分等
- **非 Tools**：Tools 页面多用 HowItWorks、BestTools、UseCases 等专用组件

---

## 四、实现示例

### 4.1 简单 H2 章节（纯文本）

```tsx
<Section
  id="what-is-indexing"
  level={2}
  title="什么是网站索引？"
  paragraphs={[
    `搜索引擎索引（Indexing）就是将网页存入数据库的过程...`
  ]}
/>
```

### 4.2 H2 章节（含链接的段落）

```tsx
<Section
  id="what-is-influencer-marketing"
  level={2}
  title="什么是红人营销？"
  showDivider={true}
  paragraphs={[
    <>红人营销是指...根据<a href="..." className="text-primary hover:underline">报告</a>显示...</>,
    `纯文本段落也可以使用字符串`
  ]}
/>
```

### 4.3 H2 章节（含子章节）

```tsx
<Section
  id="link-types"
  level={2}
  title="链接类型"
  paragraphs={[`在SEO领域，链接构建策略离不开三种基础链接类型：`]}
  subSections={[
    {
      id: "external-links",
      title: "出站链接",
      paragraphs: [`出站链接指向其他网站的页面...`]
    },
    {
      id: "internal-links",
      title: "内部链接",
      paragraphs: [`内部链接指向同一网站内的其他页面...`]
    }
  ]}
/>
```

### 4.4 段落间插入列表

```tsx
<Section
  id="link-types"
  level={2}
  title="链接类型"
  paragraphs={[`在SEO领域，链接构建策略离不开三种基础链接类型：`]}
>
  <ul className="list-disc pl-6 space-y-2">
    <li>出站链接（External Links）</li>
    <li>内部链接（Internal Links）</li>
  </ul>
</Section>
```

---

## 五、与专用组件的关系

| 页面类型 | 推荐组件 |
|----------|----------|
| Tools 技术概述 | HowItWorks |
| Tools 产品展示 | BestTools |
| Tools 应用场景 | UseCases |
| Tools 对比表格 | Table |
| SEO/Marketing 纯文字（Generic Section） | Section |
| 参考文献 | References |

---

## 六、常见错误

- ❌ 应在 Tools 用 HowItWorks 却用了 Section
- ❌ 段落中含未转义的特殊字符
- ❌ 子章节 ID 与页面其他 ID 重复
- ✅ 按页面类型选择组件�
