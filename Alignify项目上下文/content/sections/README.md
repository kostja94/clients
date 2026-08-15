# Section 章节规范文档

本目录存放**跨页面通用**的内容块规范。Section 定义格式、字数、组件用法、禁止项，**不区分**页面类型（Tools/SEO/Marketing）。

- **页面类型**：见 [templates](../templates/README.md)
- **项目总索引**：见 [README.md](../../README.md)

## 部署组件清单

> 来源：部署仓 `src/components/`，共 48 个 `.tsx` 文件。以下按职责分类，以组件源码为准。

### 一、内容块组件（ArticleFromJson 调度，`renderBlock` 分发）

共 9 个组件 + 1 个 `comparisonSection`（H2 + Table 组合），对应 `ArticleBlock.type` 字段：

| 组件文件 | JSON type | Props 核心字段 | 结构化数据 | 说明 |
|----------|-----------|---------------|-----------|------|
| `Tldr.tsx` | `tldr` | `title`, `introduction`, `items[]`, `skillCta`, `variant` | ItemList Schema | card / border-left 双变体；4-5 条要点；GEO 优化 |
| `Section.tsx` | `section` | `level`(2\|3), `title`, `paragraphs[]`, `subSections[]`, `contentBodyPreset` | — | 通用 H2/H3 + 段落；支持 prose 模式、children 插入 |
| `HowItWorks.tsx` | `howItWorks` | `technologyBase`, `advantages[]`, `architectureDifferences` | — | 技术基础段 + `<ul>` 优势列表 + 架构差异段 |
| `BestTools.tsx` | `bestTools` | `introduction`, `tools[]`(含 image/video/linkUrl/description) | — | 排名工具卡片；YT 缩略图回退；外链 UTM 处理 |
| `UseCases.tsx` | `useCases` | `introduction`, `useCases[]`(id/title/description) | — | H3 列表，每项有独立 id 锚点 |
| `HowToChoose.tsx` | `howToChoose` | `introduction`, `steps[]`，支持 `wrapperClassName` | HowTo Schema | 编号步骤（1. 2. 3. ...），3–5 步（见 section-how-to） |
| `FAQ.tsx` | `faq` | `items[]`(单语/双语), `locale` | FAQ Schema | `<details>` 手风琴；双语文案自动选择；自含 `<section>` |
| `References.tsx` | `references` | `items[]`(title/url/source/date/description), `showDivider` | — | `<ol>` 编号外链；中英日期解析；UMT 外链处理 |
| `Table.tsx` | `table` / `comparisonSection` | `items[]`(语义) / `columns[]+data[]`(通用) / `children`(原生) | — | 三模式：ComparisonTable / 通用列+数据 / 原生 `<table>` |
| （无独立组件） | `html` | `html`, `className` | — | 直接渲染 `dangerouslySetInnerHTML` |
| （无独立组件） | `comparisonSection` | `h2Text`, `h2Id`, `introHtml`, `table` | — | H2 标题 + 引导文字 + `renderTable(block)` |
| （无独立组件） | `table` | `title`, `introduction`, `table`(items/columns/headers) | — | 可选 H2 + 引导文字 + `renderTable(block)` |

### 二、布局壳层组件

| 组件文件 | 职责 | 关键特性 |
|----------|------|----------|
| `BlogLayout.tsx` | 文章页整体壳层 | 两种布局：`standard`(居中单列) / `article`(左右网格+TOC侧边栏)；内置 Article Schema、ShareButtons、ShareRail；FAQ 从 blocks 中分离到底部全宽渲染；category badge 显示 |
| `ConditionalChrome.tsx` | 全局页面包裹器 | `/skills` 路径跳过壳层；普通页面自上而下：TopBanner → Header → BreadcrumbNav → children → SecondaryCta → Footer |
| `Header.tsx` | 导航栏 | — |
| `Footer.tsx` | 页脚 | — |
| `BreadcrumbNav.tsx` | 面包屑导航 | 粘性定位；JSON-LD BreadcrumbList；按路由自动匹配 |
| `TopBanner.tsx` | 顶部推广横幅 | 可关闭；localStorage 持久化状态 |
| `SecondaryCta.tsx` | 底部上下文 CTA | 按路由匹配不同内容 |
| `ArticleTOC.tsx` | 侧边栏目录 | 粘性定位；H2/H3 自动提取；支持 html block 中的 heading 解析 |
| `ShareButtons.tsx` | 分享按钮组 | 横向排列 |
| `ShareRail.tsx` | 侧边栏分享 | 竖向排列 |

### 三、首页章节组件

| 组件文件 | 说明 |
|----------|------|
| `Chapter01Problem.tsx` | 首页叙事章节 1 |
| `Chapter02Shift.tsx` | 首页叙事章节 2 |
| `Chapter03Levers.tsx` | 首页叙事章节 3 |
| `Chapter04Receipts.tsx` | 首页叙事章节 4 |
| `Chapter05Promise.tsx` | 首页叙事章节 5 |
| `HeroSection.tsx` | 首页大标题 Hero |
| `TrustedBySection.tsx` | 首页客户 Logo 走马灯 |

