# Clink — Internal Links

> 加载时机：Phase 3 / 3.5 / 5

---

## 1. 规则

| 规则 | 标准 |
|------|------|
| 正文 blog 互链 | ≥2（Markdown `[text](/blog/{slug})`） |
| 产品页 | 仅白名单：`/products/routing`、`/products/billing`、`/clink-for-claw` 或 `/agentic-payment`（以 project-config 为准） |
| 文档 | 完整 URL `https://docs.clinkbill.com/...` |
| 锚文本 | 语义化；禁 "click here" / "learn more" |
| forthcoming | ≤1；脚注；不链 forbidden |
| frontmatter | **不使用** `related` 字段 |
| **锚文本** | 描述性、上下文原生；禁重复 slug 标题作锚（如连续三处 `[agent channels](/blog/agentic-commerce-agent-channels)`）；同一 slug 在全篇宜 2–4 处、锚文本互不重复 |

---

## 2. Reference list 三部曲锚文本变体（34 / 35 / 36）

| slug | 推荐锚文本模式（轮换，勿堆叠同句） |
|------|-----------------------------------|
| `agentic-commerce-agent-channels` | Live status for ChatGPT, Copilot, Gemini… · AI channel live-status reference · which AI shopping surfaces are live · buyer-facing agent channel list |
| `agentic-commerce-merchant-stack-cms` | Shopify Agentic Storefronts and platform enablement · commerce platform enablement reference · storefront enablement on your CMS · which CMS exposes Agentic Storefronts or UCP profiles |
| `agentic-commerce-merchant-stack-psp` | Stripe ACS, Adyen Agentic, and Worldpay enablement · PSP agentic product reference · processor-by-processor delegated checkout status · which PSP exposes a named agentic product |
| `how-to-sell-on-chatgpt` | ChatGPT merchant setup guide · step-by-step ChatGPT feed and syndication guide |

**禁止**：`reference trilogy`、连续一句链出 34+35+36 且锚文本均为 slug 标题复读。

---

## 3. Hub-Spoke 推荐互链（写在正文）

| 新文类型 | 必链 | 推荐 |
|----------|------|------|
| 任意新文 | `/blog/what-is-clink` | 相关 spoke |
| EvaluationComparison | what-is-clink + mor-vs-psp 或 smart-routing | — |
| Product（churn/routing/Lovable） | what-is-clink + smart-routing 或 mor-vs-psp | — |
| Opinion（agent） | what-is-clink + agent-payments | — |

---

## 4. Pipeline 建议正文互链

| 新 slug | 建议链向 |
|---------|---------|
| payment-orchestration-single-psp | what-is-clink, smart-routing |
| clink-vs-stripe | what-is-clink, mor-vs-psp, smart-routing |
| reduce-involuntary-churn-routing | what-is-clink, smart-routing |

---

## 5. Forbidden（G6）

`/vs/stripe` · `/vs/paddle` · `/pricing` · `/for/saas` · `/for/indie` · `/learn/*` · `/customers/*`

---

## 6. 外链

| 类型 | 要求 |
|------|------|
| 权威 | 2–6 |
| 竞品官网 | 可用；HTML 时 `rel="nofollow noopener"` |
| Placeholder | 禁止 example.com / TBD |

---

*internal-links · v1.2.0 · 2026-09-01*
