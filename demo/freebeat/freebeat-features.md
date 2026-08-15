# Freebeat Features 功能页总结

> **文档边界**：本文档仅含功能（产品**能做什么**）。Use Cases 见 [freebeat-use-cases.md](./freebeat-use-cases.md)；关键词见 [freebeat-keywords.md](./freebeat-keywords.md)；竞品见 [freebeat-competitors.md](./freebeat-competitors.md)。

---

## 一、功能概览与 URL

### 核心流程（四步）

| 步骤 | 说明 | 目标关键词 |
|------|------|------------|
| 1. Upload | 上传 MP3 或粘贴 Suno、Udio、TikTok、YouTube 链接 | music to video, song to video |
| 2. Choose Mode | Story Video / Stage Performance；风格、角色、创意方向 | AI music video generator |
| 3. Generate | 生成、查看分镜、调整方向、重生成 | AI music video maker |
| 4. Add Lyrics | 歌词同步、自定义样式、发布到 TikTok/Instagram/YouTube | lyrics video generator |

### 差异化能力（Why）

| 功能 | 说明 | 目标关键词 |
|------|------|------------|
| **Directed Music Video** | AI 导演式规划；分镜、转场、完整 MV 一站式 | AI music video generator |
| **Rhythm Is the Script** | 画面与 BPM、节拍、drop 同步 | music to video AI |
| **Control Every Detail** | 风格、角色稳定；无视觉漂移 | AI music video maker |
| **Lyrics That Sing Along** | 歌词自动同步、动态字幕、卡拉 OK 高亮 | lyrics video generator |
| **Dance. Sing. Tell Stories.** | 舞蹈、演唱、故事 MV 全覆盖 | AI dance video generator |
| **Everything, In One Place** | 音乐、视觉、创作一体化工作室 | All-in-One music video |

### All-in-One Studio（产品矩阵）

| 产品 | URL | 目标关键词 |
|------|-----|------------|
| AI Music Video Agent | /products | AI music video generator |
| AI Video Effect | /products | AI video effect |
| Music to Dance Video | /products | AI dance video generator |
| Subject Reference Video | /products | subject reference video |
| Music to Music Video | /products | music to music video |
| Music to Lyrics Video | /products | lyrics video generator |
| Free Stock Footage / Image | /products | free stock footage |
| AI Video Generator | /products | AI video generator |
| Lip sync Video | /products | lip sync video |
| Face Swap | /products | face swap |

**注**：Sitemap 结构见 [freebeat.md §4.2](./freebeat.md#42-sitemap-结构sitemapxml)；工具类页面可能位于 /tool-details 下。

### 技术原理

**音频分析**→**视觉生成**→**同步映射**→**自动化处理**。详见 [Alignify](https://alignify.co/zh/tools/music-video-generator)。

---

## 二、核心功能详情

### 1. AI Music Video Agent

- 上传歌曲或链接 → AI 分析节奏与歌曲结构
- 选择 Story Video / Stage Performance
- 自动规划分镜、节奏、氛围
- 生成、分镜预览、调整、重生成
- 零剪辑技能产出完整 MV

### 2. Rhythm Is the Script

- 每一帧跟随 BPM、节拍、drop
- 画面与能量变化同步
- 非通用时间轴，音乐驱动

### 3. Lyrics That Sing Along

- 歌词自动同步
- 动态字幕、卡拉 OK 高亮
- 自定义时长、样式、高亮

### 4. 多格式导出

- 竖屏 9:16、横屏 16:9、方形 1:1
- 适配 TikTok、Instagram、YouTube
- HD 720p、Full HD 1080p

### 5. 音乐来源

- 上传 MP3
- 链接：SoundCloud、YouTube、Suno、Udio、TikTok、Stable Audio、Riffusion

---

## 三、平台专属 URL-to-Video 页面（建议）

Freebeat 支持**粘贴链接即可生成**，无需下载音频。可为各音乐平台制作独立落地页，承接「X music to video」搜索意图。

### 3.1 页面与关键词映射

| 页面 | 建议 URL | 目标关键词 | 说明 |
|------|----------|------------|------|
| **Spotify Music to Video** | /tools/spotify-music-to-video | Spotify music to video, Spotify to video AI, Spotify MV generator | 粘贴 Spotify 链接→自动分析节奏→生成 MV；竞品：Revid、LlamaGen |
| **Suno Music to Video** | /tools/suno-music-to-video | Suno music to video, Suno to video, Suno MV generator | Suno AI 音乐→MV；竞品：Revid、SunoVideo、Neural Frames |
| **Udio Music to Video** | /tools/udio-music-to-video | Udio music to video, Udio to video, Udio MV generator | Udio AI 音乐→MV；Udio 仅生成音乐，需第三方做视频 |
| **YouTube Music to Video** | /tools/youtube-music-to-video | YouTube music to video, YouTube to video AI | YouTube 音乐链接→MV |
| **TikTok Music to Video** | /tools/tiktok-music-to-video | TikTok music to video, TikTok to video AI | TikTok 音乐→竖屏 MV；竞品：LlamaGen、MSong.ai |
| **SoundCloud Music to Video** | /tools/soundcloud-music-to-video | SoundCloud music to video, SoundCloud to video | SoundCloud 链接→MV；竞品：Revid、LlamaGen |
| **Stable Audio Music to Video** | /tools/stable-audio-music-to-video | Stable Audio music to video | Stable Audio 生成音乐→MV |
| **Riffusion Music to Video** | /tools/riffusion-music-to-video | Riffusion music to video | Riffusion 生成音乐→MV |

**平台专属竞品**：见 [freebeat-competitors.md §8](./freebeat-competitors.md#八平台专属竞品url-to-video)。**关键词映射**：见 [freebeat-keywords.md §2](./freebeat-keywords.md)。

### 3.2 页面结构建议

每页可包含：平台介绍、粘贴链接步骤、支持格式、导出选项（9:16/16:9/1:1）、与 Freebeat 主流程的衔接、FAQ（如「如何获取 Suno/Udio 链接？」）。

---

## 四、技术指标（官网）

| 指标 | 数值 |
|------|------|
| 用户 | 1,000,000+ |
| 音乐可视化 | 1,000,000,000+ 秒 |
| 覆盖国家 | 150+ |
| 视频时长 | 15 秒～约 6 分钟 |
| 分辨率 | 720p、1080p |

---

---

*文档生成日期：2026-03-16 | 来源：官网 [freebeat.ai](https://freebeat.ai/)、[Alignify 最佳AI音乐视频生成工具](https://alignify.co/zh/tools/music-video-generator)*
