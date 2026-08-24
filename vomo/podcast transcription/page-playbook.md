# VOMO — 播客平台转录页生产手册

## 1. 一句话原则

**同一转录引擎，换「这个平台为什么不给你可用的文字稿」。**

平台页不是再写一遍枢纽页的 Speaker Diarization 清单。Amazon Music 写「零 transcript 功能」；Spotify 写「应用内能看但不能复制/导出」；Podbean 写「主播要 SEO 级 show notes」。CTA 都是上传或粘贴 YouTube，**缺口叙事必须平台专属**。

---

## 2. 页面模具（按线上已上线页还原）

### 2.1 通用结构（Amazon / iHeart / Overcast / Pocket Casts / RSS）

```
面包屑           Home / Podcast Transcription / {Platform}
H1               Transcribe {Platform} Podcasts to Text
英雄段（1–2 句）  平台 transcript 缺口 + VOMO 交付物
Mock 转录预览     平台名 · Ep. · 时长 · 说话人对话（点出平台痛点）
上传区（主）       Drop file · MP3/WAV/M4A/MP4/MOV · up to 2 GB / 3 hours
Supports 行        MP3/WAV/M4A upload · MP4/MOV · Up to 3 hours
H2 价值块标题     The Transcript {Platform} Never Gives You / Leaves Out / …
6 张利益卡         emoji + 标题 + 一句（Speaker / Timestamps / 40+ langs / Summary / Export …）
H2 Who Uses       4 个 Persona（含平台场景）
H2 How to 3 steps Get audio → Upload → Export
H2 FAQS           1–2 问（首问：Does {Platform} have transcripts?）
底栏 CTA          场景化一句 + Transcribe a/an {Platform} episode
```

### 2.2 巨头变体（Spotify / Apple / Castbox / YouTube Podcast）

在通用结构基础上增加：

- **双输入 Tab**：Upload File | Paste a Link（YouTube 或 Castbox share link）
- **Trending This Week**：4 档热门节目 + 免责声明
- **FAQ 扩至 5–6 问**
- **How-to 文末**：链回枢纽 `Use the universal podcast transcription tool →`

| 页 | Paste a Link 支持 |
|----|-------------------|
| `spotify-podcast` / `apple-podcast` | YouTube 同集 |
| `youtube-podcast` | **YouTube**（主路径，paste 即转） |
| `castbox` | **Castbox share link**（castbox.fm）或 YouTube |

### 2.5 体裁变体（Business / Christian / True Crime）

**不写平台零功能**，写「这类节目转录后要干什么」。

```
H1               Transcribe {Genre} Podcasts to … / Sermons / Case File
英雄段            体裁内容密度（数字/经文/案情）+ 交付物
Mock UI           体裁专属：Business=摘要简报 / Christian=讲道片段 / True Crime=Case File
上传区（主）       同平台页
Trending This Week  该体裁 4 档热门节目
H2 价值块         4–6 卡（体裁术语/搜索/导出）
H2 How to 3 steps  Copy link（任意平台）→ Paste → Export
H2 FAQS           5 问（体裁专属 + 隐私/语言）
底栏 CTA          体裁化收束
```

| slug | Mock UI | 专属卖点 |
|------|---------|----------|
| `business` | Key takeaway + Chapters + Notion-ready | 商业术语、ARR/CAC、Export to Notion |
| `christian` | 讲道 + 经文引用 | Scripture-friendly、小组分享 |
| `true-crime` | Case File + 时间戳引用 | 人名/日期/地点搜索、legal FAQ |

### 2.3 创作者变体（Podbean）

- H2 标题偏 SEO：`Podbean Transcripts Built for Creators`
- 6 卡强调：**SEO-Ready Show Notes**、Captions for Video Cut
- Persona 含 **Marketers**（长尾搜索流量）
- FAQ：`Does Podbean transcribe automatically?` — 承认平台有限内置转录，VOMO 覆盖任意单集 + 全格式导出

### 2.4 RSS 变体（协议层）

- H1：`Transcribe Any Podcast RSS Feed to Text`
- 英雄段强调「所有 App 都在读同一个 feed」
- 6 卡第一条：**Every App, One Workflow**（列举 Spotify/Apple/Overcast/Player FM…）
- 不做「平台零功能」叙事，做「一层覆盖全部播放器」

---

## 3. 平台缺口叙事库（写页必查）

