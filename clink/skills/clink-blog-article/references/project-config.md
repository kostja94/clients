# Clink — Project Configuration

> 加载时机：Phase 0R（R1）· Phase 4（Draft）· Phase 5（SelfCheck）
> 主文件：SKILL.md §1 速查指针

---

## 1. 品牌与产品

| 配置项 | 值 |
|--------|-----|
| **品牌/产品名** | Clink |
| **主域名** | clinkbill.com |
| **文档** | docs.clinkbill.com |
| **博客路径前缀** | `/blog/` |
| **产品定位** | Payment Infrastructure for an AI-Native World |
| **品类 one-liner** | Unified subscription billing + multi-PSP payment orchestration + global tax + agent-ready payments |
| **四产品线** | Global Payments · Smart Routing · Billing · Agentic Payments（Clink for Claw） |
| **核心差异化** | 订阅数据与 PSP 解耦 · 智能路由/重试 · 135+ 币种 / 100+ 本地支付方式 · Agent 支付 |
| **目标用户** | 全球 SaaS 团队、AI-native 产品、支付/RevOps 工程师、FinOps |
| **案例客户** | BlockSec、GeeLark、Linkloud、ModelMax、PollyReach、VoiSpark、Gazolab、Virax.ai、ZingFront、NovaSonic |
| **接入模式** | Contact Sales（无公开 self-serve 定价页，截至 2026-06） |
| **CTA 主链** | https://clinkbill.com/ |
| **署名** | `Clink Team` |
| **语言** | 英文正文；中文仅用于沟通 |

### 待验证项（写作时必须限定语或标注）

| 项 | 说明 |
|----|------|
| 公开定价/费率 | 禁止写具体百分比费率（C1） |
| MoR 法律角色 | 混合 MoR 覆盖范围须限定语（C2） |
| 税务 filing/remittance 司法辖区 | 须 as-of + 建议读者 Contact Sales 确认（C2） |
| Agentic Payments | 须标 **Early Access**（截至 2026-07；路径 `/agentic-payment`）（C4） |

---

## 2. 可链接 URL 白名单（内链优先）

| 类型 | 路径 |
|------|------|
| 首页 | `/` |
| 博客 | `/blog/{slug}` — 见 `content-graph.md` |
| Smart Routing | `/products/routing` |
| Billing | `/products/billing` |
| Global Payments | `/products/payment` |
| Agentic Payments | `/agentic-payment`（canonical；勿链 `/clink-for-claw`） |
| Skill Marketplace | `/skills` |
| Contact | `/contact` |
| 文档 | `https://docs.clinkbill.com/` |
| Link PSP 指南 | `https://docs.clinkbill.com/guides/payments/link_psp` |
| Checkout Session | `https://docs.clinkbill.com/guides/payments/checkout_session` |

**G6 禁止内链（未上线）**：

| 路径 | 说明 |
|------|------|
| `/vs/stripe` | 对比页待建 |
| `/vs/paddle` | 对比页待建 |
| `/pricing` | 定价页待建 |
| `/for/saas` | 落地页待建 |
| `/learn/*` | 教育页待建 |
| `/customers/*` | 案例详情待建 |

**G6 规则**：不链 forbidden 路径；forthcoming ≤1 且仅正文脚注。

---

## 3. G1–G7 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、客户名、Early Access 状态与官网/docs 矛盾 | 逐 claim 对照 product-competitors.md |
| **G2** | 死链 | 站内 forbidden 或明显 placeholder | link_checker.py |
| **G3** | 无来源数字 | 量化 claim 无 attribution | P0 级数字须来源；行业估算须限定语 |
| **G4** | 竞品状态错误 | Stripe/Paddle/Chargebee 能力与定位错误 | 对照竞品官网 |
| **G5** | 产品能力夸大 | 「唯一」「全球首个」等无证据表述 | 禁无数据 superlative |
| **G6** | 内链指向未上线页面 | 只链 §2 白名单 | link_checker.py |
| **G7** | 品牌风险 | 贬低竞品；不公平对比 | 每竞品 ≥1 优势 |

---

## 4. C1–C4 Clink 专属 Gate

| # | 阻断条件 | 说明 |
|---|---------|------|
| **C1** | 无来源的具体 Clink 费率 | Contact Sales 模式；禁止编造 pricing table |
| **C2** | MoR/tax 超范围 claim | 无 as-of 或无限定语的 filing/remittance 全覆盖 |
| **C3** | 证言夸大 | BlockSec/GeeLark 等成功率/GMV 无 as-of 或过度推断 |
| **C4** | Agentic Payments 未标 Early Access | 截至 2026-07 须明确 Early Access |

G1–G7 + C1–C4 全部 Pass 方可交付。

---

## 5. 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章 |
| **错开方向** | 从锚点日**往前**排 |
| **避让已占用日** | 见 content-graph.md 日期表 |

已有日期：2026-06-23（what-is-clink）、2026-06-29（mor-vs-psp, smart-routing, agent-payments）。

---

## 5B. GlossaryTerm 叙事原则（category: Glossary）

| 原则 | 要求 |
|------|------|
| **教育优先** | 定义与计算章节零产品推销；Clink 仅 FAQ 前 ≤3 段 |
| **Wirecutter 式客观** | 承认 Carta/Stripe/Investopedia 等已有内容的权威；不贬低 |
| **工程实践深度** | 具体计算示例、术语边界表、陷阱清单——非教科书罗列 |
| **指标簇互链** | 财务术语互相成簇（burn-rate ↔ annual-recurring-revenue），并向 blog canon（smart-routing 等）输送流量 |
| **数据合规** | P0 数字有来源或 as-of；不写无来源的 Clink 费率（C1） |

---

## 6. 品牌 Voice 速查

| 维度 | 要求 |
|------|------|
| Professional | 精确、数据导向，无空洞 hype |
| Evidence-led | 产品 claim 引用 clinkbill.com 或 docs |
| Fair comparison | describe differences, not deficiencies |
| Category-building | 非 canon 文引用 what-is-clink，不重写全文 |

### 禁止

- revolutionary · game-changing · unlock · seamless · magic · best-in-class（无证据）
- 无来源的行业数字当作 Clink 数据
- 暗示 Clink 替代持牌银行/清算机构

---

*project-config · v1.0.0 · 2026-07-21*
