# Dynal · LinkedIn Post Generator Topic 详表

**文档职责**：本文为 **`/linkedin-post-generator/{topic}`** 子页的 **topic 选题、优先级与落地策略** 唯一权威。维护 30 个帖型 topic（10 个已上线 + 8 个 Tier 1 候选 + 12 个 Tier 2 候选）+ 5 个跨平台内容转制 topic（1 个已规划 + 4 个新增候选），覆盖 LinkedIn 全部 10 种原生格式中的 8 种，含 slug、内容类型、搜索需求侧证、B2B 场景集群映射。**不替代**主产品功能详解（见 [../dynal-features.md](../dynal-features.md)）。

> **关联**：[dynal-linkedin-post-generator.md](./dynal-linkedin-post-generator.md)（主入口、路由状态）| [dynal-pg-keywords.md](./dynal-pg-keywords.md)（PG 簇关键词详表）| [dynal-pg-competitors.md](./dynal-pg-competitors.md)（竞品深析）| [../dynal-site-structure.md](../dynal-site-structure.md)（线上 URL 权威）| [../dynal-tools.md](../dynal-tools.md)（工具 #2–#12）

**Last updated**: 2026-05-11 — 扩至 30 个帖型 topic + 5 个跨平台内容转制 topic：新增 4 个 Tier 1（video-post、newsletter-content、data-driven-post、lead-generation，覆盖格式/商业缺口）+ 6 个 Tier 2（contrarian-post、career-transition、team-appreciation、failure-lesson、learning-journey、routine-productivity，覆盖用户场景缺口）+ 4 个内容转制候选（tiktok-to-linkedin-post、youtube-to-linkedin-post、tweet-to-linkedin-post、url-to-linkedin-post，覆盖跨平台内容复用场景）。LinkedIn 平台原生格式覆盖率 80%。

---

## 0. 边界

- **本文**：仅管理 `/linkedin-post-generator/{topic}` 子页的选题与落地策略。
- **「选题类」意图**（*linkedin post ideas*、*what to post on linkedin* 等）→ 见 [../dynal-keywords.md](../dynal-keywords.md) §6 与 [../dynal-tools.md](../dynal-tools.md) 工具 #4。
- **主产品 agent 叙事**（Brand DNA、周计划、审批）→ 见 [dynal-linkedin-post-generator.md](./dynal-linkedin-post-generator.md) §1。
- **跨平台内容转制**（TikTok/YouTube/X/URL → LinkedIn）→ 见本文 §1.4；与 §1.1–§1.3 的帖型 topic 为不同维度（「来源」vs「帖型」）。

---

## 1. 帖型 Topic 总表（30 个）

### 1.1 已上线（10 个，sitemap 收录）

| # | Slug | 中文说明 | 内容类型 | 上线状态 |
|---|------|----------|----------|----------|
| 1 | `announcement-post` | 公告/公司新闻 | 公告 | sitemap: monthly/0.7 |
| 2 | `case-study` | 案例研究/客户成功 | 社会证明 | sitemap: monthly/0.7 |
| 3 | `engagement-post` | 互动/对话帖 | 互动 | sitemap: monthly/0.7 |
| 4 | `farewell-post` | 离职/告别帖 | 个人里程碑 | sitemap: monthly/0.7 |
| 5 | `hiring-post` | 招聘帖 | 雇主品牌 | sitemap: monthly/0.7 |
| 6 | `hook-generator` | Hook 生成器 | 文案结构 | sitemap: monthly/0.7 |
| 7 | `how-to-post` | 教程/指南帖 | 教育 | sitemap: monthly/0.7 |
| 8 | `recommendation` | 推荐/背书帖 | 社会证明 | sitemap: monthly/0.7 |
| 9 | `storytelling-post` | 故事叙述帖 | 个人品牌 | sitemap: monthly/0.7 |
| 10 | `thought-leadership` | 思想领导力帖 | 权威建设 | sitemap: monthly/0.7 |

### 1.2 候选 Tier 1 — 强信号优先开发（8 个）

> 标准：竞品独立页密集 + 搜索需求明确 + LinkedIn 算法趋势对齐，或格式/商业缺口明显。**建议优先开发落地页**。

