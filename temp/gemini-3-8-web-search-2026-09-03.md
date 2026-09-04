# 深度搜索报告 — Google Gemini 3.8 Flash / 3.8 Flash Cyber（2026-09-02 发布）

> **检索基准日**：2026-09-03
> **时间范围**：发布前 90 天背景 + 发布后 24 小时增量（用户指定「这两天刚发布」）
> **检索约束**：按 web-deep-search-spec v1.4，未读取本地客户文档
> **Loop 轮次**：6 轮（R1 英文广度 ×2 批 → R1b 中文 → R2 时间线/背景 → R3 反响/独立评测 → R4 市场/人事 → 终轮交叉验证）
> **来源统计**：Tier 0 · 8 · Tier 1 · 10 · Tier 2 · 6
> **置信度摘要**：核心事实（发布、双变体、定价、可用渠道、官方 benchmark、Cyber 限流）均已由 Tier 0 + ≥2 Tier 1 互证「已确认」；独立第三方量化（Artificial Analysis Index、cost-per-task、Gray Swan 数字、Fairwind 参与方名单）为 Tier 1 单源或转述 AA，标「很可能（单源）」；3.5 Pro 延期与「Skimaki」代号属媒体口径，标「很可能」。

---

## 1. 执行摘要

Google DeepMind 于 **2026-09-02（美东周三）** 正式发布 **Gemini 3.8 Flash**（GA，通用 coding/agent 主力模型）与 **Gemini 3.8 Flash Cyber**（网络安全专用，仅限 Fairwind Program 可信防御方）。官方称其为「迄今最强推理与编程模型」，是 **六周内第三个 Flash**（3.6→3.7→3.8），距 3.7 Flash 仅三周（[官方博客 Tier 0](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)）。

3.8 Flash 延续 $0.75/1M 输入、$3.75/1M 输出的年底前引导价（2027-01-01 起翻倍至 $1.50/$7.50），1M token 上下文；官方自评 DeepSWE v1.1 达 **73.7%**，仅次 Claude Opus 5（74.0%），超 GPT-5.6 Sol（72.7%）与上代 3.7 Flash（65.3%）。关键机制是「works harder」——复杂任务执行更多推理步骤与工具调用，因此高思考档 token 消耗上升（独立平台 Artificial Analysis 测单任务成本 $0.58，较 3.7 的 $0.40 涨约 40%）。

Cyber 变体为本次最大新闻点：CyberGym 漏洞发现 86.2%，CWE-Bench 自动补丁 pass@1 47.2%（逼近最强前沿模型 47.8%），Google 自报 Chrome 正确补丁量 2.6 倍、内部 20 语言漏洞发现成功率 >70%、Cloud 团队 2 小时内挖出「critical foundational」漏洞。因对网安任务放宽安全缓解，仅向政府、关基运营方与软件维护者开放，走新发布的 **Fairwind Program** 申请制。

**最重要的增量信息**：这次发布无法脱离 Google 的战略叙事——**Gemini 3.5 Pro 据 Bloomberg 因 coding 不达标被无限期推迟**，DeepMind 于 8 月初换帅（Hassabis 转任 Alphabet 首席科学家、Kavukcuoglu 任 SVP 执掌 Gemini），Flash 高频迭代 + Cyber 走政府/企业路线被媒体解读为「用低成本打规模的补位策略」。WSJ 报道 3.8 Flash 内部代号 **"Skimaki"**，在 Google 内部编码工具 Jetski 头部对决中获工程师偏好。社区反响呈两极：HN 主帖 1006 分/567 评论，实测派（Simon Willison）给正面反馈，质疑派聚焦「frontier/Pro 缺席」与「单任务成本不降反升」，且 Artificial Analysis 智能指数榜上被 Kimi K3、GLM-5.3（同为 60）反超。资本市场反应平淡：发布日 GOOGL 仅 +0.63%，此前正处于 2015 年以来最长四个月连跌。

## 2. 搜索过程摘要

| 轮次 | 新增 query 示例 | 本轮增量发现 |
|------|----------------|--------------|
| R1 | `Gemini 3.8 Google DeepMind release announcement`；`Gemini 3.8 September 2026` | 官方发布文 + model card + SiliconANGLE 建立骨架：双变体、定价、CyberGym/CWE-Bench 初值 |
| R1 深读 | fetch blog.google 官方全文、SiliconANGLE 全文 | 官方全部 benchmark、works harder 机制、Fairwind 650+ 参与方与 CodeMender、Chrome 2.6x / Wiz / <2h 战果 |
| R1b | `Gemini 3.8 Flash 谷歌 发布`（中文） | 新浪财经、少数派跟进：中文口径聚焦「竞争重点从 chat 转向编程/企业工作流」|
| R2 | `Gemini 3.7 Flash release Aug 2026`；`Gemini 3.5 Pro delayed`；`Gemini 3.8 DeepSWE Opus Sol` | 时间线定锚：3.6（7/21）→3.7（8/13）→3.8（9/2）；3.5 Pro 延期背景（Bloomberg 口径）|
| R3 | `site:news.ycombinator.com Gemini 3.8`；fetch the-decoder 全文 | HN 主帖 1006 分/567 评论；AA Intelligence Index 59；cost-per-task $0.58 vs 3.7 $0.40；Gray Swan IPI 5.5%；竞品定价（Opus 5 $5/$25、Sol $4/$20）|
| R4 | `Alphabet stock Sep 2 2026`；`Koray Kavukcuoglu DeepMind` | CNBC：GOOGL +0.63%、四个月连跌背景；8/5 DeepMind 换帅（Reuters）；WSJ/Mint 确认 Skimaki 代号与 Jetski 内测 |
| 终轮 | HN JSON top comments 解析（文件损坏，改用搜索片段定性）；数值交叉核对 | 分歧项识别：DeepSWE 73.7 vs 74、6 周 vs 三个月口径、CyberGym 对比对象命名差异 |

