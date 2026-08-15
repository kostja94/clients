# Anyway 功能分析 — 能力与产品拆解

> **本文职责**：核心功能模块、Agent-Native Payments 架构、多协议统一路由、Secure Sandbox、Verifiable Agent Traces、SuperAPI。产品概览、关键词、竞品、使用场景、增长策略见各自子文档。面向海外市场，功能名称与表述对齐国际语境。
> 关联文档：[anyway.md](./anyway.md) | [anyway-keywords.md](./anyway-keywords.md) | [anyway-competitors.md](./anyway-competitors.md) | [anyway-use-cases.md](./anyway-use-cases.md) | [anyway-growth-strategy.md](./anyway-growth-strategy.md) | [anyway-site-structure.md](./anyway-site-structure.md) | [anyway-brand-visual.md](./anyway-brand-visual.md) | [README.md](./README.md)
> 基于 [anyway.sh](https://anyway.sh/) 网站内容

---

## 1. Agent-Native Payments（核心引擎）

### 1.1 架构概览

```
Agent 发起支付意图
        ↓
Secure Sandbox（安全沙箱验证）
   ├── 检测 Prompt Injection 攻击模式
   ├── 验证支付意图与任务上下文一致性
   └── 交易参数安全校验
        ↓
协议路由层（自动协议选择）
   ├── X402（HTTP 402 Payment Required）
   ├── ACP（Agent Communication Protocol）
   ├── MPP（Multi-Party Payment）
   └── 未来新增协议热插拔
        ↓
货币路由层（自动货币选择）
   ├── 法币通道（USD、EUR 等）
   └── 加密货币通道（USDC 等）
        ↓
交易执行
   ├── 发送方扣款
   ├── 接收方收款
   └── 结算确认
        ↓
Verifiable Agent Traces（生成可验证执行记录）
   ├── 支付决策上下文
   ├── 安全沙箱验证结果
   ├── 协议与货币路由选择
   └── 密码学签名执行追溯
```

### 1.2 与传统支付的架构差异

| 维度 | 传统支付（Stripe/PayPal） | Agent-Native Payments（Anyway） |
|------|--------------------------|-------------------------------|
| 认证方式 | 人工浏览器认证、3D Secure、短信验证 | Agent 身份密钥、安全沙箱自动验证 |
| 决策主体 | 人类审批 | Agent 自主决策 + 安全沙箱保护 |
| 安全模型 | 反欺诈模型（人类行为分析） | Prompt Injection 防护 + 任务上下文一致性验证 |
| 审计追溯 | 支付记录、收据 | 支付记录 + 完整 Agent 执行追溯 |
| 协议层 | 单一 HTTP API | 多协议统一路由 |
| 货币支持 | 主要法币 | 法币 + 加密货币双通道 |
| API 设计 | 为开发者设计 | 为 Agent 设计 |

---

## 2. One Integration, Every Protocol（多协议统一路由）

### 2.1 协议覆盖

| 协议 | 描述 | 应用场景 |
|------|------|---------|
| **X402** | HTTP 402 Payment Required — 基于 HTTP 状态码的机器支付协议 | Web API 按调用付费、AI 模型 API 按 token 计费 |
| **ACP** | Agent Communication Protocol — Agent 间通信与交易协议 | Agent-to-Agent 协作、多 Agent 工作流支付 |
| **MPP** | Multi-Party Payment — 多方支付协议 | 多 Agent 分账、供应链 Agent 协同支付 |

### 2.2 路由逻辑

| 维度 | 路由策略 |
|------|---------|
| 接收方能力 | 自动检测接收方支持的协议，优先选择最高效的 |
| 成本优化 | 比较不同协议/网络的交易费用，选择成本最低的 |
| 速度要求 | 根据交易时效性需求选择最快结算通道 |
| 货币偏好 | 根据发送方/接收方的货币偏好自动路由 |
| 合规要求 | 根据交易地区自动选择合规通道 |

### 2.3 协议热插拔

架构设计支持新协议的即插即用：

```
[Agent SDK]
     ↓
[协议抽象层]  ← 标准化支付意图接口
     ↓
[协议适配器]  → X402 Adapter
              → ACP Adapter
              → MPP Adapter
              → 未来协议 Adapter（热插拔）
     ↓
[货币适配器]  → 法币 Adapter
              → Crypto Adapter
```

---

## 3. Secure Sandbox（安全沙箱）

### 3.1 解决的问题

AI Agent 容易受到 **Prompt Injection**（提示注入）攻击 — 攻击者可能在 Agent 处理的数据中嵌入恶意指令，诱骗 Agent 执行未经授权的支付。

Anyone 的 Secure Sandbox 是独立于 Agent 执行环境的安全验证层，在交易执行前进行安全校验。

### 3.2 安全验证流程

```
Agent 任务执行环境
        ↓
支付意图生成
        ↓
══════════════════════════════════
       SECURE SANDBOX
══════════════════════════════════
        ↓
1. Prompt Injection 检测
   ├── 输入数据扫描（检测注入模式）
   ├── 上下文一致性验证
   └── 异常指令识别
        ↓
2. 支付意图验证
   ├── 金额合理性校验
   ├── 接收方身份验证
   └── 任务-支付匹配度检查
        ↓
3. 权限与策略执行
   ├── Agent 支付限额策略
   ├── 白名单/黑名单检查
   └── 多签策略（如配置）
        ↓
══════════════════════════════════
       SECURE SANDBOX 通过
══════════════════════════════════
        ↓
交易执行 → Verifiable Agent Traces
```

### 3.3 安全分层策略

| 层级 | 策略 | 描述 |
|------|------|------|
| L1：输入层 | Prompt Injection 检测 | 扫描所有进入 Agent 的数据，识别恶意注入模式 |
| L2：意图层 | 上下文一致性验证 | 确保支付意图与 Agent 当前执行的任务上下文匹配 |
| L3：策略层 | 支付策略强制执行 | 应用预定义的限额、白名单、审批规则 |
| L4：执行层 | 交易隔离执行 | 在沙箱环境中执行交易，防止外部干扰 |

---

## 4. Verifiable Agent Traces（可验证执行追溯）

### 4.1 核心价值

传统支付只能回答"谁付了多少钱给谁"。Verifiable Agent Traces 还能回答：
- Agent **为什么**做出这个支付决策
- Agent 在支付前**执行了什么**任务验证
- 支付是否**符合预期**的安全策略
- 整个链条是否可以**独立验证**

### 4.2 追溯数据结构

| 组件 | 内容 | 可验证性 |
|------|------|---------|
| 任务上下文 | Agent 正在执行的任务描述、输入数据 | 哈希链保证完整性 |
| 决策日志 | Agent 做出支付决策的推理过程 | 可独立审计 |
| 安全验证 | Secure Sandbox 的验证结果（注入检测、意图匹配等） | 密码学签名 |
| 交易记录 | 支付金额、双方身份、协议、货币、时间戳 | 区块链/账本可查 |
| 任务结果 | 支付后的任务执行结果验证 | 可验证的完成证明 |

### 4.3 使用场景

| 场景 | 追溯价值 |
|------|---------|
| Agent 雇佣 Agent | 证明被雇佣的 Agent 确实完成了任务后，才释放付款 |
| 企业 Agent 运营 | 审计 Agent 的所有支付决策，满足 SOX/合规要求 |
| 开发者调试 | 回溯 Agent 的支付行为，排查异常交易 |
| 争议解决 | 提供完整的可验证记录解决支付争议 |

---

## 5. SuperAPI（统一 API 网关）

### 5.1 架构

```
Agent
  ↓
SuperAPI SDK（单一 SDK）
  ↓
API 网关
  ├── API 发现与注册
  ├── 协议路由（X402/ACP/MPP）
  ├── 计费引擎（按调用计费）
  └── 安全沙箱集成
  ↓
第三方 API 池
  ├── AI 模型（OpenAI、Anthropic 等）
  ├── 数据 API（天气、搜索、新闻等）
  ├── 工具 API（邮件、日程、CRM 等）
  └── 垂直 API（金融、医疗、物流等）
```

### 5.2 与传统 API 管理的区别

| 维度 | 传统方式 | SuperAPI |
|------|---------|---------|
| 接入方式 | 每个 API 单独申请 Key、单独计费 | 一次安装，一个 Key 访问所有 |
| 计费模式 | 分别管理多个订阅和额度 | 统一按调用计费，自动结算 |
| API 发现 | 开发者手动查找和集成 | Agent 自动发现所需 API |
| 支付集成 | 需额外集成支付 | API 调用与支付深度集成 |
| 安全 | 依赖各 API 自己的安全策略 | 统一 Secure Sandbox 保护 |

---

## 6. 功能总结

| 功能模块 | 成熟度 | 描述 |
|---------|--------|------|
| Agent-Native Payments | Beta/Waitlist | Agent 自主收款、付款、结算 |
| 多协议统一路由 | Beta/Waitlist | X402、ACP、MPP 统一接入 |
| Secure Sandbox | Beta/Waitlist | Prompt Injection 防护 + 支付安全验证 |
| Verifiable Agent Traces | Beta/Waitlist | 可验证的 Agent 执行追溯 |
| SuperAPI | Beta/Waitlist | 统一 API 网关，按调用计费 |

---

*文档创建：2026-07-09 | 模式：Mode A 冷启动 — 国际版 | 来源：[anyway.sh](https://anyway.sh/) 网站内容*