| # | Slug | 中文说明 | 内容类型 | 侧证强度 | 搜索需求信号 | 分类 |
|---|------|----------|----------|----------|-------------|------|
| 11 | `behind-the-scenes` | 幕后/公司文化/日常 | 文化/真实性 | 强 | ContentIn、Forbes（LinkedIn 2026 算法奖励类型） | 内容驱动 |
| 12 | `milestone-post` | 里程碑庆祝（周年/晋升/业绩） | 个人里程碑 | 强 | ContentIn、Grammarly、CoSchedule 均有独立模板 | 内容驱动 |
| 13 | `product-launch` | 产品发布/新功能公告 | 公告 | 强 | CoSchedule、Grammarly、ContentIn 均有独立页 | 内容驱动 |
| 14 | `industry-insight` | 行业趋势/新闻评论 | 权威建设 | 强 | Taplio News Finder、Lnkin（Perplexity 驱动）、Forbes 推荐 | 内容驱动 |
| 21 | `video-post` | LinkedIn 原生视频帖 | 格式驱动 | 中 | 视频是 LinkedIn 第二高互动率格式（6%）；"linkedin video post generator/tips" 有搜索量；竞品几乎无独立页 | **格式缺口（蓝海）** |
| 22 | `newsletter-content` | LinkedIn Newsletter 内容 | 格式驱动 | 中 | LinkedIn 增长最快格式（150% YoY）；"linkedin newsletter content" 搜索需求上升；竞品零覆盖 | **格式缺口（蓝海）** |
| 23 | `data-driven-post` | 数据/统计/图表帖 | 内容驱动 | 中 | B2B 高频需求；多图帖是获赞率最高格式（6.45%）；竞品无独立覆盖 | **内容缺口（蓝海）** |
| 24 | `lead-generation` | 获客/转化帖 | 商业驱动 | 中 | 高商业意图；"linkedin post to get clients" 精准搜索；与 Dynal「grow presence」叙事直接对齐 | **商业缺口** |

### 1.3 候选 Tier 2 — 中信号验证后上线（12 个）

> 标准：竞品有相关功能但独立页较少 + 搜索量待验证，或与现有 topic 互补但不急迫。

| # | Slug | 中文说明 | 内容类型 | 侧证强度 | 搜索需求信号 | 分类 |
|---|------|----------|----------|----------|-------------|------|
| 15 | `listicle-post` | 清单体（X 个方法/步骤/工具） | 教育 | 中 | Graphite Note、OutXAI、Forbes 推荐格式 | 内容驱动 |
| 16 | `poll-post` | LinkedIn 投票帖 | 互动 | 中 | Forbes（2026.05：LinkedIn 算法当前奖励） | 格式驱动 |
| 17 | `personal-brand` | 个人品牌建设帖 | 个人品牌 | 中 | ContentIn、Ligo、buzzli 均有独立功能 | 内容驱动 |
| 18 | `event-promotion` | 活动/webinar 推广 | 公告 | 中 | CoSchedule、ContentIn 有独立模板 | 内容驱动 |
| 19 | `carousel-post` | 轮播/PDF 文档帖 | 版式 | 中 | Taplio Carousel、Contentdrips（最高停留时长格式） | 格式驱动 |
| 20 | `blog-to-post` | URL/博客转 LinkedIn 帖 | 内容复用 | 低 | MagicPost、Taplio Repurpose、RedactAI | 内容复用 |
| 25 | `contrarian-post` | 挑战共识/争议观点帖 | 权威建设 | 中 | Forbes 2026 确认 LinkedIn 奖励可辩论内容；与 thought-leadership 互补（后者教育，此挑战） | 用户场景 |
| 26 | `career-transition` | 职业转型/新角色官宣 | 个人品牌 | 中 | 与 farewell-post（离开）互补：此面向新开始；"linkedin career change post" 有搜索需求 | 用户场景 |
| 27 | `team-appreciation` | 团队表彰/员工 spotlight | 雇主品牌 | 低 | 雇主品牌/招聘/文化建设场景；与 behind-the-scenes 互补（BTS=日常，此=表彰） | 用户场景 |
| 28 | `failure-lesson` | 失败/教训分享帖 | 个人品牌 | 中 | 高真实性帖型；LinkedIn 2026「不完美叙事」互动率更高；与 storytelling-post 互补 | 用户场景 |
| 29 | `learning-journey` | 公开学习/ Build in Public | 个人品牌 | 低 | Indie hacker/创始人高频场景；与 Dynal ICP 高度重合；"build in public linkedin" 精准 | 用户场景 |
| 30 | `routine-productivity` | 工作流/习惯/系统分享 | 教育 | 低 | 高收藏率帖型；可复制的系统类内容；与 how-to-post 互补（how-to=教人，此=分享自己） | 用户场景 |

