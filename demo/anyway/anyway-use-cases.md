# Anyway 使用场景与用户故事

> **本文职责**：典型人物画像、JTBD、场景-功能映射、用户旅程、不适用边界。产品概览、功能、关键词、竞品详见各自子文档。面向海外市场，人物画像对齐国际 AI Agent 开发者和企业用户。
> 关联文档：[anyway.md](./anyway.md) | [anyway-features.md](./anyway-features.md) | [anyway-keywords.md](./anyway-keywords.md) | [anyway-competitors.md](./anyway-competitors.md) | [anyway-growth-strategy.md](./anyway-growth-strategy.md) | [anyway-site-structure.md](./anyway-site-structure.md) | [anyway-brand-visual.md](./anyway-brand-visual.md) | [README.md](./README.md)

---

## 1. 核心人物画像

### 人物 1：AI 创业团队 CTO（Aiden）

| 属性 | 描述 |
|------|------|
| 标签 | Aiden，34 岁，AI 创业公司 CTO |
| 所在地 | 旧金山湾区，美国 |
| 公司阶段 | Seed/Series A，15 人团队 |
| 技术栈 | LangChain、OpenAI API、Node.js/Python |
| 痛点 | 构建了一个多 Agent 系统让 Agent 自主完成工作流，但当 Agent 需要调用付费 API 或在 Agent 之间分配任务并支付时，整个流程被卡住 — 需要人工介入处理支付 |
| 目标 | 让 Agent 工作流真正实现端到端自主，包括支付环节 |
| 使用模式 | 集成 Anyway SDK 到现有 Agent 框架中；Agent 自动通过 SuperAPI 发现和调用所需 API |

**JTBD**：
1. 让我的 Agent 能够自主调用和支付第三方 API，不需要我预注册每个 API Key
2. 当一个 Agent 把子任务委托给另一个 Agent 时，能自动处理支付和任务验证
3. 有完整的可审计记录，证明 Agent 的每一笔支付决策都是合理的

### 人物 2：独立开发者（Zara）

| 属性 | 描述 |
|------|------|
| 标签 | Zara，28 岁，独立 AI 开发者 |
| 所在地 | 柏林，德国 |
| 产品 | 构建了一个垂直领域的 AI Agent SaaS 服务 |
| 用户规模 | 200+ 付费用户 |
| 痛点 | 想让 Agent 服务按用量计费，但现有支付方案（Stripe）只支持固定订阅或一次性支付，无法实现 Agent 友好的动态计费 |
| 目标 | 将自己的 Agent 服务货币化 — 按实际交付价值收费，而不是固定的月度订阅 |
| 使用模式 | 使用 Anyway 生成支付链接、管理订阅和按用量计费 |

**JTBD**：
1. 给我的 Agent 服务设置灵活的价格模型（按调用、按成果、按时间等）
2. 让客户能够自动支付 Agent 交付的服务，不需要手动处理每笔交易
3. 通过 Agent Traces 向客户证明我的 Agent 确实完成了约定的工作

### 人物 3：中型企业技术负责人（Marcus）

| 属性 | 描述 |
|------|------|
| 标签 | Marcus，41 岁，中型电商公司 VP of Engineering |
| 所在地 | 纽约，美国 |
| 团队 | 50+ 工程师，正在部署 AI Agent 系统 |
| 业务场景 | 使用 AI Agent 管理数字广告投放、供应商采购和客服运营 |
| 痛点 | 想让 Agent 直接管理广告预算和支付供应商，但安全和合规团队担心两个问题：(1) Prompt Injection 可能让 Agent 把预算转到错误的地方；(2) 无法审计 Agent 为什么要花某笔钱 |
| 目标 | 找到一种既能让 Agent 自主支付，又能满足企业安全合规要求的方案 |
| 使用模式 | 在 Agent 系统中部署 Anyway Secure Sandbox；使用 Agent Traces 为 SOX 审计提供证据 |

**JTBD**：
1. 给 Agent 设定支付策略（限额、白名单、审批规则）后，Agent 在策略范围内自主执行
2. 确保 Agent 的支付不会被 Prompt Injection 劫持
3. 生成可审计的 Agent 支付报告，满足合规要求

### 人物 4：Web3/DeFi 协议团队（Leo）

| 属性 | 描述 |
|------|------|
| 标签 | Leo，30 岁，DeFi 协议联合创始人 |
| 所在地 | 新加坡 |
| 项目 | 构建 AI Agent 驱动的 DeFi 策略平台 |
| 痛点 | Agent 可以分析链上数据并生成交易策略，但执行层的支付要么只能走 Crypto（限制了用户群），要么接入法币通道太复杂 |
| 目标 | 一套统一的支付方案，让 Agent 可以在法币和加密货币之间自由路由 |
| 使用模式 | 使用 Anyway 的法币/加密双通道，Agent 根据交易场景自动选择最优货币 |

**JTBD**：
1. 让 Agent 根据接收方偏好自动选择法币或加密货币支付
2. 通过 Agent Traces 记录链上+链下的完整执行过程
3. 一次集成覆盖多个支付场景，而不是分别集成法币和加密两套系统

---

## 2. 场景-功能-关键词映射