### 四、特殊页面组件

| 组件文件 | 使用页面 | 说明 |
|----------|----------|------|
| `PartnershipPageContent.tsx` | partnership | 合作伙伴页面内容 |
| `GlossaryPageContent.tsx` | glossary/[slug] | 术语表全文页面 |
| `SkillsTerminal.tsx` | skills landing | 技能安装终端 |
| `SkillsCategoryGrid.tsx` | skills landing | 技能分类树 |
| `PromoCode.tsx` | betalist | 可展开的推广码复制块 |
| `LinkloudScaleXPopup.tsx` | `[locale]/layout.tsx` | 仅中文用户弹出 Linkloud ScaleX 推广弹窗 |

### 五、子组件（被父组件内部使用）

| 组件文件 | 父组件 | 说明 |
|----------|--------|------|
| `YouTubeThumbnailImage.tsx` | BestTools | 图片渲染，支持静态图 + YouTube 缩略图（`maxresdefault.jpg`）回退 |
| `TldrSkillCta.tsx` | Tldr | npx 命令复制块，skill promo CTA |
| `CustomerCaseCard.tsx` | CustomerTabs | 客户案例卡片 |
| `CustomerStoriesHeroLogos.tsx` | customer-stories page | 客户 Logo 网格 |

### 六、全局功能性组件

| 组件文件 | 调用位置 | 说明 |
|----------|----------|------|
| `GoogleTagManager.tsx` | 根 `layout.tsx` | GTM 脚本 + `<noscript>` 回退 |
| `PageViewTracker.tsx` | `[locale]/layout.tsx` | 路由切换虚拟 PV 追踪 |
| `CookieConsent.tsx` | `[locale]/layout.tsx` | GDPR Cookie 横幅 |

### 七、已定义但未上线的组件

| 组件文件 | 说明 |
|----------|------|
| `YouTubeThumbnail.tsx` | 独立视频缩略图组件（`videoId` + `videoUrl`），计划用于 SEO/Insights 文章嵌入，尚未接入 ArticleFromJson |

### 八、UI 基础组件（shadcn/ui，`src/components/ui/`）

| 文件 | 说明 |
|------|------|
| `button.tsx` | 按钮 |
| `tooltip.tsx` | 工具提示 |
| `separator.tsx` | 分隔线 |
| `input.tsx` | 输入框 |
| `card.tsx` | 卡片 |
| `breadcrumb.tsx` | 面包屑基础 |
| `badge.tsx` | 徽章 |
| `sonner.tsx` | Toast 通知 |

### 九、数据流

```
content/{category}/{locale}/{slug}.json     ← 构建时 readFileSync + JSON.parse
        │
        ▼
  getPageData()                              ← src/lib/page-data.ts
        │
        ▼
  ArticleFromJson.renderBlock()              ← src/content/render/ArticleFromJson.tsx
        │ 按 block.type 分发
        ▼
  Tldr / Section / HowItWorks / BestTools / UseCases / HowToChoose / FAQ / References / Table / html
        │
        ▼
  BlogLayout                                 ← Hero + 目录 + 内容区 + FAQ（底部全宽）
        │
        ▼
  ConditionalChrome                          ← TopBanner → Header → BreadcrumbNav → 内容 → SecondaryCta → Footer
```

---

## 使用说明

1. **先查对应 template**：确定页面类型（Tools/SEO/Marketing），查阅对应 template 了解章节顺序和本类型特有规则
2. **再查 section**：各章节的格式、字数、组件用法见本目录对应 section
3. **组件源码为准**：本目录文档以部署仓 `src/components/` 源码为事实来源，若有出入请以源码为准

## 组件 → Section 文档索引

| 组件 | Section 文档 |
|------|-------------|
| Tldr | [section-tldr.md](./section-tldr.md) |
| Section | [section-generic.md](./section-generic.md) |
| HowItWorks | [section-how-it-works.md](./section-how-it-works.md) |
| BestTools | [section-best-tools.md](./section-best-tools.md) |
| UseCases | [section-use-cases.md](./section-use-cases.md) |
| HowToChoose | [section-how-to.md](./section-how-to.md)（唯一真相源：定位分工 / 3–5 步 / 去模板 / 决策分叉 / 组件与 Schema / 审计） |
| FAQ | [section-faq.md](./section-faq.md) |
| References | [section-references.md](./section-references.md) |
| Table | [section-comparison-table.md](./section-comparison-table.md) |
| YouTubeThumbnailImage | [section-youtube-thumbnail.md](./section-youtube-thumbnail.md) |
| BlogLayout | [section-hero.md](./section-hero.md) |
| Header / Footer | [section-nav.md](./section-nav.md) |
| BreadcrumbNav | [section-breadcrumb.md](./section-breadcrumb.md) |
| ShareButtons / ShareRail | [section-share-buttons.md](./section-share-buttons.md) |

> **内容导入架构**（ArticleFromJson 数据流）已移至 [technical-content-import-architecture.md](../../technical/technical-content-import-architecture.md)。
