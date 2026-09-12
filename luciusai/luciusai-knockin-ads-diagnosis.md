# Knockin 品牌词广告 0 展示 — 问题诊断与解决

> **项目**：Lucius AI → Knockin（会聊天的 AI 名片）
> **落地页**：https://luciusai.com/knockin
> **问题**：Google Search 品牌词广告发布后持续 0 展示 / 0 点击 / 0 花费
> **创建**：2026-09-10 | 结论基于公开信息 + Google 官方文档推断，实时数据需在 Google Ads 后台验证

---

## 1. 问题描述

### 1.1 现象

品牌词广告 Campaign 一切"看起来正常"，但发布后展示量、点击量、花费**始终为 0**。

### 1.2 当时配置

| 项 | 值 |
|----|----|
| Campaign | Knockin \| Brand Search \| Global |
| 状态 | Enabled / Eligible，广告已通过审核 |
| 投放网络 | 仅 Google Search |
| 地区 | All countries and territories |
| 语言 | 英语、简体中文、繁体中文 |
| 落地页 | https://luciusai.com/knockin |
| 出价策略 | Target Impression Share |
| 展示位置 | Absolute top of results page（结果页第 1 位） |
| 目标展示份额 | 95% |
| Maximum CPC | $3（从 $1 → $2 → $3 逐步上调） |
| 每日预算 | $3 |
| 付款 | 已绑定有效 Mastercard，Postpay，无欠费/失败 |
| 关键词（全部完全匹配） | `[knockin]` `[knockin ai]` `[knockin app]` `[knockin card]` `[knockin business card]` `[knockin official]` `[knockin official website]` |

### 1.3 Ad Preview & Diagnosis 的表现

- 系统能匹配到 `[knockin]`；
- 曾提示 "Your ad has a low Ad Rank for this search"；
- 上调 CPC 后，时而显示 "We don't know why your ads aren't showing"、时而又提示没匹配到关键词；
- 英语/简中、桌面/移动端测试均不展示。

### 1.4 已排除的因素

- ✅ 商标封禁：查证 "knockin" 无统一强商标（仅头饰/苹果酒/音乐制品等零散申请）。
- ✅ 付款/审核：账户状态正常，符合 "Eligible"。
- ✅ 落地页：`luciusai.com/knockin` 正常返回，含品牌名与产品内容。

---

## 2. 原因分析（按重要性排序）

### 根因 1：关键词 "knockin" 搜索意图严重错配 ⭐ 最关键

"knockin" 在真实搜索世界被三股完全无关的流量占据：

| 真实含义 | 类型 |
|---------|------|
| **Knockin** 英国 Shropshire 的一个村庄/教区（knockin.parish.uk） | 导航/地理 |
| **Gene knock-in** 基因敲入技术（分子生物学，学术界高频） | 信息 |
| **"Knockin' on Heaven's Door"** Bob Dylan 原唱 / Guns N' Roses 翻唱名曲 | 娱乐 |

而落地页是一个「AI 名片 / 个人 AI 简介」产品。**搜索 "knockin" 的用户意图与产品相关性趋近于零**，Google 因此给出极低的质量得分（Ad Rank 低 → 不展示）。

这直接解释了 Ad Preview 里三个互相矛盾的现象：

- 「low Ad Rank」→ 落地页与词相关性太低；
- 「don't know why」→ 低质量得分 + 低搜索量并存；
- 「no keyword matched」→ 完全匹配 + 该地区/语言下搜索量过低，无法触发。

**与钱无关**，所以 CPC 从 $1 调到 $3 无任何变化——本质不是出价不够，而是 Google 认为这个词不该展示。

### 根因 2：真实搜索量极低，且被稀释

- Keyword Planner 的「100–1K/月」是美国 + 全部意图的宽泛估算，区间本身不确定；
- 其中 99% 是搜村庄/基因/歌曲的，**真正搜产品的量趋近于 0**；
- 「全球 + 三语言」把本就稀少的搜索机会进一步稀释到每个地区-语言组合。

即使配置 100% 正确，0 展示持续数天在统计上也成立。

### 根因 3：出价策略组合自相矛盾

同时设定了：

- **最激进的投放目标**：Absolute top + 目标份额 95%；
- **最保守的预算帽**：Max CPC $3 + 日预算 $3。

对低质量得分的词，Google 需要出很高的价才能挤进绝对顶部；$3 的 cap 达不到 → Google 宁可完全不投。Google 官方文档明确警告：*"It's important not to set this limit (Max CPC) too low. Otherwise it can restrict the bids set by the strategy and prevent you from reaching your impression share goal."*

### 根因 4：新账户学习期 + 频繁改价

- Target Impression Share 需要 7–14 天学习期；
- 反复调 CPC（$1→$2→$3）会**反复重置学习期**，每次都让系统重新冷启动。

---

## 3. 解决方式

### 3.1 核心结论

> **停掉品牌词防御，改建非品牌词获取。** "knockin" 品牌认知度目前是 0，投品牌词 = 用 $3/天抢一个几乎不存在的需求。真正机会是把 knockin 推给那些正在搜「数字名片 / AI 名片 / AI 分身」的人。

knockin 的真实定位是「会聊天的 AI 名片」（把 bio 变成 AI 分身：访客提问 → 用你的语气回答 → 约会议 → 记住访客），更接近 Delphi.ai / Personal.ai 一路，而非传统数字名片（Popl/Blinq/HiHello）。

### 3.2 投放配置调整

