# Agentic Commerce · 知识块（非线性笔记）

**材料范围**：公开网络检索（a16z Open Agentic Commerce、a16z/摩根士丹利/commercetools/Braze 行业报告、Google UCP/NRF 2026、OpenAI ChatGPT Shopping、Forrester 消费者采用数据、Rye agentic commerce landscape、SEO Turtle/DataForSEO 搜索趋势引用）；**未**引用 Alignify 站内 JSON 为独立事实来源。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/agentic-commerce](https://alignify.co/blog/agentic-commerce) · `/zh/blog/agentic-commerce` · `content/blog/en|zh/agentic-commerce.json` · slug **`agentic-commerce`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 `#agentic-commerce-tools` · `keywordEn`: **Agentic Commerce** · `keywordZh`: **代理式商务

## 与相邻 slug 分流

| slug | 典型读者 | 核心问题 | 边界 |
|------|---------|---------|------|
| **`agentic-commerce`（本页）** | 消费者、品牌/零售 PM、增长负责人 | Agent **替我购物**时发生什么？我如何授权与控风险？ | **旅程与范式**——发现→决策→（部分）结账 |
| **`ai-shopping`** | 工具选型者、电商运营 | **有哪些** AI 购物/商务 SaaS 可对比？ | **产品目录**（ChatGPT Shopping、Glance、Nosto…） |
| **`agentic-payments`** | 工程师、支付/Fintech | Agent **怎么付钱**？接哪条协议？ | **支付栈**（x402/AP2/Clink…） |
| **`geo`** | SEO/GEO 从业者 | 品牌如何被 AI 答案引用？ | 可见性策略，非结账旅程 |

## 三分法（必读）

| | **Agentic Commerce** | **AI-assisted Shopping** | **Traditional E-commerce** |
|--|---------------------|-------------------------|---------------------------|
| 谁下单 | Agent 在授权内自主或半自主 | 人类决策，AI 建议 | 人类全程点击 |
| 交互 | 对话/委托任务 | 对话+人工结账 | 搜索+PDP+购物车 |
| 典型入口 | Gemini AI Mode、ChatGPT Shopping、千问+淘宝 | 带 AI 的电商 App | Amazon、Shopify 店 |
| 本页 | ✓ 主轴 | 相邻提及 | 对照背景 |

---

## 词汇锚点

- **Agentic Commerce / 代理式商务**：AI Agent 代表用户完成**购物全链路或关键段**——发现、比较、选品、下单乃至售后——而非仅返回文字推荐。a16z 分 **Conversational**（人指挥每步）与 **Delegated**（给预算让 Agent 自主执行）。
- **Agentic Checkout / 代理式结账**：Commerce 旅程中的**交易执行层**——从「找到了」到「订单确认」；比 commerce 窄，常与 [agentic-payments.md](./agentic-payments.md) 的 checkout+settlement 重叠。
- **Discovery–Transaction Gap / 发现–交易鸿沟**：2026 典型数据形态——多数消费者用 AI **比价/发现**（行业调研常引 ~62%），显著 fewer 在 AI 内**完成结账**（~23% 量级，口径因来源而异）。品类核心瓶颈。
- **Headless Merchant / 无头商家**：面向 Agent 而非人类 UI 的商家——结构化 catalog API + 机器可读定价；a16z 2026 叙事中的长期形态。
- **UCP（Universal Commerce Protocol）**：Google+Shopify 等 2026 主推的**全链路商务语言**——发现、购物车、结账、售后；与仅 checkout 的 ACP 对比常被并列讨论。
- **ACP（Agentic Commerce Protocol）**：OpenAI+Stripe——Agent↔merchant **checkout 握手**；ChatGPT Instant Checkout 等曾试点（Forrester 称采用低迷后 OpenAI 调整策略，以官方为准）。
- **Dark Traffic / 暗流量**：用户在 ChatGPT/Gemini 发现品牌，却以品牌词搜索进站成交——last-click 归因低估 AI 渠道；commerce 运营必谈。
- **Delegated Budget / 委托预算**：用户预授权 spend cap（「买一双<$200 的跑鞋」）——commerce 信任模型的用户侧表达；底层实现见 agentic-payments。

---

## 问题域

- **搜索→购买迁移**：58% 消费者倾向用 AI 做购物决策（2023 约 25%）；Black Friday 期间生成式 AI 导流零售流量 YoY 高增——**入口从 SERP 迁到对话**。
- **平台巨头布局**：ChatGPT Shopping、Gemini AI Mode+Google Pay、Perplexity Shopping、阿里千问+淘宝+支付宝 AI付——**对话框=新收银台**竞争已开始。
- **中国验证、全球追赶**：美团/阿里 Agent 闭环购物证明可行；欧美仍处「发现强、交易弱」——Deloitte 亚太零售增量叙事与全球不同步。
- **广告模型压力**：a16z 论断 Agent 不被展示广告分散——$300B/年搜索广告逻辑受威胁；品牌需优化 **AI 可读 product feed** 而非仅 SEM。
- **消费者信任滞后**：Forrester——多数用户对 Agent 代付仍 lukewarm；Millennials/男性兴趣更高；**习惯未形成**（「ai shopping assistant」US 搜索 ~1.3K/月且 flat，SEO Turtle 2026）。

---

## 能力栈（消费者旅程）

- **意图委托**：自然语言目标→可执行 shopping task（预算、品牌偏好、时效）。
- **跨平台发现与比较**：Agent 并行查多商户/多 marketplace——人类不再逐站打开 PDP。
- **个性化与 multimodal**：自拍→穿搭 feed（Glance 类）、以图搜同款——commerce 体验层，工具清单见 ai-shopping。
- **In-conversation Checkout**：对话内展示 cart + 支付确认——Alipay AI付、Gemini+GPay 路线；与「跳转外链结账」对比。
- **Post-purchase**：追踪、退货、再购——UCP 叙事含全生命周期；多数 2026 产品仍弱。
- **Merchant Readiness**：结构化 data、API 延迟、agent-readable policy——品牌侧「被 Agent 选中」的前提。

---

## 形态谱系（消费者侧）

- **Super-app Agent Commerce**：Gemini+Shopping Graph、千问+淘宝、微信 AI 支付内测——封闭生态内闭环。
- **Answer Engine Shopping**：ChatGPT Shopping、Perplexity Shopping——发现强，结账依赖 ACP/跳转。
- **Visual / Feed Commerce**：Glance 锁屏 feed——发现即购买意图。
- **Retailer Agent Layer**：Spangle 动态 storefront——商家侧，消费者仍可能从广告进站。
- **Universal Checkout 初创**：Rye Universal Checkout——无 merchant 预集成代购（与 consumer 体验相关但偏 infra）。

---

## 风险 · 合规 · 消费者保护

- **Over-spend / 误购**：Agent 误解意图或超预算——需 mandate 与用户确认分级（L0–L5 自主化分级，京东 A2P2 类比自动驾驶）。
- **推荐偏差与付费排序**：Agent 是否优先付费商户——透明度与监管关注。
- **隐私**：购物历史、偏好进入模型上下文——与 [memory.md](./memory.md) 个人数据风险相邻。
- **归因与退款**：Agent 代下单后的售后责任链——merchant、platform、Agent 开发者分工不清。

---

## 落地碎片（消费者/品牌）

- **消费者**：从小额、可撤销委托开始（「$50 内买咖啡券」）；检查平台是否 **逐笔确认** vs 真 autonomous。
- **品牌**：优先完善 **structured product feed** 与 API 响应；别只优化人类 PDP SEO。
- **与 ai-shopping 分工**：要工具清单→ai-shopping；要理解「Agent 时代购物范式」→本页；要接 x402/AP2→agentic-payments。
- **中文市场**：关注支付宝 AI付、京东 A2P2 分级、银联 APOP——与 Google/OpenAI 叙事 parallel 但标准不互通。

---

## 工具与产品类型（消费者入口，非穷尽）

| 类型 | 代表 | 消费者体验 |
|------|------|-----------|
| Answer engine shopping | ChatGPT Shopping, Perplexity | 对话内发现+部分 checkout |
| AI Mode commerce | Google Gemini + UCP | Search/Gemini 内结账 |
| Visual discovery | Glance | 自拍→个性化 feed |
| Super-app agent | 千问+淘宝, 支付宝 AI付 | 国内闭环；AI付 3 亿+ 笔（厂商披露） |
| Conversational sales | Rep, Zowie（见 ai-shopping） | 站内对话成交 |

---

## 外链索引

| 名称 | URL |
|------|-----|
| a16z · Open Agentic Commerce | https://a16z.com/ai-shopping-online/ |
| Google UCP 公告（NRF 2026 语境） | https://blog.google/products/search/ |
| Forrester · Agentic payments/commerce | https://www.forrester.com/blogs/agentic-payments-in-b2c-commerce-where-we-are-now/ |
| Rye · Agentic commerce startups landscape | https://rye.com/blog/agentic-commerce-startups |
| Morgan Stanley projection（第三方转述） | https://fourweekmba.com/morgan-stanleys-agentic-commerce-projection-126-million-ai-shopping-agents-by-2030-while-traditional-e-commerce-halves/ |
| SEO Turtle · agentic commerce 搜索趋势 | https://seoturtle.com/seo-insights/agentic-commerce-ai-shopping-agents-seo |

## 市场注记（2026）

US「agentic commerce」搜索约 **4.4K/月**、YoY **+408%**（DataForSEO，SEO Turtle 2026 引用）；仍远低于「agentic AI」~110K/月。Juniper：2030 年全球 agentic commerce spend **$1.5T** 预测（厂商研究，非 Alignify 背书）。*网摘综合。*

---

## 延伸阅读

- [ai-shopping.md](./ai-shopping.md)
- [agentic-payments.md](./agentic-payments.md)
- [geo.md](./geo.md)
- [influencer-marketing.md](./influencer-marketing.md)（creator commerce 相邻）
