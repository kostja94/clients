# AI Agent 沙箱 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI Agent Sandbox / Agent 沙箱**——为 AI Agent 提供的隔离执行环境，运行 LLM 生成的代码、Shell、浏览器操作或文件 I/O 而不直接触碰宿主系统；验收以 **隔离等级（microVM vs gVisor vs 容器）、冷启动、会话 TTL 与网络 egress** 为主。本页为 **Agent Sandbox 产品 SSOT**（完整 URL 表仅此一处）；技能供应链 → [agent-skills.md](agent-skills.md)；远程浏览器 → [headless-browser.md](../web-data/headless-browser.md)；桌面 Agent → [agent-for-desktop.md](agent-for-desktop.md)。

**材料范围**：公开网络检索（E2B、Modal、Daytona、AWS Bedrock AgentCore、Google Agent Sandbox、Vercel Sandbox、Cloudflare Sandbox SDK、OpenSandbox、kubernetes-sigs/agent-sandbox 等厂商文档与 GA 公告）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/agent-sandbox](https://alignify.co/blog/agent-sandbox) · slug **`agent-sandbox`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#agent-sandbox-tools`](../../product/alignify-keywords-tools.md#agent-sandbox-tools)）

---

## 与相邻 slug 分流

| 维度 | **agent-sandbox（本文）** | **agent-skills** | **headless-browser** | **agent-for-desktop** | **authentication** |
|------|---------------------------|------------------|----------------------|----------------------|---------------------|
| 核心问题 | Agent **在哪安全执行**不可信代码 | Agent **接什么工具/技能** | Agent **如何操控网页** | Agent **如何动本机/桌面** | Agent **如何获权调第三方 SaaS** |
| 典型读者 | Agent 平台工程师、安全架构师 | 集成工程师 | 后端/Agent 工程师 | 知识工作者 | 身份/集成平台团队 |
| 验收核心 | 隔离等级、冷启动、TTL、egress、审计 | 技能发现、工具覆盖 | 会话稳定、Computer Use | 本机授权范围 | 委托授权、connection 隔离 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI Agent Sandbox / AI Agent 沙箱**：为 AI Agent 提供的**隔离执行环境**——Agent 在其中运行 LLM 生成的代码、Shell 命令、浏览器操作或文件 I/O，而不直接触碰宿主系统、生产数据库或企业凭据。与「应用层 allowlist」不同，沙箱强调 **OS/内核级或 hypervisor 级边界**。
- **Agent Runtime / Agent 运行时**：比沙箱更宽的**控制平面**概念——管理 Agent 生命周期、会话状态、工具编排、内存、审计与计费。沙箱常是 Runtime 栈中的 **Execute（执行）** 层。
- **Sandbox-as-tool（沙箱作工具）**：Agent **Runtime 在沙箱外**，仅在需要执行代码/命令时**临时 claim** 一个沙箱，执行完释放——适合交互式、burst 型工具调用。
- **Agent-in-sandbox（Agent 在沙箱内）**：Agent 引擎、依赖、工作区与 sidecar **整体运行在沙箱内**——适合 coding agent、长会话 Devbox（与 Bytebot、NanoClaw 类 Harness 相邻）。
- **MicroVM / Firecracker**：硬件虚拟化下的轻量 VM，独立内核，冷启动约 **100–200ms**——**不可信多租户代码**的行业常见「金标准」隔离层。
- **gVisor（runsc）**：用户态内核拦截 syscall，无独立 VM；Modal 等常用，**GPU 直通**相对友好，隔离强度介于容器与 microVM 之间。
- **Ephemeral sandbox**：任务结束即销毁；2026 年多数平台已叠加 **pause/resume、snapshot**。
- **Persistent sandbox / Devbox**：会话与文件系统跨多轮保留；适合 coding agent 与长时 Agent 工作流。
- **Checkpoint / snapshot**：冻结内存与进程态到磁盘，恢复时跳过冷启动——2026 年正成为 **table stakes**。
- **Computer Use sandbox**：沙箱内提供 **GUI/浏览器/桌面** 能力——与 headless-browser 品类交叉，但买家问题仍是「执行边界在哪」。

---

## 专题对照 / 扩展定义

**架构与隔离二分**（术语见 §词汇锚点；Type 见 §形态谱系）：

| 二分维度 | A 方向 | B 方向 |
|------|------|------|
| **架构** | **Sandbox-as-tool**（Runtime 外，按需 claim） | **Agent-in-sandbox**（Runtime 与 workspace 同处沙箱） |
| **隔离** | **MicroVM**（Firecracker、Kata） | **gVisor / 加固容器**（更快、GPU 友好，隔离较弱） |
| **生命周期** | **Ephemeral**（用完即毁） | **Persistent + checkpoint**（Devbox、hibernate） |
| **部署** | **Managed SaaS**（E2B、Modal） | **Self-hosted / K8s**（OpenSandbox、GKE Agent Sandbox） |

| 维度 | **agent-sandbox** | **openclaw-alternatives** | **cli** |
|------|-------------------|---------------------------|---------|
| 核心 | 生产级**隔离执行基础设施** | **个人助理/IM 网关**宿主 | **终端内** Agent 与命令沙箱 |
| NanoClaw | 开源 **Agent-in-sandbox Harness**（容器隔离） | 名字相近但 **不同系谱** | 可跑在沙箱内，但品类是 CLI 交付 |

---

## 问题域（为何会出现这类产品）

- **Agent 从「建议」到「执行」**：生产 Agent 会写文件、调 API、跑 Terminal——错误从「答错」升级为 **数据泄露、权限越界、自动化事故**。
- **不可信代码是默认假设**：LLM 输出与用户提供 prompt 均不可完全信任。
- **容器共享内核不够**：Docker 命名空间对 **多租户不可信 Agent 代码** 常被认为不足；microVM 与 gVisor 成为 2024–2026 主流升级路径。
- **Coding Agent 爆发**：Cursor Agent、Claude Code、Devin 类工作流需要 **每用户/每任务独立环境**——催生 Devbox 与 sub-100ms 冷启动竞争。
- **大厂 bundled**：2025–2026 年 AWS AgentCore、Google Agent Sandbox、Vercel Sandbox、Cloudflare Sandbox SDK 集中 GA。
- **企业权限焦虑**：采购方核心问题从「模型多聪明」转向 **「Agent 被限制在什么范围、能否审计」**。
- **成本与并发**：Agent 循环可产生大量短生命周期沙箱；**按秒计费、warm pool、hibernate 待机零算力** 成为 FinOps 议题。

---

## 能力栈（概念拆分，非厂商功能表）

- **隔离层**：进程/namespace → gVisor → microVM → 专用裸金属；选型在 **安全、冷启动、GPU、兼容性** 间权衡。
- **生命周期**：create → exec → pause/resume → snapshot/fork → destroy；TTL 从分钟到 **8h（AgentCore）** 或更长不等。
- **网络 egress**：默认全禁 / 白名单 / intentional 开放——企业需防 DNS exfil、metadata 服务访问。
- **文件与存储**：临时 overlay、挂载 S3/对象存储、PVC；**凭据不得写入可持久卷** 是常见基线。
- **可观测性**：命令审计、stdout/stderr 流、OpenTelemetry、CloudTrail。
- **集成面**：Python/TS SDK、REST、MCP server、OpenAI Agents SDK 兼容层。
- **计费**：按 vCPU-秒、GiB-秒、沙箱-分钟、待机 hibernate 免费等。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **I** | Managed microVM API；Firecracker 隔离 | Managed microVM SaaS | E2B、Blaxel |
| **II** | GPU serverless sandbox；gVisor + 弹性 GPU | GPU serverless sandbox | Modal Sandboxes |
| **III** | Persistent Devbox；快速 provisioning + fork/snapshot | Persistent devbox | Daytona、Sprites、Runloop |
| **IV** | Hyperscaler bundled；与现有云账单、IAM 一体 | Cloud bundled sandbox | AWS AgentCore、Google Agent Sandbox、Vercel Sandbox |
| **V** | Edge/Workers 沙箱；Containers + V8 isolates | Edge sandbox | Cloudflare Sandbox SDK |
| **VI** | K8s-native / 自托管；CRD + gVisor/Kata 可选 | K8s / OSS sandbox | OpenSandbox、kubernetes-sigs/agent-sandbox、GKE Agent Sandbox |
| **VII** | 开源 Agent Harness（Agent-in-sandbox）；IM/Skills + 容器隔离 | Harness + container | NanoClaw、Bytebot |

**Type I vs VII**（均解决「安全执行」，买家不同）：I 为 **API 多租户沙箱**；VII 为 **自托管个人/小团队 Harness**——NanoClaw 与 OpenClaw **名字相近、系谱不同**。

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **Prompt injection → 沙箱逃逸链**：沙箱需 **网络默认拒绝 + 凭据隔离**，不能假设 LLM 会拒绝。
- **供应链**：Agent 自动安装 skill/MCP 包等同 **任意代码**——需签名渠道与执行隔离（与 [agent-skills.md](agent-skills.md) 交叉）。
- **过度持久化**：checkpoint 保留内存中的 **token/密钥**；TTL 与销毁策略必须可审计。
- **共享宿主机侧信道**：容器级隔离对 **最高安全多租户** 可能不足。
- **合规与数据驻留**：BYOC/VPC/on-prem vs 纯 SaaS。
- **厂商锁定**：各平台 SDK 与镜像格式不一。
- **成本失控**：长会话 + 高并发沙箱；需 **预算顶、自动 pause、hibernate** 策略。

---

## 落地碎片（无先后）

- 先画 **Sandbox-as-tool vs Agent-in-sandbox**（对照见 §专题对照）。
- **不可信来源**（公开 API、匿名用户）→ 优先 **microVM**（Type I），不要仅依赖共享内核容器。
- **需要 GPU 在沙箱内** → Modal 等 gVisor+GPU 路径（Type II）。
- **需要数小时 Devbox** → Daytona / persistent 平台（Type III）；确认 snapshot 与 **网络策略** 默认值。
- **已在 AWS/GCP/Vercel 栈内** → 评估 bundled 产品 TCO 与 **egress 硬ening**（Type IV）。
- **K8s 已有** → GKE Agent Sandbox / OpenSandbox / SIG agent-sandbox CRD（Type VI）。
- 与 [authentication.md](../infrastructure/authentication.md) 分工：**沙箱管执行边界**，Arcade 等管 **OAuth/connection**。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **E2B** | I | Firecracker microVM；AI Agent 代码执行标杆；pause/resume + snapshot | [e2b.dev](https://e2b.dev) |
| **Modal** | II | gVisor 隔离；Sandboxes + GPU；serverless 按秒计费 | [modal.com](https://modal.com) |
| **Daytona** | III | 持久 workspace；冷启动 27–90ms 叙事；Computer Use/GPU 扩展 | [daytona.io](https://www.daytona.io) |
| **AWS Bedrock AgentCore** | IV | 托管 Agent Runtime + Code Interpreter；microVM；最长 8h 会话 | [docs.aws.amazon.com/bedrock-agentcore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) |
| **Google Agent Sandbox** | IV | Gemini Enterprise 执行层；2026 preview；gVisor/加固容器 | [cloud.google.com](https://cloud.google.com/) |
| **Vercel Sandbox** | IV | Firecracker；持久化默认；毫秒级创建叙事 | [vercel.com](https://vercel.com/) |
| **Cloudflare Sandbox SDK** | V | Workers 上容器 + isolate；与 Workers AI 集成 | [developers.cloudflare.com](https://developers.cloudflare.com/) |
| **Blaxel** | I | microVM + **hibernate 待机零算力**；sub-25ms resume | [blaxel.ai](https://blaxel.ai) |
| **Northflank** | VI | BYOC；Kata/gVisor；企业 VPC + GPU | [northflank.com](https://northflank.com) |
| **OpenSandbox** | VI | 自托管；Firecracker/Kata/gVisor；K8s 原生 | [github.com/opensandbox-group/opensandbox](https://github.com/opensandbox-group/opensandbox) |
| **kubernetes-sigs/agent-sandbox** | VI | K8s SIG Apps；Sandbox CRD | [agent-sandbox.sigs.k8s.io](https://agent-sandbox.sigs.k8s.io) |
| **NanoClaw** | VII | 开源轻量 OpenClaw 替代；Docker/Apple Container 隔离；Claude Agent SDK | [github.com/qwibitai/NanoClaw](https://github.com/qwibitai/NanoClaw) |

### 对比与测评（第三方；观点非官方）

2026 年上半年行业共识是 **「Agent 沙箱」已成独立基础设施品类**，且 **大厂集体进场**（Vercel、Cloudflare、AWS、Google）。Ry Walker Research（2026-03/06）归纳：独立 Tier 由 E2B（规模与安全，Type I）、Modal（GPU，Type II）、Daytona（开源+Devbox，Type III） 领导；持久化与 checkpoint 从差异化变为 **标配**。

Work-Bench 将 **Agent Runtime** 定义为包含 Execute（沙箱）在内的更大栈；Execute 层核心 trade-off 是 **Firecracker 安全 vs gVisor/GPU vs Docker 速度**（对照见 §专题对照）。

**NanoClaw / NanoCo**：据 2026 年科技媒体报道，NanoCo 完成 Seed 融资；产品定位为 **容器隔离的个人/企业 Agent Harness（Type VII）**，与 E2B 的 **API 多租户沙箱（Type I）** 买家不同。与 OpenClaw **名字相近、系谱不同**。

*本小节为网摘与行业观点综合，非 Alignify 实测。*

---
## 延伸阅读 · 站内外

**站外**

- **AI Agent Sandboxes Compared**（Ry Walker Research, 2026）：<https://rywalker.com/research/ai-agent-sandboxes>
- **The Rise of the Agent Runtime**（Work-Bench, 2026）：<https://www.work-bench.com/post/the-rise-of-the-agent-runtime>
- **About GKE Agent Sandbox**（Google Cloud 文档）
- **kubernetes-sigs/agent-sandbox Overview**

**站内**

- Agent Runtime：[agent-runtime.md](agent-runtime.md)——完整执行层 SSOT；本文侧重 Execute（隔离）层
- Agent Identity：[agent-identity.md](agent-identity.md)——企业 Agent IAM；OAuth 出站见 [authentication.md](../infrastructure/authentication.md)
- Agent Skills：[agent-skills.md](agent-skills.md)
- Headless Browser：[headless-browser.md](../web-data/headless-browser.md)
- OpenClaw 系谱：[openclaw-alternatives.md](openclaw-alternatives.md)