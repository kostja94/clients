# Medeo 视频模板（Templates）— 程序化 SEO 核心

> **本文档职责**：视频模板分类、多维度体系、数据 schema、URL 模式、程序化 SEO 模板。**与核心功能页严格区分**，互相引用。  
> **引用**：核心功能页（Video Generator、Xxx to Video、B-Roll）见 [medeo-features.md](./medeo-features.md)；关键词见 [medeo-keywords.md](./medeo-keywords.md)

*来源：[medeo.app/sitemap.xml](https://www.medeo.app/sitemap.xml)、[MindStudio](https://www.mindstudio.ai/blog/ai-video-templates-marketing-campaign-launches)、[Vidrel](https://vidrel.ai/blog/ai-video-formats-driving-crazy-engagement-in-2026)、[ReelMind](https://reelmind.ai/blog/smart-video-format-conversion-perfect-aspect-ratios-for-all-platforms)*

---

## 0. 核心功能页与视频模板的区分

> **严格区分**：Video Generator、Xxx to Video、B-Roll Generator 为**核心功能页**；Video Templates 为**即用风格模板**。二者有差异性，需互相引用。

| 类型 | 路径 | 定位 | 示例 |
|------|------|------|------|
| **Video Generator** | /video-generator/{slug} | 从输入（文本/图片/想法）**生成**视频 | ai-meme、explainer、tutorial、ugc-ads、spokesperson |
| **Xxx to Video** | /features/{slug} | 从某格式**转化**为视频 | blog-to-video、script-to-video、image-to-video |
| **B-Roll / 工具** | /features/{slug} | 为现有视频**添加/增强** | b-roll-generator、subtitle-generator |
| **Video Templates** | /video-templates/{slug} | **即用风格/结构**，一键套用 | brand-film、clay-animation、love-story |

**差异化**：
- **功能页**：回答「能做什么」— 能力、输入输出、工作流
- **模板页**：回答「用什么风格/结构」— 预设风格、即用、套用

**关键词与内容区分（避免重叠）**：

| 维度 | Video Generator（/video-generator/、/features/） | Video Templates（/video-templates/） |
|------|--------------------------------------------------|-------------------------------------|
| **主关键词后缀** | generator、AI X video、X to video、create X video | **template**、X style template、X format template |
| **避免使用** | 不用 template、style、preset、ready-to-use | **不用 generator**、不用 create/make X video |
| **内容聚焦** | 输入→输出、工作流、能力、如何生成 | 风格、结构、适用场景、即用套用 |
| **示例** | explainer **video generator**、AI **tutorial video** | explainer **template**、tutorial **style template** |

*重叠词（如 anime、meme、product、clay）按后缀区分：generator 页用「X generator」；template 页用「X template」。*

**互相引用**：
- 模板页 → 链至相关功能（如 clay-animation → 链至 image-to-video、photo-to-claymation）
- 功能页 → 链至相关模板（如 blog-to-video → 链至 ppt-video、line-art-explainer）
- 避免内容蚕食：模板页不重复功能描述；功能页不重复风格列表

*详见 [medeo-features.md](./medeo-features.md) 核心功能页。*

---

## 1. 模板体系维度（多维度分类）

> 程序化 SEO 可沿多个维度扩展页面，覆盖不同搜索意图。**主维度**为内容类别；**辅助维度**为格式、平台、比例、用途。

| 维度 | 说明 | 程序化扩展 | 目标关键词模式 |
|------|------|------------|----------------|
| **内容类别** | 品牌、动画、产品、情感等 | /video-templates/{category} 分类 Hub | AI {category} video template |
| **格式类型** | Tier-ranking、UGC Avatar、Faceless、Horror、POV 等 | 模板属性，单页 /video-templates/{slug} 内标注 | {format} video template |
| **平台** | TikTok、Reels、Shorts、LinkedIn | 模板属性，单页内标注 | {platform} video template |
| **画幅比例** | 9:16、16:9、1:1 | 模板属性，可筛选 | vertical video template, square video template |
| **用途** | 营销、社交、教育、娱乐 | 模板属性，可筛选 | AI marketing video template |
| **风格** | 黏土、2D、像素、电影感 | 子类，已含于内容类别 | clay animation template |

*所有 URL 统一为 `/video-templates/{slug}`，格式与平台作为模板属性在单页内展示，不单独建格式页/平台页。*

### 1.1 行业热点格式（2025–2026）

| 格式 | 表现/数据 | Medeo 对应模板 | 拓展优先级 |
|------|-----------|----------------|------------|
| **Faceless Storytelling** | 占病毒视频约 30%；97% AI 创作者使用 | narrated-story-film, scary-story, myth-meme | P0 |
| **UGC-Style AI Avatar** | 转化率提升约 161%，成本降 60–80% | spokesperson, talking-avatar, ugc-ads | P0 |
| **Horror Narration** | 互动率比普通 Vlog 高 200–400% | scary-story, nightmare, horror | P0 |
| **Tier-Ranking/Bracket** | 引发评论与辩论，持续 trending | 待建（可基于 data-lens、sketch-argument 扩展） | P1 |
| **POV Recreations** | 第一人称沉浸式 | first-person-pov | P1 |
| **High-Dopamine Edits** | 快节奏、高刺激 | velocity-edit, brainrot | P1 |
| **Quick How-To** | 碎片化教程，即时价值 | tutorial, explainer, life-hack | P1 |

*来源：[Vidrel](https://vidrel.ai/blog/ai-video-formats-driving-crazy-engagement-in-2026)、[Virvid](https://virvid.ai/blog/ultimate-guide-on-viral-ai-shorts)*

### 1.2 平台与画幅

| 平台 | 推荐比例 | 时长 | 互动率（参考） |
|------|----------|------|----------------|
| **YouTube Shorts** | 9:16 | ≤60s | 5.91% |
| **TikTok** | 9:16 | ≤10min | 5.75% |
| **Instagram Reels** | 9:16 | ≤90s | 5.53% |
| **LinkedIn** | 1:1 | 短 | 1:1 完播率约 +35% |
| **YouTube 长视频** | 16:9 | 任意 | — |

*9:16 竖屏在 TikTok 上比横屏触达约高 40%；前 2–3 秒决定留存，约 63% 高 CTR 视频在前 3 秒完成 hook。*

---

## 2. 模板分类体系（8 大类 + 格式维度）

> AI 视频模板可程序化生成分类 Hub 与单模板页，覆盖 "AI [type] video template"、"[style] video template" 等长尾搜索。

| 类别 | Slug | 说明 | 代表模板/关键词 |
|------|------|------|----------------|
| **Brand & Marketing** | brand-marketing | 品牌片、营销、产品展示 | brand-film, brand-pop-up, product-explainer-film, AI brand video template |
| **Animation Style** | animation | 2D、黏土、剪纸、乐高、像素 | 2d-animation, clay-animation, papercut-animation, lego-fy, clay animation template |
| **Product & Explainer** | product-explainer | 产品解说、PPT、线稿 | product-hero-film, ppt-video, line-art-explainer, product video template |
| **Emotion & Holiday** | emotion-holiday | 情感、节日、纪念 | love-story, valentines-day, christmas, birthday, wedding, Valentine video template |
| **Atmosphere & Vibe** | atmosphere | 氛围、感官、冥想、治愈 | cinematic-film, lofi-vibe, dreamy, calming, meditation-visual, cinematic video template |
| **Gaming & Entertainment** | gaming | 游戏、动漫、像素 | pixel-game, minecraft, anime-short-film, anime-mv, pixel game video template |
| **Creative & Meme** | creative | 脑洞、梗、恐怖 | myth-meme, lego-film, scary-story, superhero-gone-wrong, meme video template |
| **Lifestyle & Pet** | lifestyle | 宠物、生活、美食 | pet-podcast, pet-interview, mukbang-vlog, food-ball, pet video template |

*Medeo 现有 70+ 模板，路径：`/video-templates/{slug}`*

---

## 3. 可拓展维度（模板属性，非独立 URL）

> 格式与平台作为模板属性在单页内展示，不建独立格式页/平台页。所有 URL 统一 `/video-templates/{slug}`。

### 3.0 按格式类型（Format，模板属性）

> 格式类关键词**必须含 template**；`tutorial`、`explainer` 等与 Generator 同名时，模板用「X template」、生成器用「X generator」。

| 格式 | 现有模板映射 | 目标关键词（template） | 对应 Generator（避免重叠） |
|------|--------------|------------------------|----------------------------|
| Faceless | narrated-story-film, scary-story, myth-meme, horror | faceless video template | — |
| UGC Avatar | spokesperson, talking-avatar, ugc-ads | UGC video template | ugc-ads generator |
| Horror | scary-story, nightmare, horror | horror video template | — |
| POV | first-person-pov, velocity-edit | POV video template | — |
| Storytelling | love-story, narrated-story-film | storytelling video template | — |
| Product Demo | product-explainer-film, product-hero-film | product demo video template | product-ad generator |
| How-To | ppt-video, line-art-explainer, life-hack | how to video template, explainer template | tutorial/explainer generator |

### 3.0.1 按平台（Platform，模板属性）

| 平台 | 推荐模板 | 目标关键词 |
|------|----------|------------|
| TikTok | 9:16 竖屏、faceless、meme、brainrot | TikTok video template |
| Instagram Reels | fashion-reels、ugc-ads、vlog | Reels video template |
| YouTube Shorts | explainer、tutorial、reaction | YouTube Shorts template |
| LinkedIn | 1:1、product-explainer、company-culture | LinkedIn video template |

### 3.0.2 按用途（Use Case，模板属性）

| 用途 | 模板示例 | 目标关键词 |
|------|----------|------------|
| 营销获客 | brand-film, ugc-ads, product-ad, spokesperson | AI marketing video template |
| 社交涨粉 | meme, brainrot, vlog, reaction | viral video template |
| 教育/培训 | tutorial, explainer, training, faq | AI education video template |
| 品牌叙事 | brand-culture-film, love-story, impact-film | brand storytelling template |
| 产品转化 | product-hero-film, unboxing, product-details | product video template |

---

## 4. 模板子类与长尾（程序化 SEO 数据源）

### 4.1 Brand & Marketing

| 子类 | 示例模板 | 关键词 |
|------|----------|--------|
| Brand Film | brand-film, brand-pop-up, brand-culture-film, valentines-brand-film | AI brand video template, brand film generator |
| Product | product-explainer-film, product-hero-film, product-details, product-display | product video template, AI product video |
| Impact/Concept | impact-film, concept-film, narrative-product-film | AI marketing video template |

### 4.2 Animation Style

| 子类 | 示例模板 | 关键词 |
|------|----------|--------|
| 2D | 2d-animation, drawn-animation | 2D animation video template |
| Clay | clay-animation, claymation | clay animation video, claymation template |
| Paper/Yarn | papercut-animation, yarn-animation, watercolor-picture-book | paper cut animation template |
| Lego | lego-fy, lego-film | Lego style video template |
| Pixel | pixel-game | pixel art video template |

### 4.3 Product & Explainer

| 子类 | 示例模板 | 关键词 |
|------|----------|--------|
| PPT/Slides | ppt-video, mg-ppt | PPT to video template |
| Line Art | line-art-explainer, sketch-argument | line art explainer template |
| Screencast | screencast-explainer | screencast video template |
| Data | data-lens, infographic | data visualization video template |

### 4.4 Emotion & Holiday

| 子类 | 示例模板 | 关键词 |
|------|----------|--------|
| Love | love-story, love-in-minecraft, barbie-valentine, valentines-day | AI love story video, Valentine video template |
| Celebration | birthday, wedding, graduation-celebration, anniversary | AI birthday video, wedding video template |
| Holiday | christmas, holiday-greeting, lunar-new-year | Christmas video template, holiday greeting AI |

### 4.5 Atmosphere & Vibe

| 子类 | 示例模板 | 关键词 |
|------|----------|--------|
| Cinematic | cinematic-film, realistic-film, stock-based-videos | cinematic video template |
| Chill | lofi-vibe, dreamy, calming, ambience, slow-living | lofi video template, calming video |
| Wellness | meditation-visual, mindfulness, healing, white-noise | meditation video template, wellness video |
| Mood | moody, vibe, dark-atmosphere, retro | mood video template |

### 4.6 Gaming & Entertainment

| 子类 | 示例模板 | 关键词 |
|------|----------|--------|
| Anime | anime-short-film, anime-mv, anime-op | anime video template |
| Game | pixel-game, minecraft, fortnite | gaming video template |
| Story | narrated-story-film, tv-show, make-a-song | story video template |

### 4.7 Creative & Meme

| 子类 | 示例模板 | 关键词 |
|------|----------|--------|
| Meme | myth-meme, brainrot | meme video template |
| Horror | scary-story, nightmare, horror | horror video template |
| Parody | superhero-gone-wrong, wrong-dreams | parody video template |

### 4.8 Lifestyle & Pet

| 子类 | 示例模板 | 关键词 |
|------|----------|--------|
| Pet | pet-podcast, pet-interview, pet-make-up, pet-chef, puppy-complaints | AI pet video template |
| Food | mukbang-vlog, food-ball, eating-with-ip, weird-cooking, eat-anything | mukbang video template |
| Daily | daily-life, lazy-moments, life-comeback | daily life video template |

---

## 4. 程序化 SEO 数据 Schema

### 4.1 单模板页数据字段

```json
{
  "template_id": "string",
  "slug": "string",
  "category": "brand-marketing|animation|product-explainer|emotion-holiday|atmosphere|gaming|creative|lifestyle",
  "sub_category": "string",
  "format_type": "faceless|ugc-avatar|horror|pov|storytelling|high-dopamine|product-demo|how-to",
  "platforms": ["tiktok", "reels", "shorts", "linkedin", "youtube"],
  "aspect_ratios": ["16:9", "9:16", "1:1"],
  "use_cases": ["marketing", "social", "education", "entertainment", "brand"],
  "title": "string",
  "description": "string",
  "style_tags": ["string"],
  "keywords": ["string"],
  "related_templates": ["slug"],
  "url": "string",
  "preview_thumbnail": "string"
}
```

### 4.2 分类 Hub 页数据字段

```json
{
  "category": "string",
  "slug": "string",
  "sub_categories": ["string"],
  "templates_count": "number",
  "keywords": ["string"],
  "url": "string"
}
```

### 4.3 数据来源

| 来源 | 用途 | 更新频率 |
|------|------|----------|
| **Medeo Sitemap** | /video-templates/* URL 列表 | 周/月 |
| **Medeo 官网** | 模板名称、描述、预览 | 手动/爬虫 |
| **关键词工具** | AI video template、clay animation template 等搜索量 | 季度 |

---

## 5. URL 模式（程序化 SEO）

> **统一规则**：所有 URL 使用 `/video-templates/{slug}`，不额外区分格式页、平台页。格式与平台作为模板属性在单页内展示。

| 类型 | 模式 | 示例 |
|------|------|------|
| **模板 Hub** | /video-templates | 模板总览 |
| **分类 Hub** | /video-templates/{category} | /video-templates/brand-marketing、/video-templates/animation |
| **单模板** | /video-templates/{slug} | /video-templates/brand-film、/video-templates/clay-animation |

### 5.1 推荐结构

| 层级 | URL | 说明 |
|------|-----|------|
| 1 | /video-templates | 模板总览 Hub |
| 2 | /video-templates/{category} | 分类页（品牌、动画、产品、情感等） |
| 3 | /video-templates/{slug} | 单模板页 |

*格式（faceless、ugc-avatar 等）、平台（tiktok、reels 等）作为 schema 字段与单页 Evidence block 展示，不建独立 URL。*

---

## 6. 程序化 SEO 模板结构

### 6.1 分类 Hub 页模板（/video-templates/{category}）

| Section | 内容 |
|---------|------|
| **H1** | {Category} AI Video Templates |
| **Intro** | 该类别模板简介、适用场景、为何选 Medeo |
| **Evidence block** | 模板列表表（HTML table）：模板名、风格、适用平台、链至单页 |
| **Sub-categories** | 子类列表 + 锚点或链至子类 |
| **FAQ** | 如 "What is {category} AI video template?" |
| **CTA** | Start for Free、链至 /features |

### 6.2 单模板页模板（/video-templates/{slug}）

| Section | 内容 |
|---------|------|
| **H1** | {Template name} AI Video Template |
| **Intro** | 模板风格、适用场景、为何适合 [use case] |
| **Evidence block** | 模板参数（比例、风格标签、适用平台）、示例/预览 |
| **Related** | 同类别其他模板 |
| **FAQ** | 如 "How to use {template} with Medeo?" |
| **CTA** | 链至 Medeo 创建、/features |

### 6.3 单模板页格式/平台展示

> 格式与平台不建独立页，在单模板页 Evidence block 中展示。

| 展示项 | 说明 |
|--------|------|
| **格式标签** | faceless、ugc-avatar、horror、pov 等，作为标签或徽章 |
| **推荐平台** | TikTok、Reels、Shorts、LinkedIn，作为「适用平台」列表 |
| **画幅建议** | 9:16、16:9、1:1 |

### 6.4 内容要求（Programmatic SEO）

| 要求 | 说明 |
|------|------|
| **300+ 词** | 每页最低字数 |
| **Evidence block** | 每页含真实数据（模板参数、风格、平台） |
| **唯一数据** | 每页有独特描述，非简单变量替换 |
| **内部链接** | 分类↔模板、相关模板互链、链至 /features |
| **关键词隔离** | 主推 template；不重复 Generator 页的「输入→输出」「工作流」描述；链至 Generator 时用「用 X 生成器实现此风格」而非复制能力描述 |

---

## 7. 模板关键词映射（程序化 SEO 目标词）

> **关键词分配规则**：模板页**必须**含 `template`；**禁止**使用 `generator`。与 [medeo-features.md](./medeo-features.md) Video Generator 区分，避免蚕食。

| 类别 | 主关键词（含 template） | 长尾模式 | 避免（归属 Generator） |
|------|-------------------------|----------|------------------------|
| Brand & Marketing | AI brand video template, brand film template | {industry} brand video template | brand video generator → /video-generator |
| Animation | clay animation template, 2D animation template | {style} animation video template | clay animation generator → photo-to-claymation |
| Product | product video template, product explainer template | PPT to video template | product video generator, AI product video → /video-generator/product-ad |
| Emotion & Holiday | AI love story video template, Valentine video template | {holiday} video template | — |
| Atmosphere | cinematic video template, lofi video template | {mood} video template | — |
| Gaming | anime video template, pixel game video template | {game} video template | anime video generator → /video-generator/anime |
| Creative | meme video template, horror video template | {style} meme template | meme video generator → /video-generator/ai-meme |
| Lifestyle | AI pet video template, mukbang video template | pet {scenario} video template | pet video generator → /video-generator/pet |

### 7.1 格式维度关键词

| 格式 | 主关键词 | 长尾模式 |
|------|----------|----------|
| Faceless | faceless video template, AI faceless video | faceless storytelling template |
| UGC Avatar | UGC video template, AI avatar video | UGC style video template |
| Horror | horror video template, horror narration AI | horror story video template |
| POV | POV video template | POV recreation template |
| TikTok | TikTok video template, AI TikTok | TikTok viral template |
| Reels | Reels video template, AI Reels | Instagram Reels template |

*行业数据：约 52% 短视频含 AI 元素；Faceless 占病毒视频约 30%；AI 视频营销 ROI 提升约 82%；制作周期从数周缩短至数小时，成本降约 95%。*

---

## 8. 实施优先级

| 优先级 | 动作 |
|--------|------|
| **P0** | 定义数据 schema（Template、Category）；从 sitemap 提取 70+ 模板 slug |
| **P0** | 新建 /video-templates Hub、/video-templates/{category} 分类页（8 类） |
| **P1** | 单模板页 SEO 强化（现有页补充 title/meta、Evidence block、FAQ） |
| **P1** | Sitemap 分段（/video-templates/*）；noindex 低价值页 |
| **P2** | 模板描述、风格标签、关键词批量补充 |
| **P2** | 数据更新自动化（sitemap 监控、新模板接入） |
| **P2** | 模板 schema 补充 format_type、platforms 字段 | 单页内展示，支持筛选，不建独立 URL |

---

## 9. 文档关联

| 文档 | 关联 |
|------|------|
| [medeo.md](./medeo.md) | 概览；模板页链入 Features、Pricing |
| [medeo-features.md](./medeo-features.md) | 功能与生成器；模板为即用风格，与 features 互补 |
| [medeo-keywords.md](./medeo-keywords.md) | 模板关键词→目标页映射 |
| [medeo-use-cases.md](./medeo-use-cases.md) | 模板适用场景（Creators、Marketers、Educators） |
| [medeo.app/download](https://www.medeo.app/download) | 移动端应用（iOS、Android）；模板页可链至 Download 供手机端用户 |

### 9.1 模板页与功能页互相引用规则

| 方向 | 规则 | 示例 |
|------|------|------|
| **模板页 → 功能页** | 链至实现该风格的相关生成器/转化/工具 | clay-animation → image-to-video、photo-to-claymation；brand-film → b-roll-generator、product-explainer（生成器） |
| **功能页 → 模板页** | 链至可套用该功能的风格模板 | blog-to-video → ppt-video、line-art-explainer；b-roll-generator → product-explainer-film、cinematic-film |
| **模板页 → 模板页** | 链至同类别或风格相近的模板 | brand-film → product-explainer-film；clay-animation → papercut-animation |
| **避免** | 模板页不重复功能描述；功能页不重复风格列表 | 模板页写「风格、结构、适用场景」；功能页写「输入、输出、工作流」 |
| **关键词** | 模板页主推 template；功能页主推 generator | 模板 title 含「template」；功能 title 含「generator」或「AI X video」 |

**Slug 区分**：`product-explainer-film` = 模板（/video-templates/product-explainer-film）；`product-explainer` = 生成器（/video-generator/product-explainer）。引用时按实际路径区分。

**内容隔离**：模板页不写「如何用 Blog to Video 生成」等能力描述；功能页不写「clay 风格适合 TikTok」等风格列表。通过链接引用，不复制。

---

**Last updated**：2026-03-02

---

## 附录 A：模板→格式/平台映射（示例）

| 模板 Slug | 格式类型 | 推荐平台 |
|-----------|----------|----------|
| narrated-story-film, scary-story, myth-meme | faceless | TikTok, Reels, Shorts |
| spokesperson, talking-avatar, ugc-ads | ugc-avatar | TikTok, Reels, 广告 |
| horror, nightmare, dark-atmosphere | horror | TikTok, Reels |
| first-person-pov, velocity-edit | pov, high-dopamine | TikTok, Reels |
| product-explainer-film, product-hero-film | product-demo | LinkedIn, YouTube |
| tutorial, explainer, life-hack | how-to | YouTube, Shorts |
