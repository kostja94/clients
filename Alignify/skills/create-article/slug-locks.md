# Slug 锁定说明（唯一 SSOT）

> **内容**：各 slug 的 **slug / 路由 / 主称 / 标题 / 内容边界 / 内链 / 结构 / JSON 侧车** 锁定——Marketing（`creator-program` · `creator-challenge-program` · `egc-marketing` · `marketing-types`）见 **Part A**，SEO（`submit-website`）见 **Part B**。
> **本文件来源**：由原 `marketing-slug-locks` 与 `seo-slug-locks` 合并而来（**2026-09-09**），分 **Part A — Marketing slug 锁定** 与 **Part B — SEO slug 锁定**。
> **适用（User 确认边界）**：Step 01–10 全文重写 / 增量维护任一下列 slug 时**强制**对照本文件对应 Part 分节。
> **SSOT 优先级**：Brief `**SSOT**` 绝对路径 > 本文件 > `knowledge/marketing/{slug}.md` · `knowledge/seo/{slug}.md` 指针块。

---

## Part A — Marketing slug 锁定

> **内容**：各 Marketing 专文（`creator-program` · `creator-challenge-program` · `egc-marketing` · `marketing-types`）的 **slug / 路由 / 主称 / 内容边界 / 内链 / JSON 侧车** 锁定。
> **适用**：Step 01–10 全文重写 / 增量维护下列任一 slug 时**强制**对照本文对应分节。
> **SSOT 优先级**：Brief `**SSOT**` 绝对路径 > 本文件 > `knowledge/marketing/{slug}.md` 指针块。

---

### creator-program

> **Brief SSOT**: [`knowledge/marketing/_briefs/creator-program.md`](../../knowledge/marketing/_briefs/creator-program.md)  
> **适用**: Step 01–10 全文重写 / 增量维护本 slug 时**强制**对照

---

#### 路由与 Meta

| 项 | 值 |
|----|-----|
| slug | `creator-program` |
| 路由 | **存量** `/marketing/creator-program`（ZH `/zh/marketing/…`）· **禁止**迁 `/blog/` |
| OG | **不更换** · `data/og-briefs/marketing/creator-program/brief.json` |
| publishDate | **永不改**（2024-12-03）；内容大改只更新 `modifiedDate` |

---

#### 中文主称与标题

| 允许 | 禁止 |
|------|------|
| **创作者计划**（狭义 · 长期策展共创） | **Creator Ambassador Program** 作同义词（Ambassador = 社区组织 · 见 Cursor/Claude） |
| 如何用创作者计划为 AI 产品做长期内容共创 | 泛称「创作者营销」吞没 Affiliate/UGC/Challenge |
| EN: Creator Program · Creative Partner Program (CPP) · Creators Club | EN H1 含 "Guide" |

---

#### 内容边界（User locked · 2026-08-28）

##### 狭义 Program 定义（canonical）

- **长期** · **申请/邀请/作品集审核** · **主激励 = access + 放大 + 路线图反馈**
- 创作者须**基于真实使用**产出教程 / workflow / 对比
- 周期 **月–年** · 无单次 deadline

##### 明确不属于本文（硬排除 · 各写各 brief）

| 概念 | 归 |
|------|-----|
| Affiliate / Creator Affiliate | `marketing/affiliate` |
| Referral / invite credits | `marketing/referral-program` |
| Creator Challenge | `marketing/creator-challenge-program` |
| 矩阵 UGC / Earn / 按条买量 | `blog/ugc-marketing` |
| Ambassador（meetup / 论坛） | 待建专文 · 正文仅 1 句对照 |
| Creator Grant（Suno Spark 等） | 脚注 · 非 CPP |
| Creator Commerce / Marketplace 分成 | 独立小节 · 非 CPP 主定义 |

##### 相邻专题 — 禁止「GTM 族」框架

- 与 Challenge、UGC、Affiliate 等**目录相邻** · **不是**「同一 GTM 族的不同载体」
- **禁止**开篇或独立 H2 画五篇合一的「GTM 大地图」
- 对照：**引用各文已有定义** + 必要时 1 表 · 表后 ≥2 句 prose

