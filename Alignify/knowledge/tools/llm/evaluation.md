# AI Evaluation / LLM 应用评测 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI evaluation / LLM evaluation / AI 应用评测**——对 **你自己的** AI/Agent 应用输出与轨迹 **系统性打分**（offline dataset、online scorer、LLM-as-judge、CI gate、guardrail、人工审核）；验收以 **能否定义「好」、能否回归、能否挡发布** 为主。本页为 **Eval / Scorer / Quality gate SSOT**。**不是** trace/cost/prompt 运维（→ [llm-observability.md](llm-observability.md)）；**不是**公开模型 Arena/MMLU/SWE 榜（→ [llm.md](llm.md) 五轴）。

**材料范围**：公开网络检索（Braintrust、DeepEval、Ragas、Promptfoo、Patronus、Galileo、OpenAI Evals、Google Stax 等官方与社区材料）；**未**将 Alignify 站内 Tools 正文 JSON 当作独立事实来源。网摘整理日期 **2026-09-03**（自原稿拆分 obs 边界）。

**站内对照**：[alignify.co/tools/evaluation](https://alignify.co/tools/evaluation) · [alignify.co/zh/tools/evaluation](https://alignify.co/zh/tools/evaluation) · `/tools/evaluation` · `/zh/tools/evaluation` · slug **`evaluation`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) · 锚点 [`#evaluation-tools`](../../keywords/alignify-keywords-tools.md#evaluation-tools)

## 与相邻 slug 分流

| 维度 | **`evaluation`（本页）** | **`llm-observability`** | **`llm` 五轴** |
|------|--------------------------|-------------------------|----------------|
| **典型买家问题** | 用什么 **打分/挡发布**？ | 用什么 **看清线上发生了什么**？ | 哪个 **公开模型** 更强？ |
| **用户角色** | AI 工程师、QA、MLOps（质量） | 平台工程师、SRE（运行态） | 选型者、研究者 |
| **核心单元** | Scorer / dataset / experiment | Trace / span / session | Benchmark 行 |
| **交付形态** | 框架、CLI、eval-first SaaS | Obs-first SaaS、OTel 后端 | 排行榜、论文 |
| **验收核心** | 分数、回归、guardrail 通过 | 全链路可见、成本归因 | Elo、SWE-bench 等 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **LLM evaluation / 应用评测**：对 **你的应用** 输出按 rubric 打分——非公开模型榜。实现：**代码规则**、**训练分类器**、**LLM-as-judge**、**专用 Judge 模型**（Patronus/Galileo Luna）。
- **LLM-as-judge**：用 LLM 按自然语言 rubric 打分；灵活但存在位置/长度/风格偏差——需与 human calibrate。
- **Offline evaluation**：部署前对 **golden dataset** 跑 task + scorer——类似单元/集成测试；产物 **报告 + pass/fail**。
- **Online evaluation / online scoring**：对 **生产 trace 采样** 异步 scorer——无 ground truth 时依赖 judge；与 obs **共用 trace**（→ [llm-observability.md](llm-observability.md)）。
- **Scorer / Evaluator / Autorater**：打分函数或模型；Google Stax 预置五类 autorater（流畅度、事实性等）。
- **Golden dataset**：人工或策展的 input（+ optional expected output）集合——离线 eval 核心资产；常从 **失败 trace promote**（obs → eval 接缝）。
- **Trajectory eval（Agent）**：评 **多步 tool 路径 + 任务完成度**，非单轮 IO——单元是 trace/trajectory。
- **Red teaming**：越狱、注入、PII、毒性等对抗探测——DeepEval、Galileo 等。

---

## 专题对照

| 维度 | **离线（Pre-deploy）** | **在线（Post-deploy）** |
|------|------------------------|-------------------------|
| **时机** | 合并前 / 发布前 | 上线后持续 |
| **数据** | Golden dataset / 合成 | 生产 trace 采样 |
| **核心问题** | 新版是否退化？ | 质量是否在 drift？ |
| **代表** | DeepEval、Promptfoo、Braintrust experiment | Online scorer、Galileo guardrail |

| 维度 | **通用 eval** | **RAG 专项** | **Agent 专项** |
|------|--------------|-------------|----------------|
| **重点** | 单轮质量、格式、安全 | 检索 + faithfulness | tool 正确性、task completion |
| **代表** | DeepEval、Stax、Braintrust | **Ragas** | Latitude、LangWatch（eval 维）、Maxim |

### 与 llm-observability 的接缝（SSOT 分工）

| 能力 | 主 KB |
|------|--------|
| Trace ingest / cost 仪表盘 | **llm-observability** |
| Dataset / scorer / CI gate / Judge API | **evaluation（本文）** |
| Prompt 版本 **runtime** | llm-observability |
| Prompt **A/B 实验与 score 对比** | **evaluation** |
| 失败 trace → dataset row | 两页互链；操作在 obs UI，**rubric 在 eval** |

---

## 问题域

- **从 vibe check 到 metric**：Google Stax「Stop vibe testing your LLMs」——可复现质量门禁。
- **非确定性输出**：精确 match 失效 → 语义相似度、LLM-as-judge、trajectory eval。
- **Agent 复杂度**：需评 **路径 + 终局**；组件 eval（retrieval）与 E2E 互补。
- **CI/CD 左移**：DeepEval pytest、Promptfoo exit code、Braintrust GitHub Action——PR 挡退化。
- **Judge 成本**：Galileo **Luna**、Patronus **Lynx/Glider** 等 **专用模型** 降本 vs GPT-4 judge。
- **合规**：EU AI Act 等要求 **可审计质量证据**——eval 记录 + trace 归因（obs 存证）。

---

## 能力栈

- **Dataset 管理**：版本、CSV/JSONL、从生产 promote、合成生成。
- **Scorer 组合**：deterministic + LLM-judge + 专用 classifier；Ragas 组件 metric。
- **Experiment / 对比**：side-by-side、统计显著性、row-level diff（Braintrust 强项）。
- **CI/CD 集成**：pytest（DeepEval）、YAML CLI（Promptfoo）、GitHub Action（Braintrust）。
- **Online scoring & guardrail**：采样生产 trace；实时 block（Galileo Protect、Patronus API）。
- **Human-in-the-loop**：标注队列、审查 UI——低置信样本人工定标。
- **红队与安全 eval**：对抗数据集、自动化 probe。

**不在本页展开**：trace 存储架构、OTel exporter、token 仪表盘 → [llm-observability.md](llm-observability.md)。

---

## 形态谱系

| 形态 | 特征 | 代表 |
|------|------|------|
| **开源 eval 框架/CLI** | 代码/配置即 eval；无 dashboard 或轻量 | DeepEval、Promptfoo、Ragas、OpenAI Evals |
| **Eval-first SaaS** | Experiment、CI gate、online scorer 一体 | **Braintrust**、Confident AI（DeepEval 云） |
| **Judge / Guardrail-first** | 专用 Judge 模型 + 合规 | **Patronus**、**Galileo** |
| **轻量实验工具** | Web UI、预置 autorater | Google **Stax**（beta） |
| **Agent eval 专品** | 多轮、仿真 | **Latitude**、Maxim（观察） |
| **Obs-first 带 eval** | 主榜在 obs | Langfuse/LangSmith — **仅互链** [llm-observability.md](llm-observability.md) |

---

## 代表产品（主榜 · 2026-09）

> Langfuse、LangSmith、Helicone、Datadog LLM Obs 等 **Obs 主榜** 见 [llm-observability.md](llm-observability.md)。

| 名称 | 形态 | 一句话 | URL |
|------|------|--------|-----|
| **Braintrust** | Eval-first SaaS | Dataset + scorer + **Eval()** 实验 + CI gate + online scoring；**Autoevals** OSS | [braintrust.dev](https://www.braintrust.dev/) |
| **DeepEval** | OSS + Confident AI 云 | **pytest 风格**；50+ metric；红队 | [github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval) |
| **Promptfoo** | OSS CLI | YAML 断言、模型/prompt 矩阵、**CI exit code**；2026 OpenAI 收购叙事 | [promptfoo.dev](https://www.promptfoo.dev/) |
| **Ragas** | OSS 库 | **RAG 事实标准** metric；扩展 Agent | [github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas) |
| **Patronus AI** | Judge SaaS | **Lynx/Glider** 等 Judge；幻觉/合规；API 一行接入 | [patronus.ai](https://www.patronus.ai/) |
| **Galileo** | Eval + guardrail | **Luna** 低成本 judge；生产 guardrail | [galileo.ai](https://galileo.ai/) |
| **Google Stax** | 实验 Web | 预置 autorater；多模型对比 beta | [stax.withgoogle.com](https://stax.withgoogle.com/) |
| **OpenAI Evals** | OSS | YAML benchmark；GPT judge | [github.com/openai/evals](https://github.com/openai/evals) |
| **Latitude** | Agent eval | 多轮 Agent 对比、CTO 向 | [latitude.so](https://latitude.so/) |

---

## 风险 · 合规 · 治理

- **Judge 偏差**：LLM-as-judge 的 position/length bias——需 human 校准集。
- **数据隐私**：dataset 与 production sample 含 PII——DPA、脱敏、驻留。
- **完备性幻觉**：高 auto score ≠ 用户满意；需分层 + 人工抽检。
- **Reward hacking（Agent）**：优化 scorer 而非任务——多 metric + E2E。
- **Promptfoo 收购后**：OpenAI 收购（2026 报道）——多 vendor 团队关注 **vendor-neutral** CLI 备选（DeepEval/Ragas）。

---

## 落地碎片

- 先 **20–50 条 golden dataset**，再加 auto scorer；勿追求全覆盖。
- CI 从 **5–10 条核心 metric** 挡 PR：幻觉、安全、任务完成。
- 分层：**规则（快）→ LLM-judge（灵）→ 人工（兜底）**。
- RAG：**Ragas** Context Precision + Faithfulness 优先。
- **Obs + Eval 组合**：Langfuse/Phoenix **trace** + DeepEval/Promptfoo **gate** 为常见开源组合；详见 [llm-observability.md](llm-observability.md)。
- Braintrust：要 **eval 驱动发布** 且接受 SaaS 定价（Pro **$249/mo** 档，2026 官网）时优先。

---

## 工具类型速查

| 类型 | 代表 |
|------|------|
| OSS framework / CLI | DeepEval、Promptfoo、Ragas、OpenAI Evals |
| Eval-first platform | Braintrust、Confident AI |
| Judge / guardrail | Patronus、Galileo |
| Lightweight / beta | Google Stax |
| RAG library | Ragas |
| Agent eval | Latitude |

---

## 对比与测评（第三方 · 非 Alignify 实测）

2025–2026 社区共识：**Obs 与 Eval 正交但需闭环**。CI 门禁优先 **Promptfoo**（零 glue exit code）或 **DeepEval**（pytest 团队）；完整 experiment 工作流 **Braintrust**；RAG 必 **Ragas**；强监管幻觉 **Patronus/Galileo**。生产 **trace** 选型见 [llm-observability.md](llm-observability.md)（Langfuse vs LangSmith 等）。*网摘综合。*

---

## 延伸阅读 · 站内外

**站内**

- [llm-observability.md](llm-observability.md) — **Trace / cost / prompt runtime / OTel**；与本页 **score-on-trace** 接缝
- [llm.md](llm.md) · [llm-for-coding.md](llm-for-coding.md) · [llm-for-reasoning.md](llm-for-reasoning.md) — **公开模型榜**
- [agent-runtime.md](../agent/agent-runtime.md) — Agent **trajectory eval** 与 runtime 观测分工
- [ai-training-data.md](../infrastructure/ai-training-data.md) — 训前 rubric 与训后 eval 对齐

**站外 · 行业**

- 2025-03 CoreWeave ~$1.4B 收购 W&B；2025-08 Anthropic 收购 Humanloop
- 应用 eval/obs 市场与公开 **模型评测** 市场口径不同——勿混引 CAGR

**Alignify 正式页**：产品清单以 `/zh/tools/evaluation` 为准；本 KB **不**替代长文教程。