---

### 1.4 跨平台内容转制（Content Repurposing）— 5 个

> **与 §1.1–§1.3 的本质区别**：帖型 topic 回答「我要写什么类型的 LinkedIn 帖？」（announcement / case-study / thought-leadership…）；跨平台转制 topic 回答「我的内容在另一个平台，怎么转成 LinkedIn 帖？」（来源驱动而非帖型驱动）。两者互补：用户可先选来源（如 YouTube → LinkedIn），再选帖型（如 how-to-post）。
>
> 标准：竞品独立功能/工具验证 + 跨平台内容复用需求明确 + 与 Dynal「多源输入」agent 叙事对齐。

| # | Slug | 中文说明 | 来源平台 | 侧证强度 | 搜索需求信号 | 分类 |
|---|------|----------|----------|----------|-------------|------|
| CP-1 | `blog-to-post` | 博客/文章转 LinkedIn 帖 | Blog / Article URL | 中 | MagicPost、Taplio Repurpose、RedactAI 均有此功能；与 §1.3 #20 为同一 topic | 内容转制 |
| CP-2 | `tiktok-to-linkedin-post` | TikTok 短视频转 LinkedIn 帖 | TikTok | 中 | Apify Video 2 Social Post、ContentSplitter、Repurposer 均支持；短视频内容复用是 2026 跨平台趋势 | 内容转制 |
| CP-3 | `youtube-to-linkedin-post` | YouTube 视频转 LinkedIn 帖 | YouTube | 强 | RedactAI（$15.80/mo）、Tugan.ai（$29/mo）、ContentRadar（$14/mo）均有独立 YouTube→LinkedIn 功能；"youtube to linkedin post" 搜索需求明确 | 内容转制 |
| CP-4 | `tweet-to-linkedin-post` | Tweet / X 帖子转 LinkedIn 帖 | X (Twitter) | 中 | Tugan.ai、ContentRadar、Repurposer、ContentRepurpose.pro 均支持；X 与 LinkedIn 用户群高度重叠，跨平台复用需求强 | 内容转制 |
| CP-5 | `url-to-linkedin-post` | 任意 URL 转 LinkedIn 帖 | Any URL | 强 | Tugan.ai（"Article to LinkedIn Post"）、RedactAI（blog URL → LinkedIn）、ContentRadar（URL/PDF/Notion → LinkedIn）；覆盖面最广的转制入口 | 内容转制 |

> **CP-1（blog-to-post）与 §1.3 #20 为同一 topic**：在帖型维度属于「内容复用」类，在转制维度属于「Blog → LinkedIn」。两处均保留引用以维护各自维度的完整性。

---

## 2. 落地优先级建议

### 2.1 Tier 1（8 个，建议优先开发）

**格式缺口（蓝海，竞品几乎无覆盖）**：
- **#21 video-post**：LinkedIn 原生视频互动率 6%，平台第二高；"linkedin video post generator" 蓝海词
- **#22 newsletter-content**：增长最快格式（150% YoY），"linkedin newsletter content ideas" 需求上升
- **#23 data-driven-post**：B2B 数据帖高频需求；多图帖获赞率最高（6.45%）
- **#24 lead-generation**：最高商业意图；与 Dynal「grow presence」直接对齐

**内容驱动（竞品有独立页，搜索需求明确）**：
- **#11 behind-the-scenes**：Forbes 2026.05.03 确认 LinkedIn 算法奖励「真实性」内容
- **#12 milestone-post**：Grammarly、CoSchedule 均有独立生成器
- **#13 product-launch**：高商业意图，与产品增长直接相关
- **#14 industry-insight**：Taplio News Finder 模式验证；Lnkin 用 Perplexity 自动生成

### 2.2 Tier 2（12 个，搜索量工具验证后按需上线）

