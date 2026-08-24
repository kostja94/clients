# VOMO — Podcast 平台全景与播客转录机遇

## 1. 执行摘要（BLUF）

2026 年的 Podcast 平台生态呈现「**三巨头 + 长尾**」格局：YouTube、Spotify、Apple Podcasts 占据绝大多数使用量，第二梯队为 Amazon Music、iHeartRadio 等，再往下是大量垂直播放器与 RSS 工具。两大趋势深刻影响播客转录场景——**视频化**（YouTube 成为播客消费第一入口）和 **AI 能力**（转录、摘要成为平台与独立工具的新战场）。

对 VOMO 而言：**播客转录是内容创作者场景的高价值切入点**。全球播客数量已超过数百万档（主流曲库 Spotify 约 700 万档），但绝大多数节目没有完整的文字稿；内容创作者「播客 → 转录 → 博客/字幕/SNS 分发」的需求稳定且付费意愿明确。VOMO 的 Bot-free 录音、音频上传、YouTube 链接转录、SRT 字幕导出能力恰好覆盖这条工作流的核心环节。

**2026-08 线上进展**：播客楔子已从原型迁到正式域。英文 sitemap（`sitemap-en-0.xml`，2026-08-23）收录 **14 条 URL**：1 个枢纽 + **13 个子页**（10 平台 + 3 体裁）。样板页：[Amazon Music](https://vomo.ai/podcast-transcription/amazon-music)（零 transcript）、[YouTube Podcast](https://vomo.ai/podcast-transcription/youtube-podcast)（长视频播客）、[True Crime](https://vomo.ai/podcast-transcription/true-crime)（体裁切片）。策略是 **L2 枢纽吃品类词，L3 吃「平台 × transcript」或「体裁 × transcript」**。生产规范见 [page-playbook.md](./page-playbook.md)。

---

## 2. Podcast 平台市场全景（2026）

### 2.1 使用量口径说明

Podcast「使用量」存在两种主流口径，结果差异显著，评估时须同时参考：

| 口径 | 方法 | 领先者 | 局限 |
|------|------|--------|------|
| **最常用平台（问卷）** | 调研周度听众「主要使用哪个服务」 | YouTube 领先 | 不含 RSS 下载量统计，受记忆偏差影响 |
| **下载量（RSS 统计）** | 统计各平台产生的下载/订阅数 | Apple Podcasts 领先 | 无法测量 YouTube 等视频平台 |

### 2.2 最常用平台份额（问卷口径，2026）

| 平台 | 美国 | 英国 | 加拿大 | 趋势 |
|------|------|------|--------|------|
| **YouTube / YouTube Music** | 30–31% | 29%（2026 首次登顶） | 40% | ↑ 连续四年增长，视频播客驱动 |
| **Spotify** | 27–29% | 28% | 51%（18–34 岁） | ↓ 缓慢下滑但 Gen Z 渗透率最高 |
| **Apple Podcasts** | 10–15% | 10% | — | ↓ 但创作者满意度评分第一 |
| **BBC Sounds** | — | 15%（英国特有） | — | 稳定 |
| **Amazon Music / Audible** | 4–8% | ~4% | — | 稳定，靠 Prime 曝光 |
| **iHeartRadio** | 3–5% | — | — | 稳定 |
| **其他** | 其余 | 18% | — | — |

### 2.3 下载量份额（RSS 统计口径，2026）

| 平台 | 英国 | 加拿大 |
|------|------|--------|
| **Apple Podcasts** | 37.5% | ~49% |
| **Spotify** | 31.7% | ~19% |
| **Amazon Music** | 4.1% | — |

> ⚠️ 下载量口径**不计 YouTube**，也不计 Spotify 视频播放与平台原生 App（如 BBC Sounds），因此实际 YouTube 的影响被显著低估。

### 2.4 关键趋势

1. **视频化**：YouTube 占播客发现来源的 40%，84% 的 Gen Z 会观看视频播客；播客行业竞争主轴已从「Spotify vs Apple」转为「Spotify vs YouTube」。
2. **AI 功能军备竞赛**：平台原生转录/摘要（Apple、Spotify）与独立 AI 工具（Snipd、Podtastic、Castbox）同场竞争。
3. **平台整合**：Google Podcasts 于 2024 年停服、迁移至 YouTube Music；Stitcher 并入 SiriusXM；Spotify 收缩高成本独占协议（2024–2025）。
4. **创作者满意度**：2026 Podnews 报告卡中 Apple Podcasts 第一、YouTube 首次升至第二（超过 Spotify）。

---

## 3. 完整平台清单（2026）

### 3.1 全球巨头平台（综合性平台）

| 平台 | 类型 | 说明 | 状态 |
|------|------|------|------|
| **Apple Podcasts** | 系统内置 | iOS 默认预装、老牌基础设施、节目上架必选；订阅/文字稿/视频 | 活跃 |
| **Spotify** | 流媒体 | 曲库约 700 万档，算法推荐最强，Gen Z 渗透率高 | 活跃 |
| **YouTube / YouTube Music** | 视频平台 | 使用量第一，视频播客主导，替代 Google Podcasts | 活跃 |
| **Amazon Music / Audible** | 流媒体 | Prime 免费，含 Wondery 独占 | 活跃 |
| **iHeartRadio** | 广播+播客 | 传统电台跨界，免费 | 活跃 |
| **SiriusXM** | 卫星+播客 | 收购 Stitcher 内容 | 活跃 |
| **Pandora** | 音乐+播客 | SiriusXM 旗下 | 活跃 |
| **Audacy** | 广播+播客 | 美国广播集团 | 活跃 |
| **NPR One** | 公共电台 | 美国公共广播 | 活跃 |
| **TuneIn Radio** | 电台聚合 | 电台+播客 | 活跃 |
| **Deezer** | 音乐流媒体 | 法国流媒体，播客内容增长快 | 活跃 |
| **Anghami** | 区域流媒体 | 中东和北非（MENA）主流音频平台，含播客 | 活跃 |
| **Google Podcasts** | 独立 App | ⚠️ 2024-04-02 美国停服、2024-06 全球停服，迁移至 YouTube Music | 停服 |

### 3.2 专用播客播放器（RSS 聚合类）

**跨平台：**

| 播放器 | 平台 | 特色 | 模式 |
|--------|------|------|------|
| **Pocket Casts** | 全端 | 最强跨平台同步、过滤、静音修剪 | Freemium |
| **Castbox** | iOS/Android/Web | 社区评论、AI 摘要、多平台 | Freemium |
| **Player FM** | 全端 | 老牌、压缩省流量；印度与新兴市场用户多 | Freemium |
| **Podbean 播放器** | 全端 | 托管+播放一体 | Freemium |
| **Podurama** | 全端 | 免费无广告 | Free |
| **Snipd** | iOS/Android | AI 高亮/摘要/剪片段，导出 Notion/Obsidian | Freemium |
| **Goodpods** | iOS/Android | 社交发现（好友动态） | Free |
| **Fountain** | iOS/Android | 比特币闪电网络打赏（value-for-value） | Free |
| **Podverse** | 全端 | 开源，Podcasting 2.0，比特币打赏 | 开源 |
| **CurioCaster** | iOS/Android | 老牌 Podcasting 2.0 客户端，支持付费/打赏 | Free |
| **iVoox** | 全端 | 西语区强势，电台+播客 | Freemium |
| **Podtastic** ⚠️ | iOS/Android | AI 摘要/主题/智能播放（小众） | Freemium |
| **Playary** ⚠️ | 全端 | 独立音乐+播客发现（小众） | Free |

**iOS 专用：**

| 播放器 | 特色 | 模式 |
|--------|------|------|
| **Overcast** | Smart Speed、Voice Boost | Freemium |
| **Castro** | 收件箱式剧集管理（2024-01 一度下线，后被独立开发商 Bluck Apps 收购并恢复运营） | Freemium |
| **Downcast** | 一次性买断无订阅 | 买断 |
| **Castamatic** | 极简无广告 | Free |
| **EarMemo** ⚠️ | 离线本地优先，适合自有音频（小众） | 付费 |

**Android 专用：**

| 播放器 | 特色 | 模式 |
|--------|------|------|
| **Podcast Addict** | Android 重度用户最爱，最强自定义、支持 YouTube/audiobook/RSS | Freemium |
| **AntennaPod** | 开源、隐私、无广告 | 开源 |
| **Tsacdop** ⚠️ | Flutter 开源（小众，更新停滞） | 开源 |
| **Podcast Republic** | 功能丰富 | Freemium |
| **Podcast Guru** | 现代 UI | Free |

> ⚠️ 注：表中标 ⚠️ 的为极小众或更新停滞项目（Podtastic、Playary、EarMemo、Tsacdop），若用于对外内容建议谨慎引用或直接省略。

> **Podcasting 2.0 / 付费打赏型**：Fountain（比特币闪电网络打赏）、Truefans（创作者经济，可设节目订阅价）、CurioCaster（老牌客户端）、Podverse（开源）。此类平台核心是把 RSS 升级为可双向互动/打赏的协议。

### 3.3 RSS 阅读器（通用订阅）

| 阅读器 | 说明 |
|--------|------|
| **NetNewsWire** | 苹果生态免费开源 |
| **Feedly** | 最流行云端 RSS |
| **Inoreader** | 专业聚合/自动化 |
| **Reeder** | iOS 老牌 RSS 客户端 |
| **Unread** | iOS 极简 |
| **Feedbin** | 付费云 RSS |
| **Miniflux / FreshRSS / Tiny Tiny RSS** | 自托管开源 |

> **RSS 的技术意义**：播客的底层分发协议就是 RSS 2.0 + `enclosure` 标签。所有播放器（含 Apple、Spotify）都通过订阅节目 RSS feed 拉取剧集。因此「播客转录」工具只需解析 RSS feed 即可获得节目结构与音频/视频源，是接入播客生态的钥匙。

### 3.4 播客托管商（RSS feed 源头）

| 托管商 | 定位 |
|--------|------|
| **Libsyn** | 老牌头部托管 |
| **Buzzsprout** | 新手友好 |
| **Podbean** | 托管+播放+变现一体 |
| **Spotify for Podcasters**（原 Anchor） | 免费托管，Spotify 系 |
| **Transistor / Captivate / Castos / RSS.com / Podomatic** | 独立托管 |
| **Simplecast** | 企业级 |
| **Blubrry（PowerPress）** | WordPress 插件 |
| **Acast / Audioboom** | 广告变现型 |
| **Art19 / Megaphone / Omny Studio** | 大型网络/广告级 |
| **Spreaker / Zencastr / Riverside** | 录制+托管一体 |
| **RedCircle / Fireside / Resonate / Truefans** | 新兴托管 |

### 3.5 中文/华语平台

| 平台 | 说明 |
|------|------|
| **喜马拉雅 Ximalaya** | 中国最大音频平台，有声书 + 播客混合生态 |
| **小宇宙 Xiaoyuzhou** | **中文播客第一大平台** |
| **荔枝 FM / 荔枝播客** | 有声书 + 播客混合生态，含语音直播 |
| **蜻蜓 FM** | 传统电台 + 播客 |
| **网易云音乐**（内置播客） | 音乐+播客 |
| **QQ 音乐**（内置播客） | 音乐+播客 |
| **得到 App** | 知识付费+音频 |
| **猫耳 FM** | 音频/广播剧 |
| **Himalaya（国际版）** | 海外华语市场 |
| **Apple Podcasts / Spotify 中文区** | 华语用户常用 |

### 3.6 车载 / 智能音箱 / 电视 / 社交场景

| 场景 | 入口 |
|------|------|
| 车载 | CarPlay、Android Auto |
| 智能音箱 | Amazon Echo/Alexa、Google 音箱、Siri/HomePod |
| 电视 | Apple TV、Android TV、Roku |
| 音响 | Sonos 等 |
| 视频播客 | YouTube、Rumble（视频播客增长中） |
| 实时音频/回放 | X / Twitter Spaces（实时音频 + 回放播客化） |
| 社交传播 | Facebook（触达 80% 播客听众）、TikTok、Instagram Reels、X |

### 3.7 播客上架分发优先建议

> 若目标是把节目上架分发，除三大巨头外**最优先覆盖**：**小宇宙**（中文第一）、**Deezer**（欧洲流媒体）、**Player FM**（印度/新兴市场）、**Podcast Addict**（Android 重度用户）——这四类用户场景与大平台互补，边际成本低、覆盖增量明显。

---

### 3.8 已停服 / 已并入

| 平台 | 去向 |
|------|------|
| **Google Podcasts** | 2023-09 宣布关停 → 2024-04-02 美国停服 → 2024-06 全球停服，迁移至 YouTube Music |
| **Stitcher** | 并入 SiriusXM |
| **Breaker** | 2021-01 被 Twitter 收购，团队并入 Twitter Spaces，App 与网站当月下线 |
| **Anchor** | 更名 Spotify for Podcasters |
| **Gimlet / Parcast** | 2023-06 Spotify 裁员约 200 人，两厂牌合并重组并入 Spotify Studios，大量节目停更（非关停公司） |

> 注：**Luminary 未关停**——2023-04 曾大幅收缩（裁员、缩减节目，据 Bloomberg 报道），但公司/服务仍在运营，故未列入上表。

---

## 4. 平台转录相关能力矩阵

> 对播客转录工具（如 VOMO）而言，各平台的「可转录性」取决于：是否有 RSS、是否有原生转录、是否开放 API、是否支持视频。

| 平台 | RSS | 原生转录/文字稿 | API | 视频 | 对转录的意义 |
|------|-----|----------------|-----|------|-------------|
| Apple Podcasts | ✓ | ✓（付费订阅含文字稿） | 部分 | 起步 | RSS 下载量口径领先（英/加市场），文字稿为订阅卖点 |
| Spotify | ✓ | 有限 | Spotify for Podcasters | ✓ | 曲库最大，视频播客增长 |
| YouTube / YouTube Music | ✓（RSS 经第三方） | ✓（YouTube 自动字幕） | YouTube Data API / transcript API | ✓✓ | 转录第一入口，可粘贴链接获取 |
| Amazon Music | ✓ | ✗ | 有限 | ✗ | 依附 Prime，功能基础 |
| iHeartRadio | ✓ | ✗ | 有限 | ✗ | 自有内容优先 |
| 专用播放器（Overcast 等） | ✓ | ✗ | 多为本地 | 部分 | 纯消费端，转录靠外部工具 |
| 喜马拉雅等中文平台 | 私有协议 | 部分 | 开放 | 部分 | 生态封闭，转录入口为本地文件/链接 |

**结论**：RSS 是公开、标准、可程序化获取的播客内容通道；而 **YouTube 是唯一同时具备「海量播客内容 + 可粘贴链接转录」双属性的入口**，这与 VOMO 已有的 YouTube 转录功能直接契合。

### 4.1 各平台「缺口类型」（决定 L3 页怎么写）

| 缺口类型 | 平台 | 用户真实障碍 | L3 页叙事重点 |
|----------|------|--------------|---------------|
| **零功能** | Amazon Music / Audible、iHeartRadio、Overcast | 应用内完全没有 transcript | 「Text where there was none」 |
| **只读不可导出** | Spotify、Apple Podcasts | 有 auto-transcript 但不能 copy/download/跨集搜索 | 「Copy what {Platform} won't let you」 |
| **依赖发布者** | Pocket Casts | 仅 feed 附带时才显示，且不可导出 | 「Works for every episode, not just a lucky few」 |
| **创作者 SEO** | Podbean | 托管方转录有限；主播要索引与 show notes | 「SEO-ready show notes」 |
| **协议层** | RSS（全平台） | 各 App 限制不同，但音频同源 | 「One workflow for every app reading the feed」 |

> VOMO **不能**从 Spotify / Apple / Amazon 单集 URL 直接拉流。统一路径：**YouTube 同集链接** 或 **下载 MP3/M4A 后上传**。Spotify 独占集需在 FAQ 写明「需本地文件或录制」。

---

## 4.2 线上播客转录楔子（2026-08-23）

> **全量来源**：`https://vomo.ai/sitemap-en-0.xml` 中 `podcast-transcription` 共 **14** 条（含枢纽）。此前文档只记录 9 页，漏掉 Castbox、Business、Christian、True Crime、YouTube Podcast 五页。

### 4.2.1 两轴拆法

| 轴 | 数量 | 逻辑 | 示例 |
|----|------|------|------|
| **Platform（平台）** | 10 | 「我在哪个 App 听，但拿不到可导出文字稿」 | Spotify、Apple、Amazon、Castbox、YouTube Podcast |
| **Genre（体裁）** | 3 | 「这类节目内容密度高，转录后要搜名字/经文/数字」 | Business、Christian、True Crime |

两轴共用同一转录引擎；**Genre 页不写平台零功能故事**，写「这类音频转文字后要干什么」。

### 枢纽

| 路径 | 角色 | 主词 | 状态 |
|------|------|------|------|
| [`/podcast-transcription`](https://vomo.ai/podcast-transcription) | L2 枢纽 | podcast transcription、podcast to text、podcast transcript generator | 已上线 · sitemap ✓ |

枢纽内链（页脚/相关区实测）指向 **10** 个子页：Spotify、Apple、Amazon、iHeart、Podbean、Overcast、Pocket Casts、RSS、Business、YouTube Podcast。**未在枢纽露出**：Castbox、Christian、True Crime（仅 sitemap + SEO）。

> **URL 说明**：增长文档曾建议 `/tools/podcast-transcription`；**正式站为根路径 `/podcast-transcription/{slug}`**。旧 Tools 页应 301 或 canonical 到新簇。

### 4.2.2 平台子页（10）— 全量清单

| # | 平台 | slug | URL | 页型 | 核心缺口叙事 | Tools 导航 | sitemap |
|---|------|------|-----|------|--------------|------------|---------|
| 1 | Spotify | `spotify-podcast` | [/spotify-podcast](https://vomo.ai/podcast-transcription/spotify-podcast) | 巨头变体 | 应用内 auto-transcript 只读、不可导出 | ✗ | ✓ |
| 2 | Apple Podcasts | `apple-podcast` | [/apple-podcast](https://vomo.ai/podcast-transcription/apple-podcast) | 巨头变体 | 只读稿、旧集缺失、非 Apple 设备 | ✗ | ✓ |
| 3 | YouTube Podcast | `youtube-podcast` | [/youtube-podcast](https://vomo.ai/podcast-transcription/youtube-podcast) | 巨头变体 + **可 Paste YouTube** | 自动字幕无说话人/标点/导出；2–3 小时长播客 | 枢纽内链 ✓ | ✓ |
| 4 | Amazon Music | `amazon-music` | [/amazon-music](https://vomo.ai/podcast-transcription/amazon-music) | 上传 + Mock 预览 | **零** in-app transcript（含 Audible） | ✓ 下拉 | ✓ |
| 5 | iHeartRadio | `iheartradio` | [/iheartradio](https://vomo.ai/podcast-transcription/iheartradio) | 上传 + Mock 预览 | 无 transcript；多主持人 talk show | ✓ 下拉 | ✓ |
| 6 | Castbox | `castbox` | [/castbox](https://vomo.ai/podcast-transcription/castbox) | 巨头变体 + **可 Paste Castbox 链接** | AI Podcaster 仅部分节目、不可导出 | ✗ | ✓ |
| 7 | Podbean | `podbean` | [/podbean](https://vomo.ai/podcast-transcription/podbean) | 创作者/SEO | 托管方转录有限；主播要 SEO show notes | ✓ 下拉 | ✓ |
| 8 | Overcast | `overcast` | [/overcast](https://vomo.ai/podcast-transcription/overcast) | 上传 + Mock 预览 | 极简播放器，无 transcript 视图 | ✓ 下拉 | ✓ |
| 9 | Pocket Casts | `pocket-casts` | [/pocket-casts](https://vomo.ai/podcast-transcription/pocket-casts) | 上传 + Mock 预览 | 仅 feed 附带时显示；不可导出 | ✓ 下拉 | ✓ |
| 10 | RSS Feed | `rss-feed` | [/rss-feed](https://vomo.ai/podcast-transcription/rss-feed) | 协议层 | 所有 App 同源 feed，一层 workflow | ✓ 下拉 | ✓ |

**页型速记**（详见 [page-playbook.md](./page-playbook.md)）：

- **巨头变体**（Spotify、Apple、Castbox、YouTube Podcast）：Trending This Week ×4 + 双输入（YouTube / 部分可平台链）+ 扩展 FAQ
- **上传 + Mock**（Amazon、iHeart、Overcast、Pocket Casts）：英雄区对话示例 + 上传为主
- **创作者**（Podbean）：SEO / show notes 六卡
- **协议**（RSS）：「Every app, one workflow」

**输入能力差异（重要）**：

| 页 | 可直接粘贴的链接 |
|----|------------------|
| `youtube-podcast` | YouTube watch / youtu.be |
| `castbox` | Castbox share link（castbox.fm） |
| 其余平台页 | YouTube 同集 **或** 下载 MP3/M4A 上传（**不能**粘贴 Spotify/Apple URL） |

### 4.2.3 体裁子页（3）— 全量清单

| # | 体裁 | slug | URL | 主词 | 内容痛点 | 页型特征 | sitemap |
|---|------|------|-----|------|----------|----------|---------|
| 1 | Business | `business` | [/business](https://vomo.ai/podcast-transcription/business) | business podcast transcript | 数字、框架、可引用观点 → Notion/Docs 简报 | Mock **摘要 UI**（Key takeaway / Chapters / Notion-ready）；Export to Notion & Docs | ✓ |
| 2 | Christian | `christian` | [/christian](https://vomo.ai/podcast-transcription/christian) | christian podcast transcript / sermon transcript | 经文引用、讲道笔记、小组分享 | Mock 讲道片段 + 经文友好文案 | ✓ |
| 3 | True Crime | `true-crime` | [/true-crime](https://vomo.ai/podcast-transcription/true-crime) | true crime podcast transcript | 人名、日期、地点、可检索案情 | Mock **Case File** UI + 时间戳引用 | ✓ |

体裁页均有 **Trending This Week**（该体裁热门节目）+ 链回枢纽；**不进** Tools 下拉。

### 4.2.4 导航 vs sitemap 覆盖缺口

| 露出位置 | 包含的子页 |
|----------|------------|
| **Tools → Podcast Transcription 下拉（6）** | Amazon、iHeart、Podbean、Overcast、Pocket Casts、RSS |
| **枢纽内链（10）** | 上述 6 + Spotify、Apple、Business、YouTube Podcast |
| **仅 sitemap / SEO（3）** | Castbox、Christian、True Crime |

建议：Castbox 已上线，可补进 Tools 下拉或枢纽网格；Christian / True Crime 可在枢纽加「By Genre」入口。

### 4.2.5 与存量 URL 关系

| 存量 | 现状 | 处理 |
|------|------|------|
| `/use-case/podcast` | 薄解决方案页 | 导流或 canonical → `/podcast-transcription` |
| `/tools/podcast-transcript-generator` | 旧 SEO 模板页 | 301/合并 → 枢纽 |
| `/tools/ai-podcast-summarizer` | 摘要场景薄页 | 任务长尾或并入枢纽 Summary 模块 |
| `/tools/youtube-transcript` | YouTube 通用枢纽 | 通用 YouTube 转录；**视频播客**用 `/podcast-transcription/youtube-podcast`（已上线，加 podcast 话术 + 长集卖点） |
| 博客 [01-how-to-convert-podcast-to-blog-post](../blog/01-how-to-convert-podcast-to-blog-post.md) | 已链 YouTube 工具 | 更新内链指向 `/podcast-transcription` 枢纽 |

### Backlog（sitemap 尚未收录）

| 优先级 | 方向 | 建议 slug | 理由 |
|--------|------|-----------|------|
| P1 | Player FM | `player-fm` | 印度/新兴市场，零 transcript |
| P2 | Podcast Addict | `podcast-addict` | Android 重度用户 |
| P2 | 体裁：Comedy / News / Interview | `comedy` 等 | 可复用 True Crime 体裁模具 |
| P3 | 小宇宙 / 喜马拉雅 | `xiaoyuzhou` 等 | 中文生态；只能上传文件 |

**Castbox、YouTube Podcast、Business、Christian、True Crime 已上线** — 从 backlog 移除。

---

## 5. VOMO 播客转录场景

### 5.1 Persona 与 JTBD

| Persona | 核心任务（JTBD） | 痛点 |
|---------|------------------|------|
| **独立播客制作者** | 把节目转为 show notes / 博客文章 | 手动写文字稿耗时，节目 SEO 差 |
| **内容创作者（跨平台分发）** | 播客 → 字幕 / 图文 → 分发到 YouTube/小红书/SNS | 重复制作成本高 |
| **播客听众/研究者** | 把访谈、讲座转为可检索笔记 | 长节目难以回溯关键信息 |
| **媒体/出版机构** | 节目内容二次加工成文章/电子书 | 转录外包成本高、周期长 |

### 5.2 工作流映射

```
播客音频/视频（文件或 YouTube 链接）
        │
        ▼
   VOMO 转录 ── Whisper + Nova-2 双引擎 → 说话人标注 → 时间戳
        │
        ▼
   AI 处理 ── Smart Notes（摘要/要点/行动项）+ 播客专用模板
        │
        ▼
   产出与分发
     ├─ SRT 字幕 → 回传 YouTube / 视频平台
     ├─ 博客文章 / show notes → 发布回 Apple/Spotify 的 RSS 描述
     ├─ 社交媒体切片文案
     └─ 知识库 / 团队协作
```

### 5.3 VOMO 功能 ↔ 播客场景映射

| VOMO 功能 | 播客场景价值 | 对应平台机会 |
|-----------|--------------|-------------|
| 音频上传（MP3/WAV/M4A/MP4） | 转录任意已有播客文件 | Apple/Spotify/所有 RSS 节目 |
| 粘贴 YouTube 链接 | 转录视频播客，无需下载 | YouTube（使用量第一平台） |
| 播客专用会议模板 | 结构化 show notes 输出 | 内容创作者工作流 |
| 说话人识别 + 时间戳 | 多嘉宾访谈的分段检索 | 长节目内容管理 |
| 多格式导出（SRT/TXT/DOCX/PDF） | 字幕/博客/文档多用途 | 全平台回传分发 |
| Ask AI 对话式查询 | 从长节目快速提取观点/引用 | 内容二次加工 |
| VOMO CLI | 批量转录 + Agent 工作流 | 媒体机构/内容团队规模化 |

### 5.4 竞品在播客转录的做法（参考）

| 竞品 | 播客转录策略 | 对 VOMO 的启示 |
|------|--------------|----------------|
| **Descript** | 音视频编辑+转录一体，强调「编辑音频如编辑文档」 | VOMO 可突出「轻量、便宜、Bot-free」，不必做重编辑 |
| **Otter.ai** | 会议转录为主，播客转录为辅 | VOMO 用定价优势切入（$1.92/周 vs $16.99/月） |
| **Fireflies.ai** | 企业会议智能，集成 CRM | 与 VOMO 的创作者场景差异化 |
| **Snipd / Podtastic** | AI 高亮/摘要/剪片段，强调知识管理 | 提醒 VOMO 关注 AI 摘要差异化，但 VOMO 核心仍是转录质量 |

---

## 6. SEO 与内容机会

### 6.1 关键词层级与承接

| 层级 | 词性 | 示例 | 承接 |
|------|------|------|------|
| L2 枢纽 | 品类词 | podcast transcription, podcast to text, transcribe podcast | [`/podcast-transcription`](https://vomo.ai/podcast-transcription) |
| L3 平台 | 平台 × transcript | Spotify / Castbox / YouTube podcast transcript | `/podcast-transcription/{platform-slug}` |
| L3 体裁 | 体裁 × transcript | business / true crime / christian podcast transcript | `/podcast-transcription/{genre-slug}` |
| L4 任务 | 转录之后 | podcast to show notes, podcast to SRT, podcast to blog | 子页一节或 Guide |
| L3 交叉 | YouTube 通用 vs 播客 | YouTube transcript vs YouTube **podcast** transcript | `/tools/youtube-transcript` vs `/podcast-transcription/youtube-podcast` |

### 6.2 子页主词约定（13 页全表）

**平台轴（10）**

| slug | 主词 | FAQ 必答 |
|------|------|----------|
| `spotify-podcast` | Spotify podcast transcript | 应用内有稿但不能导出 |
| `apple-podcast` | Apple Podcasts transcript download | 只读 + 旧集缺失 + 非 Mac |
| `youtube-podcast` | YouTube podcast transcript | vs 自动字幕：无说话人/标点/导出 |
| `amazon-music` | Amazon Music podcast transcript | **完全没有** in-app transcript |
| `iheartradio` | iHeartRadio podcast transcript | 无 transcript 功能 |
| `castbox` | Castbox podcast transcript | AI Podcaster 不可导出；**可 Paste Castbox link** |
| `podbean` | Podbean podcast transcription | vs 平台有限自动转录 |
| `overcast` | Overcast podcast transcript | 播放器无 transcript 视图 |
| `pocket-casts` | Pocket Casts transcript | 仅发布者附带 + 不可导出 |
| `rss-feed` | podcast RSS transcript | 从 feed 下载 MP3 再上传 |

**体裁轴（3）**

| slug | 主词 | 内容卖点 |
|------|------|----------|
| `business` | business podcast transcript | 商业术语、摘要、Notion/Docs 导出 |
| `christian` | christian podcast transcript / sermon transcript | 经文引用、讲道笔记 |
| `true-crime` | true crime podcast transcript | 人名/日期/地点可检索 |

### 6.3 内容资产建议（更新后）

1. **全量 14 URL 已在英文 sitemap**（`sitemap-en-0.xml`，2026-08-23）— 补枢纽 By Platform / By Genre 网格，避免 Castbox / Christian / True Crime 成 orphan。
2. **旧 URL 收敛** — `/tools/podcast-transcript-generator` → 301；`/use-case/podcast` canonical。
3. **YouTube 双枢纽** — 通用 `/tools/youtube-transcript`；视频播客 `/podcast-transcription/youtube-podcast`；互链不抢主词。
4. **博客 L4** — 「How to export Spotify transcript」→ `spotify-podcast`；「Transcribe a sermon」→ `christian`。
5. **多语言** — 16 语言 sitemap 应同步 14 条（待抽样验证）。

---

## 7. 数据来源

| 数据点 | 来源 |
|--------|------|
| 美/英/加「最常用平台」份额 | Edison Research（UK Podcast Metrics Q1 2026）、Cumulus/Signal Hill 2026、Triton Digital 2026 |
| 下载量份额 | Triton Digital Canadian Podcast Report 2026、OP3 via Podnews |
| YouTube 播客数据 | Sounds Profitable（2026-07）、Search Engine Journal、Music Ally |
| 平台清单与 App 特色 | PCMag 2026、Inspire Fusion 2026、Similarweb Top Apps 2026 |
| VOMO 产品数据 | vomo.md、vomo-features.md（2026-07 更新） |
| 线上播客楔子全量 URL | `sitemap-en-0.xml`：**14** 条（1 枢纽 + 10 平台 + 3 体裁，2026-08-23） |

---

*遵循 [客户文档规范](../../demo/client-template.md)*
*关联：[主文档](../vomo.md) | [features](../vomo-features.md) | [use-cases](../vomo-use-cases.md) | [competitors](../vomo-competitors.md) | [keywords](../vomo-keywords.md) | [growth-strategy](../vomo-growth-strategy.md) | [page-playbook](./page-playbook.md) | [youtube-transcription](../youtube%20transcription/youtube-categories.md)*
*Last updated: 2026-08-23*
*创建日期: 2026-08-01*
*所属项目: VOMO（https://vomo.ai/）*
