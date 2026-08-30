# MeDo Blog 迁移计划：Ghost → Content-as-Code + 子目录反向代理

> **目标**：用 **Markdown in Git + Next.js SSG** 替换 Ghost；博客独立部署，经主域 **Rewrite** 挂回 `https://medo.dev/blog/*`；正文质量对齐 `medo/blog/` 现稿标准。

**Last updated**: 2026-08-28  
**状态**：计划阶段（Phase 0）

---

## 附录 A：术语与架构（自包含）

### A.1 Content-as-Code（代码库即内容库）

- 文章、页面 meta、导航以 **可版本化源文件**（Markdown + YAML front matter）存放在 Git 仓库。
- 构建阶段（SSG）将 Markdown 编译为 HTML，推送 CDN；**无运行时查 CMS 数据库**。
- Agent / 工程通过改 `.md` 与页面组件维护整站，人审 PR 后 merge 发布。
- 口号：**Git is the CMS. AI is the admin.**

### A.2 子目录反向代理（path-based composition）

当 **产品主站** 与 **博客** 物理拆成两个 deployment，仍要同域呈现 `example.com/blog/*` 时：

| 机制 | 说明 |
|------|------|
| **Rewrite** | 主站 Edge 向博客源站取 HTML，以主域路径返回；**地址栏不变** |
| **非 Redirect** | 不用 301/302 跳到部署平台子域，避免 SEO 与品牌分裂 |
| **SITE_URL** | 博客 env 设 `https://medo.dev`；canonical、og:url、sitemap 均指向主域路径 |
| **静态资源** | 双 Next 部署时不能无脑转发全部 `/_next/*`；需精确 chunk 规则或子站 `assetPrefix: '/blog'` |

**单仓单应用** 时 `/blog` 只是 App 内路由，**不需要**反向代理。当前主站 SPA + Ghost 分体 → 默认 **拆仓 + Rewrite**。

### A.3 目标 frontmatter（摘要）

```yaml
---
title: "..."
description: "..."
slug: "..."              # 常青 URL，不含年份
date: YYYY-MM-DD         # 发布时间，永不改
updated: YYYY-MM-DD      # 可选，仅实质更新
author: "Kostja"
category: Tutorial | Guide | Case Study | Product
secondary_category: Mobile App | Components | AI Frontend Design | Full-stack App
---
```

正文规范摘要：H2 英文编号 `## 1.` …；`## TL;DR`（3–5 bullet）；`## Conclusion`、`## Frequently asked questions` 无序号；FAQ 固定 6 题；站内链 `/blog/{slug}`；站外链 `<a rel="nofollow noopener">`；**不设** `## Related articles`。

### A.4 发布 Gate 摘要（G1–G7 + A1–A4）

| Gate | 要点 |
|------|------|
| G1 | 产品能力、Credits 与现网一致 |
| G2 | 内链无 404；路径在白名单内 |
| G3 | 数字有来源或 `as of {date}` |
| G4 | 竞品 GA/Beta 状态正确 |
| G5 | 禁夸大（唯一、保证过审等） |
| G6 | 不链未上线路径（`/pricing`、`/vs/*` 等） |
| G7 | 对比文客观，上架政策有官方链 |
| A1 | 移动输出类型分类正确（native vs wrapper） |
| A2 | App Store 政策 claim 带 `as of {month} {year}` |
| A3 | 对比文含竞品优势 +「何时选竞品」 |
| A4 | H1 不抢工具页 P0 词 |

完整规则见 `medo/skills/medo-blog-article/references/project-config.md`。

### A.5 可链接 URL 白名单

| 类型 | 路径 |
|------|------|
| 博客 | `/blog/{slug}` |
| 移动构建 | `/ai-mobile-app-builder` |
| 组件 | `/components` |
| 功能 | `/features` |
| 首页 | `/` |

---

## 一、背景与约束

### 1.1 为什么要迁

