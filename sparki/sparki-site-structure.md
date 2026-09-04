# Sparki 网站结构（sitemap 实测）与 /blog 迁移盘点

> **本文职责**：sparki.io 全站 URL 地图 + **/blog 线上现状审计**（OpenBlog 迁移的对象基线）。
> **来源**：`sitemap.xml`（2026-09-04 抓取，140 条、去重 139）+ `/blog` 列表页（RSC + Chrome headless 渲染）+ 3 篇文章页渲染抽查（对比类 / 发布类 / 图文类）。
> **上一版**（2026-04-08，首页 IA 推断）中标注「待验证/未来页」的 creators、industries、video-editor、features、solutions 等集群现已在 sitemap 落地；本文以实测为准更新，并新增 /blog 迁移所需的全部字段。

---

## 0. 结论摘要（2026-09-04 实测）

| 项 | 结论 |
|------|------|
| 全站 sitemap | 140 条（去重 139；`/platforms` 重复收录 1 次） |
| Blog 文章 | **61 篇**，单页列表一次性渲染，**无分页、无分类/标签筛选、无 /blog/category|tag|author 归档路由** |
| 技术栈 | 主站 Next.js（App Router，`app/(static)/blog/`）；博客内容由 **Contentful** 驱动（图片 `images.ctfassets.net`），经 `/_next/image` 优化输出 |
| 语言 | 纯英文；文章页**无 hreflang/alternate**，无 i18n 变体 |
| 文章页 SEO | 每页 BlogPosting JSON-LD + canonical + og:title/description/image/published_time；`og:type=article`；head title 带后缀 ` - Sparki Blog` |
| 作者 | 唯一署名 **Sparki Team**（JSON-LD 为 `Organization`） |
| 日期 | JSON-LD `datePublished` 带 `+08:00` 时区（CMS 时区）；**hero/列表展示为 UTC 日期**（示例：`2026-07-19T00:00+08:00` → 展示 `July 18, 2026`） |
| 目标 | 与 luciusai-blog 同构：OpenBlog 子目录模式独立部署，`/blog/*` 经主站 Rewrite 切流（见 [sparki-blog-migration-plan.md](./sparki-blog-migration-plan.md)） |

---

## 1. 全站 URL 地图（sitemap 去重 139 条）

### 1.1 分组统计

| 分组 | 收录数 | 说明 |
|------|-------:|------|
| `/blog/{slug}` 文章 | 61 | 本文 §3 主表 |
| `/industries/*` | 21（另含 hub `/industries`） | 本地商家行业落地页 |
| `/creators/*` | 18（另含 hub `/creators`） | 红人风格复制分析（策略文档见 [creators/](./creators/)） |
| `/video-editor/*` | 14 | 视频类型落地页（Product Video / Gaming 两簇） |
| `/features/*` | 5 | copy-style / long-to-short / ai-caption / ai-commentary / video-resizer |
| `/solutions/*` | 5 | highlight-reels / edit-videogen-clip / youtube-to-tiktok / daily-vlog / panoramic-camera |
| 核心页 | ~9 | `/`、`/blog`、`/pricing`、`/features`、`/solutions`、`/use-cases`、`/platforms`、`/policy`、`/terms` |
| 其余 | 4 | `/doc/api`、`/doc/developer`、`/openclaw-skill/sparki-video-editor`、`/tools/veo3.1` |

> 原 homepage「功能快捷标签 / 场景展示」推断现已在 `/features/*`、`/video-editor/*`、`/solutions/*`、`/creators/*` 等真实页面落地；**Blog 是唯一仍与主站同构、内容由 CMS（Contentful）驱动的模块**，也是本文档聚焦迁移的目标。

### 1.2 站点树（Blog 展开）

```
sparki.io/
├── /                      首页（Hero + 功能/场景 + Pricing + FAQ）
├── /pricing · /features · /solutions · /use-cases · /platforms
├── /features/*            5 大功能标签（copy-style/long-to-short/ai-caption/ai-commentary/video-resizer）
├── /solutions/*           场景方案（highlight-reels、youtube-to-tiktok…）
├── /video-editor/*        14 页（product-video/product-ad/… 、gaming/highlight…）
├── /creators/*            18 位红人
├── /industries/*          21 个行业
├── /doc/api · /doc/developer · /openclaw-skill/… · /tools/veo3.1
├── /blog                  Blog 列表（H1「Blogs」，61 张卡片，单页）
│   └── /blog/{slug}       61 篇文章（§3 主表）★迁移对象
├── /policy · /terms       法务页
```

