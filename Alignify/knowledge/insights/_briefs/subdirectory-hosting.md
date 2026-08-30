## Article Brief — subdirectory-hosting

**QualityTier**: flagship
**ArticleType**: insights-analysis
**InvestmentScore**: 4.5 — path-based composition 科普 + 与 Content-as-Code 姊妹篇 + Alignify 一手案例
**Gate A**: KEEP

**SSOT**: `E:\个人知识库\氛围编码-Vibe-Coding\同域子目录发布-Subdirectory-Hosting.md`

**User confirmed**（2026-08-27）:
- 中文主称：**主域名下的分块建站**
- 文体：原理 · 科普 · 案例；落地细节**压缩进本文**（表/prose），**禁止**正文预告未发布 skills（E49）
- Customer Stories **不详细写**，代过即可
- Alignify 案例 **仅一个页面**：`/audit-website-by-lovable`（Lovable iframe 嵌入），**不是**整站 subdirectory 模式
- skills 引用：**等 skills 发布后再加内链**（正文零提及）
- Author POV：**是** — 判断**融入**案例/坑/分工节；**`#author-take` 独立 H2：省略**
- go/no-go 矩阵：**省略**（选型已在「子目录 vs 子域名」等节表达；E50）
- publishDate：**2026-09-02**（与 how-to-build 对调）
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
2. 与 Content-as-Code 姊妹篇分工表
3. Alignify 仅 Lovable iframe 页一手边界（非整站 subdirectory）
4. 概念级坑清单（无长代码；**写进本文**，不 defer）

**Answer Blocks**（内容问题 → H2）:
1. `#not-a-new-blog-only-idea` — 并非 Blog 专属
2. `#what-is-subdirectory-hosting` — 定义与机制
3. `#vs-content-as-code` — 与姊妹篇分工
4. `#subdirectory-vs-subdomain` — SEO 选型
5. `#who-maintains-what` — 组织 RACI
6. `#cases-and-alignify` — 公开复盘 + Alignify 边界（含 Author POV 判断）
7. `#production-pitfalls` — 坑与概念验收（表 + ≥3 句 BLUF）

**Planned H2 architecture**:
| H2 | 采用 | 备注 |
|----|------|------|
| 并非新事 / 定义 / 分工 / 子目录vs子域 / 典型路径 / 谁维护 / 案例 / 坑清单 | ✅ | 从 SSOT 推导 |
| `#should-you-do-this` go/no-go | ❌ | 选型已在 §子目录vs子域 |
| `#author-take` | ❌ | POV 融入案例+坑节 |
| References | ❌ | |
| TL;DR / FAQ | ✅ | 7 问 |

**Author POV**（融入式，非独立 H2）:
1. 能单仓就不要 proxy；Alignify 主体单应用是因 Agent 维护成本
2. iframe 页不是整站 subdirectory 教科书

**Optional sections**: TL;DR ✅ · FAQ ✅ 7 · How To ❌ · References ❌ · `#author-take` ❌ · go/no-go ❌ · Skills 正文预告 ❌

**Final CTA**:
- ZH title: 产品站与内容仓要同域呈现，先对齐 Rewrite 再拆仓。
- ZH description: 多部署、单 hostname——我帮你判断子目录值不值得，以及与 Content-as-Code 怎么衔接。
- EN: Same-domain publishing with separate deploys—align rewrites before you split repos.

**Internal links**:
- → `/blog/how-to-build-a-blog-without-a-cms-using-ai`
- ← 上篇适当段落回链本篇

**OG**: accent mars-green · HERO = 单 hostname 多 origin 路径分流示意

**Revision note**（2026-08-27）: 对齐 skills v1.2 — E49/E50；删模板收束节；skills 仅发布后内链