| Ghost 痛点 | Content-as-Code 收益 |
|-----------|---------------------|
| 内容与主站 SPA 割裂；Agent 无法 grep/refactor | 正文、模板、OG、内链规则同仓版本化 |
| 本地 22 篇稿无法部署（slug 404） | `medo/blog/*.md` 可直接成为真相源 |
| Ghost 模板页（54 pages）与 posts 双体系 | 统一 frontmatter + 构建脚本生成列表/JSON-LD |
| 图片与 Ghost CDN 绑定 | 迁移至博客仓 `public/blog/images/` |

### 1.2 架构（已选型）

```
┌─────────────────────────────────────────────────────────┐
│  medo.dev（主站 deployment — 产品 SPA / 营销壳）           │
│  rewrites: /blog/* → ${BLOG_ORIGIN}/blog/*               │
└──────────────────────────┬──────────────────────────────┘
                           │ Rewrite（地址栏不变）
                           ▼
┌─────────────────────────────────────────────────────────┐
│  博客 deployment（独立仓库）                               │
│  Next.js App Router · content/blog/*.md · SSG           │
│  SITE_URL=https://medo.dev                               │
└─────────────────────────────────────────────────────────┘
```

环境变量占位（脱敏）：

| 变量 | 说明 |
|------|------|
| `BLOG_ORIGIN` | 博客 deployment 源站 origin（不含路径） |
| `SITE_URL` | `https://medo.dev` |
| `GHOST_CONTENT_API_KEY` | 只读，存 secrets，**不得写入本仓库** |

### 1.3 非目标

- 主站 `/apps/*` 广场 SSR 改造
- Ghost Admin 保留为编辑 UI（MVP 后可选 Git-based CMS 可视化层）
- Blog 双语（现规范为英文正文）

---

## 二、内容资产分类

| 类型 | 数量（初盘） | 示例 | 迁移策略 |
|------|-------------|------|----------|
| **A. editorial posts** | 17 | `build-an-app-without-coding-in-2026-...` | 导出 MD → 映射/合并/301 → 提质 |
| **B. video posts** | 9 | `/blog/video/...` | 保留 URL 或 301 + 短文 landing；`VideoObject` schema |
| **C. template pages** | ~50 | `*-template/` | **不迁入** MD 库；410/301 或下线 |
| **D. system pages** | 若干 | `/blog/`, `/blog/video/`, `/blog/about/` | 新仓重建；about 合并或 301 |
| **E. local-only** | 22 | `how-to-build-mobile-app-with-ai` 等 | **优先发布** — 已达目标标准 |

完整 URL 见 [reports/ghost-url-inventory.md](./reports/ghost-url-inventory.md)。

---

## 三、阶段计划

### Phase 0 — 发现与 URL 全量盘点 ✅ 进行中

**目标**：可执行的 **URL 主表**（slug、类型、HTTP 状态、canonical、入链、处置决策）。

| 任务 | 方法 | 交付物 |
|------|------|--------|
| 0.1 抓取 Ghost sitemap | `sitemap-posts.xml` + `sitemap-pages.xml` | `reports/ghost-url-inventory.md` |
| 0.2 补全 meta | title、description、published_at、feature_image、内链 | `reports/ghost-url-inventory.json` |
| 0.3 Ghost Content API | 凭据从 secrets 读取；导出 posts + pages JSON | `exports/ghost-raw/`（**gitignore**） |
| 0.4 GSC 已索引 URL | 已收录 blog URL 优先保 slug | `reports/gsc-indexed-blog-urls.csv` |
| 0.5 内外链图 | 爬取 `<a href>` + 对照 `medo/blog/blog-structure-internal-links.md` | `reports/link-graph.json` |
| 0.6 Slug 映射表 | Ghost slug ↔ 本地 slug ↔ 目标 slug ↔ 301 | `reports/slug-mapping.csv` |

**验收**：覆盖 100% sitemap URL；每条有 `action`: `keep` | `301` | `merge` | `retire` | `rewrite`。

---

