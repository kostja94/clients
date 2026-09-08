# Clink — Meta Title & Description（轻量任务）

> **何时用**：用户仅要求优化/生成 title、description（或既存文章的 meta）。**硬性规则**：只读本文件；**禁止**改 H2 / TL;DR / FAQ / 正文；**禁止**跑完整 Phase 0–6 创作流程。
> 新稿 Phase 2 也引用本文件生成 meta（完整流程仍在 SKILL.md §3）。
> Slug 规则不在此处——见 `slug-gate.md`。

---

## 1. Title 公式（按类型）

| 类型 | 公式 | 示例 |
|------|------|------|
| BrandIntroduction | `What Is Clink? — {Value Prop}` | What Is Clink — Payment Infrastructure for an AI-Native World |
| Comparison | `{A} vs {B}: How to Choose {Frame}` | MoR vs PSP — How to Choose the Right Payment Infrastructure Model |
| Product | `{Capability}: How {Mechanism} Recovers {Outcome}` | Smart Payment Routing — How Multi-PSP Orchestration Recovers 3–5% Revenue |
| Opinion | `{Thesis}: The Case for {Category}` | AI Agents Need Payments Too — Agent-Native Transaction Rails |
| EvaluationComparison | `Clink vs {Competitor}: {Differentiator Frame}` | Clink vs Stripe — Billing Meets Orchestration |
| GlossaryTerm | `What Is {Term}? — {Scope}, Explained` | What Is a Burn Rate? — Definition, Formula, and Runway |
| IndustryNews | `{Event} Reported at {Scale} — What It Means for {Audience}` | Stripe OpenRouter Acquisition Reported at $7B+ — What It Means for Agent Payments |
| StripeRisk | `{Situation} — What It Means and What to Do{ / First Steps}` | Stripe Account Suspended, Closed, or Frozen — What to Do in the First 72 Hours |
| AgenticPayments Research | `What Is {Protocol/Scope}? — {Angle} Explained` / `{Scope} — Supported List (2026 Reference)` | What Is x402 Agent Payments? — HTTP 402 Protocol Explained |
| Merchant How-To | `How to {Action} on {Channel} in {Year} — {Guide}` | How to Sell on ChatGPT in 2026 — Merchant Setup Guide |

**Title 公式另见 article-types §3 各类型 H2 首行**（title 与正文 H2 措辞互补，不复制）。

## 2. 字符与关键词规则

| 项 | 规则 |
|----|------|
| Title 长度 | 45–70 chars 优先（**硬上限 90**）；主关键词尽量前置 |
| Description 长度 | 120–160 chars 优先（**硬上限 280**） |
| Description 内容 | 利益 + 主意图关键词；主关键词出现于前 80 chars |
| 写法 | 陈述事实与价值，不用 hype 词（见 writing-constraints §8） |
| GlossaryTerm | Title 保留 "What Is {Term}?" 可读形式；slug 用纯术语不加 `what-is-`（见 article-types §3） |
| 与正文一致性 | meta 必须与正文首段/BLUF 一致，不得引入正文没有的承诺 |

## 3. 轻量任务流程

1. 读取目标文章 frontmatter + TL;DR/首段（确认主关键词与结论）
2. 按 §1 公式产出 2–3 组候选（title + description）
3. 每组标注字符数；推荐含主关键词前置的一组
4. 输出建议修改；**等用户确认后**才写入 frontmatter——不得顺手改正文

## 4. 输出格式

```markdown
## Meta — {slug}
**Current**: title (N chars) / description (N chars)
**Candidate A**: {title} ({N} chars) · {description} ({N} chars)
**Candidate B**: ...
**Recommend**: A — {一句理由}
**Note**: 是否涉及 updated 日期更新 / canonical 影响
```

---

*meta-title-description · v1.0.0 · 2026-09-08 · title-only 轻量入口（禁跑完整流程）*