- **#15 listicle-post**：搜索量分散于长尾「X ways to...」句式；可先做 blog resource
- **#16 poll-post**：LinkedIn 原生功能，独立生成器需求待验证
- **#17 personal-brand**：与 Brand DNA 叙事强相关；适合与 agent 主叙事合并
- **#18 event-promotion**：季节性需求
- **#19 carousel-post**：与 [../dynal-tools.md](../dynal-tools.md) 工具 #9 重叠；需定产品边界
- **#20 blog-to-post**：与 [../dynal-tools.md](../dynal-tools.md) 工具 #6 重叠
- **#25 contrarian-post**：与 thought-leadership 互补（挑战 vs 教育）；搜索量待验证
- **#26 career-transition**：与 farewell-post 互补（新开始 vs 离开）；更积极的个人品牌意图
- **#27 team-appreciation**：雇主品牌/招聘联动；低搜索量但精准
- **#28 failure-lesson**：高真实性、高互动率趋势帖型
- **#29 learning-journey**：Indie hacker/创始人精准人群；低量高价值
- **#30 routine-productivity**：高收藏率；系统化内容差异化强

### 2.3 跨平台内容转制（5 个，建议与帖型 topic 并行开发）

**来源平台覆盖（竞品已普遍布局）**：
- **CP-3 youtube-to-linkedin-post**：侧证最强——RedactAI、Tugan.ai、ContentRadar、MagicPost 均有独立功能；YouTube 是 B2B 内容营销最大视频源
- **CP-5 url-to-linkedin-post**：覆盖面最广——任意 URL 均可转制；Tugan.ai 核心功能
- **CP-2 tiktok-to-linkedin-post**：短视频跨平台复用——2026 年 Gen Z 进入 B2B 决策层的趋势驱动
- **CP-4 tweet-to-linkedin-post**：X 用户群与 LinkedIn 高度重叠——thought leadership 内容双平台发布的刚需
- **CP-1 blog-to-post**：已有规划；与 tools 工具 #6 边界待定

**战略价值**：跨平台转制直接对齐 Dynal「多源输入」（notes/links/files）agent 叙事——不是「又一个 repurposing tool」，而是「你的 AI LinkedIn agent 理解你的全部内容资产」。且竞品（Taplio、ContentIn）的 repurposing 均为附属功能，无独立 topic 页矩阵，Dynal 可占「YouTube to LinkedIn post generator」等关键词的品类独占。

---

## 3. LinkedIn 平台格式覆盖率

> Dynal 30 个 topic 覆盖 LinkedIn 全部 10 种原生格式中的 8 种（缺 Long-Form Article 和 Reshare，两者生成器搜索需求极低）。

| LinkedIn 原生格式 | 2026 互动率 | Dynal topic 覆盖 |
|---|---|---|
| Text-Only | 4.50% | ✅ 多数 topic（默认帖型） |
| Single Image | 5.30% | ✅ 间接覆盖（各 topic 模板可含图） |
| Multi-Image | 6.45% | ✅ data-driven-post、behind-the-scenes |
| Document/Carousel（PDF） | **7.00%** | ✅ carousel-post |
| Native Video（<90s） | 6.00% | ✅ **video-post（新增）** |
| Poll | 4.20% | ✅ poll-post |
| Long-Form Article | 中低 | ❌ 不覆盖（搜索需求极低） |
| Newsletter | 150% YoY 增长 | ✅ **newsletter-content（新增）** |
| Event + LinkedIn Live | 事件驱动 | ✅ event-promotion |
| Reshare / Repost | 浮动 | ❌ 不覆盖（非生成器场景） |
| **跨平台转制** | — | ✅ **5 个转制 topic（新增）**：TikTok / YouTube / X / URL / Blog → LinkedIn |

> 跨平台转制覆盖的不是 LinkedIn 原生格式，而是**内容来源维度**——解决「我的内容在别处，如何变成 LinkedIn 帖」的完整场景。

---

## 4. B2B 场景集群映射

以下场景型关键词集群用于 Blog/资源长文规划，与 topic 子页互补：

