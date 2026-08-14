# Clink 增长策略

> **本文档职责**：渠道、内容战役、实验；对齐关键词与网站结构。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[clink.md](./clink.md) | [clink-keywords.md](./clink-keywords.md) | [clink-site-structure.md](./clink-site-structure.md) | [clink-use-cases.md](./clink-use-cases.md)

**Last updated**: 2026-07-21 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [clink.md](./clink.md) |
| 关键词 | [clink-keywords.md](./clink-keywords.md) |
| 网站结构 | [clink-site-structure.md](./clink-site-structure.md) |
| 使用场景 | [clink-use-cases.md](./clink-use-cases.md) |
| 竞品 | [clink-competitors.md](./clink-competitors.md) |
| 功能 | [clink-features.md](./clink-features.md) |

---

## 1. 增长目标与约束

| 维度 | 策略 |
|------|------|
| **主转化** | Contact / Login → KYB → Link PSP → 首笔 Checkout |
| **主战场** | 全球 SaaS、AI App；**差异化战役**：Agent 经济（Agentic Payments + Skill Marketplace） |
| **内容支柱** | 支付成功率、订阅计费、多 PSP、Agent 支付 |
| **约束** | 金融合规表述需法务审定；证言引用需授权 |

---

## 2. 渠道与战役（≥3）

### 方向 A：SEO + 对比页

| 要素 | 内容 |
|------|------|
| **目标** | 拦截 subscription billing、payment orchestration、stripe alternative |
| **交付** | /vs/stripe、/vs/paddle、/pricing、/for/saas |
| **联动** | [clink-site-structure.md](./clink-site-structure.md) Phase 2 |

### 方向 B：开发者关系（DevRel）

| 要素 | 内容 |
|------|------|
| **目标** | Quickstart 完成率、API 集成数 |
| **战术** | docs Quickstart、OpenAPI、TypeScript SDK、**llms.txt** 对 Agent 友好 |
| **内容** | 「Create checkout in 10 minutes」、Test Clock 教程 |
| **联动** | 仓库内可复用 Oginify 类接入 playbook（内部） |

### 方向 C：Agent 生态（Agentic Payments）

| 要素 | 内容 |
|------|------|
| **目标** | Early Access 名单、Skill 安装量 |
| **战术** | OpenClaw / ModelMax 合作叙事；GitHub Skill；*Sell to Millions of Agents* |
| **信息** | 60 秒支付闭环、预算与风控 demo（官网交互） |
| **联动** | [/agentic-payment](https://clinkbill.com/agentic-payment)、[/skills](https://clinkbill.com/skills) |

### 方向 D：客户故事与伙伴

| 要素 | 内容 |
|------|------|
| **目标** | 信任与垂类渗透（安全、云手机、AI 语音等） |
| **战术** | 将首页证言扩展为 `/customers/*`；Logo 墙伙伴联合 PR |
| **客户名（官网）** | BlockSec、GeeLark、Linkloud、VoiSpark、Gazolab、Virax.ai、ZingFront、NovaSonic |

---

## 3. 内容主题线

| 主题簇 | 载体 | 优先级 |
|--------|------|--------|
| 支付成功率 | /products/routing、博客 | P0 |
| 订阅与税务 | /products/billing | P0 |
| 多 PSP 架构 | docs/link_psp、/learn | P1 |
| Agent 支付 | /agentic-payment、/skills | P0 |
| 选型对比 | /vs/* | P0 |
| 亚太出海 | 案例、中文帖（可选） | P1 |

---

## 4. 发布计划（草案 90 天）

| 周次 | 交付 |
|------|------|
| W1–2 | /vs/stripe 首版 + 首页内链优化 |
| W3–4 | /pricing + /for/saas |
| W5–6 | 博客：payment retry best practices |
| W7–8 | /for/ai-apps + Agentic Payments Early Access 邮件序列 |
| W9–12 | 2 个客户案例页 + GEO FAQ |

---

## 5. 实验与度量

| ID | 假设 | 指标 | 状态 |
|----|------|------|------|
| E1 | Hero CTA「Explore Agentic Payments」提升 Agent 页访问 | CTR | 待验证 |
| E2 | /vs/stripe 提升非品牌 organic 注册 | 注册来源 | 待验证 |
| E3 | docs Quickstart 缩短 TTV | 7 日内首笔 session | 待验证 |
| E4 | 证言视频化提升 Contact 转化 | 表单提交 | 待验证 |

**核心指标建议**：激活商户数、Link PSP 数、Checkout Session 量、订阅 MRR 经平台、支付成功率 uplift。

---

## 6. 执行待办

| 待办 | 优先级 |
|------|--------|
| 上线 /pricing | P0 |
| 创建 /vs/stripe、/vs/paddle | P0 |
| /for/saas、/for/ai-apps | P1 |
| 客户案例独立 URL | P1 |
| 核对 Support/Contact 真实 URL 入 sitemap | ~~P1~~ ✅ Contact 已入 sitemap；Support 仍链 docs |
| Backlog R1–R2 定价与 MoR 口径 | P0 |

---

*下一轮建议：模式 C，入口 clink-competitors（定价/MoR 核实后更新对比页）*
