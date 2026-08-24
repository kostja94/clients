# 聚合页面模板

本文档定义 Alignify 聚合页面的组织和管理规则，用于 `/blog`、`/explore`、`/tools`、`/seo`、`/marketing` 等索引页面。

**参考**：content-rules-common 聚合页面管理规则、[section-consistency](../section/section-consistency.md)（内容型页面一致性）

---

## 〇、一致性规范

**聚合页面**：分类列表格式、链接标签风格、布局结构需在同类型聚合页之间保持一致。新增分类或链接时，参考已有页面的命名与分组方式。

**内容型页面**（Tools、SEO、Marketing）：一致性见 [section-consistency](../section/section-consistency.md) 及各对应 template。

---

## 一、适用范围

| 路径 | 文件位置 | 说明 |
|------|----------|------|
| `/blog` | `src/blogs/BlogIndex.tsx` | 博客索引页面 |
| `/explore` | `app/explore/page.tsx` | 网站内容索引页面 |
| `/tools` | `app/tools/page.tsx` | AI 工具聚合页面 |
| `/seo` | `app/seo/page.tsx` | SEO 优化指南聚合页面 |
| `/marketing` | `app/marketing/page.tsx` | 营销策略聚合页面 |

---

## 二、页面结构（通用）

聚合页面通常包含：

1. **Hero Section**：H1 标题 + 描述段落
2. **分类列表**：按类别分组的链接列表
3. **Footer Stats**：总页面数等统计信息

**布局**：`grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-4 gap-y-2`

**Explore 页面**：使用内联 categories 数据，无 ArticlesSection 等专用组件。中英文分别维护分类列表。

---

## 三、分类规则

### 3.1 BlogIndex.tsx (`/blog`)

| 分类 | 路径匹配 | 数据来源 |
|------|----------|----------|
| SEO 优化类 | `/seo/*` | `app/seo/` |
| 增长策略类 | `/marketing/*`, `/insights/*` | `app/marketing/`, `app/insights/` |
| AI 工具类 | `/tools/*` 主要页面 | 主要工具分类页面 |
| 活动类 | `/events/*` | `app/events/` |

**排除**：聚合页面本身、示例页面（`example-article`）

### 3.2 explore/page.tsx (`/explore`)

- **包含**：SEO、增长策略、AI 工具、活动、资源、行业洞察等
- **格式**：`{ label, url }` 或 `{ chineseKeyword, englishKeyword, chineseDescription, url }`
- **排除**：聚合页面本身、示例页面

### 3.3 tools/page.tsx (`/tools`)

- **分类**：Image & Visual、Video、Audio & Voice、Design、3D、Coding、Search、LLM、Productivity & Business 等
- **内链引用**：新工具页面需在对应分类章节添加链接

### 3.4 seo/page.tsx (`/seo`)

- **分类**：Basic & Learning、Website Structure、Link Building、Technical SEO、Data Analysis
- **路径**：`/seo/*` 的所有页面

### 3.5 marketing/page.tsx (`/marketing`)

- **分类**：按策略类型分组
- **路径**：`/marketing/*` 的所有页面

### 3.6 events 活动页面

- **路径**：`/events/*`（如 `/events/praxis-2025-09-27`）
- **页面专用组件**：**AITrafficTable**（Praxis 等活动中嵌入 AI 流量数据表）

---

## 四、检查频率与更新时机

- **每 3 天检查一次**：确保新创建页面被添加到相应聚合页面
- **创建新页面时**：立即检查并更新相关聚合页面
- **使用检查脚本**：`node scripts/check-aggregation-pages.js`

---

## 五、检查清单

- [ ] `/blog` 包含所有 SEO、增长策略、AI 工具、活动页面
- [ ] `/explore` 包含所有页面
- [ ] `/tools` 在相关章节包含新工具页面链接
- [ ] `/seo` 包含所有 SEO 相关页面
- [ ] 所有链接的 URL 路径正确
- [ ] 排除测试页面和示例页面

---

## 六、注意事项

- **内链引用**：聚合页面内的链接用于组织分类，与文章内容中的 SEO 内链概念不同
- **Tools.tsx**：若使用 `src/legacy-pages/Tools.tsx`，需在「各类型AI工具详细介绍」部分添加内链引用