##### 案例 — 仅海外 · Tier 0 Program 页

| 收录 | 排除 |
|------|------|
| Ideogram Creators Club · Runway CPP · Luma CPP · Higgsfield CPP · Kling · Leonardo LCP（标注 on hold） | ElevenLabs/Gamma/CapCut **Affiliate** |
| Marketplace：Notion / Framer / Webflow（**Creator Commerce 小节**） | Higgsfield **Earn** · Picsart Earn |
| Civitai 付费创作者（直付型 · 1 行） | Galaxy.ai · Viggle · TryParrotAI 等未审计存量行 |

**维护**: 准入/on-hold 以官方 live 页为准 · 正文不写会过期的 cohort deadline

##### Optional sections

| 节 | 决策 |
|----|------|
| TL;DR md | 省略（JSON 侧车 **重写**） |
| FAQ md | 省略（`faq-data.json` 7 问 **改写**） |
| References md / JSON | 省略 |
| `#author-take` | **采用** — Kostja Program 评估经验 |
| go/no-go | **采用** |
| 三问判定 | **采用**（KB §1.2） |

---

#### 内链（C 项目运营型）

| 段落 | 目标 slug |
|------|-----------|
| vs Challenge / 漏斗 | `marketing/creator-challenge-program` |
| vs 矩阵 UGC / Earn | `blog/ugc-marketing` |
| vs Affiliate（附带通道） | `marketing/affiliate` |
| vs Referral | `marketing/referral-program` |
| Hub / 选型 | `marketing/marketing-types` |
| vs 单次红人采买 | `marketing/influencer` |

目标：**4–5 distinct 出链** · 段 ≤1 链 · EN/ZH 同构 · 修复存量零出链孤岛

---

#### Step 08 JSON 侧车

| 文件 | 键 | 动作 |
|------|-----|------|
| `tldr-data.json` | `/marketing/creator-program` · `/zh/marketing/creator-program` | **重写** introduction + 5 items |
| `faq-data.json` | 同上 | **改写** 7 问（增边界分流） |
| `references-data.json` | 同上 | **删除键**（若 Brief 省略 References） |

---

#### 发布后指标

**Primary**: EN `creator program AI` · `creative partner program`；ZH `创作者计划` · `AI 创作者计划` · `CPP`

**Secondary**: 与 `creator-challenge-program` / `ugc-marketing` 的选型长尾互不 cannibalize

---

### creator-challenge-program

> **Brief SSOT**: [`knowledge/marketing/_briefs/creator-challenge-program.md`](../../knowledge/marketing/_briefs/creator-challenge-program.md)  
> **适用**: Step 01–10 全文重写 / 增量维护本 slug 时**强制**对照

---

#### 路由与 Meta

| 项 | 值 |
|----|-----|
| slug | `creator-challenge-program` |
| 路由 | **存量** `/marketing/creator-challenge-program`（ZH `/zh/marketing/…`）· **禁止**迁 `/blog/` |
| OG | **不更换** · `data/og-briefs/marketing/creator-challenge-program/brief.json` |
| publishDate | **永不改**（2025-01-20）；内容大改只更新 `modifiedDate` |

---

#### 中文主称与标题

| 允许 | 禁止 |
|------|------|
| **创作者挑战赛**（语境：AI 产品的创作者挑战赛） | **AI 创作者** 作 H1/主称（语义不明） |
| 如何用创作者挑战赛为 AI 产品带来增长 | 泛称「创作竞赛：UGC 话题营销」作唯一标题 |

**EN 框架名**: Creator Challenge / creator contest（首段解释 Challenge · Festival · Clash 变体）

---

#### 内容边界（User locked · 2026-08-27）

##### 相邻专题 — 禁止「GTM 族」框架

- 与 `ugc-marketing`、`embedded-virality`、`watermark-growth`、`creator-program` 等**目录相邻**，**不是**「同一 GTM 族的不同载体」。
- 分工、对照表、内链：**引用各文已有定义**（例：矩阵 UGC = 品牌买内容；Challenge = 品牌办赛；Embedded = 默认 badge）。
- **禁止**开篇或独立 H2 画「GTM 组合拳地图」把多篇合成一族。

