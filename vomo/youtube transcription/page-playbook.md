# VOMO — YouTube 分类转录页生产手册

## 1. 一句话原则

**同一工具，换「这类视频的听觉故障 + 谁必须用文字」。**  
禁止再写一遍枢纽页的通用卖点清单。如果把类目名换成另一个页仍然成立，这段就废了。

对照：News 写「人名、地名、数字被自动字幕拧坏，截稿前要可引用」；Education 写「术语只说一遍，整节课要变成可检索笔记」。两页 CTA 都是粘贴链接，理由完全不同。

---

## 2. 页面模具（按线上已上线页还原）

顺序固定，不要增删大节、不要把 FAQ 挪到中间。

```
面包屑 / 轴标签     YouTube Category | Topic | Sport | Format
H1                  YouTube {Name} Transcript Generator
英雄段（1–2 句）     这类音频为什么难 + VOMO 交什么
工具区               Upload File | Paste a Link | 主按钮
辅助说明             Only YouTube URLs… / Supports: 链接 + 音视频格式 + 语种
示例卡 × 8           标题 · 频道 · Use This Link（Shorts/部分页可带头像时长）
H2 Why Transcribe    总述 1 句 + 3 张利益卡
H2 Why Choose VOMO   总述 1 句 + 4 条能力（A–D）
H2 Who Uses VOMO     总述 1 句 + 4 个 Persona
H2 How to … 3 steps  粘贴 → 转录（点出本类差异）→ 导出/引用
H2 FAQS              6 问；第一问默认展开
底栏 CTA             一句场景化收束 + Start transcribing / Try VOMO
```

### 2.1 英雄段公式

`{听觉或时效故障}。Paste the link and VOMO returns {本类交付物}。`

| 页 | 已上线英雄段在写什么 |
|----|----------------------|
| News | 五分钟新闻里的人名地名数字；自动字幕例行拧坏 → 带时间戳、分说话人、头条要点在上 |
| Education | 课比手速快；自动字幕丢掉关键术语 → 可变成笔记的带时间戳稿 |
| Interview | 两个人抢话，自动字幕塌掉 → 每条标说话人 + 时间戳 |
| How-To | 跟着教程就要暂停倒带 → 整段变成可按自己节奏读的步骤 |
| Sports | 发布会是引用金矿，人名和现场噪音毁字幕 → 人名对、引用能用 |
| Shorts | 又快又密，经常没字幕 → 几秒出完整脚本 |
| Live Stream | 直播数小时无脚本无章节 → 整场回放变成可搜文本 |
| Health | 药名剂量临床词是自动字幕的崩点 → 医学词汇能活下来 |

### 2.2 Why Transcribe（3 卡）

每卡：**短标题 + 一句后果**。三卡应分别覆盖：① 听错的代价 ② 时长/结构 ③ 下游任务（引用、笔记、字幕、步骤）。

### 2.3 Why VOMO（4 条）

从 [youtube-categories.md §4.2 / §10](./youtube-categories.md) 为本类挑 4 条，写成「故障 → 结果」，不要功能名堆砌。

禁止四页共用同一组：

- Transcripts in seconds
- Any video length
- Timestamps for every line
- Summaries and exports

那是枢纽的 ABCD。子页必须换成本类故障。

### 2.4 Who Uses（4 人）

每人：**角色名 + 两句**（要做什么 / 没有文本会怎样）。四个角色不要全是「创作者」。News 用记者、事实核查、监测、研究者；Education 用学生、教师、研究者、助教。

### 2.5 三步 How-to

1. 粘贴 **这类** 链接（点名形态：lecture / presser / Shorts / replay）
2. 转录时发生的 **本类差异**（分说话人 / 隔离游戏音 / 保留剂量）
3. 导出或下游动作（引用、SRT、步骤清单、笔记）

### 2.6 FAQ（6 问）

第一问回答本类最可能的异议，并在页上展开。其余 5 问覆盖：噪音/口音、说话人、时长、非 YouTube 上传、其他语言或导出。  
**不要承诺画面里没说出口的步骤。** How-To 页已写清：只转说出的步骤。  
**不要承诺未结束的直播。** Live Stream 页：等回放。  
**Music 页已限制歌词：** 以口播/访谈为主，唱段不可靠——新页涉及配乐时沿用这条诚实边界。

### 2.7 示例卡规则

- **正好 8 条**，与已上线页一致。
- 频道一眼能代表该类：News 用 BBC / CNN / Al Jazeera / NBC；Education 用 MIT / Yale；Sports 用 ESPN / FOX Sports。
- 标题用真实公开视频，不要编造片名。
- 不要八条都来自同一频道（Technology 页 Mrwhosetheboss 过密，补页不要学）。
- Film 页用影评 / video essay，不要用整部正片；Music 用访谈/纪录片，不要用官方 MV 当主示例。
- Shorts 必须是 `/shorts` 形态；Live Stream 必须是回放/发布会，不要用 8 分钟 Vlog 充数。
- 版权：只链公开 YouTube URL，不提供下载片源。

