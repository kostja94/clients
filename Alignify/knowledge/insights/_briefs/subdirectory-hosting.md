## Article Brief — subdirectory-hosting

**QualityTier**: flagship
**ArticleType**: insights-analysis
**InvestmentScore**: 4.5 — path-based composition 科普 + 与 Content-as-Code 姊妹篇 + Alignify 一手案例
**Gate A**: KEEP

**SSOT**: `E:\个人知识库\Vibe Coding\Subdirectory-Hosting-同域子目录发布.md`

**User confirmed**（2026-08-27）:
- 中文主称：**主域名下的分块建站**
- 文体：原理 · 科普 · 案例；落地细节一带而过（后续单独 skills）
- Customer Stories **不详细写**，代过即可
- Alignify 案例 **仅一个页面**：`/audit-website-by-lovable`（Lovable iframe 嵌入），**不是**整站 subdirectory 模式
- skills 引用：**等 skills 发布后再加**
- Author POV：**是**（Kostja 第一人称）
- publishDate：**往前移** → 2026-09-02（与 how-to-build 对调，how-to-build → 2026-09-03）
- 内链：**双向**与 `how-to-build-a-blog-without-a-cms-using-ai`
- References：**不需要**
- OG：**需要** EN/ZH

**Primary keyword**（ZH）: 主域名下的分块建站 · 同域子目录发布 · subdirectory hosting
**Primary keyword**（EN）: subdirectory hosting · same-domain publishing · path-based composition
**Search intent**: Definition + Architecture + Decision
**Target reader**: 产品站与博客/文档分仓的 founder、工程负责人、SEO 选型者
**Hub / category**: coding-dev · tools `/tools` Hub · dev-coding 分组

**One-line thesis**:
一个域名、多套独立部署——用 **Rewrite（透明反向代理）** 把 `/blog`、`/docs` 等子路径拼回同一 hostname，而不是 301 跳到 `*.vercel.app` 或子域。

**Moat Asset**:
1. 与 blog 优先叙事脱钩——WordPress 时代就有 `/blog` 心智
2. 与 [Content-as-Code 姊妹篇](/blog/how-to-build-a-blog-without-a-cms-using-ai) 分工表
3. Alignify 仅 Lovable iframe 页一手边界（非整站 subdirectory）
4. 概念级坑清单（无长代码）

**Answer Blocks**（major H2）:
1. `#what-is-subdirectory-hosting` — 定义与机制
2. `#vs-content-as-code` — 多部署粘合 vs 内容仓
3. `#subdirectory-vs-subdomain` — SEO 决策（深链 SEO 文）
4. `#who-maintains-what` — 工程 vs 市场分工
5. `#should-you-do-this` — 适合谁 go/no-go

**Planned H2 architecture**:
| H2 | 必选 | 呈现 |
|----|------|------|
| 并非新事 | ✅ | prose |
| 主域名下的分块建站是什么 | ✅ | BLUF + 表 + prose |
| 与 Content-as-Code 分工 | ✅ | 表 + 双向内链 |
| 子目录 vs 子域名 | ✅ | 决策表 + 链 SEO 文 |
| 典型路径 | ✅ | 表 |
| 谁维护什么 | ✅ | 表 + prose |
| 案例 | ✅ | Customer Stories 一笔带过；Alignify iframe 页 |
| 概念级坑清单 | ✅ | 表，无长代码 |
| 适合谁 | ✅ | go/no-go |
| 结论 | ✅ | prose |

**publishDate**: 2026-09-02

**Author POV**: Kostja 第一人称
**Voice**: 原理科普 + 一手判断

**Optional sections**: TL;DR ✅ · FAQ ✅ 7 · How To ❌ · References ❌

**Final CTA**:
- ZH title: 产品站与内容仓要同域呈现，先对齐 Rewrite 再拆仓。
- ZH description: 多部署、单 hostname——我帮你判断子目录值不值得，以及与 Content-as-Code 怎么衔接。
- EN: Same-domain publishing with separate deploys—align rewrites before you split repos.

**Internal links**:
- → `/blog/how-to-build-a-blog-without-a-cms-using-ai`
- ← 上篇适当段落回链本篇

**OG**: accent mars-green · HERO = 单 hostname 多 origin 路径分流示意
