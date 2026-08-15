# Commonstack Use Cases

> **本文职责**：典型场景、Persona、不适用边界；**不含**功能参数表、关键词表、增长阶段表（见 [commonstack-features.md](./commonstack-features.md)、[commonstack-keywords.md](./commonstack-keywords.md)、[commonstack.md](./commonstack.md) §3）。  
> 关联：[commonstack.md](./commonstack.md) | [commonstack-features.md](./commonstack-features.md) | [commonstack-keywords.md](./commonstack-keywords.md)

产品形态一句话：见 [commonstack.md](./commonstack.md) 客户概览。

---

## 一、典型场景

| 场景 | 描述 | 价值 |
|------|------|------|
| **多模型应用** | 同一产品在聊天、摘要、代码、视觉等场景使用不同厂商模型 | 无需维护多套账户与 SDK 分叉 |
| **从单厂商迁移 / 扩展** | 已有 OpenAI 或 Anthropic 集成，希望增加 DeepSeek、Google 等 | 改 Base URL 与模型名即可试点 |
| **成本与可用性实验** | 对比延迟与单价；未来「路由 + fallback」上线后可进一步自动化 | 降低单点供应商风险（能力以路线图为准） |
| **Agent 与自动化** | 后台服务、工作流、Cron 任务统一走一条 HTTP API | 密钥与账单集中管理 |
| **小团队商业化** | 按量付费、合并账单，减少财务对账成本 | 适合初创与项目制客户 |

---

## 二、Persona

| Persona | 诉求 | Commonstack 契合点 |
|---------|------|---------------------|
| **后端工程师** | 稳定 API、清晰错误、兼容现有客户端 | 双协议、标准参数 |
| **全栈 / indie** | 少运维、快集成、能支付宝等 | 文档所述支付方式与 Quickstart |
| **技术负责人** | 供应商策略、成本可见性 | Model Library 定价、合并计费 |
| **AI 产品团队** | 快速试模型、A/B | Playground + 统一 Key |

---

## 三、不适用或需自行评估

| 情况 | 说明 |
|------|------|
| **强合规数据驻留** | 需核对官方数据处理、区域与 DPA，不能默认与直连厂商等价 |
| **超低延迟专用集群** | 若需专属推理集群或本地部署，需对比 Groq、自建等方案 |
| **非 LLM 工作流** | 图像/视频管线可能更适合 Fal、Replicate 等；与 Commonstack 重叠部分以模型能力为准 |

---

## 四、JTBD 映射表（v9 新增）

| 用户任务（JTBD） | 典型问法 | 意图类型 | 优先级 | 状态 | 建议承接（URL 或载体） |
|------------------|----------|----------|--------|------|------------------------|
| 从 OpenAI 迁移到多模型 API | "How do I switch from OpenAI to a multi-model API?" | 信息/商业 | P0 | 待建页 | /blog/migrate-from-openai, /docs/openai-compatible |
| 用一个 Key 调用多个厂商模型 | "single API key multiple LLMs" | 商业 | P0 | 已承接 | /、Model Library |
| 减少 LLM API 成本 | "reduce LLM API cost without switching providers" | 商业 | P0 | 待建内容 | /compare, /blog/llm-cost-optimization |
| 为 Agent 选择 API 网关 | "best API gateway for AI agents" | 商业 | P1 | 待建页 | /use-cases/agents |
| 用支付宝支付海外 LLM 服务 | "Alipay LLM API payment" | 商业 | P1 | 部分承接 | /pricing（待独立） |
| 同时用 DeepSeek 和 Claude | "use DeepSeek and Claude together one API" | 信息 | P1 | 已承接 | Model Library, Quickstart |
| 对比 OpenRouter 找个替代 | "OpenRouter alternative better Alipay" | 商业 | P1 | 待建页 | /compare |
| 统一管理多个 AI 供应商账单 | "consolidated LLM billing" | 商业 | P2 | 部分承接 | /pricing（待独立） |
| 自建 LLM 路由省钱 | "local LLM router cost saving" | 信息 | P2 | 已承接 | UncommonRoute GitHub, /open-source |
| 在合规环境下使用 LLM API | "LLM API data handling compliance" | 信息 | P2 | 待建页 | /security |

## 五、场景-功能-关键词交叉映射（v9 新增）

| 场景 | 核心功能 | 关键词簇 | Persona |
|------|----------|----------|---------|
| 多模型应用 | 双协议端点、多厂商模型接入 | unified LLM API, multi-provider AI API | 后端工程师、AI 产品团队 |
| 从单厂商迁移 | OpenAI 兼容、Anthropic 兼容、Quickstart | OpenAI compatible API, switch from OpenAI | 全栈/indie、后端工程师 |
| Agent 与自动化 | 标准参数透传、路由（路线图） | AI agent API gateway, LLM routing | AI 产品团队 |
| 成本实验 | 按 token 计费、Playground、Model Library | token billing LLM, LLM cost optimization | 技术负责人、全栈/indie |
| 小团队商业化 | 合并账单、支付宝、首充 bonus | Alipay LLM API, consolidated billing | 全栈/indie、初创团队 |

---

*落地页与博客选题、页面阶段规划：见 [commonstack-growth-strategy.md](./commonstack-growth-strategy.md)。网站结构：见 [commonstack-site-structure.md](./commonstack-site-structure.md)。*

---

*文档生成日期：2026-03-29 | 最近更新：2026-05-10（v9 扩充：新增 JTBD 映射表 §4、场景-功能-关键词映射 §5）*

