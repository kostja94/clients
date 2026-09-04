# Sparki Blog Article Brief — What Is a Vlog?

> 生成：sparki-blog-article skill v1.0.0 · 2026-09-04 · Phase 0–3 交付
> 正文目标语言 en-US（本文件为工作稿，字段英文，说明中文）

---

## Phase 0 — Intake & Gate A

```
## Mode: flagship
## ArticleType: CategoryPOV
## InvestmentScore: 4.2 — 搜索稳定大词(5) / vlog=ICP核心场景但awareness级(3) / SERP无创作者向+AI向角度(4) / 深度调研一手素材足(4) / 2+年常青(5)
## Category (frontmatter): ai-video-editor
## Author: Sparki Team
## Gate A: KEEP
```

**六必问推演摘要**（topic-driven 推断）：
1. Primary keyword = **what is a vlog**（awareness 信息类）
2. 发布目的：SEO（截取 definition 级大词）+ 品牌（把 "vlog" 概念转为创作者语境，铺 AI vlog editing 需求）
3. 竞争关系：SERP Top = Wikipedia / Dictionary.com / Dan Sanchez / 器材厂商（Tamron、Insta360）→ 泛科普 + 器材向，**无 Creator-practical / AI-workflow 角度**（信息增量成立）
4. 内链白名单：已对照 project-config §2 确认可链页面
5. ArticleType：`what is` → CategoryPOV（推断；本词非单一功能、非红人）
6. CreatorClone：不适用

**KEEP 判定**：搜索意图独立（无既有 61 篇直接竞争）✓ · 读者阶段 Awareness（vs 既有 CreatorClone/HowTo 的 Consideration）✓ · 深度不可压缩 ✓ → **KEEP**

---

## Phase 0R — Research 三角

**R1**：project-config + article-types + content-graph + keywords 已读 ✓
**R2**（SERP Top）：`what is a vlog` → Wikipedia / Dictionary.com / Tamron / Dan Sanchez / Insta360
**R3**：sparki.io/features 已抓取 → 五功能（Copy Style / Long to Short / AI Caption / AI Commentary / Video Resizer）与白名单一致 ✓；footer 暴露 `/vlog` solution 入口（白名单对应项为 `/solutions/daily-vlog`）

**Synthesis Statement**：
> SERP 把 vlog 定义成"视频博客"，停留在词典层；我们从创作者执行视角重定义——vlog 的本质是"单一 creator 同时是叙述者与拍摄者的第一人称视频"，其 2026 现实是剪辑从技术门槛变为最大时间瓶颈（daily vlog 转型、短视频化、AI 进入工作流）。这是 SERP 空白。

**Information increment（≥2）**：
- [x] 定义三特征 + 与 blog / video essay / documentary 的边界（非"任何网上视频"）
- [x] 双维度类型法：叙事架构（talking-head / follow-me-around）× 主题 niche
- [x] 2026 增量：daily vlog 需故事化、长改短切条成增长机制、AI 剪辑进入创作链路
- [x] 一手事实源：Wikipedia 历史时间线、Guardian 2004 报道、MW/Cambridge 定义、YouTube CEO 2026 信

**Research Log**：R2/R3 完成，`competitor:TBD`（definition 词无传统竞品对标；链接照 Wikipedia/MW 即可）

---

## Phase 1 — Article Brief