## 3. 搜索意图拆解

| 意图 | 检索词示例 | 结果状态 |
|------|------------|----------|
| 概念基线三问：不适用（单一产品发布追踪，非概念/品类主题） | — | 不适用（按 §2.1.1「单一产品发布」豁免；改走事实/时间/产品轴）|
| 事实轴：发布主体/时间/型号 | `Gemini 3.8 release announcement` | 已覆盖（Tier 0 官方博客 + 3×Tier 1）|
| 产品轴：功能/限制/定价/上下文/知识截止 | `Gemini 3.8 Flash model card`、`llm-stats pricing` | 已覆盖（官方 model card + docs + T1）|
| 性能轴：官方 vs 独立 benchmark | `DeepSWE HLE-Verified Artificial Analysis` | 已覆盖（官方自评 + AA 独立指数）|
| 时间轴：3.6→3.7→3.8 节奏 | `Gemini 3.7 Flash release date` | 已覆盖（官方 8/13 博客 + T1）|
| 解读轴：为什么快发 Flash / Pro 缺席 | `Gemini 3.5 Pro delayed coding` | 已覆盖（Bloomberg 口径转述 + Ars/the-decoder 解读）|
| 反响轴：社区评价 | `site:news.ycombinator.com Gemini 3.8` | 已覆盖（HN 1006 分帖 + 对比分帖）|
| 风险轴：Cyber 双用/访问限制 | Fairwind 官方页 + the-decoder | 已覆盖（官方安全口径 + T1 解读）|
| 市场轴：发布日股价/行业压力 | `Alphabet stock Sep 2 2026` | 已覆盖（CNBC）|
| 中文轴：中文权威媒体口径 | `量子位 机器之心 Gemini 3.8`、新浪/少数派 | 部分覆盖（少数派 + 新浪财经；36氪/量子位未检索到专题稿 → 见 §7.7）|

## 4. 核心发现（多源验证）

### 4.1 发布概况：双变体、定价与可用性