---

## 2. /blog 线上现状（迁移对象审计）

### 2.1 列表页 `/blog`

- H1「Blogs」；CSS grid 卡片：`aspect-[16/9]` 封面（next/image，源为 Contentful）→ 标题（H2）→ 简介（description 截断 3 行）→ 日期 + 作者（Sparki Team）。
- **单页全部 61 篇**，无分页、无 Load more、无可见分类/搜索筛选（渲染后 DOM 仅含 61 张卡片与 Get Started CTA）。
- 每张卡片无 category 标签，日期为 UTC 日期（如 `July 18, 2026`）。

### 2.2 文章页 `/blog/{slug}`

- **head**：title 带 ` - Sparki Blog` 后缀；canonical；og:title/description/image/published_time/modified_time；**BlogPosting JSON-LD** 字段齐全：`headline / description / datePublished / dateModified / keywords / articleSection / author(Organization: Sparki Team) / image`。
- **hero 区**：H1 + 元信息行（日期 · 作者 · category chip）；封面图（hero 主图 = `og:image`）。
- **正文容器** `.sparki-rich-content`：H2/H3、段落、ul/ol、**HTML 表格**（对比文常见，抽查 OpusClip 对比文含 3 表）、blockquote、部分文章含 `<figure><img>` 内图（抽查图文文 5 图）；无代码块、无 iframe 媒体（抽查样本内）。
- 正文互链：站内 blog 交叉引用形如 `/blog/{slug}`（相对路径）；外部站外链接绝对 URL。
- 页尾 CTA：`Edit with Sparki / … / Get Started for Free`（链接目标待上线前从按钮 href 确认）。

### 2.3 素材与 chrome（做 OpenBlog 皮肤/导航用）

| 项 | 值 |
|----|----|
| Logo | 主站资源 `/landing-v1/home/home_page_logo.png?v=20260714-1`（下载至 `public/brand/`） |
| Favicon | `/favicon.svg` + `/favicon-{16,32,48,96}.png` + `/apple-touch-icon.png` |
| header nav | Home `/` · Blog `/blog` · Pricing `/pricing`（+ logo→`/`） |
| footer「功能」列 | `/features/copy-style`…`video-resizer`；`/solutions/highlight-reels`…`panoramic-camera`；`/video-editor/product-video`；`/video-editor/gaming` |
| footer「资源」列 | Blog `/blog` · Creators `/creators` · Industries `/industries` · Use Cases `/use-cases` · API `/doc/api` · OpenClaw `/openclaw-skill/sparki-video-editor` |
| footer 底部 | Pricing `/pricing` · Contact Us `mailto:support@sparksview.com` · Terms `/terms` · Privacy `/policy` |
| Socials | X `x.com/sparkilovesedit` · YouTube `@sparkiai_official/shorts` · Instagram `sparki_ai_official` · TikTok `sparkiai_official` · Discord `discord.gg/3cWs84Jza8` |

---

## 3. Blog 文章 URL 主表（61 篇，迁移基线）

> 列说明：`URL`= 现网永久链接（迁移后保持不变）；发布日期 = hero/列表展示的 **UTC 日期**（= `datePublished` 转 UTC 后日期）。正文 category（`articleSection`）与 tags（`keywords`）以单篇导出时 JSON-LD 抓取为准，不在此表逐一预填。

