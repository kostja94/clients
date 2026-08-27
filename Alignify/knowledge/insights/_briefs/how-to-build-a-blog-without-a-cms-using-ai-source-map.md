## Source Map — how-to-build-a-blog-without-a-cms-using-ai

> **内部交付物**（不发布）。与部署仓 References JSON 对齐；Draft 新增 claim 须补行。  
> **Checked as-of**: 2026-08-27  
> **正文**: `content/blog/{zh,en}/how-to-build-a-blog-without-a-cms-using-ai.md`

| Claim | Section / ¶ | Source URL | Checked | Confidence |
|-------|---------------|------------|---------|:----------:|
| Cursor 曾用 Sanity 等 Headless CMS，2026 迁回 Markdown + 同仓代码 | 大企业案例 · Cursor 行 | https://leerob.com/agents | 2026-08-27 | High |
| Lee Robinson 公开表述 *Content is just code*；CMS 抽象阻碍 Agent 直接改站 | 大企业案例 · Cursor 行 | https://leerob.com/agents | 2026-08-27 | High |
| Sping 从 WordPress/Umbraco 类 CMS 转向 Astro + Claude skill 工作流 | 大企业案例 · Sping 行 | https://sping.nl/en/insights/from-cms-to-ai-agent/ | 2026-08-27 | High |
| Sanity 2026 回应「删 CMS」趋势：*You should never build a CMS* 及后续讨论 | Sanity 专章 | https://www.sanity.io/blog/you-should-never-build-a-cms | 2026-08-27 | High |
| Sanity 主张 Agent 应通过 MCP Server 接 CMS，而非全员搬回 Git | Sanity 专章 | https://www.sanity.io/blog/you-should-never-build-a-cms | 2026-08-27 | High |
| Markdown + SSG 在 build 阶段编译 HTML，无运行时查 CMS 数据库 | AI 替你做三件事 · 内容层段 | https://staticsignal.io/posts/markdown-driven-content-how-to-build-a-blog-without-a-cms/ | 2026-08-27 | High |
| 可选 Git-based CMS 层：Tina、Decap 仍以 Git 为真相源 | AI 替你做三件事 · 内容层段 | https://tina.io/docs/ · https://decapcms.org/docs/intro/ | 2026-08-27 | Medium |
| Strand / seite / Glint 等栈：MDX/Markdown in Git + MCP/Agent 工具 | 大企业案例 · OSS 行 | https://github.com/strand-dev · https://seite.app · https://github.com/glint-dev/glint | 2026-08-27 | Medium |
| GitCMS / Postlark：Git 真相源 + 可选编辑 UI 或 MCP | 大企业案例 · GitCMS 行 | https://gitcms.io · https://postlark.com | 2026-08-27 | Medium |
| 从业者 Slogan *Git is the CMS. AI is the admin.*（行业口语概括，非单一官方文档） | 开篇 · 零经验段 | 多源社区讨论；Alignify SSOT `Content-as-Code-代码库即内容库.md` | 2026-08-27 | Medium |
| Alignify 四阶段演进（WordPress → Lovable → JSON 字段 → Markdown+Git+Skills） | Alignify 实践 | 作者一手实践 + 部署仓 `alignify-by-kostja` 可验证 | 2026-08-27 | High |
| Vercel Preview 给 PR 预览链接；merge 触发 CI deploy | 协作流程 · Step 4 | https://vercel.com/docs/deployments/preview-deployments | 2026-08-27 | High |
| Next.js App Router + generateMetadata + sitemap 为常见博客骨架 spec | 协作流程 · Step 2 | https://nextjs.org/docs/app/building-your-application/routing · https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps | 2026-08-27 | High |

### EEAT 速查（E1–E6）

| # | Pass | 证据 |
|---|------|------|
| E1 | ✅ | 上表 High/Medium 行；References JSON 4 条 A/B 类 |
| E2 | ✅ | Cursor/Sping/Sanity 均链官方或一手博客 |
| E3 | ✅ | as-of 2026-08-27；Cursor/Sanity 叙事标注 2026 |
| E4 | ✅ | 无 unsupported「最好/唯一」；选型段保留 WordPress/Sanity 适用场景 |
| E5 | ✅ | 无 ROI/准确率硬数字；定性为主 |
| E6 | ✅ | 非 Tools 对比文；「应保留 Headless CMS + MCP」为诚实反例 |

### References JSON 对齐（仅 A/B 类上站）

| References 条目 | Source Map 行 |
|-----------------|---------------|
| Lee Robinson — Coding Agents & Complexity Budgets | Cursor 迁移两行 |
| Sanity — You should never build a CMS | Sanity 专章两行 |
| Sping — From CMS to AI agent | Sping 行 |
| Static Signal — Markdown-Driven Content | SSG 无运行时 DB 行 |