### Phase 1 — 内容与资源导出

**目标**：正文、frontmatter、内链、图片、embed **可离线重建**。

#### 1.1 正文 → Markdown

| 字段 | Ghost 来源 | 目标 |
|------|-----------|------|
| title | `title` | `title` |
| description | `custom_excerpt` / meta | `description` |
| slug | `slug` | 常青 slug；去 `-2` 等 artifact |
| date | `published_at` | `date` |
| updated | `updated_at` | `updated`（仅实质更新） |
| author | `authors[0].name` | `author` |
| category | 人工映射 | 见附录 A.3 |
| secondary_category | 人工映射 | 见附录 A.3 |

**工具**：Ghost Content API + 自写 `blog-migration/scripts/export-ghost-to-md.py`（推荐）；或通用 Ghost→MD 转换器 + frontmatter 后处理。

**正文清洗**：
- Ghost card → 标准 MD；复杂表格可保留 HTML
- 站内链 → `/blog/{slug}` 相对路径
- 站外链 → `rel="nofollow noopener"`
- 移除 Ghost shortcode / 空 anchor

#### 1.2 图片与静态资源

| 步骤 | 说明 |
|------|------|
| 枚举 | `feature_image` + 正文 `<img>` + sitemap `image:loc` |
| 下载 | 脚本批量拉取 Ghost CDN 全量 |
| 入库 | `public/blog/images/{slug}/` |
| 改写 URL | MD 与 OG 指向新路径；生产不依赖 Ghost CDN |
| OG/Hero | 绝对 URL = `{SITE_URL}/blog/images/...` |

#### 1.3 内链与外链

| 资产 | 导出 |
|------|------|
| 内链 | 源 slug → 目标 slug、锚文本、上下文 |
| 外链 | URL、rel、HEAD 存活 |
| CTA | 对照附录 A.5 白名单 |

交付：`exports/markdown/`、`exports/images/`、`reports/links.csv`（exports **gitignore**）。

**验收**：随机 5 篇 Ghost 文 → 离线 MD 与线上一致（结构 ±10%；H2 编号 Phase 5 统一）。

---

### Phase 2 — 构建博客 deployment

**目标**：独立 Next.js 博客，**真相源 = Git Markdown**。

#### 2.1 仓库结构（建议）

```
medo-blog/
├── content/blog/           # 与 medo/blog/ 同步
│   ├── *.md
│   ├── components/
│   └── design/
├── data/
│   └── blog-meta.ts        # 列表、OG 侧车（可选）
├── public/blog/images/
├── src/app/blog/
│   ├── page.tsx
│   └── [slug]/page.tsx
├── AGENTS.md
├── next.config.ts
└── .env.production         # SITE_URL，不入库
```

#### 2.2 必备能力

| 能力 | 要求 |
|------|------|
| SSG | `generateStaticParams` ← `content/blog/**/*.md` |
| SEO | `generateMetadata`、canonical、sitemap.xml、rss.xml |
| JSON-LD | `BlogPosting` + `BreadcrumbList` + FAQ（见 `medo/archive/medo-schema-spec.md`） |
| 列表 | 按 `date` 降序；`category` / `secondary_category` 筛选 |
| 区块 | 渲染 `## TL;DR`、`## Frequently asked questions` |
| 内链 | `/blog/{slug}` 相对路径 |
| Preview | PR → 预览 deployment；预览 env 单独 `SITE_URL` |

#### 2.3 与 `medo/blog/` 的关系

| 策略 | 说明 |
|------|------|
| **推荐** | 部署仓 `content/blog/` = `medo/blog/` 同步副本（CI rsync 或 submodule） |
| 策略文档 | `medo/blog-migration/`、`medo/skills/` 留在上下文仓，不混入 Next 应用 |

**验收**：`npm run build` 成功；Preview 可浏览 E 类 22 篇 + 已映射 A 类稿。

---

### Phase 3 — 主站反向代理

