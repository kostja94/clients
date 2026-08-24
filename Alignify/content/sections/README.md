# Section 章节规范文档

本目录存放**跨页面通用**的内容块规范。Section 定义格式、字数、禁止项，**不区分**页面类型（Tools/SEO/Marketing）。

- **页面类型**：见 [templates](../templates/README.md)
- **项目总索引**：见 [README.md](../../README.md)

## 部署组件清单（2026-08-23）

> 来源：部署仓 `E:\自有部署项目\alignify production\src/components\`（28 个 `.tsx`）

### 一、文章渲染相关

| 组件 | 职责 | 数据源 |
|------|------|--------|
| `ArticleFromJson.tsx` | 调度 block 渲染 | `getMarkdownDoc()` → 内部 `ArticleDocV1` |
| `Section.tsx` | H2/H3 + 段落 + subSections | md `<!-- block:section -->` |
| `Tldr.tsx` | 核心要点 | `src/data/tldr-data.json`（按 `pageUrl`） |
| `FAQ.tsx` | 常见问题 | `src/data/faq-data.json`（全局 ConditionalChrome） |
| `References.tsx` | 参考文献 | `src/data/references-data.json` |
| `BlogLayout.tsx` | 文章壳层、Hero、Schema | frontmatter → `blogLayout` |
| `ArticleTOC.tsx` | 侧边栏目录 | 从 blocks 提取 H2/H3 |

**运行时 block 类型**（`ArticleBlock`）：`section` | `html` | `tldr`/`faq`/`references`（md 中 residual，渲染时 skip，改从集中 JSON 注入）。

> **已删除组件**（旧 JSON 体系）：`HowItWorks.tsx`、`BestTools.tsx`、`HowToChoose.tsx`、`UseCases.tsx` — 对应章节现为 Markdown `section` 正文。

### 二、布局壳层

`ConditionalChrome` · `Header` · `Footer` · `BreadcrumbNav` · `TopBanner` · `SecondaryCta` · `ShareButtons` · `ShareRail`

### 三、首页 / 其他

`HeroSection` · `Chapter01–05` · `GlossaryPageContent` · `SkillsTerminal` · UI 组件（`button`/`card`/…）

---

## 内容格式 SSOT

| 类型 | 路径 | 说明 |
|------|------|------|
| 正文 | `content/{blog,tools,seo,marketing,insights,events}/{locale}/{slug}.md` | YAML frontmatter + block 标记 |
| TL;DR / FAQ / References | `src/data/*-data.json` | 键 = 完整 `pageUrl` |
| Meta | `src/data/*-meta.ts` | SEO title/description + ISO 日期 |
| 遗留 JSON | `content/glossary/`、`content/media-kit/` | 8 文件 |

---

## 组件 → Section 文档索引

| 章节 | Section 文档 |
|------|-------------|
| TL;DR | [section-tldr.md](./section-tldr.md) |
| 通用 section | [section-generic.md](./section-generic.md) |
| Best 榜单（正文） | [section-best-tools.md](./section-best-tools.md) |
| 如何选择（正文） | [section-how-to.md](./section-how-to.md) |
| FAQ | [section-faq.md](./section-faq.md) |
| References | [section-references.md](./section-references.md) |
| 对比表 | [section-comparison-table.md](./section-comparison-table.md) |
| Hero | [section-hero.md](./section-hero.md) |

**编辑顺序**：先查 template → 再查 section → **以部署仓源码为准**。
