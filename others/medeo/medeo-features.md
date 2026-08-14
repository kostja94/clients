# Medeo Features 功能页总结

> **本文档职责**：100+ AI 视频生成器、功能分类、Benefit、URL、目标关键词；链至 Use Cases、**严格区分**视频模板。  
> **引用**：[medeo.md](./medeo.md) 产品概览 | [medeo-templates.md](./medeo-templates.md) 视频模板（差异化） | [medeo-use-cases.md](./medeo-use-cases.md) 场景 | [medeo-keywords.md](./medeo-keywords.md) 关键词

**Medeo 为 AI Video Agent**：理解意图→规划工作流→自主执行（脚本、配音、画面、剪辑）→支持迭代优化。100+ 生成器按任务/场景调用，区别于单次 prompt 的简单生成器。*详见 [medeo.md](./medeo.md) §产品定位。*

**核心功能页与视频模板严格区分**：

| 类型 | 路径 | 回答的问题 | 示例 | 与模板的差异 |
|------|------|------------|------|--------------|
| **Video Generator** | /video-generator/{slug} | 从什么**输入**生成视频？ | ai-meme、explainer、tutorial、ugc-ads | 生成器 = 能力/工作流；模板 = 预设风格/结构 |
| **Xxx to Video** | /features/{slug} | 从什么**格式**转为视频？ | blog-to-video、script-to-video、image-to-video | 转化 = 输入→输出；模板 = 即用风格套用 |
| **B-Roll / 工具** | /features/{slug} | 为视频**添加/增强**什么？ | b-roll-generator、subtitle-generator | 工具 = 增强现有视频；模板 = 从零套用风格 |
| **Video Templates** | /video-templates/{slug} | 用什么**风格/结构**？ | brand-film、clay-animation、love-story | 模板 = 即用预设；生成器 = 自定义输入生成 |

*详见 [medeo-templates.md](./medeo-templates.md) §核心功能页与视频模板的区分。功能页与模板页**互相引用**，避免内容蚕食。*

**关键词与内容区分（避免与 Templates 重叠）**：

| 维度 | Video Generator / Features | Video Templates |
|------|----------------------------|-----------------|
| **主关键词后缀** | **generator**、AI X video、X to video、create X video | template、X style template |
| **避免使用** | 不用 template、style、preset | 不用 generator |
| **内容聚焦** | 输入→输出、工作流、能力 | 风格、结构、适用场景 |
| **示例** | explainer **video generator**、**AI** tutorial video、**meme** video **generator** | explainer **template**、tutorial **style template** |

*功能页 title/meta 应含 `generator` 或 `AI X video`，不主推 `template`；模板页主推 `template`，不主推 `generator`。*

---

## 一、功能分类概览（6 大类）

| 分类 | 说明 | 代表功能 | 目标关键词（含 generator，避免 template） |
|------|------|----------|------------------------------------------|
| **Entertainment & Gaming** | 动漫、游戏、创意粉丝内容 | Minecraft、Anime、Brainrot、Reaction、Genshin | anime video generator, meme video generator, gaming clip AI |
| **Social & Lifestyle** | 病毒趋势、Vlog、社交 | Meme、Vlog、Travel、Pet、Fashion Reels | meme video generator, AI vlog maker, pet video generator |
| **Marketing & Business** | 品牌、产品、专业身份 | B-Roll、UGC Ads、Product Ad、Spokesperson | B-roll generator, UGC ad video AI, product ad generator |
| **Education & How-To** | 教程、课程、解说 | Explainer、Tutorial、Training、Subtitle | AI explainer video, tutorial video generator, training video generator |
| **Content Repurposing** | 文本/链接/文件→视频 | Blog、Script、PDF、Slides、URL、Tweet、Podcast | blog to video, script to video |
| **Special Moments & Vibes** | 节日、氛围、个人时刻 | Birthday、Wedding、Christmas、Meditation | AI birthday video, meditation video |

