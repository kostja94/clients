# Commonstack Features 功能与能力

> **本文职责**：协议端点、模型与计费、开发者体验、路线图、URL 建议；**不含**客户概览、关键词表、竞品、GitHub 仓库清单（见 [commonstack.md](./commonstack.md) 及各子文档）。  
> 关联：[commonstack.md](./commonstack.md) | [commonstack-open-source.md](./commonstack-open-source.md) | [commonstack-keywords.md](./commonstack-keywords.md) | [commonstack-use-cases.md](./commonstack-use-cases.md) | [commonstack-competitors.md](./commonstack-competitors.md) | [commonstack-growth-strategy.md](./commonstack-growth-strategy.md) | [commonstack-site-structure.md](./commonstack-site-structure.md)  
> 基于 [docs.commonstack.ai](https://docs.commonstack.ai/)（About、Quickstart、Playground 等）

**与 [commonstack-use-cases.md](./commonstack-use-cases.md) 的边界**：本文写「**能做什么**」；用例文档写「**谁、在什么情境**」。

---

## 一、协议与端点

| 能力 | 说明 |
|------|------|
| **OpenAI 兼容 API** | Base URL：`https://api.commonstack.ai/v1` — 可与常见 OpenAI 风格客户端配合 |
| **Anthropic 兼容 API** | Base URL：`https://api.commonstack.ai` — 可与 Anthropic 风格集成配合 |
| **同一域名与同 Key** | 双协议共用同一 API Key，减少配置分叉（见官方 About 页） |
| **标准参数透传** | 文档说明沿用熟悉的请求参数，降低迁移摩擦 |

---

## 二、模型与提供商覆盖

- 文档列举：**OpenAI、Anthropic、Google、DeepSeek、MiniMax、智谱（Zhipu）、xAI** 等（具体型号与能力以 [Model Library](https://commonstack.ai/model-library) 为准）。
- **多模态**：在基础模型支持的前提下提供图像相关能力；文档提及 **image-to-text**、**text-to-image**，以及通过 **nanobanana** 的 **image-to-image** 编辑类能力。

---

## 三、计费与支付

| 项目 | 说明 |
|------|------|
| **模式** | 按 token 用量计费；文档表述为无强制月费类订阅（以官网条款为准） |
| **账单** | 多提供商合并计费，便于对账 |
| **支付** | 文档提及信用卡（Stripe）、支付宝等 |
| **新用户激励** | 首充 **20% bonus**，上限 **$500** 充值对应区间（以官网最新政策为准） |

---

## 四、开发者体验

| 项目 | 说明 |
|------|------|
| **Quickstart** | [quickstart](https://docs.commonstack.ai/overview/quickstart) — 宣称约 2 分钟内可完成首次调用 |
| **Playground** | [platform/playground](https://docs.commonstack.ai/platform/playground) — 在线试模型 |
| **支持** | 强调**非纯聊天机器人**，工程团队直接协助集成问题 |

---

## 五、与开源仓库的对应关系

托管 API 与 **Routing** 路线图（下文 §六）可与组织 [CommonstackAI](https://github.com/CommonstackAI) 下本地路由、OpenClaw 工具链形成「自托管 / 托管」对照；**仓库列表与 Star 等仅以** [commonstack-open-source.md](./commonstack-open-source.md) **为准**，本文不重复。

---

## 六、路线图（Coming soon）

| 能力 | 说明 |
|------|------|
| **Prompt caching** | 对支持该能力的模型，透传上游 prompt caching，降低重复上下文成本 |
| **Routing & fallback** | 按成本、延迟、吞吐等智能路由；上游不可用时自动 fallback |

上线后需在 Features 与竞品对比中同步更新差异化表述。

---

## 七、功能页 / URL 建议（独立建站时）

以下为 **建议** 的信息架构，便于 SEO 与文档分层（非承诺已存在）：

| 主题 | 建议路径 | 目标关键词方向 |
|------|----------|----------------|
| 模型目录 | /model-library（已有） | per-model pricing, LLM API list |
| OpenAI 兼容 | /docs/openai-compatible | OpenAI compatible API, base URL |
| Anthropic 兼容 | /docs/anthropic-compatible | Anthropic API gateway |
| 计费说明 | /pricing 或 /billing | token pricing, pay as you go LLM |
| 安全与合规 | /security | data handling, API key security |

---

*文档生成日期：2026-03-29 | 来源：[docs.commonstack.ai](https://docs.commonstack.ai/)、[github.com/CommonstackAI](https://github.com/CommonstackAI)*
