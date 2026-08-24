
# VOMO — YouTube 分类全景与转录落地页机遇

> 遵循 [客户文档规范](../../demo/client-template.md)
> 关联：[主文档](../vomo.md) | [features](../vomo-features.md) | [use-cases](../vomo-use-cases.md) | [keywords](../vomo-keywords.md) | [growth-strategy](../vomo-growth-strategy.md) | [site-structure](../vomo-site-structure.md) | [page-playbook](./page-playbook.md) | [podcast transcription/](../podcast%20transcription/podcast-platforms.md)

---

## 1. 执行摘要（BLUF）

YouTube 是全球最大的口语内容库，也是 VOMO 已验证的 P0 交易入口。枢纽 [`/tools/youtube-transcript`](https://vomo.ai/tools/youtube-transcript) 承接 `YouTube transcript generator`（行业公开数据约 **823K**/月 head 词量级，2026 初），再按 **Category / Topic / Sport / Format** 四轴拆子页。

**核心判断（产品端 first-party + 人工阅读，2026-08）：** 用户不是单纯要「YouTube 文字稿」，而是把 **平均约 48 分钟** 的长视频变成可学习、可执行、可复用的知识。重复导入信号包括：AI/Claude/Agent 工作流、Python/SQL 完整课、TED/Crash Course/BibleProject、健康/补剂访谈、交易/宏观、新闻冲突、商业/个人品牌课，以及 *Top 5 YouTube AI Summary Tools* 类竞品评测视频。

**文档职责：** 本页是 YouTube 转录簇的**分类权威清单**——四轴全量表、轴间边界、线上库存、SEO 主词、排产优先级。页面模具见 [page-playbook.md](./page-playbook.md)。

**规模：** 规划 **1 枢纽 + 43 子页**（Category 18 + Topic 16 + Sport 4 + Format 5）。**已上线 17 子页**（2026-08-23）。Topic 从原 11 扩至 **16**（新增 `ai`、`programming`、`software`、`finance`、`psychology`），**不改**已上线页的 slug 与轴标签。

---

## 2. 分类体系：四轴 + 任务层

### 2.1 四轴各回答什么问题

| 轴 | 问的问题 | 页上写什么 | 页上禁止写什么 |
|----|----------|------------|----------------|
| **Category** | 这是**哪种 YouTube 片子**？（听感/结构） | 讲座结构、步骤口播、抢话、现场噪音、vlog 无脚本 | Python、Claude、黄金、补剂、经文等领域专名 |
| **Topic** | 这片子在**讲哪门知识**？ | 领域术语、数字、命令、框架、经文 | 再写「课很长 / 要倒带 / 两人抢话」（归 Category） |
| **Sport** | 哪项**运动**的发布会/评论？ | 球员/队名/联赛专名 | 通用体育评论（归 Category `sports`） |
| **Format** | **片长/形态**是否改变 workflow？ | TED 18 分钟、Shorts 60 秒、直播回放数小时 | 领域知识（归 Topic） |

**验收：** Category hero 换成另一 Category 名必须失效；Topic hero 换成另一 Topic 名必须失效。

### 2.2 任务层（Task）— 不写进 URL，决定 hero 与 4 条卖点

| Task | 用户在干什么 | 优先卖点 | 典型轴 |
|------|--------------|----------|--------|
| **Learn** | 上课、复习、记术语 | 章节、长课一次转完、可搜索 | Education、Science、Programming |
| **Execute** | 跟做、抄命令、按步骤 | 步骤清单、命令可复制 | How-To、Software、AI |
| **Decide** | 看专家观点、选型、判断 | 摘要、数字准确、Ask AI | Finance、AI、Health |
| **Quote** | 引原话、写稿、监测 | 说话人、时间戳 | Interview、News、Sports |
| **Reuse** | 变笔记、博文、简报 | 导出 Notion/Docs、框架 | Business、Psychology |

同一视频可对应一页 Category + 一页 Topic；**每个 URL 只站一轴**，用示例卡 + FAQ 横链，**不建**二维组合 URL。

### 2.3 与 YouTube 官方类目、播客楔子的关系

- **官方 API 类目** →  mostly 映射 **Category** 轴（§3.1）
- **产品 12 知识簇** →  mostly 映射 **Topic** 轴（§4）；课程/访谈/How-to 形态归 **Category**
- **YouTube 上的播客** → [`/podcast-transcription/youtube-podcast`](https://vomo.ai/podcast-transcription/youtube-podcast)（播客楔子）；YouTube 簇 `interview` Category 与之互链

---

## 3. Category 轴（18）

### 3.1 官方可上传类目对照（Data API）

| API ID | 官方类目 | VOMO Category slug |
|--------|----------|-------------------|
| 1 | Film & Animation | `film`、`animation` |
| 2 | Autos & Vehicles | `car-review` |
| 10 | Music | `music` |
| 15 | Pets & Animals | `pet-video` |
| 17 | Sports | `sports`（+ Sport 子轴） |
| 19 | Travel & Events | `travel`、`event` |
| 20 | Gaming | `gaming`（+ Format 子轴） |
| 22 | People & Blogs | `vlog` |
| 23 | Comedy | `comedy` |
| 24 | Entertainment | `entertainment` |
| 25 | News & Politics | `youtube-news`（+ Topic `politics`） |
| 26 | Howto & Style | `how-to`（+ Topic Food/Fitness/Beauty/Fashion） |
| 27 | Education | `education`（+ Format `ted-talk`） |
| 28 | Science & Technology | `science`（+ Topic Technology 等） |
| 29 | Nonprofits & Activism | `nonprofit` |

> 来源：[YouTube Data API videoCategories](https://developers.google.com/youtube/v3/docs/videoCategories)

### 3.2 Category 全量清单（18）

| # | 导航名 | slug | URL | 状态 | 主 Task | 核心听觉/结构故障 | 主词（SEO） | Persona（Who Uses） |
|---|--------|------|-----|------|---------|-------------------|-------------|-------------------|
| 1 | Education | `education` | `/tools/youtube-transcript/education` | **已上线** | Learn | 课比手速快；术语只说一遍；整门课要可检索 | YouTube lecture transcript | 学生、教师、研究者、助教 |
| 2 | Science | `science` | `/tools/youtube-transcript/science` | **已上线** | Learn | 公式、论文名、型号口播；讲座式解释 | YouTube science video transcript | 学生、教师、科普写作者、字幕 |
| 3 | How-To | `how-to` | `/tools/youtube-transcript/how-to` | **已上线** | Execute | 跟着做要倒带；步骤埋在连续口播里 | YouTube tutorial transcript | DIY、厨师、创作者、支持文档 |
| 4 | Vlog | `vlog` | `/tools/youtube-transcript/vlog` | **已上线** | Reuse | 无脚本、户外噪音、快语速 | YouTube vlog transcript | 创作者、剪辑、品牌、粉丝 |
| 5 | Interview | `interview` | `/tools/youtube-transcript/interview` | **已上线** | Quote | 多人抢话；长回答要可引用 | YouTube interview transcript | 记者、创作者、研究者、剪辑 |
| 6 | News & Politics | `youtube-news` | `/tools/youtube-transcript/youtube-news` | **已上线** | Quote | 人名地名数字；截稿时效 | YouTube news transcript | 记者、事实核查、监测、研究者 |
| 7 | Entertainment | `entertainment` | `/tools/youtube-transcript/entertainment` | **已上线** | Quote | 多 host/嘉宾/笑声叠层 | YouTube entertainment transcript | 剪辑、写手、社媒、粉丝 |
| 8 | Comedy | `comedy` | `/tools/youtube-transcript/comedy` | **已上线** | Quote | 笑点靠 exact wording；笑声不断 | YouTube comedy transcript | 喜剧人、剪辑、写手、字幕 |
| 9 | Gaming | `gaming` | `/tools/youtube-transcript/gaming` | **已上线** | Reuse | 游戏音盖过解说；超长 VOD | YouTube gaming transcript | 主播、攻略、剪辑、字幕 |
| 10 | Sports | `sports` | `/tools/youtube-transcript/sports` | **已上线** | Quote | 发布会；人名+现场噪音 | YouTube sports transcript | 记者、剪辑、分析、球迷 |
| 11 | Music | `music` | `/tools/youtube-transcript/music` | **已上线** | Quote | 人声压在配乐下；访谈/纪录片口播 | YouTube music interview transcript | 记者、标签、制作人、粉丝 |
| 12 | Film | `film` | `/tools/youtube-transcript/film` | **已上线** | Quote | 影评/essay；对白混在配乐里 | YouTube film essay transcript | 影评人、学生、剪辑、字幕 |
| 13 | Animation | `animation` | `/tools/youtube-transcript/animation` | 待建 | Quote | 配音+音效；评论/制作访谈 | YouTube animation video transcript | 评论、字幕、学生、剪辑 |
| 14 | Travel | `travel` | `/tools/youtube-transcript/travel` | 待建 | Reuse | 地名/交通/价格在街采噪音里 | YouTube travel vlog transcript | 旅行作者、向导、品牌、观众 |
| 15 | Event | `event` | `/tools/youtube-transcript/event` | 待建 | Quote | 会场混响；主持/嘉宾/问答 | YouTube conference transcript | 主办、记者、剪辑、观众 |
| 16 | Car Review | `car-review` | `/tools/youtube-transcript/car-review` | 待建 | Decide | 年款/马力/价格听错 | YouTube car review transcript | 评测作者、购车者、媒体、培训 |
| 17 | Pet Video | `pet-video` | `/tools/youtube-transcript/pet-video` | 待建 | Learn | 户外噪音+护理剂量口播 | YouTube pet video transcript | 创作者、兽医内容、品牌、主人 |
| 18 | Nonprofit | `nonprofit` | `/tools/youtube-transcript/nonprofit` | 待建 | Quote | 证词、数据、呼吁要可引用 | YouTube nonprofit video transcript | 传播、记者、捐赠人、研究 |

**Category 覆盖的产品簇：** 课程/讲座/完整教程、实操 How-to、播客/访谈/对话、新闻/体育评论、历史/纪录片（形态层）、娱乐 — **学科细分（数学/医学/法律）用 Topic 或 Education 示例卡，不另开 Category**。

**slug 规则：** kebab-case；**唯一例外** `youtube-news`（勿建 `/news`）。Interview 非官方类目，保留为能力锚点。

---

## 4. Topic 轴（16）

### 4.1 Topic 与 Category 边界（总表）

| Topic | 只管（领域词） | 让给 Category | 让给相邻 Topic |
|-------|----------------|---------------|----------------|
| Business | 创业、营销、个人品牌、面试、领导力 | Interview=对话形态；Education=课形态 | Finance=市场/交易 |
| Finance | 交易、宏观、黄金、能源、风险、数字 | News=突发口播 | Business=创业课 |
| AI | Claude、Agent、工作流、AI 工具对比 | Education=系统课形态 | Technology=硬件/发布会；Programming=代码课 |
| Programming | Python、SQL、安全、数据工程课；命令 | Education=课结构 | AI=选型；Software=SAP/Power BI |
| Software | Power BI、SAP、WordPress、认证软件操作 | How-To=通用动手 | Programming=写代码 |
| Technology | 评测、芯片、发布会、型号 | Science=科学讲座 | AI / Programming |
| Health | 临床、药名、剂量、专家访谈 | Fitness=组数动作 | Psychology=成长方法 |
| Psychology | 心理、关系、生产力框架 | Religion=经文讲道 | Health=临床 |
| Religion | 经文、神学、讲道 | — | Psychology |
| Knowledge | Crash Course 式解释；跨学科科普 | Education=整门课；TED=Format | Science |
| Politics | 竞选、政策、辩论长谈 | youtube-news=通讯社突发 | — |
| Military | 代号、军阶、装备 | News=战报快讯 | Politics |
| Food | 配方、克数、温度 | how-to=通用步骤 | — |
| Fitness | 组数、动作名、训练 | how-to=通用步骤 | Health |
| Beauty / Fashion | 成分、色号 / 设计师、面料 | how-to | — |

### 4.2 Topic 全量清单（11 旧 + 5 新）

| # | Topic | slug | URL | 状态 | 优先级 | 主 Task | 主词 | 副词（FAQ） | 产品/搜索信号 |
|---|-------|------|-----|------|--------|---------|------|-------------|---------------|
| 1 | Business | `business` | `/tools/youtube-transcript/business` | **404** | **P0** | Reuse | YouTube business video transcript | entrepreneurship notes, personal brand | 产品强；枢纽有入口卡 |
| 2 | Health | `health` | `/tools/youtube-transcript/health` | **已上线** | **P0** | Decide | YouTube health video transcript | medical lecture, supplement interview | 产品强；需加深补剂/专家访谈 |
| 3 | AI & Agents | `ai` | `/tools/youtube-transcript/ai` | **新增** | **P0** | Execute+Decide | youtube ai transcript | claude, ai agent workflow, ai summary tools | 重复导入最强；搭 `youtube transcript ai` |
| 4 | Programming | `programming` | `/tools/youtube-transcript/programming` | **新增** | **P0** | Learn+Execute | youtube coding tutorial transcript | python lecture transcript, sql tutorial | Python/SQL/安全完整课 |
| 5 | Finance | `finance` | `/tools/youtube-transcript/finance` | **新增** | **P0** | Decide | youtube finance transcript | stock market analysis transcript | 黄金/能源/宏观；站点无页 |
| 6 | Technology | `technology` | `/tools/youtube-transcript/technology` | **已上线** | P1 | Decide | youtube tech review transcript | keynote transcript | **收窄**：不吃编程课/AI 课 |
| 7 | Software & Tools | `software` | `/tools/youtube-transcript/software` | **新增** | P1 | Execute | software tutorial youtube transcript | power bi, sap training transcript | SAP/Power BI/WordPress |
| 8 | Religion | `religion` | `/tools/youtube-transcript/religion` | 待建 | P1 | Learn+Quote | youtube sermon transcript | bible study video transcript | BibleProject 重复信号 |
| 9 | Knowledge | `knowledge` | `/tools/youtube-transcript/knowledge` | 待建 | P1 | Learn | crash course transcript youtube | documentary youtube transcript | Crash Course 经典 IP |
| 10 | Psychology | `psychology` | `/tools/youtube-transcript/psychology` | **新增** | P1 | Learn+Reuse | self improvement youtube notes | productivity video transcript | 成长/关系/生产力 |
| 11 | Politics | `politics` | `/tools/youtube-transcript/politics` | 待建 | P2 | Quote | political debate youtube transcript | campaign speech transcript | 与 News 分工 |
| 12 | Military | `military` | `/tools/youtube-transcript/military` | 待建 | P2 | Quote | military analysis youtube transcript | — |  niche |
| 13 | Food | `food` | `/tools/youtube-transcript/food` | 待建 | P2 | Execute | recipe youtube transcript | cooking video to text | 与 how-to 近 |
| 14 | Fitness | `fitness` | `/tools/youtube-transcript/fitness` | 待建 | P2 | Execute | workout tutorial youtube transcript | — | 与 how-to 近 |
| 15 | Beauty | `beauty` | `/tools/youtube-transcript/beauty` | 待建 | P3 | Reuse | beauty tutorial transcript | — | 搜索有、48min 主线弱 |
| 16 | Fashion | `fashion` | `/tools/youtube-transcript/fashion` | 待建 | P3 | Reuse | fashion youtube transcript | — | 同上 |

**不做为 Topic 的：** `python`、`sql`、`claude` 各一页（作示例+FAQ）；`youtube-podcast`（播客楔子）；`lecture`/`course`/`documentary` Category（形态词）。

---

## 5. Sport 轴（4）

挂在 Category `sports` 之下；**通用发布会/评论** 吃 `sports`，本轴只吃**联赛/项目专名**。

| # | 导航名 | slug | URL | 状态 | 主词 | 专名故障 | 内链 |
|---|--------|------|-----|------|------|----------|------|
| 1 | Football | `football` | `/tools/youtube-transcript/football` | 待建 | YouTube football press conference transcript | 球员、俱乐部、战术 | → `sports` |
| 2 | Basketball | `basketball` | `/tools/youtube-transcript/basketball` | 待建 | YouTube basketball interview transcript | NBA/NCAA 专名 | → `sports` |
| 3 | MMA & Boxing | `mma-boxing` | `/tools/youtube-transcript/mma-boxing` | 待建 | MMA press conference transcript | 选手、量级、回合 | → `sports` |
| 4 | American Football | `american-football` | `/tools/youtube-transcript/american-football` | 待建 | NFL press conference transcript | 位置、码数 | → `sports` |

> 产品数据里「体育」多为**评论/分析**，非联赛专名 SEO；Sport 四页 **P2**，低于 Topic P0。

---

## 6. Format 轴（5）

**形态/片长**改变 workflow 时才独立成页；领域内容归 Topic。

| # | 导航名 | slug | URL | 状态 | 主 Task | 形态故障 | 主词 | 与 Category/Topic 分工 |
|---|--------|------|-----|------|---------|----------|------|------------------------|
| 1 | TED Talk | `ted-talk` | `/tools/youtube-transcript/ted-talk` | **已上线** | Quote | 18 分钟讲稿；官方稿难导出；TEDx 常无稿 | TED talk transcript | 知识口播 → Topic Knowledge；课 → Education |
| 2 | YouTube Shorts | `shorts` | `/tools/youtube-transcript/shorts` | **已上线** | Execute | 60 秒密口播；无声播放 | YouTube Shorts transcript | 与 48min 主线弱；SEO 保留 |
| 3 | Live Stream | `live-stream` | `/tools/youtube-transcript/live-stream` | **已上线** | Quote | 数小时无章节；回放 | YouTube livestream transcript | 新闻/发布会 → News/Sports |
| 4 | Strategy Games | `strategy-games` | `/tools/youtube-transcript/strategy-games` | 待建 | Reuse | 策略黑话+游戏音；要**有解说** | strategy game youtube transcript | → Category `gaming` |
| 5 | RPG Games | `rpg-games` | `/tools/youtube-transcript/rpg-games` | 待建 | Reuse | 技能/任务/装备名；长流程 | RPG walkthrough transcript | → Category `gaming` |

> Shorts slug 为 `shorts`，不是 `youtube-shorts`（404）。

---

## 7. 轴间边界速查（扩表）

| 左 | 右 | 分界一句 | 示例片怎么分 |
|----|-----|----------|--------------|
| Education (C) | Programming (T) | C=课形态；T=代码/数据知识 | 同 CS 课：Education 强调整学期可检索；Programming 强调命令语法 |
| Education (C) | AI (T) | C=课；T=Agent/工具/选型 | Ng 机器学习课→Education；「Top 5 AI Summary Tools」→AI |
| How-To (C) | Software (T) | C=任何动手步骤；T=某软件/认证体系 | 修马桶→How-To；Power BI 仪表盘→Software |
| How-To (C) | Programming (T) | How-To 不吃完整编程课 | 装 VS Code→How-To；100 Days of Python→Programming |
| Technology (T) | AI (T) | T=硬件/型号/发布会；AI=模型/Agent/工具栈 | 手机评测→Technology；Claude Agent→AI |
| Technology (T) | Programming (T) | Technology 不写语法课 | WWDC→Technology；SQL 窗口函数→Programming |
| Business (T) | Finance (T) | Business=创业/职业；Finance=市场/交易 | How I Built This→Business；黄金宏观→Finance |
| Interview (C) | 任意 Topic | Interview 只卖说话人/原话 | Huberman：Interview=谁说的；Health=剂量病名 |
| Science (C) | Knowledge (T) | Science=讲座式科学；Knowledge=Crash Course 式解释 | 大学物理课→Science；Crash Course 单集→Knowledge |
| News (C) | Politics (T) | News=突发/通讯社；Politics=政策/竞选长谈 | 地震快讯→News；国会听证→Politics |
| Sports (C) | Football 等 (S) | Sports=通发；Sport=联赛专名 | 通稿→Sports；英超发布会→Football |
| Gaming (C) | Strategy/RPG (F) | Gaming=通 VOD；Format=类型黑话 | 通用解说 VOD→Gaming；文明 VI 攻略解说→Strategy |
| TED (F) | Knowledge (T) | TED=18 分钟讲稿形态；Knowledge=系列解释 IP | TED 舞台→TED；Crash Course→Knowledge |
| youtube-transcript 枢纽 | AI Summary 任务词 | 枢纽吃 head 词；Topic/L4 吃 summary/notes | `youtube transcript`→枢纽；`youtube ai transcript`→AI |

---

## 8. 线上库存汇总

### 8.1 枢纽

| URL | 角色 | 状态 |
|-----|------|------|
| [`/tools/youtube-transcript`](https://vomo.ai/tools/youtube-transcript) | L2；head 词 + Paste YouTube + 四轴入口 | **已上线** |

枢纽入口卡（2026-08-23）：仅 **News**（Category）、**Business**（Topic，链 404）。导航下拉已有 38 切片，**卡片层待铺开**。

### 8.2 按轴统计

| 轴 | 规划 | 已上线 | 待建/404 | 新增（本方案） |
|----|------|--------|----------|----------------|
| Category | 18 | 12 | 6 | 0 |
| Topic | **16** | 2 | 9 + business **404** | **5** |
| Sport | 4 | 0 | 4 | 0 |
| Format | 5 | 3 | 2 | 0 |
| **合计** | **43** | **17** | **26** | **5** |

### 8.3 已上线 17 页（快查）

`education` · `science` · `how-to` · `vlog` · `interview` · `youtube-news` · `entertainment` · `comedy` · `gaming` · `sports` · `music` · `film` · `health` · `technology` · `ted-talk` · `shorts` · `live-stream`

### 8.4 P0 排产（不改旧页，只增/补）

1. `business`（Topic，404 补洞）
2. `ai` · `programming` · `finance`（Topic 新增）
3. 改写叙事（可选）：`education`、`technology`、`health` — 对齐产品 48 分钟 + 知识任务
4. 枢纽 By Category / By Topic 网格；P0 Topic 进第一屏

---

## 9. 产品簇 → 四轴映射

| 产品端内容簇 | Category | Topic | Format | 备注 |
|--------------|----------|-------|--------|------|
| 课程、讲座、考试、完整教程 | **Education** | （学科作示例，不拆页） | — | 数学/医学/法律/会计/语言/认证 |
| AI、编程、软件工具 | How-To（部分） | **AI** · **Programming** · **Software** · Technology | — | 三者边界见 §4.1 |
| 实操 How-to | **How-To** | Food · Fitness | — | |
| 商业、营销、创业、职业 | Interview（对话形态） | **Business** | — | |
| 播客、访谈、人物对话 | **Interview** | — | — | + 播客 `youtube-podcast` |
| 金融、投资、交易、宏观 | News（快讯形态） | **Finance** | — | |
| 健康、医学、健身、营养 | — | **Health** · Fitness | — | |
| 心理、自我成长、生产力 | — | **Psychology** | — | |
| 宗教、神学、讲道 | — | **Religion** | — | 对齐 BibleProject |
| 新闻、政治、社会、体育评论 | **youtube-news** · Sports | Politics | Live Stream | 体育评论≠Sport 联赛页 |
| 历史、科学、纪录片、文化 | Science · Film | **Knowledge** | TED | |
| 娱乐、影视、音乐、游戏 | Entertainment · Comedy · Music · Film · Gaming | — | Shorts | 产品优先级低于学习簇 |

---

## 10. SEO 与关键词

### 10.1 层级

| 层级 | 示例 | 承接 |
|------|------|------|
| L2 枢纽 | youtube transcript (~823K)、youtube transcript generator (~110K)、youtube video transcript (~135K) | `/tools/youtube-transcript` |
| L3 Category | youtube lecture transcript、youtube interview transcript、youtube news transcript | `/tools/youtube-transcript/{category-slug}` |
| L3 Topic | youtube ai transcript、youtube coding tutorial transcript、youtube finance transcript | `/tools/youtube-transcript/{topic-slug}` |
| L3 Sport | youtube football press conference transcript | Sport slug |
| L3 Format | TED talk transcript、youtube livestream transcript | Format slug |
| L4 任务 | youtube to notes、youtube video summarizer、youtube to blog | 枢纽 hero + Guide；**不新开第五轴** |

> 头词量级来源：行业公开数据（2026 初）；Topic 长尾待 Ahrefs/Semrush 回填。

### 10.2 Title / H1 约定

- **模式：** `YouTube {Name} Transcript Generator`（News 页 title 用 News，slug 仍 `youtube-news`）
- **页眉标签：** `YouTube Category` | `YouTube Topic` | `YouTube Sport` | `YouTube Format`
- **每页一个主词**；副词进 FAQ

### 10.3 高优 Topic 搜索包（写 brief 用）

| Topic | Primary | Secondary |
|-------|---------|-----------|
| ai | youtube ai transcript | ai agent tutorial notes, youtube ai summary tools |
| programming | youtube coding tutorial transcript | python lecture transcript, sql tutorial to text |
| business | youtube business video transcript | entrepreneurship video notes, personal brand |
| finance | youtube finance transcript | stock market analysis transcript, macro economics |
| health | youtube health video transcript | medical lecture transcript, expert interview |
| software | software tutorial youtube transcript | power bi youtube notes, sap training |
| religion | youtube sermon transcript | bible study video transcript |
| knowledge | crash course transcript youtube | documentary youtube transcript |

---

## 11. 与存量 URL / 播客 / 博客

| 路径 | 关系 |
|------|------|
| `/tools/youtube-video-summarizer` | 摘要 L4；子页提 summary，不重复建页 |
| `/tools/transcribe-ted-audio-video` | 301/导流 → `ted-talk` |
| `/tools/transcribe-lecture-to-text` | 导流 → `education` |
| `/tools/transcribe-interview-to-text` | 通用访谈；YouTube 访谈 → `interview` |
| `/podcast-transcription/youtube-podcast` | 视频播客；与 `interview` 互链 |
| `/guide/how-to-extract-audio-from-a-youtube-video` | 非 YouTube 场景 FAQ 内链 |
| [podcast transcription/](../podcast%20transcription/podcast-platforms.md) | Business/Christian/True Crime 体裁话术可对照 Topic |

---

## 12. 明确不做

| 不做 | 原因 |
|------|------|
| Category：`course`、`lecture`、`documentary`、`podcast` | 形态词已有 Education / Interview / Film |
| Topic：按品牌/语言拆页（`python`、`claude`、`cnn`） | 示例卡承接；维护爆炸 |
| 二维 URL `/education/programming` | 用横链代替 |
| 第五轴「Task」URL | Task 只驱动文案 |
| 为产品弱簇优先铺 Sport 联赛 / Beauty / Fashion | 让位于 Topic P0 |

---

## 13. 导航与 sitemap 缺口

| 露出 | 现状 | 建议 |
|------|------|------|
| 顶栏四轴下拉 | 38 切片（旧规划） | 更新 Topic 至 16 项（+5 新 Topic 名） |
| 枢纽卡片 | 仅 News + Business | P0：Education、AI、Programming、Interview、Finance |
| 英文 sitemap | 2026-07 仅枢纽 | 17 已上线子页 + 新增页及时收录 |

---

## 14. 数据来源

| 数据点 | 来源 |
|--------|------|
| YouTube 官方类目 ID | [videoCategories API](https://developers.google.com/youtube/v3/docs/videoCategories) |
| 四轴结构与线上 17 页 | vomo.ai 实测 2026-08-23 |
| 产品内容簇 / 48 分钟 / 重复导入 | 产品端 first-party 2026-08 |
| head 词量级 | 行业公开数据（youtube transcript ~823K 等，2026 初） |
| Topic 扩列（+5） | 产品数据 + SEO 意图对齐方案 2026-08-24 |
| 页面模具 | [page-playbook.md](./page-playbook.md) |
| 播客 YouTube 页 | [podcast-platforms.md](../podcast%20transcription/podcast-platforms.md) §4.2 |

---

*Last updated: 2026-08-24*
*创建日期: 2026-08-23*
*所属项目: VOMO（https://vomo.ai/）*