---

## 3. 文案语气

| 要 | 不要 |
|----|------|
| 具体故障：药名、队名、型号、倒带、截稿 | 「强大的 AI」「99% 准确」当主句 |
| 动词清楚：paste、quote、export、search | 「赋能」「一站式」 |
| 承认边界：官方 TED 稿、歌词、未结束直播、没说出口的步骤 | 贬低 YouTube 官方字幕到「完全不能用」而不举例 |
| 英文页、短句、具体名词 | 中英混标题；把子页写成 2000 字博客 |

产品事实与 [vomo-features.md](../vomo-features.md) 对齐：粘贴 YouTube 链接、上传音视频、说话人、时间戳、Smart Notes / 章节、导出 TXT/DOCX/PDF/SRT。免费试用话术与站点现行 CTA 一致。不在分类页发明新套餐。

---

## 4. SEO 与内链

- **Title：** `{YouTube} {Name} Transcript Generator | {本类结果} | VOMO`
- **H1：** 与 title 同义，允许视觉换行。
- **主词一个。** 见 [youtube-categories.md §10](./youtube-categories.md)。
- **链回** `/tools/youtube-transcript`（面包屑或首段一次即可）。
- **横链最多 2 个近亲**（Science↔Technology，Sports↔Football），不要在正文堆 38 个分类。
- **不要** 再造 `/tools/transcribe-youtube-{slug}` 平行 Tools 页。
- News 保持 `/youtube-news`；新 News 相关内容不要创建 `/news`。

---

## 5. 交付检查清单（发页前）

- [ ] 轴标签正确（Category / Topic / Sport / Format）
- [ ] slug 与 [youtube-categories.md §3–§6](./youtube-categories.md) 权威清单一致；不是第二个 News / Shorts 别名
- [ ] 英雄段换成别的类目会失效
- [ ] Why ×3、VOMO ×4、Persona ×4、步骤 ×3、FAQ ×6
- [ ] 8 条真实示例，频道多样
- [ ] 未承诺：未结束直播、未说出的步骤、整部受版权电影、可靠歌词
- [ ] 枢纽入口卡已加上（至少 Category/Topic 网格里看得到）
- [ ] 需要索引则写入英文 sitemap

---

## 6. 待建 / 待核验页 Brief

先打开 URL。已是完整模具页则只做质检，不要重写。404 或薄页才按 brief 生产。  
`business` 已确认 404，**第一个补。**

### 6.1 P0 — Business（Topic）`/tools/youtube-transcript/business`

| 项 | 内容 |
|----|------|
| 主词 | YouTube business video transcript |
| 英雄故障 | 创业路演、访谈里的框架/数字/公司名被听错；要可复用笔记不是重看 |
| 交付物 | 带时间戳的可引用稿 + 摘要/框架 |
| FAQ 首问 | 和 Finance Topic 有何不同？（Business=创业/职业；Finance=市场/交易） |
| 边界 | 不抢 Interview Category 的「说话人」叙事 |

### 6.2 P0 — 新增 Topic（产品数据驱动）

**AI** `ai`（Topic）  
故障：模型名、产品名、workflow 步骤被听成普通词；用户要选型结论。交付：可对比要点 + 时间戳。示例：Claude/Agent 搭建、*Top 5 YouTube AI Summary Tools*。FAQ：与 Programming / Technology 的分界（见 youtube-categories §4.1）。

**Programming** `programming`（Topic）  
故障：函数名、SQL、路径被转写错。交付：可复制命令 + 整门课可搜索。示例：Python/SQL/网络安全完整课。FAQ：与 Education（课形态）/ Software（SAP 点菜单）的分界。

**Finance** `finance`（Topic）  
故障：价格、百分比、ticker、宏观专名。交付：可核对数字 + 摘要。示例：黄金、能源、市场风险。FAQ：与 Business 的分界。

**Software** `software`（Topic，P1）  
故障：菜单路径、版本、认证考点。交付：步骤清单（只说出口的步骤）。示例：Power BI、SAP、WordPress。

**Psychology** `psychology`（Topic，P1）  
故障：概念名、框架被听错。交付：可复用框架笔记。示例：关系、习惯、生产力（无讲台经文）。FAQ：与 Religion / Health 的分界。

> 全量 Topic 表见 [youtube-categories.md §4.2](./youtube-categories.md)。

### 6.3 P1 — 高意图 Brief（Category / Sport / 其余 Topic）

**Politics** `politics`（Topic）  
故障：候选人、法案编号、机构名被拼音化。交付：可引用、可对照日期的文本。Persona：记者、政策研究员、竞选传播、事实核查。近亲：只链 `youtube-news`。示例：国会听证、竞选演讲、政策长访——不要复用 News 的突发灾情片。

