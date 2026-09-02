# AI 推理基础设施 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI Inference Infrastructure / 推理托管**——为开源或定制模型提供 **GPU 调度、推理引擎、扩缩与计费**，验收以 **tok/s、TTFT、$/1M tokens、冷启动** 为主。本页为 **推理基础设施产品 SSOT**（完整 URL 表仅此一处）；多模型 API 路由 → [api.md](api.md)；模型能力评测 → [llm.md](../llm/llm.md)。

**材料范围**：公开网络检索（厂商文档、定价页、融资新闻、券商报告、独立基准测试与行业分析）；归纳 **AI 推理基础设施**——为开源和定制化模型提供 GPU 调度、推理优化、自动扩缩、可观测性和计费的全套系统软件与算力层。覆盖范围包括但不限于：推理托管平台（Inference-as-a-Service）、自建推理引擎、推理芯片、边缘推理网络。**未**引用 Alignify 站内文章或站内 JSON 内容稿。具体参数、定价与 SLA 以各官网为准。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/inference-infrastructure](https://alignify.co/blog/inference-infrastructure) · [alignify.co/zh/blog/inference-infrastructure](https://alignify.co/zh/blog/inference-infrastructure) · 正文 md 已同步至部署仓 `alignify-by-kostja/content/blog/{en|zh}/inference-infrastructure.md`（上下文仓不再保留 JSON） · slug **`inference-infrastructure`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（待新增锚点 `#inference-infrastructure-tools`）· `keywordEn`: **AI Inference Infrastructure** · `keywordZh`: **AI推理平台（底层：AI推理基础设施）

## 与相邻 slug 分流

| 维度 | **inference-infrastructure（本文）** | **api** | **llm** | **workflow** |
|------|-----|------|------|------|
| 核心问题 | 怎么**部署和运行**自己的模型（GPU 调度、扩缩、推理优化） | 怎么**统一调用**多模型/多模态 AI 能力（协议、路由） | **哪个**模型能力强（评测、排行） | 怎么**编排**多步 AI 流程 |
| 典型读者 | 平台架构师、MLOps 工程师、CTO | 后端工程师、集成开发团队 | 模型选型者、CTO | 自动化工程师 |
| 交付形态 | GPU 集群、推理端点、推理引擎、芯片 | API endpoint、SDK、统一网关 | 基准数字、Elo 排行 | 低代码/无代码编排器 |
| 验收核心 | 吞吐（tok/s）、TTFT、$/1M tokens、冷启动延迟、GPU 利用率 | 延迟（TTFT）、多模态覆盖、可用性 | Arena Elo、MMLU、SWE-bench | 流程成功率、异常处理 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI 推理基础设施 / AI Inference Infrastructure**：为 AI 模型在生产环境中运行推理而构建的底层系统——包括 GPU 算力调度、推理引擎（vLLM、SGLang、TensorRT-LLM）、自动扩缩、模型版本管理、可观测性和计费层。与"训练基础设施"的关键区别：推理是持续消耗（每次用户请求都在花钱），训练是一次性投入。与"统一 API 平台"的区别：推理基础设施解决的是"把模型跑起来"的工程问题，API 平台解决的是"统一调用多个模型"的集成问题。
- **推理引擎 / Inference Engine**：在 GPU 上高效运行大模型的核心软件层——负责 KV Cache 管理、连续批处理（continuous batching）、量化（FP8/INT4）、张量并行和流水线并行。代表方案：vLLM、SGLang、TensorRT-LLM、清程极智赤兔（Chitu）。推理引擎是推理基础设施栈中最核心的软件组件，直接影响吞吐量和延迟。
- **推理托管平台 / Inference-as-a-Service**：将开源模型部署到 GPU 集群上，暴露为 OpenAI 兼容 API 的托管服务。用户无需自建 GPU 集群，按 token 或 GPU 秒付费。代表：Baseten、Together AI、Fireworks AI、Groq、DeepInfra、Modal。2026 年此品类独立估值合计已超 300 亿美元。
- **Serverless 推理 / Serverless Inference**：按实际使用量计费的推理模式——无请求时 scale-to-zero，有请求时自动拉起（通常伴随冷启动延迟 1–30 秒）。典型实现：Hugging Face Inference Providers（routed serverless）、Modal（1s 冷启动，内存快照技术）。与 Dedicated 实例互补，适合流量波动场景。
- **Dedicated 推理 / Dedicated Inference**：独占 GPU 实例的推理模式——固定成本、可预测延迟、无冷启动。适合稳定高吞吐的生产环境。典型实现：Fireworks Dedicated GPU、Together AI Dedicated Endpoints、Baseten Dedicated Inference。
- **多云端推理 / Multi-Cloud Inference**：跨多个云厂商（AWS、GCP、Azure、OCI 等）调度 GPU 算力用于推理——利用不同区域的价格差异和可用性差异，降低单点依赖。Baseten 对接 20 家云厂商为此模式代表。
- **推理芯片 / Inference Chip**：专为 AI 推理优化的处理器——裁剪训练所需的高精度计算单元，聚焦 INT8/FP8 低精度推理，换取更高的每瓦 token 吞吐量。代表：Groq LPU（自研语言处理单元）、Cerebras WSE-3（晶圆级芯片）、曦望启望 S3（国产推理 GPU，LPDDR6 + PCIe Gen6）。
- **PD 分离 / Prefill-Decode Disaggregation**：将推理的两个阶段拆分到不同 GPU 上执行的架构优化——Prefill（预填充，计算密集型）和 Decode（逐 token 生成，内存带宽密集型）分属不同集群，避免相互干扰，提升整体吞吐。Mooncake（字节跳动）、Splitwise（微软）等方案已在生产环境验证。
- **Token 经济学 / Token Economics**：以每百万 token 成本为核心指标的经济分析框架——衡量推理基础设施的竞争力。2026 年价格跨度约 600×：从 $0.10/1M（Gemini Flash-Lite）到 $60/1M（GPT-5.4 Pro）。推理基础设施层通过开源模型托管可将成本压至闭源 API 的 20–40%。
- **冷启动 / Cold Start**：serverless 推理端点从零到就绪的延迟——包括 GPU 实例分配、模型权重加载到显存、推理引擎初始化的总时间。Modal 通过内存快照技术将冷启动压至 ~1s，传统方案通常在 10–60s。Dedicated 实例无此问题。

---

## 专题对照 / 扩展定义

| 二分维度 | A 方向 | B 方向 |
|------|------|------|
| **平台定位** | **推理托管平台**（Baseten、Together AI、Fireworks）：暴露 OpenAI 兼容 API，用户不感知底层 GPU | **自建推理引擎**（vLLM、SGLang、赤兔）：部署在自有 GPU 上，完全控制但需自行运维 |
| **部署模式** | **Serverless**（Modal、HF Inference Providers）：按量付费、零运维、有冷启动 | **Dedicated**（Fireworks Dedicated、Baseten Dedicated）：独占 GPU、可预测延迟、按实例时间计费 |
| **模型来源** | **开源模型托管**（Together AI 200+ 模型、DeepInfra）：80–95% 低于闭源 API 价格 | **定制模型托管**（Baseten Truss、Modal custom container）：用户上传自有模型权重 |
| **算力策略** | **多云聚合**（Baseten 20+ 云厂商）：跨云调度、提升可用性 | **自有芯片/集群**（Groq LPU、Cerebras WSE-3）：垂直整合、性能极致 |
| **计费粒度** | **按 token**（Together AI、Groq）：精细匹配实际用量，适合波动流量 | **按 GPU 秒/时**（Modal、Baseten Dedicated）：可预测成本，适合稳定高吞吐 |
| **覆盖范围** | **纯推理**（Baseten、Groq）：专注推理环节，不做训练 | **训推一体**（Together AI、H3C UniPoD）：推理 + 微调 + 预训练，全生命周期 |

---

## 问题域（为何会出现这类产品）

- **开源模型性能逼近闭源**：Llama 4、DeepSeek V3.2 等开源模型在多项基准上接近 GPT-5、Claude Opus 4.6 水平。企业不再必须依赖 OpenAI/Anthropic 的闭源 API——但运行开源模型需要 GPU 集群和推理引擎，催生了对托管推理基础设施的需求。Baseten 客户中几乎所有企业都在混合使用开源与闭源模型。

- **推理成本压力持续上升**：Agent 工作流（生成→工具调用→再生成）可产生单次用户请求 5–50× 的预期 token 消耗。企业 AI 支出中 30–50% 投向定制化和后训练模型，而非直接调用闭源 API。Baseten 声称客户使用其平台后推理成本通常降低 40% 以上。

- **GPU 集群运维门槛极高**：运行 Llama 4 405B 需要 8×H100，部署 Stable Diffusion 3 需要 A100。GPU 驱动兼容性、显存管理、模型并行切分、batch size 调优——每一项都是专业工程领域。推理托管平台将这些抽象为 API，省去自建 GPU 集群的资本支出和运维负担。

- **供应商风险分散需求**：单一云厂商可能 GPU 缺货、区域配额耗尽、或价格上涨。多云端推理平台（如 Baseten 对接 20 家云厂商）通过跨云调度实现 99.99% 可用性，避免单点依赖。

- **延迟与地域要求**：金融交易、实时语音、代码补全等场景对延迟有硬性要求（TTFT < 200ms）。推理基础设施需在全球多区域部署 GPU 节点，确保请求就近路由。Groq LPU 以 50–150ms TTFT 在实时场景领先；边缘推理网络（CloudSky、Akamai）进一步将推理推向靠近用户的边缘节点。

- **从训练到推理的产业重心转移**：2023 年 AI 算力以训练为主（~70%），2026 年推理占比已升至 60–70%。德勤预计 2026 年推理工作负载将占全部 AI 算力的约三分之二，推理芯片市场规模超 500 亿美元。训练是一次性的，推理是持续的——基础设施的经济重心正在转移。

- **多模型编排复杂度**：一个典型 AI 应用同时调用多个模型——GPT-5 做函数调用、Claude 写代码、Stable Diffusion 生成图片、Whisper 做转录。每种模型需要不同的 GPU 配置、推理引擎参数和扩缩策略。Baseten Chains、Together AI 的 compound AI 编排功能正是为此而生。

---

## 能力栈（概念拆分，非厂商功能表）

- **推理引擎层**：vLLM（开源标杆，PagedAttention 显存管理）→ SGLang（结构化生成优化）→ TensorRT-LLM（NVIDIA 官方，最强单卡性能）→ 赤兔 Chitu（国产自主，适配昇腾/沐曦/海光/摩尔线程）。核心指标：吞吐量（tok/s/GPU）、TTFT（首 token 延迟）、TPOT（每输出 token 时间）。

- **调度与编排层**：静态 GPU 分配（手动指定 GPU 型号和数量）→ 自动扩缩（基于 QPS 或 GPU 利用率的弹性伸缩）→ 智能路由（按模型类型和延迟要求匹配最优 GPU 池）→ 多云调度（跨 AWS/GCP/Azure/OCI 的 GPU 容量管理和成本仲裁）。

- **模型管理**：模型权重存储（S3/对象存储 → GPU 显存加载）→ 版本控制（模型快照，防止提供方升级破坏下游）→ A/B 部署（同一端点后端挂多个模型版本，按流量比例路由）→ 回滚（推理质量下降时秒级切回旧版）。

- **优化技术栈**：量化（FP16 → FP8 → INT4，精度损失 ~1% 但吞吐翻倍）→ KV Cache 优化（PagedAttention、Mooncake 分布式缓存，首 token 延迟降 90%）→ PD 分离（prefill 和 decode 分 GPU 执行，吞吐提升 30–50%）→ 投机解码（用小模型草稿 + 大模型校验，延迟降 2–3×）。

- **可观测性**：推理延迟分布（P50/P95/P99 TTFT 和 TPOT）→ GPU 利用率与显存占用 → token 级成本追踪（per-request/per-user/per-model）→ 错误率按模型版本分拆 → 冷启动频率与耗时 → 429 限流触发次数。

- **计费与 FinOps**：按 token 计费（适合 LLM 文本推理）→ 按 GPU 秒计费（适合媒体生成和批量推理）→ 按实例时间（Dedicated 独占）→ 混合计费（serverless burst + dedicated baseline）。2026 年趋势：token 级成本归属到团队/项目，设置预算硬顶和自动降级策略。

- **安全与合规**：API key 轮换 → 请求日志脱敏 → 数据驻留（区域端点）→ VPC/PrivateLink 连接 → SOC 2 / HIPAA / GDPR 认证 → Zero Data Retention（推理后不存储输入输出）。Fireworks AI 和 Baseten 在企业合规认证上领先。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **I** | 纯推理托管——OpenAI 兼容 API | pure-play inference hosting | Baseten、DeepInfra |
| **II** | 全栈 AI 云——训推微调 | full-stack AI cloud | Together AI |
| **III** | 代码优先 GPU 平台——函数式部署 | code-first GPU compute | Modal |
| **IV** | 芯片驱动推理——垂直整合 | chip-native inference | Groq、Cerebras、曦望 S3 |
| **V** | 多云端调度——跨云容量 | multi-cloud orchestration | Baseten 多云模式、Nebius |
| **VI** | 训推一体硬件超节点 | unified train-infer hardware | H3C UniPoD、NVIDIA DGX |
| **VII** | 开源推理引擎——自建 | open-source inference engine | vLLM、SGLang、TensorRT-LLM、赤兔 Chitu |
| **VIII** | 边缘推理网络 | edge inference network | CloudSky、Akamai AI Inference |

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **供应商锁定与迁移成本**：各家推理托管平台的 API 虽然都声称 "OpenAI 兼容"，但推理优化技术（量化方案、KV Cache 实现、扩缩策略）差异巨大。从 Baseten 迁到 Together AI 或反之，不仅涉及 API 改造，还可能面临性能退化——相同模型在不同平台的吞吐量可差 2–5×。最低防护：抽象推理层，保留至少两家平台的接入能力。

- **成本失控与 Agent 放大效应**：Agent 工作流中"生成→工具调用→再生成"的循环可导致单次用户请求产生 5–50× 的预期 token 消耗。serverless 推理虽按量付费零运维，但冷启动期间仍会计费（部分平台按 GPU 实例启动时间收费）。最低防护：设置 $X/hard limit + 429 阻断开销，对 Agent 循环设置 max_tool_calls 上限。

- **模型版本与行为漂移**：开源模型更新频繁（Llama 4.x、DeepSeek V3.x），同一推理端点升级模型版本后，下游应用的输出质量可能发生语义级变化。使用 dated model snapshot 而非 rolling latest 是基础操作。专用推理端点（Dedicated）允许锁定模型版本，serverless 方案需确认平台是否支持版本快照。

- **GPU 供应链与地缘政治风险**：2026 年 H100/H200/B200 供应仍然紧张，美国对华出口管制持续加码。依赖单一芯片供应商（如仅用 NVIDIA）或单一区域 GPU 集群的推理平台面临地缘政治风险。多云端 + 国产芯片（昇腾、曦望）的混合策略是长期方向。

- **数据隐私与模型安全**：第三方推理平台处理用户 prompt 和响应时，数据经过平台的控制平面。Baseten 和 Fireworks 提供 Zero Data Retention（推理后不存储输入输出），但多数平台默认保留日志用于监控。医疗/金融合规场景需确认 VPC 内推理（数据不出企业边界）和 SOC 2/HIPAA 认证状态。

- **推理芯片路线图风险**：Groq LPU 凭借极致速度差异化，但其创始人 Jonathan Ross 已于 2025 年 12 月加入 NVIDIA（NVIDIA 以 ~$200 亿授权 LPU 技术），Groq 后续芯片路线图存在不确定性。Cerebras WSE-3 虽已上市（2026 年 5 月 IPO），但晶圆级芯片的生态兼容性和产能扩展仍有待验证。

- **毛利率与商业模式可持续性**：推理托管平台的商业模式本质是"租 GPU → 加推理软件层 → 转售为 API"。当云厂商（AWS Bedrock、Azure AI、GCP Vertex AI）全面推出类似服务时，中间层的毛利率可能被持续压缩。Baseten 的 40% 推理成本降幅承诺依赖于跨云比价优势——当所有云厂商价格趋同时，这一优势会减弱。

- **边缘推理的安全边界扩展**：边缘推理将模型推理推向 CDN 节点和本地设备，虽然降低了延迟，但也扩大了攻击面——边缘节点的物理安全、固件更新、模型权重防窃取均为新增风险。Akamai 和 CloudSky 的边缘推理方案目前主要面向媒体处理和轻量级 LLM，尚未覆盖金融级安全场景。

---

## 落地碎片（无先后）

- 先统计当前 AI 工作负载的**推理 vs 训练用量比例**——按 GPU 小时、token 量、模型类型分拆。多数团队会发现推理占比在 60–80%，但 GPU 集群配置仍以训练为导向。用数据说服团队将预算从训练集群向推理托管平台倾斜。

- 选型时先评估**模型来源需求**：如果主要用开源模型的 OpenAI 兼容 API（Llama、DeepSeek 等），优先对比 Together AI、Fireworks、DeepInfra 的按 token 定价；如果需要部署自己的微调模型权重，优先看 Baseten（Truss 容器方案）或 Modal（Python 函数式部署）。

- 对生产环境设置**推理端点分级**：Tier 1（用户面向前端，<200ms TTFT，Dedicated 实例）→ Tier 2（内部工具/Analytics，<2s TTFT，serverless）→ Tier 3（批量/离线评估，24h 内完成，Batch API 折扣 50%）。

- 建立**模型回归集**：保存 50–100 个典型 prompt 与参考响应，每次切换推理平台或升级模型版本后重跑对比。重点监测：事实准确性、输出格式合规性、拒绝率变化、延迟分布（P50/P95/P99）。

- 多云策略从两家起步：一个主推理平台（基于性能/价格）+ 一个备用平台（基于地理覆盖/合规）。不追求一次性覆盖 20 家云厂商，Baseten 的多云价值在于自动故障转移，而非同时使用所有的云。

- 对 Agent 工作流设置**max_tool_calls 上限**和**总步数硬顶**——防止循环失控导致推理成本暴增。每个 Agent 会话设置 token 预算上限（如 100K tokens/session），超限后降级至更便宜的模型或中断。

- 定期审视**推理平台 vs 自建引擎的 TCO**：当推理 token 消耗超过 ~10B tokens/月时，自建 vLLM/SGLang 集群的 GPU 租赁成本可能开始低于托管平台。但这个拐点取决于团队是否有 GPU 运维能力——清程极智赤兔引擎的部署成本（DeepSeek-V3 满血版仅需 1 台 8 卡服务器，硬件 150 万）是一个参考锚点。

---

## 工具与产品类型（「LLM inference」「model inference」「AI inference platform」「inference provider」检索常混在一起的品类；非穷尽）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **纯推理托管平台** | Type I | 见 §外链索引 |
| **全栈 AI 云** | Type II | 见 §外链索引 |
| **代码优先 GPU 部署** | Type III | 见 §外链索引 |
| **芯片驱动推理** | Type IV | 见 §外链索引 |
| **开源推理引擎** | Type VII | 见 §外链索引 |
| **边缘推理网络** | Type VIII | 见 §外链索引 |
| **多云端调度** | Type V | 见 §外链索引 |
| **训推一体硬件** | Type VI | 见 §外链索引 |

---

## 外链索引（工具与平台；非广告、无排序优先级）

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **Baseten** | 纯推理托管平台，对接 20+ 云厂商，Truss 容器 + Chains SDK 多模型编排，SOC 2 Type II/HIPAA；客户含 Cursor/Notion/HeyGen/Patreon；2026 年 6 月 F 轮 $1.5B 估值 $13B，年化营收 ~$600M | [baseten.co](https://www.baseten.co) |
| **Together AI** | 全栈 AI 云，200+ 开源模型，推理+微调（SFT+RLHF），FlashAttention-4/ATLAS 研究驱动；估值 $7.5B，年化营收 ~$1B | [together.ai](https://www.together.ai) |
| **Fireworks AI** | 400+ 模型，FireAttention 引擎，多模态+企业合规（SOC 2/HIPAA/GDPR），Zero Data Retention + BYOC；估值 $15B，年化营收 ~$800M | [fireworks.ai](https://fireworks.ai) |
| **Modal** | 代码优先 GPU 部署，Python 函数式，1s 冷启动（内存快照），per-second 计费；估值 $4.65B（Series C 2026.5），年化营收 ~$300M | [modal.com](https://modal.com) |
| **Groq** | 自研 LPU 芯片，840 tok/s Llama 3.1 8B、50–150ms TTFT，3M+ 开发者；NVIDIA 以 ~$20B 授权 LPU 技术（2025.12），独立运营中 | [groq.com](https://groq.com) |
| **Cerebras** | 晶圆级芯片 WSE-3，2026 年 5 月 IPO NASDAQ: CBRS，IPO 募资 $5.5B，首日市值 ~$66B | [cerebras.ai](https://www.cerebras.ai) |
| **DeepInfra** | 开源模型推理托管，~5T tokens/周，$107M Series B（NVIDIA/Samsung Next）；覆盖 LLM+图像+音频 | [deepinfra.com](https://deepinfra.com) |
| **vLLM** | 开源推理引擎标杆，PagedAttention 显存管理，社区最活跃的推理框架 | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) |
| **SGLang** | 开源推理引擎，结构化生成优化，RadixAttention 前缀缓存 | [github.com/sgl-project/sglang](https://github.com/sgl-project/sglang) |
| **TensorRT-LLM** | NVIDIA 官方推理引擎，最强单卡性能，与 NVIDIA 生态深度集成 | [github.com/NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) |
| **赤兔 Chitu** | 国产自主推理引擎，适配昇腾/沐曦/海光/摩尔线程；DeepSeek-V3 满血版 1 台 8 卡服务器即可部署（硬件成本 150 万） | 清程极智（清华系） |
| **曦望启望 S3** | 国产推理 GPU，首个用 LPDDR6 + PCIe Gen6，显存最大近 600GB，目标"百万 Token 一分钱"；估值超 100 亿元 | 曦望（Sunrise） |
| **CloudSky** | GPU 原生边缘云，覆盖 300+ 城市，服务 6 亿用户；边缘推理网络 | [cloudsky.com](https://www.cloudsky.com) |

### 对比与测评（第三方；观点非官方）

2026 年 AI 推理基础设施市场的核心叙事是**开源模型崛起驱动推理需求爆发**。Baseten CEO 图欣·斯里瓦斯塔瓦对《华尔街日报》表示："核心趋势是开源模型的性能正大幅提升；开源生态越成熟，我们的业务规模也会同步增长。"这一判断得到了数据支撑——Baseten 年化营收同比增长约 20 倍，Baseten 客户中几乎所有企业都在混合使用开源与闭源模型。

从竞争格局看，四家头部推理基础设施公司合计估值已超 300 亿美元——Together AI（$7.5B）、Fireworks AI（$15B）、Baseten（$13B）、Modal（$4.65B）。18 个月前此品类甚至不被认为是一个独立的市场类别。Fortune Business Insights 将推理基础设施市场规模估为 2026 年 $118B，预计 2034 年达 $313B。

**竞争维度正在分化**：Together AI 以模型目录广度（200+）和微调生态领先；Fireworks AI 以多模态 + 企业合规（SOC 2/HIPAA/GDPR）差异化；Baseten 以多云端调度（20 家云厂商）和纯推理定位聚焦；Modal 以代码优先体验和极低冷启动（1s）切入开发者市场。Groq 和 Cerebras 从芯片层面突破，但对 NVIDIA 生态有不同程度的依赖（Groq 已与 NVIDIA 达成 ~$20B 技术授权）。

**成本效益是最核心的竞争维度**。Baseten 声称客户使用其平台后推理成本降低 40% 以上。Together AI 的 batch API 提供 ~50% 折扣。清程极智赤兔引擎将 DeepSeek-V3 满血版的硬件部署成本从 600 万降至 150 万。但毛利率可持续性存疑——每经（NBD）2026 年 6 月报道援引投资人观点称"目前市场确实存在一定泡沫迹象"，云厂商全面入局后中间层的毛利率压力不容忽视。

**边缘推理和端侧推理是新兴方向**。CloudSky 提出"推理不能只在数据中心"，Akamai 将推理推向 CDN 节点。端侧推理芯片（曦望 S3）和模型压缩技术（1.58-bit 三值模型）进一步将推理从云端向边缘和终端分流。2026 年 30–50% 的轻量级推理任务已向端侧迁移。

**中国市场的特殊变量**：美国芯片出口管制加速了国产推理芯片（昇腾、曦望、墨芯）和国产推理引擎（赤兔 Chitu）的发展。中国日均 Token 调用量从 2024 年初的 1000 亿飙升至 2026 年 3 月的 140 万亿，增长 1400 倍。硅基流动（$20 亿+ B 轮）、无问芯穹（累计 $22 亿+）等本土推理平台快速崛起，与 Baseten/Together AI 形成跨市场对标。

*本小节为网摘与行业观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读 · 站内外

- **Baseten 完成 15 亿美元 F 轮融资，估值达 130 亿美元**（智东西, 2026-06-23）：Baseten 融资详情、客户名单、行业竞争格局与推理赛道分析。  
  - 智东西报道（用户提供原文）
- **Inference companies enter the heart of the AI boom**（Jawlah, 2026）：推理基础设施行业全景——Together AI、Baseten、Fireworks、Modal 四家对比。  
  - <https://jawlah.co/en/57906>
- **AI Inference Platforms Compared**（Ry Walker Research, 2026）：推理平台的定价、延迟、模型覆盖横向对比。  
  - <https://rywalker.com/research/ai-inference-platforms>
- **The Inference Layer**（The Synthesis, 2026-05）：推理基础设施作为一个新兴市场品类的行业分析——"此品类 18 个月前尚不存在"。  
  - <https://dev.to/thesythesis/the-inference-layer-587d>
- **What's an inference provider?**（Technically, 2026）：推理提供方的定义与行业入门。  
  - <https://technically.dev/posts/whats-an-inference-provider>
- **Deep Learning Inference Platforms — Global Market Share and Ranking**（QYResearch, 2026）：深度学习推理平台全球市场份额与排名。  
  - <https://www.qyresearch.com/reports/6065890/deep-learning-inference-platforms>
- **AI inferencing will define 2026, and the market's wide open**（SDxCentral, 2026）：推理将成为 2026 年 AI 产业的核心叙事。  
  - <https://www.sdxcentral.com/analysis/ai-inferencing-will-define-2026-and-the-markets-wide-open/>
- **It's Time to Break Up with Your Cloud: Why AI Teams are Switching**（DigitalOcean, 2026）：AI 团队从传统云厂商转向推理专业平台的原因分析。  
  - <https://www.digitalocean.com/community/conceptual-articles/ai-workflow-focused-clouds>
- **Training vs Inference Infrastructure**（Introl, 2026）：训练基础设施与推理基础设施的差异——优化模式、硬件需求、成本结构。  
  - <https://introl.com/blog/training-vs-inference-infrastructure-optimizing-ai-workload-patterns>
- **AI infrastructure spending to hit USD $37.5bn by 2026**（Gartner, 2025）：Gartner 对 AI 基础设施支出的预测。  
  - <https://datacenter.news/story/ai-infrastructure-spending-to-hit-usd-37-5bn-by-2026-says-gartner>
- **疯狂扩产的"Token工厂"：营收数十倍增长，一场场资本狂欢正在上演**（每日经济新闻, 2026-06-18）：中国推理平台融资热潮与泡沫争议。  
  - <http://www.nbd.com.cn/articles/2026-06-18/4431155.html>
- **未来推理将吃掉 70% 算力，30% 留给训练**（量子位 · 硅谷投资人张璐, 2026-05）：推理算力占比预测与 Agent 对推理需求的驱动分析。  
  - <https://www.qbitai.com/2026/05/423441.html>
- **Alignify · 统一 AI API 平台**（知识块，与本文互补）：[`api.md`](api.md)——怎么统一调用多模型；本文是怎么部署和运行自己的模型。  
- **Alignify · 通用大模型评测**（知识块，与本文互补）：[`llm.md`](../llm/llm.md)——哪个模型更强。