| # | URL | 标题 | 发布日期 |
|---|-----|------|---------|
| 01 | `/blog/how-to-automatically-add-b-roll-to-talking-head-videos` | AI B-Roll Generator for Talking-Head Videos: How to Auto-Add B-Roll | 2026-07-27 | |
| 02 | `/blog/how-to-turn-a-podcast-episode-into-shorts-with-ai` | Podcast Clips: Turn Episodes Into Shorts With AI | 2026-08-01 | |
| 03 | `/blog/what-ai-video-editors-can-automate` | Can AI Edit Videos? What It Can and Can’t Automate | 2026-07-31 | |
| 04 | `/blog/jenn-im-toddler-meals-content` | How to Document Toddler Meals Like Jenn Im | 2026-07-30 | |
| 05 | `/blog/opusclip-vs-vizard-vs-klap-vs-sparki-ai-video-editors` | OpusClip vs Vizard vs Klap vs Sparki: Which AI Video Editor Fits Long-to-Short Workflows | 2026-07-18 | |
| 06 | `/blog/how-to-master-hyper-realistic-illusion-content-like-amauryguichonchef` | How to Master Hyper-Realistic Illusion Content Like AmauryGuichonChef | 2026-07-01 | |
| 07 | `/blog/ai-commentary-generator-videos` | AI Commentary Generator for Videos Guide | 2026-07-01 | |
| 08 | `/blog/ai-commentary-sports-highlights` | AI Commentary for Sports Highlights | 2026-06-30 | |
| 09 | `/blog/how-to-master-the-satisfying-prank-format-like-candy-superstar` | How to Master the "Satisfying Prank" Format Like candy.superstar | 2026-06-29 | |
| 10 | `/blog/how-to-master-the-aspirational-couple-vlog-like-theabnormalcouple` | How to Master the "Aspirational Couple" Vlog Like TheAbnormalCouple | 2026-06-28 | |
| 11 | `/blog/how-to-master-the-nyc-girly-self-care-aesthetic-like-elysian-living` | How to Master the "NYC Girly" Self-Care Aesthetic Like Elysian.living | 2026-06-25 | |
| 12 | `/blog/how-to-master-luxury-fashion-content-creation-like-sooyaaa` | How to Master Luxury Fashion Content Creation Like sooyaaa | 2026-06-23 | |
| 13 | `/blog/how-to-master-viral-food-content-creation-like-bayashitv` | How to Master Viral Food Content Creation Like BayashiTV | 2026-06-22 | |
| 14 | `/blog/how-to-master-adventure-content-creation-like-karaandnate` | How to Master Adventure Content Creation Like KaraAndNate | 2026-06-21 | |
| 15 | `/blog/how-to-produce-viral-comedy-skits-like-lillysingh` | How to Produce Viral Comedy Skits Like Lilly Singh | 2026-06-17 | |
| 16 | `/blog/how-to-master-travel-highlight-reels-like-nicolelaeno` | How to Master Travel Highlight Reels Like NicoleLaeno | 2026-06-17 | |
| 17 | `/blog/jenn-im-viral-content-strategy` | How to Create Viral Content Like Jenn Im | 2026-06-11 | |
| 18 | `/blog/engaging-lifestyle-vlogs-spencer-barbosa` | How to Create Engaging Lifestyle Vlogs Like Spencer Barbosa | 2026-06-08 | |
| 19 | `/blog/brooke-monk-disney-food-review-analysis` | How to Create Viral Disney Food Reviews Like Brooke Monk | 2026-06-04 | |
| 20 | `/blog/katie-feeney-hyrox-viral-video-analysis` | How to Create Engaging Viral Video Content Like Katie Feeney | 2026-06-01 | |
| 21 | `/blog/viral-travel-adventure-kara-nate` | How to Create Viral Travel Content Like Kara and Nate | 2026-05-24 | |
| 22 | `/blog/pamela-reif-strength-narrative-shorts` | How to Cultivate Strength Narratives Like PamelaReif | 2026-05-20 | |
| 23 | `/blog/craft-viral-winter-travel-videos-sydney-sweeney` | How to Craft Viral Winter Travel Videos Like Sydney Sweeney | 2026-05-18 | |
| 24 | `/blog/how-to-replicate-jake-paul-heliskiing-vlog-adventure-luxury` | How to Create Hypnotic Heliskiing Videos Like Jakepaul | 2026-05-11 | |
| 25 | `/blog/youtube-caption-generator-vs-manual-cleanup` | YouTube Caption Generator vs Manual Cleanup: Where the Time Actually Goes | 2026-05-10 | |
| 26 | `/blog/ai-caption-generator-how-to-pick-the-right-workflow` | AI Caption Generator: How to Pick the Right Workflow | 2026-05-10 | |
| 27 | `/blog/how-to-edit-a-festival-vlog-like-charli-damelio` | How to edit a Festival Vlog Like Charli D'Amelio | 2026-05-08 | |
| 28 | `/blog/selena-gomez-red-eyeliner-routine` | How to Edit a Viral Makeup Video Like Selena Gomez | 2026-05-08 | |
| 29 | `/blog/how-to-edit-a-high-end-lip-combo-video-like-kendall-jenner` | How to edit a High-End Lip Combo Video Like Kendall Jenner | 2026-04-29 | |
| 30 | `/blog/how-to-make-a-viral-4am-morning-routine-vlog-that-feels-elevated-like-alice-wu` | How to Edit a Viral Morning Routine Vlog like Alice Wu | 2026-04-29 | |
| 31 | `/blog/webinar-to-social-clips-without-re-editing` | How to Turn a Webinar into Social Clips Without Re-Editing Every Version | 2026-04-23 | |
| 32 | `/blog/podcast-to-shorts-without-losing-context` | How to Turn a Podcast into Shorts Without Losing Context | 2026-04-23 | |
| 33 | `/blog/long-video-to-short-video-extract-highlights-vs-rebuild-structure` | Long Video to Short Video: Rebuild Structure or Extract Highlights? | 2026-04-22 | |
| 34 | `/blog/how-to-edit-like-kylie-jenners-hot-videos` | How to Edit Like Kylie Jenner’s Hot Videos | 2026-04-09 | |
| 35 | `/blog/how-to-edit-viral-morning-routine-vanessa-faga` | How to Edit a Viral Morning Routine Vlog like Vanessa Faga | 2026-04-02 | |
| 36 | `/blog/sparki-vs-capcut` | Sparki vs CapCut: Template Editing vs Reference-Based Workflow | 2026-03-29 | |
| 37 | `/blog/copy-video-editing-style-from-reference` | How to Copy a Video Editing Style From a Reference Clip | 2026-03-29 | |
| 38 | `/blog/resize-video-for-shorts-reels-tiktok` | How to Resize Video for Shorts, Reels, and TikTok: Crop, Blur, or Reframe | 2026-03-06 | |
| 39 | `/blog/long-video-to-short-video` | How to Convert Long Video to Short Video: Best AI Tools and Workflow | 2026-03-06 | |
| 40 | `/blog/capcut-auto-captions-alternatives` | CapCut Auto Captions Alternatives: Accuracy, Segmentation, Styles Compared | 2026-03-05 | |
| 41 | `/blog/best-linux-video-editors` | Best Linux Video Editors: Pro NLE vs FOSS vs Browser-Based (2026) | 2026-03-04 | |
| 42 | `/blog/seedance-clips-to-shorts-post-production-workflow` | From Seedance Clips to Shorts: A Post-Production Workflow | 2026-02-21 | |
| 43 | `/blog/descript-vs-gling` | Descript vs Gling.ai (2026): Which Tool Matches Your Videos Editing Workflow? | 2026-02-17 | |
| 44 | `/blog/best-video-editor-without-download-3-browser-workflows` | Best Video Editor Without Download: 3 Browser Workflows That Actually Work | 2026-02-01 | |
| 45 | `/blog/potato-pc-video-editing-guide-low-end-laptop` | The Potato PC Video Editing Guide: Finish Edits on a Low-End Laptop Without the Lag | 2026-01-26 | |
| 46 | `/blog/video-editor-for-chromebook-guide` | Best Video Editor for Chromebook: 4 Scenario-Based Fixes (Plus Tools That Fit Each One) | 2026-01-26 | |
| 47 | `/blog/talking-head-editing-agent` | How to Edit Talking Head Videos Without the "Robot" Feel: An Agentic Editing Workflow | 2026-01-10 | |
| 48 | `/blog/descript-alternative-2026` | Descript Alternative in 2026: Choosing Between CapCut, Gling, and the Agent Path | 2026-01-09 | |
| 49 | `/blog/opusclip-alternatives-subtractive-vs-additive-editing` | OpusClip Alternatives: Editing Raw Footage vs Clip-Based AI | 2026-01-08 | |
| 50 | `/blog/chat-to-edit-commentary-video-editing` | Commentary Video Editing Burnout: How Chat-to-Edit AI Replaces the Timeline | 2025-12-24 | |
| 51 | `/blog/edit-vlog-15-minutes-smart-cut` | How to Edit a Vlog in 15 Minutes: The "Smart Cut" Process (Escaping the Rule of 60) | 2025-12-23 | |
| 52 | `/blog/raw-footage-to-montage-ai` | The Ghost of "Editing Past": Why You Never Edit Your Raw Footage (And How AI Fixes It) | 2025-12-22 | |
| 53 | `/blog/ai-video-editor-understands-your-footage` | Why AI Video Editors Need to Understand Your Footage (Christmas Was Just the Test Run) | 2025-12-22 | |
| 54 | `/blog/edit-youtube-videos-with-ai-agent` | Editing YouTube Videos in 2025 With an AI Agent Instead of a Timeline | 2025-12-03 | |
| 55 | `/blog/ai-reels-editing-2025` | Instagram Reels Specs 2025 & How to Cut Editing Time by 90% | 2025-12-02 | |
| 56 | `/blog/learn-video-editing-with-ai` | How to Edit Videos in 2025: Video Editing Tips for Beginners Using AI | 2025-12-02 | |
| 57 | `/blog/tiktok-ai-video-editor` | Best AI Video Editors for TikTok: Tools That Actually Re-Edit for 9:16 | 2025-12-02 | |
| 58 | `/blog/ai-video-editor` | AI Video Editing Paradigms in 2025: What Real Users Really Think | 2025-11-21 | |
| 59 | `/blog/best-capcut-alternatives-2025` | 4 Best CapCut Alternatives in 2026 (1k+ Reddit/G2 Reviews) | 2025-11-20 | |
| 60 | `/blog/gemini-3-pro-ai-video-editor` | Gemini 3 Pro for Video Editing: Why Its Three Core Upgrades Finally Make AI Editors Useful | 2025-11-20 | |
| 61 | `/blog/the-rise-of-vibe-video-editing` | The Rise of Vibe Video Editing: Let Sparki Handle Your Video | 2025-10-31 | |
<!-- 共 61 行 -->