##### 案例与资源 — 仅海外 · evergreen

| 包含 | 排除 |
|------|------|
| Higgsfield、Runway、Artlist/AKOOL/Flova×Seedance、Koe、Suno、Civitai、OpenArt、CapCut CRE[AI]TE、Google AI Film Award、Luma、Chroma Awards、Melies、Curious Refuge、AdArena 等 | 抖音/B 站国内大赛、aitop100.cn、量子位等**作为国内案例主文** |
| 奖池量级、机制、平台绑定（无具体日历 deadline） | 正文写「2026-08-27 检索基准」「9/14 截止」等**会过期日期** |

**维护**: SSOT 个人知识库可写 live deadline；**站点正文**写 evergreen 机制 + 「以 Official Rules 为准」。

##### 案例呈现

- 保留 **6–8 个**海外 Tier 0 锚点 + **1 张精选速查表**（非 24 行巨表）。
- **落地页截图**：保留 **4–6 张**，`article-image-grid--2` 或 `--3`，每格 caption；禁止 9 格无差别堆叠。

##### Optional sections

| 节 | 决策 |
|----|------|
| TL;DR md | 省略（JSON 侧车保留） |
| FAQ md | 省略（`faq-data.json` 存量 7 问，改写对齐 v2） |
| References md / JSON | 省略 |
| `#author-take` | **采用** — Kostja 第一人称办赛/评估经验 |
| go/no-go | 采用（`marketing-strategy` §3.2） |

---

#### 内链（Batch 2）

| 段落 | 目标 slug |
|------|-----------|
| §什么是 / vs  adjacent | `blog/ugc-marketing` |
| vs Program | `marketing/creator-program` |
| watermark / badge | `blog/watermark-growth`、`blog/embedded-virality` |
| 赛后 → ambassador | `marketing/affiliate` |

目标：**4–5 distinct 出链** · 段 ≤1 链 · EN/ZH 同构。

---

#### 发布后指标

**Primary**: 品牌词排名 — EN `creator challenge AI` / `AI creator contest`；ZH `创作者挑战赛` / `AI 产品 创作 竞赛`。

---

*User 锁定项变更时同步更新本文件与 `_briefs/creator-challenge-program.md`。*

---

### egc-marketing

> **Brief SSOT**: [`knowledge/marketing/_briefs/egc-marketing.md`](../../knowledge/marketing/_briefs/egc-marketing.md)  
> **素材 SSOT**: `E:\个人知识库\增长策略-Growth\渠道分发-Distribution\员工发声-AI-DevTools-EGC.md`

---

#### 路由与 Meta

| 项 | 值 |
|----|-----|
| slug | `egc-marketing` |
| 路由 | **新文** `/blog/egc-marketing`（ZH `/zh/blog/egc-marketing`）· `content/blog/` |
| OG | **新生成** · `data/og-briefs/blog/egc-marketing/brief.json` |
| publishDate | Step 08 当日（`next-publish-date.mjs --check`） |

---

#### 中文主称与标题

| 允许 | 禁止 |
|------|------|
| **员工原创内容**（EGC） | 把 Employee Advocacy 与 EGC 混为一谈 |
| 标题 A：如何用员工原创内容（EGC）为 AI/DevTools 建立开发者信任（2026） | SSOT 文件名直译作 H1 |
| 员工发声（口语副称） | 国内平台案例作主文 |

**EN 框架名**: Employee Generated Content (EGC) · Employee-led marketing · split from employee advocacy (resharing)

---

#### 内容边界

##### 相邻专题 — 禁止「GTM 族」

- 与 `ugc-marketing`（外购创作者）、`creator-challenge-program`（办赛）、`rate-limit-reset`（reset 商业策略 vs **谁来说**）、`x-formerly-twitter`（平台算法 vs **组织 GTM**）**目录相邻，不是一族**。
- 内链引用各文已有定义；**禁止** GTM 组合拳大地图。

