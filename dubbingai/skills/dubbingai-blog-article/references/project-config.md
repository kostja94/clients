## §1 项目配置与 G1–G7 阻断规则

> **Distilled for dubbingai-blog-article v1.2.1 · source audit 2026-06-16**

### 1.1 项目配置

| 配置项 | Dubbing AI 值 |
|--------|---------------|
| **品牌/产品名** | Dubbing AI |
| **内部昵称** | 大饼（团队内部，正文不出现） |
| **主域名** | dubbingai.io |
| **中文站** | dubbing.tech（本 skill 不写中文正文） |
| **博客 URL** | `https://dubbingai.io/blog/{slug}` |
| **博客双入口** | 主站 `/blog` 与子域 `blog.dubbingai.io` 并存；内链优先主站路径 |
| **品类 one-liner** | Real-time AI voice changer + soundboard for gamers, streamers, creators |
| **双核心** | Real-time Voice Changer + Soundboard |
| **Hero 数据（须 as-of）** | 500+ character voices · 100,000+ meme sounds · <30ms latency · <3% CPU · 40+ languages |
| **硬件差异化** | Dubbing Box（shop.dubbingai.io）— Android/Switch/Xbox/PS5/PC；竞品无同类硬件 |
| **Primary ICP** | 游戏玩家、Twitch/YouTube 主播、Discord 用户 |
| **Secondary ICP** | VRChat/Roblox 创作者、短视频创作者、会议娱乐用户 |
| **作者默认** | `Kostja` |
| **CTA 主链** | `https://dubbingai.io/download-desktop` |
| **CTA 次级** | `/` · `/discord-voice-changer` · `/online-voice-changer` |
| **语言/市场** | 英文正文；B2C US/global |
| **禁止内链** | `/alternatives/*`（待建）· `/faq`（用 `/questions`）· forthcoming ≤1 且仅 Related |

### 1.2 G1–G7 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、定价与 dubbingai.io 矛盾 | 对照 `product-competitors.md` + `proof-gate.md` |
| **G2** | 死链 | 站内/站外 404 或域名拼写错误 | 对照 §1.4 白名单；FAQ 必须 `/questions` |
| **G3** | 无来源数字 | 量化 claim 无 attribution | P0 须 Source URL 或 as-of 官网表述 |
| **G4** | 竞品/品类错误 | Voicemod 定价、Voice.ai 社区规模、Murf 实时能力错误 | 官方 docs 验证 |
| **G5** | 产品能力夸大 | Dubbing Box「全平台零配置」、延迟保证泛化 | 区分 Desktop vs 硬件场景 |
| **G6** | 内链未上线 | 链禁止列表或 forthcoming 正文核心流程 | forthcoming ≤1 · Related 脚注 only |
| **G7** | 品牌/合规风险 | 名人/政治声音冒充教唆、贬低竞品无据 | 禁 "impersonate for fraud"；对比须公平 |

### 1.3 双核心意图 → 落地页

| 用户意图 | 动作词 | 主链目标 |
|---------|--------|---------|
| **下载实时变声** | download, install, desktop, gaming | `/download-desktop` · `/` |
| **Discord 设置** | Discord voice, virtual mic | `/discord-voice-changer` · `/blog/how-to-change-your-voice` |
| **在线/上传** | online, upload, browser | `/online-voice-changer` |
| **现成 meme 音效** | soundboard, meme sounds, download sfx | `/community-sounds` · `/soundboard` |
| **AI 生成音效** | generate sfx, text to sound | `/sound-effect-generator`（禁当 community-sounds） |
| **克隆** | voice cloning, custom voice | `/voice-cloning` |
| **硬件/主机** | PS5, mobile, Switch, Xbox | `https://shop.dubbingai.io/` · `/supported-apps` |
| **角色 preset** | Gojo, Jett, anime voice | `/voice-changer/{slug}` · `/all-voice-changers` |
| **FAQ** | support, questions | `/questions` |
| **选型 hub** | best AI voice changer | `/blog/best-ai-voice-changer` |

### 1.4 可链接 URL 白名单

