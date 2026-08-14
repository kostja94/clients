## §1 项目配置与 G1–G7 阻断规则

> **Distilled for hellyeah-blog-article v1.0.0 · source audit 2026-06-02**

### 1.1 项目配置

| 配置项 | Hellyeah 值 |
|--------|-------------|
| **品牌/产品名** | Hellyeah、Hellyeah AI Inc. |
| **产品名大小写** | 正文与 frontmatter 统一 **Hellyeah**；域名 hellyeahai.com 小写 |
| **主域名** | hellyeahai.com |
| **博客路径前缀** | `/blog/`（frontmatter `slug` 含此前缀） |
| **博客状态** | ⚠️ sitemap 未收录（2026-06-02）；成稿加 `status: draft` |
| **作者** | `Kostja`（默认） |
| **Primary ICP** | Growth / marketing / revenue leaders；Founders；Growth engineers；Performance / Lifecycle marketers |
| **Secondary ICP** | Agency teams；RevOps；Enterprise procurement |
| **公司类型** | Consumer apps、AI apps、Gaming、Marketplaces、Fintech、E-commerce、Creator-led、Agencies、AI-native startups |
| **品类 one-liner** | AI-native CLI for building, testing, and scaling growth campaigns from one command layer |
| **Hero 叙事** | *npm install your growth engine* |
| **增长循环 RCLL** | Research → Create → Launch → Learn |
| **Manifesto 四平台** | AIMA sees · Mutation reacts · Forge builds · Déjà Vu remembers |
| **商业转化** | `/demo`（15 min）；Contact；**AIMA Free $0**（WhatsApp）；企业 **Forward-Deployed Growth Pod**（% managed spend，经 demo） |
| **CTA 主链（企业）** | `https://www.hellyeahai.com/demo` |
| **CTA 次级（自服务）** | `https://www.hellyeahai.com/aima` |
| **CLI 入口** | `https://www.hellyeahai.com/#cli` |
| **语言/市场** | 英文正文；B2B enterprise growth（US/global） |
| **禁止内链** | `/platforms/*`、`/trust-center`、`/about-us`、`/arenas/*`、`/integrations`（404）；forthcoming `/alternatives/*`（正文 ≤1 脚注） |

### 1.2 G1–G7 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、定价、平台状态与 hellyeahai.com 矛盾 | 对照 `product-competitors.md` + `proof-gate.md`。Déjà Vu = private alpha；AIMA = $0 Free；SOC 2 = in flight。 |
| **G2** | 死链 | 站内或站外链接 404/域名拼写错误 | 逐个检查内链（对照 §1.4 白名单）。外链可有 1–2 失效，不能全挂。 |
| **G3** | 无来源数字 | 量化 claim 无 attribution | P0 须 `[Source: URL]` 或链 `/customers/{slug}`。能力页统计须链 capability 页。 |
| **G4** | 竞品/平台状态错误 | GA/Beta/定价与官方公告矛盾 | 打开竞品官网验证。Cometly/Koast 等引用前二次核实。 |
| **G5** | 产品能力夸大 | 超出 GA 或已文档化能力 | 「designed to」「aims to」≠ 已实现。禁全自主替人决策。 |
| **G6** | 内链指向未上线页面 | 链到禁止内链列表或未发布路径 | 对照 §1.4。forthcoming ≤1 且仅 Related 脚注。 |
| **G7** | 重大品牌风险 | 未授权案例数字、贬低性竞品措辞、合规误导 | 案例 % 须授权；勿写 SOC 2 Type II certified；勿写 $1,500/month AIMA 起价。 |

**G6 补充**：forthcoming 上限 ≤1 个，且仅限文末 Related 脚注。正文核心流程不得含 forthcoming 链接。

### 1.3 双核心意图 → 落地页（创作内链必查）

