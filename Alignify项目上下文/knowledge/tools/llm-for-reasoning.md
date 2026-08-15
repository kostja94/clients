# AI Reasoning LLM / 推理向大模型 · 知识块（非线性笔记）

**材料范围**：公开网络检索（GPQA / ARC-AGI-2 论文；BenchLM GPQA；Meta Muse Spark **Contemplating** 官方披露）；**未**引用 Alignify 站内正文或本站实测。网摘整理日期 **2026-06-23**。

**站内对照**：正式页 **`/tools/llm-for-reasoning`**、**`/zh/tools/llm-for-reasoning`** · `content/tools/en|zh/llm-for-reasoning.json`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 `#llm-for-reasoning-tools`

**Hub · HLE 完整定义 · 五轴分流**：[llm.md](./llm.md) · **排行快照**：[llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md) §Reasoning

**站内相邻**：[llm-for-math.md](./llm-for-math.md) · [llm-for-coding.md](./llm-for-coding.md)

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **推理向 LLM**：**Thinking / Reasoning / o-series / R1 类**——长链思考、测试时算力、自洽检查；**延迟与 $/call 通常高于 chat**。
- **知识 vs 推理**：**MMLU** 测博学选择题 ≠ 多步演绎；**GPQA Diamond** 更近专家难题（[benchlm.ai/benchmarks/gpqa](https://benchlm.ai/benchmarks/gpqa)）。
- **HLE**：完整定义见 **[llm.md](./llm.md) §词汇锚点**；本轴用于 **tail 区分** 与 **with tools vs no tools** 对照——勿重复展开。
- **ARC-AGI-2**：少样本视觉-符号格子抽象推理——**ARC-1 高分不保证 ARC-2**（[arXiv:2505.11831](https://arxiv.org/abs/2505.11831) · [arcprize.org](https://arcprize.org/)）。
- **Refinement loop**：外部迭代改答——与 **Contemplating**（多 Agent 并行）同属测试时扩展家族，**协议不同不可混读分数**。
- **Contemplating（Meta Muse Spark）**：多 Agent 并行推理模式；官方引 HLE **58%**、FrontierScience **38%**（[官方博客](https://ai.meta.com/blog/introducing-muse-spark-msl/)——据 Meta 公开资料）。

---

## 专题对照：推理轴 vs 邻近轴

| 测什么 | **推理 / 抽象** | **数学竞赛** | **编程工程** |
|--------|------------------|--------------|--------------|
| 代表基准 | GPQA、ARC-AGI、HLE 子域 | AIME、FrontierMath | SWE-bench、Terminal-Bench |
| 专轴 | 本页 | [llm-for-math.md](./llm-for-math.md) | [llm-for-coding.md](./llm-for-coding.md) |

---

## 问题域

- **GPQA 前排挤**：2026-04 起头部常 **<2pt** 分差——tail 看 HLE、ARC-AGI-2。
- **ARC 零样本 vs 高 harness**：同一模型 5% → 50%+ 的鸿沟——读协议是否允许 refinement loop（本笔记 **不裁定** 是否「真推理」）。
- **工具**：HLE **with tools** vs **no tools** 分数差巨大——**不可并列**。
- **命题偏差与学科覆盖**：GPQA Diamond 偏向博士生视角的专家题，过度代表特定学科（生物/物理/化学）——选型需确认任务分布是否匹配。
- **测试时扩展的 ROI 悖论**：更长的 thinking chain 提升分数——但边际收益递减且推理 token 成本指数上升——企业采购需设定 $/GPQA点 的性价比阈值。

---

## 形态谱系（推理策略）

- **Type A — 测试时扩展（Test-Time Compute）**：o 系、Extended Thinking——质量↑ 成本↑。
- **Type B — Refinement Loop**：外部多轮改答——ARC 竞赛常见。
- **Type C — 工具增强**：Python、搜索——HLE with tools 测此能力。
- **Type D — 少样本抽象**：ARC-AGI——「从零推断规则」。
- **Type E — 多 Agent 并行（Contemplating）**：Meta Muse Spark——latency 与单 Agent 长思考 trade-off 不同。

---

## 落地碎片

- **严谨论证 / 科学问答**：GPQA + HLE + **自建逻辑题**；数学专项 → [llm-for-math.md](./llm-for-math.md)。
- **延迟敏感**：默认 chat SKU；批处理研究再开 Thinking。
- **预算有限**：默认档位常够文档分析；仅 **5+ 步逻辑链** 任务值得高推理档。
- **抽象规则任务**：看 ARC 类能力——GPQA 预测力弱。

---

## 排行快照

GPQA Diamond Top N 见 **[llm-leaderboard-snapshots.md §Reasoning](./llm-leaderboard-snapshots.md)**（2026-06-23）。

**轴内解读**：2026 年中 GPQA 前排 Anthropic / OpenAI / DeepSeek / Qwen **~90–94%** 档聚集——选型看 **$/thinking token** 与 **HLE/ARC tail**，非 GPQA 第 1 vs 第 3 的 1pt 差。Muse Spark **Contemplating** 展示 **multi-agent test-time** 可抬 HLE，但 **API 未全面开放**（见 snapshots §Muse Spark）。

---

## Thinking SKU · 厂商对照（成稿块）

| Provider | 产品信号 | 测试时扩展形态 | 公开基准叙事 | 采购注意 |
|----------|----------|----------------|--------------|----------|
| **OpenAI** | o 系 / high reasoning | 长 CoT、内部 deliberation | GPQA、HLE with tools | $/reasoning tok 高 |
| **Anthropic** | Extended Thinking | 可见/不可见思考链 | SWE + GPQA 双强叙事 | 与 Opus chat **不同路由** |
| **DeepSeek** | R1 类 | 开源推理链可见 | GPQA 前排、成本低 | 自托管 vs API |
| **Google** | Gemini thinking | 多模态+推理 | MMLU-Pro、MMMU | GCP 条款 |
| **Meta** | **Contemplating** | **多 Agent 并行** | HLE **58%** 官方博客 | Muse **preview** |
| **Alibaba** | Qwen thinking | — | GPQA **~90%** 档 | 国内合规 |

**成稿 TLDR**：「**同厂 chat 分 ≠ thinking 分**——API 模型名与 **reasoning 开关** 须写清。」

---

## GPQA vs HLE vs ARC · 分工表（成稿块）

| 基准 | 题面 | 饱和度（2026 叙事） | 测什么 | 不测什么 |
|------|------|---------------------|--------|----------|
| **GPQA Diamond** | 专家级 MCQ | 前排 **<2pt** | 科学难题选择题 | 代码仓库、奥数速算 |
| **HLE** | 封闭学术题（定义见 hub） | tail **仍有区分** | 高难度知识+推理；**with tools** 子集 | 人类偏好、工程 patch |
| **ARC-AGI-2** | 少样本格子抽象 | 头部 **低分** | 规则归纳 | 博学 MCQ |
| **MMLU-Pro** | 通识 MCQ+干扰 | 中等饱和 | 知识 | 多步工程推理 |

**HLE 完整定义**：仅 [llm.md §词汇锚点](./llm.md)——本页只谈 **with tools / no tools** 与 **Contemplating** 对照。

---

## Contemplating vs o-series vs R1（成稿块）

| 维度 | **Contemplating（Muse）** | **o 系 / Extended Thinking** | **R1 类（DeepSeek 等）** |
|------|---------------------------|------------------------------|---------------------------|
| **架构叙事** | 多 Agent 并行 | 单模型长思考 | 单模型+可见 CoT |
| **官方 HLE 信号** | **58%**（博客） | 随 SKU 变 | 公开 GPQA 强、HLE 见第三方 |
| **延迟** | 很高 | 高 | 中–高 |
| **可用性** | API preview | 全面 API | 开源+API |
| **成稿提示** | 勿与 o 系 **百分数直比**——harness 不同 | — | — |

---

## 企业场景 · 推理轴（成稿块）

| 场景 | 基准组合 | SKU 建议 | 风险 |
|------|----------|----------|------|
| 医学文献综述 | GPQA + **领域 RAG** | Thinking 批处理 | 幻觉 **高 stakes** |
| 法律条款推理 | 自建逻辑题 + GPQA | Thinking + 引用溯源 | CoT 不可作法律依据 |
| 科研 hypothesis | HLE 子集 + 内部题 | Contemplating **若可接入** | preview 不可用则 Opus/o |
| 抽象规则引擎 | ARC 类内部集 | Refinement loop 试跑 | GPQA **弱预测** |
| 客服复杂投诉 | **默认 chat** | 仅 escalations 开 Thinking | 成本失控 |

---

## 常见误读 FAQ（推理轴 · 成稿块）

| 误读 | 纠正 |
|------|------|
| 「GPQA 第一 = 推理 AGI」 | GPQA **趋饱和**——看 HLE/ARC tail |
| 「HLE 一个分 = 所有 HLE 子集」 | **with tools / 多模态 / 纯文本** 分列 |
| 「ARC 5% = 模型很笨」 | ARC-2 **设计难**；harness 可 **10×** 分差 |
| 「MMLU 高 = GPQA 高」 | 知识 **≠** 专家难题推理 |
| 「Thinking 永远值得开」 | **$/call** 可差 10–100× |
| 「Contemplating HLE 58% = 可采购同等能力」 | Muse **API 未全面开放** |
| 「推理强 = 数学竞赛强」 | 见 [llm-for-math.md](./llm-for-math.md) |
| 「推理强 = 代码 SWE 强」 | 见 [llm-for-coding.md](./llm-for-coding.md) |

---

## 风险 · 合规 · 治理（推理轴特有）

- **推理成本不可见**：同 90% 分可能差 **10–100× $/call**——须对照定价。
- **思考链不透明**：CoT 可能对用户不可见——安全对齐与透明性张力。
- **任务特异性**：GPQA 高 ≠ ARC-AGI 高——按任务选基准。

共享治理见 [llm.md](./llm.md) §风险 · 合规 · 治理。

---

## 工具与产品类型（评测基准）

| 基准类型 | 代表基准 | 特点 |
|---------|---------|------|
| 博士级推理 | GPQA Diamond, Humanity's Last Exam | 专家级难度 |
| 抽象推理 | ARC-AGI-2, Abstraction and Reasoning Corpus | 视觉+逻辑 |
| 长上下文推理 | BABILong, RULER | 跨段落推理 |
| 测试时推理 | AIME with TTC, SWE-bench (extended) | 思维链扩展 |

### 对比与测评（第三方；观点非官方）

2026 年中推理 LLM 共识：GPT-5 Pro Max 在 HLE 与 GPQA 领先；Claude 4 Opus 在 ARC-AGI-2 展现抽象推理优势；Thinking/Reasoning 模式（o-series 风格）从高端模型向中端渗透（Gemini 3 Pro Thinking、Claude 3.5 Extended Thinking）。测试时计算扩展（TTS）在数学证明任务中收益显著。实时排行见 [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md)。

---

## 外链索引

| 名称 | URL |
|------|-----|
| ARC-AGI-2 | [arXiv:2505.11831](https://arxiv.org/abs/2505.11831) |
| BenchLM · GPQA | [benchlm.ai/benchmarks/gpqa](https://benchlm.ai/benchmarks/gpqa) |
| HLE | [agi.safe.ai](https://agi.safe.ai/) |
| Muse Spark 博客 | [ai.meta.com/blog/introducing-muse-spark-msl/](https://ai.meta.com/blog/introducing-muse-spark-msl/) |

---

## 延伸阅读

- [llm.md](./llm.md) · [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md) · [llm-for-math.md](./llm-for-math.md)
