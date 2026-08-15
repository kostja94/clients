# Anyway — AI Agent 金融操作系统

> **本文职责**：本文件只承担 **产品概览、定位、核心架构、产品矩阵与关键外链**。关键词全表、竞品拆解、功能明细、使用场景、增长策略、网站结构均以子文档为准，避免重复。面向海外市场，关键词、竞品、人物画像均对齐国际语境。

## 文档导航

| 文档 | 职责 |
|------|------|
| [anyway-features.md](./anyway-features.md) | Agent-Native Payments、多协议统一路由、Secure Sandbox、Verifiable Agent Traces、SuperAPI |
| [anyway-use-cases.md](./anyway-use-cases.md) | 人物画像、JTBD、场景-功能映射、用户旅程、不适用边界 |
| [anyway-keywords.md](./anyway-keywords.md) | 关键词分类（品牌/核心功能/差异化/长尾/竞品截流）、意图分析、目标页映射 |
| [anyway-competitors.md](./anyway-competitors.md) | 竞品矩阵（传统支付/Agent 支付协议/Agent 基础设施）、场景级对照、差异化分析 |
| [anyway-growth-strategy.md](./anyway-growth-strategy.md) | 增长渠道、开发者策略、战役节奏、话术框架、KPI 指标 |
| [anyway-site-structure.md](./anyway-site-structure.md) | 页面优先级、URL 架构、导航层级、关键词/场景/增长映射 |
| [anyway-brand-visual.md](./anyway-brand-visual.md) | 品牌色彩、字体、Logo、图标系统、UI 组件风格 |
| [README.md](./README.md) | 文件夹索引与文件清单 |