| 用户意图 | 动作词 | 主链目标 |
|---------|--------|---------|
| **Enterprise / Demo** | evaluate, enterprise, pod, managed spend | `/demo` · `/about` |
| **Self-serve / AIMA** | assistant, WhatsApp, free, ads manager | `/aima` |
| **GEO / AI search** | programmatic GEO, generative engine optimization, LLM SEO | **`/capabilities/seo-geo`**（canonical，P5） |
| **Performance / ROAS** | ROAS, paid ads, performance marketing | `/capabilities/performance-marketing` · `/aima` |
| **Experimentation** | continuous experiments, A/B throughput | `/deja-vu`（private alpha） |
| **Real-time signals** | event-driven, marketing intelligence | `/mutation` |
| **Agentic workflows** | custom workflow, agentic growth | `/forge` · `/capabilities/agentic-marketing` |
| **Trust / procurement** | SOC 2, security, compliance | `/security` |

### 1.4 可链接 URL 白名单

| 类型 | 路径 |
|------|------|
| 博客 | `/blog/{slug}` — 见 `content-graph.md` |
| 首页 / CLI | `/` · `/#cli` |
| 四平台 | `/aima` · `/forge` · `/mutation` · `/deja-vu` |
| 能力索引 | `/capabilities` |
| 能力线（6） | `/capabilities/agentic-marketing` · `/capabilities/performance-marketing` · `/capabilities/seo-geo` · `/capabilities/lifecycle-automation` · `/capabilities/creative-generation` · `/capabilities/influencer-marketing` |
| Solutions（5） | `/solutions/automate-marketing` · `/solutions/improve-conversion-rate` · `/solutions/improve-marketing-roi` · `/solutions/reduce-cac` · `/solutions/scale-paid-ads` |
| Arena（7） | `/for/mobile-apps` · `/for/b2b-enterprise` · `/for/consumer-tech` · `/for/ecommerce` · `/for/gaming` · `/for/fintech` · `/for/edutech` |
| 案例（9） | `/customers/jt-express` · `/customers/playco` · `/customers/final-round-ai` · `/customers/eragon` · `/customers/viggle` · `/customers/fish-audio` · `/customers/truist` · `/customers/befreed` · `/customers/the-dyrt` |
| 品牌/转化 | `/demo` · `/about` · `/manifesto` · `/customers` · `/contact` |
| 合规 | `/security` · `/privacy` · `/terms` |
| 法务外链 | 竞品官网、Nielsen（Creative 页引用）、行业报告 |

**内链格式**：Markdown `[锚文本](/capabilities/seo-geo)`；slug **不含** `NN-` 文件名前缀。

### 1.5 废弃路径（勿链、勿写）

| 废弃 | 替代 |
|------|------|
| `/platforms/aima` 等 | `/aima` 等 |
| `/trust-center` | `/security` |
| `/about-us` | `/about` |
| `/arenas/{slug}` | `/for/{slug}` |
| `/capabilities/geo` | `/capabilities/seo-geo` |
| `/capabilities/lifecycle` | `/capabilities/lifecycle-automation` |
| `/capabilities/influencer` | `/capabilities/influencer-marketing` |

### 1.6 Trust 表述（可写 / 禁写）

| 可写 | 禁写 |
|------|------|
| ISO 27001、GDPR、CCPA、DPF、HIPAA-ready（首页信任条；非法律意见） | SOC 2 Type II **certified** |
| SOC 2 **in flight**（AIMA 页） | $1,500/month AIMA 起价 |
| `/security`：TLS 1.3、AES-256、per-tenant keys、immutable audit log（7y）、SSO SAML/OIDC、SCIM | 「端到端加密」等未在 Trust 页明示的表述 |
| AIMA OAuth-only | Déjà Vu 作为 GA 全功能 |

### 1.7 Frontmatter 规范（创作用）

```yaml
---
title: "{H1-aligned title}"
description: "{140–160 chars; primary keyword in first 80 chars}"
slug: /blog/{url-slug}
author: Kostja
date: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
category: {Pillar|Framework|CommercialEducational|PlatformExplainer|Alternative|UseCase|Diagnosis|Compliance}
status: draft
---
```

> **2026-08-11 起废弃**：`keywords` / `image` / `imageAlt` 不再写入 frontmatter（image 由 CMS/OG 管理；keywords 仅用于 SEO 规划）。
