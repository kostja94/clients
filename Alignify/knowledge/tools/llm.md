# Large Language Model / 通用大语言模型 · 知识块（非线性笔记）

**材料范围**：公开网络检索（LMSYS / **Chatbot Arena**、BenchLM / LM Market Cap 方法论、MMLU / MMLU-Pro / HLE 论文与项目站、厂商 2026 年中发布博客）；**未**引用 Alignify 站内已发布正文或本站实测。网摘整理日期 **2026-06-23**。**快变排行数字** 唯一维护于 **[llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md)**（快照 2026-06-23）。

**站内对照**：正式页 **`/tools/llm`**、**`/zh/tools/llm`** · `content/tools/en|zh/llm.md` · slug **`llm`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 `#llm-tools` · `keywordEn`: **Large Language Model** · `keywordZh`: **大语言模型

## LLM 评测五轴

| 角色 | 文件 |
|------|------|
| **Hub（本页）** | 方法论、五轴分流、读榜清单、共享治理、行业格局叙事 |
| **快变快照** | [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md) |
| **专轴** | [llm-for-coding.md](./llm-for-coding.md) · [llm-for-math.md](./llm-for-math.md) · [llm-for-reasoning.md](./llm-for-reasoning.md) · [multimodal-llm.md](./multimodal-llm.md) |

## 与相邻 slug 分流（非五轴）

