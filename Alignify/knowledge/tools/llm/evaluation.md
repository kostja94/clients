# AI Evaluation / AI 模型评测 · 知识块（非线性笔记）

**叙述主词**：**AI evaluation / LLM evaluation / AI 评测**（对 AI 模型或 AI 应用输出进行系统性质量评估的工具与平台——覆盖离线评测、在线监控、人工审核、CI/CD 集成的完整评测生命周期）。与 **LLM 基准评测**（`llm`、`llm-for-coding`、`llm-for-reasoning`）相邻但**不同维度**——本页讨论的是**"你用什么工具来评测你自己的 AI 应用"**，而非"各模型的 Arena Elo 排行榜"。

**材料范围**：公开网络检索（厂商产品页、行业评测、开发者社区讨论与对比文）；**未**将 Alignify 站内 Tools 正文 JSON 当作独立事实来源复述。网摘整理日期 **2026-05-13**。

**站内对照**：[alignify.co/tools/evaluation](https://alignify.co/tools/evaluation) · [alignify.co/zh/tools/evaluation](https://alignify.co/zh/tools/evaluation) · `/tools/evaluation` · `/zh/tools/evaluation` · `content/tools/zh/evaluation.md`、`content/tools/en/evaluation.md` · slug **`evaluation`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#evaluation-tools`](../../keywords/alignify-keywords-tools.md#evaluation-tools)

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`evaluation`（本页）** | **`llm` / `llm-for-coding` / `llm-for-reasoning`** |
|------|--------------------------|---------------------------------------------------|
| **典型买家问题** | 用什么工具系统化评测我的 AI 应用/Agent？ | GPT-5 和 Claude-5 哪个编程更强？ |
| **用户角色** | AI 工程师、MLOps、QA | 技术选型者、CTO、开发者个人 |
| **评测对象** | 你自己的 AI 应用/Agent/流水线 | OpenAI、Anthropic、Google 等厂商的公有模型 |
| **交付形态** | SDK + SaaS 平台，离线+在线一体 | 排行榜、基准论文、第三方评测站 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **LLM evaluation / 大模型评测**：使用预定义的指标（准确性、流畅度、事实一致性、安全性等）对 LLM 输出进行打分。可用**代码规则**（如正则匹配）、**训练模型**（分类器/嵌入相似度）、或 **LLM-as-judge**（用另一个 LLM 打分）实现。
- **LLM-as-judge（LLM 当裁判）**：用一个（通常更强的）LLM 对目标 LLM 的输出打分。优势是灵活——可评估「品牌语调」「逻辑连贯性」等主观维度；代价是成本（调用费）和可靠性（裁判 LLM 本身有偏见与随机性）。
- **Offline evaluation（离线评测）**：在部署前用静态数据集跑模型输出并打分——类似软件工程的单元测试/集成测试。核心产物是**评分报告**与**通过/不通过门禁**。
- **Online evaluation / production monitoring（在线评测/生产监控）**：在应用上线后持续采集真实用户交互、检测质量退化（如幻觉率上升、安全违规）。核心产物是**告警**与**趋势仪表盘**。
- **Autorater（自动评分器）**：预定义的评测规则或模型，可自动对输出打分——无需人工逐条审阅。Google Stax 预置了流畅度、事实一致性、安全性、指令遵循、简洁度五类 autorater。
- **Golden dataset / 评测基准集**：一组经人工标注的「标准答案」输入输出对，用于衡量模型或应用在新版本上是否退化。是离线评测的核心资产。
- **Trace / span**：一次 AI 调用的完整记录（输入→中间步骤→最终输出→评分）。Braintrust、LangSmith 等平台以 trace 为基本单位构建评测数据集。
- **Red teaming / 红队测试**：系统性探测 AI 应用的安全漏洞——越狱、提示注入、偏见输出、PII 泄露等。DeepEval 和 Galileo 提供自动化红队检测器。

---

## 专题对照 / 扩展定义

| 维度 | **离线评测（Pre-deploy）** | **在线监控（Post-deploy）** |
|------|---------------------------|----------------------------|
| **时机** | 部署前 | 上线后持续运行 |
| **数据来源** | 人工构建的数据集 / 合成数据 | 真实用户交互 |
| **核心问题** | 「新版本比旧版本更好吗？」 | 「现在线上质量在下降吗？」 |
| **代表性工具** | DeepEval、OpenAI Evals、Stax | LangSmith、Galileo、Braintrust |

| 维度 | **通用评测框架** | **RAG 专项评测** | **Agent 专项评测** |
|------|-----------------|-----------------|-------------------|
| **评测重点** | 单轮输出质量 | 检索质量 + 生成忠实度 | 多轮工具调用、目标达成率 |
| **代表性工具** | DeepEval、Stax、Braintrust | Ragas | LangWatch、Latitude |

---

## 问题域（为何会出现这类产品）

- **从「vibe check」到系统化评测**：早期 AI 应用开发依赖开发者「凭感觉」判断输出好不好。随着应用从原型走向生产，主观判断无法复现、无法规模化——评测工具填补了从「feel」到「metric」的鸿沟。Google Stax 的口号"Stop vibe testing your LLMs"精准概括了这一动力。
- **LLM 的非确定性**：同一 prompt 在不同时间、不同模型版本下输出不同——传统软件测试的「期望输出 = 实际输出」模式失效。需要专门设计的评测方法论（语义相似度 vs 精确匹配、LLM-as-judge 等）。
- **Agent 的复杂性爆炸**：当 AI 从单次问答扩展到多步工具调用 Agent，评测难度指数级上升——不仅要测「最终答案对不对」，还要测「中间每一步的工具选择是否合理」。
- **CI/CD 的左移需求**：软件工程最佳实践要求「在合并前发现问题」。DeepEval 的 pytest 风格 API 让 AI 评测可嵌入 GitHub Actions——在 PR 阶段就拦住退化。
- **成本与速度的平衡**：用 GPT-4 当裁判评测每一笔生产流量成本过高。Galileo 的 Luna 蒸馏模型（<200ms, 低成本）代表了「专用评测模型替代通用 LLM 当裁判」的趋势。
- **Regulation 压力**：EU AI Act、中国深度合成管理规定等对 AI 系统提出可审计的质量与安全要求——评测工具成为合规基础设施。

---

## 能力栈（概念拆分，非厂商功能表）

- **数据集管理**：构建、导入（CSV/JSONL）、版本管理评测数据集。部分平台支持 LLM 自动生成合成测试数据。
- **评分器（Scorer / Evaluator）**：代码规则（regex、长度检查）、训练模型（分类器、NLI 模型）、LLM-as-judge（用 GPT/Claude 打分）。可组合使用。
- **对比评测（A/B / side-by-side）**：两个模型或 prompt 在同一数据集上跑，输出统计显著性对比。Stax 和 Braintrust 在此维度突出。
- **CI/CD 集成**：pytest 插件（DeepEval）、GitHub Action（Braintrust）、CLI（OpenAI Evals）——将评测嵌入开发流水线。
- **生产追踪与监控**：自动采集生产流量、在线评分、设置告警阈值。LangSmith 和 Galileo 在此最强。
- **人工审核工作流**：对自动评分不确定的样本路由到人工评审队列。LangSmith（标注队列）和 Braintrust（Kanban 审查 UI）提供。
- **Prompt 管理**：将 prompt 版本化并与评测结果关联——知道「哪个 prompt 版本通过了哪些评测」。Braintrust 和 LangSmith 的 Prompt Hub 覆盖此层。

---

## 形态谱系（与具体品牌解耦）

- **开源评测框架**：以代码库形式提供，需自行部署与集成。DeepEval（pytest 风格）、OpenAI Evals（YAML 基准）、Ragas（RAG 专项）为代表。适合自建管线的工程团队。
- **一体化评测平台（SaaS）**：从数据管理→离线评测→在线监控→人工审核的闭环。Braintrust、LangSmith、LangWatch 为代表。适合需要完整工作流的中大型团队。
- **评测优先的可观测性平台**：以生产监控为核心，通过专用模型（如 Galileo Luna）降低评测成本。Galileo 为代表。
- **实验性质开发者工具**：Google Stax 为典型——免费的 Web 工具，面向个人开发者和小团队快速上手评测，预置 autorater 降低入门门槛。目前仍在 beta 阶段。
- **RAG 专项评测库**：Ragas 为行业标准——聚焦检索增强生成管线的组件级评测（检索质量 vs 生成质量）。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **评测本身的偏差**：LLM-as-judge 存在位置偏差（偏好第一个选项）、长度偏差（偏好更长输出）、风格偏差——评测工具的选择会影响「什么是好」的定义。
- **数据隐私**：将用户交互数据发送到评测平台的隐私风险——需审查各平台的 DPA、数据驻留、是否将评测数据用于训练。
- **评测的完备性幻觉**：高自动评分 ≠ 真实用户满意。评测工具覆盖已知维度，但用户可能在意工具未测的维度（如语气、文化适配性）。
- **Agent 评测的「奖励黑客」**：Agent 可能学到「让评分器高分」而非「完成真实任务」的策略——需要多维度交叉验证而非单指标优化。

---

## 落地碎片（无先后）

- 从小做起：先建 20–50 条人工标注的 golden dataset，再引入自动评分器。不要一上来就追求覆盖所有维度。
- CI/CD 集成从「门禁」开始：在 PR 合并前跑 5–10 个核心评测（幻觉、安全性、任务完成率），先拦住明显退化。
- 评测体系需要分层：代码规则（快速、便宜）→ LLM-as-judge（灵活）→ 人工抽检（兜底）——三层递进，按成本-收益分配。
- RAG 应用优先引入 Ragas：它是 RAG 评测的事实标准，Context Precision + Faithfulness 两个指标已经能覆盖大部分质量问题。
- 生产监控不要只看平均值：关注 P99 延迟、最差 5% 输出、特定用户群组（如非英语用户）的分层指标。
- Google Stax 适合快速入门（免费、Web UI、预置 autorater），DeepEval 适合已有 pytest 管线的团队，Braintrust 适合需要完整评测→优化闭环的中大型团队。

---

## 工具与产品类型（「LLM evaluation」「AI testing」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **Open-source eval framework** | 代码库/CLI，需自行集成 | DeepEval、OpenAI Evals、Ragas |
| **Full-cycle eval platform (SaaS)** | 离线+在线+人工+Prompt 管理一体化 | Braintrust、LangSmith、LangWatch |
| **Eval-first observability** | 生产监控为主，专用评分模型 | Galileo、Arize AX |
| **Experimental / lightweight eval** | 免费 Web 工具，预置 autorater | Google Stax（beta） |
| **RAG-specialized eval** | 检索+生成组件级评测 | Ragas（行业标准） |

---

## 外链索引（术语与官方动态；外链；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Google Stax** | 实验性 LLM 评测工具包，预置流畅度/事实一致性/安全性/指令遵循/简洁度五类 autorater，支持多模型对比（Gemini/GPT/Claude/Grok/DeepSeek）与自定义评分器，免费 beta | [stax.withgoogle.com](https://stax.withgoogle.com/) |
| **Braintrust** | 最完整的一体化评测平台——离线评测+在线评分+Prompt 管理+数据集管理+AI 优化 Agent（Loop），免费层 1M spans/月，Notion/Stripe/Vercel 等使用 | [braintrust.dev](https://www.braintrust.dev/) |
| **DeepEval**（Confident AI） | 开源 pytest 风格评测框架，50+ 指标含幻觉/偏见/毒性检测，CI/CD 原生集成，红队测试支持 | [github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval) |
| **LangSmith**（LangChain） | LangChain/LangGraph 生态的原生评测与可观测性平台——一行环境变量即可全链路追踪，Prompt Hub + 人工标注队列 | [smith.langchain.com](https://smith.langchain.com/) |
| **Galileo** | 评测优先的生产可观测性平台，Luna 蒸馏模型实现低成本（<200ms）幻觉/提示注入/PII 检测，支持实时 guardrail | [rungalileo.io](https://www.rungalileo.io/) |
| **Ragas** | RAG 评测的事实标准开源库——Context Precision、Context Recall、Faithfulness 等组件级指标，正在扩展 Agent 评测 | [github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas) |
| **OpenAI Evals** | OpenAI 官方开源评测框架，YAML 定义基准，GPT-4 为裁判，内置 QA/推理/代码/内容过滤等预置评测集 | [github.com/openai/evals](https://github.com/openai/evals) |
| **LangWatch** | 一体化评测+可观测性平台，Agent 专项评测（工具调用准确率、目标达成率），重视隐私与安全合规 | [langwatch.ai](https://langwatch.ai/) |
| **Latitude** | Agent 评测平台，CTO 向，强调多轮 Agent 工具调用评测与生产级对比 | [latitude.so](https://latitude.so/) |

### 对比与测评（第三方；观点非官方）

2025–2026 年开发者社区对 AI 评测工具的共识：没有「全家桶」能覆盖所有场景。技术选型的分水岭是「你更需要离线 CI/CD 评测」还是「生产监控」。需要 CI/CD 的门禁用 DeepEval（pytest 原生）或 Braintrust（自带 GitHub Action）；需要生产监控看 Galileo（Luna 低成本）或 LangSmith（LangChain 生态无缝）；做 RAG 评测 Ragas 是必选项。Braintrust 的完整闭环（离线→在线→优化 Agent）在 Notion（70 AI 工程师）、Stripe 等中型团队中口碑最强。Google Stax 适合个人开发者和小团队快速上手，但目前仍在 beta 阶段且功能范围有限。核心趋势：从拼凑 3–4 个独立工具转向一体化平台，Agent-native 评测（多轮、工具使用感知）是 2026 年的架构分水岭。*本小节为网摘综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- **站内相邻知识块**：[llm.md](llm.md)（通用大模型评测——Arena Elo/MMLU 排行榜）、[llm-for-coding.md](llm-for-coding.md)（代码模型评测——SWE-bench/LiveCodeBench）、[llm-for-reasoning.md](llm-for-reasoning.md)（推理模型评测——GPQA/HLE/ARC-AGI-2）。
- **行业事件**：2025 年 3 月 CoreWeave 以 ~$1.4B 收购 Weights & Biases；2025 年 8 月 Anthropic 收购 Humanloop。
- **市场数据**：AI 模型评测平台市场从 2025 年 $1.86B 增长至 2026 年 $2.36B（CAGR 27.3%），预计 2030 年达 $6.24B。
- **Alignify Tools 正文**：产品清单与选型步骤以线上 `/zh/tools/evaluation` 为准；本知识块**不**替代站内长文教程，仅作概念索引与外链锚点。