**目标**：访客与爬虫只见 `https://medo.dev/blog/*`。

#### 3.1 主站配置

| 项 | 规则 |
|----|------|
| 环境变量 | `BLOG_ORIGIN` = 博客源站 origin |
| Rewrite | `/blog/:path*` → `${BLOG_ORIGIN}/blog/:path*`（`beforeFiles` 优先） |
| 静态资源 | 精确转发 blog 的 `/_next/static/*`，或子站 `assetPrefix: '/blog'` |
| robots | 根 robots 声明 `https://medo.dev/blog/sitemap.xml` |
| Analytics | `/blog` 子路径单独分组 |

#### 3.2 权威 URL 验收 checklist

- [ ] `canonical` = `https://medo.dev/blog/{slug}`
- [ ] `og:url` 同上
- [ ] sitemap `<loc>` 无部署平台子域泄漏
- [ ] RSS / JSON-LD `@id` 指向主域
- [ ] OG 图片 URL 可 200
- [ ] `trailingSlash` 主站与子站一致

#### 3.3 职责分工（RACI）

| 事项 | Owner |
|------|-------|
| 主域 DNS + Rewrite | 主站/平台工程 |
| 子站内容与 build | 内容/营销 |
| `SITE_URL` / canonical | 子站 env（平台 Review） |
| `/_next` 冲突 | 平台工程 |
| 上线验收 | 平台工程 + 内容 |

**验收**：生产 `/blog/` 样式完整；GSC URL Inspection 显示主域 URL。

---

### Phase 4 — URL 映射、重定向与切流

#### 4.1 映射策略

| 场景 | 规则 |
|------|------|
| Ghost slug = 本地 slug | 本地稿覆盖 Ghost 导出 |
| 主题重复 | 合并为一篇 canonical，其余 **301** |
| Ghost 长尾 slug | 301 至常青 slug（记入 `slug-mapping.csv`） |
| Template pages | 默认 **410** 或 301 至 `/` / 未来 `/templates/*` |
| Video posts | 保留 `/blog/video/{slug}` 或 301 + embed |

#### 4.2 切流步骤

1. 子站 build + 主站 Rewrite **Preview 环境**验证
2. 生产开启 Rewrite（Ghost 并行，便于回滚）
3. 根 sitemap 加入 `/blog/sitemap.xml`
4. GSC / IndexNow 提交
5. Ghost 只读观察 2–4 周
6. 下线 Ghost `/blog` 路由

**验收**：无部署子域泄漏；旧 URL 抽样 301 正确；新 22 slug 返回 200。

---

### Phase 5 — 质量优化

**目标**：迁移稿达到 `medo/blog/` **Gate 可发布** 标准（附录 A.3、A.4）。

#### 5.1 提质优先级

| 优先级 | 范围 | 动作 |
|--------|------|------|
| P0 | 本地 22 篇 | **先上线**；补 OG 与 meta 侧车 |
| P1 | GSC 已索引 + 有流量 Ghost posts | 按 SKILL 重写至 Gate Pass |
| P2 | 其余 editorial | 合并或 stub + 301 |
| P3 | Video posts | 摘要 + VideoObject |
| P4 | Template pages | 不提质；Phase 4 退场 |

#### 5.2 自动化质检

| 脚本 | 用途 |
|------|------|
| `scripts/export-ghost-html-to-md.py` | 单篇 Ghost HTML → MD + manifest（Phase 1 试点） |
| `frontmatter_validator.py` | 必填字段、category 枚举 |
| `link_checker.py` | 内链白名单、无 404 |
| `word_count_narrative.py` | TL;DR、FAQ 长度 |
| schema 检查 | JSON-LD 对照 `medo/archive/medo-schema-spec.md` |

脚本可复用 `medo/skills/medo-blog-article/tools/` 现有实现。

**验收**：P0+P1 通过 G1–G7 + A1–A4。

---

### Phase 6 — 运维与 Ghost 下线