| 平台 | slug | 核心缺口（英雄段 / FAQ 第一句） | 勿写成 |
|------|------|----------------------------------|--------|
| **Spotify** | `spotify-podcast` | 应用内 auto-transcript 只读、不可复制/导出/跨集搜索 | 「Spotify 没有 transcript」（它有，只是不可用） |
| **Apple Podcasts** | `apple-podcast` | iOS 17.4+ 有只读稿；不可复制/下载；旧集常缺；非 Apple 设备难用 | 「Apple 完全没有 transcript」 |
| **Amazon Music** | `amazon-music` | Amazon Music + Audible **零** transcript 功能 | 暗示应用内有隐藏导出 |
| **iHeartRadio** | `iheartradio` | 大型 talk show 平台，**无** transcript 面板/导出 | 只写「广播」不写多主持人 |
| **Overcast** | `overcast` | 极简播放器，**无** transcript 视图 | 批评 Smart Speed（那是卖点） |
| **Pocket Casts** | `pocket-casts` | 仅当发布者在 feed 附带才显示；**不可导出**；独立节目大多没有 | 「Pocket Casts 从不显示 transcript」 |
| **Podbean** | `podbean` | 托管方有限自动转录；创作者要 **SEO + 全格式导出** | 与 RSS 页完全同文案 |
| **Castbox** | `castbox` | AI Podcaster 仅部分节目、锁在 App 内不可导出 | 「Castbox 完全没有 transcript」 |
| **YouTube Podcast** | `youtube-podcast` | 自动字幕：无说话人/标点/章节/真导出；2–3 小时长播客 | 与通用 YouTube 工具同文案 |
| **RSS Feed** | `rss-feed` | 工作在上层协议，绕过各 App 限制 | 再开 Spotify/Apple 平行页抢词 |

体裁页（§2.5）不适用上表；主词用 `{genre} podcast transcript`。

## 4. 输入方式话术

| 输入 | 适用页 |
|------|--------|
| **Paste YouTube link** | 枢纽、`youtube-podcast`、Spotify/Apple 等（YouTube 同集） |
| **Paste Castbox share link** | `castbox` only |
| **Upload MP3/M4A/MP4** | 全部 14 页 |
| **Paste Spotify / Apple URL** | ✗ **不支持** — FAQ 必须说明 |

Spotify / Apple / Amazon 等（除 Castbox、YouTube Podcast）英雄段标准句式：

> Paste the YouTube version of the episode, or download the audio and upload it …

---

## 5. SEO 与内链

- **Title 模式**：`{Platform} Podcast Transcription — Transcribe Any Episode to Text | VOMO`
- **H1 模式**：`Transcribe {Platform} Podcasts to Text`（RSS 用 `Any Podcast RSS Feed`）
- **主词**：`{platform} podcast transcript` / `transcribe {platform} podcast`
- **链回枢纽**：`/podcast-transcription`（面包屑 + Apple/Spotify How-to 文末）
- **横链**：最多 2 个近亲平台（如 Overcast ↔ Pocket Casts），正文不堆 8 个平台链
- **YouTube 播客**：已上线 `/podcast-transcription/youtube-podcast`；通用 YouTube 链 `/tools/youtube-transcript`，两页互链
- **旧 Tools 页**：`/tools/podcast-transcript-generator` 等应 301 或 canonical → 新簇，勿平行维护

---

## 6. 交付检查清单

- [ ] slug 与 [podcast-platforms.md §4.2](./podcast-platforms.md) 一致
- [ ] 英雄段换成别的平台会失效
- [ ] 平台缺口事实准确（Spotify/Apple 是「只读」不是「没有」）
- [ ] Mock 预览对话点出本平台痛点（不要八页同一脚本）
- [ ] 6 利益卡至少 2 张平台专属（Podbean=SEO；iHeart=多主持人）
- [ ] How-to 三步含「Get audio」的具体来源
- [ ] FAQ 首问回答「平台有没有 transcript」
- [ ] 未承诺「粘贴 Spotify 链接即可转录」
- [ ] Tools 导航 Podcast Transcription 下拉可发现（若已进导航）
- [ ] 需要索引则写入 sitemap

---

## 7. Backlog Brief

| 优先级 | 方向 | slug | 说明 |
|--------|------|------|------|
| P1 | Player FM | `player-fm` | 未上线 |
| P2 | Podcast Addict | `podcast-addict` | 未上线 |
| P2 | 体裁：Comedy / News | `comedy` 等 | 复用 §2.5 模具 |
| P3 | 中文平台 | `xiaoyuzhou` 等 | 只能上传 |

**已上线 14 URL**（1 枢纽 + 10 平台 + 3 体裁）— 见 [podcast-platforms.md §4.2](./podcast-platforms.md)。

---

*遵循 [客户文档规范](../../demo/client-template.md)*
*关联：[podcast-platforms](./podcast-platforms.md) | [主文档](../vomo.md) | [features](../vomo-features.md)*
*用途：按同一模具写出 [`/podcast-transcription/amazon-music`](https://vomo.ai/podcast-transcription/amazon-music) 这一级平台子页。*
*Last updated: 2026-08-23*
*创建日期: 2026-08-23*
*所属项目: VOMO（https://vomo.ai/）*