```markdown
## Article Brief

**Mode**: flagship
**ArticleType**: CategoryPOV
**InvestmentScore**: 4.2 — 见 Phase 0
**SuccessMetric**: 首月自然搜索 Impression 增长；进站后访问 /solutions/daily-vlog 或 /features/long-to-short 占比 ≥8%；CTR ≥3%
**MoatAssetPlanned**: 创作者视角定义 + 双维度类型法 + 2026 剪辑现实（非词典复述）
**AnswerBlocks**:
  1. What exactly is a vlog — and what is it not?
  2. What are the main types and formats of vlogs?
  3. Where is vlogging going in 2026, and what does making one actually take?
  4. Do you need AI editing tools to vlog — and where do they fit?
**PostPublishReviewDates**: T+7 / T+30 / T+90 / T+180

**Working title**: What Is a Vlog? Types, Formats, and How Creators Make Them
**Primary keyword**: what is a vlog
**Search intent**: Informational (definition / awareness)
**Category**: ai-video-editor
**Reader stage**: Awareness
**Publish goal**: SEO + brand
**Target audience**: Aspiring creators / vlogger-curious viewers who hit "what is a vlog" and are deciding whether to start
**Synthesis Statement**: 见 Phase 0R
**One-line thesis**: A vlog is first-person video where one person is the narrator and the camera — and in 2026, editing is the real barrier to entry, not filming.
**Differentiation angle**: Creator-execution lens + dual-axis taxonomy + 2026 workflow reality (vs SERP dictionary/gear marketing)
**Information increment**: 见 Phase 0R（≥3 项已验证）
**Candidate examples**: talking-head (MKBHD/teaching) vs follow-me-around (travel/daily) 两类典型 + 短视频切条案例
**Word count target**: 2400–2700（CategoryPOV 2000–3000 区间，产品占比 ≤25%）
**Topic Scope / Cluster**: Platform & Format / AI editing Category POV 交界（新簇入口候选：Vlog 101）
**Planned internal links**:
  - /blog/edit-vlog-15-minutes-smart-cut（相对，vlog 智能剪辑工作流）
  - /blog/how-to-edit-a-festival-vlog-like-charli-damelio（相对，vlog 实操红人文）
  - https://sparki.io/solutions/daily-vlog（绝对 URL，vlog solution 页）
  - https://sparki.io/features/long-to-short（绝对 URL，短视频化环节）
**Slug candidate**: what-is-a-vlog
**Author**: Sparki Team
```

---

## Phase 2 — Slug、Date & Gate B

| 项 | 值 |
|----|----|
| **slug / 文件名** | `what-is-a-vlog`（= 文件名；无 NN；≤60 字符 ✓） |
| **title** | "What Is a Vlog? Types, Formats, and How Creators Make Them"（长度 ~63，建议 Draft 阶段压缩至 45–60，如 "What Is a Vlog? Types, Formats, and How to Start" ~49） |
| **description** | 建议 ~140 chars：`What is a vlog? A vlog is a first-person video blog where one creator narrates and films. Learn vlog types, formats, and what editing takes in 2026.` |
| **date（建议）** | 2026-09-08（UTC）— content-graph 显示最近占用 08-01；9 月上旬目前无占位；发布前需以部署仓 frontmatter 二次确认 |
| **tags** | `["what is a vlog", "vlogging", "types of vlogs", "vlog editing", "AI video editor"]` |
| **category** | `ai-video-editor` |
| **author** | `Sparki Team` |

**Gate B**：6 问通过；12 反模式零触发（无年份/无 `ultimate`/`guide` 后缀 ✓ 常青 ✓ kebab ✓ 含主词 ✓）。

---

## Phase 3 — Outline

```
## Outline — what-is-a-vlog

| § | H2 | Answer block | Reader state | Target words | Links / Notes |
|---|-----|--------------|--------------|-------------|---------------|
| TL;DR | — | AB-0 | 刚搜进来：一句话答案? | 100 | bullet 1 = snippet（定义） |
| 1 | What a Vlog Actually Is (and Isn't) | AB-1 | 想要可靠定义 | 600 | 三特征；vs blog/video essay/documentary；引 MW/Wikipedia |
| 2 | The Two Architectures and the Main Vlog Types | AB-2 | 想了解有哪些形态 | 650 | 双维度法；类型表（文本表非伪列表需谨慎）；1–2 实例 |
| 3 | Where Vlogging Is Now in 2026 | AB-3 | 想知道是否过时 | 500 | daily vlog 转型；短视频化；AI 剪辑进入链路；link long-to-short（绝对 URL） |
| 4 | What Making a Vlog Actually Takes | AB-3 | 想评估起步成本 | 450 | 设备门槛降→剪辑成瓶颈；手动 vs AI 工作流；link /blog/edit-vlog-15-minutes-smart-cut + /solutions/daily-vlog |
| 5 | Conclusion | — | 决定是否上车 | 150 | CTA（试一条 10 分钟素材）；产品占比 ≤25% |
| FAQ | 4 | — | PAA + 异议 | 250 | 首句即答：Is a vlog just a YouTube video? / Do vlogs need editing? / Do you need a camera? |
```

**Estimated total**: ~2700 words（含产品段落 ≤25% 控制）