*Sitemap 来源：[medeo.app/sitemap.xml](https://www.medeo.app/sitemap.xml) — 约 230+ URL（features 40+、video-generator 120+、video-templates 70+）*

---

## 二、Video Templates（视频模板，70+）— 与核心功能页严格区分

> **差异化**：模板 = 即用风格/结构，一键套用；**非**生成器（/video-generator）或转化（/features/xxx-to-video）。  
> **程序化 SEO**：详见 [medeo-templates.md](./medeo-templates.md)。

| 类别 | 示例模板 | 目标关键词（含 template） | 对应 Generator（避免重叠） |
|------|----------|---------------------------|----------------------------|
| Brand & Marketing | brand-film、brand-pop-up、product-explainer-film | AI brand video template | product-ad generator |
| Animation Style | 2d-animation、clay-animation、papercut-animation | clay animation template, 2D animation template | photo-to-claymation |
| Product & Explainer | product-hero-film、ppt-video、line-art-explainer | product video template, PPT to video template | slides-to-video, explainer |
| Emotion & Holiday | love-story、valentines-day、christmas、birthday | AI love story video template, Valentine video template | — |
| Atmosphere & Vibe | cinematic-film、lofi-vibe、dreamy、meditation-visual | cinematic video template | — |
| Gaming & Entertainment | pixel-game、anime-short-film、anime-mv | pixel game video template, anime video template | anime video generator |
| Creative & Meme | myth-meme、scary-story、superhero-gone-wrong | meme video template, horror video template | meme video generator |
| Lifestyle & Pet | pet-podcast、mukbang-vlog、food-ball | AI pet video template | pet video generator |

*路径：`/video-templates/{slug}`。模板页应链至相关**生成器**（如 brand-film → b-roll-generator、product-explainer）、**Xxx to Video**（如 ppt-video → slides-to-video）及**相关模板**（如 brand-film → product-explainer-film）。注意：product-explainer-film 为模板；product-explainer 为生成器，路径不同。*

---

## 三、Content Repurposing（核心转化能力）

| 功能 | URL | Benefit | 目标关键词 |
|------|-----|---------|------------|
| **Blog to Video** | /features/blog-to-video | 博客→自动脚本、配音、剪辑 | blog to video AI, blog to video converter |
| **Script to Video** | /features/script-to-video | 脚本→AI 主持人、口型同步 | script to video AI |
| **Image to Video** | /features/image-to-video | 图片→动态视频 | image to video AI |
| **URL to Video** | /features/url-to-video | 网页→旁白视频 | URL to video |
| **Idea to Video** | /features/idea-to-video | 想法→视频 | idea to video AI |
| **Slides to Video** | /features/slides-to-video | PPT→动态视频 | slides to video |
| **PDF to Video** | /features/pdf-to-video | PDF→视频 | PDF to video |
| **Tweet to Video** | /features/tweets-to-video | 推文→病毒视频 | tweet to video |
| **Podcast to Video** | /features/podcast-to-video | 播客→视频 | podcast to video |
| **LinkedIn Post to Video** | /features/linkedin-posts-to-video | LinkedIn→专业视频 | LinkedIn to video |
| **Reddit Threads to Video** | /features/reddit-threads-to-video | Reddit 帖子→故事视频 | Reddit to video |
| **Quote to Video** | /features/quote-to-video | 金句→视频 | quote to video |
| **Transcript to Video** | /features/transcript-to-video | 转录稿→视频 | transcript to video |
| **Taking Photo** | /features/taking-photo | 照片→说话视频 | photo to talking video |
| **Photo to Facial Expression** | /features/photo-to-facial-expression | 照片→表情动画 | photo to expression |
| **Photo to Claymation** | /features/photo-to-claymation | 照片→黏土动画 | photo to claymation |
| **Photo to Dance Video** | /features/photo-to-dance-video | 照片→舞蹈视频 | photo to dance |
| **Couple Portrait to Video** | /features/couple-portrait-to-video | 情侣照→视频 | couple portrait to video |
| **Poetry to Video** | /features/Poetry | 诗歌→儿童视频 | poetry to video |

### Sora 2 系列（/features）

| 功能 | URL | 目标关键词 |
|------|-----|------------|
| Sora 2 to Animation | /features/sora-2-to-animation | Sora 2 animation |
| Picture with Sora 2 | /features/picture-with-sora-2 | Sora 2 image to video |
| Sora Story/Dream/Prompt to Video | /features/sora-story-to-video、sora-dream-to-video、sora-prompt-to-video | Sora 2 video |
| Sora 2 to Video | /features/sora-2-to-video | Sora 2 video generator |

### 业务/营销转化（/features）

| 功能 | URL |
|------|-----|
| Case Study to Video | /features/case-study-to-video |
| Research Paper to Video | /features/research-paper-to-video |
| Online Course to Video | /features/online-course-to-video |
| Product Review to Video | /features/product-review-to-video |
| Ad to Video、Social Media Ad to Video | /features/ad-to-video、social-media-ad-to-video |
| SOP to Video、Proposal to Video、Project Plan to Video | /features/sop-to-video、proposal-to-video、project-plan-to-video |
| Meeting Notes to Video、Job Description to Video | /features/meeting-notes-to-video、job-description-to-video |
| Self Introduction to Video | /features/self-introduction-to-video |
| Data Report、Research Notes、Training Manual to Video | /features/data-report-to-video、research-notes-to-video、training-manual-to-video |
| Facebook/Instagram Post to Video | /features/facebook-post-to-video、instagram-post-to-video |
| Text to Food Video | /features/text-to-food-video |
| Wrong Dreams、Oddities to Video | /features/wrong-dreams-to-video、oddities-to-video |
| Brainrot for Marketing、Italian Brainrot、Stream to Clips | /features/brainrot-for-marketing、italian-brainrot-generator、stream-to-clips |
| Synthetic Reality to Video | /features/synthetic-reality-to-video |

---

## 四、Marketing & Business

| 功能 | URL | Benefit | 目标关键词 |
|------|-----|---------|------------|
| **B-Roll Generator** | /features/b-roll-generator | 为任意视频添加动态 B-Roll | AI B-roll generator |
| **UGC Ads Video** | /video-generator/ugc-ads | 高转化 UGC 广告 | UGC ad video AI |
| **Product Ad Video** | /video-generator/product-ad | 产品广告视频 | AI product ad |
| **AI Spokesperson** | /video-generator/spokesperson | AI 发言人视频 | AI spokesperson video |
| **Talking Avatar** | /video-generator/talking-avatar | 真人感 Talking Avatar | talking avatar AI |
| **Breaking News Video** | /video-generator/breaking-news | 突发新闻视频 | AI news video |

---

## 五、Education & How-To

| 功能 | URL | Benefit | 目标关键词 |
|------|-----|---------|------------|
| **Explainer Video** | /video-generator/explainer | 复杂概念→简单视频 | AI explainer video |
| **Tutorial Video** | /video-generator/tutorial | 专业教程视频 | AI tutorial video |
| **Training Video** | /video-generator/training | 培训材料→视频课程 | AI training video |
| **Subtitle Generator** | /features/subtitle-generator | 任意视频→字幕 | auto subtitle generator |
| **AI Voiceover** | /video-generator/voiceover | 任意视频→AI 配音 | AI voiceover |

---

## 六、Entertainment & Gaming

| 功能 | URL | Benefit | 目标关键词 |
|------|-----|---------|------------|
| **AI Meme Video** | /video-generator/ai-meme | 梗图/趋势→Meme 视频 | AI meme generator |
| **Minecraft to Video** | /features/minecraft-video-generator | 游戏地图→视频 | Minecraft video AI |
| **Anime Video** | /video-generator/anime | 想法→动漫视频 | anime video generator |
| **Reaction Video** | /video-generator/reaction | 专业反应视频 | AI reaction video |
| **Gaming Clip** | /video-generator/gaming-clips | 长直播→病毒剪辑 | gaming clip AI |
| **Seedance 2.0** | /video-generator/seedance-2 | 新一代 AI 视频标准 | Seedance 2.0 |

---

## 七、Social & Lifestyle

| 功能 | URL | Benefit | 目标关键词 |
|------|-----|---------|------------|
| **AI Stock Video** | /feature/ai-stock-video-generator | 文字→电影级素材 | AI stock video generator |
| **Travel Video** | /video-generator/travel | 目的地/旅行 Vlog | AI travel video |
| **Vlog Video** | /video-generator/vlog | 日常→电影感 Vlog | AI vlog maker |
| **Pet Video** | /video-generator/pet | 宠物→可爱 AI 视频 | AI pet video |

---

## 八、内链规划

```
首页 (/)
  ├── /features
  ├── /video-templates（70+ 模板，程序化 SEO 见 [medeo-templates.md](./medeo-templates.md)）
  ├── /features/blog-to-video、/features/script-to-video、/features/image-to-video
  ├── /video-generator/ai-meme、/video-generator/explainer 等
  ├── /creators、/marketers、/educators（Use Cases）
  ├── /pricing、/download（移动端 iOS/Android）、/rewards-help
  ├── /legal、/legal/privacy-policy、/legal/terms-of-use
  └── /signin

各功能页「Explore More」互链：blog-to-video ↔ script-to-video ↔ meme ↔ b-roll
```

**核心功能页 ↔ 视频模板 互相引用**：
- 功能页（blog-to-video、b-roll-generator、explainer 等）→ 链至相关模板（如 /video-templates/ppt-video、line-art-explainer）
- 模板页（/video-templates/*）→ 链至相关功能（如 brand-film → 链至 product-explainer-film、b-roll-generator）
- 避免内容蚕食：功能页讲能力/工作流；模板页讲风格/结构

**Use case links**（链至 Use Cases，不重复场景内容）：
- [For Content Creators](/creators) | [For Marketers](/marketers) | [For Educators](/educators)

**移动端**：手机端创作支持 iOS、Android，[Download](https://www.medeo.app/download)。功能页可链至 Download 供移动端用户获取。

---

## 九、文档导航

→ [medeo.md](./medeo.md) 概览 | [medeo-templates.md](./medeo-templates.md) 模板（程序化 SEO） | [medeo-use-cases.md](./medeo-use-cases.md) 场景 | [medeo-competitors.md](./medeo-competitors.md) 竞品 | [medeo-keywords.md](./medeo-keywords.md) 关键词

**Last updated**：2026-03-02