| 梯队 | 场景关键词簇 | 对应 topic | 内容建议 |
|------|-------------|-----------|----------|
| T1 | b2b linkedin post / content | — | 漏斗阶段 × 帖子类型矩阵 |
| T1 | storytelling on linkedin | #9 storytelling-post | 叙事弧结构 + 禁忌 |
| T1 | linkedin video content | #21 video-post | 视频帖结构/时长/字幕最佳实践 |
| T1–T2 | thought leadership linkedin post | #10 thought-leadership, #25 contrarian-post | 观点帖 vs 挑战帖结构对比 |
| T2 | case study / customer success | #2 case-study | 字段化骨架 + 合规引述 |
| T2 | data-driven linkedin content | #23 data-driven-post | 数据可视化 + 叙事技巧 |
| T2 | company page post / best practices | — | 主页语气、频次、员工协同 |
| T2 | hiring post / job announcement | #5 hiring-post | 短结构 + 文化亮点 |
| T2 | linkedin newsletter strategy | #22 newsletter-content | 通讯内容规划/选题/订阅增长 |
| T2 | linkedin lead generation | #24 lead-generation | 非硬广获客话术 + CTA 设计 |
| T2–T3 | post for founders / consultants / marketers | — | 每角色 1 篇或合集 |
| T3 | executive / ceo linkedin post | — | 高管语气 + 代笔与审批 |
| T3 | saas / b2b saas linkedin post | — | ICP 语言 + 产品帖 vs 洞察帖 |
| T3 | product launch / company milestone | #13 product-launch, #12 milestone-post | 发布公式 + 多版本 |
| T3 | career transition / new role | #26 career-transition | 转型叙事 + 新身份建立 |
| T3–T4 | social selling post | — | 非硬广话术 + DM 边界 |
| T4 | client testimonial / win story | #8 recommendation, #2 case-study | 与 case study 簇互链 |
| T4 | team appreciation / culture | #27 team-appreciation | 雇主品牌 + 招聘联动 |
| T1–T2 | content repurposing / cross-platform | CP-2 tiktok, CP-3 youtube, CP-4 tweet, CP-5 url | 多平台内容工作流 + 各平台→LinkedIn 改写最佳实践 |
| T2 | video content → linkedin | CP-2 tiktok, CP-3 youtube | 视频→文本帖的叙事转换 + 关键帧提取 |
| T3 | twitter/x → linkedin | CP-4 tweet-to-linkedin-post | Thread→Carousel、短文→长文结构转换 |

**集群维护**：canonical 支柱文之间交叉内链；每篇至少一处指向 `/linkedin-post-generator/` hub。

---

## 5. 搜索量数据口径

- 上表 §2 各 topic 的搜索量、KD 估算以 [dynal-pg-keywords.md](./dynal-pg-keywords.md) 为权威。
- **B2B 场景集群**（§4 上表）的关键词种子见 [dynal-pg-keywords.md](./dynal-pg-keywords.md) §2。
- 须用 Semrush/Ahrefs 统一拉取后，按 Volume 重排 §4 梯队顺序。

---

## 6. 战略价值：独占品类认知

目前竞品（Taplio、MagicPost、ContentIn、Copy.ai、Grammarly）**没有一家**有独立的 topic 子页矩阵。Taplio 最多做了 Hook Checker 子路径。35 个 topic 页（30 帖型 + 5 转制）不只是 SEO 长尾矩阵——它是 Dynal 在 PG 赛道的**独占品类认知**：

- **帖型维度**：当用户搜索 "linkedin newsletter post generator" 或 "linkedin contrarian post examples" 时，只有 Dynal 有专门落地页承接。
- **转制维度**：当用户搜索 "youtube to linkedin post generator" 或 "tiktok to linkedin post" 时，同样只有 Dynal 有独立 topic 页——竞品的 repurposing 均为附属功能，无独立 URL。

这反向强化了「AI LinkedIn agent」的叙事：不是一个通用生成器，而是**理解每种帖型场景、每条内容来源的专业代理**。

---

## 7. 维护

- **新增 topic 上线后**：同步更新本文 §1 状态列 + sitemap 收录信息（参考 [../dynal-site-structure.md](../dynal-site-structure.md)）。
- **搜索量变化**：以 [dynal-pg-keywords.md](./dynal-pg-keywords.md) 为引用源；更新关键词数据后复核本文 §2 优先级。
- **竞品新增独立 topic 页**：同步更新 [dynal-pg-competitors.md](./dynal-pg-competitors.md) §3 URL 样本。
- **格式覆盖率**：LinkedIn 平台新增格式时复核 §3 并评估是否需要新增 topic。