**产品占比控制**：§1–3 不出现产品名；§4 末段集中出现 Sparki + 白名单绝对 URL（≤2 次）；FAQ 仅 1 条可含产品。全程不用禁词、不虚构开场。

**内链验证（对照 internal-links R1–R6）**：
- blog 互链 ≥2 且分散：`/blog/edit-vlog-15-minutes-smart-cut`（§4）、`/blog/how-to-edit-a-festival-vlog-like-charli-damelio`（§2 实例处）✓
- 主站绝对 URL：`https://sparki.io/solutions/daily-vlog`（§4）、`https://sparki.io/features/long-to-short`（§3）✓
- 外链 2–4：Wikipedia vlog 页 + Merriam-Webster vlog 定义（§1），可加 The Guardian 2004（历史）✓
- 无相对 `/features`、无未上线页面、锚文本描述性 ✓

**Phase 3.5**：N/A — single article

---

## OG / Cover Image Prompt（APINEED · 1200×630）

**交付物 #7**。执行规格（按 apineed gpt-image-2 惯例）：

| 参数 | 值 |
|------|----|
| Provider / Model | APINEED · `gpt-image-2` |
| 请求尺寸 | 1536×1024（`quality=high`）→ **top-aligned trim → 1200×630**（OG 最终） |
| output | JPEG 原图 → 裁切后存 WebP/PNG |
| 输出路径（frontmatter cover） | `/blog/images/what-is-a-vlog/cover.webp`（对齐 OpenBlog cover 约定；具体目录以部署仓 images 规范为准） |
| Key | `APINEED_API_KEY`（环境变量，禁入 git） |

**Composition brief（R1 强相关）**：
- HERO：年轻创作者手持相机（含翻转屏/手机 gimbal）对着自己拍——talking-head + follow-me-around 双语义合一
- 次级 tile：生活场景快照（城市街景 / 厨房 / 户外）以拼贴形式散落，暗示"记录日常"
- 顶部构图：上方 10% 留标题安全区（`CROP SAFE ZONE`），headline 文本由脚本/画布置于左上 8% 内，左 48% 宽度内，避免贴边
- 无品牌 logo / App 名入画（由后期叠加）；无多余可读文字

**English prompt（可直接注入）**：
```
APINEED CROP SAFE ZONE: keep top 10% clear for a headline, left 8% margin safe, subject must avoid the bottom band that gets cropped out. Editorial collage, 1536x1024, high quality. Visual-only: (1) HERO — a young creator filming themself with a mirrorless camera on a gimbal, talking to the lens with an authentic smile, urban soft light; (2) secondary tiles — candid moments of daily life: coffee shop, city street walk, cooking at home, outdoor travel shot; (3) subtle filmstrip/play-button motif linking the tiles. Warm cinematic color grade with teal-and-orange accent. Headline area intentionally left as open negative space at top. No text, no logos, no watermark.
```

**验收**：不看 URL 能猜主题（vlog/creator）· 画布除标题无多余文字 · 严格 1200×630 · 仅 1 个品牌标记后期叠加。

---

## Source Map（Phase 0R 素材对应）

| 事实 | 来源 |
|------|------|
| 定义：blog form whose medium is video | Wikipedia Vlog / Merriam-Webster / Cambridge |
| 两母型：talking-head vs follow-me-around | Wikipedia Vlog |
| 历史起点：Adam Kontras 2000-01-02；"year of the video blog" 2004 | Wikipedia + The Guardian (2004-08-07) |
| 词典收录：MW 2009、OED 2016 | The Guardian (2009-07-09) / East Bay Times |
| 2026 平台口径：>$100B 支付创作者、短/长生态、AI 治理 | YouTube CEO Neal Mohan 2026 letter (blog.youtube) |
| creator economy ≈$310B (2026) | Grand View Research（经 PRNewswire） |

---

## 后续步骤（Phase 4–6 待命）

1. 本 brief 与 outline 确认 → 按 sparki-blog-article skill Phase 4（Draft）加载 article-types + writing-constraints + product-competitors
2. 成稿落盘 `E:\客户部署项目\sparki-blog\content\blog\what-is-a-vlog.md`（`draft: true`）
3. 头图经 APINEED 生成 + trim 1200×630 → 部署仓 images 目录；frontmatter `cover` 指向
4. Phase 5 跑 3 个 validator + `npm run validate:posts`；通过后给 final-audit 指令