---

## 4. 文章字段 → OpenBlog frontmatter 映射（导出脚本据此实现）

| frontmatter | 来源（文章页） | 处理规则 |
|-------------|---------------|---------|
| `title` | JSON-LD `headline`（兜底 `og:title` 去 ` - Sparki Blog`） | 保留原名，YAML 引号转义 |
| `description` | `meta description` / JSON-LD `description` | 80–320 字符校验 |
| `slug` | canonical 末段 | **文件名 = `{slug}.md`**（校验脚本强一致） |
| `date` | JSON-LD `datePublished` | **转 UTC 后取日期**（与线上展示一致），格式 `YYYY-MM-DD` |
| `updated` | JSON-LD `dateModified`（仅当 ≠ date） | 转 UTC 后取日期 |
| `author` | JSON-LD `author.name` | `Sparki Team` |
| `category` | JSON-LD `articleSection` | trim 尾部空格（抽样值如 `AI Tools`） |
| `tags` | JSON-LD `keywords` | 逗号拆分、trim（未来如需标签页可直接启用） |
| `cover` | `og:image` / hero `/_next/image` src 中 `url` 参数解码 | 下载 → `/blog/images/{slug}/{原文件名}` |
| `locale` | — | `en` |
| `draft` | — | `false` |
| 正文图片 | `.sparki-rich-content` 内 `<figure><img>` 的 `/_next/image` src | 解码 `url` 参数 → Contentful 原图 → 本地化 + md 引用替换 |

