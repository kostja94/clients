# 组件清单 / Component Inventory

> Alignify 部署仓库全部组件的完整目录。每个条目包含：文件路径、Props 接口、功能说明、被哪些模块引用。
> 最后更新：2026-06-09
> 部署仓库：`D:\部署项目\alignify-by-kostja`

---

## 一、页面壳层 / Page Shell

所有页面共享的外层结构组件。

| 组件 | 文件 | Props | 说明 | 引用者 |
|------|------|-------|------|--------|
| **ConditionalChrome** | `src/components/ConditionalChrome.tsx` | `{ children: ReactNode }` | 根据路由决定是否包裹 TopBanner + Header + BreadcrumbNav + SecondaryCta + Footer。Skills 落地页（`(landing)` route group）跳过所有 chrome。 | `app/[locale]/layout.tsx` |
| **TopBanner** | `src/components/TopBanner.tsx` | 无（从 next-intl 读取） | 可关闭的顶部推广横幅，链接到 oginify.com。localStorage 持久化关闭状态。 | `ConditionalChrome.tsx` |
| **Header** | `src/components/Header.tsx` | 无（从 `usePathname` / `useLocale` / `useTranslations` 读取） | 固定顶部导航栏，含 Tools / Marketing / SEO / Resources / About 下拉菜单 + 移动端汉堡菜单 + Skills 安装入口。动态读取 `skills-catalog.json` 显示技能数量。 | `ConditionalChrome.tsx` |
| **Footer** | `src/components/Footer.tsx` | 无（从 `useTranslations` / `useLocale` 读取） | 站点页脚：Logo、导航列（Tools / Marketing / SEO / Resources）、社交链接、版权信息、隐私链接。 | `ConditionalChrome.tsx` |
| **BreadcrumbNav** | `src/components/BreadcrumbNav.tsx` | 无（从 `usePathname` / `useLocale` 读取） | 粘性面包屑导航条，自动根据当前路由段生成路径映射，含 JSON-LD BreadcrumbList 结构化数据。通过 6 个注册表（TOOLS / SEO / MARKETING / INSIGHTS / GLOSSARY / BLOG）自动填充标签。 | `ConditionalChrome.tsx` |
| **SecondaryCta** | `src/components/SecondaryCta.tsx` | 无（从 `usePathname` 读取） | 页面底部上下文 CTA 区块，根据路由匹配展示不同语言和内容的行动号召。 | `ConditionalChrome.tsx` |

---

## 二、文章渲染 / Article Rendering

内容页面通过 JSON → 组件块的管道渲染。

### 2.1 核心渲染器

| 组件 | 文件 | Props | 说明 | 引用者 |
|------|------|-------|------|--------|
| **ArticleFromJson** | `src/content/render/ArticleFromJson.tsx` | `{ doc: ArticleDocV1; imageUrl?: string; heroContent?: ReactNode }` | JSON 文档 → React 组件的核心调度器。遍历 `doc.blocks`，按 `block.type` 分派到 Tldr / Section / HowItWorks / BestTools / UseCases / HowToChoose / FAQ / References / Table / html 等组件，包裹在 BlogLayout 中。 | 全部内容页：`tools/[slug]`、`seo/[slug]`、`marketing/[slug]`、`insights/[slug]`、`blog/[slug]`、`events/*`、`media-kit` |
| **BlogLayout** | `src/components/BlogLayout.tsx` | `{ children; title; excerpt; author?; publishDate?; modifiedDate?; readTime?; pageUrl?; imageUrl?; locale?; hideHero?; heroContent?; citations?; layout?; tocItems?; coverImage?; faqSection? }` | 文章页面完整壳层：Hero 区块 + 内容主体 + TOC 侧边栏 + 分享侧栏 + FAQ 区块。根据 `locale` 自动推导阅读时间默认值。 | `ArticleFromJson.tsx` |
| **ArticleTOC** | `src/components/ArticleTOC.tsx` | `{ items: TocItem[]; title?: string }` | 粘性目录侧边栏，IntersectionObserver 驱动的高亮追踪。 | `BlogLayout.tsx`、`ArticleFromJson.tsx` |
| **ShareButtons** | `src/components/ShareButtons.tsx` | `{ pageTitle?; pageUrl?; isEnglishPage?; className? }` | Twitter / LinkedIn / Facebook 分享按钮 + 复制链接（含 toast 提示）。 | `BlogLayout.tsx` |
| **ShareRail** | `src/components/ShareRail.tsx` | `{ url: string; title: string }` | 紧凑垂直分享按钮组，用于文章侧栏。 | `BlogLayout.tsx` |

