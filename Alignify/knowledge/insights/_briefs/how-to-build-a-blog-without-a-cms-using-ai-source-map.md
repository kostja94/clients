## Source Map — how-to-build-a-blog-without-a-cms-using-ai

> **内部交付物**（不发布）。与部署仓 References JSON 对齐；Draft 新增 claim 须补行。  
> **Checked as-of**: 2026-08-27  
> **正文**: `content/blog/{zh,en}/how-to-build-a-blog-without-a-cms-using-ai.md`

| Claim | Section / ¶ | Source URL | Checked | Confidence |
|-------|---------------|------------|---------|:----------:|
| Content as Code：内容/meta/导航以 Git 源文件为真相源，构建生成站点 | `#what-is-content-as-code` | https://leerob.com/agents | 2026-08-27 | High |
| Lee Robinson *Content is just code*；Agent 改内容应同改代码 | `#what-is-content-as-code` | https://leerob.com/agents | 2026-08-27 | High |
| Cursor 曾用 Sanity 等 Headless CMS，2026 迁回 Markdown + 同仓代码 | 大企业案例 · Cursor 行 | https://leerob.com/agents | 2026-08-27 | High |
| Sanity 2026 回应「删 CMS」：*You should never build a CMS* | Sanity 专章 | https://www.sanity.io/blog/you-should-never-build-a-cms | 2026-08-27 | High |
| Sanity 主张 MCP Server 接 CMS | Sanity 专章 | https://www.sanity.io/blog/you-should-never-build-a-cms | 2026-08-27 | High |
| Next.js SSG build 阶段编译 Markdown，无运行时 CMS DB | `#what-ai-replaces` | https://nextjs.org/docs/app/building-your-application/routing | 2026-08-27 | High |
| 可选 Git-based CMS：Tina、Decap 以 Git 为真相源 | `#what-ai-replaces` | https://tina.io/docs/ · https://decapcms.org/docs/intro/ | 2026-08-27 | Medium |
| Strand / seite / Glint：MDX/Markdown in Git + MCP/Agent | 大企业案例 · OSS 行 | https://github.com/strand-dev · https://seite.app · https://github.com/glint-dev/glint | 2026-08-27 | Medium |
| GitCMS / Postlark：Git 真相源 + 可选 UI/MCP | 大企业案例 · GitCMS 行 | https://gitcms.io · https://postlark.com | 2026-08-27 | Medium |
| Alignify 四阶段演进 | `#alignify-evolution` | 作者一手 + `alignify-by-kostja` 可验证 | 2026-08-27 | High |
| Vercel Preview + merge deploy | `#how-to-build-workflow` | https://vercel.com/docs/deployments/preview-deployments | 2026-08-27 | High |
| generateMetadata + sitemap 常见博客 spec | `#how-to-build-workflow` | https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps | 2026-08-27 | High |

### EEAT 速查（E1–E6）

| # | Pass | 证据 |
|---|------|------|
| E1 | ✅ | 上表 High/Medium；References JSON 2 条 A/B 类 |
| E2 | ✅ | Cursor/Sanity 链官方或一手博客 |
| E3 | ✅ | as-of 2026-08-27 |
| E4 | ✅ | 无 unsupported 绝对化；选型矩阵保留反例 |
| E5 | ✅ | 定性为主 |
| E6 | ✅ | Sanity/Headless 列为诚实反例 |

### References JSON 对齐（仅 A/B 类上站）

| References 条目 | Source Map 行 |
|-----------------|---------------|
| Lee Robinson — Coding Agents & Complexity Budgets | Content as Code + Cursor 行 |
| Sanity — You should never build a CMS | Sanity 专章两行 |