##### 案例 — 非创始人 · 海外 · evergreen

| 包含 | 排除 |
|------|------|
| Tibo、Rohan、Boris、Michele/Matt、Tom/Mingjie 等 | 创始人主案例（Amjad/Truell/Scott Wu 仅对照 1 段） |
| Tier 1 转引（BI/TC）作事实锚 | 国内平台、会过期 deadline 写进正文 |

##### 案例呈现 — react-tweet live embed（方案 A）

- 部署仓已接入 **`react-tweet`**：`src/components/TweetEmbed.tsx` + MD 管道 `<!-- block:tweet -->` / `<!-- tweet-id:STATUS_ID -->`。
- 案例节嵌入 2–4 条公开 X status；Boris 主战场 LinkedIn 仍以 prose + Tier 1 来源链呈现。
- Tweet ID 清单见 Brief **Tweet embed manifest**。

##### Author POV

- Kostja 判断**融入** `#org-playbook`（Signature Voice 选型、ghostwriter 节奏）。
- **无**独立 `#author-take` H2。

##### 表格与段落

- 所有表 **`childrenHtml`**；长文**段落为主**，禁止 GFM 表 / bullet 堆叠。

---

#### 内链（Batch 4）

**出链**: ugc-marketing, creator-challenge-program, rate-limit-reset, x-formerly-twitter, marketing-types, influencer 或 creator-program  
**入链回写**: rate-limit-reset, ugc-marketing, x-formerly-twitter, marketing-types（各 ≤1）

---

### marketing-types

> **Brief**: [`knowledge/marketing/_briefs/marketing-types.md`](../../knowledge/marketing/_briefs/marketing-types.md)

---

#### 路由 · Meta · OG

| 项 | 值 |
|----|-----|
| slug | `marketing-types` |
| 路由 | **存量** `/marketing/marketing-types` |
| OG | **不更换** |
| publishDate | **2026-02-12 不改**；大改只更 `modifiedDate` |
| **ZH title** | 如何用营销类型框架为 AI 产品选 GTM 路线（2026） |
| **EN title** | How to Choose GTM Routes for AI Products: Marketing Types Framework (2026) |

---

#### 页面角色

**Hub 索引** — 四维 taxonomy + 阶段选型 + 链到已上线专文；**不是** 14 类 Program 百科。

| 维度 | 正文要求 |
|------|----------|
| **Motion** | 独立 H2；与阶段矩阵联动 |
| **Channel** | Creation/Capture/Acceleration 角色表 + 渠道清单表；**无** 11 渠道 H3 |
| **Platform** | 平台族表；**仅 global** |
| **Program** | Partner 6 + Creator 5 + Lifecycle 三表 + 5 prose 节 |
| **七类映射** | 独立 H2；表无链或链仅在下文 prose；**只链已上线** |

---

#### 硬约束

- **禁止**「同一 GTM 族」式合并框架；专文**分工见各文**
- **Referral 先于 Affiliate** 写进启动序列
- **Creator Challenge** = Creator 子形态；链 `creator-challenge-program`，不与 Program 混 KPI
- **创业公司计划** 须拆：Cloud Credits vs Early Adopter / Startup Tier
- 表内**无链**（Hub 同 creator-challenge 规则）；段 ≤1 链

---

#### Hub 出链（Batch 3）

| 段落 | 目标 |
|------|------|
| Channel / SEO | keyword-research |
| Platform / LLM | geo |
| Program / 定价 | pricing-strategy |
| Program / Creator | creator-program, ugc-marketing, creator-challenge-program |
| Referral vs Affiliate | referral-program, affiliate |
| Lifecycle | lifetime-deal, embedded-virality |

**入链**：creator-challenge、ugc、geo、pricing 等 Hub 引用节回链本页（锚文本「营销类型选型」类）。

---

*2026-08-27 User 锁定*

---

## Part B — SEO slug 锁定

