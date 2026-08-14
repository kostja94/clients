# Vofy — 站点结构（Site Map）

> 关联：[vofy-sitemap-optimization-zh.md](./vofy-sitemap-optimization-zh.md) · [vofy-keywords.md](./vofy-keywords.md) · [vofy-features.md](./vofy-features.md)
> 数据来源：[sitemap.xml](https://www.vofy.art/sitemap.xml) + 导航内链
> 快照日期：2026-06-22 · **381 URL**（lastmod 2026-06-18）

**官网首页**：[vofy.art](https://www.vofy.art/)

---

## 总览（数量汇总）

| 层级 | 分类 | 数量 | 路径形态 |
|------|------|------|----------|
| L1 | 核心 / 营销页 | **25** | `/`、`/pricing`、`/blog`（索引）、`/ai-tools`、`/ai-effects`、Use Cases、Campaign 等 |
| L2 | AI 能力 hub | **6** | `/ai-image-*`、`/ai-video-*`（均在 sitemap） |
| L3 | 模型 | **23** + 2 目录 | `/models`、`/models/rankings`、`/models/{slug}` |
| L4 | Apps | **259** | 5 hub + **254** 工具 `/apps/{slug}` |
| L5 | Blog | **75** | `/blog` + **74** 篇 `/blog/{slug}` |
| L6 | 活动 / 用例 / 社区 | **含于 L1** | `/use-cases/*`、`/campaign/*`、`/community`、`/canvas` |
| — | 工作台（不索引） | — | `/studio/*` · robots Disallow |
| — | 旧路径 / 未收录 | — | `/apps`（200）、`/explore`、`/assets`（404） |

> **口径**：381 = 25 核心 + 23 模型 slug + 74 Blog 文章 + 259 Apps（5 hub + 254 工具）。`/models`、`/models/rankings` 计入 L1；23 个模型 slug 计入 L3。

---

## L1 核心营销页（25）

| 路径 | 说明 | 导航位置 | lastmod |
|------|------|----------|---------|
| `/` | 首页 / 主转化 | Logo · Home | 2026-06-18 |
| `/ai-image-generate` | AI 生图 | Image 下拉 · Create Image | 2026-06-09 |
| `/ai-image-editor` | AI 修图 | Image 能力 hub | 2026-06-09 |
| `/ai-video-generate` | AI 生视频 | Video 下拉 · Create Video | 2026-06-09 |
| `/ai-video-motion-control` | 动作控制 | Video 下拉 · 首页快捷卡 | 2026-06-09 |
| `/ai-video-editor` | AI 视频编辑 | Video 下拉 | 2026-06-09 |
| `/ai-video-extender` | AI 视频延长 | Video 下拉 | 2026-06-09 |
| `/models` | 模型目录 | 主导航 Models 入口 | 2026-06-09 |
| `/models/rankings` | 模型排行 | Models 子页 | 2026-06-09 |
| `/blog` | Blog 索引 | 页脚 / 内容营销 | 2026-06-18 |
| `/ai-tools` | 工具主目录（新） | 主导航 Tools | 2026-06-17 |
| `/ai-effects` | 特效主目录（新） | 主导航 Effects | 2026-06-17 |
| `/pricing` | 定价 | 顶栏 -30% · 页脚 | 2026-03-20 |
| `/privacy` | 隐私政策 | 页脚 | 2026-02-14 |
| `/terms` | 服务条款 | 页脚 | 2026-02-14 |
| `/community` | 社群作品墙 | 主导航 Community | 2026-06-18 |
| `/canvas` | Canvas 产品 | 主导航 Canvas · 首页模块 | 2026-06-08 |
| `/use-cases` | Use Cases 索引 | 首页 Built for creators | 2026-06-09 |
| `/use-cases/marketing-teams` | 营销团队 | Use Cases 子页 | 2026-06-09 |
| `/use-cases/indie-filmmakers` | 独立电影人 | Use Cases 子页 | 2026-06-09 |
| `/use-cases/ecommerce` | 电商 | Use Cases 子页 | 2026-06-09 |
| `/use-cases/social-creators` | 社交创作者 | Use Cases 子页 | 2026-06-09 |
| `/use-cases/designers` | 设计师 | Use Cases 子页 | 2026-06-09 |
| `/use-cases/agencies` | 代理商 | Use Cases 子页 | 2026-06-09 |
| `/campaign/world-cup-2026` | 世界杯 Campaign | 时令 landing | 2026-06-12 |

---

## L2 产品能力页

### 2.1 AI 能力 Hub（6 · sitemap 收录）

旧导航 **Image / Video** 单页已拆分为以下独立 hub（详见 [vofy-keywords.md §3.2](./vofy-keywords.md)）：

| 能力 | 路径 | 旧导航映射 |
|------|------|------------|
| AI 生图 | `/ai-image-generate` | Image → Create Image |
| AI 修图 | `/ai-image-editor` | Image → Inpaint / Edit |
| AI 生视频 | `/ai-video-generate` | Video → Create Video |
| 动作控制 | `/ai-video-motion-control` | Video → Motion Control |
| AI 视频编辑 | `/ai-video-editor` | Video → Video Edit |
| AI 视频延长 | `/ai-video-extender` | Video → Video Extend |

### 2.2 工作台 `/studio/*`（不索引）

| 用途 | 路径示例 | SEO 状态 |
|------|----------|----------|
| 图像生成 | `/studio/create/image?mode=create&model=gpt-image-2` | robots **Disallow** |
| 图像编辑 / Inpaint | `/studio/edit/image` | robots **Disallow** |
| 视频生成 | `/studio/create/video?mode=create` | robots **Disallow** |
| 动作控制 | `/studio/create/video?mode=motion-control` | robots **Disallow** |
| Canvas 工作台 | `/studio/canvas/projects` | robots **Disallow** |
| 历史 / Assets | `/studio/history` | robots **Disallow**（导航「Assets」实际指向此处） |

首页 **WHAT'S NEW** 轮播仍链至 `/studio/create/...` 带 `model=` 参数；SEO canonical 应指向对应 `/models/{slug}` 或能力 hub。

---

## L3 模型（`/models` + 23 slug）

路径规则：**扁平 slug**（如 `/models/sora-2`），**非** `/models/sora/2`（旧形态 404）。

| 路径 | 说明 | lastmod |
|------|------|---------|
| `/models` | 模型聚合目录 | 2026-06-09 |
| `/models/rankings` | 模型排行 hub | 2026-06-09 |
| `/models/seedance-2.0` | Seedance 2.0 AI Video Generator | 2026-04-03 |
| `/models/seedance-2.0-fast` | Seedance 2.0 Fast AI Video Generator | 2026-06-09 |
| `/models/seedance-1.5-pro` | Seedance 1.5 Pro AI Video Generator | 2025-12-16 |
| `/models/seedream-4.5` | Seedream 4.5 AI Image Generator | 2025-12-03 |
| `/models/seedream-5.0-lite` | Seedream 5.0 Lite AI Image Generator | 2026-03-12 |
| `/models/nano-banana-pro` | Nano Banana Pro AI Image Generator | 2026-03-12 |
| `/models/nano-banana-1.0` | Nano Banana AI Image Generator | 2025-08-26 |
| `/models/nano-banana-2` | Nano Banana 2 AI Image Generator | 2026-03-12 |
| `/models/gpt-image-1.5` | GPT Image 1.5 AI Image Generator | 2026-03-12 |
| `/models/gpt-image-2` | GPT Image 2 AI Image Generator | 2026-04-22 |
| `/models/kling-2.6` | Kling 2.6 AI Video Generator | 2026-06-09 |
| `/models/kling-3.0` | Kling 3.0 AI Video Generator | 2026-03-12 |
| `/models/kling-2.6-motion-control` | Kling 2.6 Motion Control | 2026-05-22 |
| `/models/kling-3.0-motion-control` | Kling 3.0 Motion Control | 2026-05-22 |
| `/models/sora-2` | Sora 2 & Sora 2 Pro AI Video Generator | 2025-09-30 |
| `/models/sora-2-pro` | Sora 2 Pro AI Video Generator | 2026-05-27 |
| `/models/veo-3.1` | Veo 3.1 & Veo 3.1 Fast | 2026-03-11 |
| `/models/veo-3.1-fast` | Veo 3.1 Fast AI Video Generator | 2026-06-09 |
| `/models/veo-3.1-lite` | Veo 3.1 Lite AI Video Generator | 2026-04-02 |
| `/models/grok-imagine-image-1.0` | Grok Imagine Image | 2026-05-22 |
| `/models/grok-imagine-image-quality` | Grok Imagine Image Quality | 2026-05-07 |
| `/models/grok-imagine-image-pro` | Grok Imagine Image Pro | 2026-05-07 |
| `/models/grok-imagine-video-1.0` | Grok Imagine Video | 2026-03-30 |

> ⚠️ 首页 WHAT'S NEW 部分卡片仍使用旧路径（如 `/models/gpt-image/2`、`/models/seedance/2.0`），与 sitemap 扁平 slug 不一致，需工程侧修复内链。

---

## L4 Apps（259）

### 4.1 `/apps` vs `/ai-tools` vs `/ai-effects`

| 维度 | `/apps` | `/ai-tools` + `/ai-effects` |
|------|---------|----------------------------|
| 现网状态 | ✅ 200 | ✅ 200 |
| Sitemap | ❌ 不在 | ✅ 在（lastmod 2026-06-17） |
| 定位 | 旧版「All AI Creative Tools」聚合页 | **新版主目录** — Tools / Effects 分流 |
| Hub 子页 | 5 个 `/apps/image-*` **在 sitemap** | 与 hub 内容可能重叠，需确认 canonical |
| SEO 建议 | 301 → `/ai-tools` 或加入 sitemap | 作为工具类目 **primary landing** |

### 4.2 Apps 类目 Hub（5）

| Hub | 路径 | 说明 | lastmod |
|-----|------|------|---------|
| Image Editing | `/apps/image-editing` | 去背、修图、放大、清理等实用编辑 | 2026-06-17 |
| Image Effects | `/apps/image-effects` | 叠加、光效、模糊、创意特效 | 2026-06-17 |
| Image Filters | `/apps/image-filters` | 一键滤镜、美颜、发色等预设 | 2026-06-17 |
| Image Generators | `/apps/image-generators` | 角色、图形、设计素材生成 | 2026-06-17 |
| Image Styles | `/apps/image-styles` | 完整艺术风格与视觉语言转换 | 2026-06-17 |

### 4.3 `/apps` 聚合页 IA（目录行为 · 2026-06-22 观察）

引用页标题：**All AI Creative Tools & Apps | Vofy**。抓取时约 **254** 条工具（较旧文档 108 条已大幅扩容）。

| Tab / 分区 | 说明 |
|------------|------|
| **All** | 全部工具汇总 |
| **Featured** | 首页级推荐（首页「New effects & tools」与 Featured 联动） |
| **Image / Video** | 按媒体形态二次筛选 |

**Featured Video 示例**（首页 Hot effects / 旧文档保留）：

- Pet Fake-Sleeps With a Phone Video Generator → `/apps/pet-fake-sleeps-with-a-phone-video-generator`
- Anime Live2D Video Generator → `/apps/anime-live2d-video-generator`
- AI Camera Movement Effect → `/apps/ai-camera-movement-effect`
- Live Photo Maker → `/apps/live-photo-maker`
- Memory Motion Video Generator → `/apps/memory-motion-video-generator`
- AI Money Rain Video Generator → `/apps/ai-money-rain-video-generator`
- AI Kissing Video Generator → `/apps/ai-kissing-video-generator`
- AI Hugging Video Generator → `/apps/ai-hugging-video-generator`

**Image 子类规模**（站内宣称，会随上新变化；程序化 SEO 应定期 reconcile）：

| 子类（英文） | 规模（约） | 对应 Hub |
|--------------|-----------|----------|
| Effects | ~19+ | `/apps/image-effects` |
| Outfit & Hair | ~18+ | `/apps/image-filters` |
| Face & Body | ~13+ | `/apps/image-filters` |
| Anime | ~7+ | `/apps/image-styles` |
| Photoshoot | ~6+ | `/apps/image-generators` |
| Headshots | ~5+ | `/apps/image-generators` |
| Cleanup | ~10+ | `/apps/image-editing` |
| Art / Character / Design | 各 ~7–8+ | `/apps/image-styles` / `image-generators` |

**代表性单工具聚类**（节选 · 用作内容聚类，完整 slug 见附录）：

- **Effects**：`color-splash`、`add-hearts-to-photo`、`emoji-filter`、`ghost-filter`、`image-blender`
- **Outfit & Hair**：`hair-color-filter`、`grey-hair-filter`、`pixie-cut-filter`、`blonde-hair-filter`、`beard-filter`
- **Face & Body**：`black-eye-filter`、`blue-eye-filter`、`fat-to-fit`、`braces-filter`
- **Anime**：`90s-anime-filter`、`family-guy-art-style`、`rick-and-morty-art-style`、`ai-pokemon-generator`、`chibi-maker`
- **Photoshoot**：`ai-pin-up-generator`、`80s-grain-filter`、`golden-hour-filter`、`rainbow-air-filter`、`old-camera-filter`
- **Headshots**：`ai-generated-man`、`ai-photo-id`、`dating-profile-photos`、`ai-generated-yearbook`、`linkedin-headshot-generator`
- **Cleanup**：`remove-lens-flare`、`photo-color-correction`、`remove-shadow-from-photo`、`face-cut-out`、`remove-sticker-from-photo`
- **Art / Character / Design**：`pop-art-filter`、`ai-style-transfer`、`digital-art-styles`、`cinematic-art`、`random-cartoon-generator`、`ai-disney-poster`、`animal-hybrid-generator`、`monster-generator`、`ai-sprite-generator`、`stained-glass-generator`、`doodle-font-generator`、`ai-cad-drawing-generator`、`mandala-generator`、`coat-of-arms-generator`

### 4.4 单工具 slug 附录（254）

完整清单来源：[sitemap.xml](https://www.vofy.art/sitemap.xml)。下表按 slug 字母序，每行 4 列：

| slug | slug | slug | slug |
|------|------|------|------|
| 80s-grain-filter | 90s-anime-filter | abstract-art-generator | add-bokeh |
| add-hearts-to-photo | add-noise-to-image | add-santa-hat-to-photo | add-watermark |
| ai-action-figure-generator | ai-age-generator | ai-angel | ai-beauty-filter |
| ai-bikini-generator | ai-braids | ai-breast-expansion | ai-cad-drawing-generator |
| ai-camera-movement-effect | ai-character-generator | ai-disney-poster | ai-face-expression-changer-free |
| ai-fashion-collage-poster-generator | ai-football-jersey-poster-maker | ai-generated-man | ai-generated-yearbook |
| ai-giant-soccer-stadium-effect | ai-halloween-filter | ai-hugging-video-generator | ai-kissing-video-generator |
| ai-money-rain-video-generator | ai-nail-art | ai-outfit-try-on | ai-person-generator |
| ai-pet-portrait-generator-free | ai-photo-id | ai-pin-up-generator | ai-pokemon-generator |
| ai-portrait-background-generator | ai-portrait-generator | ai-product-background-generator | ai-selfie-with-celebrity |
| ai-sprite-generator | ai-style-transfer | ai-tattoo-generator | ai-woman-generator |
| album-cover-maker | american-gothic-art | animal-hybrid-generator | anime-background-generator |
| anime-live2d-video-generator | art-nouveau-style | attack-on-titan-art | autumn-heart-style |
| baby-filter | bald-filter | bangs-filter | barbie-filter |
| beard-filter | birthday-polaroid-photo-maker | black-eye-filter | black-hair-filter |
| bleach-art-style | blemish-remover | blonde-hair-filter | blue-eye-filter |
| blur-image | body-editor | bold-glamour-filter | boondocks-filter |
| braces-filter | brat-generator | buzzcut-filter | cartoon-to-realistic-ai |
| change-background-color | change-color-of-image | change-photo-background | charcoal-sketch |
| chibi-maker | chinese-art-styles | cinematic-art | cinematic-flash-effect |
| clip-art-generator | coat-of-arms-generator | color-splash | colored-pencil-portrait |
| compress-image | crop-image | curly-hair-filter | cyberpunk-style |
| daidai-dance-video-generator | dating-profile-photos | demon-slayer-art | digital-art-styles |
| disney-style | dog-dad-card-maker | dollar-engraving-style | doodle-font-generator |
| double-chin-remover | double-exposure-effect | dragon-ball-art-style | dreamcore-filter |
| duotone-effect | emoji-filter | engagement-photos | expand-image |
| eye-bag-remover | eye-color-change | eyebrow-filter | eyelash-filter |
| face-cut-out | face-shape-filter | face-slimmer | face-swap |
| family-guy-art-style | fantasy-art-generator | fashion-magazine-cover | fat-filter |
| fat-to-fit | favorite-team-goal-hug-video-generator | film-grain-filter | first-fathers-day-card-maker |
| flip-image | funko-pop-yourself | funny-dad-legend-card-maker | funny-face-filter |
| ghibli-style | ghost-filter | glitch-effect | golden-hour-filter |
| graduation-photo | graffiti-art-generator | green-screen-remover | grey-hair-filter |
| hair-color-filter | halloween-background | hello-kitty-creator | image-blender |
| image-enhancer | image-tinter | image-to-emoji-converter | impressionist-style |
| ink-wash-style | japanese-street-interview-video-generator | jawline-enhancement | jojo-art-style |
| jujutsu-kaisen-art | kawaii-filter | light-leaks | linkedin-headshot-generator |
| liquify-effect | live-photo-maker | logo-remover | long-hair-filter |
| luxury-birthday-number-poster-maker | makeup-filter | mandala-generator | manga-art-style |
| meat-heist-video-generator | memory-motion-video-generator | mermaid-filter | mirror-image-generator |
| monster-generator | mugshot-filter | naruto-japanese-style-ai | native-american-art |
| negative-image | neon-style | no-beard-filter | notebook-doodle-style |
| old-camera-filter | old-filter | pastel-effect | pet-fake-sleeps-with-a-phone-video-generator |
| photo-color-correction | photo-to-3d-model | photo-to-art | photo-to-ascii-art |
| photo-to-cartoon | photo-to-clay | photo-to-coloring-page | photo-to-illustration |
| photo-to-lego | photo-to-oil-painting | photo-to-pixel-art | photo-to-vector-art-converter |
| photo-to-watercolor | photos-to-canvas-art | piercing-filter | pink-hair-filter |
| pixelate-image | pixie-cut-filter | png-maker | pokemon-trainer-generator |
| pop-art-filter | premium-editorial-portrait | ps2-filter | rainbow-air-filter |
| random-cartoon-generator | red-eye-remover | relight-photo | remove-background |
| remove-color-from-image | remove-lens-flare | remove-object | remove-people-from-photos |
| remove-shadow-from-photo | remove-sticker-from-photo | remove-text-from-photo | remove-watermark |
| renaissance-portrait | replace-background | resize-image | restore-old-photo |
| retouch-portraits | rick-and-morty-art-style | short-hair-filter | shots |
| silhouette-maker | silver-hair-filter | simpsons-character-creator | skin-color-changer |
| skin-enhancer | south-park-character-creator | stadium-fan-photo-generator | stained-glass-generator |
| stencil-maker | straight-hair-filter | street-fashion-portrait-generator | super-dad-poster-maker |
| superhero-generator | swimsuit-try-on | symbol-generator | teal-and-orange-cinematic-portrait |
| teeth-whitening-filter | text-to-brainrot | through-the-water-style | tilt-shift-effect |
| turn-photo-into-line-drawing | tv-football-player-video-generator | unblur-image | underwater-portrait-generator |
| unpixelate-image | upscale-image | urban-reflection-portrait-generator | vhs-retro-effect |
| vignette-effect | waist-slimmer | wolf-cut-filter | word-art-generator |
| world-cup-crowd-cam-video-generator | world-cup-free-kick-video-generator | world-cup-heart-cam-video-generator | world-cup-live-crowd-cam-video-generator |
| world-cup-player-poster-maker | wrinkle-remover |

---

## L5 Blog（75）

| 路径 | 说明 | lastmod |
|------|------|---------|
| `/blog` | Blog 索引 | 2026-06-18 |

**74 篇文章 slug**（字母序 · 完整主题聚类见 [vofy-blog-inventory-zh.md](./vofy-blog-inventory-zh.md)）：

| slug | slug | slug | slug |
|------|------|------|------|
| 10-best-prompts-photorealistic-ai-portraits | ai-art-styles | ai-baby-face-photo-generator | ai-camera-movement-effect-guide |
| ai-celebrity-selfie-generator | ai-couple-photoshoot-generator-romantic-photos | ai-green-screen-remover-guide | ai-haircut-virtual-try-on |
| ai-hugging-video-generator-guide | ai-kissing-video-generator-from-photos | ai-money-rain-video-generator | ai-ninja-outfit-generator |
| ai-skin-color-changer | ai-skin-enhancer-portrait-retouching-guide | ai-south-park-character-creator-guide | ai-tankini-swimsuit-try-on |
| anime-live2d-video-generator-guide | april-fools-ai-prank-ideas-photos-videos | barbie-filter-pink-aesthetic-guide | best-kling-3-0-prompts |
| best-kling-3-0-settings | birthday-poster-ideas-ai | cartoon-to-realistic-ai-transformation-guide | dog-dad-card-maker-guide |
| doodle-font-generator-spring-2026 | easter-ai-image-prompts-bunnies-eggs-cards | easter-church-graphics-holy-week | edit-images-with-gpt-image-2 |
| fashion-magazine-cover-from-photo | fathers-day-ai-card-poster-ideas | first-fathers-day-card-from-photo | ghibli-style-image-generator-guide |
| gpt-image-2-guide | gpt-image-2-prompts-guide | gpt-image-2-vs-midjourney-comparison | gpt-image-2-vs-nano-banana |
| how-to-animate-old-photos-into-gentle-memory-videos | how-to-change-eye-color-ai | how-to-change-face-expression-with-ai | how-to-create-photorealistic-product-images-nano-banana-2 |
| how-to-remove-shadows-from-photos | kling-3-0-complete-guide | kling-3-0-image-to-video-guide | kling-3-0-prompt-examples |
| live-photo-maker-online-guide | mothers-day-ai-image-generator | mothers-day-gpt-image-2-product-photos | multilingual-mothers-day-campaign-ideas |
| multilingual-mothers-day-marketing-assets | nano-banana-2-ecommerce-product-images | nano-banana-2-education-storytelling-prompts | nano-banana-2-gemini-3-1-flash-image-generation |
| nano-banana-2-photorealistic-image-generation | nano-banana-2-prompt-social-media-viral-guide | nano-banana-2-prompts-brand-marketing | nano-banana-2-vs-seedream-5-comparison |
| nanobanana-2-creative-experimental-prompts | nanobanana-2-prompts-complete-guide | nanobanana-2-trump-image-generation-guide | no-beard-filter-ai-guide |
| old-camera-filter-vintage-photo-generator | pet-fake-sleep-phone-video | photo-to-line-drawing | piercing-filter-virtual-try-on-guide |
| remove-color-from-image | rick-morty-art-style-guide | seedance-2-character-stability-basics | seedance-2-consistent-character-advanced-guide |
| seedance-2-prompt-guide-playbook | selfie-to-linkedin-headshot | vintage-pin-up-art-generator-guide | warm-sunset-glow-photography-ai |
| why-ai-images-look-fake-photorealistic-solutions | world-cup-ai-ideas |

**主题簇**（代表 URL · 详见 [vofy-keywords.md §五](./vofy-keywords.md)）：Seedance 2 · Kling 3.0 · GPT Image 2 · Nano Banana 2 · App How-To（视频/图像）· 风格指南 · Father's/Mother's Day · World Cup 2026 · 对比选购 · 人像摄影。

---

## L6 活动 / 用例 / 社区

| 路径 | 说明 | 导航 / 入口 | sitemap |
|------|------|-------------|---------|
| `/use-cases` | Use Cases 索引 | 首页 Built for creators | ✅ |
| `/use-cases/marketing-teams` | 营销团队 | 首页卡片 | ✅ |
| `/use-cases/indie-filmmakers` | 独立电影人 | 首页卡片 | ✅ |
| `/use-cases/ecommerce` | 电商 | 首页卡片 | ✅ |
| `/use-cases/social-creators` | 社交创作者 | 首页卡片 | ✅ |
| `/use-cases/designers` | 设计师 | 首页卡片 | ✅ |
| `/use-cases/agencies` | 代理商 | 首页卡片 | ✅ |
| `/campaign/world-cup-2026` | 世界杯时令 Campaign | 营销 landing · 联动 Apps/Blog | ✅ |
| `/community` | 社群作品墙 · UGC 展示 | 主导航 Community · 首页 Trending | ✅ |
| `/canvas` | Canvas 协作画布产品页 | 主导航 Canvas · 首页模块 | ✅ |

---

## 导航结构（现网 2026-06-22）

| 区域 | 项 | 目标 URL | 备注 |
|------|-----|----------|------|
| 品牌 | Logo **VOFY** | `/` | — |
| 主导航 | Home | `/` | — |
| 主导航 | **Image** ▾ | `/ai-image-generate` | 下拉：Create Image、Inpaint（→ `/studio/edit/image`）、模型快捷入口 |
| 主导航 | **Video** ▾ | `/ai-video-generate` | 下拉：Create Video、Motion Control、Video Edit、Video Extend、模型快捷入口 |
| 主导航 | **Canvas** | `/studio/canvas/projects` | 产品页 `/canvas` 为营销着陆 |
| 主导航 | **Effects** ▾ | `/ai-effects` | All Image/Video Effects |
| 主导航 | **Tools** ▾ | `/ai-tools` | All Image Tools + 5 Apps hub 入口 |
| 主导航 | **Community** | `/community` | — |
| 主导航 | **Assets** | `/studio/history` | 非 `/assets`（已 404） |
| 顶栏 | **-30%** | `/pricing` | 时令促销横幅 |
| 外链 | Discord | 站外 | 社群心智 |
| ~~已下线~~ | ~~Explore~~ | `/explore` | ❌ **404** · 替代：`/` 或 `/ai-tools` |
| ~~已下线~~ | ~~Assets 旧路径~~ | `/assets` | ❌ **404** · 导航 Assets 已改指 `/studio/history` |

**Image / Video 下拉内模型快捷入口**均链至 `/models/{slug}`（扁平路径）。部分 **SOON** 项（Upscale、Remove Background、Lipsync）暂指向 `#`。

---

## 首页模块（IA 顺序）

1. **Hero**：「Fresh effects. Latest models. Ready to create.」+ 主画布（模型选型、Credits 预估、Create）
2. **快捷跳转卡**：Create Video · Create Image · Effects · Motion Control · Inpaint Image
3. **New effects & tools every week**：横向 Featured 工具卡（链至 `/apps/{slug}`）— 当前含 Father's Day、Birthday、World Cup 等时令工具
4. **Hot effects / Trending creations**：热门特效瀑布流
5. **Fresh viral video effects**：视频特效推广 → `/ai-effects`
6. **Canvas for bigger creative ideas** → `/canvas`
7. **Built for creators and creative teams**：6 张 Use Cases 卡 → `/use-cases/{slug}`
8. **How it works**：三步流程（选 effect → 加素材/prompt → 生成分享）
9. **Questions creators ask first**：FAQ 折叠（Vofy 是什么、模型、Apps、Credits 等）
10. **WHAT'S NEW**（页脚区）：模型轮播 → `/models/{slug}` 或 `/studio/create/...`
11. **COMMUNITY**：筛选 All / Image / Video + 瀑布流（handle、prompt 节选）→ `/community`

---

## 不在 sitemap 但存在的页面

| URL | 状态 | SEO 含义 |
|-----|------|----------|
| `/apps` | ✅ 200 · robots Allow | 旧版工具聚合索引；**未列入 sitemap**；主目录已迁移至 `/ai-tools`、`/ai-effects` |
| `/studio/*` | ✅ 需登录 | robots **Disallow** · 正确排除 |
| `/explore` | ❌ 404 | 旧导航项，已下线 |
| `/assets` | ❌ 404 | 旧导航项；现网「Assets」改链 `/studio/history` |
| `/tools/*` | ❌ 404 | 旧路径，已迁移至 `/apps/{slug}` |
| `/models/{vendor}/{version}` | ❌ 404 | 旧模型路径，已扁平化为 `/models/{slug}` |
| `/p/*`、`/u/*`、`/c/*`、`/share/*` | 部分可访问 | UGC 分享页 · 不在 sitemap |

---

## 内容机会（与结构挂钩）

| 模块 | 机会 |
|------|------|
| **What's New → `/studio`** | 每模型一篇中英文短攻略；canonical 指向 `/models/{slug}` |
| **`/apps` 类目 hub** | 为每个子类做 pillar 页，下挂内链至子工具 |
| **Community** | 每周精选 + 「复制同款 prompt/Credits」运营；增加 E-E-A-T |
| **Use Cases / Campaign** | 行业落地页 ↔ Apps/Blog 双向内链 |
| **合规** | 对身体/亲密类工具增设可读使用边界 |

---

## 快速修复观察项（信任 / SEO）

- 首页 WHAT'S NEW 部分仍含旧模型路径（`/models/gpt-image/2` 等）— 应统一为扁平 `/models/{slug}`。
- 「254 / 100+」工具计数需在 `/apps`、`/ai-tools`、meta 描述间保持一致。
- 大量工具共用相似 meta 时需模版化区分 Title（工具名靠前 + 「Online | Vofy」）。
- `/apps` vs `/ai-tools` canonical 策略待明确（见 [vofy-sitemap-optimization-zh.md §2.1 问题 5](./vofy-sitemap-optimization-zh.md)）。

---

## 维护说明

| 触发 | 动作 | 关联文档 |
|------|------|----------|
| 每次部署 | 核对 sitemap 生成、新增 URL 入库 | [vofy-sitemap-optimization-zh.md](./vofy-sitemap-optimization-zh.md) |
| 新增 Apps / Blog / 模型 | 更新本文 slug 附录 + `vofy-keywords.md` URL 映射 | [vofy-keywords.md](./vofy-keywords.md) |
| 导航改版 | 更新「导航结构」与 L1 表格「导航位置」列 | 本文 |
| 每月 | 全量 sitemap 审计：404、lastmod、计数 reconcile | sitemap 文档 §七 |
| Apps 上新 | reconcile `/apps` 子类计数与 Featured 列表 | [apps/01-vofy-style-effect-filter-framework-zh.md](./apps/01-vofy-style-effect-filter-framework-zh.md) |

> 建议以 `curl https://www.vofy.art/sitemap.xml` 或 Python 脚本定期导出 slug 清单，与本文附录 diff 后更新。

---

*基于 2026-06-22 现网 sitemap 全量导出（381 URL）· 非 Demo 推断*