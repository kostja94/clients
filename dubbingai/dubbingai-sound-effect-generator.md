# Dubbing AI Sound Effects 与 Sound Effect Generator（术语 + 程序化 SEO + 页面落地）

> 关联：[dubbingai.md](./dubbingai.md) | [dubbingai-site-structure.md](./dubbingai-site-structure.md) | [dubbingai-internal-links.md](./dubbingai-internal-links.md) | [dubbingai-features.md](./dubbingai-features.md) | [dubbingai-soundboard.md](./dubbingai-soundboard.md) | [dubbingai-keywords.md](./dubbingai-keywords.md) | 基于官网 [dubbingai.io](https://dubbingai.io/)  
> 基于 Skills：**keyword-research**、**competitor-research**、**programmatic-seo**、**landing-page**（活动/工具落地转化结构）、**template-page**（Hub vs 分类详情、模板+数据）、**internal-links**（站内互链）。**全站导航/Footer/跨产品线跳转**见 [dubbingai-internal-links.md](./dubbingai-internal-links.md)；**本工具 Hub + 分类页区块、验收与埋点**见 **第六节、第七节、第十一节**；**长尾分类营销页**合并模板与数据字段见 **§11.4**，文案公式与上线验收见 **§11.5–§11.9**。

**用途**：

1. **术语**：统一 **sound effects** 与 **soundboard** 的表述；说明 **Sfx** 分类与产品关系；与 [dubbingai-soundboard.md](./dubbingai-soundboard.md) 配合使用。  
2. **Sound Effect Generator**（[sound-effect-generator](https://dubbingai.io/sound-effect-generator)）：页面层级、关键词、内链与**可扩展程序化落地页**。与 **Soundboard / Community Sounds**（现成库）区分：**Generator = 文本/参数生成自定义短音效**；**Soundboard = 浏览与播放库内音效**。  
3. **落地执行**：Hub / 分类页的区块顺序、程序化数据字段、JSON-LD、技术清单、埋点与验收清单均在本文（**第六节、第七节、第十一节**）；**勿再维护**独立文件 `dubbingai-sfx-generator-page-build-playbook.md`。**与全站导航/Footer 的跳转关系**见 [dubbingai-internal-links.md](./dubbingai-internal-links.md)。**原 playbook → 本文对照**见 **第十一节开头**。

**生成物**在概念上属于 **sound effects**；对外勿与「音效板」产品名混用，见 **第一节、第二节**。

---

## 一、Sound effects 与 Soundboard 的区别

二者**不是对立概念**，而是 **「素材类型」** 与 **「工具/产品形态」** 的关系。

| 概念 | 英文 | 含义 |
|------|------|------|
| **音效 / 声音特效** | **Sound effects**（常缩写 **SFX**） | 单条**音频内容**：为配合画面、游戏、直播、梗文化而使用或采集的短音频（提示音、环境声、爆炸、meme 梗音、UI 声等）。在影视与游戏工业里，一般指**非对白、非配乐**、用于叙事或氛围的声音元素。 |
| **音效板** | **Soundboard** | **收纳、分类、一键播放**大量短音频的**工具或界面**（桌面/Web/App、硬件采样垫等）。用户通过按钮、热键触发播放；里面装的往往是 **sound effects**、meme 片段、短音乐等。 |

**一句话**：**Sound effects 是「有什么声音」；Soundboard 是「用什么界面/产品来快速播放这些声音」。**

**与「音乐」的边界**：Sound effects / SFX 通常强调**短、可重复触发、场景化**；长段 BGM、可循环制作物更易归入 **Music** 分类。实际以站内导航与版权说明为准。

---

## 二、在 Dubbing AI 产品中的对应关系

| 对外/站内说法 | 对应关系 |
|---------------|----------|
| **Soundboard**（功能名） | 产品核心能力之一，与 **Real-time Voice Changer** 并列；见 [dubbingai-features.md](./dubbingai-features.md) 第三节。 |
| **Community Sounds** | 音效浏览与发现入口；分类 URL 为 `/community-sounds/{category}`，见 [dubbingai-soundboard.md](./dubbingai-soundboard.md) 第一节、第八节。 |
| **Sfx**（导航分类） | 站内 **Sound effects** 取向的**内容分类**之一，路径示例：[community-sounds/sfx](https://dubbingai.io/community-sounds/sfx)。与 **Memes、Games、Music** 等并列，不是「另一个产品」，而是 **Soundboard 内容库中的一类**。 |
| **sound effects / free sound effects**（检索词） | 优先落地到 **Sfx 分类页** 及 Hub；与「meme soundboard」等词并存时，按搜索意图分配，见 [dubbingai-keywords.md](./dubbingai-keywords.md)。 |
| **Sound Effect Generator**（工具） | **AI 从文本生成**短音效，路径 [/sound-effect-generator](https://dubbingai.io/sound-effect-generator)；与「库内下载」区分；**URL、模板与长尾见本文第四节起**。 |

**文案建议**：介绍「功能」时用 **Soundboard**；介绍「某类素材」时用 **sound effects** 或站内分类名 **Sfx**；介绍「**自定义生成**」时用 **Sound Effect Generator**，避免与音效板混称。

---

## 三、SEO 与元数据提示（术语与落地）

- **sound effects**、**free sound effects**、**sfx sounds**：偏 **Transactional / 素材发现**，适合 **Sfx 分类页** Title/Description 与首段。
- **meme soundboard**、**Discord soundboard**：偏 **工具选型**，适合 **Hub `/community-sounds`**、`/soundboard` 与 Memes 等类页。
- **AI sound effect generator**、**text to sound effect**：偏 **生成工具**，适合 **`/sound-effect-generator`**（见本文第四节 URL 与第六节主站模板起）。
- 同一页面避免重复堆砌「soundboard」与「sound effects」而无定义；可用 FAQ：*What’s the difference between the soundboard and sound effects?* 指向 **第一节、第二节**。

---

## 四、Sound Effect Generator：页面层级与 URL 模式

### 目标与原则

| 目标 | 做法 |
|------|------|
| **转化** | 首屏即工具；全页单一主 CTA：**Generate**（分类页可预填该类示例 prompt）。 |
| **SEO** | Hub 占 **工具核心词**；分类页占 **{类型} + AI / sfx / generator** 长尾；每页有 **证据块**（prompt + 场景），避免薄内容。 |
| **意图分流** | 「即时生成自定义短音效」→ Generator；「梗音 / 热门采样 / 浏览库」→ Community Sounds / Soundboard（首段或对比块写清并内链）。 |

### URL 与索引

| 页面类型 | URL 模式 | 索引 | 目标关键词（主） / 备注 |
|----------|----------|------|-------------------------|
| **工具 Hub** | `/sound-effect-generator` | index, follow；canonical 自身 | AI sound effect generator, free sound effect generator, text to sound effect |
| **分类营销页** | `/sound-effect-generator/{slug}` | index, follow（达标页） | `slug` 与 **§10.1** 一致（如 `whoosh`、`ui-element`、`horror`） |
| **未达标草稿** | 同上 | **noindex** 直至 ≥300 词 + 证据块齐 | 或暂不发布 |
| **冲突备选路径** | `/sound-effects/{slug}` | **301** → 规范 URL，或 canonical 指向 `/sound-effect-generator/{slug}` | 只保留一套规范 |

**面包屑（分类页）**：`Home` → `Sound Effect Generator` → `{Category}`。

**说明**：

- 当前站点 **单页工具** 即主承载；SEO 以 **强化主 URL** 为 P0。
- **阶段 B** 与 [ElevenLabs Sound Effects](https://elevenlabs.io/sound-effects) 同类：**按音效类型（Air、Horror、UI…）建分类落地页**，路径中的 `{category}` = **§10.1 建议 slug**（如 `air`、`ui-element`），非「YouTube / podcast」等平台向路径。
- 分类页仅在 **每页 ≥300 词、独立示例 prompt、FAQ、与相邻分类互链** 时批量上线，避免 thin content；否则先在主站用 H2 覆盖。

---

## 五、已上线页面内容分析

基于 [Sound Effect Generator](https://dubbingai.io/sound-effect-generator) 当前结构（标题、功能区块、FAQ）。

| 模块 | 现状 | SEO 评估 |
|------|------|----------|
| **H1** | Free Sound Effect Generator | 含核心词；可测「AI」「online」变体 Title 做 CTR |
| **功能** | 英文描述 → 生成；Duration 1–10s；Step 1–20；每日免费 3 次；WAV 下载 | 首段应写清 **限制与价值**（便于 FAQ、结构化数据） |
| **How-to** | 3 步：描述 → 参数 → Generate | 适合 HowTo schema；与竞品对比「无需 DAW」 |
| **FAQ** | 字数上限、免费、格式、每日次数等 | 可扩：版权/商用提示、与 Soundboard 区别、英文 prompt 原因 |
| **内链** | Useful Tools、Footer | 需指向 **Community Sounds / Sfx**、**Soundboard**、**下载 App** |

**内容缺口**：首屏未强区分 **「AI 生成音效」** vs **「10 万+ 现成音效库」**；建议在 Intro 增加一句并链到 `/community-sounds/sfx` 与 `/soundboard`。

---

## 六、主站 SEO 内容模板（/sound-effect-generator）完整结构

自上而下**固定顺序**（工具可插在 Hero 下或 Hero 内嵌；以下以「工具在上」为例）。**字数**：Intro + Feature + How-to + Use cases + 对比 + FAQ 合计建议 **≥400 词**（英文），便于与摘要竞争。

| # | 区块 | 目的（Landing 五步） | 内容要点 | Schema / 备注 |
|---|------|----------------------|----------|----------------|
| 1 | **Nav / 轻量顶栏** | — | 保留品牌回首页；工具页可减少全站导航干扰，Footer 补全站入口。 | — |
| 2 | **Hero：H1 + 副标题 + 工具** | Stop + 意图 | H1 含 *AI / free / sound effect / generator*；副标题一句 *text-to-sfx*；下方即生成器组件。 | — |
| 3 | **信任条（可选）** | Earn trust | 安全处理、不存储、WAV、每日免费次数（与产品一致）。 | — |
| 4 | **Intro 段（短）** | Explain | 2～4 句：谁适合用；**一句区分**「AI 生成」vs「10 万+ 现成库」+ 链 `/community-sounds/sfx`、`/soundboard`。 | — |
| 5 | **Feature bullets** | Explain | 在线、无需 DAW、时长/步进、导出格式、额度透明。 | — |
| 6 | **How to use（3 步）** | Explain | 描述 → 参数 → Generate；配 **2～3 个示例 prompt**（thunder / laser / UI beep）。 | HowTo |
| 7 | **Use cases（H2）** | Explain | YouTube / 短视频 / 游戏 / 直播等（与关键词文档一致，不堆砌）。 | — |
| 8 | **对比块** | Remove doubt | 两列：**要自定义生成** → 本页；**要梗音热门采样** → Community Sounds。 | 内链 |
| 9 | **按类型浏览（P1 后）** | 内链 + 发现 | 网格链向 `/sound-effect-generator/{slug}`（首批 8 类可先行）。 | — |
| 10 | **FAQ** | Remove doubt | 字数限制、免费、格式、次数、英文 prompt 原因、商用（法务审）、与 Soundboard 区别。 | FAQPage |
| 11 | **CTA 条** | Make the ask | Download App、Browse Community Sounds；主按钮仍引导回生成或注册。 | — |
| 12 | **Footer** | — | Useful Tools 与全站一致；链 **Voice Changer**、**Blog**。 | — |

**技术/信任**：页面已提处理安全、不存储；可在 FAQ 复述以满足 YMYL 类工具信任。

---

## 七、内链规划

**Sound Effect Generator 与全站（Hub、Footer、Community Sounds、Voice Changer）的跳转树与矩阵**已集中至 **[dubbingai-internal-links.md](./dubbingai-internal-links.md) 第六节**。

**本文档独有**：程序化分类 slug 与 **Sfx / meme 库**不重复造 URL——场景互链规则仍见 **[dubbingai-soundboard.md](./dubbingai-soundboard.md)**「Sound Effect Generator 与本文档的分工」；Community Sounds 分类数据见 soundboard **§8.0**。

---

## 八、关键词映射

| 类型 | 关键词 | 目标页 |
|------|--------|--------|
| **品牌+工具** | Dubbing AI sound effect generator | /sound-effect-generator |
| **核心** | AI sound effect generator, free sound effect generator online | /sound-effect-generator |
| **意图** | text to sound effect, AI sfx generator, generate sound effects from text | /sound-effect-generator |
| **分类意图** | air sound effects, horror sfx AI, UI sound effect generator | **`/sound-effect-generator/{category}`**（阶段 B，slug 见 §10.1） |
| **平台/场景（辅）** | for YouTube、for streaming | 主站 H2、**Blog**；不与「Air/Horror…」分类页抢同一 Title |
| **库 vs 生成** | free sound effects download | /community-sounds、/community-sounds/sfx（勿与生成器抢同一 Title） |

---

## 九、长尾关键词扩展

> 优先 KD 适中、与产品能力一致；**英文 prompt** 若在长期保留，须在文案中说明，避免「多语言生成」类词误导。

### 9.1 核心商业/工具词

| 关键词 | 搜索意图 | 备注 |
|--------|----------|------|
| AI sound effect generator | Commercial / Transactional | 主词 |
| free sound effect generator | Transactional | 与「免费额度」文案一致 |
| online sound effect generator no download | Transactional | 匹配 Web 工具 |
| text to sound effect AI | Informational / Commercial | 与功能强相关 |
| AI sfx generator | Commercial | 缩写 sfx 与 [Sfx 分类页](https://dubbingai.io/community-sounds/sfx) 互链 |

### 9.2 分类长尾（阶段 B 主战场）与场景辅词

| 关键词簇 | 落地建议 |
|----------|----------|
| **类型词 + AI / generator**（与 §10.1 一致） | **`/sound-effect-generator/{slug}`**：如 *whoosh sound effect AI*、*horror sfx generator*、*air ambience sound effect* |
| **game / cartoon / sci-fi** 等 | 对应 slug 分类页 `game`、`cartoon`、`sci-fi`；并链 `/community-sounds/games`（库意图） |
| YouTube / podcast / streaming（平台向） | 主站 H2 或 Blog；**不单独做** `/youtube` 子路径，避免与 ElevenLabs 式 **类型分类** 重复 |
| TikTok、Shorts | 与 `/community-sounds/tiktok` 区分生成 vs 采样；长尾以 Blog 或主站段落承接 |

### 9.3 修饰词（Intent modifiers）

| 修饰 | 示例 |
|------|------|
| **free** | free AI sound effects generator |
| **best** | best free sound effect generator（需可验证主张） |
| **how to** | how to make sound effects with AI → 指向本工具 + 教程 |

---

## 十、竞品与差异化（工具向）

| 类型 | 说明 | Dubbing AI 可强调 |
|------|------|-------------------|
| **通用 AI 音频** | MusicLM、AudioCraft 等偏音乐/长音频 | **短音效**、**秒级参数**、与 **Dubbing 生态**（变声 + 音效库 + 生成）一体 |
| **SFX 素材站** | 免版税库、一次性下载 | **即时生成**；库内 **Community Sounds** 覆盖热门梗 |
| **游戏中间件** | Wwise 等 | 非同一用户；本工具面向 **创作者轻量需求** |

*详细竞品矩阵仍以 [dubbingai-competitors.md](./dubbingai-competitors.md) 主竞品为准；本节仅服务 **工具落地页** 叙事。*

### 10.1 优秀竞品对标：ElevenLabs SFX 营销分类（全量）

[ElevenLabs Sound Effects](https://elevenlabs.io/sound-effects) 在「**Trending and popular sound effect categories**」下列出高密度 **营销/检索向** 分类，覆盖影视、游戏、UI、环境声等意图；以下为 **全量收录**（与竞品英文命名一致），供 Dubbing AI **阶段 B 分类落地页**（`/sound-effect-generator/{slug}`）、Prompt 示例库、Blog 与筛选文案使用。  
**说明**：分类名来自竞品公开页；**建议 slug** 为站内 kebab-case **与阶段 B URL 段一致**；**示例关键词** 为常见英文长尾方向（实际上线需用工具验量）。**与 Community Sounds**：本表 slug 仅用于 **生成器** `/sound-effect-generator/{slug}`；站内 **Community Sounds** 分类 segment 为另一套（如 Funny 类为 **`funnist`**），见 [dubbingai-site-structure.md](./dubbingai-site-structure.md) 第四节。

| # | 分类（与 ElevenLabs 一致） | 建议 slug | 示例关键词 / 内容角度 |
|---|---------------------------|-----------|------------------------|
| 1 | Air | `air` | air sound effects, wind ambience |
| 2 | Aircraft | `aircraft` | aircraft sound effects, plane flyby |
| 3 | Alarm | `alarm` | alarm sound effect, siren sfx |
| 4 | Ambience | `ambience` | ambient sound effects, room tone |
| 5 | Animal | `animal` | animal sound effects, creature sfx |
| 6 | Bell | `bell` | bell sound effect, church bell |
| 7 | Boat | `boat` | boat sound effects, ship horn |
| 8 | Booms | `booms` | cinematic boom, explosion impact |
| 9 | Bullet | `bullet` | bullet sound effects, gun ricochet |
| 10 | Cartoon | `cartoon` | cartoon sound effects, boing slapstick |
| 11 | Communication | `communication` | radio static, walkie talkie |
| 12 | Creature | `creature` | monster growl, alien creature |
| 13 | Crowd | `crowd` | crowd ambience, stadium cheer |
| 14 | Cymbals | `cymbals` | cymbal crash, percussion hit |
| 15 | Devices | `devices` | electronic device beeps |
| 16 | Door | `door` | door creak, knock open close |
| 17 | Electricity | `electricity` | electric zap, tesla arc |
| 18 | Environment | `environment` | environmental soundscape |
| 19 | Fire | `fire` | fire crackling, flame whoosh |
| 20 | Foley | `foley` | foley footsteps, cloth rustle |
| 21 | Food & Drink | `food-drink` | eating drinking foley |
| 22 | Footstep | `footstep` | footsteps sfx, walking on gravel |
| 23 | Funny | `funny` | funny sound effects, comedic |
| 24 | Game | `game` | game sound effects, 8-bit retro |
| 25 | Gore | `gore` | gore horror sfx（合规与年龄提示） |
| 26 | Horror | `horror` | horror sound effects, scary ambience |
| 27 | Human | `human` | human voice grunt, breath |
| 28 | Ice | `ice` | ice crack, freeze crunch |
| 29 | Laser | `laser` | laser blast, sci-fi pew |
| 30 | Leather | `leather` | leather creak, jacket movement |
| 31 | Machinery | `machinery` | machinery industrial loop |
| 32 | Magic | `magic` | magic spell, sparkle |
| 33 | Mechanical Object | `mechanical-object` | gears, mechanical click |
| 34 | Misc | `misc` | miscellaneous sfx |
| 35 | Motor | `motor` | motor engine loop |
| 36 | Object | `object` | object drop, impact |
| 37 | Office | `office` | office ambience, keyboard |
| 38 | Percussion | `percussion` | percussion hits, drums |
| 39 | Robot | `robot` | robot beep, servo |
| 40 | Rope | `rope` | rope tension, creak |
| 41 | Sci-fi | `sci-fi` | sci-fi sound effects, spaceship |
| 42 | Sport | `sport` | sport stadium, ball whistle |
| 43 | Transport | `transport` | transport vehicle pass-by |
| 44 | UI element | `ui-element` | UI click, notification beep |
| 45 | Vegetation | `vegetation` | leaves rustle, grass |
| 46 | Vehicle | `vehicle` | car pass-by, skidding |
| 47 | Voice | `voice` | voice clip, shout（与 Voice Changer 区分：此处偏 SFX） |
| 48 | Water | `water` | water splash, underwater |
| 49 | Weapon | `weapon` | weapon reload, sword swing |
| 50 | Weather | `weather` | thunder rain windstorm |
| 51 | Whistle | `whistle` | whistle blow, referee |
| 52 | Whoosh | `whoosh` | whoosh transition, sfx sweep |

**落地优先级建议**：**Whoosh、UI element、Ambience、Horror、Sci-fi、Game、Footstep、Weather** 等检索面大、与创作者场景强相关，优先做 **示例 Prompt + 短教程**；**Gore** 等敏感类需合规审核与年龄提示。

**与 Dubbing AI 差异化**（相对 ElevenLabs）：ElevenLabs 强调 **四条采样、Explore、商业授权分层**；Dubbing AI 可强调 **与 Voice Changer + Community Sounds 同一套账号/生态**、**WAV 导出**、**每日免费额度**（以官网为准），并在同类分类页上对比 **「生成 → 放进 Soundboard 热键」** 工作流。

---

## 十一、程序化扩展（分阶段）

**索引**：执行顺序 **§11.0**；Hub 强化 **§11.1**；分类页策略与区块 **§11.2**；UGC/教程 **§11.3**；模板与数据字段 **§11.4**；文案公式、JSON-LD、技术、埋点、验收 **§11.5–§11.9**。

**原 `dubbingai-sfx-generator-page-build-playbook.md` 并入位置（单一信源）**：

| 原 playbook 内容 | 本文位置 |
|------------------|----------|
| 目标与原则、URL、索引、面包屑 | **第四节**（目标与原则、URL 与索引） |
| Hub 自上而下 12 步完整结构 | **第六节** |
| 内链树 + 矩阵 | **第七节**；全站扩展见 [dubbingai-internal-links.md](./dubbingai-internal-links.md) |
| P0/P1 批次、分类 9 区块、数据字段、文案、JSON-LD、技术、埋点、验收 | **第十一节** §11.0–§11.9 |

### 11.0 执行阶段划分（P0 / P1 / P1+ / P2）

| 阶段 | 内容 | 产出 |
|------|------|------|
| **P0** | Hub 按 **第六节**整页落地 + 技术 SEO + 内链 | 一条可转化、可收录的主 URL |
| **P1** | 分类页模板 + 数据表；**优先批次** slug 上线（见下表） | 8～12 个高价值分类页先索引 |
| **P1+** | 其余 **§10.1** 共 52 类滚动发布 | 监控收录与质量，避免单日暴增 |
| **P2** | Blog / 教程、Prompt 库、与 Soundboard 联动专题 | 支撑长尾与内链，非替代 B 类页 |

**P1 优先批次（建议）**：与 **§10.1 落地优先级** 对齐，**第一批**：`whoosh`, `ui-element`, `ambience`, `horror`, `sci-fi`, `game`, `footstep`, `weather`。**第二批**示例：`air`, `laser`, `magic`, `cartoon`, `door`, `fire`, `water`, `vehicle`… 直至覆盖 52 类。

### 11.1 阶段 A（P0）：单页做强

- Title/Description/H1 覆盖 **AI + sound effect + generator + free/online**。
- 结构化数据：FAQPage、SoftwareApplication 或 WebApplication（按实现）；细则见 **§11.6**。
- 内链：**Sfx**、**Soundboard**、**下载**。

### 11.2 阶段 B（P1）：类型分类页（对齐 ElevenLabs）

**策略**：与 ElevenLabs 一致，按 **音效类型** 做程序化分类页，而非按「YouTube / podcast」等平台。完整 **slug 列表** 即 **第十节 §10.1** 表（Air、Aircraft、…、Whoosh 共 52 类）。

**URL 规范**：`/sound-effect-generator/{category}`，其中 `{category}` = §10.1 **建议 slug** 列（如 `air`、`food-drink`、`ui-element`）。与主站 `/sound-effect-generator` 的互链、面包屑、canonical 需统一。

**条件**（避免 thin content）：每分类页 ≥300 词；含 **该类典型 prompt 2–4 条**、**生成结果/场景说明**、**FAQ 1–3**（可与主站 FAQ 去重）；**横向** 链向 3–4 个相关 slug（如 `weather` ↔ `thunder` ↔ `rain` 类意图）；**纵向** 链主站、Sfx、Soundboard。

**分批上线**：优先 **§10.1 落地优先级** 已列类型（Whoosh、UI element、Ambience、Horror、Sci-fi、Game、Footstep、Weather 等）；其余按检索与制作资源滚动发布。

**与 Community Sounds**：若用户意图是「下采样 / 梗音」，优先 **库**；分类页首段用一句说明「自定义生成 vs 现成库」并链 `/community-sounds/sfx`。

**与 Hub 共用同一套生成器组件**；差异在 **元数据、H1、预填 prompt、证据块、FAQ、内链**。分类页自上而下建议顺序：

| # | 区块 | 内容 |
|---|------|------|
| 1 | **面包屑** | Home → Sound Effect Generator → {Category} |
| 2 | **H1** | 公式：`**{Category}** Sound Effects — Free AI Generator`（或验词后微调） |
| 3 | **工具区** | 默认预填 **第一条 `prompt_examples`**；用户可改。 |
| 4 | **Intro 段（80～120 词）** | 该类检索意图 + 一句 **库 vs 生成** + 链 Sfx。 |
| 5 | **Evidence block（核心）** | **2～4 条英文 prompt**（列表或卡片）；**1 段场景**（谁在什么项目里用）；可选 **参数建议**（时长/步进）。 |
| 6 | **Decision 短块** | 何时用生成；何时去 **Community Sounds** 找现成采样。 |
| 7 | **相关类型（横向）** | 3～4 个 `related_slugs` 卡片。 |
| 8 | **FAQ（1～3）** | 仅本类；与 Hub FAQ **去重**。 |
| 9 | **次 CTA** | Browse `/community-sounds/sfx`、Download、回 Hub。 |

**合格线**：正文 **≥300 词**，且 Evidence 为**人工写过**的叙述，非仅替换 `{category}` 的模板句。

---

### 11.3 阶段 C（P2）：UGC、Explore 与深度内容

- **阶段 B 已覆盖类型页**；本节侧重 **补充层**：用户上传/精选进 Explore（若产品具备）、**API 文档**、**长教程**（工作流：分类页 → 生成 → 导入 Soundboard）。
- **Prompt 示例库**（可索引标签页）：与 **§10.1 slug** 共用同一套分类，内容以 **UGC + 编辑精选** 避免与 B 重复；可做 `/sound-effects/playground/{id}` 类仅当有唯一内容。
- **与 Voice Changer / Soundboard 联合**：「先生成音效 → 再绑定热键」专题或 Blog。

### 11.4 长尾分类营销页：Landing Page × Programmatic SEO 合并模板（Skills 对齐）

**文档现状**：第九节长尾、第十节 §10.1 的 **slug 与示例关键词**、第十一节 §11.2 的上线条件已覆盖「**有什么分类、落什么 URL**」。本节补齐 **「每一类长尾页长什么样」**——把 **programmatic-seo** 的「模板 + 数据 + 证据块」、**landing-page** 的「单目标转化五步法」、**template-page** 的「聚合 Hub / 详情页分工」压成**一张可执行的区块表**，并给出 **每页数据字段**，便于建站/ CMS 或批量生成。

#### 页面类型分工（template-page）

| 类型 | URL | 角色 | 主 CTA |
|------|-----|------|--------|
| **聚合 Hub + 工具** | `/sound-effect-generator` | 全站生成器入口；可带「按类型浏览」链接到分类 | **Generate**（首屏工具） |
| **程序化详情（分类营销页）** | `/sound-effect-generator/{slug}` | 每个 **§10.1 slug** 一条；针对「{类型} + AI / generator / sfx」长尾 | **Generate**（与该类预设 prompt 联动）+ 次要：**Browse Community Sounds** |

分类页不是纯 SEO 文：仍以 **工具可用** 为第一屏，文案与 FAQ 承担 **Remove doubt** + **意图对齐**（landing-page）。

#### pSEO 五段 × Landing 五步（合并映射）

| pSEO 区块（programmatic-seo） | Landing 作用（landing-page） | 分类页 `{slug}` 填什么（Dubbing） |
|-------------------------------|------------------------------|-----------------------------------|
| **Intro**（H1 + 首段） | **Stop the scroll** + 意图匹配 | 「{Category} sound effects — AI generator」类标题；首段 1 句价值 + 1 句与 **库** 区分（链 Sfx） |
| **Evidence block** | **Explain value** + 差异化 | **每页唯一**：2–4 条 **英文示例 prompt**、1 段 **场景**（游戏/短视频/UI）；可附 **时长/步进** 建议；避免仅换 `{category}` 名的空壳 |
| **Decision**（短） | **Earn trust** / 下一步 | 「何时用生成 vs 何时去 Community Sounds」；可选 **与 ElevenLabs 同类**一句对比（生态/额度/WAV，以官网为准） |
| **FAQ** | **Remove doubt** | 1–3 条**仅本类**问题（版权、语言、是否适合直播等去重主站） |
| **CTA** | **Make the ask** | 单一主 CTA：**Generate**；次 CTA：Download App、Browse Sfx |

**字数**：与 §11.2 一致，正文 **≥300 词**（含 Evidence 叙述）；**证据块**占主要篇幅，避免 boilerplate 套模板。

#### 程序化「数据层」字段（每行 = 一个 category / 一页）

供表格或 CMS 导入，与 **§10.1** 表合并使用：

| 字段 | 说明 |
|------|------|
| `slug` | 与 URL 段一致，见 §10.1 |
| `category_label` | 展示用名（与 ElevenLabs 一致） |
| `primary_keyword` | 主目标长尾词（验量后锁定） |
| `h1` / `title` | 含品类 + generator / AI，避免与 Hub 抢同一主词 |
| `meta_description` | 含品类 + 免费/在线 + CTA 语 |
| `intro_paragraph` | 唯一首段（非仅替换变量） |
| `prompt_examples` | 2–4 条，字符串数组 |
| `use_case_paragraph` | 该类典型使用场景 |
| `related_slugs` | 3–4 个横向内链 slug |
| `faq_items` | 1–3 条 JSON；与主站 FAQ 去重 |
| `schema_notes` | FAQPage + WebApplication；可与主站共用同一 `SoftwareApplication` 定义 |
| `default_prompt_index` | 可选；默认 `0`，指定默认预填的 `prompt_examples` 下标 |
| `sensitive_flag` | 可选；如 Gore：**合规与年龄门** |

**生成方式**：表格维护 → 静态生成（SSG）或 CMS 动态页；**禁止**仅 CSV 换词无编辑审阅。

#### 风险与节奏（programmatic-seo）

- **批量同时上线**易触发质量信号：按 **§10.1 落地优先级** 分批；**sitemap** 分段提交；监控 **收录与跳出**。  
- **低价值页**可 `noindex` 或暂不生成；**仅标题+一段换词**的页不发布。  
- 与 [Google 垃圾内容政策](https://developers.google.com/search/docs/essentials/spam-policies?hl=zh-cn) 对齐：**滥用规模化内容** = 以操纵排名为主、对用户无帮助；本方案以 **证据块（prompt + 场景）** 为 **信息增量**（见仓库根 `内容-信息增量-笔记.md`）。

### 11.5 文案公式（Title / Meta / H1，可直接套变量）

- **Hub Title**：`Free AI Sound Effect Generator | Text to SFX Online | Dubbing AI`（≤60 字符优先，可测 CTR）。  
- **Hub Description**：含 *AI, sound effects, text, online, free, WAV* + 一句库互补。  
- **分类 Title**：`{Category} Sound Effects AI Generator (Free Online) | Dubbing AI`  
- **分类 Description**：`Create {category} SFX from text. Free online AI sound effect generator. WAV export. Also browse Community Sounds for ready-made clips.`  
- **H1 Hub**：`Free Sound Effect Generator` 或含 **AI**。  
- **H1 分类**：`{Category} Sound Effects — AI Generator`。

### 11.6 结构化数据（JSON-LD 清单）

| 页面 | 建议 |
|------|------|
| **Hub** | `WebApplication` 或 `SoftwareApplication`（name、url、offers 若有）、`FAQPage`、`HowTo`（对应三步） |
| **分类页** | `FAQPage`（仅当页 FAQ）、`WebApplication`（与 Hub 同一应用 `@id` 可复用）；**勿**重复堆砌多个 Product |

由开发按 [Google 结构化数据常规指南](https://developers.google.com/search/docs/appearance/structured-data) 实现；上线前用富媒体测试工具校验。

### 11.7 技术清单

| 项 | 要求 |
|----|------|
| **Canonical** | 自引用；参数 URL 规范化。 |
| **Index** | Hub + 已达标分类 index；未达标 noindex。 |
| **Sitemap** | `sitemap-sfx-generator.xml` 分段；新 URL 分批提交。 |
| **性能** | LCP：首屏工具可交互；图片 WebP；CLS 稳定。 |
| **移动端** | CTA、生成区拇指区；无横向滚动。 |

### 11.8 分析埋点（建议事件名）

| 事件 | 说明 |
|------|------|
| `sfx_generate_click` | 点击 Generate |
| `sfx_download` | 导出 WAV |
| `sfx_category_prompt_apply` | 分类页使用预填 prompt |
| `sfx_nav_to_library` | 点击 Community Sounds / Sfx |

### 11.9 上线与验收清单

#### Hub（P0）

- [ ] Title/Description/H1 含核心词且不重复堆砌  
- [ ] Intro 区分生成 vs 库 + 内链  
- [ ] How-to + 示例 prompt + FAQ  
- [ ] 内链：Sfx、Soundboard、下载、Voice Changer  
- [ ] JSON-LD：FAQ + HowTo + WebApplication  
- [ ] 移动端与 CWV 达标  

#### 分类页（每 slug）

- [ ] ≥300 词 + 2～4 prompt + 场景段  
- [ ] 唯一 Title/Description；canonical 正确  
- [ ] 横向 + 纵向内链  
- [ ] 与 Hub FAQ 去重  
- [ ] 敏感类（Gore 等）合规与提示  

#### 程序化风控

- [ ] 分批发布，避免单日大量相似 URL  
- [ ] 无「仅换城市名式」换词；每页有信息增量  
- [ ] 定期抽查排名与收录，低质页 noindex 或加强内容  

---

## 十二、与相关产品文档

| 文档 | 关系 |
|------|------|
| **本文档** | **第一～三节**：术语与 SEO；**第四节～第七节**：URL、主站区块、内链摘要（全站见 internal-links）；**第八～十节**：关键词与竞品；**第十一节**：程序化阶段、分类模板、数据字段、文案公式、技术、埋点、验收 |
| [dubbingai-internal-links.md](./dubbingai-internal-links.md) | 全站内链、导航、Footer、聚合页 |
| [dubbingai-site-structure.md](./dubbingai-site-structure.md) | 线上网站结构、Footer、URL |
| [dubbingai-soundboard.md](./dubbingai-soundboard.md) | 现成库与分类 URL；与 Generator 分工 |
| [dubbingai-keywords.md](./dubbingai-keywords.md) | 全站关键词与落地页映射 |

---

## 十三、文档导航

| 文档 | 用途 |
|------|------|
| [dubbingai.md](./dubbingai.md) | 主文档 |
| [dubbingai-features.md](./dubbingai-features.md) | 功能与工具线 |
| [dubbingai-soundboard.md](./dubbingai-soundboard.md) | Soundboard 程序化 |
| [dubbingai-sound-effect-generator.md](./dubbingai-sound-effect-generator.md) | 本文档：音效术语 + Generator 程序化 + Hub/分类落地与验收 |
| [dubbingai-internal-links.md](./dubbingai-internal-links.md) | 全站内链与跳转 |
| [dubbingai-keywords.md](./dubbingai-keywords.md) | 关键词映射 |

### 文档修订

| 日期 | 说明 |
|------|------|
| 2026-04-06 | 独立 playbook：Hub + 分类页完整构建方案 |
| 2026-04-07 | 原 `dubbingai-sfx-generator-page-build-playbook.md` 全文并入本文（**第四节** 目标与 URL、**第六节** Hub 区块、**第七节** 内链矩阵、**第十一节** §11.0–§11.9）；该独立文件已删除，勿再恢复双份维护。与 Soundboard 互链见 [dubbingai-soundboard.md](./dubbingai-soundboard.md)「Sound Effect Generator 与本文档的分工」 |
| 2026-04-07 | 第七节内链树迁入 [dubbingai-internal-links.md](./dubbingai-internal-links.md) 第六节；本文保留分工与 slug 边界 |

*本方案与仓库根目录 [内容-信息增量-笔记.md](../../内容-信息增量-笔记.md) 中的「证据块 / 避免规模化低质内容」原则一致。*