> **内容**：存量 `/seo/{slug}` 或新文 `/blog/{slug}` 的**边界、去重、Brief 锁定**；成文流程仍走 [`SKILL.md`](SKILL.md)。
> **SSOT 优先级**：Brief `**SSOT**` 绝对路径 > 本文件 > `knowledge/seo/{slug}.md` 指针块。

| slug | Skills | Brief | 外部 SSOT |
|------|--------|-------|-----------|
| `submit-website` | [本文件 §submit-website](#submit-website) | [`knowledge/seo/_briefs/submit-website.md`](../../knowledge/seo/_briefs/submit-website.md) | Submit-Website + Platform-Properties（**单篇合并**） |

**姊妹去重**：不重复 `how-search-engine-works` 三阶段长文、`website-indexing` 排查、`search-engine` 全球引擎地图。

---

### submit-website

> **Brief SSOT**: [`knowledge/seo/_briefs/submit-website.md`](../../knowledge/seo/_briefs/submit-website.md)  
> **素材 SSOT（双源）**:  
> - `E:\个人知识库\数据分析-Analytics\GSC\网站提交与验证-GSC-Submit-Website.md`  
> - `E:\个人知识库\数据分析-Analytics\GSC\社媒平台属性-GSC-Platform-Properties.md`  
> **User 确认（2026-09-01）**: **不拆文**；Website + Platform 均在本文完整覆盖。

---

#### 路由与 Meta

| 项 | 值 |
|----|-----|
| slug | `submit-website` |
| 路由 | **存量** `/seo/submit-website` · `/zh/seo/submit-website` · `content/seo/{en,zh}/submit-website.md`（**不重迁 URL**） |
| articleType | `seo-guide` |
| OG | 沿用 [`data/og-briefs/seo/submit-website/brief.json`](../../data/og-briefs/seo/submit-website/brief.json) · 重构后 **复核**：副视觉可增「Website + Platform 双 property 类型」示意 |
| publishDate | **保留** `2025-02-13` |
| modifiedDate | Step 08 重构完成日 |

---

#### 中文主称与标题

| 允许 | 禁止 |
|------|------|
| **向 Google Search Console 提交网站与社媒账号** | 把「提交」写成「保证收录/排名」 |
| 副轴：**Website 验证 · Platform OAuth · 站点地图 · Bing 并行** | 把 Platform 数据解释成 TikTok/IG 站内流量 |
| EN: *Submit to Google Search Console: Websites, Social Accounts & Bing* | 把 IndexNow 写成 Google 官方能力 |
| Platform properties 作 **2026 增量 H2**（非另文） | 另开 slug `gsc-platform-properties` |

**读者任务**：  
- 有网站 → Domain/URL-prefix 选型 → 验证 → sitemap / URL Inspection → Bing Import  
- 有 IG/TikTok/X/YouTube → Platform OAuth → 读 Google Search/Discover 表现  

---

#### 内容边界（SSOT 分工）

##### 本文 SSOT（必须写深）

**Website property（Submit-Website KB）**

1. Property 类型 — Domain vs URL-prefix；拆几个 = 几套 token  
2. 验证方法表 — DNS / HTML / meta / GA/GTM；Tag vs 文件 redirect  
3. 验证后 — Sitemap、URL Inspection、等待预期  
4. Bing 并行 — GSC Import vs 独立；IndexNow 仅 Bing  
5. 反模式 — 提交≠收录、删 token、共用 token、只做 GSC  

**Platform property（Platform-Properties KB · 2026-07）**

6. 四平台支持表 — IG / TikTok / X / YouTube；明确 ❌ LinkedIn 等  
7. OAuth 添加与授权维护 — 无 DNS/sitemap/Request indexing  
8. 报告口径 — Performance / Insights；Google 面 vs 平台内  
9. 限制 — 无 API、无历史回填、每账号一 property  
10. 易混三分 — Website vs Platform vs Search profile  

##### 出站（≤1 段 + 内链，禁止长复写）

| 主题 | 链到 |
|------|------|
| 三阶段原理 | `/seo/how-search-engine-works` |
| 全球站长工具 | `/seo/search-engine` `#seo-stack-by-market` |
| 索引排查 | `/seo/website-indexing` |
| Sitemap 技术 | `/seo/sitemap` |
| IndexNow / Indexing API | `skills/ops/indexnow.md` · `skills/ops/google-indexing.md` |
| Gen AI 报告 | Platform-Updates 姊妹（若已上线） |

##### Moat（单篇整合）

- Website：**决策树 + 两串 meta 示例 + Bing Import 5 分钟并行**  
- Platform：**2026 四平台 + 测量边界表 + vs Search profile**  
- 统一：**GSC property 类型三分法**（Domain / URL-prefix / Platform）

---

#### 结构锁定（Planned H2 · 单篇完整版）

| # | H2 / 锚点 | 目标 | KB |
|---|-----------|------|-----|
| 1 | `#submit-vs-index` | BLUF：Add property = 监控通道，≠ 收录 | Submit §9 |
| 2 | `#gsc-property-overview` | **三分法**总览表：Website Domain / URL-prefix / Platform | 两 KB §3 |
| 3 | `#website-property-types` | Domain vs URL-prefix 主表 + 覆盖粒度 | Submit §3 |
| 4 | `#choose-website-property` | 决策树 + 多 property 场景 + meta 示例 | Submit §3.3–3.4 |
| 5 | `#verify-website-ownership` | 流程 + 验证方法 SSOT 表 | Submit §4–5 |
| 6 | `#after-website-verification` | Sitemap · URL Inspection · 等待 | Submit §6 |
| 7 | `#platform-properties` | 2026 宣布 · 四平台 · OAuth 步骤 | Platform §3–4 |
| 8 | `#platform-reports-and-limits` | 报告口径 · 测量边界 · 无 API/无回填 | Platform §5–7 |
| 9 | `#property-boundaries` | Website vs Platform vs Search profile | Platform §9 |
| 10 | `#bing-parallel` | GSC Import · GSC vs BWT | Submit §7 |
| 11 | `#anti-patterns` | 两 KB 反模式合并 | Submit §9 · Platform §8 |
| 12 | `#conclusion` | 收束 | — |

**Optional JSON**：TL;DR ✅（含 Platform 一句）· FAQ ✅（7 问，**必含** Website/Platform 区分 + OAuth + Bing Import）· References ✅

** deliberate 省略**：全球引擎 encyclopedia · 三阶段长文 · IndexNow/API runbook · 站点结构/更新频率长节

---

#### 内链（seo-guide · 本文锁定）

**全文 distinct 站内链 ≤4**（含结论；FAQ 若链则计入）：

| slug | 出现位置 | 理由 |
|------|----------|------|
| `how-search-engine-works` | `#submit-vs-index` 首段 | 提交 vs 三阶段，一次即可 |
| `website-indexing` | `#submit-vs-index` 第二段 | 未收录排查下游 |
| `checklist` | `#conclusion` | 验证前收束 |

**禁止**为凑数链：`search-engine`、`sitemap`、`internal-links`、`learn-seo`（与本文任务无关或分散阅读）。

#### 段落（presentation.md · 本篇强制）

- 每个 major H2 **首段 ≥3 句** prose BLUF  
- **禁止** `**第一步**` / `**Step 1**` 伪列表短段链  
- `#anti-patterns` 用 **2 段长 prose**，禁止 bold 单句 × N  
- 表前末句自然引出「见下表」；表后 **≥2 句** 展开

---

#### 表格与段落

- Property 三分、验证方法、Platform 支持/测量边界、GSC vs BWT → **`childrenHtml` 表**
- `#platform-properties` 与 `#verify-website-ownership` 之间用 1 段桥接：「无自有网站也可添加 Platform property，与 Website **并行**、数据独立」

---

#### Author POV

- 融入 `#choose-website-property`（DNS → 1× Domain）或 `#platform-properties`（创作者应并行加 Website + Platform，若两者皆有）
- **无**独立 `#author-take` H2

---

*本文件由原 `marketing-slug-locks`（Part A）与 `seo-slug-locks`（Part B）合并而来，合并日期：2026-09-09。*
