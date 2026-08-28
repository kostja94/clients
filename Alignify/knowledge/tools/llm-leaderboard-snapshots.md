# LLM 评测排行快照 · 快变事实层

**材料范围**：公开网络检索（[BenchLM](https://benchlm.ai/) 聚合榜、厂商官方博客与评测方法论、Chatbot Arena）；**未**引用 Alignify 站内 JSON 或本站实测。**本文件为 LLM 评测五轴唯一数字维护点**——框架与分流见 [llm.md](llm/llm.md)；专轴解读见 [llm-for-coding.md](llm/llm-for-coding.md) 等。

**快照日期**：**2026-06-23** · **建议复审周期**：每 **90** 天 · **上次数据源 verified 标注**：BenchLM 主站 Last verified **2026-06-18**（以原页为准）

**站内对照**：非独立 slug；数字被 [llm.md](llm/llm.md) 及四专轴引用。

---

## 读榜规则（全系列共用）

- **去重规则（Top N by provider）**：在指定 BenchLM 子榜上按分数从高到低扫描，**同一 provider 只保留首条**，直至凑满 N 家（同一公司多 SKU 时本表为「provider 一览」而非原生 Top N 行）。
- **provisional vs verified**：BenchLM 区分 **source-unverified** 与 **verified** 行——采购优先 **verified**；本表未逐行标注时默认 **provisional**，回源核对。
- **禁止跨表直比**：不同子榜（Verified vs Pro、MMMU vs MMMU-Pro、AIME vs FrontierMath）**百分数不可并列**；不同 **Agent harness**（bash 工具、采样次数、Thinking 模式）未对齐时禁止比绝对分。
- **厂商自报**：Meta 等官方博客数字与第三方聚合可能差 1–3pt——以 **官方 methodology + 第三方交叉** 为准。
- **非采购依据**：下列表格仅供把握 2026 年中格局；选型须 **内部 golden set + 合同条款**。

---

## Overall · BenchLM 综合 Top 5（按 provider 去重）

**来源**：[BenchLM Leaderboard](https://benchlm.ai/leaderboard) · [Best Overall](https://benchlm.ai/best/overall) · 快照 **2026-06-18

| # | Provider | 代表模型 | Overall | 备注 |
|---|----------|-----------|---------|------|
| 1 | Anthropic | Claude Mythos 5 (Project Glasswing) | 99 | prov.；受限预览 SKU |
| 2 | Z.AI | GLM-5.2 | 91 | **开源权重**前列 |
| 3 | Alibaba | Qwen3.7 Max | 90 | prov. |
| 4 | OpenAI | GPT-5.4 Pro | 90 | prov. |
| 5 | Google | Gemini 3.1 Pro | 89 | prov.；性价比 flagship 叙事 |

*按 provider 去重后 **同一 Anthropic 只占一行**（Fable 5 / Opus 4.8 等次 SKU 不重复计入）。**可采购**对照：Claude Opus 4.8 **93**、GPT-5.5 **87** 仍在 Top 15——见 [benchlm.ai/leaderboard](https://benchlm.ai/leaderboard)（Last verified **2026-06-18**）。*

---

## 分轴快照

### Coding · SWE-bench Verified Top 5

**来源**：[BenchLM sweVerified](https://benchlm.ai/benchmarks/sweVerified) · 快照 **2026-06-18** · 指标：**% Resolved** · harness 见原站

| # | Provider | 代表模型 | Verified % | 备注 |
|---|----------|-----------|------------|------|
| 1 | Anthropic | Claude Mythos 5 | 95.5 | prov.；BenchLM sweVerified #1（2026-06-18） |
| 2 | OpenAI | GPT-5.3 Codex | 85 | prov. |
| 3 | DeepSeek | DeepSeek V4 Pro (Max) | 80.6 | 开源阵营前列 |
| 4 | MiniMax | MiniMax M3 等 | 80.5 | prov. |
| 5 | Alibaba | Qwen 系条目 | 80.4 | prov.；SKU 以原表为准 |

***可采购对照**（非去重表）：Claude Opus 4.8 **88.6%**（BenchLM #3）；Meta Muse Spark **77.4%**（#22，[官方 methodology](https://ai.meta.com/static-resource/muse-spark-eval-methodology)）。第三方 harness：Opus 4.8 **~88.6%** vs GPT-5.5 **~72%** Verified——[axis-intelligence](https://axis-intelligence.com/gpt-5-5-vs-claude-opus-4-8/)（2026-05，**非 BenchLM 官方**）。*

**SWE-bench Pro（节选）**：Claude Opus 4.8 **~69.2%** vs GPT-5.5 **~58.6%**（第三方 harness 口径，[axis-intelligence](https://axis-intelligence.com/gpt-5-5-vs-claude-opus-4-8/) · 2026-05）；BenchLM [swePro](https://benchlm.ai/benchmarks/swePro) 行列更多、分差更大。

**Terminal-Bench / OSWorld（Agent 环境，非 SWE）**：GPT-5.5 在 **Terminal-Bench 2.x** 常引 **~78–82%** 档、Claude Opus 4.8 **~74–75%**（同一第三方文）；**OSWorld-Verified** Claude **~83%** vs GPT **~79%**——与 SWE 排序**不必一致**。

---

### Reasoning · GPQA Diamond Top 5

**来源**：[BenchLM GPQA](https://benchlm.ai/benchmarks/gpqa) · 快照 **2026-06-18

| # | Provider | 代表模型 | GPQA Diamond | 备注 |
|---|----------|-----------|--------------|------|
| 1 | Anthropic | Claude Fable 5 | 94.5 | prov.；BenchLM GPQA #1 |
| 2 | OpenAI | GPT-5.5 等 | 93.6 | prov.；BenchLM #5 |
| 3 | Alibaba | Qwen3.6 Max（Closed） | 92.4 | prov. |
| 4 | Google | Gemini 系 | 92.2 | prov. |
| 5 | Z.AI | GLM-5 等 | 91.2 | prov.；开源/open-weight |

*前排分差常 **<2pt**——GPQA 趋饱和；更难 tail 见 HLE、ARC-AGI-2（框架见 [llm-for-reasoning.md](llm/llm-for-reasoning.md)）。*

---

### Math · AIME26（display-only）

**来源**：[BenchLM AIME26](https://benchlm.ai/benchmarks/aime2026) · [BenchLM math](https://benchlm.ai/math) · 快照 **2026-06-18

BenchLM 注明 **AIME26 为 display-only、不计入总榜加权**；该页收录行数少，**按 provider 去重后常不足 5 家**。

| # | Provider | 代表模型 | AIME26 | 备注 |
|---|----------|-----------|--------|------|
| 1 | Z.AI | GLM-5.2 | 99.2% | display；BenchLM #1 |
| 2 | Moonshot AI | Kimi K2.6 | 96.4% | display |
| 3 | Alibaba | Qwen3.6 Plus（Closed） | 95.3% | display |
| 4 | Anthropic | Claude 系条目 | 95.1% | display；SKU 以原表为准 |
| 5 | Microsoft | Microsoft 系条目 | 94.5% | display |

---

### Multimodal · MMMU-Pro Top 5

**来源**：[BenchLM MMMU-Pro](https://benchlm.ai/benchmarks/mmmuPro) · 快照 **2026-06-18

| # | Provider | 代表模型 | MMMU-Pro | 备注 |
|---|----------|-----------|----------|------|
| 1 | OpenAI | GPT-5.4 Pro | 94% | prov. |
| 2 | Anthropic | Claude Mythos 5 | 92.7% | prov. |
| 3 | Google | Gemini 3.1 Pro | 83.9% | prov. |
| 4 | Meta | Muse Spark | 80.4% | **官方** methodology；BenchLM #9 |
| 5 | Moonshot AI | Kimi K2.6 | 79.4% | prov. |

*MMMU（非 Pro）与 MMMU-Pro **分数区间不可比**。*

---

### Knowledge · MMLU-Pro Top 5

**来源**：[BenchLM MMLU-Pro](https://benchlm.ai/benchmarks/mmluPro) · 快照 **2026-06-18** · 指标：**% accuracy

| # | Provider | 代表模型 | MMLU-Pro | 备注 |
|---|----------|-----------|----------|------|
| 1 | Alibaba | Qwen3.7 Max | 89.6% | prov.；BenchLM MMLU-Pro #1 |
| 2 | Anthropic | Claude Opus 4.5 | 89.5% | prov. |
| 3 | DeepSeek | DeepSeek V4 Pro 等 | 87.5% | prov.；开源阵营 |
| 4 | Moonshot AI | Kimi 系 | 87.1% | prov. |
| 5 | NVIDIA | NVIDIA 系 | 86.8% | prov. |

*原版 MMLU 在前沿模型上 **>90% 饱和**——读榜优先 MMLU-Pro 或 HLE tail（见 [llm.md](llm/llm.md) §词汇锚点）。*

---

### Math · FrontierMath（Tier 分层 · 公开报告节选）

**来源**：[Epoch AI FrontierMath](https://epoch.ai/frontiermath/tiers-1-4/the-benchmark) · [arXiv:2411.04872](https://arxiv.org/abs/2411.04872) · 快照 **2026-06-23

FrontierMath 用 **未公开题集** + Python 验证器；**Tier 越高越难**。下列为 **2025–2026 公开材料中的格局叙述**（非实时榜行；精确 % 回源 Epoch 原页）：

| Tier | 难度叙事 | 2026 年中格局（公开材料） |
|------|----------|---------------------------|
| **T1–T2** | 研究生级、可验证 | Epoch 公开评估：前沿模型 **整体 <2%**（旧版全集）；**显著高于** AIME 饱和区 |
| **T3** | 研究级组合题 | 头部闭源 **低–中个位 %**；开源常 **落后 5–15pt**（轴内，非跨表） |
| **T4** | 极难、长链证明 | 最佳模型 **极低分**——与 AIME **96% 档不可比** |

**MathArena / USAMO 线**：证明题人审榜与 FrontierMath **排序不必一致**——教辅场景见 [llm-for-math.md](llm/llm-for-math.md) §形态谱系 Type B。

**BRUMO / MATH-500（加权参与）**：BenchLM math 子分仍引用——较 AIME 更有 **日常数学任务** 区分度；具体行见 [benchlm.ai/math](https://benchlm.ai/math)。

---

### Reasoning · ARC-AGI-2（公开竞赛叙事 · 非百分制统一榜）

**来源**：[ARC Prize](https://arcprize.org/) · [arXiv:2505.11831](https://arxiv.org/abs/2505.11831) · 快照 **2026-06-23

ARC-AGI-2 **不是**与 GPQA 同单位的 % 榜——读 **pass@k、refinement loop 是否允许、私有集 vs 公开集**。

| 信号 | 2026 年中公开叙事 | 读榜注意 |
|------|-------------------|----------|
| **ARC-AGI-1 饱和** | 多模型 **>80%** 公开集 | 不代表 ARC-2 同等 |
| **ARC-AGI-2 tail** | 头部 **个位–低两位 %** 常见 | harness 可差 **10×+** |
| **与 GPQA** | GPQA 高 **不预测** ARC-2 高 | 见 [llm-for-reasoning.md](llm/llm-for-reasoning.md) |

---

### Preference · Chatbot Arena（文本 · 按 provider 去重节选）

**来源**：[lmarena.ai/leaderboard](https://lmarena.ai/leaderboard/) · **实时变动** · 本表为 **2026-06-23 检索时第三方转述 + 官方博客语境**——**引用须回源 live 榜

| # | Provider | 代表模型 | 文本 Elo（约） | 备注 |
|---|----------|-----------|----------------|------|
| 1 | Anthropic | Claude Fable 5 | **1507.6** | BenchLM 主榜 Elo 列（2026-06-18） |
| 2 | Google | Gemini 3.1 Pro | **1486.4** | 同上 |
| 3 | OpenAI | GPT-5.4 Pro | **1478.0** | 同上 |
| 4 | Alibaba | Qwen3.7 Max | **1474.7** | 同上 |
| 5 | xAI | Grok 4.1 | **1459.6** | 同上 |

*BenchLM 主榜 Elo 与 [lmarena.ai](https://lmarena.ai/leaderboard/) **live 榜可能漂移**——成稿须双源标注日期。Meta 博客语境 Muse Spark **~1474–1491** Elo（第三方转述）。*

**Vision / 多模态 Arena**：类目独立——MMMU 高 **不保证** Arena Vision 高；见 [multimodal-llm.md](llm/multimodal-llm.md)。

Arena 反映 **人类双盲偏好**（helpfulness、风格、拒绝率），与 SWE/GPQA **排序常不一致**——读 [llm.md](llm/llm.md) §专题对照 · 通用榜 vs 专轴。

---

## 跨轴案例 · Meta Muse Spark（2026-04-08）

**来源（官方）**：[Introducing Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/) · [Eval Methodology](https://ai.meta.com/static-resource/muse-spark-eval-methodology) · Meta Superintelligence Labs（MSL）

| 基准 | 分数 | 模式 / harness | 来源类型 |
|------|------|----------------|----------|
| MMMU-Pro | 80.4% | standard 10-option；rule-based grading | 官方 methodology |
| GPQA Diamond | ~89.5% | 4-run average | 官方 methodology（第三方转述；以 PDF 为准） |
| SWE-bench Verified | 77.4% | bash + file tools；15 attempts avg | 官方 methodology |
| SWE-bench Pro | 55.0% | public set；4 attempts avg | 官方 methodology |
| HLE | 58% | **Contemplating** 多 Agent 并行 | 官方博客 |
| FrontierScience Research | 38% | Contemplating | 官方博客 |
| LiveCodeBench Pro | 80.0% | 见 methodology | BenchLM 聚合引官方 |

**官方自述 gap**：long-horizon **agentic systems** 与 **coding workflows** 仍为投资方向——勿用 MMMU/GPQA 高分代替企业 SWE harness 结论。

**可用性**：meta.ai / Meta AI app；API **private preview**——非开源 Llama 路线。

---

## 采购警示 · availability gap（非排名）

| 现象 | 含义 |
|------|------|
| **Claude Mythos / Project Glasswing** | BenchLM Overall 常列榜首，但 **受限组织预览**——「最强」≠「可合同采购」 |
| **Claude Fable / Opus 4.8** | 公开 API 与 agentic coding 叙事主力；与 GPT-5.5 任务分工见 coding 轴 Terminal vs SWE |
| **GPT-5.5 / Codex SKU** | 全面可用；Terminal-Bench 叙事强于部分 SWE Pro 对比文 |
| **Gemini 3.1 Pro** | 常列「性价比 flagship」（BenchLM best/overall 叙事） |
| **GLM-5.2 / DeepSeek V4 / Qwen3.7** | 开源或开放权重前列；与闭源头部仍可能有 **5–15pt** 轴内差距（随轴而异） |
| **Muse Spark** | Meta 2026 重新入场信号；跨轴分数须读 **methodology**，API 未全面开放 |

---

## 外链索引

| 名称 | URL |
|------|-----|
| BenchLM 总榜 | [benchlm.ai/leaderboard](https://benchlm.ai/leaderboard) |
| BenchLM 方法论 | [benchlm.ai/methodology](https://benchlm.ai/methodology) |
| SWE-bench 官方 | [swebench.com](https://www.swebench.com/) |
| HLE | [agi.safe.ai](https://agi.safe.ai/) |
| Muse Spark 博客 | [ai.meta.com/blog/introducing-muse-spark-msl/](https://ai.meta.com/blog/introducing-muse-spark-msl/) |
| Muse Spark 评测方法 | [ai.meta.com/static-resource/muse-spark-eval-methodology](https://ai.meta.com/static-resource/muse-spark-eval-methodology) |
| Chatbot Arena | [lmarena.ai/leaderboard](https://lmarena.ai/leaderboard/) |

---

## 延伸阅读

- 框架 hub：[llm.md](llm/llm.md)
- 专轴：[llm-for-coding.md](llm/llm-for-coding.md) · [llm-for-math.md](llm/llm-for-math.md) · [llm-for-reasoning.md](llm/llm-for-reasoning.md) · [multimodal-llm.md](llm/multimodal-llm.md)