**日期换算示例**：`datePublished: 2026-07-19T00:00+08:00` = UTC `2026-07-18T16:00Z` → `date: 2026-07-18`（与 hero/列表一致）。

**正文处理规则**：表格转 **GFM 管道表**（⚠️ OpenBlog 模板渲染器 = react-markdown+remark-gfm、无 rehype-raw，原生 `<table>` 会被丢弃；GFM 由渲染器原生支持，表格样式见 `src/app/globals.css` 的 `.markdown-content table`）；链接保持 `/blog/{slug}` 相对形态（跨文互链零改写成本）；非 blog 站内/站外链接按原文保留。

---

## 5. 与迁移的关系、待办与风险

| 项 | 说明 / 状态 |
|----|------------|
| 部署项目 | `E:\客户部署项目\sparki-blog`（新建，方法同 luciusai-blog） |
| OpenBlog 源 | `E:\自有部署项目\openblog`（`create-openblog` 脚手架） |
| 完整方案 | [sparki-blog-migration-plan.md](./sparki-blog-migration-plan.md) |
| 主站 Rewrite | `/blog/*` 切流需 sparki.io 运维侧配置（Vercel rewrites / Cloudflare Rule），**归属待确认** |
| 分类/标签路由 | 现网无 `/blog/category|tag/*`；迁移期建议**保留数据、关闭页面开关**，维持 URL 地图不变 |
| CTA 目标 href | 上线前从页面按钮抓取确认 |
| 抓取合规 | `robots.txt` Content-Signal `search=yes`；仅为**自有内容迁移**做低并发抓取，不进入 AI 训练 |

---

*遵循 [客户文档规范](../demo/client-template.md)*
*关联：[sparki.md](./sparki.md) | [sparki-blog-migration-plan.md](./sparki-blog-migration-plan.md) | [creators](./creators/) | [video-types](./video-types/)*
*Last updated: 2026-09-04*
