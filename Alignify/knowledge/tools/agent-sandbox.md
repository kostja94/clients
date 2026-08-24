# AI Agent 沙箱 · 知识块（非线性笔记）

**材料范围**：公开网络检索（E2B、Modal、Daytona、AWS Bedrock AgentCore、Google Agent Sandbox、Vercel Sandbox、Cloudflare Sandbox SDK、OpenSandbox、kubernetes-sigs/agent-sandbox 等厂商文档与 GA 公告；Ry Walker Research、Firecrawl、Work-Bench、Google Cloud 文档等行业分析；**未**引用 Alignify 站内文章或站内 JSON 内容稿。具体冷启动、定价与隔离实现以各官网为准。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/agent-sandbox](https://alignify.co/blog/agent-sandbox) · [alignify.co/zh/blog/agent-sandbox](https://alignify.co/zh/blog/agent-sandbox) · 正文 md 已同步至部署仓 `alignify-by-kostja/content/blog/{en|zh}/agent-sandbox.md` · slug **`agent-sandbox`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#agent-sandbox-tools`](../../product/alignify-keywords-tools.md#agent-sandbox-tools)）· `keywordEn`: **AI Agent Sandbox** · `keywordZh`: **AI Agent 沙箱

## 与相邻 slug 分流

| 维度 | **agent-sandbox（本文）** | **agent-skills** | **headless-browser** | **agent-for-desktop** | **authentication** | **inference-infrastructure** |
|------|---------------------------|------------------|----------------------|----------------------|---------------------|-------------------------------|
| 核心问题 | Agent **在哪安全执行**不可信代码与工具调用 | Agent **接什么工具/技能** | Agent **如何操控网页**（CDP/BaaS） | Agent **如何动本机/桌面** | Agent **如何获权调第三方 SaaS** | **模型推理**在哪跑（GPU/token） |
| 典型读者 | Agent 平台工程师、安全架构师 | 集成工程师、Agent 应用开发者 | 后端/Agent 工程师 | 知识工作者、Cowork 用户 | 身份/集成平台团队 | MLOps、平台架构师 |
| 交付形态 | 隔离 VM/容器 API、SDK | MCP/Skill 目录、网关 | 远程浏览器会话 | 桌面客户端、托管 VM | OAuth/MCP runtime | 推理端点、GPU 集群 |
| 验收核心 | 隔离等级、冷启动、会话 TTL、网络 egress、审计 | 技能发现、工具覆盖、治理 | 会话稳定、反爬、Computer Use | 本机授权范围、GUI 成功率 | 委托授权、connection 隔离 | TTFT、$/1M tokens、吞吐 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI Agent Sandbox / AI Agent 沙箱**：为 AI Agent 提供的**隔离执行环境**——Agent 在其中运行 LLM 生成的代码、Shell 命令、浏览器操作或文件 I/O，而不直接触碰宿主系统、生产数据库或企业凭据。与「应用层 allowlist」不同，沙箱强调 **OS/内核级或 hypervisor 级边界**。
- **Agent Runtime / Agent 运行时**：比沙箱更宽的**控制平面**概念——管理 Agent 生命周期、会话状态、工具编排、内存、审计与计费。沙箱常是 Runtime 栈中的 **Execute（执行）** 层；Runtime 还可包含 Gateway、Memory、Observability 等（Work-Bench 等投资叙事）。
- **Sandbox-as-tool（沙箱作工具）**：Agent **Runtime 在沙箱外**，仅在需要执行代码/命令时**临时 claim** 一个沙箱，执行完释放——适合交互式、burst 型工具调用（Sandbox0 等架构讨论）。
- **Agent-in-sandbox（Agent 在沙箱内）**：Agent 引擎、依赖、工作区与 sidecar **整体运行在沙箱内**——适合 coding agent、长会话 Devbox、本地进程态连续（与 Bytebot、NanoClaw 类 Harness 相邻）。
- **MicroVM / Firecracker**：硬件虚拟化下的轻量 VM，独立内核，冷启动约 **100–200ms**，被 E2B、Vercel Sandbox、AWS Lambda 等采用；**不可信多租户代码**的行业常见「金标准」隔离层。
- **gVisor（runsc）**：用户态内核拦截 syscall，无独立 VM；Modal 等常用，**GPU 直通**相对友好，隔离强度介于容器与 microVM 之间。
- **Ephemeral sandbox（ ephemeral 优先）**：任务结束即销毁；历史上 E2B 主打形态，2026 年多数平台已叠加 **pause/resume、snapshot**。
- **Persistent sandbox / Devbox**：会话与文件系统跨多轮保留；Daytona、Sprites、Vercel Sandbox 默认或强持久化，适合 coding agent 与长时 Agent 工作流。
- **Checkpoint / snapshot**：冻结内存与进程态到磁盘，恢复时跳过冷启动；2026 年 E2B、Daytona、Runloop、Vercel 等均已支持，正成为 **table stakes**。
- **Computer Use sandbox**：沙箱内提供 **GUI/浏览器/桌面** 能力，不仅是 Python REPL——与 headless-browser 品类交叉，但买家问题仍是「执行边界在哪」。

---

## 专题对照 / 扩展定义

| 二分维度 | A 方向 | B 方向 |
|------|------|------|
| **架构** | **Sandbox-as-tool**（Runtime 外，按需 claim 沙箱） | **Agent-in-sandbox**（Runtime 与 workspace 同处沙箱） |
| **隔离** | **MicroVM**（Firecracker、Kata） | **gVisor / 加固容器**（更快、GPU 友好，隔离较弱） |
| **生命周期** | **Ephemeral**（用完即毁） | **Persistent + checkpoint**（Devbox、hibernate） |
| **部署** | **Managed SaaS**（E2B、Modal） | **Self-hosted / K8s**（OpenSandbox、GKE Agent Sandbox） |
| **买家** | **产品嵌入**（API 给终端用户跑代码） | **企业内 Agent 部署**（BYOC、VPC、CloudTrail） |

| 维度 | **agent-sandbox** | **openclaw-alternatives** | **cli** |
|------|-------------------|---------------------------|---------|
| 核心 | 生产级**隔离执行基础设施** | **个人助理/IM 网关**宿主与托管发行版 | **终端内** Agent 与命令沙箱 |
| NanoClaw | 开源 **Agent-in-sandbox Harness**（容器隔离） | 名字相近但 **不同系谱**（OpenClaw 网关） | 可跑在沙箱内，但品类是 CLI 交付 |

---

## 问题域（为何会出现这类产品）

- **Agent 从「建议」到「执行」**：Copilot 只生成建议；生产 Agent 会写文件、调 API、跑 Terminal——错误从「答错」升级为 **数据泄露、权限越界、自动化事故**。
- **不可信代码是默认假设**：LLM 输出与用户提供 prompt 均不可完全信任；**运行时确定**的代码无法走传统「先 review 再 deploy」流程。
- **容器共享内核不够**：Docker 命名空间对 **多租户不可信 Agent 代码** 常被认为不足；microVM 与 gVisor 成为 2024–2026 主流升级路径。
- **Coding Agent 爆发**：Cursor Agent、Claude Code、Devin 类工作流需要 **每用户/每任务独立环境**，与会话级状态——催生 Devbox 与 sub-100ms 冷启动竞争。
- **大厂 bundled**：2025–2026 年 AWS AgentCore、Google Agent Sandbox、Vercel Sandbox、Cloudflare Sandbox SDK 集中 GA——「Agent 沙箱」从独立品类向 **云平台标配能力** 演化。
- **企业权限焦虑**：采购方核心问题从「模型多聪明」转向 **「Agent 被限制在什么范围、能否审计」**——沙箱 + IAM/MCP 授权并列出现。
- **成本与并发**：Agent 循环可产生大量短生命周期沙箱；**按秒计费、warm pool、hibernate 待机零算力**（Blaxel 等）成为 FinOps 议题。

---

## 能力栈（概念拆分，非厂商功能表）

- **隔离层**：进程/namespace → gVisor → microVM（Firecracker/Kata/libkrun）→ 专用裸金属；选型在 **安全、冷启动、GPU、兼容性** 间权衡。
- **生命周期**：create → exec → pause/resume → snapshot/fork → destroy；TTL 从分钟到 **8h（AgentCore）** 或 **无限（Daytona 叙事）** 不等。
- **网络 egress**：默认全禁 / 白名单 /  intentional 开放（企业需防 DNS exfil、metadata 服务访问——AgentCore 2026 安全研究曾引发讨论）。
- **文件与存储**：临时 overlay、挂载 S3/对象存储、PVC（K8s Agent Sandbox）；**凭据不得写入可持久卷** 是常见基线。
- **可观测性**：命令审计、stdout/stderr 流、OpenTelemetry、CloudTrail；与 **Agent 可解释性** 弱于传统服务——需平台侧日志。
- **集成面**：Python/TS SDK、REST、MCP server（AIO Sandbox 等）、OpenAI Agents SDK 兼容层。
- **计费**：按 vCPU-秒、GiB-秒、沙箱-分钟、待机 hibernate 免费等；与 **serverless GPU**（Modal Sandboxes）交叉。

---

## 形态谱系（与具体品牌解耦）

- **Type I — Managed microVM API**：Firecracker 隔离，API 创建/执行/销毁；代表定位 E2B、Blaxel（microVM + hibernate）。
- **Type II — GPU serverless sandbox**：gVisor + 弹性 GPU；Agent 内需跑 ML/重计算；代表定位 Modal Sandboxes。
- **Type III — Persistent Devbox**：快速 provisioning + 长会话 + fork/snapshot；代表定位 Daytona、Sprites、Runloop。
- **Type IV — Hyperscaler bundled**：与现有云账单、IAM、模型栈一体；AWS AgentCore Code Interpreter/Runtime、Google Agent Sandbox、Vercel Sandbox。
- **Type V — Edge/Workers 沙箱**：Cloudflare Containers + V8 isolates；低延迟、与 Workers AI 同栈。
- **Type VI — K8s-native / 自托管**：OpenSandbox、kubernetes-sigs/agent-sandbox、GKE Agent Sandbox；CRD + gVisor/Kata 可选。
- **Type VII — 开源 Agent Harness（Agent-in-sandbox）**：可读 codebase + 容器隔离 + IM/Skills；NanoClaw、Bytebot（容器内桌面）——**不是** E2B 式 API 平台，但解决同类「安全执行」问题。

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **Prompt injection → 沙箱逃逸链**：恶意网页/文档诱导 Agent 执行 exfil 命令；沙箱需 **网络默认拒绝 + 凭据隔离**，不能假设 LLM 会拒绝。
- **供应链**：Agent 自动安装 skill/MCP 包等同 **任意代码**；需签名渠道与执行隔离（与 agent-skills 品类交叉）。
- **过度持久化**：checkpoint 保留内存中的 **token/密钥**；TTL 与销毁策略必须可审计。
- **共享宿主机侧信道**：容器级隔离对 **最高安全多租户** 可能不足；金融/政府场景倾向 microVM 或专用集群。
- **合规与数据驻留**：BYOC/VPC/on-prem（Northflank、OpenSandbox 自托管）vs 纯 SaaS；医疗/金融需确认日志是否含用户数据。
- **厂商锁定**：各平台 SDK 与镜像格式不一；E2B 兼容协议（agent-sandbox 社区项目）试图降低迁移成本。
- **成本失控**：长会话 + 高并发沙箱；需 **预算顶、自动 pause、hibernate** 策略。

---

## 落地碎片（无先后）

- 先画 **Sandbox-as-tool vs Agent-in-sandbox**：交互式 coding agent 常偏后者；无状态「跑一段 Python」偏前者。
- **不可信来源**（公开 API、匿名用户）→ 优先 **microVM**（E2B 等），不要仅依赖共享内核容器。
- **需要 GPU 在沙箱内** → Modal 等 gVisor+GPU 路径；E2B 传统强项在 CPU 代码执行。
- **需要数小时 Devbox** → Daytona / persistent 平台；确认 snapshot 与 **网络策略** 默认值。
- **已在 AWS/GCP/Vercel 栈内** → 评估 bundled 产品 TCO 与 **egress 硬ening** 再选独立 SaaS。
- **K8s 已有** → GKE Agent Sandbox / OpenSandbox / SIG agent-sandbox CRD，避免重复造调度层。
- 与 [authentication.md](./authentication.md) 分工：**沙箱管执行边界**，Arcade 等管 **OAuth/connection**；两者需同时设计。
- NanoClaw 类 **自托管 Harness**：适合「可读 codebase + 容器隔离 + 个人/小团队」，**不等于**替代 E2B 生产 API。

---

## 工具与产品类型（「AI agent sandbox」「code execution sandbox」检索常混在一起的品类；非穷尽）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **Managed microVM SaaS** | E2B、Blaxel | API-first；Fortune 100 采用叙事；Firecracker |
| **GPU serverless sandbox** | Modal Sandboxes | T4–B200；OpenAI Agents SDK 集成 |
| **Persistent Devbox** | Daytona、Runloop、Sprites | sub-100ms–2s 创建；Computer Use 扩展 |
| **Cloud bundled** | AWS AgentCore、Google Agent Sandbox、Vercel Sandbox | IAM/账单一体；preview/GA 节奏快 |
| **Edge sandbox** | Cloudflare Sandbox SDK | Containers + isolates |
| **Enterprise BYOC** | Northflank | Kata/gVisor；多云 VPC |
| **K8s / OSS** | OpenSandbox、kubernetes-sigs/agent-sandbox | 自托管；CNCF Landscape（OpenSandbox） |
| **All-in-one 容器** | AIO Sandbox | Browser+Shell+Jupyter+MCP 单容器 |
| **Harness + 容器** | NanoClaw、Bytebot | Agent-in-sandbox；非多租户 SaaS |

---

## 外链索引（工具与平台；非广告、无排序优先级）

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **E2B** | Firecracker microVM；AI Agent 代码执行标杆；pause/resume + snapshot；SDK Python/TS | [e2b.dev](https://e2b.dev) |
| **Modal** | gVisor 隔离；Sandboxes + GPU；serverless 按秒计费；2026 年大额融资与规模化叙事 | [modal.com](https://modal.com) |
| **Daytona** | 持久 workspace；冷启动 27–90ms 叙事；开源社区大；Computer Use/GPU 扩展 | [daytona.io](https://www.daytona.io) |
| **AWS Bedrock AgentCore** | 托管 Agent Runtime + Code Interpreter；microVM；最长 8h 会话；CloudTrail | [docs.aws.amazon.com/bedrock-agentcore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) |
| **Google Agent Sandbox** | Gemini Enterprise 执行层；2026 preview；gVisor/加固容器；sub-second 创建 | [cloud.google.com](https://cloud.google.com/) |
| **Vercel Sandbox** | Firecracker；持久化默认；Vercel 平台团队；毫秒级创建叙事 | [vercel.com](https://vercel.com/) |
| **Cloudflare Sandbox SDK** | Workers 上容器 + isolate；与 Workers AI 集成 | [developers.cloudflare.com](https://developers.cloudflare.com/) |
| **Blaxel** | microVM + **hibernate 待机零算力**；sub-25ms resume | [blaxel.ai](https://blaxel.ai) |
| **Northflank** | BYOC；Kata/gVisor；企业 VPC + GPU | [northflank.com](https://northflank.com) |
| **OpenSandbox** | 自托管；Firecracker/Kata/gVisor；K8s 原生 | [github.com/opensandbox-group/opensandbox](https://github.com/opensandbox-group/opensandbox) |
| **kubernetes-sigs/agent-sandbox** | K8s SIG Apps；Sandbox CRD；Agent runtime 标准 API 探索 | [agent-sandbox.sigs.k8s.io](https://agent-sandbox.sigs.k8s.io) |
| **NanoClaw** | 开源轻量 OpenClaw 替代；Docker/Apple Container 隔离；Claude Agent SDK | [github.com/qwibitai/NanoClaw](https://github.com/qwibitai/NanoClaw) |

### 对比与测评（第三方；观点非官方）

2026 年上半年行业共识是 **「Agent 沙箱」已成独立基础设施品类**，且 **大厂集体进场**（Vercel、Cloudflare、AWS、Google）。Ry Walker Research（2026-03/06）归纳：独立 Tier 由 **E2B（规模与安全）**、**Modal（GPU）**、**Daytona（开源+Devbox）** 领导；持久化与 checkpoint 从差异化变为 **标配**。

Work-Bench 将 **Agent Runtime** 定义为包含 Execute（沙箱）在内的更大栈；Execute 层核心 trade-off 是 **Firecracker 安全 vs gVisor/GPU vs Docker 速度**。Firecrawl（2026）将沙箱分为 **Browser / Code / Full Dev Env** 三类——与 headless-browser、agent-for-desktop 分流。

**NanoClaw / NanoCo**：据 2026 年科技媒体报道，NanoCo 完成 Seed 融资并拒绝收购报价；产品定位为 **容器隔离的个人/企业 Agent Harness**，与 E2B 的 **API 多租户沙箱** 买家不同。与 OpenClaw **名字相近、系谱不同**——OpenClaw 是网关型个人助理，NanoClaw 强调 OS 级隔离与小 codebase。

*本小节为网摘与行业观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读与参考材料

- **AI Agent Sandboxes Compared**（Ry Walker Research, 2026）：15+ 平台对比矩阵、冷启动、持久化、融资动态。  
  - <https://rywalker.com/research/ai-agent-sandboxes>
- **The Rise of the Agent Runtime**（Work-Bench, 2026）：Runtime 栈四分法；沙箱在 Execute 层的位置。  
  - <https://www.work-bench.com/post/the-rise-of-the-agent-runtime>
- **About GKE Agent Sandbox**（Google Cloud 文档）：K8s 原生 Agent 沙箱、gVisor、Python SDK。  
  - <https://cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox>
- **Host agent or tools with Amazon Bedrock AgentCore Runtime**（AWS 文档）：Runtime 能力、MCP、长时会话。  
  - <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html>
- **Overview | Agent Sandbox**（kubernetes-sigs）：Sandbox CRD 与 Agent runtime 用例。  
  - <https://agent-sandbox.sigs.k8s.io/docs/getting_started/overview/>
