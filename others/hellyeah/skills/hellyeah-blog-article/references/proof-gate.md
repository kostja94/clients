## Proof Gate（P1–P5，一票否决）

Hellyeah 博客涉及 B2B 案例指标、平台状态、合规采购——此类声明需最严格证据标准。**P1–P5 任一项 Fail = 不得发布。**

| # | 阻断条件 | 严格标准 |
|---|---------|---------|
| **P1** | 案例指标无溯源 | 任何客户量化指标（ROAS、reach、CAC、ARR 等）须链 `/customers/{slug}` 或标注 "per authorized customer case study"。禁将单案例写成行业普适保证。 |
| **P2** | SOC 2 已认证 | 仅可写 **SOC 2 in flight**。禁 "SOC 2 Type II certified/compliant" 除非 `/security` 页明示更新。 |
| **P3** | Déjà Vu 写为 GA | 必须标注 **private alpha**。禁 "available now" / "generally available" / "sign up today" 作为 Déjà Vu 主 CTA。 |
| **P4** | Autonomous/agentic 夸大 | 禁「全自主替人决策」「无需人工审批」。须体现 spend caps、approvals、growth memory。Agentic 声明须与 Forge/AIMA 页内能力一致。 |
| **P5** | GEO 同义词未链 canonical | 任何 GEO / generative engine optimization / AI search visibility / LLM SEO 讨论须 **≥1 次** 内链 `/capabilities/seo-geo`。 |

---

## 客户案例 Proof 表（P0 引用须链案例页）

| 客户 | 公开指标 | 路径 | 主平台 |
|------|---------|------|--------|
| J&T Express | 120M reach；−55% CPM；1.4B impressions | `/customers/jt-express` | AIMA |
| Playco | 20M MAU；5.7× creative throughput；−31% CPI | `/customers/playco` | AIMA |
| Final Round AI | $12M ARR in 14mo；4.2× ROAS | `/customers/final-round-ai` | AIMA |
| Eragon | −28% CAC payback；2.4× activation；210% QoQ pipeline | `/customers/eragon` | Mutation |
| Viggle | #2 US App Store；11× DAU lift | `/customers/viggle` | Déjà Vu |
| Fish Audio | +340% MoM signups；−54% CAC | `/customers/fish-audio` | AIMA |
| Truist | $58M spend optimized；+24% acct openings | `/customers/truist` | Forge |
| BeFreed | 240 ads/week；−38% CPI | `/customers/befreed` | AIMA |
| The Dyrt | 4.0× organic；+62% subs | `/customers/the-dyrt` | Mutation |

**引用格式**：
> Final Round AI reached [$12M ARR in 14 months with 4.2× ROAS improvement](https://www.hellyeahai.com/customers/final-round-ai), per Hellyeah's published case study.

---

## 能力页统计（P1；引用前建议产品确认）

引用时须链对应 capability 页 + 标注 "as stated on Hellyeah capability page"：

| 能力 | 路径 | 页内统计（站内宣称） |
|------|------|---------------------|
| Agentic Marketing | `/capabilities/agentic-marketing` | 8× launch；4× experiments；73% ops 痛点 |
| Performance Marketing | `/capabilities/performance-marketing` | 3.2× ROAS avg；67% wasted spend ↓ |
| SEO / GEO | `/capabilities/seo-geo` | 20–80 文/月；GEO 多模型 |
| Lifecycle Automation | `/capabilities/lifecycle-automation` | 3.4× open rate；80% manual ↓ |
| Creative Generation | `/capabilities/creative-generation` | 47% sales lift（Nielsen 引用） |
| Influencer Marketing | `/capabilities/influencer-marketing` | $24B market；73% ROI 难衡量 |
| Capabilities 索引 | `/capabilities` | 8× launch、4× experiments 等汇总统计 |

---

## 平台状态表（G1 / P3 / P4）

| 模块 | 路径 | 状态 | 博客写法 |
|------|------|------|---------|
| CLI | `/#cli` | Live beta 叙事 | 可写；4 min · no credit card |
| AIMA | `/aima` | Live · WhatsApp | Free $0；SOC 2 in flight |
| Forge | `/forge` | Live | 六自动化系统 |
| Mutation | `/mutation` | Live | 60s 响应叙事 |
| Déjà Vu | `/deja-vu` | **Private alpha** | 必须标注；禁 GA 表述 |
| Blog | `/blog` | ⚠️ sitemap 未收录 | 成稿 status: draft |
| Alternatives | `/alternatives/*` | 规划 | 正文禁链；竞品外链 |

---

## 禁写清单（Proof / 定价 / 合规）

| 禁写 | 正确写法 |
|------|---------|
| SOC 2 Type II certified | SOC 2 in flight |
| AIMA from $1,500/month | AIMA Free $0；enterprise Pod = % managed spend |
| Déjà Vu is available now | Déjà Vu is in private alpha |
| Guaranteed ROAS / CAC outcomes | 案例指标 + 链案例页 + "results vary" |
| Agents replace humans entirely | Agents operate workflows with spend caps and approvals |
| `/platforms/aima` | `/aima` |

---

## AIMA 定价事实（G1）

| 档位 | 线上表述 |
|------|---------|
| AIMA Free | **$0 forever** · WhatsApp-first |
| Forward-Deployed Growth Pod | Enterprise · **% of managed spend** · 经 `/demo` 申请 |
| 对比表（AIMA 页） | vs Agency $3–10k retainer · vs SaaS $200–2k/mo/tool |

---

## Phase 5 对照

SelfCheck 首维须逐项 Pass P1–P5，与 G1–G7 并列 Hard Gate。
