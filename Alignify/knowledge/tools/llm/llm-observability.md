# LLM 可观测性 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**LLM Observability / LLM Tracing / AI 应用可观测性**——LLM 与 Agent 应用在**运行时**的 trace、span、session、token/cost、latency、prompt 版本、告警与 debug；验收以 **能否还原一次请求的完整上下文、定位慢/贵/错在哪一步** 为主。本页为 **Obs-first 平台与 OTel  instrumentation SSOT**（完整 URL 表仅此一处）。**不是**「输出好不好、能否挡发布」（→ [evaluation.md](evaluation.md)）；**不是**「公开模型 Arena/MMLU 榜」（→ [llm.md](llm.md)）；**不是**「统一 API 路由」（→ [api.md](../infrastructure/api.md)）；**不是**「GPU 推理部署」（→ [inference-infrastructure.md](../infrastructure/inference-infrastructure.md)）。

**材料范围**：公开网络检索（Langfuse、LangSmith、Arize Phoenix、Helicone、Datadog、Traceloop、Opik、LangWatch 官方文档；ClickHouse 收购公告；OpenInference/OTel GenAI 语义约定索引）；**未**引用 Alignify 站内 Tools 正文 JSON。**定价与 GA 以各官网为准**。网摘整理日期 **2026-09-03**。

**站内对照**：slug **`llm-observability`** · KB only（发文走 `/blog/llm-observability`）

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) · `keywordEn`: **LLM Observability** · `keywordZh`: **LLM 可观测性**（辅：**LLM Tracing**、**AI Observability**）

## 与相邻 slug 分流

| 维度 | **llm-observability（本文）** | **evaluation** | **`llm` 五轴** | **api** | **agent-runtime** | **agent-memory** |
|------|------------------------------|----------------|--------------|---------|-------------------|------------------|
| 核心问题 | **发生了什么**、为何慢/贵、哪步错 | **好不好**、能否 ship、是否退化 | **哪个公开模型更强** | **怎么调用多模型** | **Agent 怎么可靠跑** | **Agent 记住什么** |
| 评测单元 | **Trace / span / session** | Scorer / dataset / CI gate | Benchmark 行 | API 请求 | Agent loop / 工作流 | 记忆状态 |
| 典型读者 | AI 平台工程师、SRE、MLOps | AI 工程师、QA | 选型者、研究者 | 后端/全栈 | Agent 平台工程师 | Agent 应用开发者 |
| 验收核心 | 全链路可见、成本归因、prompt 版本 | 分数、回归、guardrail | Elo / SWE-bench 等 | 延迟、路由、配额 | 耐久性、HITL | 检索准确 |
| 开源自托管 | Langfuse MIT、Phoenix、Opik | DeepEval、Ragas、Promptfoo | — | LiteLLM 等 | 部分 runtime OSS | Mem0 等 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **LLM Observability / 可观测性**：对 LLM 应用运行态的 **trace + metrics + logs** 组合理解——含 prompt/completion、tool call、retrieval、token、latency、cost；**不等于**仅 APM 错误率（传统 APM 弱于 prompt 版本与 eval score 语义）。
- **Trace / Span / Observation**：一次用户请求为 **trace**；其内 LLM 调用、tool、retrieval 为 **span/observation**；Agent 场景为 **树/图** 而非单条 log。
- **Session**：多轮对话/thread 的聚合单位——chatbot 体验以 session 为界，非单次 completion。
- **Generation**：一次模型调用记录（input tokens、output tokens、model id、latency）——Langfuse 等平台的计费 **unit** 常含 trace + observation + **score**。
- **OpenTelemetry（OTel）**：可移植 telemetry 标准；**OTel GenAI** 与 **OpenInference** 语义约定使 trace 可进 Datadog/Jaeger 或 LLM 专用后端。
- **Prompt management（运维向）**：prompt **版本、label、runtime fetch、缓存**——与 eval 的「prompt A/B 实验」衔接，但本页 SSOT 在 **部署与监控** 侧。
- **Tail sampling**：高流量下仅保留失败/慢请求/full trace 子集——控制 obs 成本。
- **Eval score on trace**： scorer 产出的分数 **写回 span**（OpenInference `evaluations.*`）——Obs 与 Eval 的 **接缝**； scorer 定义见 [evaluation.md](evaluation.md)。

---

## 专题对照

### Observability vs Evaluation vs 公开模型榜

| 问句 | 看哪块 |
|------|--------|
| 这次请求 **调了哪些 tool、花了多少 token**？ | **llm-observability（本文）** |
| 这次输出 **是否幻觉、能否过 CI gate**？ | [evaluation.md](evaluation.md) |
| **GPT vs Claude** 在 SWE-bench 谁高？ | [llm.md](llm.md) 五轴 |

