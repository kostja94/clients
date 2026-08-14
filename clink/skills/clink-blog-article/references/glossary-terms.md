# Clink Glossary — 术语表（Financial & Billing）

> 加载时机：Phase 0（选题）· Gate A（KEEP/MERGE）
> 图例：✅ published | 📝 backlog | ❌ 不纳入

---

## 速查表

| # | Term | Cat | Primary slug intent | blog_status | canonical_slug |
|---|------|-----|---------------------|----------------|-------------|
| 1 | Annual Recurring Revenue (ARR) | A | annual-recurring-revenue | ✅ | annual-recurring-revenue |
| 2 | Monthly Recurring Revenue (MRR) | A | monthly-recurring-revenue | ✅ | monthly-recurring-revenue |
| 3 | Net Revenue Retention (NRR) | A | net-revenue-retention | ✅ | net-revenue-retention |
| 4 | Gross Revenue Retention (GRR) | A | grr | 📝 P2 | — |
| 5 | Burn Rate | C | burn-rate | ✅ | burn-rate |
| 6 | Runway | C | runway | ✅ | runway |
| 7 | Churn Rate | B | customer-churn-analysis | 📝 P1 | — |
| 8 | Logo Churn vs Revenue Churn | B | logo-churn-vs-revenue-churn | 📝 P2 | — |
| 9 | Involuntary Churn | B | involuntary-churn | 📝 P0 | — |
| 10 | Voluntary Churn | B | voluntary-churn | 📝 P2 | — |
| 11 | Customer Lifetime Value (LTV) | C | ltv | 📝 P2 | — |
| 12 | CAC / Payback Period | C | cac-payback | 📝 P2 | — |
| 13 | Dunning | D | dunning | 📝 P1 | — |
| 14 | Payment Decline / Soft Decline | D | soft-decline | 📝 P0 | — |
| 15 | Authorization Rate | D | authorization-rate | 📝 P2 | — |
| 16 | Expansion Revenue | E | expansion-revenue | 📝 P1 | — |
| 17 | Merchant of Record (MoR) | F | mor-vs-psp（已有 canon，blog 侧） | — | mor-vs-psp |
| 18 | Tax Nexus | F | tax-nexus | 📝 P2 | — |

---

## 分类 A–G

### A — Revenue 收入指标
- **ARR**（✅ canonical）— 订阅年化经常性收入；ARR = MRR × 12，并调整 expansion/contraction/churn。
- **MRR** — 月度经常性收入；短合同/按月计费用 MRR 而非 ARR。
- **NRR** — 含 expansion/contraction/churn 的净留存率；>100% 表示现有客户净增长。
- **GRR** — 不含 expansion 的毛留存率；只反映客户基本留存。

### B — Churn / Retention 流失与留存
- **Churn Rate** — 客户流失率；logo churn（客户数）与 revenue churn（金额）须分开看。
- **Involuntary Churn** — 非自愿流失：卡过期、余额不足、软拒绝导致扣款失败——**支付基础设施可干预**（智能重试/路由，链 smart-routing 论证）。
- **Voluntary Churn** — 主动取消：定价、价值感知、竞品迁移。
- **Logo vs Revenue Churn** — 客户数 vs 金额口径；小客户流失对大 ARR 影响有限。

### C — Cash / Unit Economics 现金流与单元经济
- **Burn Rate**（✅ canonical）— 月度净现金消耗；Gross burn（总支出）vs Net burn（支出 − 收入）。
- **Runway** — 现金余额 ÷ 月净 burn；决定融资时点。
- **LTV** — 客户生命周期价值；与 CAC 联合评估健康度。

### D — Payments 支付
- **Dunning** — 扣款失败后的自动重试/催缴流程；dunning 配置直接决定 involuntary churn 率。
- **Soft Decline** — 临时性拒绝（风控标志、临时错误），可安全重试/换通道；Hard decline 不可重试。
- **Authorization Rate** — 授权成功率；多 PSP 路由可提升区域授权率（链 smart-routing）。

### E — Pricing / Subscription 定价与订阅
- **Expansion Revenue** — 增购/升档收入；NRR 的上行驱动。

### F — Tax / Compliance 税务与合规
- **MoR**（已有 blog canon `mor-vs-psp`，glossary 不重写）— 法律卖家角色的选型框架见 canon 文。
- **Tax Nexus** — 征税关联点；跨境 SaaS 需逐辖区判断。

### G — Agent / AI-Native Payments（远期）
- **Agent Payment Session** — Agent 自主支付会话（链 `/agentic-payment`，须标 Early Access）。

---

## 明确不纳入 glossary

- Clink 专有：Smart Routing、Clink for Claw、Portable Billing → 产品页/blog canon，不建 glossary 词条
- 纯会计：GAAP、ASC 606、accrual → 超出范畴
- 泛 VC 术语无订阅关联：pre-money/valuation → 与 Clink 品类弱相关

---

## Backlog 批次建议

| Batch | 术语 | 备注 |
|-------|------|------|
| **P0** | Involuntary Churn、Soft Decline | 与 smart-routing 产品论证强互链，最佳 SEO 增量 |
| **P1** | Dunning、Expansion Revenue、Churn Rate、Runway（已出） | 组成完整财务指标簇 |
| **P2** | GRR、Logo vs Revenue Churn、Voluntary Churn、LTV、CAC、Authorization Rate、Tax Nexus、MRR/NRR 相关（已出） | 长尾 |

---

## 指标簇结构

```
闭环: annual-recurring-revenue ↔ burn-rate ↔ monthly-recurring-revenue ↔ net-revenue-retention ↔ runway
 ├── MRR（月度收入）→ ARR（年化收入）→ NRR（留存质量）
 ├── burn-rate（现金速度）→ runway（时间耗尽）
 └── 全部 → smart-routing / mor-vs-psp / what-is-clink（blog canon）
```

**规则**：已有 canonical 术语在新文中仅 recap（≤150 词）+ link；对比 intent 单独成文时自身为 canonical。

---

*glossary-terms · v1.0.0 · 2026-08-03*