### 2.2 内容块组件（由 ArticleFromJson 调度）

| 组件 | 文件 | Props | 说明 |
|------|------|-------|------|
| **Tldr** | `src/components/Tldr.tsx` | `{ id?; title; introduction?; items: string[]; intro?; skillCta?; variant? }` | TL;DR 核心要点区块，含 ItemList Schema 结构化数据。支持 card 和 border-left 两种样式变体。 |
| **TldrSkillCta** | `src/components/TldrSkillCta.tsx` | `{ skillCta: { skills: string[]; description: string; locale? } }` | 嵌入 Tldr 内部的 npx 命令复制块，用于安装 Claude Skills。动态读取 `skills-catalog.json` 显示数量。 |
| **Section** | `src/components/Section.tsx` | `{ id?; level?; title; paragraphs?; subSections?; className?; showDivider?; contentBodyPreset?; children?; headingStyle? }` | 可复用的标题 + 段落区块，支持子区块和自定义子元素（列表、表格等）。 |
| **HowItWorks** | `src/components/HowItWorks.tsx` | `{ id: string; title: string; technologyBase: string; advantages: Advantage[]; architectureDifferences: string; locale? }` | "工作原理"区块：技术基础 + 优势列表 + 架构差异说明。 |
| **BestTools** | `src/components/BestTools.tsx` | `{ id: string; title: string; introduction: string; tools: Tool[]; locale? }` | 排名的工具卡片列表，含图片、描述、外部链接。 |
| **UseCases** | `src/components/UseCases.tsx` | `{ id?; title; introduction?; useCases: UseCase[]; locale? }` | 使用场景列表，每个场景含 H3 标题和 HTML 描述。 |
| **HowToChoose** | `src/components/HowToChoose.tsx` | `{ id; title; introduction; steps: HowToStep[]; pageUrl? }` | 编号步骤列表，含 HowTo Schema JSON-LD 结构化数据。 |
| **FAQ** | `src/components/FAQ.tsx` | `{ items: FAQItem[]; pageUrl?: string; locale? }` | 手风琴 FAQ 区块，含 FAQ Schema JSON-LD。`<details>/<summary>` 实现（Bing 可爬取），禁止内部链接。 |
| **References** | `src/components/References.tsx` | `{ items: ReferenceItem[]; title?: string; locale?; showDivider?: boolean }` | 编号引用列表，含外部链接和日期解析。 |
| **Table** | `src/components/Table.tsx` | `{ items?; toolType?; toolTypeEn?; columnHeaders?; columns?; data?; children?; caption?; variant? }` | 数据对比表格，支持三种模式：items / columns+data / children。 |
| **HeroSection** | `src/components/HeroSection.tsx` | `{ locale? }` | 首页专用的 Hero 区块，含大标题和副标题。 |

---

## 三、独立页面组件 / Standalone Page Components

不被 ArticleFromJson 调度，由特定页面直接导入的组件。