### Offline trace replay vs Online monitoring

| 维度 | **Online（生产）** | **Offline（开发/排障）** |
|------|-------------------|-------------------------|
| 数据来源 | 实时 ingest | 历史 trace 导出 / 采样 replay |
| 核心用途 | 告警、成本、退化发现 | Debug、策展进 dataset |
| 与 eval 衔接 | Online scorer 采样 | 失败 trace → golden row |

### Lane 谱系（Obs 视角）

| Lane | 特征 | 代表（规格见 §外链） |
|------|------|---------------------|
| **L1 — OSS self-host** | MIT/Apache；ClickHouse/Postgres 栈；数据主权 | **Langfuse**、Arize **Phoenix**、Comet **Opik** |
| **L2 — Framework-tied** | 与 LangChain/LangGraph 零配置 | **LangSmith** |
| **L3 — APM 延伸** | 已有 Datadog/New Relic，补 LLM 语义 | **Datadog LLM Observability** |
| **L4 — Gateway + Obs** | 代理多模型 API，顺带记 log | **Helicone**（与 [api.md](../infrastructure/api.md) 分流） |
| **L5 — OTel-native SaaS** | 托管 + 深度 eval 套件 | Arize **AX**（eval 亦强 → 互链 evaluation） |
| **L6 — Eval-first（对照）** | 以 experiment 为中心，trace 服务 eval | **Braintrust** — **主榜在** [evaluation.md](evaluation.md) |

---

## 问题域

- **非确定性与 silent failure**：200 OK 但答案错、RAG 检索偏了——无 trace 只能猜。
- **Agent 多步爆炸**：单请求 N 次 LLM + M 次 tool；传统 logging 丢因果链。
- **成本静默泄漏**：token 按 user/session/feature 不可见则无法优化。
- **Prompt 版本漂移**：生产跑 v3、文档写 v5——需 prompt registry 与 trace 绑定。
- **Vendor 与收购**：Langfuse（2026-01 **ClickHouse 收购**，仍 MIT OSS）；买家需看 cloud vs self-host roadmap。
- **Obs 同质化、Eval 分化**：2026 行业共识——**纯 trace UI 趋同**，差异化在 **eval 闭环**（→ evaluation 页）。

---

## 能力栈

- **Instrumentation**：SDK（Python/JS）、框架集成（LangChain、OpenAI SDK）、OTel exporter、proxy（LiteLLM/Helicone）。
- **Ingest & storage**：高吞吐写（常 **ClickHouse** 类列存）；保留策略与 PII 脱敏。
- **Query UI**：trace 树、agent graph、session 视图、按 user/metadata 过滤。
- **Cost & latency analytics**：按 model、prompt version、feature 聚合。
- **Prompt management**：版本、label、playground、runtime serve。
- **Alerting**：延迟/成本/错误率阈值；部分平台支持 **eval score** 告警（与 evaluation 重叠）。
- **Trace → dataset**：将生产失败样本 **promote** 为 eval 用例——接缝能力；dataset/scorer 细节 → evaluation。

---

## 代表产品（主榜 · 2026-09）

> **非排名**；Braintrust / Patronus / Galileo 等 **eval-first** 见 [evaluation.md](evaluation.md)。

| 产品 | Lane | 一句话 | 备注 |
|------|------|--------|------|
| **Langfuse** | L1 | OSS **LLM 工程平台**（trace + prompt + eval 钩子）；2026 起隶属 ClickHouse，仍 MIT 自托管 | 品牌搜索量在品类内领先（SEO 第三方估） |
| **LangSmith** | L2 | **LangChain/LangGraph** 原生 trace + Prompt Hub + 标注队列 | npm 下载量高（LangChain 生态） |
| **Arize Phoenix** | L1/L5 | **OTel-native** OSS + 商业 **AX** 路径 | ELv2 OSS 后端 |
| **Helicone** | L4 | **AI Gateway** + 请求级 observability；快速接入 | 与 api 网关分流 |
| **Datadog LLM Obs** | L3 | 已有 Datadog 栈的 **LLM 语义层** + eval 模板 | Pro ~$160/mo 档（2026 官网） |
| **Traceloop** | L1 | **OTel** LLM tracing SaaS；SOC2 | 与 OpenLLMetry 叙事 |
| **Opik**（Comet） | L1 | Comet **开源** LLM obs + experiment；可自托管 | eval 能力链 evaluation |
| **LangWatch** | L1 | Agent trace + OTel；欧洲合规叙事 | Agent eval 细节 → evaluation |

### Langfuse vs LangSmith（买家常搜对比 · 非 SSOT 排名）

