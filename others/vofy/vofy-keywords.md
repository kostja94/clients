# Vofy — 关键词与 URL 机会

> 关联：[vofy.md](./vofy.md) | [vofy-site-structure.md](./vofy-site-structure.md) | [vofy-sitemap-optimization-zh.md](./vofy-sitemap-optimization-zh.md) | [apps/01-vofy-style-effect-filter-framework-zh.md](./apps/01-vofy-style-effect-filter-framework-zh.md)

**最近更新**：2026-06-22 · 基于 [现网 sitemap](https://www.vofy.art/sitemap.xml)（381 URL · lastmod 2026-06-18）全量导出

---

## 一、品牌与品类词（英）

| 意图 | 示例关键词 |
|------|------------|
| 品牌 | `Vofy`, `VOFY`, `vofy.art` |
| 品类 | `AI creative studio`, `all-in-one AI image video`, `AI video generator platform`, `AI image generator online`, `multi-model AI studio`, `AI motion control`, `AI inpainting` |
| 模型名（信息型 · 会变） | `Seedance 2.0`, `Veo 3.1 Lite`, `Kling 3.0`, `Sora 2`, `GPT Image 2`, `Nano Banana 2`, `Grok Imagine` |
| Apps 长尾（工具型） | `AI hair color filter online`, `AI yearbook photo`, `LinkedIn headshot AI`, `AI kissing video`, `fake sleep pet video AI`, `color splash photo AI`, `remove lens flare photo AI` |

## 二、中文（内容与投放扩展）

| 意图 | 示例 |
|------|------|
| 品类 | AI 画图网站、一站式 AI 生图生视频、多模型视频生成、积分制 AI 创作 |
| 场景 | 电商主图批量、社交媒体短视频、换装试发色、怀旧老照片动起来 |

---

## 三、目标 URL 映射（2026-06-22 现网验证）

### 3.1 核心着陆页

| 主题 | 路径 | 代表关键词 | 备注 |
|------|------|------------|------|
| 首页 / 主转化 | `/` | `Vofy`, `AI creative studio`, `what do you want to create` | Hero、What's New、Community 入口 |
| **工具主目录（新）** | `/ai-tools` | `AI tools online`, `all AI creative tools` | **sitemap 收录**；lastmod 2026-06-17 |
| **特效主目录（新）** | `/ai-effects` | `AI photo effects`, `AI video effects` | **sitemap 收录**；lastmod 2026-06-17 |
| 工具聚合（旧） | `/apps` | `Vofy apps`, `AI apps` | ✅ 200 · robots Allow · **不在 sitemap**；建议 canonical → `/ai-tools` |
| 单工具页 | `/apps/{slug}` | 见 §3.5 · 254 个工具 | 程序化 SEO 主战场；**无** `/tools/*` 路径 |
| 模型目录 | `/models` | `AI models comparison`, `best AI video model` | 模型聚合 + 内链至各 `/models/{slug}` |
| 模型排行 | `/models/rankings` | `AI model rankings 2026` | 信息型 hub |
| Blog 索引 | `/blog` | `Vofy blog`, `AI image video tutorials` | 74 篇文章索引 |
| 定价 | `/pricing` | `Vofy pricing`, `AI credits pricing` | lastmod 2026-03-20 · 待核实 |
| 社群展示 | `/community` | `Vofy community`, `AI art gallery` | 用户作品墙 |
| 画布产品 | `/canvas` | `Vofy canvas`, `AI canvas editor` | 独立产品模块 |
| 法律 | `/privacy`、`/terms` | — | 信任与广告投放前置 |

### 3.2 AI 能力 Hub（Image / Video 已拆分）

| 能力 | 路径 | 代表关键词 |
|------|------|------------|
| AI 生图 | `/ai-image-generate` | `AI image generator`, `text to image online` |
| AI 修图 | `/ai-image-editor` | `AI photo editor`, `AI inpainting online` |
| AI 生视频 | `/ai-video-generate` | `AI video generator`, `text to video AI` |
| 动作控制 | `/ai-video-motion-control` | `AI motion control video`, `motion transfer AI` |
| AI 视频编辑 | `/ai-video-editor` | `AI video editor online` |
| AI 视频延长 | `/ai-video-extender` | `AI video extender`, `extend video with AI` |

> 旧导航 **Image / Video** 单页已拆为以上 6 个独立 hub，均在 sitemap。

### 3.3 Use Cases · Campaign · 已下线路径

| 主题 | 路径 | 代表关键词 | 状态 |
|------|------|------------|------|
| Use Cases 索引 | `/use-cases` | `AI for marketing teams`, `AI creative use cases` | ✅ sitemap |
| 营销团队 | `/use-cases/marketing-teams` | `AI tools for marketing`, `campaign asset AI` | ✅ |
| 独立电影人 | `/use-cases/indie-filmmakers` | `AI video for filmmakers`, `indie film AI tools` | ✅ |
| 电商 | `/use-cases/ecommerce` | `AI product photos ecommerce`, `AI background remover shopify` | ✅ |
| 社交创作者 | `/use-cases/social-creators` | `AI content creator tools`, `social media AI generator` | ✅ |
| 设计师 | `/use-cases/designers` | `AI design tools`, `AI mockup generator` | ✅ |
| 代理商 | `/use-cases/agencies` | `AI tools for agencies`, `client creative AI workflow` | ✅ |
| 世界杯 Campaign | `/campaign/world-cup-2026` | `World Cup AI photo`, `football fan AI video` | ✅ 时令 landing |
| ~~探索~~ | `/explore` | — | ❌ **404** · 勿再引用 |
| ~~素材库~~ | `/assets` | — | ❌ **404** · 勿再引用 |
| ~~旧工具路径~~ | `/tools/*` | — | ❌ **404** · 已迁移至 `/apps/{slug}` |

### 3.4 `/apps` vs `/ai-tools` 关系

| 维度 | `/apps` | `/ai-tools` + `/ai-effects` |
|------|---------|----------------------------|
| 现网状态 | ✅ 可访问 | ✅ 可访问 |
| Sitemap | ❌ 不在 | ✅ 在（lastmod 2026-06-17） |
| robots.txt | Allow | Allow（通过 `/` Allow） |
| 定位 | 旧版「All AI Creative Tools」聚合页 | **新版主目录**，按 Image / Video / Effects 等分类 |
| Apps hub 子页 | 5 个 `/apps/image-*` hub **在 sitemap** | 与 `/ai-tools` 可能内容重叠，需确认 canonical |
| SEO 建议 | 301 → `/ai-tools` 或 noindex；若保留则加入 sitemap | 作为工具类目的 **primary landing**；内链、面包屑、GSC 监控均以此为准 |

### 3.5 Apps Hub 与单工具（sitemap 259 URL）

**Hub 页（5）**：

| Hub | 路径 | 品类关键词 |
|-----|------|-----------|
| Image Editing | `/apps/image-editing` | `AI photo editing tools`, `online photo editor AI` |
| Image Effects | `/apps/image-effects` | `AI photo effects`, `photo effect filter online` |
| Image Filters | `/apps/image-filters` | `AI photo filters`, `filter photo online free` |
| Image Generators | `/apps/image-generators` | `AI image generator apps`, `AI art generator online` |
| Image Styles | `/apps/image-styles` | `AI art styles`, `photo style transfer online` |

**单工具页（254）**：路径 `/apps/{slug}`。代表 slug 与长尾词（完整清单见 sitemap 导出）：

| slug 示例 | 代表关键词 |
|-----------|-----------|
| `hair-color-filter` | `AI hair color filter`, `virtual hair dye` |
| `linkedin-headshot-generator` | `LinkedIn headshot AI`, `professional headshot generator` |
| `ai-kissing-video-generator` | `AI kissing video from photos` |
| `ai-hugging-video-generator` | `AI hugging video generator` |
| `pet-fake-sleeps-with-a-phone-video-generator` | `pet fake sleep video AI` |
| `memory-motion-video-generator` | `animate old photo AI`, `memory motion video` |
| `remove-background` | `remove background from image free` |
| `color-splash` | `color splash photo effect` |
| `remove-lens-flare` | `remove lens flare from photo` |
| `ai-generated-yearbook` | `AI yearbook photo generator` |
| `world-cup-player-poster-maker` | `World Cup AI poster`, `football fan poster AI` |

### 3.6 工作台（不可索引）

| 主题 | 路径 | 备注 |
|------|------|------|
| 图像工作台 | `/studio/create/image` | `mode`、`model`、`workspace` 查询参数 · robots Disallow |
| 视频工作台 | `/studio/create/video` | `mode=create`、`mode=motion-control` 等 · robots Disallow |
| 社群外链 | Discord | 非站内 SEO 着陆 |

---

## 四、模型关键词 → `/models/{slug}` 映射（23 页）

路径规则：**扁平 slug**（如 `/models/sora-2`），**非** `/models/sora/2`。

| slug | 页面标题（现网 `<title>`） | 代表关键词 |
|------|---------------------------|------------|
| `seedance-2.0` | Seedance 2.0 AI Video Generator | `Seedance 2.0`, `Seedance AI video`, `Seedance 2 prompts` |
| `seedance-2.0-fast` | Seedance 2.0 Fast AI Video Generator | `Seedance 2 Fast`, `fast AI video generation` |
| `seedance-1.5-pro` | Seedance 1.5 Pro AI Video Generator | `Seedance 1.5 Pro`, `Seedance pro video` |
| `seedream-4.5` | Seedream 4.5 AI Image Generator | `Seedream 4.5`, `Seedream AI image` |
| `seedream-5.0-lite` | Seedream 5.0 Lite AI Image Generator | `Seedream 5 Lite`, `Seedream 5.0` |
| `nano-banana-pro` | Nano Banana Pro AI Image Generator | `Nano Banana Pro`, `Gemini image AI` |
| `nano-banana-1.0` | Nano Banana AI Image Generator | `Nano Banana AI`, `Nano Banana image` |
| `nano-banana-2` | Nano Banana 2 AI Image Generator | `Nano Banana 2`, `Nano Banana 2 prompts` |
| `gpt-image-1.5` | GPT Image 1.5 AI Image Generator | `GPT Image 1.5`, `OpenAI image model` |
| `gpt-image-2` | GPT Image 2 AI Image Generator | `GPT Image 2`, `GPT Image 2 vs Midjourney` |
| `kling-2.6` | Kling 2.6 AI Video Generator | `Kling 2.6`, `Kling AI video` |
| `kling-3.0` | Kling 3.0 AI Video Generator | `Kling 3.0`, `Kling 3 prompts`, `best Kling settings` |
| `kling-2.6-motion-control` | Kling 2.6 Motion Control AI Video Generator | `Kling motion control`, `Kling 2.6 motion` |
| `kling-3.0-motion-control` | Kling 3.0 Motion Control AI Video Generator | `Kling 3 motion control` |
| `sora-2` | Sora 2 & Sora 2 Pro AI Video Generator | `Sora 2`, `OpenAI Sora alternative`, `Sora 2 prompts` |
| `sora-2-pro` | Sora 2 Pro AI Video Generator | `Sora 2 Pro`, `Sora pro video` |
| `veo-3.1` | Veo 3.1 & Veo 3.1 Fast AI Video Generator | `Veo 3.1`, `Google Veo AI video` |
| `veo-3.1-fast` | Veo 3.1 Fast AI Video Generator | `Veo 3.1 Fast`, `fast Veo video` |
| `veo-3.1-lite` | Veo 3.1 Lite AI Video Generator | `Veo 3.1 Lite`, `Veo lite video` |
| `grok-imagine-image-1.0` | Grok Imagine Image AI Image Generator | `Grok Imagine image`, `Grok AI image generator` |
| `grok-imagine-image-quality` | Grok Imagine Image Quality AI Image Generator | `Grok Imagine quality`, `Grok image quality mode` |
| `grok-imagine-image-pro` | Grok Imagine Image Pro AI Image Generator | `Grok Imagine Pro`, `Grok image pro` |
| `grok-imagine-video-1.0` | Grok Imagine Video AI Video Generator | `Grok Imagine video`, `Grok video AI` |

---

## 五、Blog 关键词簇（74 篇 · 代表 URL）

| 簇 | 代表 URL | 代表关键词 |
|----|---------|------------|
| **Seedance 2** | `/blog/seedance-2-prompt-guide-playbook` | `Seedance 2 prompts`, `consistent character AI video` |
| **Kling 3.0** | `/blog/kling-3-0-complete-guide` | `Kling 3.0 guide`, `Kling image to video` |
| **GPT Image 2** | `/blog/gpt-image-2-guide` | `GPT Image 2 tutorial`, `GPT Image 2 vs Midjourney` |
| **Nano Banana 2** | `/blog/nano-banana-2-photorealistic-image-generation` | `Nano Banana 2 prompts`, `photorealistic AI image` |
| **App How-To · 视频** | `/blog/ai-kissing-video-generator-from-photos` | `AI kissing video tutorial`, `photo to kissing video` |
| **App How-To · 图像** | `/blog/ai-haircut-virtual-try-on` | `AI virtual haircut`, `hair color try on` |
| **风格指南** | `/blog/ghibli-style-image-generator-guide` | `Ghibli AI filter`, `Studio Ghibli style AI` |
| **Father's Day** | `/blog/fathers-day-ai-card-poster-ideas` | `Father's Day AI card`, `AI dad poster` |
| **Mother's Day** | `/blog/mothers-day-ai-image-generator` | `Mother's Day AI image`, `AI mother's day gift` |
| **World Cup 2026** | `/blog/world-cup-ai-ideas` | `World Cup AI content`, `football fan AI ideas` |
| **对比 / 选购** | `/blog/gpt-image-2-vs-nano-banana` | `GPT Image 2 vs Nano Banana`, `best AI image model` |
| **人像 / 摄影** | `/blog/10-best-prompts-photorealistic-ai-portraits` | `photorealistic AI portrait prompts` |

> 完整 slug 列表见 [sitemap](https://www.vofy.art/sitemap.xml) 或 [vofy-blog-inventory-zh.md](./vofy-blog-inventory-zh.md)。

---

## 六、Canvas · Community · Campaign 关键词簇

| 模块 | URL | 代表关键词 | 内容策略 |
|------|-----|------------|---------|
| **Canvas** | `/canvas` | `Vofy canvas`, `AI canvas workspace`, `collaborative AI art` | 产品功能页；对标 Figma / Canva AI 工作流 |
| **Community** | `/community` | `Vofy community gallery`, `AI art showcase`, `prompt sharing` | UGC 展示；长尾 prompt 词 + 模型标签 |
| **World Cup Campaign** | `/campaign/world-cup-2026` | `World Cup 2026 AI`, `football fan photo AI`, `soccer video AI` | 时令 campaign landing；联动 Apps（如 `world-cup-player-poster-maker`）与 Blog |

---

## 七、待办（SEO / 内容）

- [x] 导出 `/apps` 全量 slug 清单（2026-06-22 从 sitemap 获取 **254** 个工具 + 5 hub）  
- [ ] 抓取 `lastmod`/索引情况，判断是否需独立 `softwareapplication` 或精简 `FAQ`/`HowTo` 策略（对齐 schema 总则）  
- [ ] 明确 `/apps` → `/ai-tools` canonical 并在 GSC 监控重复收录  
- [ ] 「What's New」每条 → 短文 + 内链至对应 `/studio` 预设或 `/models/{slug}`  
- [ ] 对比页：**Vofy vs Leonardo / Runway / Pika** 等须在事实与日期脚注上严谨  
- [ ] 敏感类目（人像、亲密特效）页的 **风险提示与合规** 模块，降低品牌风险  
- [ ] 为 23 个模型页建立 cluster 内链（模型页 ↔ Blog ↔ Apps ↔ Use Cases）

---

*基于 2026-06-22 现网 sitemap 全量导出（381 URL）· 非 Demo 推断*