| 组件 | 文件 | Props | 说明 | 引用者 |
|------|------|-------|------|--------|
| **SkillsTerminal** | `src/components/SkillsTerminal.tsx` | `{ command: string; copyLabel?: string; locale? }` | 可复制的终端命令行块，带 `$` 提示符。 | `app/[locale]/skills/(landing)/page.tsx` |
| **SkillsCategoryGrid** | `src/components/SkillsCategoryGrid.tsx` | `{ catalog: Catalog }` | 可展开的终端风格技能分类树，显示各类别数量。 | `app/[locale]/skills/(landing)/page.tsx` |
| **GlossaryPageContent** | `src/components/GlossaryPageContent.tsx` | `{ data: GlossaryDataJson; locale: string; slug: string }` | 完整术语表页面：搜索过滤 + 粘性分类导航 + 分类区块 + 术语卡片含定义和链接。 | `app/[locale]/glossary/[slug]/page.tsx` |
| **PartnershipPageContent** | `src/components/PartnershipPageContent.tsx` | `{ locale: "en" \| "zh" }` | 合作伙伴页面内容，含精选合作方卡片。 | `app/[locale]/partnership/page.tsx` |
| **CustomerCaseCard** | `src/components/CustomerCaseCard.tsx` | `{ name: string; logo: string; description: string; website?: string; locale? }` | 客户案例卡片：Logo（含首字母回退）+ 名称 + 描述 + 可选网站链接。 | `GrowthCaseStudiesIndex.tsx` |
| **CustomerStoriesHeroLogos** | `src/components/CustomerStoriesHeroLogos.tsx` | 无 | 3×2 灰度客户 Logo 网格，用于 Hero 区块。 | `app/[locale]/customer-stories/page.tsx` |
| **GrowthCaseStudiesIndex** | `src/marketing/GrowthCaseStudiesIndex.tsx` | `{ locale: "zh" \| "en" }` | 23 个增长案例研究表格 + 2 个平台链接。 | `app/[locale]/marketing/growth-case-studies/page.tsx` |
| **PromoCode** | `src/components/PromoCode.tsx` | `{ code: string; label?: string; locale?: string }` | 可展开的推广码，含复制到剪贴板功能。根据 `locale` 显示中/英文按钮标签。 | `app/[locale]/betalist/page.tsx` |
| **YouTubeThumbnail** | `src/components/YouTubeThumbnail.tsx` | `{ videoId: string; videoUrl: string; title?: string; className?: string }` | 可点击的 YouTube 缩略图，3 级图片回退（maxresdefault → hqdefault → default），含播放按钮覆盖层。 | `app/[locale]/insights/indie-hackers/page.tsx` |
| **YouTubeThumbnailImage** | `src/components/YouTubeThumbnailImage.tsx` | `{ imageSrc: string; imageAlt: string; youtubeUrl?: string }` | 通用图片组件，支持静态图和 YouTube 缩略图回退，可选链接到 YouTube。 | `BestTools.tsx` |
| **CookieConsent** | `src/components/CookieConsent.tsx` | 无（从 `usePathname` 读取） | GDPR Cookie 同意横幅，含接受/拒绝按钮，写入 cookie 并推送到 GTM dataLayer。 | `app/[locale]/layout.tsx` |
| **TrustedBySection** | `src/components/TrustedBySection.tsx` | 无 | 水平滚动客户 Logo 走马灯，渐变边缘淡出效果。 | `app/[locale]/page.tsx` |

---

## 四、首页章节 / Homepage Chapters

首页的 5 个叙事章节，每个渲染为全宽双栏区块（图片 + 文字）。

全部位于 `src/components/chapters/`，Props 统一为 `{ locale?: "zh" | "en" }`，由 `app/[locale]/page.tsx` 引用。

| 组件 | 文件 | 内容主题 |
|------|------|----------|
| **Chapter01Problem** | `chapters/Chapter01Problem.tsx` | "大多数 AI 初创死于沉默" — 问题陈述 |
| **Chapter02Shift** | `chapters/Chapter02Shift.tsx` | "发现行为已经转移到了答案内部" — 趋势转变 |
| **Chapter03Levers** | `chapters/Chapter03Levers.tsx` | "三个杠杆，一套打法" — 方法论（编号列表 + 粘性图片） |
| **Chapter04Receipts** | `chapters/Chapter04Receipts.tsx` | "数据会自我叠加" — 数据网格 + CTA |
| **Chapter05Promise** | `chapters/Chapter05Promise.tsx` | 结尾宣言 — 纸纹网格背景 |