| slug | 典型问题 | 与本页边界 |
|------|---------|-----------|
| **`api`** | 怎么统一调用多模型？ | 本页：**哪个更强**；api：**怎么接** |
| **`inference-infrastructure`** | 怎么部署运行自己的模型？ | 本页：公开基准；infra：GPU/推理引擎 |
| **`evaluation`** | 用什么评 **我的** AI 应用？ | 本页：厂商公开榜；evaluation：离线/在线评测工具 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **LLM / 通用大模型**：在离散 token 上建模并经对齐为对话/工具产品；**通用**指跨任务平均表现，**不等于**每一专轴第一。
- **Chatbot Arena / LMSYS**：双盲对战 + **Elo** 人类偏好榜；[lmarena.ai](https://lmarena.ai/leaderboard/)——偏主观综合体验，与自动化基准互补。
- **MMLU / MMLU-Pro**：多学科选择题知识；MMLU 易饱和，Pro 延缓饱和。
- **加权综合分**：BenchLM 等将知识/推理/编码/多模态/Agent 加权合成 **Overall**——**换权重即换冠军**；见 **provisional vs verified**。
- **HLE（Humanity's Last Exam）**：高难度封闭学术题集合，拉开 MMLU 饱和区；含多模态子集——读分须看是否 **with tools**、是否纯文本子集（[agi.safe.ai](https://agi.safe.ai/) · [arXiv:2501.14249](https://arxiv.org/abs/2501.14249)）。**专轴展开**：推理见 [llm-for-reasoning.md](./llm-for-reasoning.md)；勿在专轴重复本定义。
- **provisional vs verified**：聚合榜行可能含厂商通报；采购优先 **verified / 独立复现**（[BenchLM methodology](https://benchlm.ai/methodology)）。

---

## 五轴总分流（避免混买混评）

| slug | 测什么 | 代表基准 / 信号 | 常见误用 |
|------|--------|-------------------|----------|
| **`llm`（本页）** | 跨任务平均、人类偏好、综合加权 | Arena Elo、BenchLM Overall、MMLU-Pro | 用总榜一名断言「最佳程序员/数学家」 |
| **`llm-for-coding`** | 仓库补丁、竞赛代码、CLI Agent | SWE-bench*、LiveCodeBench、Terminal-Bench | 用 HumanEval 饱和分选 enterprise monorepo |
| **`llm-for-math`** | 竞赛短答、证明、研究级数学 | AIME、FrontierMath、MATH-500/BRUMO | 用 AIME 满分断言 FP&A/工程计算能力 |
| **`llm-for-reasoning`** | 专家问答、抽象推理、测试时扩展 | GPQA Diamond、ARC-AGI-2、HLE 子域 | 用 GPQA 高分断言 ARC 格子推理同等 |
| **`multimodal-llm`** | 图文/视频理解 | MMMU-Pro、MM-Vet v2、Video-MME | 与 **image-generator**（生成）或 **world-model**（动力学）混谈 |

**排行数字**：各轴 Top N 见 [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md)——**勿在本页或专轴复制完整表格**。

---

## 专题对照：「通用榜」 vs 单边专轴

| 维度 | **通用综合 / Arena** | **单边专轴** |
|------|---------------------|--------------|
| **在测什么** | 偏好或多基准加权平均 | 代码仓库 / 奥数 / GPQA / 图表专家题等 |
| **典型信号** | Arena Elo、BenchLM Overall | SWE-bench、AIME、FrontierMath、MMMU-Pro、ARC-AGI-2 |
| **去哪读** | 本页 + snapshots §Overall | 四专轴 + snapshots 对应 § |

---

## 问题域（为何「最强模型」口径林立）

- **偏好 vs 客观**：Arena 反映投票人群与提示分布；学术基准反映可自动判分——**不一致是常态**。
- **饱和与迭代**：MMLU、AIME、GPQA 等前排挤；维护方 **降权 display-only 项**、抬高 HLE / SWE Pro / FrontierMath（以各站方法论为准）。
- **模式与 harness**：Thinking / Contemplating / 工具开关 / Agent 脚手架未对齐时 **禁止**跨表比绝对分。
- **收录与自报**：provisional 行可能仅反映厂商新闻稿；见 snapshots §读榜规则。
- **availability gap**：BenchLM Overall 榜首（如 Mythos 5）可能 **受限预览**——「最强」≠「可采购」；见 snapshots §采购警示。

---

## 读榜检查清单（全系列共用）

1. **子榜全称**：Verified vs Pro、MMMU vs MMMU-Pro、AIME display-only vs FrontierMath。
2. **Overall 还是分榜**：coding / math / vision / hard prompts 分列。
3. **Arena 类目**：文本 vs 视觉；样本量与置信区间（[lmarena.ai](https://lmarena.ai/leaderboard/)）。
4. **MMLU 版本**：原版 / Pro / few-shot；HLE 是否含图、是否允许 Python。
5. **Agent harness**：SWE 是否固定 mini-SWE-agent；Terminal-Bench 与 SWE **不可混读**。
6. **时间与快照**：checkpoint 日期、BenchLM Last verified、本库 [snapshots 日期](./llm-leaderboard-snapshots.md)。
7. **来源类型**：verified > 第三方独立 > 厂商自报 alone。

---

## 能力栈（读「通用榜」时）

- **BenchLM 类目缩写**：AG（Agent）/ CO（Coding）/ RE（Reasoning）/ MM（Multimodal）/ KN（Knowledge）等——见 [benchlm.ai](https://benchlm.ai/)。
- **综合 vs 单价**：Overall 高模型可能 **$/1M tok** 高一个数量级——选型对照 [api.md](./api.md) 定价层。
- **长子集 SKU**：Codex、Thinking、Extended——仍在通用族内，评测侧重点不同；编程见 [llm-for-coding.md](./llm-for-coding.md)。

---

## 形态谱系（产品层，与厂商解耦）

- **Instant / Chat SKU**：低延迟默认对话。
- **Reasoning / Thinking SKU**：测试时算力更高；o 系、R1 类、Extended Thinking、Meta **Contemplating**（多 Agent 并行）。
- **Codex / Coder SKU**：路由到代码优化后训练——仍可能出现在 Overall 加权中。
- **Multimodal-native SKU**：图文联合输入（如 Muse Spark）——理解榜见 [multimodal-llm.md](./multimodal-llm.md)。

---

## 落地碎片：选型三步

1. **写任务清单**（延迟、成本、是否 Agent、是否多模态、是否数学/代码/推理专精）。
2. **映射专轴**（上表五轴）+ 读 snapshots 对应 §——总榜只给「第一印象」。
3. **内部 golden set** 试跑 + 合同（训练退避、驻留）——Arena/ BenchLM **不能替代** 步骤 3。

---

## 选型速查（决策块）

| 你的首要任务 | 先读专轴 | 再看 snapshots § |
|--------------|----------|------------------|
| 修 GitHub issue / monorepo | [llm-for-coding](./llm-for-coding.md) | Coding |
| CLI / 终端自动化 | [llm-for-coding](./llm-for-coding.md)（Terminal-Bench） | Coding |
| 奥数 / 证明 / 研究数学 | [llm-for-math](./llm-for-math.md) | Math |
| 科学论证 / GPQA / ARC | [llm-for-reasoning](./llm-for-reasoning.md) | Reasoning |
| 图表 / 病历 / 视频理解 | [multimodal-llm](./multimodal-llm.md) | Multimodal |
| 「哪个综合最强」印象 | 本页 + snapshots §Overall | Overall |
| 统一 API 接入 | [api.md](./api.md) | — |
| 自建 GPU 部署 | [inference-infrastructure.md](./inference-infrastructure.md) | — |
| 评自己的应用质量 | [evaluation.md](./evaluation.md) | — |

---

## 行业注记 · 2026 年中格局（叙事层；数字见 snapshots）

- **Anthropic 梯队**：BenchLM Overall 常由 **Mythos 5 / Fable 5 / Opus 4.8** 占据前列——agentic coding 与 SWE Pro 叙事强；Mythos/Glasswing **预览可用性** 受限（snapshots §采购警示）。
- **OpenAI GPT-5.5 / Codex 线**：全面可用；第三方常引 **Terminal-Bench** 相对强项 vs Claude 的 **SWE Pro / OSWorld**（[axis-intelligence 对比](https://axis-intelligence.com/gpt-5-5-vs-claude-opus-4-8/)——**观点综合，非唯一数字源**）。
- **Google Gemini 3.1 Pro**：BenchLM [best/overall](https://benchlm.ai/best/overall) 常列「性价比 flagship」——知识与非 reasoning 场景叙事。
- **Meta Muse Spark（2026-04-08）**：MSL 原生多模态 + tool-use + **Contemplating** 测试时多 Agent；跨 MMMU-Pro / GPQA / SWE 官方分数见 snapshots §Muse Spark（[官方博客](https://ai.meta.com/blog/introducing-muse-spark-msl/)）。
- **开源/开放权重**：**GLM-5.2、DeepSeek V4 Pro、Qwen3.7** 等在 Overall 与分轴逼近闭源——轴内仍可能有差距；详见 snapshots 各 §。

*精确分数与名次勿从本段转引——回源 [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md) 与原 URL。*

---

## 主流厂商 · SKU 对照（2026 年中 · 产品层叙事）

| Provider | 通用 chat / instant | Reasoning / Thinking | Coding SKU | 多模态理解 | 开放权重 | 采购注意 |
|----------|---------------------|----------------------|------------|------------|----------|----------|
| **OpenAI** | GPT-5.5 等 | o 系 / high reasoning 档 | GPT-5.x **Codex** | GPT-5.x 图像输入 | 部分开源历史线 | API 全面；Enterprise 条款 |
| **Anthropic** | Claude Sonnet 档 | Extended Thinking | **Claude Code** / Opus agentic | Claude 视觉 | 无全量开源 frontier | Mythos/Glasswing **预览** |
| **Google** | Gemini Flash | Gemini thinking 模式 | 内嵌 IDE / Cloud | **Gemini 3.1 Pro** 长视频 | Gemma 等 | GCP 区域与数据条款 |
| **Meta** | Meta AI app | **Contemplating**（Muse） | tool-use + SWE 官方分 | **Muse Spark** native | Llama 与 Muse **不同线** | Muse API **private preview** |
| **DeepSeek** | V4 chat | R1 类推理 | V4 Pro coding 叙事 | 视觉 SKU 随版本 | **开放权重前列** | 自托管 vs API |
| **Alibaba** | Qwen chat | Qwen thinking | Qwen-Coder | Qwen-VL | Qwen 开源系 | 国内云与合规 |
| **Z.AI** | GLM chat | — | GLM coding | GLM-V | **GLM-5.2 开源权重** | 见 snapshots Overall |

*SKU 名与 API 路由以厂商文档为准；本表供 **成稿抽取** 与选型对话，非实时价目表。*

---

## MMLU / 知识轴 · 怎么读（成稿块）

- **MMLU**：57 学科选择题——2024 起 frontier **>90%** 常见，**弱区分**「谁更博学」。
- **MMLU-Pro**：更多推理型干扰项——BenchLM **KN** 类目仍引用；Top N 见 snapshots §Knowledge。
- **与 HLE 分工**：MMLU 饱和后，**tail 区分**靠 HLE、FrontierMath、GPQA——勿用 MMLU 一名断言科研论证能力。
- **与专轴分工**：编程/数学/视觉 **各自有金标**——MMLU 高不保证 SWE、AIME、MMMU-Pro 同序。

**成稿可用 TLDR**：「MMLU 适合讲 **通识知识基线**；选型仍须映射到 **任务专轴** + 内部试跑。」

---

## Chatbot Arena · 怎么读（成稿块）

- **测什么**：匿名双盲对战后的人类 **偏好 Elo**——综合 helpfulness、风格、安全拒绝、多轮连贯。
- **不测什么**：**不**等价 SWE Resolved %、AIME、MMMU-Pro——Arena 第一 ≠ 最佳程序员。
- **类目**：**Text** vs **Vision** 分列；hard prompts / coding 等子榜（以 [lmarena.ai](https://lmarena.ai/leaderboard/) 为准）——跨类目 **禁止**比 Elo。
- **样本与置信**：新模型 Elo 波动大——读 **对战数** 与置信区间（原站提供）。
- **人群偏差**：投票用户、语言、提示分布影响排名——**非全球均匀抽样**。
- **与 BenchLM Overall**：Arena 偏 **体验**；BenchLM 偏 **多基准加权**——两者 champion 可不同。

**成稿可用 TLDR**：「Arena 回答 **用户更愿意用哪个**；BenchLM/SWE 回答 **客观基准上谁更强**——采购须两者 + golden set。」

**排行数字**：文本 Elo 节选见 [llm-leaderboard-snapshots.md §Preference](./llm-leaderboard-snapshots.md)。

---

## 开源 vs 闭源 · 选型对照（成稿块）

| 维度 | **开放权重 / 可自托管** | **闭源 API** |
|------|-------------------------|--------------|
| **典型代表** | GLM-5.2、DeepSeek V4 Pro、Qwen3.x | GPT-5.5、Claude Opus、Gemini 3.1 Pro |
| **Overall 叙事** | snapshots 中 **Top 5 可占 2–3 席** | Mythos 等 **预览 SKU** 可能不可采购 |
| **轴内差距** | coding/math tail 仍可能 **落后 5–15pt** | agentic coding、SWE Pro 叙事常领先 |
| **合规** | 权重审计、本地驻留、 air-gap | Enterprise DPA、区域推理 |
| **成本结构** | CapEx（GPU）+ 运维 | OpEx（$/tok）+ 阶梯价 |
| **何时优先开源** | 数据不可出境、需微调、高 QPS 自研 | 追 frontier tail、低运维、快速迭代 |

**落地**：开源 **≠** 零成本——见 [inference-infrastructure.md](./inference-infrastructure.md)；统一多模型接入见 [api.md](./api.md)。

---

## Thinking / Reasoning 模式 · 成本与场景（成稿块）

| 模式 | 典型产品信号 | 延迟 | $/call 叙事 | 适合任务 |
|------|--------------|------|-------------|----------|
| **Instant / Chat** | 默认对话 SKU | 低 | 低 | 客服、摘要、翻译 |
| **Extended Thinking** | Claude thinking、o 系 | 高 | **10–100×** 可能 | 多步论证、复杂规划 |
| **Contemplating** | Muse Spark 多 Agent | 很高 | 预览/API 未统一 | 研究级 HLE/FrontierScience |
| **Refinement loop** | ARC 竞赛 harness | 可变 | 依赖轮次 | 抽象规则、可迭代改答 |

**成稿提示**：同一张 GPQA 榜行，**chat 分 vs thinking 分** 可能不同 SKU——读榜须对齐 **API 路由名**。

---

## 企业采购工作流（成稿块 · 七步）

1. **任务清单**：写清 P0 场景（coding / 数学 / 推理 / 多模态 / 综合 chat）与 **延迟、成本、合规** 硬约束。
2. **映射五轴**：用上表 §五轴总分流——禁止用 Overall 一名覆盖全部。
3. **读 snapshots**：对应 §Overall / Coding / Math / Reasoning / Multimodal / Knowledge / Preference——带 **快照日期** 写进内部 memo。
4. **短名单 2–3 家**：含 **可采购** SKU（排除 Mythos 类预览，除非已获组织白名单）。
5. **Golden set 试跑**：50–200 条内部题；指标 **任务成功率、幻觉率、$/成功任务**——非公开榜 %。
6. **合同**：训练退避、驻留区域、indemnity、SLA、**第二 provider** 条款。
7. **季度复审**：只更新 [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md) + 本页 §行业注记——框架段 stable。

---

## 常见误读 FAQ（Hub · 成稿块）

| 误读 | 纠正 | 延伸阅读 |
|------|------|----------|
| 「BenchLM Overall 第一 = 买它就行」 | Overall **换权重换冠军**；Mythos 等可能 **不可采购** | snapshots §采购警示 |
| 「Arena Elo 高 = SWE 最强」 | Arena 测 **偏好**，SWE 测 **补丁** | [llm-for-coding.md](./llm-for-coding.md) |
| 「MMLU 90%+ = 科研助手够用」 | MMLU 饱和；科研 tail 看 **HLE / GPQA / FrontierMath** | [llm-for-reasoning.md](./llm-for-reasoning.md) |
| 「AIME 满分 = 公司财务建模强」 | AIME **display-only** 且与 FP&A 分布无关 | [llm-for-math.md](./llm-for-math.md) |
| 「MMMU 高 = 视频理解强」 | 静态 **≠** Video-MME | [multimodal-llm.md](./multimodal-llm.md) |
| 「开源权重 Overall 高 = 全轴第一」 | 轴内 tail 仍可能有 **双位数 gap** | snapshots 分轴 § |
| 「厂商博客一个数 = 第三方榜同分」 | 自报 vs prov. vs verified **差 1–5pt 常见** | snapshots §读榜规则 |
| 「Thinking 开永远更好」 | **$/call 与延迟** 常不可接受 | 上表 §Thinking 模式 |
| 「一个 benchmark 选型足够」 | **禁止**；须 golden set | §落地碎片 · 选型三步 |
| 「GPT-4o / Claude 3.5 仍代表 2026 格局」 | 2024 checkpoint **仅历史引用** | 四专轴 §轴内解读 |

---

## 场景 → 读榜路径（成稿块 · 扩展）

| 场景 | 第一基准 | 第二基准 | 勿用 |
|------|----------|----------|------|
| 企业 issue 修复 | SWE Verified + **自建 harness** | SWE Pro | HumanEval |
| DevOps / shell Agent | Terminal-Bench | 内部 CLI 脚本集 | SWE alone |
| 高中奥数辅导 | MATH-500 / BRUMO | 自建错题 | AIME 排名 alone |
| 量化研究辅助 | **业务试算** | FrontierMath 叙事 | AIME |
| 医学文献问答 | GPQA + **领域 RAG** | HLE 子集 | MMLU alone |
| 法律合同推理 | 自建逻辑题 + GPQA | Thinking SKU 试跑 | Arena alone |
| 票据 / UI 截图 | MMMU-Pro + **JSON 输出 SLA** | 内部 OCR 集 | MM-Vet judge  alone |
| 长视频摘要 | Video-MME | 内部视频集 | MMMU |
| 「写代码 + 看图改 UI」 | SWE Multimodal | [multimodal-llm](./multimodal-llm.md) | GPQA |
| 综合聊天产品选型 | Arena Text + snapshots Overall | MMLU-Pro | SWE 一名 |

---

## Alignify 成稿抽取索引（Hub · 块目录）

| 块标题 | 用途 | 下游 slug |
|--------|------|-----------|
| §词汇锚点 | TLDR、术语表 | `llm` |
| §五轴总分流 | 导航、内链 hub | 全五轴 |
| §读榜检查清单 | FAQ、方法论段 | 全五轴 |
| §主流厂商 · SKU 对照 | 厂商段落、对比表 | `llm` |
| §MMLU / 知识轴 | 知识榜解读 | `llm` |
| §Chatbot Arena | 偏好榜解读 | `llm` |
| §开源 vs 闭源 | 采购决策 | `llm` + infra |
| §Thinking 模式 | 成本段 | `llm-for-reasoning` |
| §企业采购工作流 | B2B 清单体 | `llm` |
| §常见误读 FAQ | FAQ 节 | `llm` |
| §场景 → 读榜路径 | 用例矩阵 | 全五轴 |
| §行业注记 | 2026 格局段 | `llm` |
| §风险 · 合规 · 治理 | 合规段 | 全五轴（共享） |
| snapshots §Overall 等 | **数字**（带日期） | 引用 snapshots |

*写正式 Tools 页时：**框架段抽 hub/专轴，数字段只引 snapshots 并带 `2026-06-23`。*

---

## 风险 · 合规 · 治理（五轴共享；专轴只写轴特有风险）

- **训练数据退避**：Chat vs API vs Enterprise 条款不同——采购以合同为准。
- **数据驻留与跨境**：推理区域（EU-only 等）影响 GDPR/出境合规。
- **输出事实性**：高 stakes 场景须人工或规则校验——LLM 可产生 plausible 错误。
- **供应商锁定**：API 格式、function calling、提示模板不兼容——关键路径保留 **第二 provider**。
- **榜单数字≠生产表现**：Benchmark 分布 ≠ 你的任务分布；**禁止**用 Overall 替代内部评测。
- **评测污染与自报**：公开题可能进入训练集；厂商博客分数须第三方交叉（见 snapshots §读榜规则）。

---

## 外链索引

| 名称 | URL |
|------|-----|
| **排行快照（Alignify KB）** | [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md) |
| Chatbot Arena | [lmarena.ai/leaderboard](https://lmarena.ai/leaderboard/) |
| BenchLM | [benchlm.ai](https://benchlm.ai/) · [methodology](https://benchlm.ai/methodology) |
| Humanity's Last Exam | [agi.safe.ai](https://agi.safe.ai/) · [arXiv:2501.14249](https://arxiv.org/abs/2501.14249) |
| CodeSOTA 宽表 | [codesota.com/llm](https://codesota.com/llm) |
| LiveCodeBench | 实时编程评测基准（防污染）[livecodebench.github.io](https://livecodebench.github.io/) |

---

## 工具与产品类型（LLM 评测）

| 基准类型 | 代表基准 | 用途 |
|---------|---------|------|
| 综合知识 | MMLU-Pro, GPQA Diamond | 学术/专业知识覆盖 |
| 编程能力 | SWE-bench Verified, LiveCodeBench | Agent 软件工程 |
| 数学推理 | AIME, FrontierMath | 形式推理与计算 |
| 多模态 | MMMU-Pro, MM-Vet v2 | 图文/视频理解 |
| 人类偏好 | Chatbot Arena, WildBench | 用户排名 |

### 对比与测评（第三方；观点非官方）

2026 年中格局：Claude 系列在编程与推理领先；GPT-5 系列在多模态与通用任务全面；Gemini 3 在长上下文有差异化。闭源 vs 开源差距在缩小（DeepSeek-R1、Qwen3 逼近前沿）。实时排行见 [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md)。

---

## 延伸阅读

- 快变数字：[llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md)
- 专轴：[llm-for-coding.md](./llm-for-coding.md) · [llm-for-math.md](./llm-for-math.md) · [llm-for-reasoning.md](./llm-for-reasoning.md) · [multimodal-llm.md](./multimodal-llm.md)
- 相邻：[api.md](./api.md) · [inference-infrastructure.md](./inference-infrastructure.md) · [evaluation.md](./evaluation.md)
