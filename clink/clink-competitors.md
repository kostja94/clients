# Clink 竞品分析

> **本文档职责**：竞品矩阵、场景对比、差异化；功能见 [clink-features.md](./clink-features.md)。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[clink.md](./clink.md) | [clink-keywords.md](./clink-keywords.md)

**Last updated**: 2026-06-04 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [clink.md](./clink.md) |
| 功能 | [clink-features.md](./clink-features.md) |
| 关键词 | [clink-keywords.md](./clink-keywords.md) |
| 使用场景 | [clink-use-cases.md](./clink-use-cases.md) |
| 网站结构 | [clink-site-structure.md](./clink-site-structure.md) |
| 增长策略 | [clink-growth-strategy.md](./clink-growth-strategy.md) |

---

## 一、竞品分层

| 层级 | 代表 | 与 Clink 关系 |
|------|------|----------------|
| **PSP / 网关** | Stripe, Adyen, Airwallex | Clink **可连接**而非完全替代 |
| **MoR + 计费** | Paddle, Lemon Squeezy | 税务与卖方身份一体化；Clink 强调 **数据便携 + 编排** |
| **计费专精** | Chargebee, Recurly, Stripe Billing | 订阅逻辑强；Clink 叠加 **路由 + 多 PSP** |
| **纯编排** | Spreedly, Primer | 偏路由；Clink 含 **Billing + Tax + Portal** |
| **Agent 支付** | 新兴/自建 | Clink for Claw 先发叙事 |

---

## 二、直接竞品拆解（≥3）

### 2.1 Stripe（+ Stripe Billing）

| 维度 | Stripe | Clink |
|------|--------|-------|
| **角色** | 支付处理器 + 可选 Billing | 编排层 + 计费；**底层可连 Stripe** |
| **优势** | 生态、文档、开发者心智第一 | 多 PSP 路由、重试、便携订阅数据 |
| **税务** | Stripe Tax 计算；注册代缴仍多在商户 | 宣称 built-in tax、filing/remittance（范围 **待验证**） |
| **Agent** | 无官方「Agent top-up」产品柱 | **Clink for Claw** 明确 |
| **机会** | 已用 Stripe 但成功率/备份网关痛点 | 「Link Stripe + 第二 PSP」故事 |

**最后验证**：2026-06-04 | **AI 可见度**：高

### 2.2 Paddle

| 维度 | Paddle | Clink |
|------|--------|-------|
| **角色** | Merchant of Record | 编排 + 计费；商户可能仍为法律卖方（**待验证**） |
| **优势** | 全球 VAT 省心、发票以 Paddle 名义 | 灵活组合 PSP、自定义 checkout 路径 |
| **费率** | 通常高于 Stripe（行业常见 ~5% + 固定） | 宣称 transparent unified costs（**待验证**） |
| **机会** | 不想 MoR 发票品牌、要自管数据 | 对比页 /vs/paddle |

**最后验证**：2026-06-04 | **AI 可见度**：高

### 2.3 Chargebee

| 维度 | Chargebee | Clink |
|------|-----------|-------|
| **角色** | 订阅计费与营收运营 | 计费 + **支付性能**（路由/重试）一体 |
| **优势** | 复杂定价模型、RevRec 集成成熟 | 支付编排原生、Agent 线 |
| **重叠** | 订阅、Portal、Coupon | 高度重叠，差异在 **routing + multi-PSP** |
| **机会** | 支付失败率高的 Chargebee 客户 | 强调 *success rate* 证言主题 |

**最后验证**：2026-06-04 | **AI 可见度**：中

---

## 三、场景级对照表（≥2）

### 表 A：「全球 SaaS 要降支付失败率」

| 选项 | 路由/重试 | 订阅+Portal | 多 PSP |
|------|-----------|-------------|--------|
| 仅用 Stripe | Radar/部分重试 | Stripe Billing | 单 PSP |
| Stripe + Spreedly | 强 | 需另接计费 | 强 |
| **Clink** | 产品柱 Smart Routing | Billing 柱 | Link PSP 文档 |

### 表 B：「国内主体、Vibe Coding 快速接支付」

| 选项 | 出海开户 | Agent 文档 | 托管结账 |
|------|----------|------------|----------|
| Stripe 直连 | 门槛高 | 人类文档优秀 | 可 |
| Paddle MoR | 可行 | 一般 | 可 |
| **Clink** | 生态案例 + 中文社区经验（Oginify 等） | llms.txt、Agent Skill | Hosted Checkout |

*内部案例见仓库 Oginify 文档，对外引用需客户授权。*

---

## 四、差异化总表

| 维度 | Clink 主张 | 风险/待验证 |
|------|------------|-------------|
| 数据便携 | 换 PSP 不重写 | 迁移实操案例公开度 |
| 成功率 | 路由 + 重试 | 需第三方基准或白皮书 |
| 全球本地化 | 135+ 币种、100+ LPM | 与 Adyen 等对比口径 |
| 税务 | Automatic filing/remittance | 覆盖法域列表 |
| AI-Native | Agent payment、1-click agent-ready | Early Access 阶段 |
| 定价透明 | No hidden fees | 公开费率表 |

---

## 五、威胁与机会

| 类型 | 内容 |
|------|------|
| **威胁** | Stripe 加强 Orchestration / Billing 一体化 |
| **威胁** | Paddle 等 MoR 对 indie 心智稳固 |
| **机会** | Agent 经济支付需求上升（2026 叙事） |
| **机会** | 多 PSP  failover 成为 SaaS 标配意识 |
| **机会** | 亚太 SaaS 出海案例（证言客户）内容 SEO |

---

## 六、对比内容建议

| 页面 | 话题 |
|------|------|
| /vs/stripe | 编排 + 便携数据 vs 单 PSP |
| /vs/paddle | MoR vs 自主品牌 + 多 PSP |
| /vs/chargebee | 支付性能 + 计费一体 |
| /learn/mor-vs-orchestration | 教育型，降低选型困惑 |

---

*竞品费率与法域覆盖以各官网最新为准；本 demo 不含未核实流量数据。*