| 场景 | 使用功能 | 目标关键词 | 人物 |
|------|---------|-----------|------|
| Agent 调用付费 API | SuperAPI + Agent-Native Payments | API for AI agents、agent payment gateway、SuperAPI | Aiden |
| Agent 委托任务给其他 Agent | Agent-to-Agent Settlement + Agent Traces | agent-to-agent settlement、verifiable agent traces | Aiden、Leo |
| Agent 管理广告预算 | Agent-Native Payments + Secure Sandbox | autonomous procurement AI、agent ad spend | Marcus |
| Agent 服务按用量收费 | Monetization + Agent-Native Payments | monetize AI agent、agent subscription billing | Zara |
| 企业 Agent 支付合规 | Secure Sandbox + Agent Traces | secure agent transactions、prompt injection protection | Marcus |
| 法币/加密混合支付 | Multi-Protocol Routing + 双货币通道 | agent crypto payments、fiat crypto payment AI | Leo |
| 多 Agent 分账 | MPP + Agent-Native Payments | multi-party payment AI、agent revenue sharing | Aiden、Leo |

---

## 3. 典型用户旅程

### 旅程 1：开发者首次接入 → 首次 Agent 自主支付

```
1. 发现 → 通过 Google 搜索"agent payments"、X/Twitter 讨论或 AI 开发者社区发现 Anyway
2. 着陆 → 访问 anyway.sh，被"Agents can do almost anything. Except pay for it."戳中痛点
3. 评估 → 阅读 Features 和 Security 页，确认 Secure Sandbox 和 Agent Traces 满足需求
4. 接入 → npm/pip install anyway-sdk，按照 Quickstart 5 分钟完成集成
5. 配置 → 设置 Agent 支付策略（限额、白名单）
6. 首次运行 → Agent 自主调用 SuperAPI 的某个 API，自动完成支付并收到结果
7. 信任建立 → 在 Dashboard 查看 Agent Traces，看到完整的执行记录和安全验证
8. 扩展 → 启用更多协议（X402、ACP、MPP），让 Agent 访问更广泛的支付网络
```

### 旅程 2：独立开发者货币化 Agent 服务

```
1. 痛点触发 → 完成 Agent 产品开发，但 Stripe 的固定订阅模式不适配 Agent 按用量计费需求
2. 搜索 → "monetize AI agent"、"agent subscription billing"
3. 着陆 → 访问 Anyway /use-cases/monetize 页面
4. 上手 → 创建 Account，设置价格模型（按 API 调用 / 按任务 / 按时间）
5. 集成 → Agent 通过 Anyway SDK 生成 Payment Link，嵌入到服务交付流程中
6. 验证 → 客户 Agent 自动支付后，Agent Traces 同时向双方证明服务已完成
7. 持续 → Dashboard 监控收入、交易量、客户使用模式
```

### 旅程 3：企业合规评估 → 安全部署

```
1. 需求发起 → 工程团队提议让 Agent 自主管理支付 → 安全团队要求审查方案
2. 安全评估 → 安全团队审查 Secure Sandbox 的 Prompt Injection 防护机制和 Agent Traces 的可审计性
3. PoC → 在测试环境部署 Anyway，模拟 Prompt Injection 攻击验证防护效果
4. 策略配置 → 为 Agent 配置支付策略：单笔限额、日限额、白名单接收方
5. 灰度上线 → 先让 Agent 管理小额预算，观察 30 天
6. 审计验证 → 安全/合规团队审查 Agent Traces 报告
7. 全量部署 → Agent 全面接管指定范围内的支付执行
```

---

## 4. 不适用边界

| 不适用场景 | 原因 | 替代方案 |
|-----------|------|---------|
| 人类消费者支付场景 | Anyway 为 Agent-to-Agent/Agent-to-Service 设计 | Stripe Checkout、PayPal |
| 高频交易支付 | 毫秒级支付不是 Agent 支付的核心需求 | 专用交易系统 |
| 纯人工审批流程 | Anyway 的价值在于 Agent 自主性 | 传统 ERP 中的支付审批流 |
| 非 AI Agent 场景 | 如果不需要 Agent 自主决策，传统支付方案更成熟 | Stripe、Adyen |
| 纯现金/线下支付 | Anyway 的数字支付基础设施无法覆盖 | 传统 POS / 银行转账 |

---

## 5. 用户增长假设

| 假设 | 验证方法 | 优先级 |
|------|---------|--------|
| "Agent 被卡在支付环节"是广泛存在的痛点 | Waitlist 注册用户的痛点调研 | P0 |
| 开发者愿意为 Agent 原生支付切换/新增支付方案 | 集成率 vs. Waitlist 注册率 | P0 |
| Secure Sandbox 是企业采用的核心决策因素 | 企业用户访谈 | P1 |
| SuperAPI 是主要的激活和留存钩子 | 功能使用分析 | P1 |
| 独立开发者货币化需求是早期最大的付费市场 | 付费用户调研 | P1 |
| Agent 支付网络效应（用的人越多，价值越大） | 网络密度分析 | P2 |

---

*文档创建：2026-07-09 | 模式：Mode A 冷启动 — 国际版 | 人物画像：基于网站目标用户描述 + Agent 支付市场研究推导*
