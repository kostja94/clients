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

---

## 2. Hub-Spoke 推荐互链（写在正文）

| 新文类型 | 必链 | 推荐 |
|----------|------|------|
| 任意新文 | `/blog/what-is-clink` | 相关 spoke |
| EvaluationComparison | what-is-clink + mor-vs-psp 或 smart-routing | — |
| Product（churn/routing/Lovable） | what-is-clink + smart-routing 或 mor-vs-psp | — |
| Opinion（agent） | what-is-clink + agent-payments | — |

---

## 3. Pipeline 建议正文互链

| 新 slug | 建议链向 |
|---------|---------|
| payment-orchestration-single-psp | what-is-clink, smart-routing |
| clink-vs-stripe | what-is-clink, mor-vs-psp, smart-routing |
| reduce-involuntary-churn-routing | what-is-clink, smart-routing |

---

## 4. Forbidden（G6）

`/vs/stripe` · `/vs/paddle` · `/pricing` · `/for/saas` · `/for/indie` · `/learn/*` · `/customers/*`

---

## 5. 外链

| 类型 | 要求 |
|------|------|
| 权威 | 2–6 |
| 竞品官网 | 可用；HTML 时 `rel="nofollow noopener"` |
| Placeholder | 禁止 example.com / TBD |

---

*internal-links · v1.1.0 · 2026-07-21*
