# Alignify 页面模板 (Templates)

本目录存放**按页面类型复用的模板**：章节顺序、引用哪些 section、**本类型特有规则**、检查清单。

**职责**：Templates 定义「如何组装内容型页面」，Section 定义「每块内容怎么写」。各 template 引用 [sections](../sections/README.md)，并补充本类型特有规则。

**项目总索引**：参见 [README.md](../../README.md)。

---

## 创建与翻译入口

| 场景 | 入口文档 |
|------|----------|
| **创建中文内容** | [template-tools](./template-tools.md)（Tools）或对应 template |
| **翻译为英文** | [template-tools](./template-tools.md) §十四 翻译原则 + 对应 template |

**中英流程**（详见 [content-rules](../../.cursor/rules/content-rules.mdc) §四）：
- **先中文**：新增内容时仅创建中文版，不提前创建英文
- **后英文**：中文创建完毕之后一次性批量优化英文页面
- **非逐句对应**：英文页面不与中文完全一致；如 Tools 页可针对具体工具做本地化优化（示例、定价、地区适用性等）

**一致性**：同类型页面之间、章节之间、章节内组成之间，字数与表达需高度一致。详见 [section-consistency](../section/section-consistency.md)，各 template 均含「〇、一致性规范」小节。

**流程**：1. 查阅 [section-content-import](../section/section-content-import.md) 了解统一导入模式 → 2. 查阅对应 template 了解章节顺序与一致性规范 → 3. 查阅 section 了解各章节格式 → 4. 参阅 [section-seo](../section/section-seo.md) 了解 Meta、Date、Alt

**JSON 正文内链**（`content/seo`、`content/tools`）：见 [alignify-internal-links.md](../alignify-internal-links.md)。

**新增页面步骤**：
- **Tools**：更新 `tools-pages-config`、sitemap、`zh/tools`；创建 JSON、page.tsx（BreadcrumbNav 自动从 TOOLS_PAGES 派生标签，无需手动同步）
- **SEO/Marketing**：更新 `site-pages-config`、sitemap、索引页；创建 JSON、page.tsx

---

## 模板列表

| 文件 | 适用场景 | 说明 |
|------|----------|------|
| [template-bloglayout.md](./template-bloglayout.md) | 通用 | BlogLayout 使用规范、PageLayout、TopBanner |
| [template-landing.md](./template-landing.md) | 首页 | HeroSection、TrustedBySection、ContentValueSection |
| [template-tools.md](./template-tools.md) | Tools 类页面 | AI 图片工具、视频工具、招聘工具等工具推荐、产品对比、排名列举 |
| [template-seo.md](./template-seo.md) | SEO 类页面 | Schema、链接建设、SearchEngine、StatCounterEmbed 等 |
| [template-skills.md](./template-skills.md) | Agent Skills 规范页 | Sitemap 等供 AI Agent 使用的规范文档，MD + readFileSync 渲染 |
| [template-marketing.md](./template-marketing.md) | Marketing 类页面 | 联盟营销、红人营销、创作者计划、Lifetime Deal、GEO、Reddit 营销等策略指南 |
| [template-aggregate.md](./template-aggregate.md) | 聚合页面 | /blog、/explore、/tools、/seo、/marketing 等索引页面 |
| [template-glossary.md](./template-glossary.md) | Glossary 页面 | GlossaryViewer、GlossaryPageContent |

---

## 使用说明

1. **创建内容型页面**：先查阅对应 template 了解章节顺序、本类型特有规则
2. **中英流程**：先完成中文，再一次性批量优化英文；英文可不与中文逐句对应（如 Tools 本地化）
3. **翻译为英文**：参见 [template-tools](./template-tools.md) 第十四节「翻译为英文」
4. **创建 Agent Skills 规范页**：参见 [template-skills](./template-skills.md)（如 Sitemap 规范）
5. **查 section**：各章节的格式、字数见 `content/sections/` 对应文档
6. **优化现有页面**：对照 template 的质量检查清单
