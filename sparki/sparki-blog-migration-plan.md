# Sparki Blog 迁移计划：Contentful 线上博客 → OpenBlog

> **目标**：用 **Markdown in Git + OpenBlog + Next.js SSG** 替换 sparki.io/blog 现由「主站 Next.js 页 + Contentful」驱动的博客模块；所有在线文章（61 篇）连同图片迁移为 md，URL 保持 `/blog/{slug}` 不变。
>
> **OpenBlog 源码**：`E:\自有部署项目\openblog`  
> **部署项目（新建）**：`E:\客户部署项目\sparki-blog`  
> **参考同构项目**：`E:\客户部署项目\luciusai-blog`（38+38 en/zh 已迁移上线）  
> **策略仓**：`e:\clients\sparki\`（本文档 + site-structure，不混入 Next 应用）

**Last updated**：2026-09-04

---

## 当前进度

| 阶段 | 状态 | 说明 |
|------|------|------|
| Phase 0 URL/结构盘点 | ✅ 完成 | sitemap 快照 + DOM 审计 → [sparki-site-structure.md](./sparki-site-structure.md)（61 篇主表 §3） |
| Phase 1 线上导出 | ✅ 完成（2026-09-04） | **61/61 篇 md + 205 张本地图片**（见下方「Phase 1 执行记录」）；脚本 `E:\客户部署项目\sparki-blog\scripts\export_sparki_blog.py` |
| Phase 2 OpenBlog 脚手架 | 🟡 部分完成 | 脚手架+chrome/config/.env/logo/favicon 已完成；**主题品牌化（sparki tokens）待做**，先以 vercel-geist 上线同构 |
| Phase 3 主站切流 | ⏳ 待执行 | sparki.io `/blog/*` Rewrite（需运维侧） |
| Phase 4 上线质检 | 🟡 预发布门禁已过 | 本地 validate/build/冒烟✅（见 Phase 1 执行记录 §1.7）；**线上 URL/图片/GSC 复爬 diff** 待切流后 |
| Phase 5 增量维护 | ⏳ 待执行 | OpenBlog skills 内容工作流 |

---

## 现状盘点结论（2026-09-04 实测，详见 site-structure）

- **61 篇**英文文章；单页列表无分页/分类；每篇有 BlogPosting JSON-LD；纯英文无 i18n。
- 内容源 **Contentful**（图片 `images.ctfassets.net`，页面经 `/_next/image` 优化）。
- 作者唯一 `Sparki Team`；`articleSection`→category，`keywords`→tags；hero/列表日期 = `datePublished` 的 UTC 日期。
- 正文为 `.sparki-rich-content`：H2/H3、表格、列表、blockquote、部分含 figure 内图；站内 blog 互链为 `/blog/{slug}`。
- 需保持不变量：URL `/blog/{slug}`、标题/日期/作者/category/tags、站内互链、图片可访问。

---

## 架构

```
sparki.io（主站 Next.js — 首页/营销页/导航）
  rewrites: /blog/* → BLOG_ORIGIN        ← Phase 3，需主站运维配置
       ↓
E:\客户部署项目\sparki-blog（OpenBlog 独立部署）
  SITE_URL=https://sparki.io · DEPLOY_MODE=subdirectory · BLOG_BASE_PATH=/blog
       ↓
e:\clients\sparki\（策略仓 — 本文档、site-structure；内容变更走 git/PR）
```

与 luciusai-blog 完全同构；OpenBlog 子目录模式下公开 URL 自带 `/blog` 前缀，主站 Rewrite 原样透传即可（无 subdomain 的 middleware 依赖）。

---

## Phase 0 — URL/结构盘点（✅ 本次已完成）

产物：
1. `sparki-site-structure.md` 更新：全站 URL 地图、/blog 线上结构审计、**61 篇主表**（URL+标题+UTC 日期）、字段映射表（§4）、chrome/素材清单。
2. 盘点脚本/样本（临时，不入库）：sitemap 快照、列表 RSC 解析、3 篇文章 headless DOM 审计。

---

## Phase 1 — 线上导出（61 篇 md + 图片）

在部署项目内建 `scripts/export_sparki_blog.py`（复用 luciusai `lucius_export_lib.py` 的模式，替换站点相关选择器）：

### 1.1 抓取（headless 渲染）
- 对 61 个 `/blog/{slug}` 用 **Chrome headless `--dump-dom`** 渲染（页面正文在 RSC payload，需 JS 执行后才有 DOM；直接 curl 无正文）。
- 低并发（4–6 路，自带 user-data-dir），遵守 `robots.txt`（自有内容迁移、`search=yes`、不用于训练）。
- 原始渲染 HTML 存 `temp/render/{slug}.html` 供重试/复现。

### 1.2 元数据（meta_from_page）
- **JSON-LD BlogPosting**（渲染后 DOM 中）为主源：headline/description/datePublished/dateModified/keywords/articleSection/author/image。
- **SSR head 交叉校验**：canonical、og:image、og:published_time、`<title>`（去 ` - Sparki Blog` 后缀）。
- date/updated 规则：ISO 转 UTC 后取 `YYYY-MM-DD`（例 `2026-07-19T00:00+08:00` → `2026-07-18`）。

### 1.3 正文 → Markdown
- 选区 `.sparki-rich-content`。
- 表格先抽取为占位符；**转 GFM 管道表**后还原（⚠️ 实测本模板 Markdown 渲染器 = react-markdown + remark-gfm、**无 rehype-raw**：原生 `<table>` HTML 会被直接丢弃；GFM 管道表可原生渲染，并在 `src/app/globals.css` 补了 `.markdown-content table` 边框/表头样式）。
- `html2text`（body_width=0、保留链接/图片、保护链接）转 md；图片替换见 1.4；链接保持 `/blog/{slug}` 相对形态，外部链接原样保留。

### 1.4 图片本地化
- 收集：cover（og:image / hero next/image）+ 正文 `<figure><img>`。
- 页面 src 形如 `/_next/image?url=<urlencoded ctfassets>` → **解码 `url` 参数得 Contentful 原图**后下载，避免拿优化缩略图。
- 落盘 `public/blog/images/{slug}/{原文件名(去 URL 编码/去 query)}`（重名加序号）；记远端→本地映射并全量替换 md。
- 输出日志记录每篇 images/表格/外部链接/告警，供 Gate 质检。

### 1.5 Frontmatter
按 site-structure §4 映射表生成；`slug` 与文件名强一致；`category`/`tags` 取自 JSON-LD。

### 1.6 Gate 1 质检（导出后必过）
- `npm run validate:posts`（openblog frontmatter + slug=文件名 校验）。
- grep 残留：md 中无 `images.ctfassets.net`、`/_next/image`、`sparki.io/blog` 绝对链接。
- 抽样 diff：每簇（creator-series / 对比 / how-to / 产品发布 / 图文类）取 1–2 篇，标题/H2 数与源页比对；表格、blockquote 无损。
- 图片 404 检查：本地化图片全部存在且尺寸非 0。

---

### 1.7 Phase 1 执行记录（2026-09-04，已完成）

- **执行方式**：`scripts/export_sparki_blog.py`（Chrome headless 渲染 → JSON-LD/meta → md → 图片本地化 → frontmatter）。全部 61 slug 按 4 批并行（每批 `--jobs 2`），3 个首轮渲染超时的 slug（kylie-jenners / elysian-living / nicolelaeno）单独重试成功。
- **产物**：`content/blog/*.md` 61 篇；`public/blog/images/{slug}/` 本地图片（md 中图片引用 144 处 + cover 均落盘，0 缺失）；Contentful 原图按 `?w=1600&q=82` 约束宽度下载。
- **内容保真**：日期统一转 UTC 日期（frontmatter 覆盖 2025-10-31 → 2026-08-01）；category/tags/作者 `Sparki Team` 来自 JSON-LD；正文表格全部转 GFM 管道表（0 处残留原生 HTML table）；站内互链 `/blog/{slug}` 零改写、互链目标 100% 有效。
- **预发布门禁（已过）**：`npm run validate:posts` 61/61 ✅；`npm run build`（Next 16.3.3）SSG 70 路由全部生成 ✅；`next start` 冒烟抽查文章页：h1/正文图/3 张 GFM 表格渲染正常、`ctfassets/_next/image` 远端残留 0 ✅。
- **留档/可复现**：渲染 HTML 缓存于 `temp/render/{slug}.html`，任意后续再导出可用 `--cache` 离线重刷（约 5s）；导出日志 `temp/export-log.jsonl`。
- **遗留（非阻塞）**：主题仍为 vercel-geist 中性态（决策项 C 品牌化未做）；正文 CTA/站外链接按原文保留，其中少量写成 `<https://…>` 自动链接形态。

---

## Phase 2 — OpenBlog 脚手架与品牌

1. **脚手架**（方法同 luciusai-blog）：
   ```powershell
   cd E:\自有部署项目\openblog
   npm run create-openblog -- sparki-blog --dir "E:\客户部署项目\sparki-blog"
   cd E:\客户部署项目\sparki-blog
   npm run dev    # http://localhost:3000/blog
   ```
2. **openblog.config.ts**（✅ 已落地于部署项目）：
   ```ts
   site: { name: "Sparki", tagline: "The first AI editing agent",
           url: "https://sparki.io", deployMode: "subdirectory", blogBasePath: "/blog", locale: "en-US" }
   chrome: { mode: "openblog-default", siteUrl/homeUrl: "https://sparki.io",
             logo: "/brand/sparki-logo.png",
             nav: [ Home→https://sparki.io(external), Blog→/blog(match), Pricing→https://sparki.io/pricing(external) ],
             footer: …依 site-structure §2.3 素材清单回填（Features/Explore/Follow 三列 + legal） }
   content: { adapter: "local-md", options: { dir: "content/blog" } }
   features: { authors: true, categories: false, tags: false, rss: false }  // 决策项 A/B 已定
   theme: { preset: "vercel-geist", colorMode: "system", strategy: "hybrid" }
   ```
   - **决策项 A（taxonomy，已定）**：现网无 `/blog/category|tag/*` 路由 → 关闭页面开关、**数据仍写入 frontmatter**（未来要开分类页可直接启用）。
   - **决策项 B（作者，已定）**：作者唯一 `Sparki Team` → `authors: true` 单作者（author box 可选关闭）。
   - **决策项 C（主题，待做）**：现用 vercel-geist 中性起步；sparki 品牌色/字体（`text-sparki-*` tokens）以 CSS 变量对齐后再灰度 1 篇 diff。
3. 品牌素材（✅）：logo 已下载自主站 → `public/brand/sparki-logo.png`；favicon 复用主站同名资源。
4. `.env` / `.env.local`（✅）：`SITE_URL`、`DEPLOY_MODE=subdirectory`、`BLOG_BASE_PATH=/blog`、`ASSET_PREFIX=/blog`。
5. 示例文章 `hello-world.md`（✅ 已清理）。

---

## Phase 3 — 主站切流（需运维配合）

- sparki.io 当前自身是 Next.js（Vercel/自建待确认）——由站点维护方在 Vercel `rewrites` 或 Cloudflare Rule 添加：
  `/blog/:path*` → `https://{sparki-blog-origin}/blog/:path*`（子目录模式原样透传）。
- 灰度：先给少量 URL 或查询参数白名单切流；回滚即删 rule。
- 主站导航中 `/blog`、footer「Blog」无需改动（URL 不变）。

---

## Phase 4 — 上线质检清单

| # | 检查 | 通过标准 |
|---|------|---------|
| 1 | 61 URL 状态 | 新源全部 200，旧源 404 前完成切流后消失 |
| 2 | SEO head | canonical=`sparki.io/blog/{slug}`、title 后缀行为与现网对齐、BlogPosting JSON-LD 字段齐全 |
| 3 | sitemap | 新源 blog sitemap = 61（± 增量），robots 可爬 |
| 4 | 图片 | cover/内图 100% 本地化且 200；无 Contentful/`/_next/image` 残留 |
| 5 | 互链 | 61 篇站内 `/blog/{slug}` 互链无 404（脚本扫全量） |
| 6 | 视觉 | 列表/文章页 vs 现网 headless 截图 diff（桌面+移动） |
| 7 | 性能/GA | LCP 达标；GA/Clarity 事件可用性由主站侧确认 |

---

## Phase 5 — 增量内容运营

- 新文章走 OpenBlog 内容工作流：`blog-cms`（入口）→ `create-post`/`publish`/`validate-blog-seo` skills（位于 `E:\自有部署项目\openblog\skills`）；Markdown in Git 即 CMS。
- 内容方向对接现有关键词/场景资产：[sparki-keywords.md](./sparki-keywords.md)、[sparki-use-cases.md](./sparki-use-cases.md)、creators/video-types 系列沿用（creator 风格解析与 SEO 词簇可继续批量产文）。
- **中文版决策项 D**：现网纯英文；若未来加 `/zh/blog/*`，参考 luciusai `content/blog/zh/` + i18n 路由，本次不预建。

---

## 风险与注意事项

| 风险 | 缓解 |
|------|------|
| 切流归属：sparki.io 主站运维不在本仓控制 | Phase 3 前先与客户确认 Vercel/Cloudflare 配置入口与回滚开关 |
| Contentful 资产域名需在切流后继续可读（历史外链/缓存） | 导出阶段即全量本地化；旧图在灰度窗口继续由主站承载 |
| 部分封面文件名含 URL 编码/非 ASCII（如 `%C3%A5…`、乱码中文名） | 下载时以解码后 basename + 冲突序号落盘，md 引用一律走本地映射表 |
| 日期时区（`+08:00` vs 展示 UTC） | 全量按「转 UTC 日期」归一，避免前后台日期不一致 |
| 正文结构多样化（对比文多表格/图文文多 figure） | 导出门禁抽样覆盖两簇；html2text 前先占位表格 |
| 抓取合规 | 仅自有内容、低并发、不入训练集（robots `Content-Signal: search=yes, ai-train=no`） |

---

## 关联文档

| 文档 | 用途 |
|------|------|
| [sparki-site-structure.md](./sparki-site-structure.md) | 61 篇 URL 主表 + 字段映射 + chrome/素材清单（Phase 0 基线） |
| [sparki.md](./sparki.md) | 产品/策略索引 |
| `E:\客户部署项目\luciusai-blog` | 同构参考：README、openblog.config.ts、scripts/（export/validate/theme:sync） |
| `E:\自有部署项目\openblog` | OpenBlog 源码（README、INTEGRATION.md、skills/） |

*Last updated: 2026-09-04*
