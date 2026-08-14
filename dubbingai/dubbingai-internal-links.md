# Dubbing AI 站内链接与跳转（全站）

> **站点**：[dubbingai.io](https://dubbingai.io/)  
> **关联**：[dubbingai.md](./dubbingai.md) | [dubbingai-site-structure.md](./dubbingai-site-structure.md) | [dubbingai-features.md](./dubbingai-features.md) | [dubbingai-keywords.md](./dubbingai-keywords.md) | [dubbingai-voice-changer.md](./dubbingai-voice-changer.md) | [dubbingai-soundboard.md](./dubbingai-soundboard.md) | [dubbingai-sound-effect-generator.md](./dubbingai-sound-effect-generator.md)  
> **Skills 对齐**：**internal-links**（站内链接、锚文本、Hub-spoke、孤立页）、**website-structure**（层级与聚合页）、**sitemap**（URL 发现与子图分工，**以 [site-structure §〇.2–§7.6](./dubbingai-site-structure.md) 为准**）；面包屑细节见 **breadcrumb** skill。

**用途**：统一描述 **网站页面之间的互相跳转与链接**——含**正文**、**顶栏/导航**、**聚合/Hub**、**Footer**、**Useful Tools**、**面包屑**及**程序化页**的纵向/横向互链。**线上 URL 与 Footer 矩阵**以 [dubbingai-site-structure.md](./dubbingai-site-structure.md) 为准；**关键词与目标 URL 映射**以 [dubbingai-keywords.md](./dubbingai-keywords.md) 为准；本文负责 **链到哪里去、在什么场景链、如何同时满足爬虫路径与真实用户意图**。

---

## 一、框架：SEO × 用户意图 × 链接拓扑

总纲：**既要符合 SEO**（可发现、权重传递、锚文本与目标页主题一致），**又要符合用户跳转逻辑**（先完成当前任务，再给出自然「下一步」）。链接落在两类载体上——**固定跳转区块** 与 **上下文内链**；关系上分 **纵向（详情↔聚合）** 与 **横向（同类页）**，需组合使用。

### 1.1 双重目标（搜索引擎 + 用户）

| 维度 | 目标 | 落地要求 |
|------|------|----------|
| **SEO** | 控制孤立页、向商业/工具页传递权重、锚文本与落地页一致 | 重要 URL 至少有 **导航 / Hub / Footer** 之一 + **正文或固定相关组件** 之一；与 [dubbingai-keywords.md](./dubbingai-keywords.md) 主映射一致 |
| **用户** | 当前页完成任务；若需要「上一级 / 换一个相近的 / 互补工具」，**一步**可达期望 | **主 CTA**（如下载、生成）不被次要链接淹没；互补路径放在 Intro、对比块、文末相关推荐 |

### 1.2 固定跳转区块 vs 上下文内链

| 类型 | 是什么 | 用户何时用 | SEO 作用 |
|------|--------|------------|----------|
| **固定区块** | 顶栏、Hub 分类网格、Footer、Resources、Useful Tools、面包屑、「Related / 相关分类」等版式稳定区域 | 认路、换频道、从任意页回到全站工具矩阵 | 全站入口一致，降低孤儿页；锚文本可偏 **栏目名 / 品牌功能名** |
| **上下文内链** | 首段、正文、**对比表**、FAQ、教程步骤、Evidence 里「若你要…请去…」 | 读到某段才产生需求（例如「我只要现成梗音」） | **意图强相关**，利于主题聚类；锚文本用 **自然句 + 目标词变体** |

**分工**：固定区块回答 **「随时能从这跳到哪」**；上下文回答 **「读完这句最该去哪」**。避免只有 Footer 堆砌或只有正文零散链接。

### 1.3 纵向：详情页 ↔ 聚合页（Hub / Spoke）

| 方向 | 典型用户意图 | 做法 |
|------|----------------|------|
| **聚合 → 详情** | 从总览进入具体游戏、音效分类、生成器类型 | Hub 列表/网格链到 spoke；锚文本含 **品类、游戏名、slug** |
| **详情 → 聚合** | 回到总览换别的、确认在全站的位置 | 面包屑、「Browse all…」、Voice Changer 回 **All Voice Changers**；Generator 分类页回 **Sound Effect Generator Hub** |

对 **SEO**：强化层级与栏目关系；对 **用户**：始终能 **上浮一层** 再选。

### 1.4 横向：同类页 ↔ 同类页（Peer）

| 场景 | 用户意图 | 做法 |
|------|----------|------|
| **同簇内容分类** | 看了 memes 还想看 tiktok / funnist（Funny 类） | Community Sounds **3～4 个相近 segment** 互链 |
| **同游戏多角色** | Valorant 用户从 Jett 换同游戏另一角色 | `/voice-changer/…` **同游戏**互链 |
| **同工具线多类型** | whoosh 生成后想试 horror | `/sound-effect-generator/{slug}` 的 **related_slugs** 卡片 |
| **库 ↔ 生成（意图级横向）** | 要采样不要生成，或反之 | **对比块**两列 + 各列独立 URL（分工见专项文档，避免 Title 冲突） |

对 **SEO**：加强相关主题页互联；对 **用户**：**少回首页** 即可「换一个相近选项」。

### 1.5 意图—路径速查

| 用户心里的一句话 | 优先：固定区块 | 次要：上下文放哪 |
|------------------|----------------|-------------------|
| 「下载安装」 | 顶栏 Download、Footer | — |
| 「逛音效库」 | Community Sounds、Footer | Intro 一句与 Generator 区分 |
| 「AI 做一段音效」 | Generator、Useful Tools | Intro 主任务 + 对比块链库 |
| 「变声 / 某游戏 / 某角色」 | All Voice Changers、平台入口 | 角色页正文「同游戏」横向 |
| 「和 Soundboard 啥区别」 | — | FAQ、对比块 |
| 「支持 Discord 吗」 | Supported Apps、Footer | FAQ、平台页 |

### 1.6 基础原则（internal-links skill 对齐）

| 原则 | 说明 |
|------|------|
| **深度** | 重要落地页距首页 ≤3 次点击；靠 Hub + 导航 + 固定区块 + 正文推荐共同保证。 |
| **避免孤立页** | 可索引 URL 宜同时具备 **一条全局入口**（导航/Footer/Hub）与 **一条语义入口**（正文或相关组件）。**注意**：多条产品线 Hub（如 `/community-sounds`、`/soundboard`、`/all-voice-changers`）**不在 sitemap 中**，更依赖 **Explore / Footer / 正文** 内链（见 **§十**、[site-structure §〇.3](./dubbingai-site-structure.md)）。 |
| **纵向 + 横向** | Hub↔Spoke 必备；Peer 按簇配置，避免全站只有纵向没有横向。 |
| **锚文本** | 描述目标；自然变体；忌「点击这里」与全站单一机械重复。 |
| **意图分流** | 库 vs 生成在 **固定区 + 对比块**可预期出现；正文按句意链，避免关键词映射冲突（见 [dubbingai-sound-effect-generator.md](./dubbingai-sound-effect-generator.md)、[dubbingai-soundboard.md](./dubbingai-soundboard.md)）。 |

---

## 二、全站顶层入口（首页与主导航）

**对应框架**：**§1.2 固定区块**（全站一致的「从哪都能去」）；与 **§1.3 纵向** 中「首页 → 各级 Hub」的顶层一段。

从首页 `/` 可达的核心产品路径（与 [dubbingai-features.md](./dubbingai-features.md) 产品线一致）：

```
首页 (/)
  ├── /explore                   ← Explore 营销落地（长版首页结构 + Footer 矩阵）
  ├── /download-desktop          ← 桌面客户端下载
  ├── /voice-cloning             ← Voice Cloning
  ├── /community-sounds          ← Community Sounds（音效发现 Hub）
  ├── /soundboard                ← Soundboard 产品级说明
  ├── /sound-effect-generator    ← AI 音效生成（Web 工具）
  ├── /online-voice-changer      ← 在线变声
  ├── /sdk                       ← SDK
  ├── /discord-voice-changer     ← 平台页示例（另有 /zoom-voice-changer、/vrchat-voice-changer 等）
  ├── /all-voice-changers        ← Voice Changer 列表 Hub
  ├── /supported-apps            ← 支持的应用
  ├── /questions                 ← FAQ（非 /faq）
  ├── /blog                      ← 博客/教程
  ├── /articles                  ← Articles 程序化 SEO（compare / list / use-case）
  ├── /affiliate                 ← 联盟
  ├── /llm-info                  ← LLM / 品牌说明（Footer「Hey AI…」）
  ├── /earbuds                   ← 硬件配件（Explore 内链）
  └── shop.dubbingai.io          ← Dubbing Box 硬件
```

**Sitemap 缺口提醒**：上列 `/explore`、`/download-desktop`、`/all-voice-changers`、`/community-sounds`、`/soundboard`、`/sound-effect-generator`、`/voice-cloning`、`/sdk`、`/llm-info`、`/earbuds` 及首页 **`/`** 均 **不在** 任一子 sitemap 中（2026-06-22）；内链是这些 URL 的主要发现路径。明细见 **[§十](#十sitemap-与内链配合)**、[site-structure §〇.3](./dubbingai-site-structure.md)。

**说明**：主导航与 Footer 的完整列表、外链与 **Audio Converter → `/converter`** 等路径见 **[dubbingai-site-structure.md](./dubbingai-site-structure.md)**；新页上线后应挂入 **主导航** 或 **Footer** 或 **相关工具区** 之一，避免孤儿页（见 **§1.6**、**§十**）。

---

## 三、Footer、Resources 与 Useful Tools

**对应框架**：**§1.2 固定区块**；与 **§1.5** 中「下载 / 逛库 / 工具」的兜底入口。

**Resources**（Explore / Footer）：SDK、Soundboard、Affiliate、FAQ（`/questions`）、Blog、Supported Apps、All Voice Changers 等——与 **[dubbingai-site-structure.md](./dubbingai-site-structure.md) §3.2** 一致；部分页面另含 Mobile Voice Changer、Download，以线上为准。

**Blog 双入口**：主站 **`/blog`** 与子域 **`blog.dubbingai.io`** 并存；部分工具页 Footer 的 Blog 指向子域。文案与内链优先主站路径；细节见 **site-structure §1.2、§3.4**。

**Useful Tools**（与 Explore 一致）：Online Voice Changer、Vocal Remover、Instrumental Remover、Voice Recorder、Audio Converter（**`/converter`**）、Sound Effect Generator、Utell（外链）、Voice Cloning、Monica AI Image（外链）等——**完整表**见 **site-structure §3.3**。

**法律与联系**（多见于工具页轻量 Footer）：`/privacy-policy`、`/terms-of-use`、`/refund-policy`、`/contact-us` ——见 **site-structure §一、§3.4**。

| 模块 | 内链要求 |
|------|----------|
| **Footer 全站（Explore 型）** | 各工具线互链一致：**Voice Changer**、**Blog**（多为 `/blog`）、**Community Sounds**、**Sound Effect Generator**（与 [dubbingai-sound-effect-generator.md](./dubbingai-sound-effect-generator.md) 第六节 Footer 描述对齐）。 |
| **Footer 工具页轻量** | 与全站矩阵同族区块，但 Blog 可能为子域；并含法律页链接 —— **site-structure §3.4**。 |
| **工具落地页** | 减少顶栏干扰时，仍须在 **Footer** 补全站入口（首页、下载、同类工具）。 |

---

## 四、Voice Changer：Hub 与 Spoke

**对应框架**：**§1.3 纵向**（`/all-voice-changers` ↔ 各 spoke）+ **§1.4 横向**（同游戏/同系列角色互链）。

**权威细分**（模板、关键词）：[dubbingai-voice-changer.md](./dubbingai-voice-changer.md)。

```
/all-voice-changers（Hub）
  ├── /league-of-legends-voice-changer
  ├── /voice-changer/jett
  ├── /voice-changer/one-piece/
  ├── /voice-changer/gojo
  └── … 其他游戏/角色/系列页

典型 spoke 回链：
  /voice-changer/jett        → /all-voice-changers、/valorant-voice-changer（同游戏 Hub；并存 `/voice-changer/valorant` spoke）
  /voice-changer/one-piece/  → /all-voice-changers、/discord-voice-changer
```

**原则**：Hub → 各 spoke；Spoke → Hub；**同游戏/同系列角色**横向互链。

**Sitemap**：spoke 主要在 **`voice-changer-sitemap.xml`**（389 URL）；Hub **`/all-voice-changers`** **不在** sitemap——须靠 Explore / Footer Resources 与 spoke 回链保证可发现性（**§十**）。

---

## 五、Soundboard、Community Sounds 与 Sound Gallery

**对应框架**：**§1.3 纵向**（`/community-sounds` ↔ 各分类）+ **§1.4 横向**（相近 segment 互链）；**sound-gallery** 长尾页以 **回 Hub + 同主题分类** 为主纵向。

**权威细分**（§8.0 分类表、Evidence）：[dubbingai-soundboard.md](./dubbingai-soundboard.md)。

```
/community-sounds、/soundboard（Hub）
  ├── /community-sounds/memes … /community-sounds/other  （12 类，见 soundboard §8.0）
  └── 分类页互链：相近主题 3～4 个（如 memes ↔ tiktok ↔ funnist）

/sound-gallery/{slug}（独立长尾页，若保留）
  ├── 回链 Hub：/community-sounds、/soundboard
  ├── 相关：同主题 community-sounds 分类（若存在）
  ├── /supported-apps、/questions
  └── /discord-voice-changer（若平台相关）

规划中的扩展类（尚无 /community-sounds 路径）
  └── 见 soundboard §8.3；上线后纳入与 Hub 的**同构内链**
```

**Hub / Footer**：「Community Sounds」列表 **segment** 与 [dubbingai-soundboard.md](./dubbingai-soundboard.md) **§8.0** 一致；高量类（Memes、Music）优先链向 Hub 与相近类。

**主站 vs meow 子域（内链写作须区分 URL）**：

| 入口 | URL 形态 | Sitemap |
|------|----------|---------|
| 主站导航 / Footer | `/community-sounds`、`/community-sounds/{segment}` | ❌ 不在 dubbingai.io 子 sitemap |
| meow 子域 | `https://meow.dubbingai.io/{segment}`（含 `/voices`） | ✅ `meow-sitemap.xml` |

内链文案优先写 **主站 `/community-sounds/…`**（与 Explore 一致）；跨子域跳转仅在产品明确指向 meow 时使用。详见 [site-structure §4.1–§4.2](./dubbingai-site-structure.md)。

**Sound Gallery / soundboard 长尾**：主要在 **`soundboard-sitemap.xml`**（含 `/sound-gallery/*`、`/soundGallery/*`、`*-soundboard`）；回链 Hub 时同时考虑 **`/community-sounds`** 与 **`/soundboard`**（后者亦在 sitemap 缺口表，**§十**）。

**程序化模板中的内链位**（正文模块）：Intro、How to make a Soundboard、FAQ、**Supported Apps**、Home、Voice Changer、Sound Gallery（见 soundboard 第三节模板表）。

---

## 六、Sound Effect Generator（工具 Hub 与分类页）

**对应框架**：**§1.3 纵向**（Generator Hub ↔ `/sound-effect-generator/{slug}`）+ **§1.4 横向**（`related_slugs`）、**§1.4 库↔生成**（对比块与 Sfx）；**§1.2** 中固定区「按类型浏览」网格。

**权威细分**（§10.1 slug、验收）：[dubbingai-sound-effect-generator.md](./dubbingai-sound-effect-generator.md)。

```
/sound-effect-generator（工具主站）
  ├── /community-sounds、/community-sounds/sfx   ← 「现成音效库」
  ├── /soundboard                                   ← 「音效板产品」
  ├── /download-desktop（或首页下载）
  ├── /online-voice-changer                         ← 同类 Web 工具集群
  ├── /blog
  └── Footer：与全站 Useful Tools / Footer 互链一致

/sound-effect-generator/{slug}（阶段 B · 类型分类）
  ├── 必回链主站 Hub；面包屑：Home → Sound Effect Generator → {Category}
  ├── 横向：同簇 3～4 个相关 slug（见主文档 §10.1 related_slugs）
  └── 纵向：/community-sounds/sfx、相关主题 Community Sounds（库 vs 生成分流）
```

**矩阵（每页必查）**

| 从 | 链向 |
|----|------|
| Generator Hub | `/community-sounds`、`/community-sounds/sfx`、`/soundboard`、`/download-*`、`/online-voice-changer`、首批 `/sound-effect-generator/{slug}` |
| Generator 分类页 | Hub、`/community-sounds/sfx`、相关 3～4 slug、必要时主题 Community Sounds（如 games） |
| 全站 Footer | Generator Hub 与 Voice Changer、Blog 等与全站策略一致 |

**说明**：生成器侧 **不重复** 造 meme 类 Community Sounds URL；仅在场景文案中互链（见 soundboard「分工」专节）。

**Sitemap**：Hub **`/sound-effect-generator`** 及分类 spoke **均不在** 任一子 sitemap（2026-06-22）——Footer / Useful Tools / 与 Community Sounds、Soundboard 的对比块内链 **尤其重要**（**§十**）。

---

## 七、面包屑

**对应框架**：**§1.3 纵向** 的「上浮一层」控件；与 **JSON-LD BreadcrumbList** 一致便于 SEO 与 SERP 展示。

| 页面类型 | 面包屑模式 |
|----------|------------|
| Community Sounds 分类 | `Home` → `Community Sounds` → `{Category}`（以线上实现为准） |
| Sound Effect Generator 分类 | `Home` → `Sound Effect Generator` → `{Category}` |
| Voice Changer 子页 | 通常含 `Home` → `Voice Changers` 或 `All Voice Changers` → `{Game/Series/Role}`（与 [breadcrumb](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) 结构化数据一并校验） |

---

## 八、正文与组件中的链接位（固定区块 + 上下文）

**对应框架**：**§1.2** 与 **§1.3 / §1.4** 在**单页内**的落地：同一页既要有 **版式稳定**的模块，又要有 **随阅读触发**的句子级链接。

### 8.1 页面内「固定」模块（位置可预期）

| 模块 | 纵向（↔聚合） | 横向（同类） | 用户与 SEO |
|------|----------------|--------------|------------|
| **首屏后「按类型浏览」网格**（Generator） | 链向 Hub 下各 `/sound-effect-generator/{slug}` | 同类卡片并列 | 用户：快速换类型；SEO：Hub 向 spoke 分流 |
| **Related / 相关分类**（Community Sounds） | 回链 **Community Sounds Hub**（可选） | 3～4 个相近 segment | 用户：不换频道即可换类；SEO：peer 互联 |
| **同游戏角色区**（Voice Changer） | 回 **All Voice Changers** | 同游戏多角色链接 | 用户：横向探索；SEO：系列内链接 |
| **文末 CTA 条** | 常指向下载或主工具 Hub | 次要链接 Browse 库 / Blog | 用户：转化或兜底；SEO：重要 URL 多次合理入口 |

### 8.2 上下文内链（随段落出现）

| 位置 | 典型意图 | 链什么 |
|------|----------|--------|
| **首段 Intro** | 区分「我要生成」vs「我只要库内采样」 | 各 **一句** 链到互补路径（**§1.2 上下文**） |
| **正文中间** | 提到 Discord/OBS/场景时 | **Supported Apps**、平台页、教程（自然句内锚文本） |
| **对比块** | 并排决策：库 vs 生成、自定义 vs 梗音 | 两列各 **明确 URL**（**§1.4 意图级横向**） |
| **Evidence / 列表** | 「类似音效在 Sfx / Games」 | 指向 **Community Sounds** 具体类或 **Generator** 另一类型（勿堆叠） |
| **FAQ** | 版权、商用、与 Soundboard 区别、英文 prompt | 链到 **合规页**、**Supported Apps**、分工说明 |
| **Blog** | 教程中「下一步」 | **纵向**回链对应工具 Hub；**横向**链相近教程 |

### 8.3 自检：一页是否同时具备「纵 + 横 + 固定 + 上下文」

| 检查项 | 合格 |
|--------|------|
| 纵向 | 详情页是否有 **回聚合 Hub**（面包屑或文内「Browse all」至少一种）？ |
| 横向 | 是否有 **2–4 个同类/相近**链接（peer 或 related）？ |
| 固定 | 是否有 **Footer / 相关模块 / CTA 条** 中至少一类覆盖全站入口？ |
| 上下文 | Intro 或对比块是否 **说清楚意图分流**（至少库/生成或主任务/次任务）？ |

---

## 九、锚文本与关键词映射

- **SEO**：锚文本与目标页主题一致，支撑 **§1.1**；全站映射以 [dubbingai-keywords.md](./dubbingai-keywords.md) 为准，避免同一商业关键词指向多个冲突落地页。  
- **用户**：锚文本让读者 **预判点击后看到什么**（功能名、平台名、品类名），与 **§1.5** 意图列一致；忌「点击这里」「更多」。  
- **变体**：同一目标页允许多种自然说法（**§1.6**），避免全站重复同一锚文本。

---

## 十、Sitemap 与内链配合

**权威明细**：[dubbingai-site-structure.md](./dubbingai-site-structure.md) **§〇.2–§〇.3、§7.6**（2026-06-22 爬取，去重 **1646** URL）。**勿**再引用 [_archive/dubbingai-io-sitemap-diagnosis.md](./_archive/dubbingai-io-sitemap-diagnosis.md) 中「根 sitemap 返回 HTML / robots 无 Sitemap」等 **2026-06-04 结论**——线上已变化。

### 10.1 子 sitemap 与内链分工

| 子 sitemap | URL 数 | 内链文档对应区块 | 内链侧要点 |
|------------|--------|------------------|------------|
| [`/sitemap.xml`](https://dubbingai.io/sitemap.xml) | 60 | §三 部分静态页 | 通用页 + 多语言首页；**非** index，与 `www-sitemap.xml` 重叠 |
| [`/blog-sitemap.xml`](https://dubbingai.io/blog-sitemap.xml) | 83 | §8.2 Blog | 博文互链回工具 Hub；见 [blog checklist](./blog/internal-external-links-checklist.md) |
| [`/tools-sitemap.xml`](https://dubbingai.io/tools-sitemap.xml) | 451 | §三 Useful Tools | `converter/*`、在线工具 × 语言前缀；Footer 互链 |
| [`/voice-changer-sitemap.xml`](https://dubbingai.io/voice-changer-sitemap.xml) | 389 | §四 | spoke 密集；**Hub `/all-voice-changers` 不在 sitemap**，靠 Footer Resources |
| [`/soundboard-sitemap.xml`](https://dubbingai.io/soundboard-sitemap.xml) | 187 | §五 | sound-gallery 长尾；Hub `/soundboard` **不在 sitemap** |
| [`/meow-sitemap.xml`](https://dubbingai.io/meow-sitemap.xml) | 13 | §五 meow | 子域 segment；与主站 `/community-sounds/*` URL 不同 |
| [`/articles/sitemap.xml`](https://dubbingai.io/articles/sitemap.xml) | 477 | §10.2 | compare / list / use-case；**robots 未声明**，靠站内链与 GSC 提交 |

**robots.txt**（2026-06-22）已声明 6 行 `Sitemap:`（含 `meow-sitemap.xml`）；**未声明** `articles/sitemap.xml`、`www-sitemap.xml`。

### 10.2 Articles 程序化内链

```
/articles（Hub）
  ├── /articles/catalog
  └── /articles/{lang}/{compare|list|use-case}/{slug}
        ├── 纵向：回 /articles、/articles/catalog
        ├── 横向：同 type 相近 slug；compare 页互链竞品组合
        └── 转化：链向 /download-desktop、/online-voice-changer、/voice-changer/{slug}、/community-sounds/…
```

- **与 `/blog` 分工**：Ghost 博文走 `blog-sitemap.xml`；Articles 矩阵独立，内链宜 **回产品线 Hub**（§二–§六），勿与商业关键词映射冲突（**§九**）。
- **语言**：sitemap 内 `ar/de/en/es/fr/pt`；内链锚文本与目标页语言一致。

### 10.3 内链优先补强的 URL（sitemap 缺口）

下列 Hub / 转化页 **仅依赖内链**（Explore、Footer、正文、Hub–Spoke 回链）方可被爬虫发现——抽检时 **不可** 假设 sitemap 已覆盖：

`/`、`/explore`、`/download-desktop`、`/all-voice-changers`、`/community-sounds`（及全部分类）、`/soundboard`、`/sound-effect-generator`、`/voice-cloning`、`/sdk`、`/llm-info`、`/earbuds`、`/mobile-voice-changer`。

---

## 十一、维护与抽检

| 项 | 说明 |
|----|------|
| **新页上线** | 更新第二节/第五节/第六节树状图；在 Hub、Footer、或至少一篇正文中添加入口；并对照 **§8.3** 自检。 |
| **批量程序化** | 分批上线；监控孤立页与重复导航；见 sound-effect-generator §11.9 验收。 |
| **单页质量** | 重点页抽查 **纵 + 横 + 固定 + 上下文** 是否齐备（**§8.3**）。 |
| **Sitemap 对照** | 以 [site-structure §〇.2](./dubbingai-site-structure.md) 为准；新 spoke 上线后核对是否进入对应子 sitemap；**Hub 缺口 URL** 须确认 Explore/Footer 仍有链（**§10.3**）。 |
| **死链与重复 URL** | 与 GSC、**§10.1** 子 sitemap 对照；`sound-gallery` 与 `community-sounds` 并存时注意 canonical/主入口策略（见 soundboard）；`soundGallery` / `sound-gallery` 混写时内链与 canonical 逐条对齐。 |

---

## 十二、文档导航

| 文档 | 用途 |
|------|------|
| [dubbingai.md](./dubbingai.md) | 主文档、站点概览 |
| [dubbingai-site-structure.md](./dubbingai-site-structure.md) | **线上网站结构**、Footer 矩阵、**Sitemap 清单（§〇.2）** |
| **本文档** | **全站内链**：SEO×用户意图框架（§一）、各产品线树（§二–§六）、固定+上下文（§八）、锚文本（§九）、**Sitemap 配合（§十）** |
| [dubbingai-keywords.md](./dubbingai-keywords.md) | 关键词 → 目标 URL |
| [dubbingai-features.md](./dubbingai-features.md) | 功能线与产品线 |
| [dubbingai-voice-changer.md](./dubbingai-voice-changer.md) | Voice Changer 程序化细节 |
| [dubbingai-soundboard.md](./dubbingai-soundboard.md) | Soundboard / Community Sounds 程序化细节 |
| [dubbingai-sound-effect-generator.md](./dubbingai-sound-effect-generator.md) | Generator 术语与程序化细节 |
| [blog/internal-external-links-checklist.md](./blog/internal-external-links-checklist.md) | **Blog** 专用：内链分层、博文互链矩阵、`related` 与抽检表 |

### 文档修订

| 日期 | 说明 |
|------|------|
| 2026-04-07 | 初版：集中全站内链与跳转；从 features / voice-changer / soundboard / sound-effect-generator 迁入树状与矩阵 |
| 2026-04-07 | 第二版：增补 §一 框架（双重目标、固定/上下文、纵向/横向、意图速查）；§八 拆为固定模块/上下文/自检；§二–§七 与 §一 对应说明；§九–§十 与框架对齐 |
| 2026-04-07 | 第三版：与 [dubbingai-site-structure.md](./dubbingai-site-structure.md) 对齐；§二 增补 `/explore`、`/sdk`、`/questions`；§三 与 Explore Footer 一致；Community Sounds Funny → `funnist` |
| 2026-06-22 | 对照 sitemap + Explore 内链爬取：新增 **§十 Sitemap 与内链配合**；§1.6 / §二 / §四–§六 标注 sitemap 缺口；§五 区分主站 Community Sounds 与 meow 子域；§十一 更新 sitemap 抽检说明；Valorant 同游戏 Hub 优先 `/valorant-voice-changer` |