| 任务 | 说明 |
|------|------|
| AGENTS.md | 目录、frontmatter、内链、禁止 forthcoming 链 |
| CI | PR → lint + build + link check |
| 发布 | merge main → 子站 deploy → Rewrite 生效 |
| Ghost 下线 | JSON 归档 → Admin 只读 → 取消 `/blog` |
| 文档回写 | `medo/medo-site-structure.md`、`medo/blog/README.md` 部署节 |

---

## 四、Slug 映射（初稿）

### 4.1 本地稿优先（Ghost 无对应或 404）

| 本地 slug | 角色 | Ghost 近似文 |
|-----------|------|-------------|
| `how-to-build-mobile-app-with-ai` | Hub | `how-to-build-a-real-mobile-app-with-an-ai-app-builder` → 301 |
| `what-is-vibe-coding` | Spoke | — |
| `best-ai-mobile-app-builders` | Spoke | `6-best-full-stack-app-builder-tools-in-2026` 部分重叠 |
| `publish-ai-app-app-store` | Spoke | — |
| `medo-components` + `components/*` | 簇 | — |
| `best-ai-design-skills` + `design/*` | 簇 | UI enhancer 文部分重叠 |

### 4.2 Ghost 独有条目

| Ghost slug | 建议 action |
|------------|-------------|
| `best-lovable-alternative-in-2026-medo-vs-lovable-vs-bolt` | keep |
| `medo-hackathon-2026-guide-launch-your-ai-app-win-50k` | keep |
| `unlock-your-earnings-with-the-medo-affiliate-program` | keep |
| `*-template`（~50） | retire |
| `/blog/video/*`（9） | keep 或 301 + embed |

定稿表：`reports/slug-mapping.csv`（Phase 0 产出）。

---

## 五、风险与回滚

| 风险 | 缓解 |
|------|------|
| 双 Next `/_next` CSS 404 | `assetPrefix: '/blog'` 或精确 rewrite |
| canonical 泄漏部署子域 | `SITE_URL` 强制主域；CI 检查 |
| 模板页 404 潮 | GSC 监控；分批 410 |
| 重复内容 | 切流前 Ghost noindex 或先 301 |
| 图片 hotlink 失效 | Phase 1 镜像后再改 MD |

**回滚**：主站移除 Rewrite → Ghost `/blog` 恢复。

---

## 六、里程碑（建议）

| 里程碑 | 范围 | 工期 |
|--------|------|------|
| M0 | Phase 0 — URL 主表 + slug 映射 | 3–5 天 |
| M1 | Phase 1 — 导出 + 图片 | 5–7 天 |
| M2 | Phase 2 — 子站 MVP（22 篇 Preview） | 7–10 天 |
| M3 | Phase 3+4 — 生产 Rewrite + 切流 | 3–5 天 |
| M4 | Phase 5 — P1 提质 | 持续 |
| M5 | Phase 6 — Ghost 下线 | M3 + 14 天 |

---

## 七、Phase 0 行动项

- [ ] 配置 Ghost Content API 只读凭据（**仅存 secrets**）
- [ ] sitemap → JSON 脚本 → `ghost-url-inventory.json`
- [ ] 导出 GSC 已索引 blog URL
- [ ] slug 映射评审：template pages 退场策略
- [ ] 确认主站网关类型（Next / Nginx / CDN Worker）→ Rewrite runbook
- [ ] 创建博客 deployment 仓库

---

## 八、本计划引用的 medo 项目文档

| 文档 | 用途 |
|------|------|
| `medo/blog/README.md` | frontmatter 与正文规范 |
| `medo/blog/blog-structure-internal-links.md` | 内链图 |
| `medo/skills/medo-blog-article/SKILL.md` | 创作流程与 Gate |
| `medo/skills/medo-blog-article/references/project-config.md` | G1–G7、白名单 |
| `medo/archive/medo-schema-spec.md` | JSON-LD |
| `medo/archive/medo-indexing-diagnosis.md` | Ghost 收录现状 |