---

## 五、分析与追踪 / Analytics & Tracking

| 组件 | 文件 | Props | 说明 | 引用者 |
|------|------|-------|------|--------|
| **GoogleTagManager** | `src/components/GoogleTagManager.tsx` | 无（读取 `NEXT_PUBLIC_GTM_ID`） | 加载 GTM `<Script>` + `<noscript>` 回退。导出三个具名导出：`GoogleTagManagerScript`、`GoogleTagManagerNoscript`、默认导出。 | `app/layout.tsx` |
| **PageViewTracker** | `src/components/PageViewTracker.tsx` | 无 | 客户端路由切换时向 GTM dataLayer 推送 `virtual_pageview` 事件。 | `app/[locale]/layout.tsx` |

---

## 六、UI 基础组件 / UI Primitives

全部位于 `src/components/ui/`，基于 shadcn/ui（Radix + Tailwind）再导出。Props 为标准 React HTML 属性 + shadcn variant 属性。

| 组件 | 文件 | 说明 |
|------|------|------|
| **Button** | `ui/button.tsx` | 按钮，variants: default / destructive / outline / secondary / ghost / link，sizes: default / sm / lg / icon |
| **Badge** | `ui/badge.tsx` | 标签，variants: default / secondary / destructive / outline |
| **Breadcrumb** | `ui/breadcrumb.tsx` | 面包屑构件：Breadcrumb / BreadcrumbList / BreadcrumbItem / BreadcrumbLink / BreadcrumbPage / BreadcrumbSeparator / BreadcrumbEllipsis |
| **Card** | `ui/card.tsx` | 卡片容器：Card / CardHeader / CardTitle / CardDescription / CardContent / CardFooter |
| **Input** | `ui/input.tsx` | 输入框，转发原生 HTML input 属性 |
| **Separator** | `ui/separator.tsx` | 分隔线（Radix），支持 horizontal / vertical |
| **Sonner** | `ui/sonner.tsx` | Toast 通知容器（sonner 库），含主题化 Toaster + toast 导出 |
| **Tooltip** | `ui/tooltip.tsx` | 工具提示（Radix）：TooltipProvider / Tooltip / TooltipTrigger / TooltipContent |

---

## 七、内容渲染工具 / Content Rendering Utilities

非组件函数，用于 JSON 内容的辅助处理。

| 文件 | 导出 | 说明 | 引用者 |
|------|------|------|--------|
| `src/content/render/ArticleToMarkdown.ts` | `articleToMarkdown(doc, locale)` | 将 ArticleDocV1 JSON 转换为 Markdown 字符串（用于 SEO 知识块提取） | `scripts/permanent/` |
| `src/content/render/htmlToMarkdown.ts` | `htmlToMarkdown(html)` | 将 ArticleDocV1 的 HTML 块转换为 Markdown | `ArticleToMarkdown.ts` |
| `src/content/types/article-doc.ts` | `ArticleDocV1` 接口 | 文章 JSON 文档的类型定义 | 全局 |

---

## 八、统计 / Stats

| 类别 | 数量 | 活跃 | 未使用（已删除） |
|------|------|------|------------------|
| 页面壳层 | 6 | 6 | — |
| 文章渲染 | 11 | 11 | — |
| 独立页面组件 | 11 | 11 | — |
| 首页章节 | 5 | 5 | — |
| 分析/追踪 | 2 | 2 | — |
| UI 基础 | 8 | 8 | — |
| 渲染工具 | 2 + 1 类型 | 3 | — |
| **合计** | **46** | **46** | GlossaryViewer（251 行）、CustomerStoriesIndex |