| 结论 | 来源 A（Tier 0） | 来源 B/C（Tier 1） | 置信度 |
|------|----------------|-------------------|--------|
| 2026-09-02 发布 Gemini 3.8 Flash（GA）与 3.8 Flash Cyber，六周内第三个 Flash，距 3.7 Flash 三周 | [Google 官方博客](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) 09-02 | [Ars Technica](https://arstechnica.com/ai/2026/09/google-releases-gemini-3-8-flash-its-third-flash-model-in-six-weeks/)；[SiliconANGLE](https://siliconangle.com/2026/09/02/google-launches-two-gemini-3-8-models-with-cutting-edge-reasoning-capabilities/) | 已确认 |
| 引导价 $0.75/$3.75 每百万输入/输出 token，至 2026-12-31；2027-01-01 起 $1.50/$7.50 | 官方博客脚注 | [9to5Google](https://9to5google.com/2026/09/02/gemini-3-8-flash-launch/)；[the-decoder](https://the-decoder.com/gemini-3-8-flash-is-googles-third-budget-model-in-six-weeks-while-frontier-models-remain-mia/) | 已确认 |
| 1M token 上下文（输入 1,048,576 / 最大输出 65,536）；多模态输入、文本输出；思考档 low/medium/high（默认 medium）；model id `gemini-3.8-flash`（无 preview 后缀）| [官方 model card](https://deepmind.google/models/model-cards/gemini-3-8-flash/) | [llm-stats](https://llm-stats.com/models/gemini-3.8-flash)；少数派 | 已确认 |
| 知识截止 2026 年 3 月（部分域；另一些域沿用 Gemini 3 家族 2025 年 1 月基线）| 官方 model card | [9to5Google](https://9to5google.com/2026/09/02/gemini-3-8-flash-launch/) | 已确认 |
| 可用渠道：开发者 API/AI Studio/Android Studio/Antigravity/Stitch；企业 Gemini Enterprise；消费者 Gemini app + Search AI Mode + Google Sheets（AI Pro/Ultra 订阅）| 官方博客 | 9to5Google；少数派 | 已确认 |

叙述：这是官方「workhorse」（主力型）叙事的最新一档——强调以低成本档位逼近高价 frontier 模型，而非追求单点最大智能。官方明确 3.7 Flash **继续受支持**，供对 token 效率敏感的 workload 使用（官方博客）。

### 4.2 官方自评性能与「works harder」机制

| 结论 | 来源 A（Tier 0） | 来源 B/C（Tier 1） | 置信度 |
|------|----------------|-------------------|--------|
| DeepSWE v1.1（长周期软件工程）73.7%，超多数更大 frontier 模型 | [官方博客](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) | [the-decoder](https://the-decoder.com/gemini-3-8-flash-is-googles-third-budget-model-in-six-weeks-while-frontier-models-remain-mia/)（含对照：Opus 5 = 74.0、GPT-5.6 Sol = 72.7、3.7 Flash = 65.3）；[SiliconANGLE](https://siliconangle.com/2026/09/02/google-launches-two-gemini-3-8-models-with-cutting-edge-reasoning-capabilities/)（领先 Sol 约 1%、略逊 Opus）| 已确认（官方数值；对照经 T1 复核一致）|
| HLE-Verified 54.9%（STEM/人文/专业多步推理）| 官方博客 | 9to5Google、少数派 | 已确认 |
| 在 Vals Finance Agent V2、Harvey Legal Agent Benchmark 等金融/法律专业基准超 3.7 与 frontier 模型 | 官方博客 | 9to5Google | 已确认 |
| 16 项自评基准中 9 项超 Claude Opus 5 与 GPT-5.6 Sol；Terminal-Bench 1.1 等 coding 基准占优 | — | [SiliconANGLE](https://siliconangle.com/2026/09/02/google-launches-two-gemini-3-8-models-with-cutting-edge-reasoning-capabilities/)（转官方图）| 很可能（单源 T1，源自官方图）|
| 机制「works harder」：复杂任务执行额外推理步骤 + 迭代调用工具，高 effort 档 token 消耗更多 | 官方博客 | the-decoder（解读）、9to5Google | 已确认 |
| OSWorld-2.0（agentic computer use）较 3.7 有改进但仍明显落后 Claude Opus | — | [Ars Technica](https://arstechnica.com/ai/2026/09/google-releases-gemini-3-8-flash-its-third-flash-model-in-six-weeks/) | 很可能（单源 T1，官方未披露该维度）|

叙述：Ars 指出多数测试相对 3.7 仅是「marginal improvement」，编码类增益更大；3.8 之所以能登 DeepSWE 榜首，靠的是把 Flash 档做到 frontier 级编码 + 成本优势的组合，而非绝对能力登顶。SiliconANGLE 补充官方对外口径为「most intelligent Flash model」（Seeking Alpha 亦沿用）。

### 4.3 Gemini 3.8 Flash Cyber 与 Fairwind Program

| 结论 | 来源 A（Tier 0） | 来源 B/C（Tier 1） | 置信度 |
|------|----------------|-------------------|--------|
| Cyber 与通用版同底层、专攻漏洞发现与自动修复；缓解策略放宽，故仅限可信防御方 | [官方博客](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)；[Fairwind 官方页](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/) | 9to5Google（replacing 3.5 Flash Cyber）、Ars | 已确认 |
| CyberGym 漏洞发现 86.2%，超上代 3.5 Flash Cyber（77.5%）与更大型 frontier 模型 | 官方博客（超 3.5 与更大模型）| [the-decoder](https://the-decoder.com/gemini-3-8-flash-is-googles-third-budget-model-in-six-weeks-while-frontier-models-remain-mia/)（86.2 vs 77.5 vs GPT-5.6 Sol 83.6 vs GPT-5.5-Cyber 85.6）；[SiliconANGLE](https://siliconangle.com/2026/09/02/google-launches-two-gemini-3-8-models-with-cutting-edge-reasoning-capabilities/)（Claude Mythos 5 = 83.8、Sol = 83.6）| 已确认（86.2 官方口径；各对比对象随不同官方图口径不一，见 §8）|
| 内部 20 种编程语言综合漏洞基准成功率 >70% | 官方博客 | — | 已确认（官方自报内部指标）|
| CWE-Bench（Collinear 主办，外部补丁基准）pass@1 = 47.2%，处 Pareto 前沿，逼近最强前沿模型 47.8% | [官方博客](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)；[Fairwind 页](https://deepmind.google/fairwind-program/)（点名对比对象为 Fable 5 = 47.8）| the-decoder（「leading frontier model」47.8）| 已确认 |
| 内部战果：Chrome 正确补丁 2.6×；Wiz 内部渗透基准 recall +7.5–9.7% 且成本低 2.3–5.2×；Cloud 漏洞研究团队 <2 小时发现需数月工作量的 critical foundational 漏洞 | 官方博客 | 9to5Google、Ars、SiliconANGLE | 已确认（Tier 0 声明，多家 T1 复述）|
| 访问机制：Fairwind Program（新设）申请制，面向政府、关基运营方、软件维护者；配 CodeMender harness；≥650 参与方（含 Snowflake、CrowdStrike、Datadog）| [Fairwind 官方页](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/) | [SiliconANGLE](https://siliconangle.com/2026/09/02/google-launches-two-gemini-3-8-models-with-cutting-edge-reasoning-capabilities/)（650+ 及名单）| 650+ 及名单为很可能（单源 T1）；机制本身已确认 |
| 定位表述：防御优先（fix）而非进攻（exploitation）| 官方博客 | the-decoder | 已确认 |
| 支持 zero data retention（经 Gemini Enterprise Agent Platform managed model 提供）| [Fairwind 页](https://deepmind.google/fairwind-program/) | — | 已确认（官方 FAQ 口径）|

叙述：Cybersecurity 专用大模型 + 限量分发是本次发布媒体最大增量点（多数 T1 在导语强调「主流 AI 模型中尚属首次」）。官方刻意强调防御定位，避免双用争议；但放宽安全缓解的模型只发给政府与关基方，本身即构成新的治理讨论（见 §7.5）。

### 4.4 独立评测与第三方量化（增量）

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| Artificial Analysis Intelligence Index：3.8 Flash high=59 / medium=57 / low=52（3.7 Flash 为 56；GPT-5.6 Sol xhigh、Grok 4.6 medium 同为 59）| [Artificial Analysis 发布页](https://artificialanalysis.ai/models/releases/gemini-3-8-flash) | the-decoder | 很可能（第三方实测，T1 转述一致）|
| AA 智能榜第 8，被 Kimi K3（60）与 GLM-5.3（60）反超 | HN 对比帖（[item 49539315](https://news.ycombinator.com/item?id=49539315)，引 AA 截图）| — | 很可能（T2 转 AA；AA 官网链接随智能排行浮动）|
| cost-per-task：3.8 Flash $0.58/任务（其智能级 Pareto 最便宜），但较 3.7 Flash $0.40 上升约 40%（token 消耗↑所致）| the-decoder（引 AA）| — | 很可能（单源 T1）|
| high 档输出速度约 300 tokens/s、单任务约 2.5 分钟（low 档约 48 秒）| the-decoder（引 AA）| AA 官网（high 302 t/s）| 很可能 |
| Gray Swan IPI（提示注入）攻击成功率 5.5%：低于 DeepSeek V4 Pro 60.1%、Kimi K3 52.7%、Grok 4.6 51.8%；仅 Claude Opus 5（4.8%）更优 | the-decoder | 官方博客（定性「significant leap in prompt injection robustness as measured by Gray Swan」，无数值）| 很可能（数值单源 T1；官方定性佐证）|
| 竞品每 token 定价参照：Claude Opus 5 = $5/$25，GPT-5.6 Sol = $4/$20 | the-decoder | — | 很可能（单源 T1）|

叙述：第三方数据补全了官方通稿外的关键判断——「便宜但更费 token」使单任务成本实际抬升约四成，这解释了官方为何主动建议效率敏感场景留在 3.7 Flash；也解释了 HN 上「性价比是否真成立」的争论。另一方面 prompt-injection 韧性数字（Gray Swan 口径）是 3.8 系列相对竞品的一个真实卖点。

### 4.5 战略背景：3.5 Pro 缺席、DeepMind 换帅、市场语境

| 结论 | 来源 A | 来源 B/C | 置信度 |
|------|--------|---------|--------|
| Gemini 3.5 Pro（原 I/O 2026 预告、6 月目标）因 coding 未达内部标准被推迟，无确定日期；Google 发言人称多款模型在合作测试中 | Bloomberg（原始报道未直接访问）| [Wionews 转述](https://www.wionews.com/technology/google-delays-gemini-3-5-pro-after-ai-model-misses-coding-targets-report-says-1784276836487)、[winbuzzer 转述](https://winbuzzer.com/2026/07/20/google-reportedly-delays-gemini-35-pro-over-coding-issues-xcxwbn/)、Ars（「reportedly delayed」）| 很可能（T1 多家转述 Bloomberg 一致，无 Tier 0 反驳）|
| Google 自 2026 年初起未再发 frontier 级 Pro 模型，3.8 发布加剧「可能再无 3.5 Pro」的猜测 | Ars、the-decoder（「frontier models remain MIA」）| — | 观点（T1 解读，非事实）|
| 8/5 DeepMind 换帅：Hassabis 转任 GDM Chair + Alphabet Chief Scientist；Kavukcuoglu 任 SVP（director 级别）掌 Gemini 研发/app/开发者团队，直接汇报 Pichai；Jeff Dean 等多人离任 | [Pichai 内部信（官方）](https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/) | [Reuters/The Star](https://www.thestar.com.my/tech/tech-news/2026/08/06/google-shakes-up-ai-leadership-as-deepmind-chief-shifts-role) | 已确认 |
| 3.8 Flash 内部代号「Skimaki」，在 Google 内部编码平台 Jetski 的头部对局中获工程师偏好（胜过 Anthropic Opus）| [WSJ / Mint](https://www.livemint.com/global/new-google-ai-model-said-to-narrow-gap-on-coding-ability-11788341542644.html) 2026-09-02 | — | 很可能（单源 T1 WSJ）|
| 9/1（发布前日）WSJ 等预报「周三见」，GOOGL 常规时段跌约 1.3%、盘后转涨 0.6–0.7% | CNBC | 多家财经转述 | 已确认（方向）|
| 发布日 GOOGL 收 $337.12（+0.63%）；进入 9 月前处四个月连跌（2015 年以来最长），AI 落后 + DeepMind 重组 + 人才流失背景下以发布重建叙事 | [CNBC](https://www.cnbc.com/2026/09/02/google-starts-september-with-ai-momentum-after-long-losing-streak.html) | Seeking Alpha、tradevae | 已确认（CNBC）；伯克希尔 CEO Greg Abel 公开背书 Alphabet AI（CNBC 转述）|

叙述：三件事串成完整解读链——①编码短板 → 3.5 Pro 延期 → 战略资源向 Flash 倾斜；②8 月换帅后 3.7/3.8 是新产品导向节奏的产物；③面向企业/政府的 Cyber 变体与「经济价值型任务」定位，显示 Gemini 正把战场从聊天问答挪到编程与 agentic 商业化。这些均为媒体解读与转述，未见 Google 官方明说（§8 有标注）。

## 5. 时间线

| 日期 | 事件 | 来源（Tier）|
|------|------|-------------|
| 2025 初–2026 | Gemini 3 家族成型，多数模型知识基线部分域仍为 2025-01 | 官方 model card（T0）|
| 2026-05 | Google I/O 2026：Pichai 预告 Gemini 3.5 Pro「已内部使用」 | Bloomberg 转述（T1）|
| 2026-07 中 | Bloomberg：3.5 Pro 因 coding 未达内部标准被推迟（错过 6 月窗口）| Bloomberg→Wionews/winbuzzer（T1）|
| 2026-07-21 | Gemini 3.6 Flash + 3.5 Flash-Lite + 3.5 Flash Cyber 发布 | 官方博客 / HN（T0/T2）|
| 2026-08-05 | DeepMind 换帅：Hassabis → Chair/首席科学家，Kavukcuoglu → SVP；Jeff Dean 等离任 | Pichai 信（T0）/ Reuters（T1）|
| 2026-08-13 | Gemini 3.7 Flash GA（$0.75/$3.75 引导价，3.6 半价；Spark 接入）| 官方博客（T0）|
| 2026-09-01 | WSJ：3.8 Flash（代号 Skimaki）最快周三发布；GOOGL 常规时段跌约 1.3% | WSJ/Mint（T1）、CNBC（T1）|
| 2026-09-02 | **Gemini 3.8 Flash GA + 3.8 Flash Cyber + Fairwind Program 发布**；全渠道上线；GOOGL +0.63% 收 $337.12 | 官方博客（T0）、CNBC（T1）|
| 2026-09-02 | HN 主帖（id 49537553）1006 分 / 567 评论 | HN（T2）|
| 2026-09-03 | 中文媒体跟进（新浪财经专题、少数派早报）| 中文 T1 |

## 6. 实体关系

```
Alphabet
 └─ Google DeepMind（SVP Koray Kavukcuoglu 负责 Gemini 研发，2026-08 起）
     ├─ Gemini 3.8 Flash（GA，通用）→ API / AI Studio / Antigravity / Android Studio / Stitch
     │                                → Gemini Enterprise（企业）/ Gemini app + AI Mode + Sheets（消费，AI Pro/Ultra）
     └─ Gemini 3.8 Flash Cyber（受限）→ Fairwind Program（政府、关基、软件维护者，申请制）
                                          └─ CodeMender harness（DeepMind 出品）
      内部使用者：Chrome Security / Google Cloud Vulnerability Research
      外部背书者：Wiz、Palo Alto Networks、Armadin、Snowflake、CrowdStrike、Datadog 等
竞品（2026-09 语境）：
  OpenAI：GPT-5.6 Sol/Luna/Terra、GPT-5.5-Cyber   Anthropic：Claude Opus 5 / Sonnet 5 / Fable 5 / Mythos 5
  xAI：Grok 4.6   中国系：DeepSeek V4 Pro、Kimi K3、GLM-5.3、Qwen 3.x    推理加速：Cerebras
前代 Flash 线：3.5 Flash → 3.6 Flash（7/21）→ 3.7 Flash（8/13）→ 3.8 Flash（9/2）；Cyber 线：3.5 Flash Cyber → 3.8 Flash Cyber
```

## 7. 增量信息

### 7.0 增量对照表（多源 diff，相对 Tier 0 官方博客的新增点）

| 增量主张 | 相对 Tier 0 的新增点 | 首见来源（Tier）| 互证来源 | 验证结果 | 置信度 |
|---------|---------------------|-----------------|---------|---------|--------|
| 3.5 Pro 因 coding 未达标延期 | 官方博客未提；解释「为何只发 Flash」 | Bloomberg → Wionews（T1）| winbuzzer（T1）、Ars 复述 | 很可能（多源 T1 一致）| 很可能 |
| 3.8 Flash 代号 Skimaki、Jetski 内测偏好胜 Opus | 官方未披露代号 | WSJ/Mint（T1）| — | 很可能（单源 T1）| 很可能（单源，待确认）|
| 8/5 DeepMind 换帅是节奏背景 | 官方 3.8 文未关联人事 | Pichai 内部信（T0）| Reuters（T1）| 已确认（人事事实独立于发布文）| 已确认 |
| AA Intelligence Index 59（high）/57/52 | 官方不给独立综合指数 | AA 官网（T2-独立评测）| the-decoder（T1）| 很可能 | 很可能 |
| cost-per-task $0.58，较 3.7（$0.40）高约 40% | 官方仅提示「高 effort 更多 token」，未量化 | the-decoder（T1，引 AA）| — | 很可能（单源 T1）| 很可能（单源）|
| Gray Swan IPI 攻击成功率 5.5%、竞品对照 | 官方仅定性「显著提升」| the-decoder（T1）| 官方定性（T0）| 很可能（数值单源 T1）| 很可能（单源数值）|
| CyberGym 对比对象明细（3.5 Cyber 77.5、GPT-5.5-Cyber 85.6 等）| 官方仅称「超 3.5 与更大模型」| the-decoder（T1）| SiliconANGLE（T1，另一组对象）| 部分一致 → 并列见 §8 | 已确认主体 |
| Fairwind 参与方 ≥650、含 Snowflake/CrowdStrike/Datadog | 官方页未给数量 | SiliconANGLE（T1）| — | 很可能（单源 T1）| 很可能（单源）|
| CWE-Bench 对手点名为 Anthropic Fable 5（47.8%）| 官方博客写「leading frontier model」| Fairwind 页（T0，点名 Fable 5）| the-decoder（T1）| 已确认 | 已确认 |
| OSWorld-2.0 computer use 仍落后 Claude Opus | 官方未披露 | Ars（T1）| — | 很可能（单源 T1）| 很可能（单源）|
| 中文叙事：竞争重点从 chat 转向编程/企业工作流/经济价值 | 中文口径归纳 | 新浪财经（T1）| 少数派（T1）| 部分（观点归纳）| 观点 |

### 7.1 已验证增量信息

| 增量事实 | 来源 | 置信度 | 备注 |
|---------|------|--------|------|
| 3.5 Flash Cyber 为 3.8 Cyber 前代（7 月同批发布），CyberGym 77.5% | the-decoder（T1）| 很可能 | 单源给出数值 |
| 3.7 Flash DeepSWE v1.1 官方自评 65.3%（3.8 相对提升 8.4 个百分点）| datanorth/miraflow（T1）与 the-decoder 一致 | 已确认 | 多 T1 与官方 3.7 文一致 |
| CWE-Bench 对比对象 = Anthropic Fable 5（47.8%）| Fairwind 官方页 | 已确认 | Google 自列 |
| 3.8 Flash 引导价与 3.7 相同、仅为 3.6 引导价的一半 | 官方 3.7/3.8 博客 | 已确认 | |
| OSWorld computer use 为已知短板（官方未回应）| Ars（T1）| 很可能（单源）| |
| DeepMind 8/5 重组后 Gemini 已跨 950M 月活 | Pichai 内部信引 AIM/LinkedIn 摘要（T1）| 很可能 | 非 3.8 直接事实 |
| CNBC：Gemini 3.8 被官方定位为对抗「2015 年来最长四个月连跌」叙事的抓手 | CNBC（T1）| 已确认（事实为 CNBC 报道本身）| 市场解读类 |

### 7.2 未通过验证的传闻

| 传闻/主张 | 来源（Tier）| 拒绝原因 |
|----------|-------------|---------|
| 8 月 Business Insider 报道称 Google 员工在测内部「Gemini 3.x」build | shattered.io 转述（T2 聚合）| 无法访问 BI 原文、无独立互证；仅作线索不采信 |
| 「即将发布 Gemini 4」的具体时间窗口 | the-decoder（T1，评论性）| 属评论推测，非事实陈述 |
| Seek 数据显示发布日涨幅「1%」等 | 低质财经站（T2）| 与 CNBC 0.63% 收盘口径不一致；取 CNBC |

### 7.3 权威媒体解读

- **Ars Technica（Ryan Whitwam）**：Pro 模型线自 2026 年初暂停；「如果这些数字反映现实，连 Flash 都在跟市场领导者竞争」；同时点出 computer use 仍是 Google 短板、价格战是对竞品降价的回应。（[全文已深读](https://arstechnica.com/ai/2026/09/google-releases-gemini-3-8-flash-its-third-flash-model-in-six-weeks/)）
- **The Decoder（Matthias Bastian）**：直接以「第三个平价模型、frontier 仍 MIA」为题；核心论点是快速迭代既可是「实力」也可是「对 3.5 Pro/ Gemini 4 缺席的掩护」；引用新任 DeepMind 主管表态「不只在价格性能上竞争，也要在 raw capability 上领先」。（[全文已深读](https://the-decoder.com/gemini-3-8-flash-is-googles-third-budget-model-in-six-weeks-while-frontier-models-remain-mia/)）
- **WSJ（Erin Woo，经 Mint 转载）**：首发内部代号与 Jetski 偏好测试，称 3.8 Flash 是 Google 在「编码落后 OpenAI/Anthropic」领域的补救动作，发布时间与 9/2 完全吻合。（[链接](https://www.livemint.com/global/new-google-ai-model-said-to-narrow-gap-on-coding-ability-11788341542644.html)）
- **CNBC**：把发布放回投资语境——四个月连跌、AI 基建巨额投入、广告 14% 增长对冲、反垄断剥离 AdX 判决同周落地；伯克希尔 Greg Abel 公开背书。（[链接](https://www.cnbc.com/2026/09/02/google-starts-september-with-ai-momentum-after-long-losing-streak.html)）

### 7.4 社区与舆论反响（Tier 2，观点非事实）

HN 主帖 [Gemini 3.8 Flash and 3.8 Flash Cyber](https://news.ycombinator.com/item?id=49537553)（1006 分 / 567 评论，发布后约 17 小时）大致三种立场：

1. **实用实测派（少量正面）**：Simon Willison 用自己的开源 coding agent（llm-coding-agent）实测「做得很扎实」，并展示了模型生成的工具链产物。
2. **性价比质疑派（规模较大）**：围绕 AA 的 cost-per-task 展开论战——一方称 3.8「在几乎所有单任务成本基准上显著低于 GPT-5.6 Sol」；另一方反驳称 Sol high 档单任务成本其实介于 3.8 medium/high 之间、3.8 单任务反而更贵，且「Luna high 比 3.8 high 便宜 30 倍」。一条高赞评论总结：「3.8 真正令人印象深刻的只有 Google 的基础设施优势。」
3. **战略讽刺派**：延续 3.7 发布时对「Google 落后了、缺差异化、API key 申请摩擦大」的批评（见 3.7 HN 帖 [item 49289112](https://news.ycombinator.com/item?id=49289112)）；对「又一次 Flash、Pro 何时来」普遍不耐烦。

姊妹帖 [Kimi K3 and GLM-5.3 are better than Gemini 3.8 Flash](https://news.ycombinator.com/item?id=49539315) 直指 AA 智能榜上 Kimi K3、GLM-5.3（60）高于 3.8（59），但承认 3.8 单任务成本更低——中国系开源/低价模型的紧逼是本次评论区高频背景音。

总体情绪：**中性偏 skeptical**——「模型本身 OK、价格战有看点，但 Google 在 frontier 的缺席与单任务成本上升抵消了部分兴奋」。

### 7.5 争议与风险

- **Cyber 双用治理**：3.8 Flash Cyber 是放宽安全缓解（官方自述「more permissive set of mitigations」）的模型，仅向政府/关基/软件维护者分发。The Decoder 与 SilonANGLE 均强调此「首个面向防御的主流网安大模型」在攻击面自动化上的潜在争议（自动挖洞工具无论定位防御，都可能被滥用）。官方回应 = Frontier Safety Framework + 申请制 + 优先 fix 而非 exploit 的设计。（[官方安全口径](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)）
- **发布节奏信任**：Ars/the-decoder 提出高频小步发布 + 延期 3.5 Pro 的组合可能稀释「frontier」品牌信任；多家媒体用「Google 落后」作为默认叙事框架。
- **成本透明度**：官方「同价」宣传（与 3.7 相同 per-token）被 AA 数据部分证伪——按任务算贵约 40%；官方已在文档层面建议效率敏感者留在 3.7（官方口径，未被视为隐瞒但存在营销落差）。
- **可靠性历史**：官方 model card 主动披露「timeout issues」「occasionally not reach Critical Capability Levels」等框架语句（[model card](https://deepmind.google/models/model-cards/gemini-3-8-flash/)），说明长推理负载下超时是已知限制。

### 7.6 竞品与行业对照

| 对照项 | Gemini 3.8 Flash | Claude Opus 5 | GPT-5.6 Sol | 备注/来源 |
|--------|-----------------|---------------|-------------|----------|
| 每百万 token 输入/输出 | $0.75/$3.75（2027 后 $1.5/$7.5）| $5/$25 | $4/$20 | the-decoder（T1）|
| DeepSWE v1.1（官方口径）| 73.7% | 74.0% | 72.7% | Google 图（T0/T1）|
| AA Intelligence Index | 59（high）| — | 59（xhigh）| 并列；低于 Kimi K3/GLM-5.3 的 60（T2 转 AA）|
| CyberGym（漏洞发现）| 86.2%（Cyber）| — | 83.6% | the-decoder（T1）；另有 GPT-5.5-Cyber 85.6% |

行业含义（媒体共识）：Flash 线实质承担「对抗 DeepSeek/中国系低价模型 + 服务企业大规模 agent 工作流」的走量职能；Cyber/企业/政府路线是高毛利补充；真正的前沿旗舰竞争（Pro vs Opus vs GPT-5.6）因 3.5 Pro 缺席仍悬而未决。

### 7.7 中文语境

- **少数派「派早报」**（[链接](https://sspai.com/post/114113)）：9/3 早报收录发布，事实口径与官方一致（六周三款、DeepSWE 73.7→实为 54.9 HLE 引用准确、Cyber 限流说明）。
- **新浪财经专题**（[链接](https://finance.sina.com.cn/stock/t/2026-09-03/doc-iniqnieq2620132.shtml)）：9/3 长篇，增量观察为「谷歌正在把 Gemini 竞争重点从单纯聊天/问答推向编程、企业工作流以及能直接创造经济价值的 AI 执行任务」；并引用 AA 口径「不到四个月第四款 Flash」。
- **Unite.AI 中文**、繁体博客 Penchan 等亦有转载/整理稿，内容为官方通稿复述，无独家中信源价值。
- **缺位说明**：检索范围内未见 36氪、量子位、机器之心对本次发布的专题深度稿；中文社区（V2EX 等）未见显著独立讨论帖。中文权威覆盖以新闻稿复述为主，增量有限。

## 8. 分歧与待核实

| 项 | 说法 A | 说法 B | 建议 |
|----|--------|--------|------|
| DeepSWE v1.1 | 官方口径 73.7%（9to5 注明「Updated score」）| 个别第三方稿写 independent high 档 74%（buildfastwithai 等 SEO 类，非白名单）| 取官方 73.7%；74 疑为不同测法/四舍五入，不做事实 |
| Flash 发布节奏口径 | 官方/多数媒体：六周内第三款（3.6 于 7/21）| 9to5Google 导语写「三个月内第三次 Flash 更新」| 疑笔误；官方 + 3 家 T1 支持六周口径 |
| CyberGym 对比对象 | SiliconANGLE：Claude Mythos 5（83.8）、GPT-5.6 Sol（83.6）| the-decoder：3.5 Flash Cyber（77.5）、GPT-5.6 Sol（83.6）、GPT-5.5-Cyber（85.6）| 两组均出自 Google 官方图（可能对比组不同）；Sol=83.6 交叉一致；并列引用、不合并 |
| AA 智能指数排位 | the-decoder：3.8「与 GPT-5.6 Sol xhigh、Grok 4.6 medium 并列 59」| HN 帖：3.8 第 8、低于 Kimi K3 与 GLM-5.3（60）| 不冲突（并列对象不同）；榜单随 reasoning 档与数据更新浮动 |
| 3.5 Pro 延期程度 | 「数月推迟」（InsideAI）| 「无限期/无日期」（Wionews、Google 发言人「在测试中」）| Google 未给日期 = 无确定日期；以无日期为表述 |
| 发布日股价 | CNBC：+0.63% 收盘 $337.12 | 盘后口径 +0.6–0.7%；另见 ~1% | 收盘 0.63% 为基准（CNBC）；其他为盘后/盘中快照 |
| 3.5 Pro 是否会被 3.8 Flash 线彻底取代 | Ars/the-decoder：可能性上升（观点）| Google：仍在测试、未取消 | 观点，不做定论 |

## 9. 对用户问题的直接回答

**Q：Google Gemini 3.8 是什么、什么时候发布？**
2026-09-02（美东周三）由 Google DeepMind 发布，含 **Gemini 3.8 Flash**（GA，通用 coding/agent「workhorse」，1M 上下文，输入 $0.75 / 输出 $3.75 每百万 token，2027-01-01 起 $1.50/$7.50）与 **Gemini 3.8 Flash Cyber**（网安专用，仅限 Fairwind Program 可信防御方）。官方口径「迄今最强推理与编程模型」，六周内第三个 Flash。开发者可经 Gemini API/AI Studio/Antigravity/Android Studio/Stitch 使用；消费者走 AI Pro/Ultra 订阅（Gemini app、Search AI Mode、Sheets）。

**Q：它强在哪、有无独立验证？**
官方自评 DeepSWE v1.1（长程编码）73.7%，逼近 Claude Opus 5（74.0%），超过 GPT-5.6 Sol（72.7%）；HLE-Verified 54.9%；金融/法律专业基准超 3.7 与 frontier。独立平台 Artificial Analysis 智能指数 59（high），与 GPT-5.6 Sol（xhigh）、Grok 4.6 持平，但落后 Kimi K3、GLM-5.3（60）——即「不是绝对最强，而是该价位最强、单任务成本 Pareto 最优」。注意「works harder」使单任务成本较 3.7 上升约 40%，效率敏感场景官方建议仍用 3.7。

**Q：Cyber 变体和 Fairwind 是什么、为什么值得关注？**
网安专用模型，同底层 + 放宽安全缓解，聚焦「自动发现并修复漏洞」（明确防御优先于 exploit）。CyberGym 86.2%、CWE-Bench pass@1 47.2%（逼近最强 47.8%）、内部 20 语言基准成功率 >70%；Google 自报 Chrome 正确补丁 2.6×、<2 小时挖出 critical 漏洞。仅限政府、关基、软件维护者申请（Fairwind Program，≥650 参与方，配 CodeMender）。这是主流大厂首次以「受限分发」方式上线防御型网安大模型，治理与滥用风险仍是开放话题。

**Q：行业/社区怎么看？**
两极：HN 主帖 1006 分/567 评论偏 skeptical——认可模型实用性（Simon Willison 实测）与价格战，但质疑「frontier/Pro 缺席」「单任务成本不降反升」，且中国系模型在 AA 榜反超。主流解读把这次发布串进「3.5 Pro 延期 → DeepMind 换帅 → Flash 高频补位」的叙事；资本市场平淡（发布日 GOOGL +0.63%，处四个月连跌后重建叙事的节点）。

## 10. 参考链接（按 Tier 排序）

### Tier 0 官方
- [Introducing Gemini 3.8 Flash and 3.8 Flash Cyber — Google 官方博客（09-02，已深读全文）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- [Gemini 3.8 Flash Model Card — Google DeepMind（09-02）](https://deepmind.google/models/model-cards/gemini-3-8-flash/)
- [Gemini 3.8 Flash 产品页 — Google DeepMind](https://deepmind.google/models/gemini/flash/)
- [Google's Fairwind Program — Google 官方博客](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)
- [Fairwind Program — Google DeepMind 官方页](https://deepmind.google/fairwind-program/)
- [Introducing Gemini 3.7 Flash — Google 官方博客（08-13，时间线锚点）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/)
- [The next chapter of our AI momentum — Pichai/Hassabis 内部信（08-05，DeepMind 换帅）](https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/)

### Tier 1 权威媒体
- [Ars Technica：Google releases Gemini 3.8 Flash, its third Flash model in six weeks（09-02，全文已深读）](https://arstechnica.com/ai/2026/09/google-releases-gemini-3-8-flash-its-third-flash-model-in-six-weeks/)
- [SiliconANGLE：Google launches two Gemini 3.8 models（09-02，全文已深读）](https://siliconangle.com/2026/09/02/google-launches-two-gemini-3-8-models-with-cutting-edge-reasoning-capabilities/)
- [The Decoder：…third budget model in six weeks while frontier models remain MIA（09-02，全文已深读）](https://the-decoder.com/gemini-3-8-flash-is-googles-third-budget-model-in-six-weeks-while-frontier-models-remain-mia/)
- [9to5Google：Gemini 3.8 Flash rolling out three weeks after last release（09-02，全文已读）](https://9to5google.com/2026/09/02/gemini-3-8-flash-launch/)
- [CNBC：Google starts September with AI momentum after long losing streak（09-02）](https://www.cnbc.com/2026/09/02/google-starts-september-with-ai-momentum-after-long-losing-streak.html)
- [WSJ/Mint：New Google AI model said to narrow gap on coding ability（09-02，Skimaki 代号）](https://www.livemint.com/global/new-google-ai-model-said-to-narrow-gap-on-coding-ability-11788341542644.html)
- [Reuters/The Star：Google shakes up AI leadership as DeepMind chief shifts role（08-06）](https://www.thestar.com.my/tech/tech-news/2026/08/06/google-shakes-up-ai-leadership-as-deepmind-chief-shifts-role)
- [Wionews：Google delays Gemini 3.5 Pro …（Bloomberg 转述）](https://www.wionews.com/technology/google-delays-gemini-3-5-pro-after-ai-model-misses-coding-targets-report-says-1784276836487)
- [少数派派早报（09-03，中文）](https://sspai.com/post/114113)
- [新浪财经：才三周Flash就换代（09-03，中文）](https://finance.sina.com.cn/stock/t/2026-09-03/doc-iniqnieq2620132.shtml)

### Tier 2 补充（反响/社区/独立评测）
- [Hacker News 主帖：Gemini 3.8 Flash and 3.8 Flash Cyber（1006 分/567 评论）](https://news.ycombinator.com/item?id=49537553)
- [HN 分帖：Kimi K3 and GLM-5.3 are better than Gemini 3.8 Flash](https://news.ycombinator.com/item?id=49539315)
- [HN 历史帖：Gemini 3.7 Flash（反响基线）](https://news.ycombinator.com/item?id=49289112)
- [Artificial Analysis：Gemini 3.8 Flash 发布页（独立评测）](https://artificialanalysis.ai/models/releases/gemini-3-8-flash)
- [llm-stats：Gemini 3.8 Flash 定价/上下文/时延聚合](https://llm-stats.com/models/gemini-3.8-flash)
- [Seeking Alpha：Google unveils 'most intelligent' Gemini 3.8 Flash model（转述/市场）](https://seekingalpha.com/news/4639546-google-unveils-its-most-intelligent-gemini-38-flash-model-announces-fairwind-program)

---

*本报告按 web-deep-search-spec v1.4 生成，检索日 2026-09-03，共 6 轮 loop。报告正文简体中文，产品/API 名保留英文原文。未读取任何本地客户业务文档。*