| 类型 | 路径 |
|------|------|
| 博客（Track S） | `/blog/best-ai-voice-changer` · `/blog/how-to-change-your-voice` · `/blog/how-to-change-google-assistant-voice` · `/blog/{slug}` |
| 首页 / 下载 | `/` · `/download-desktop` · `/explore` |
| Articles | `/articles` · `/articles/catalog` · `/articles/{lang}/{compare|list|use-case}/{slug}` |
| 平台页 | `/discord-voice-changer` · `/zoom-voice-changer` · `/vrchat-voice-changer` · `/fortnite-voice-changer` · `/valorant-voice-changer` · `/roblox-voice-changer` |
| 功能 | `/voice-changer` · `/all-voice-changers` · `/voice-changer/{slug}` · `/voice-cloning` · `/online-voice-changer` · `/soundboard` · `/community-sounds` · `/sound-effect-generator` · `/supported-apps` |
| 硬件 | `https://shop.dubbingai.io/` · `/earbuds` |
| FAQ | `/questions` |
| SDK | `/sdk` |
| Agent 信息 | `/llm-info` |

**内链格式**：Markdown `[锚文本](https://dubbingai.io/path)` 或相对 `/path`；slug **不含** `NN-` 文件名前缀。

### 1.5 废弃路径（勿链）

| 废弃 | 替代 |
|------|------|
| `/faq` | `/questions` |
| `/alternatives/voicemod`（待建） | 博客 Alternative 文 + 竞品外链 |
| `top-5-voice-changers`（301 源） | `/blog/best-ai-voice-changer` |

### 1.6 Trust 表述（可写 / 禁写）

| 可写 | 禁写 |
|------|------|
| 500+ voices, 100k+ sounds（as of 官网） | 「1000 tones」等过时 CMS 数字 |
| <30ms latency, <3% CPU（ marketed；建议用户自测） | 保证所有 PC 达标 |
| Dubbing Box 支持 listed consoles/mobile | 所有手机免配置实时变声 |
| Voicemod Pro ~$50/yr（有来源） | Voicemod「声音少/不如 Dubbing」无据贬低 |
| Murf 适合录制/旁白 | Murf 适合 live Discord gaming |

### 1.7 Frontmatter 双模板

> **2026-08-11 起废弃**：`image` / `keywords` / `related` 不再写入 frontmatter（image 由 CMS 单独管理；keywords/related 由正文内链与 CMS 配置承载）。

**Track S**

```yaml
---
title: "{H1-aligned title}"
description: "{140–160 chars; primary keyword in first 80 chars}"
slug: "{url-slug-without-year}"
date: {YYYY-MM-DD}          # 发布时间，永不改变
updated: {YYYY-MM-DD}       # 可选；最近一次实质性内容更新；无更新则省略
author: Kostja
---
```

**Track C**

```yaml
---
title: "..."
description: "..."
slug: "{url-slug}"
date: {YYYY-MM-DD}          # 发布时间，永不改变
updated: {YYYY-MM-DD}       # 可选；最近一次实质性内容更新；无更新则省略
author: Kostja
category: "{soundboard-tips|sound-effect-tips|voice-changer-tips|voice-actors|voice-changer-review}"
lang: "en"
status: "published"
source: "cms"
canonical: "https://dubbingai.io/blog/{slug}/"
migrated_at: {YYYY-MM-DD}
superseded_by: ""
---
```

> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅**实质性更新**（新增数据/章节/修正事实）时更新，错别字/样式不动它。页面**只显示一个日期**（有 `updated` 显示它）——勿同时显示两个日期（实证导致 CTR 下跌）。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。

### 1.8 Track S 内链硬性要求（Hub-Spoke 网络：1 Hub + 4 Spokes）

> Canonical Registry 以 `content-graph.md` §4.4 为准。

| slug | 建议正文互链（原 `related`） | 首段分流 | 最低 blog 互链 |
|------|----------------|---------|:---:|
| `best-ai-voice-changer`（#01 Hub） | `how-to-change-google-assistant-voice`, `how-to-change-your-voice`, `dubbing-ai-vs-voicemod` | 选型 vs Assistant vs 实操 vs 对比 | ≥3 |
| `how-to-change-google-assistant-voice`（#02 IntentSplit） | `best-ai-voice-changer`, `how-to-change-your-voice` | Assistant TTS ≠ live mic | ≥2 |
| `how-to-change-your-voice`（#03 HowTo） | `best-ai-voice-changer`, `how-to-change-google-assistant-voice`, `dubbing-ai-vs-voicemod` | Job A live vs Job B file；选型/Assistant/对比分流 | ≥3 |
| `dubbing-ai-vs-voicemod`（#04 Alternative） | `best-ai-voice-changer`, `how-to-change-your-voice`, `how-to-change-google-assistant-voice` | Hub 对比深潜；Assistant 误搜分流 | ≥3 |

新 Track S 稿：首段或第二段 ≥1 blog 互链；正文 blog 互链 1–4 条；产品内链分散在不同 H2。
