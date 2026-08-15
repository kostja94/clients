# Hero 区域 Section 规范

本文档定义 BlogLayout 的 Hero 区域布局、两种布局模式、作者信息及 category 标签规范。**H1、Excerpt 规范**见 [section-heading-best-practices](../content-rules/section-heading-best-practices.md)。

**来源**：`src/components/BlogLayout.tsx`（部署仓源码）。

---

## 一、适用范围

- 使用 BlogLayout 的 Tools、SEO、Marketing、Insights、Events 页面
- BlogLayout 通过 `layout` prop 控制两种模式：`standard` 和 `article`

---

## 二、两种布局模式

### 2.1 `standard` 模式（居中单列）

**触发条件**：`layout="standard"`（默认），或不满足 `article` 条件时自动使用。

- **结构**：标题、摘录、作者行、分享按钮在 `max-w-4xl` 内**水平居中**（`text-center`、`justify-center`）
- **header 间距**：`pt-20 md:pt-24 pb-14 md:pb-20`
- **背景**：`bg-surface`，底部分割线 `border-b border-border/50`
- **垂直间距**：英文 `space-y-4`，中文 `space-y-6`
- **heroContent**：有实质内容时，渲染在标题块下方，容器 `w-full max-w-6xl mt-10 md:mt-12`

### 2.2 `article` 模式（左右网格 + 侧边栏 TOC）

**触发条件**：`layout="article"` 且 `tocItems.length > 0`。ArticleFromJson 自动为 `/tools/`、`/seo/`、`/marketing/`、`/insights/`、`/events/` 路径启用。

- **结构**：左右两栏 Grid（`lg:grid-cols-2`），左栏文字、右栏封面图
- **左栏**：category badge + H1 + excerpt + 作者行
- **右栏**：coverImage（`aspect-[1200/630]`，圆角 `rounded-xl`，边框 `border`）
- **正文区**：`lg:grid-cols-12` 网格，左侧 `lg:col-span-3` 为粘性 TOC + ShareRail，右侧 `lg:col-span-9` 为内容区
- **H1 样式**：`text-4xl md:text-5xl lg:text-6xl font-normal leading-[1.05]`

### 2.3 `hideHero` 模式

当 `hideHero=true` 时，Hero 区域完全隐藏，H1 直接渲染在 `<main>` 内容区顶部。

---

## 三、Category 标签

BlogLayout 支持在 Hero 内显示品类标签（来自 `category` 和 `categorySecondary` prop）：

| 模式 | 位置 | 样式 |
|------|------|------|
| `standard` | H1 上方居中 | `px-3 py-1 text-xs rounded-full bg-primary/10 text-primary border border-primary/20` |
| `article` | H1 上方左对齐 | 同上 |

可用的 category ID 及中英文标签：

| ID | 中文 | 英文 |
|----|------|------|
| `ai-video` | AI视频与动画 | AI Video & Animation |
| `ai-audio` | AI音频与语音 | AI Audio & Voice |
| `ai-creative` | AI创意与设计 | AI Creative & Design |
| `ai-text` | AI文本与写作 | AI Text & Writing |
| `coding-dev` | 编码与开发 | Coding & Dev Tools |
| `ai-agents` | AI智能体与模型 | AI Agents & Models |
| `data-infra` | 数据与网络基础设施 | Data & Web Infra |
| `search-geo` | 搜索与GEO | Search & GEO |
| `marketing` | 营销与增长 | Marketing & Growth |
| `business` | 商业与垂直行业 | Business & Verticals |
| `insights` | 洞察与报告 | Insights & Reports |

---

## 四、作者信息区域

- **作者**：默认 "Kostja"，通过 `author` prop 传入。标准模式显示纯文本链接（`/author/kostja`），article 模式带圆形头像 + 可点击的 Link。
- **日期**：优先 `modifiedDate`，无则 `publishDate`。中文显示「更新于 YYYY-MM-DD」，英文「Updated on YYY-MM-DD」。
- **readTime**：默认 `8 min read` / `8 分钟阅读`，通过 `readTime` prop 覆盖。

---

## 五、分享按钮

- **standard 模式**：ShareButtons 在作者行下方 `pt-2`，居中
- **article 模式**：ShareRail 在左侧 TOC 下方（侧边栏竖向排列），不显示 ShareButtons
- **详细**：见 [section-share-buttons](./section-share-buttons.md)

---

## 六、Author Avatar

article 模式在作者行显示 Kostja 头像（`/avatars/kostja-avatar.png`），28×28 圆形。

---

## 七、站内其他 Hero（非 BlogLayout）

- **中英文首页**：`HeroSection` 为单列居中，精选图置于 CTA 下方
- **`/skills` 着陆页**：保留桌面端左文右终端的双栏编排，不走 BlogLayout（`ConditionalChrome` 中 `/skills` 路径跳过 Header/Footer）