| 项 | 原配置 | 建议改为 | 原因 |
|----|--------|---------|------|
| 出价策略 | Target Impression Share | `Maximize Clicks` 或 `Manual CPC` | 新账户无转化数据时 Google 官方推荐 |
| 展示位置 | Absolute top 95% | `Anywhere` 或 `Top` | 非品牌词竞争大，先求有展示 |
| 关键词匹配 | 完全匹配（保留） | 精确 + 短语，**禁用广泛匹配** | 广泛匹配会带入 "knockin" 无关流量 |
| 地区 | All countries | 先聚焦英语市场 | 落地页纯英文，多地区稀释预算 |
| 语言 | 英/简中/繁中 | 先只留 English | 繁中/简中质量分低 |

> 改完后 **3–7 天不要动任何设置**，给足学习期再观察。

### 3.3 可投放关键词清单（按优先级分层）

**第一梯队：AI 差异化词 ⭐ 最该投（低竞争 + 精准命中卖点）**

| 关键词 | 理由 |
|--------|------|
| `AI business card` | 品类 = AI 名片，精准描述"会聊天的名片" |
| `AI business card that replies` / `chatbot business card` | 命中"名片会说话"独家差异点 |
| `AI bio` / `AI profile` / `AI profile page` | 落地页 slogan "Your bio can finally answer back" 语义一致 |
| `personal AI chatbot` | 主品类词（内部已定 P0），有稳定搜索心智 |
| `AI clone` / `digital mind` / `AI digital twin` | Delphi 靠这些词占位 AI 助手；差异化在名片/B2B 场景 |

**第二梯队：品类词（有量但竞争大，需差异化文案）**

| 关键词 | 量级参考 | 备注 |
|--------|---------|------|
| `digital business card` | 竞品 Popl 品牌词 15.8K/月（$2.04 CPC），主词更大 | 文案强调"会聊天"差异化 |
| `NFC business card` | 强购买意图 | ⚠️ 意图不匹配（knockin 无 NFC 硬件），慎投 |
| `virtual business card` / `electronic business card` | 同义变体 | 可作短语补充 |

**第三梯队：场景/角色长尾词（高转化、量小但精准）**

- `AI business card for founders` / `for sales` / `for coaches` / `for freelancers`（落地页正好列这四类人群）
- `digital business card for realtors` / `for small business`（竞品已验证）
- `AI profile for founders`

**第四梯队：竞品截流词（蹭已有搜索心智）**

- `Popl alternative` / `Blinq alternative` / `HiHello alternative`（数字名片赛道被搜最多的对比词）
- `Delphi alternative`（AI 分身赛道）
- `BizCard alternative`（最直接的 AI 名片竞品，AI Clone Agent）

### 3.4 落地页按意图分组

| 搜索意图 | 落地页内容方向 |
|---------|--------------|
| `digital business card` / `Popl alternative` | 首屏对比"传统名片 vs 会聊天的 AI 名片" |
| `AI business card` / `personal AI chatbot` | 强调"上传资料 → 3 分钟生成会说话的名片" |

### 3.5 验证真实搜索量（坐实根因的实锤）

1. **Google Trends**（trends.google.com，免费免登录）：搜 `knockin` 看趋势是否几乎为 0、相关搜索是否全是村庄/基因/歌曲。
2. **Keyword Planner** 精确匹配：看 `knockin` 历史量是否"数据不足"或个位数。
3. 若坚持走 SEO 而非付费，先用 Google Search Console 看官网自然触达的词。

---

## 4. 数据参考（非 Google 官方精确值，仅方向性）

| 数据点 | 数值 | 来源 |
|--------|------|------|
| `popl` 品牌词月流量 / CPC | 15.8K / $2.04 | navtools.ai（第三方估算） |
| AI 工具类关键词中位 CPC（2026-05） | $4.55 | aitoolsbreakdown（53 词样本） |
| 高意图 AI 商业词 CPC 上限 | $23–32 | 同上（"best ai tools for business/marketing"） |
| "best digital business card" 类问题 | ChatGPT 端稳定被问，Popl/Blinq/Linq 抢排名 | aibrandtracker（KeywordEverywhere） |

⚠️ 具体词（`digital business card`、`AI business card` 等）的**精确月搜索量需在 Keyword Planner 查精确匹配验证**，不要直接引用第三方估算。

---

## 5. 一句话总结

问题真实存在，但不是"广告没展示"的技术故障，而是**投了一个搜索意图错配、真实搜索量趋近于零的关键词**。品牌词广告只有在用户真的会搜这个词时才有意义——而 "knockin" 目前还不是一个被大众用来搜这个产品的词。应把预算从"品牌词防御"转向"非品牌词获取"，主投 `AI business card`、`personal AI chatbot`、`AI bio`、`digital business card` 等词，用 Maximize Clicks 先跑出展示和数据，把 knockin 第一次推给需要它的人。

---

## 关联文档

- [luciusai-ai-business-card-research.md](./luciusai-ai-business-card-research.md) — AI 名片/数字名片赛道研究（竞品格局、品类拆解）
- [luciusai-personal-chatbot.md](./luciusai-personal-chatbot.md) — Personal Chatbot 产品定位与竞品（Delphi/Personal.ai/Popl）
- [luciusai-keywords.md](./luciusai-keywords.md) — 关键词策略总表
- [luciusai-growth-strategy.md](./luciusai-growth-strategy.md) — 增长策略
- [README.md](./README.md) — 文件索引
