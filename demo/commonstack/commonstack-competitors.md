# Commonstack 竞品分析

> **本文职责**：竞品类型、代表产品、与 Commonstack 的差异；**不含**关键词映射表（见 [commonstack-keywords.md](./commonstack-keywords.md)）。自托管分布式推理（Parallax）与托管 API 的分工见 [commonstack-ecosystem.md](./commonstack-ecosystem.md)。  
> 关联：[commonstack.md](./commonstack.md) | [commonstack-ecosystem.md](./commonstack-ecosystem.md) | [commonstack-use-cases.md](./commonstack-use-cases.md) | [commonstack-keywords.md](./commonstack-keywords.md) | [commonstack-growth-strategy.md](./commonstack-growth-strategy.md) | [commonstack-site-structure.md](./commonstack-site-structure.md)

产品形态一句话与官方入口：见 [commonstack.md](./commonstack.md)；技术事实以 [About Commonstack](https://docs.commonstack.ai/) 为准。

---

## 一、竞品类型拆解

| 类型 | 核心场景 | 代表 | 与 Commonstack 关系 |
|------|----------|------|---------------------|
| **A. 多模型聚合 API** | 统一路由、兼容 OpenAI 等 | OpenRouter、Together、Fireworks、Portkey | 最直接可比 |
| **B. 极速推理云** | 低延迟 Llama 等 | Groq | 部分场景重叠；Groq 更偏自研推理栈 |
| **C. 媒体 / 生成 API** | 图像、视频工作流 | Fal、Replicate | 与 LLM 网关交叉在「多模型一站式」；Fal 更偏生成管线 |
| **D. 直连云** | 官方 SLA、全量功能 | OpenAI、Anthropic、Google | 客户可能「直连 + 聚合」并存 |

---

## 二、A. 多模型聚合 API

| 竞品 | 定位摘要 | 与 Commonstack 对比维度 |
|------|----------|---------------------------|
| **[OpenRouter](https://openrouter.ai/)** | 大量模型、OpenAI 兼容、竞价与路由 | 模型数量与社区生态通常更强；Commonstack 强调 **Anthropic 原生兼容端点 + OpenAI 双协议同 Key**、支付与支持方式（见各自官网） |
| **Together AI** | 开源模型、专用推理 | 偏开源模型与自托管叙事；聚合层逻辑类似 |
| **Fireworks** | 企业级推理、开源与微调 | 偏企业与低延迟集群 |
| **Portkey** | 网关 + 可观测 + 路由 | 偏「控制面」与可观测；Commonstack 若强化 routing 则边界接近 |

**Commonstack 差异化（基于公开文档，需随产品迭代核对）**：

- 明确 **两套协议端点**（OpenAI `/v1` 与 Anthropic 根路径）同域同 Key  
- **支付宝**等与地区相关的支付选项（文档提及）  
- **Prompt caching、智能路由与 fallback** 在路线图中 —— 上线后与 OpenRouter 等对比需更新  

---

## 三、B. Groq 等低延迟云

| 竞品 | 说明 |
|------|------|
| **Groq** | LPU 推理、延迟极优；模型列表以官方为准 |

**关系**：若用户需求是「极致 tokens/s」，可能优先 Groq；Commonstack 定位更偏 **多厂商一站式与双协议兼容**，可并存于架构中（不同路径调不同供应商）。

---

## 四、C. Fal、Replicate（媒体与生成）

| 竞品 | 说明 |
|------|------|
| **[Fal](https://fal.ai/)** | 图像/视频等生成 API、Serverless GPU、工作流 |
| **Replicate** | 模型市场、多模态与生成类 API |

**关系**：Commonstack 文档强调 **LLM 网关** 与多模态（视觉、文生图等）。与 Fal 的重叠主要在「少对接多家、统一计费」的体验，但 **Fal 更侧重生成与媒体管线**，比价时应分场景：纯聊天/Agent 用聚合 LLM API；重生成管线可对比 Fal/Replicate。

---

## 五、Gaps 与机会（对 Commonstack）

| 维度 | 机会 |
|------|------|
| **文档与 SEO** | Model Library、迁移指南、与 OpenRouter 的客观对比页 |
| **路线图** | caching、routing 上线后形成与「仅聚合列表」类产品的差异叙事 |
| **信任** | 安全白皮书、数据流、区域与合规页面（视目标市场） |
| **开发者关系** | 示例仓库、CI 里换 Base URL 的模板 |

---

## 六、场景级竞品对照表（v9 新增）

### 6.1 场景：Agent 开发与工具调用

| 维度 | Commonstack | OpenRouter | Portkey | LiteLLM |
|------|-------------|------------|---------|---------|
| **Agent 专用路由** | 路线图（智能路由 + fallback） | Adaptive Quality Routing（5 分钟重评估） | 可观测 + 网关 | 自托管路由 |
| **工具调用支持** | 标准参数透传 | 标准 | 标准 | 标准 |
| **成本控制** | 按 token 合并账单 | 按 token | 按请求/企业 | 自控 |
| **部署** | 托管 API + 自托管（UncommonRoute） | 仅托管 | 托管 | 仅自托管 |

### 6.2 场景：成本敏感型初创团队

| 维度 | Commonstack | OpenRouter | Together AI | 直连 DeepSeek |
|------|-------------|------------|-------------|---------------|
| **最低成本模型** | 多厂商（含 DeepSeek、MiniMax） | 300+ 模型，含免费模型 | 偏开源模型 | 极低价（$0.14/M） |
| **计费透明度** | 合并账单，首充 20% bonus | 无加价透传 | 声称 60% 成本节省 | 极简 |
| **支付宝支持** | ✓（文档提及） | ✗ | ✗ | ✗ |
| **供应商锁定风险** | 低（多厂商） | 低 | 中（偏开源） | 高（单厂商） |

### 6.3 场景：中国企业 / 合规需求

| 维度 | Commonstack | 硅基流动 (SiliconFlow) | 七牛云 AI | 百度千帆 |
|------|-------------|----------------------|-----------|----------|
| **国产模型覆盖** | DeepSeek、MiniMax、智谱 | 全（华为昇腾部署） | 全 | 全（文心系列） |
| **Claude 直连** | ✓（Anthropic 原生协议） | ✗ | ✓ | ✗ |
| **合规认证** | 待确认 | 政企方案 | 商用 | 等保 2/3 级 |
| **支付宝** | ✓ | 待确认 | 待确认 | 微信/支付宝 |
| **国际模型覆盖** | OpenAI、Anthropic、Google、xAI | 偏国产 | 有 | 偏国产 |

---

## 七、竞品动态（2026 Q1-Q2 快照）

| 日期 | 事件 | 对 Commonstack 的影响 |
|------|------|----------------------|
| 2026-04 | 中国模型在 OpenRouter 的 token 份额升至 36% | 强化「国产模型覆盖 + 支付宝」差异化 |
| 2026-04 | OpenRouter 周 token 量突破 12 万亿 | 市场快速增长，Commonstack 需加速内容覆盖 |
| 2026-04 | AI.cc 报告 API 集成 300% YoY 增长 | 新用户涌入期，Quickstart 体验是转化关键 |
| 2026-03 | Gradient Network $10M 融资 | 同团队品牌背书，可组合为「全栈 AI」故事 |
| 2026-Q1 | Agent 工作负载占新增集成 41% | 优先建设 Agent 场景内容和路由功能 |

*来源:联网检索，OpenRouter 公开数据，各公司公开页面*

---

*文档生成日期：2026-03-29 | 最近更新：2026-05-10（v9 扩充：新增场景级对照表 §6、竞品动态 §7） | 来源：[docs.commonstack.ai](https://docs.commonstack.ai/)、联网检索（2026-05）*
