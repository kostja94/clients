# Dubbing AI 网站结构（dubbingai.io）

> **站点根**：https://dubbingai.io/  
> **关联**：[dubbingai.md](./dubbingai.md) | [dubbingai-internal-links.md](./dubbingai-internal-links.md) | [dubbingai-features.md](./dubbingai-features.md) | [dubbingai-soundboard.md](./dubbingai-soundboard.md) | [dubbingai-voice-changer.md](./dubbingai-voice-changer.md)  
> **Skills 对齐**：**website-structure**（信息架构、Hub/详情）、**internal-links**（与全站内链文档配合）。

**用途**：描述 **线上站点层级与主要 URL**，供 SEO、内链、产品与文档对齐。**信息来源**：2026-06-22 对 **8 个子 sitemap + `/explore` 首包内链** 的自动化爬取（去重 **1646** URL）；辅以 [Explore 页](https://dubbingai.io/explore) Footer 矩阵对照。**站点改版后请更新本文**。

**URL / slug 命名总则**见 **第七节**（与 §1.1、第四～六节中的路径模式互参）。

---

## 〇、站点层级与 URL 校验

### 〇.1 树状层级（概览）

```
dubbingai.io/
├── /（首页）· /explore（长版营销 + 全站 Footer 矩阵）
├── 下载：/download-desktop · /download
├── 定价：/pricing
├── 支持：/questions（FAQ）· /supported-apps · /llm-info
├── 博客：/blog（主站路径）；blog.dubbingai.io（子域入口，与主站并存，见 §1.2）
├── Articles 程序化：/articles · /articles/catalog · /articles/{lang}/{compare|list|use-case}/{slug}
├── 使用场景：/use-cases/{slug}
├── 商业：/affiliate · /earbuds · shop.dubbingai.io（硬件）
├── 硬件：/dubbing-box · /dubbing-headphones
├── 竞品对比：/compare/dubbing-ai-vs-voice-ai
├── 法律与联系：/privacy-policy · /terms-of-use · /refund-policy · /contact-us
├── 产品线：/voice-cloning · /online-voice-changer · /soundboard · /sound-effect-generator · /sdk
├── 工具（Useful Tools）：/converter · /converter/{pair} · /vocal-remover · /instrumental-remover · /voice-recorder …
├── 移动端：/mobile-voice-changer
├── Community Sounds（主站导航）：/community-sounds · /community-sounds/{segment}
│   └── 子域 meow.dubbingai.io：/voices · /{segment}（segment 与主站一致，见 §4.1）
├── Voice Changer：/all-voice-changers · /voice-changer · /{name}-voice-changer · /voice-changer/{slug}
└── 音效长尾：/sound-gallery · /soundGallery/… · /sound-gallery/… · /upload-sound（两种风格并存，见第六节）
```

### 〇.2 Sitemap 与内链校验（2026-06-22）

**子 sitemap 清单**（`robots.txt` 已声明前 6 项；`/articles/sitemap.xml` 有效但未写入 robots）：

| Sitemap | URL 数 | 范围摘要 |
|---------|--------|----------|
| [`/sitemap.xml`](https://dubbingai.io/sitemap.xml) | 60 | 与 `www-sitemap.xml` 高度重叠：多语言首页、`/download`、`/affiliate`、`/questions`、政策页等 |
| [`/www-sitemap.xml`](https://dubbingai.io/www-sitemap.xml) | 60 | 同上（与根 sitemap 约 58 条重复） |
| [`/blog-sitemap.xml`](https://dubbingai.io/blog-sitemap.xml) | 83 | `/blog` + 82 篇博文 |
| [`/tools-sitemap.xml`](https://dubbingai.io/tools-sitemap.xml) | 451 | 在线工具 + `converter/*` 组合页 × 10 语言前缀 |
| [`/voice-changer-sitemap.xml`](https://dubbingai.io/voice-changer-sitemap.xml) | 389 | `/voice-changer` Hub、游戏/平台页、角色 spoke、多语言版 |
| [`/soundboard-sitemap.xml`](https://dubbingai.io/soundboard-sitemap.xml) | 187 | `/sound-gallery`、`/soundGallery/*`、`*-soundboard` 页 + 多语言版 |
| [`/meow-sitemap.xml`](https://dubbingai.io/meow-sitemap.xml) | 13 | **meow.dubbingai.io** 社区 segment（见 §4.1） |
| [`/articles/sitemap.xml`](https://dubbingai.io/articles/sitemap.xml) | 477 | Articles 程序化矩阵（见 §1.3） |

**合并去重**：**1646** URL（`dubbingai.io` 1631 + `meow.dubbingai.io` 13；子图之间 URL **几乎不重叠**）。

**Articles 类型分布**：`compare` 199 · `list` 120 · `use-case` 156 · 根 `/articles` + `/articles/catalog` 各 1。

**Voice Changer 英文抽样**：扁平游戏/平台页约 **15**；`/voice-changer/{slug}` 角色 spoke 约 **213**（sitemap 内，不含仅导航曝光页）。

### 〇.3 Explore 内链有、Sitemap 未收录（索引缺口）

以下路径在 [`/explore`](https://dubbingai.io/explore) **首包 HTML 内链**中出现，但 **8 个子 sitemap 均未包含**（2026-06-22）——线上可访问，但需依赖内链或手动提交才能被爬虫系统发现：

| 路径 | 说明 |
|------|------|
| `/explore` | 全站 Footer 矩阵母页 |
| `/download-desktop` | 主转化下载（`/download` 在 sitemap，`download-desktop` 不在） |
| `/all-voice-changers` | Voice Changer 聚合 Hub |
| `/community-sounds` 及 `/community-sounds/{segment}` | 主站 Community Sounds（segment 列表见第四节） |
| `/soundboard` · `/sound-effect-generator` · `/voice-cloning` | Footer Features / Tools 产品线 |
| `/sdk` · `/llm-info` | Resources / AI 说明 |
| `/earbuds` | Explore 内链硬件相关页 |

*首页 `https://dubbingai.io/` 同样不在任一 sitemap 中。*

### 〇.4 URL 抽样（历史，2026-04-07）

以下路径经 **HTTP 可访问**（返回页面内容）；**是否 301 合并、canonical 指向** 以浏览器开发者工具或 Search Console 为准。

| URL | 结果 | 备注 |
|-----|------|------|
| `https://dubbingai.io/explore` | 可访问 | 全站型 Footer |
| `https://dubbingai.io/questions` | 可访问 | FAQ |
| `https://dubbingai.io/converter` | 可访问 | 工具页；Footer 可能为轻量变体（§3.4） |
| `https://dubbingai.io/sdk` | 可访问 | §〇.3：sitemap 缺口 |
| `https://dubbingai.io/download-desktop` | 可访问 | §〇.3：sitemap 缺口 |
| `https://dubbingai.io/mobile-voice-changer` | 可访问 | 部分内页 Resources 出现；sitemap 未收录 |
| `https://dubbingai.io/blog` | 可访问 | 主站博客入口 |
| `https://blog.dubbingai.io/` | 可访问 | 子域根；与 `/blog` 并存 |
| `https://dubbingai.io/privacy-policy` | 可访问 | 法律页；robots 有 `Disallow`（见 §7.6） |

**HTTP 抽样（`curl -I`，2026-04-07）**：`/sound-effect-generator`、`/sound-effect-generator/whoosh`、`/community-sounds/memes`、`/sound-gallery/explosion-sound`、`/soundGallery/gojo-sound-effect`、`/de/`、`/zh/explore` → **200**；`/voice-changer/gojo` → **301** → `…/voice-changer/gojo/`；`/voicechanger/gojo` → **301** → `…/voice-changer/gojo`。详见 **第七节**。

---

## 一、顶层页面与角色

| URL | 角色 |
|-----|------|
| [`/`](https://dubbingai.io/) | 首页：主转化（下载）、产品价值与社交证明 |
| [`/explore`](https://dubbingai.io/explore) | **Explore**：长版营销落地 + 与首页同构的 Footer 导航矩阵；站内多处链向「Explore more」 |
| [`/download-desktop`](https://dubbingai.io/download-desktop) | 桌面客户端下载 |
| [`/llm-info`](https://dubbingai.io/llm-info) | 「Hey AI, know us better」—面向 LLM/检索增强的品牌说明（Footer 常见） |
| [`/questions`](https://dubbingai.io/questions) | **FAQ**（站外常称 FAQ，路径为 `questions` 非 `faq`） |
| [`/blog`](https://dubbingai.io/blog) | 博客 |
| [`/affiliate`](https://dubbingai.io/affiliate) | 联盟 / Partnership |
| [`/articles`](https://dubbingai.io/articles) | **Articles** 程序化 SEO 根（compare / list / use-case，见 §1.3） |
| [`/earbuds`](https://dubbingai.io/earbuds) | 硬件配件相关落地（Explore 内链；sitemap 未收录） |
| [`/supported-apps`](https://dubbingai.io/supported-apps) | 支持的应用列表 |
| [`/sdk`](https://dubbingai.io/sdk) | SDK |
| [`/converter`](https://dubbingai.io/converter) | Audio Converter（**非** `/audio-converter`） |
| [`/download`](https://dubbingai.io/download) | 下载落地（部分内页 CTA 使用；主站常用 **`/download-desktop`**） |
| [`/mobile-voice-changer`](https://dubbingai.io/mobile-voice-changer) | 移动端变声说明（部分内页 Resources 出现） |
| [`/pricing`](https://dubbingai.io/pricing) | 定价页：Free / Pro / Studio 三档方案 |
| [`/dubbing-box`](https://dubbingai.io/dubbing-box) | **Dubbing Box** 硬件落地页：口袋大小 AI 变声盒子（USB-C 直连手机/Switch/Xbox/PS5）|
| [`/dubbing-headphones`](https://dubbingai.io/dubbing-headphones) | **Dubbing Earbuds** 落地页：AI 变声耳机硬件 |
| [`/compare/dubbing-ai-vs-voice-ai`](https://dubbingai.io/compare/dubbing-ai-vs-voice-ai) | 竞品对比页：Dubbing AI vs Voice.ai |
| [`/privacy-policy`](https://dubbingai.io/privacy-policy) | 隐私政策 |
| [`/terms-of-use`](https://dubbingai.io/terms-of-use) | 使用条款 |
| [`/refund-policy`](https://dubbingai.io/refund-policy) | 退款政策 |
| [`/contact-us`](https://dubbingai.io/contact-us) | 联系我们 |

**中文站**（独立域名）：[dubbing.tech](https://dubbing.tech/) — Footer 标注为「dubbing ai cn」。

**硬件**：Dubbing Box → [shop.dubbingai.io](https://shop.dubbingai.io/)（商城）；主站 `/dubbing-box` 为营销落地页（见上表）。

### 1.1 Voice Changer：路径规范与别名（文档与内链须统一）

| 类型 | 推荐 canonical（Explore / 新版游戏页 / 面包屑） | 说明 |
|------|-----------------------------------------------|------|
| **游戏 / 平台** | `/{name}-voice-changer` | 例：`/valorant-voice-changer`、`/fortnite-voice-changer`、`/discord-voice-changer` |
| **角色 / IP** | `/voice-changer/{slug}` | 例：`/voice-changer/gojo`、`/voice-changer/jett/`（**`voice-changer` 两段之间带连字符**） |
| **历史别名** | `/voicechanger/{slug}`（**无** `voice` 与 `changer` 之间的连字符） | 线上可能仍解析；**SEO 文案、内链、sitemap 以带连字符及上表格式为准**，避免混写 |

### 1.2 博客：主站路径与子域并存

- **主站**：[`/blog`](https://dubbingai.io/blog) — Explore / 多数 Footer 的「Blog」指向此路径。
- **子域**：[`blog.dubbingai.io`](https://blog.dubbingai.io/) — 根路径可访问；部分 **工具页** Footer 的 Blog 链到子域（见 §3.4）。
- **文档建议**：内链与文案优先写 **`https://dubbingai.io/blog`**；若需统一重复内容策略，以线上 **canonical** 与 **GSC** 为准。

### 1.3 Articles 程序化矩阵

- **根与目录**：[`/articles`](https://dubbingai.io/articles)、[`/articles/catalog`](https://dubbingai.io/articles/catalog)
- **URL 模式**：`/articles/{lang}/{type}/{slug}`
  - **`type`**：`compare`（竞品对比）、`list`（榜单/清单）、`use-case`（场景）
  - **`lang`**（sitemap 内）：`ar`、`de`、`en`、`es`、`fr`、`pt`（各约 79–80 条 spoke）
- **Sitemap**：[`/articles/sitemap.xml`](https://dubbingai.io/articles/sitemap.xml)（477 URL，元数据最规范；**未**写入 `robots.txt`）
- **与 `/blog` 分工**：`/blog` 为 Ghost 博文；`/articles` 为独立程序化 SEO 矩阵，二者 URL 空间不重叠。

### 1.4 Use Cases（使用场景）

- **URL 模式**：`/use-cases/{slug}`
- **现有 slug**：
  | slug | 标签 | 简介 |
  |------|------|------|
  | `gaming` | Gaming | 竞技玩家与队友场景 |
  | `streaming` | Streaming | Twitch、YouTube、Kick 创作者 |
  | `vtubing` | VTubing | 虚拟主播保护真实声音 |
  | `privacy-and-security` | Privacy & Security | 保护语音身份隐私 |
- **页面结构**：Why（为什么用）、Scenarios（场景卡片）、HowTo（操作步骤）、FAQ、Final CTA
- **与 Articles 的区分**：`/use-cases/{slug}` 为产品营销场景页（少量人工精选）；`/articles/{lang}/use-case/{slug}` 为程序化 SEO 长尾矩阵（156 条）。二者 URL 空间不重叠。

### 1.5 Compare（竞品对比页）

- **URL 模式**：`/compare/{a}-vs-{b}`（kebab-case）
- **现有页面**：`/compare/dubbing-ai-vs-voice-ai` — Dubbing AI vs Voice.ai 专项对比
- **页面结构**：Hero（标题+摘要）、竞品能力环（雷达/双栏）、逐一规格对比表、推荐场景、迁移步骤、FAQ

---

## 二、主导航产品线（顶栏语义）

与 [dubbingai-features.md](./dubbingai-features.md) 一致，线上通常为：

- **Voice Changer**：变声主产品线（桌面端为核心）
- **Soundboard**：音效板能力 + 与 Community Sounds 联动
- **Community Sounds**：下拉进入各 **内容分类**（见第四节）
- **SDK**
- **Useful Tools**：下拉为各 Web 工具（见第三节）

*具体标签以线上为准。*

---

## 三、Footer：Features / Resources / Useful Tools（与 Explore 一致）

以下为 [Explore](https://dubbingai.io/explore) 页脚 **三组固定区块**（多数内页复用）。**顺序与文案**以产品为准。

### 3.1 Features

| 链接文案 | URL |
|----------|-----|
| Online Voice Changer | `/online-voice-changer` |
| Community Sounds | `/community-sounds` |
| Voice Cloning | `/voice-cloning` |

### 3.2 Resources

| 链接文案 | URL |
|----------|-----|
| Article | `/articles` |
| SDK | `/sdk` |
| Soundboard | `/soundboard` |
| Affiliate | `/affiliate` |
| FAQ | `/questions` |
| Blog | `/blog` |
| Supported Apps | `/supported-apps` |
| All Voice Changers | `/all-voice-changers` |

*部分页面 Resources 区另含 **Mobile Voice Changer**、**Download** 等，以线上为准。*

### 3.3 Useful Tools

| 链接文案 | URL | 备注 |
|----------|-----|------|
| Online Voice Changer | `/online-voice-changer` | 与 Features 重复入口，常见 |
| Vocal Remover | `/vocal-remover` | |
| Instrumental Remover | `/instrumental-remover` | |
| Voice Recorder | `/voice-recorder` | |
| Audio Converter | `/converter` | |
| Sound Effect Generator | `/sound-effect-generator` | |
| Utell Accent Conversion | `https://utell.ai/` | 外链 |
| Voice Cloning | `/voice-cloning` | |
| Monica AI Image | `https://monica.im/image-tools/ai-image-generator-from-text?utm_source=dubbing_ai` | 外链（线上 Footer 可能出现双斜杠 `//image-tools`，以实际为准） |

### 3.4 Footer 变体（全站矩阵 vs 工具页轻量）

| 形态 | 典型页面 | 说明 |
|------|----------|------|
| **全站 Explore 型** | `/explore`、首页、`/blog` 等 | 与 **§3.1～§3.3** 一致；Resources 中 Blog 多为 **`/blog`**。 |
| **工具页轻量** | 如 `/converter` | 仍含 Features / Resources / Useful Tools 等区块，但 **Blog** 可能链到 **`blog.dubbingai.io`**；页脚或区块中另含 **法律与联系**：`/privacy-policy`、`/terms-of-use`、`/refund-policy`、`/contact-us`（与 §一表格一致）。 |

*改版后以线上为准；内链文档写作时：优先引用 **主站路径**，并知悉工具页可能展示子域 Blog。*

---

## 四、Community Sounds：分类 segment（线上）

### 4.1 主站路径（导航 / 内链）

路径：`/community-sounds/{segment}`。下列 segment 与 [Explore Footer](https://dubbingai.io/explore) **Community Sounds** 列表一致（2026-06-22 内链校验）。

| 展示名 | `segment` | 备注 |
|--------|-----------|------|
| Memes | `memes` | |
| Music | `music` | |
| Games | `games` | |
| Anime | `anime` | |
| SFX | `sfx` | |
| Tiktok | `tiktok` | |
| Random | `random` | |
| Funny | **`funnist`** | 线上 canonical segment 为 **`funnist`**（非 `funny`）；内链与文档须与此一致，见 [dubbingai-soundboard.md](./dubbingai-soundboard.md) §8.0 |
| Creepy | `creepy` | |
| Movies | `movies` | |
| Sports | `sports` | |
| Other | `other` | |

### 4.2 子域 meow.dubbingai.io（sitemap 收录）

[`meow-sitemap.xml`](https://dubbingai.io/meow-sitemap.xml) 收录 **meow.dubbingai.io** 上的扁平 segment 路径（**非** `/community-sounds/` 前缀）：

| 展示名 | meow 路径 | 对应主站 segment |
|--------|-----------|------------------|
| （Voices 总览） | `/voices` | — |
| Memes … Other | `/{segment}` | 与 §4.1 表相同（含 **`funnist`**） |

**注意**：主站 `/community-sounds/*` 与 meow 子域 `/{segment}` **内容体系相关但 URL 不同**；主站 Community 路径 **不在** dubbingai.io sitemap 中（见 §〇.3）。

---

## 五、Voice Changer：Footer 曝光入口（Explore 节选）

以下为 Explore 页 **Voice Changer** 列表现网 URL（游戏/平台/角色混合；完整列表以 [All Voice Changers](https://dubbingai.io/all-voice-changers) 为准）。

| 类型 | 示例路径 |
|------|----------|
| 游戏 / 平台 | `/league-of-legends-voice-changer`、`/valorant-voice-changer`、`/dota2-voice-changer`、`/fortnite-voice-changer`、`/csgo-voice-changer`、`/steam-voice-changer`、`/discord-voice-changer`、`/obs-voice-changer`、`/zoom-voice-changer`、`/roblox-voice-changer`、`/vrchat-voice-changer`、`/whatsapp-voice-changer`、`/apex-voice-changer`、`/pubg-voice-changer`、`/lethal-company-voice-changer` |
| 角色 / IP | `/voice-changer/gojo`、`/voice-changer/cod/`、`/voice-changer/jojo/`、`/voice-changer/spacemarine/` |

**聚合 Hub**：[`/all-voice-changers`](https://dubbingai.io/all-voice-changers)

---

## 六、Sound Effects / Sound Gallery（长尾音效页）

线上存在 **两种 URL 风格并存**（站内核验 canonical 与主入口时需注意）：

| 风格 | 示例 | 说明 |
|------|------|------|
| `soundGallery`（驼峰路径） | `/soundGallery/gojo-sound-effect`、`/soundGallery/minecraft-sound-effect` | Explore Footer 中部分条目 |
| `sound-gallery`（短横线） | `/sound-gallery/fart-sound/`、`/sound-gallery/vine-boom-sound` | 同板块内混用 |
| `*-soundboard` | `/sound-gallery/donald-trump-soundboard`、`/sound-gallery/fnaf-soundboard` | soundboard-sitemap 收录 |
| 上传入口 | `/upload-sound` | soundboard-sitemap 收录 |

**聚合入口**：[`/sound-gallery`](https://dubbingai.io/sound-gallery)（Hub；各语言版如 `/de/sound-gallery` 亦在 sitemap）。

程序化 SEO 与内链策略见 [dubbingai-soundboard.md](./dubbingai-soundboard.md) 第一节、第八节。

---

## 七、URL 与 slug 规则（全站）

本节归纳 **可访问路径上的模式**（非站内全部组合枚举）。**canonical、hreflang、重复 URL** 以线上标签与 Search Console 为准。

### 7.1 域名与路径风格

| 维度 | 规则 |
|------|------|
| **主站** | `https://dubbingai.io`，路径 **小写**；多段使用 **kebab-case**（短横线连接）。 |
| **并存入口** | **博客**：`/blog` 与 `https://blog.dubbingai.io/`（见 §1.2）。**中文品牌站**：`dubbing.tech`（Footer「cn」）。**硬件商城**：`shop.dubbingai.io`。 |
| **外链工具** | Footer 常见 `utell.ai`、`monica.im`（带 `utm_source`），**不属于** `dubbingai.io` 路径规则。 |

### 7.2 多语言 URL 前缀

首页 HTML 暴露 `hreflang`：**根路径英文** + 下列语言子路径（前缀 **`/{lang}/`**，其后接站内同类路径）：

`de`、`fr`、`jp`、`ru`、`es`、`pt`、`it`、`kr`、`zh`、`tr`（sitemap / tools 子图均用 **`jp`** 作日语前缀）。

**并存**：Explore 内链亦出现 **`/ja`**，与 **`/jp`** 均可 **200**（内容等价，canonical 以线上标签为准；文档内链宜与目标页实际 URL 一致，勿混写）。

### 7.3 全站 URL 模式总表（slug 段含义）

| 页面类型 | URL 模式 | `slug` / 段约定 | 备注 |
|----------|----------|-----------------|------|
| **静态 / 营销** | `/{page}` | 单词或短横线词组 | 例：`explore`、`download-desktop`、`questions`、`sound-effect-generator` |
| **Voice Changer · 游戏/平台** | `/{name}-voice-changer` | `name` = 游戏或平台名 kebab | 扁平单段；抽样 `/valorant-voice-changer` 与 `…/` 均 **200**，内链与 canonical 宜统一一种 |
| **Voice Changer · 角色/系列** | `/voice-changer/{slug}/` | `slug` 小写 kebab | **canonical 多为带尾斜杠**；无斜杠 **301** 至带斜杠（抽样 Gojo） |
| **Voice Changer · 历史别名** | `/voicechanger/{slug}` | 同左 | **301** 至 `/voice-changer/{slug}` 再至带 `/`（见 §1.1） |
| **Use Cases** | `/use-cases/{slug}` | `slug` = `gaming`、`streaming`、`vtubing`、`privacy-and-security` | 产品营销场景页（§1.4），非 `/articles` 程序化矩阵 |
| **Compare** | `/compare/{a}-vs-{b}` | kebab | 竞品对比例：`/compare/dubbing-ai-vs-voice-ai`（§1.5） |
| **Pricing** | `/pricing` | — | 定价页：Free / Pro / Studio |
| **Hardware** | `/dubbing-box` · `/dubbing-headphones` | — | Dubbing Box / Dubbing Earbuds 硬件营销落地 |
| **Hub · Voice** | `/all-voice-changers` | — | 聚合列表 |
| **Community Sounds** | `/community-sounds` · `/community-sounds/{segment}` | `segment` 见第四节表；**Funny → `funnist`** | 分类单段 |
| **Sound Effect Generator** | `/sound-effect-generator` · `/sound-effect-generator/{slug}` | `{slug}` = 类型 kebab（如 `whoosh`、`horror`、`ui-element`） | 详见 [dubbingai-sound-effect-generator.md](./dubbingai-sound-effect-generator.md) §4、§10.1 |
| **Sound Gallery（长尾）** | `/soundGallery/{name}-sound-effect` **或** `/sound-gallery/{…-sound-effect/}` **或** `/sound-gallery/{…-sound}` **或** `/sound-gallery/{name}-soundboard` | 驼峰目录与短横线目录**并存**；尾缀 `-sound-effect`、`-sound`、`-soundboard` 混用 | 内链与 sitemap 统一时需逐条对齐 |
| **Articles 程序化** | `/articles` · `/articles/catalog` · `/articles/{lang}/{compare\|list\|use-case}/{slug}` | `lang`：ar/de/en/es/fr/pt | 见 §1.3；sitemap 477 条 |
| **Blog 文章** | `/blog/{post-slug}/` | kebab | `blog-sitemap.xml` 83 条 |
| **meow 社区** | `https://meow.dubbingai.io/{segment}` | segment 同 §4.1 | `meow-sitemap.xml` |
| **法律与联系** | `/privacy-policy`、`/terms-of-use`、`/refund-policy`、`/contact-us` | 固定文件名 | 见 §一 |

### 7.4 slug 字符与语义约定

- **字符集**：`a-z`、`0-9`、连字符 `-`；**不写**空格与下划线于路径中。
- **大小写**：路径段 **一律小写**（避免大小写重复 URL）。
- **连字符**：多词合成用 **kebab**（`league-of-legends-voice-changer`、`goofy-ahh-sound-effect`）。
- **例外与坑**：Community Sounds 的 Funny 类线上 segment 为 **`funnist`**（非 `funny`）。`soundGallery` 为 **驼峰路径段**，与 `sound-gallery` 并存，**勿**在文档中假设单一风格。

### 7.5 尾随斜杠与 301（抽样结论）

| 路径模式 | 行为（HEAD 抽样） |
|----------|-------------------|
| `/voice-changer/{slug}`（无尾 `/`） | **301** → 同路径 **带尾斜杠** |
| `/voice-changer/{slug}/` | **200** |
| `/voicechanger/{slug}` | **301** → `/voice-changer/{slug}`（再跳转到带 `/`） |
| `/{game}-voice-changer` 与 `…/` | 抽样 **均为 200** → 需依赖 **canonical** 去重 |
| `/community-sounds/memes` 与 `…/memes/` | 抽样 **均为 200** |

### 7.6 robots.txt 与 sitemap

**[`/robots.txt`](https://dubbingai.io/robots.txt)**（2026-06-22 复测）要点：

```
User-agent: *
Allow: /
Disallow: /sounds/
Disallow: /login/
Disallow: /terms-of-policy
Disallow: /privacy-policy

Sitemap: https://dubbingai.io/sitemap.xml
Sitemap: https://dubbingai.io/blog-sitemap.xml
Sitemap: https://dubbingai.io/tools-sitemap.xml
Sitemap: https://dubbingai.io/meow-sitemap.xml
Sitemap: https://dubbingai.io/soundboard-sitemap.xml
Sitemap: https://dubbingai.io/voice-changer-sitemap.xml
```

| 项 | 现状（2026-06-22） |
|----|-------------------|
| **根 `/sitemap.xml`** | ✅ 返回 **有效 XML**（60 URL），与 `www-sitemap.xml` 高度重叠；**非** sitemap index |
| **子 sitemap** | ✅ 8 路有效（见 §〇.2）；合计去重 **1646** URL |
| **robots 未声明** | ⚠️ [`/articles/sitemap.xml`](https://dubbingai.io/articles/sitemap.xml)（477 URL）、[`/www-sitemap.xml`](https://dubbingai.io/www-sitemap.xml) |
| **索引缺口** | ⚠️ 首页、`/explore`、产品线 Hub（`/soundboard`、`/sound-effect-generator` 等）、主站 `/community-sounds/*` 等 **不在任一 sitemap**（§〇.3） |
| **Disallow 冲突** | `Disallow: /privacy-policy` 与 sitemap 内 `/privacy-policy` 并存；以 GSC 实测为准 |
| **历史笔误** | `Disallow: /terms-of-policy` vs 现用 `/terms-of-use` |

*历史诊断（2026-06-04 根 sitemap 返回 HTML）见 [_archive/dubbingai-io-sitemap-diagnosis.md](./_archive/dubbingai-io-sitemap-diagnosis.md)。*

### 7.7 与专项文档的分工

| 主题 | 文档 |
|------|------|
| Voice Changer 程序化 spoke、关键词 | [dubbingai-voice-changer.md](./dubbingai-voice-changer.md) |
| Sound Effect Generator 分类 slug 全表 | [dubbingai-sound-effect-generator.md](./dubbingai-sound-effect-generator.md) §10.1 |
| Community Sounds 内容、Evidence | [dubbingai-soundboard.md](./dubbingai-soundboard.md) |
| 内链锚文本与 Hub–Spoke、Sitemap 缺口 | [dubbingai-internal-links.md](./dubbingai-internal-links.md) **§十** |

---

## 八、与内部文档的对应关系

| 主题 | 文档 |
|------|------|
| 全站内链、固定区块 vs 上下文、Sitemap 配合 | [dubbingai-internal-links.md](./dubbingai-internal-links.md) **§十** |
| Community Sounds 内容模板、Evidence | [dubbingai-soundboard.md](./dubbingai-soundboard.md) |
| Voice Changer 程序化 spoke | [dubbingai-voice-changer.md](./dubbingai-voice-changer.md) |
| Sound Effect Generator | [dubbingai-sound-effect-generator.md](./dubbingai-sound-effect-generator.md) |
| 关键词 → URL | [dubbingai-keywords.md](./dubbingai-keywords.md) |

---

## 九、文档导航

| 文档 | 用途 |
|------|------|
| [dubbingai.md](./dubbingai.md) | 主文档、产品上下文 |
| **本文档** | **线上网站结构、主要 URL、Footer 矩阵、第七节 URL/slug 规则** |
| [dubbingai-internal-links.md](./dubbingai-internal-links.md) | 内链策略、跳转逻辑、**Sitemap×内链（§十）** |
| [dubbingai-soundboard.md](./dubbingai-soundboard.md) | Soundboard / Community Sounds SEO |
| [dubbingai-voice-changer.md](./dubbingai-voice-changer.md) | Voice Changer SEO |

---

## 十、Affiliate 页面参考（/affiliate）

| 字段 | 内容 |
|------|------|
| **Meta Title** | Dubbing AI Affiliate Program \| Earn Up to 30% Commission Promoting Voice Changer Tools |
| **Meta Description** | Join Dubbing AI's affiliate program to earn 10%-30% commissions promoting real-time voice changers and soundboards. Perfect for streamers, gamers, and content creators. Apply today! |
| **佣金** | 10%–30% recurring |
| **审核周期** | 约 7 天 |
| **目标受众** | 游戏主播、内容创作者、科技测评 |
| **内链建议** | 首页、/online-voice-changer、OBS/Steam/VRChat 平台页、Blog 教程 |

---

### 文档修订

| 日期 | 说明 |
|------|------|
| 2026-04-07 | 初版：依据 [dubbingai.io/explore](https://dubbingai.io/explore) Footer 与路径校验；标注 `funnist`、`/questions`、`/converter`、soundGallery 混用 |
| 2026-04-07 | 增补 §1.1 Voice Changer 路径规范（`/{game}-voice-changer` vs `/voice-changer/{角色}` vs `/voicechanger/*` 别名）、`/download`；关键词与竞品表 URL 已对齐 |
| 2026-04-07 | 增补 §〇 树状层级与 URL 校验表；§1.2 博客双入口；顶层法律页与 `/mobile-voice-changer`；§3.4 Footer 全站型 vs 工具页轻量 |
| 2026-04-07 | 新增 **第七节 URL 与 slug 规则**：多语言前缀、全站模式总表、尾随斜杠/301 抽样、robots 与 sitemap 说明、§〇.2 与 HTTP 抽样互链 |
| 2026-06-22 | **Sitemap + Explore 内链全量爬取**：§〇.2–§〇.3 子 sitemap 清单（1646 URL）、索引缺口表；新增 §1.3 Articles、§4.2 meow 子域；更新 §7.2（`jp`/`ja`）、§7.6 robots/sitemap 现状；第六节增补 `*-soundboard`、`/upload-sound` |
| 2026-06-22 | §3.2 Resources 增 **Article → `/articles`**（Explore 现网） |
| 2026-07-06 | **补充代码库已有页面**：§一新增 `/pricing`、`/dubbing-box`、`/dubbing-headphones`、`/compare/dubbing-ai-vs-voice-ai`；新增 §1.4 Use Cases（4 个 slug）、§1.5 Compare（竞品对比页结构）；更新 §〇.1 树状层级、§7.3 URL 模式总表 |
