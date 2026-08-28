# Agentic Payments · 知识块（非线性笔记）

**材料范围**：公开网络检索（Google AP2/UCP 规范、Coinbase x402 Foundation、Stripe ACP/MPP 文档、Visa TAP、Forrester/PYMNTS/Juniper 行业分析、FluxA/Clink/Basis Theory/Skyfire 官网与融资新闻、Crossmint/Alatirok 协议对比文）；**未**引用 Alignify 站内 JSON 为独立事实来源。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/agentic-payments](https://alignify.co/blog/agentic-payments) · `/zh/blog/agentic-payments` · `content/blog/en|zh/agentic-payments.md` · slug **`agentic-payments`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 `#agentic-payments-tools` · `keywordEn`: **Agentic Payments** · `keywordZh`: **智能体支付

## 与相邻 slug 分流

| slug | 典型读者问题 | 交付形态 | 与本 slug 的边界 |
|------|-------------|---------|------------------|
| **`agentic-payments`（本页）** | 「Agent 怎么授权、结算、走哪条支付协议？」 | x402/AP2/MPP/ACP 支付层、Agent Wallet、PCI/稳定币 rails | — |
| **`agentic-commerce`** | 「Agent 替我购物时经历什么？消费者/商家要准备什么？」 | 发现→比价→结账旅程、平台产品（Gemini/ChatGPT） | 本页只管**动钱**；commerce 管**买什么、在哪买** |
| **`ai-shopping`** | 「有哪些 AI 购物/商务工具值得对比？」 | 工具目录（ChatGPT Shopping、Glance、Nosto…） | shopping = **产品谱系**；本页 = **支付基础设施** |
| **`authentication`** | 「人类/Agent 如何 OAuth 接 SaaS？」 | CIAM、出站工具授权 | 本页含**支付授权/委托**，不含通用 IdP 选型 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **Agentic Payments / 智能体支付**：AI Agent 在用户授权边界内**发起、授权并完成支付**的金融能力——区别于人类点击「立即支付」，也区别于传统订阅 cron。核心难题是：**非人类参与者**如何过风控、留审计链、设 spending cap。
- **Authorization Layer / 授权层**：证明「用户同意这笔 spend」——Google **AP2**（Mandates：Intent/Cart/Payment）、Mastercard **Agentic Tokens**、京东 **A2P2** 任务委托凭证。回答 *who authorized*。
- **Checkout Layer / 结账层**：Agent 与商户握手创建订单——OpenAI+Stripe **ACP**（Agentic Commerce Protocol checkout）、Google **UCP** 中的 checkout 原语。回答 *what is being purchased*。
- **Settlement Layer / 结算层**：价值如何移动——**x402**（HTTP 402 + USDC 微支付）、Stripe **MPP**（Machine Payments Protocol，会话式 streaming pay）、卡组织现有 rails。回答 *how money moves*。
- **Agent Wallet / 智能体钱包**：Agent 持有或代理的支付容器——FluxA Agent Wallet/AgentCard、Fireblocks Agentic Payments Suite、支付宝「AI 钱包」额度管理。可与用户主卡分离，带预算信封（budget envelope）。
- **Agentic Payment Skill**：Agent 可调用的支付能力包——Clink 的 PCI L1 **Agentic Payment Skill**（信用卡/Apple Pay/本地钱包），与「加密-only 钱包」路线对照。
- **x402**：Coinbase+Cloudflare 发起、2026 年捐给 Linux Foundation 的 **HTTP 原生微支付**协议——`402 Payment Required` → 稳定币结算 → 重试带 payment header。适合 Agent→API、Agent→Agent 高频低价调用。
- **Verification / 验真层**：商户区分可信 Agent vs 恶意 bot——Visa **TAP**（Trusted Agent Protocol）、Cloudflare 联合试点。常与 AP2 Mandate 叠加，**不是**结算协议本身。

---

## 专题对照：支付栈六层（2026 行业共识）

| 层 | 典型协议/产品 | 解决什么 |
|----|--------------|---------|
| Discovery | UCP product schemas | Agent 如何知道商品与价格 |
| Communication | A2A、MCP | Agent 如何调用商户/API |
| Identity / Trust | TAP、KYA、ARI（A2P2） | Agent 是否可信、代表谁 |
| Authorization | AP2、ACT 2.0、Agentic Tokens | 用户是否授权该笔 spend |
| Checkout | ACP | Agent↔merchant 订单握手 |
| Settlement | x402、MPP、卡 rails | 资金清算 |

*行业表述*：协议**组合使用**多于「单协议赢者通吃」——AP2 授权 + ACP 结账 + x402 结算是常见架构叙事。

---

## 问题域（为何 2025–2026 爆发）

- **Agent 从「答问题」到「代办事」**：订机票、买 API 额度、续 SaaS——每一步都可能触发支付；人类逐笔确认不可扩展。
- **现有支付为人设计**：3DS、短信 OTP、KYC 界面——Agent 无法「看屏幕点确认」；需要 programmatic mandate 与 scoped token。
- **微支付经济**：Agent 单次 API 调用 $0.001–$0.05——信用卡 interchange 不经济；x402/稳定币使 **pay-per-call** 可行（公开数据称 x402 累计亿级笔数，具体口径随统计源变化）。
- **大厂卡位协议**：Google AP2+UCP、OpenAI+Stripe ACP、银联 APOP、支付宝 ACT 2.0、京东 A2P2——争夺「Agent 时代结算入口」规则制定权。
- **OpenClaw/龙虾生态**：FluxA「龙虾抢红包」等活动将 **Agent Wallet** 从概念推到可玩场景——与 [openclaw-alternatives.md](agent/openclaw-alternatives.md) 执行链相邻。

---

## 能力栈（概念拆分）

- **Mandate / 委托凭证**：可验证、可审计的 spend 边界（金额、商户、时效）——AP2 JSON-LD + ECDSA；缺失则 chargeback 与合规无解。
- **Scoped Payment Token**：单次或限域支付令牌——ACP Shared Payment Token；避免 Agent 持有 PAN。
- **Budget Envelope / Kill Switch**：Agent 级 spend ledger + 硬顶——UsageBox 等行业文强调：rails 成熟后 **metering 层** 才是规模化瓶颈。
- **Cross-rail Reconciliation**：同一 Agent 混用 x402（链上）与卡（法币）时的对账与归因。
- **Fiat vs Crypto 路线**：FluxA/x402 偏 crypto-native；Clink 偏 **PCI + 现有卡组织**——「AI 红利不应只属于有加密钱包的人」是其公开叙事。

---

## 形态谱系

- **协议/标准层**：x402、AP2、ACP、MPP、UCP（支付相关扩展）、APOP、A2P2、ACT 2.0
- **Agent Wallet 平台**：FluxA、Fireblocks Agentic Payments Suite、支付宝 AI 钱包
- **Fiat Agentic Payment Infra**：Clink、SolvaPay、Basis Theory（tokenization + Agentic Commerce Consortium）
- **Crypto KYA + Pay**：Skyfire KYAPay
- **卡组织方案**：Visa TAP、Mastercard Agent Pay / Agentic Tokens

---

## 风险 · 合规

- **Runaway Agent Spend**：无 budget enforcement 的 Agent Wallet 是 liability；须 kill switch 在 authorization 之上。
- **Chargeback 归属**：Agent 发起交易时 dispute 责任在 user、platform 还是 merchant——AP2 Mandate 旨在提供 auditable chain，司法辖区仍在演进。
- **协议碎片化**：A2P2/APOP/ACT/x402 互不兼容——开发者接入成本与重复验真。
- **Crypto 波动与合规**：稳定币 rails 受地区监管约束；Clink 路线强调 PCI L1 与本地支付方式覆盖 135+ 货币。

---

## 落地碎片

- 先画三层：**授权（AP2）→ 结账（ACP）→ 结算（x402 或 MPP/卡）**；不要用一个协议名覆盖全栈。
- B2B Agent 买 API：**x402 或 MPP** 优先；消费者零售 Agent：**ACP + 卡 rails + AP2**。
- 上生产前必须有 **per-agent spend ledger**，再 hand Agent the wallet。
- 与 [agentic-commerce.md](agentic-commerce.md) 分流：消费者「Agent 帮我买」读 commerce；工程师「怎么接支付」读本页。

---

## 工具与产品类型

| 类型 | 代表 | 备注 |
|------|------|------|
| HTTP 微支付协议 | x402 Foundation | Agent→API；USDC；零协议费叙事 |
| 授权协议 | Google AP2 | Mandates；60+ 伙伴；可扩展 x402 结算 |
| Checkout 协议 | Stripe/OpenAI ACP | Agent↔merchant REST checkout |
| 会话结算 | Stripe MPP + Tempo | streaming / session billing |
| Agent Wallet（crypto） | FluxA | Agent Wallet、AgentCard、AEP2 |
| Fiat Agentic Payment | Clink | Agentic Payment Skill；PCI L1；BV 等种子轮 |
| Tokenization / 联盟 | Basis Theory | Agentic Commerce Consortium |
| KYA + Pay | Skyfire | 身份+支付 crossover |
| 企业稳定币 | Fireblocks Agentic Payments Suite | PSP/企业 Agent 钱包 |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| x402 Foundation | HTTP 402 稳定币微支付；Linux Foundation 治理 | https://www.x402.org/ |
| Google AP2 | Agent Payments Protocol 规范 | https://github.com/google-agentic-commerce/AP2 |
| Stripe ACP | Agentic Commerce Protocol（checkout） | https://stripe.com/docs/agentic-commerce |
| Clink | Fiat Agentic Payment Skill；PCI L1 | https://clinkbill.com/ |
| FluxA | Agent Wallet / x402 生态活动 | https://fluxapay.xyz/ |
| Crossmint 协议对比 | AP2/x402/ACP/MPP 分层说明 | https://www.crossmint.com/learn/agentic-payments-protocols-compared |
| Forrester | Agentic Payments in B2C Commerce | https://www.forrester.com/blogs/agentic-payments-in-b2c-commerce-where-we-are-now/ |
| Juniper 2026 | Agentic commerce 支付基础设施 Leaderboard | https://www.juniperresearch.com/press/agentic-commerce-set-to-generate-15-trillion-globally-by-2030-as-payments-infrastructure-leaders-revealed/ |

## 对比与测评（第三方）

2026 年共识是 **composed stack**：Consumer checkout 常用 ACP+卡+AP2；machine commerce 常用 x402/MPP。「x402 vs AP2」是错误 framing——前者 settlement，后者 authorization。Presenc AI 2026 基准：仅 ~17% 品牌接受任一 major agent payment protocol——品类仍极早期。*网摘综合，非 Alignify 实测。*

---

## 延伸阅读

- [agentic-commerce.md](agentic-commerce.md)（消费者旅程）
- [ai-shopping.md](ai-shopping.md)（购物工具目录）
- [authentication.md](infrastructure/authentication.md)（OAuth 委托，非支付 rails）
- [openclaw-alternatives.md](agent/openclaw-alternatives.md)（FluxA 红包等活动载体）