**Food** `food`（Topic）  
故障：克数、温度、锅具口播埋在闲聊里。交付：可复制的用量与步骤摘要。Persona：家庭厨师、食谱编辑、创作者、过敏/饮食记录者。边界：没念出来的画面步骤不编造。近亲：`how-to`。

**Fitness** `fitness`（Topic）  
故障：组数、秒数、动作名在配乐里丢失。交付：可执行的组次清单 + 时间戳回看示范。Persona：教练、学员、健身编辑、物理治疗学习者。边界：不写医疗建议；示范仍以视频为准。

**Football** `football`（Sport）  
故障：球员名、俱乐部、比分、战术词。交付：发布会/解说引用。Persona：记者、切片编辑、分析、球迷。链回 `sports`。示例用足球发布会与战术分析，不要混 NBA。

**Basketball** `basketball`（Sport）  
同上，专名换成 NBA/NCAA/FIBA。Sports 页已有一批篮球发布会，本页示例必须更「篮球专名」，避免八条克隆 Sports。

**Animation** `animation`（Category）  
故障：配音、旁白、音效叠在一起；video essay 引用台词。交付：旁白/评论可检索。Persona：评论作者、字幕、学生、切片。边界：不提供整部动画电影逐字稿下载。与 `film` 分开：本页示例用动画评论/制作访谈，不用真人影评。

**Travel** `travel`（Category）  
故障：地名、车站、价格在风声和街采里。交付：行程与地点可搜。Persona：旅行作者、向导、品牌、观众做攻略。近亲：`vlog`（旅行 vlog 仍以地点/交通专名为主，不要写成日常 routine）。

### 6.4 P2 — 补全导航（短 brief）

写页时仍走第 2 节模具；下表只锁故障与 Persona。

| Slug | 轴 | 听觉故障 | 四人 |
|------|----|----------|------|
| `event` | Category | 会场混响、主持/嘉宾/观众问答 | 主办、记者、剪辑、未到场观众 |
| `car-review` | Category | 型号、年款、马力、价格被听成别的车 | 评测作者、购车者、经销商培训、媒体 |
| `pet-video` | Category | 户外/家居噪音 + 口播护理剂量 | 创作者、兽医内容、品牌、宠物主人 |
| `nonprofit` | Category | 证词、数据、捐赠呼吁要可引用 | 传播官、记者、捐赠人、研究者 |
| `religion` | Topic | 经文、人名、礼仪术语不可近似 | 讲者、学员、译者、档案 |
| `military` | Topic | 代号、军阶、装备型号 | 记者、分析、学员、档案 |
| `knowledge` | Topic | 跨学科解释片术语（不是课程、不是 TED） | 终身学习者、编辑、教师、字幕 |
| `beauty` | Topic | 产品名、成分、色号 | 创作者、编辑、柜台培训、观众 |
| `fashion` | Topic | 设计师、系列、面料、尺码 | 记者、买手、学生、品牌社媒 |
| `mma-boxing` | Sport | 选手名、量级、回合、赛后采访噪音 | 记者、切片、分析、粉丝 |
| `american-football` | Sport | 球员、位置、码数、发布会 | 记者、切片、分析、粉丝 |
| `strategy-games` | Format | build、patch、地图黑话压在游戏音下 | 主播、攻略作者、剪辑、选手 |
| `rpg-games` | Format | 技能、任务、装备名；超长流程 | 主播、攻略、剪辑、字幕 |

`strategy-games` / `rpg-games` 必须链回 `gaming`，示例不要再用「No Commentary 全流程」占满 8 卡——那种片几乎没有可转口播，Gaming 页已偏了。本两页应选 **有解说的** 策略/RPG。

---

## 7. 生产顺序（建议）

```
1. HEAD 核验 youtube-categories.md §8 全部 slug
2. P0：business → ai → programming → finance
3. 按模具一次只做 1 页；过第 5 节清单
4. 枢纽补入口卡 + sitemap
5. P1 Topic（software、religion、knowledge…）→ P2 Category/Sport/Format
6. 博客只做 L4 任务文，不代替子页
```

一页一个 brief 发实现，不要十条需求塞进一次改动。

---

*遵循 [客户文档规范](../../demo/client-template.md)*
*关联：[youtube-categories](./youtube-categories.md) | [主文档](../vomo.md) | [features](../vomo-features.md)*
*用途：按同一模具写出 [`/tools/youtube-transcript/youtube-news`](https://vomo.ai/tools/youtube-transcript/youtube-news) 这一级子页。不在此改产品逻辑。*
*Last updated: 2026-08-24*
*创建日期: 2026-08-23*
*所属项目: VOMO（https://vomo.ai/）*