*产品入口*：[anyway.sh](https://anyway.sh/)

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | Fintech / AI Agent 基础设施 / 支付网络 |
| 网站 | https://anyway.sh/ |
| 产品形态 | **Agent 金融操作系统**：Agent-Native Payments（Agent 原生支付网络）+ SuperAPI（统一 API 网关），让 AI Agent 自主完成收款、付款和结算 |
| 当前阶段 | 邀请制 Waitlist，尚未公开上线 |
| 核心产品 | **Agent-Native Payments**：Agent 自主支付、收款与结算网络；**SuperAPI**：一次安装给 Agent 所需全部 API，按调用计费 |
| 目标用户 | SMB（中小企业）、创业团队使用 AI Agent 进行商业运营；独立开发者将 AI Agent 货币化 |
| 关键差异化 | Agent 原生设计（非传统支付 API 封装）；统一 X402/ACP/MPP 等多协议路由；Secure Sandbox 防 Prompt 注入劫持；Verifiable Agent Traces（可验证 Agent 执行追溯） |
| 支持协议 | X402、ACP、MPP 等 Agent 支付协议 |
| 支持货币 | 法币 + 加密货币 |
| 团队背景 | 由世界级机构资深运营人士组成 |
| 更新日期 | 2026-07-09 |

---

## 公司背景（2026-07）

| 项目 | 内容 |
|------|------|
| 定位 | AI Agent 时代的支付网络基础设施 |
| 公司阶段 | 早期，邀请制 Waitlist 阶段 |
| 核心叙事 | "Agents can now do almost anything. Except pay for it." — 填补 Agent 自主支付能力空白 |
| 市场时机 | 2026 年为 Agentic AI 元年，Agent-to-Agent 自主交易需求爆发；支付协议碎片化（X402、ACP、MPP 等多标准并存）创造了统一层的机会 |
| 团队 | 由世界级机构资深运营人士组建 |
| 来源 | [anyway.sh](https://anyway.sh/) 网站内容 |

---

## 1. 产品定位与价值主张

**Anyway** 是面向 AI Agent 时代的支付网络。核心洞察："Agent 现在几乎能做任何事情，除了付钱。"

当前支付基础设施（Stripe、PayPal、银行转账）全部是为人类设计的 — 需要人工认证、浏览器交互、手动审批。AI Agent 虽然可以自主决策、执行任务，但一到需要付款时就被卡住。

Anyway 提供 **Agent-Native Payments**：从零为 AI Agent 设计的支付基础设施，让 Agent 可以自主收款、付款和结算。同时提供 **SuperAPI** — 一次安装即可让 Agent 获得所有需要的 API 能力，按调用计费。

### 核心价值主张

| 维度 | 主张 |
|------|------|
| Agent 原生 | 从零为 Agent 设计，不是传统支付 API 的 Agent 封装 — 支持 Agent 自主决策后的直接执行 |
| 协议统一 | 一次集成覆盖 X402、ACP、MPP 等所有主流 Agent 支付协议，同时支持法币和加密货币 — 不用逐个对接 |
| 安全沙箱 | 独立安全沙箱防止 Prompt Injection 劫持 Agent 交易 — 解决 Agent 支付的核心安全风险 |
| 可验证追溯 | 证明 Agent 执行了什么，而不仅仅是支付了什么 — Agent Traces 提供完整的可审计执行记录 |
| 按需 API | SuperAPI — 一次安装给 Agent 全部所需 API，按调用计费，无需管理多个 API Key |

---

## 2. 产品矩阵

### 2.1 Agent-Native Payments（核心产品）

```
Agent 发起支付意图
        ↓
Secure Sandbox（安全沙箱验证）
        ↓
协议路由层（自动选择 X402 / ACP / MPP）
        ↓
货币路由层（法币 / 加密货币）
        ↓
交易执行
        ↓
Verifiable Agent Traces（生成可验证执行记录）
```

### 2.2 SuperAPI（API 网关）

一次安装即可让 Agent 获得所有所需的 API 能力：

| 特性 | 描述 |
|------|------|
| 统一接入 | 单一 SDK / API Key 接入所有第三方 API |
| 按调用计费 | 无需为每个 API 单独管理订阅和额度 |
| 自动发现 | Agent 可自动发现和调用所需 API 能力 |
| 内置计费 | API 调用与支付系统深度集成，使用即付 |

> 完整的功能拆解与架构分析见 [anyway-features.md](./anyway-features.md)。

---

## 3. 核心使用场景

| 场景 | 描述 |
|------|------|
| **Agent-to-Agent 结算** | 当一个 Agent 雇佣另一个 Agent 时，Anyway 处理支付、通过 Agent Traces 验证任务、完成结算 — 全链路自主 |
| **替代人工执行支付** | 让 Agent 处理广告投放、采购和运营中的支付环节 — 直接向供应商付款并自动验证结果 |
| **Agent 服务货币化** | 将自己的 Agent 变成一门生意 — 生成支付链接、支持订阅和按用量计费、为 Agent 交付的服务收费 |
| **Agent 按需支付 API** | Agent 需要工具才能工作 — Anyway 让它们自动发现、调用并支付 API、工具和服务 |

> 完整的人物画像、用户旅程与场景分析见 [anyway-use-cases.md](./anyway-use-cases.md)。

---

## 4. 竞品格局（摘要）

> 完整竞品矩阵、场景级对照表、SWOT 分析见 [anyway-competitors.md](./anyway-competitors.md)。

Agent 支付赛道分为四类参与者：

| 赛道 | 代表产品 | Anyway 的关键差异 |
|------|---------|------------------|
| 传统支付平台 | Stripe、PayPal、Adyen | 全为人类设计，无 Agent 原生支持；需浏览器/人工认证 |
| Agent 支付协议 | X402、ACP、MPP | 单协议覆盖，碎片化问题；无统一路由层 |
| Crypto/Web3 支付 | Solana Pay、USDC on Base | 仅加密货币，缺少法币通道；安全模型不适用 Agent 场景 |
| Agent 基础设施 | LangChain、AutoGPT | 编排/工具层，无原生支付能力 |

**Anyway 的竞争真空**：[Agent 原生支付] + [多协议统一路由] + [法币/加密双通道] + [Secure Sandbox] + [Verifiable Traces] 的独特组合。目前没有产品同时覆盖这五个维度。

---

## 5. 关键指标（预估）

| 指标 | 数据 | 备注 |
|------|------|------|
| 阶段 | 邀请制 Waitlist | 尚未公开上线 |
| 核心产品 | 2 个 | Agent-Native Payments + SuperAPI |
| 支持协议 | 3+ | X402、ACP、MPP |
| 支持货币 | 法币 + 加密 | 双通道 |
| 目标市场 | 全球 | SMB + 创业团队 + 独立开发者 |

---

*文档创建：2026-07-09 | 模式：Mode A 冷启动 — 国际版 | 主来源：[anyway.sh](https://anyway.sh/) 网站内容 | 网站抓取日期：2026-07-09*