| 维度 | Langfuse | LangSmith |
|------|----------|-----------|
| 生态 | Framework-agnostic、OTel | **LangChain/LangGraph 最深** |
| 许可/自托管 | **MIT 全栈自托管** | SaaS 为主，Enterprise 自托管 |
| 定价感知 | Unit 制，Core **$29/mo** 起 | Per-seat + trace 超额 |
| 选型一句 | 要 **数据主权 / 非 Lang 锁定** | 已 **全栈 LangGraph** |

*完整 scorer/CI 对比见 [evaluation.md](evaluation.md)。*

---

## 选型决策树

1. **首要问题是什么？** 质量打分/挡 PR → **evaluation**；看不见线上请求 → **本文**。
2. **已全栈 LangChain/LangGraph？** 是 → **LangSmith** 默认；否 → **Langfuse** / Phoenix。
3. **必须自托管 / 数据不出 VPC？** → **Langfuse**、**Phoenix**、**Opik**。
4. **已有 Datadog APM？** → **Datadog LLM Obs** 或 OTel 双写 Langfuse + Datadog。
5. **先要网关统一计费再 obs？** → **Helicone** + 可选第二 obs 层。
6. **Agent 生产链**：runtime → **本文 obs** → [evaluation.md](evaluation.md) scorer；与 [agent-runtime.md](../agent/agent-runtime.md) **Observe** 层对齐。

---

## 风险 · 合规 · 工程治理

- **PII in trace**：prompt/completion 常含个人数据——masking、区域、保留期、DPA。
- **采样与遗漏**：tail sampling 可能丢掉 rare failure——关键 path 可 force sample。
- **Obs 成本**：verbose Agent trace 体积大；Langfuse **units**、Datadog **spans** 需预算告警。
- **双平台写入**：OTel 允许 **Langfuse + 现有 APM**；避免两套 truth 无关联。
- **Eval 分离存储**：score 若不在 span 上，debug 需跳 dashboard——优先选 **score-on-trace** 栈。

---

## 落地碎片

- 先 **instrument 一条 happy path**，再扩 Agent 全图——勿先买平台后改代码。
- **Prompt 版本** 与 **trace metadata** 从第一天绑定——否则无法做 prompt 回归。
- 生产 obs 与 eval：**同一 OTel/SDK** 进 trace，scorer 异步写 score（见 evaluation §接缝）。
- RAG debug：在 trace 里看 **retrieval span** 的 chunk，比只看 final answer 快一个数量级。
- ClickHouse 收购后：关注 Langfuse **cloud 与 self-host** 路线图；短期官方承诺 OSS 不变（2026-01 公告）。

---

## 外链索引

### Tier 0 · 官方

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Langfuse** | Docs · Pricing · Self-host | [langfuse.com/docs](https://langfuse.com/docs) · [pricing](https://langfuse.com/pricing) |
| **ClickHouse × Langfuse** | 收购与 OSS 承诺 | [clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability) |
| **LangSmith** | LangChain 可观测性 | [docs.smith.langchain.com](https://docs.smith.langchain.com/) |
| **Arize Phoenix** | OSS OTel LLM obs | [phoenix.arize.com](https://phoenix.arize.com/) |
| **Helicone** | Gateway + observability | [helicone.ai](https://www.helicone.ai/) |
| **Datadog LLM Observability** | APM 延伸 | [docs.datadoghq.com/llm_observability](https://docs.datadoghq.com/llm_observability/) |
| **Traceloop** | OpenLLMetry | [traceloop.com](https://www.traceloop.com/) |
| **Opik** | Comet LLM obs | [comet.com/site/products/opik](https://www.comet.com/site/products/opik/) |
| **LangWatch** | Agent obs | [langwatch.ai](https://langwatch.ai/) |
| **OpenInference** | Span 语义约定 | [openinference.io](https://openinference.io/) |

### L6 · Eval-first · 见 evaluation

| 名称 | 说明 | URL |
|------|------|-----|
| **Braintrust** | Eval-first；trace 服务 experiment | [braintrust.dev](https://www.braintrust.dev/) — **主榜** [evaluation.md](evaluation.md) |

---

## 延伸阅读 · 站内

- [evaluation.md](evaluation.md) — **Scorer / dataset / CI gate / Judge**；score 写回 trace 的接缝
- [llm.md](llm.md) — **公开模型榜**（Arena/SWE-bench）；勿与本页混
- [api.md](../infrastructure/api.md) — 统一 API / 网关；Helicone 分流
- [agent-runtime.md](../agent/agent-runtime.md) — Runtime **Observe** 层；托管 runtime  bundled obs
- [agent-memory.md](../agent/agent-memory.md) — 记忆组件 vs trace 存储
- [inference-infrastructure.md](../infrastructure/inference-infrastructure.md) — 模型 **部署** vs 应用 **运行观测**
- [ai-training-data.md](../infrastructure/ai-training-data.md) — 训前数据；训后质量链 **evaluation**
