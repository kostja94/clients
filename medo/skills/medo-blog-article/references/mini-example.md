# Mini Example — #29 medo-vs-lovable

> Agent 在 Phase 1（Brief）与 Phase 3（Outline）前加载。范例对应下一篇 P0 优先级。

---

## 1. Phase 0 干跑摘要

```
## Mode: standard
## ArticleType: SearchCapture
## InvestmentScore: 4.2 — {五因子摘要：搜索需求 4 / 商业相关性 5 / 差异化 4 / 证据可得性 4 / 生命周期 4}
## Topic Scope: ai-mobile-app / C2 对比选择
## Author: Kostja

Gate A: KEEP
- 搜索意图独立：medo vs lovable / lovable alternative 无已有文
- 读者阶段：Tool selection（Evaluation）
- 深度不可压缩：移动输出 + 上架路径对比 >800 词

信息增量（≥1，Phase 0R R2+R3 验证）：
- Native Swift/Kotlin vs Lovable Capacitor web-wrap 深度对比
- 非开发者 TestFlight/QR 路径 vs Lovable 额外 wrap 步骤
- Wirecutter 式：≥1 Lovable 优势场景 + ≥1 MeDo 优势场景
```

---

## 2. Article Brief（完整范例）

```markdown
## Article Brief

**Mode**: standard
**ArticleType**: SearchCapture
**InvestmentScore**: 4.2
**SuccessMetric**: {可量化 — 选型页 /blog/medo-vs-lovable 排名进入 SERP Top 5 + Demo 点击}
**MoatAssetPlanned**: 原创三分类框架（native vs cross-platform vs web wrapper）+ 双工作流并列表
**AnswerBlocks**:
  1. What are MeDo and Lovable, actually?
  2. What kind of mobile output does each tool produce?
  3. How do the build → test → ship workflows compare?
  4. How do pricing and code ownership compare?
  5. When should a non-developer choose one over the other?
**PostPublishReviewDates**: T+7 / T+30 / T+90 / T+180

**Working title**: MeDo vs Lovable: Which AI Builder Ships Real Mobile Apps?
**Primary keyword**: MeDo vs Lovable
**Article type**: Alternative
**MeDo category**: Guide
**Search intent**: Commercial
**Reader stage**: Tool selection
**Publish goal**: SEO + Conversion
**Target audience**: Non-developer with a mobile app idea, evaluating MeDo vs Lovable after seeing PH/social buzz
**Synthesis Statement**（来自 Phase 0R）: {R3 验证后填写}
**One-line thesis**: Native output is the whole game for mobile — Lovable wins web SaaS, MeDo wins App Store paths.
**Word count target**: 2200–2600
**Cluster role**: Spoke
**Cluster ID**: ai-mobile-app
**Pillar link**: /blog/how-to-build-mobile-app-with-ai
**Differentiation angle**: Lovable official content never writes this comparison; we own native-vs-wrap narrative
**Information increment**:
  1. Side-by-side mobile output architecture (native generators vs web wrappers)
  2. Build → QR test → TestFlight vs build → export → Capacitor wrap → submit
  3. Honest "when Lovable is better" for web SaaS MVPs
**Planned internal links**:
  - /blog/how-to-build-mobile-app-with-ai
  - /blog/best-ai-mobile-app-builders
  - /blog/publish-ai-app-app-store
  - /ai-mobile-app-builder
**KEEP/MERGE**: KEEP
**Author**: Kostja（默认）
```

---

## 3. Phase 2 — Slug + Frontmatter 范例

**Slug 候选**：
1. `medo-vs-lovable` ✅ 推荐
2. `lovable-alternative-mobile-app` — 可用但丢 MeDo 品牌对比意图
3. `medo-lovable-comparison-2026` ❌ 含年份

**publishDate**：对照 content-graph.md 日期表，从锚点日往前逐日分配（每自然日 ≤1 篇）。

**Gate B**：6 问全 Pass；12 反模式零触发。

```yaml
---
title: "MeDo vs Lovable: Which AI Builder Ships Real Mobile Apps?"
description: "MeDo vs Lovable compared for mobile: native Swift/Kotlin vs web-wrapper output, App Store paths, pricing, and when each tool is the better fit."
slug: "medo-vs-lovable"
date: 2026-08-XX       # 发布时间，永不改变（锚点日往前排）
updated: 2026-08-XX    # 可选；无实质更新可省略
author: "Kostja"
category: "Guide"
secondary_category: "Mobile App"
---
```

**SERP Fit**（⚠️ 范例占位 — Agent 执行时须用实际搜索结果替换）：
- Top 3 预期：Lovable 自有 guides、第三方 listicles、Reddit 讨论
- They miss：真原生 vs Capacitor 深度、非开发者上架路径并列
- Our contribution：移动垂类 Wirecutter 式双产品对比

---

## 4. Outline 范例

```markdown
## Outline — medo-vs-lovable

| § | H2 | Answer block ID | Reader mental state | Target words | Links / Notes |
|---|-----|-----------------|---------------------|-------------|---------------|
| Open | hook: mobile icon vs website-in-shell | AB-0 | 刚搜进来：两者都叫 AI builder，选谁？ | 180 | link: best-ai-mobile-app-builders |
| TL;DR | 4 bullets | AB-0 | 找对地方了吗？ | 140 | both products named |
| 1 | What MeDo and Lovable actually are | AB-1 | 两个工具分别解决什么问题？ | 320 | MIAODA + lovable.dev |
| 2 | Side-by-side comparison table | AB-2 | 一眼看到输出类型差异 | 200 | 8-column table |
| 3 | Mobile output: native code vs web wrapper | AB-2 | A1 核心：真原生 vs Capacitor 意味着什么 | 480 | Guideline 4.2 mention |
| 4 | Build, test, and ship: two workflows | AB-3 | 我要做哪些额外步骤？ | 420 | QR/TestFlight vs export/wrap |
| 5 | Pricing, credits, and code ownership | AB-4 | 谁更便宜、代码归谁？ | 300 | as-of {month} {year} |
| 6 | When to choose MeDo — and when to choose Lovable | AB-5 | 我该选哪个？ | 400 | A3 core |
| — | Conclusion | — | 准备行动 / 仍有一个顾虑 | 160 | CTA /ai-mobile-app-builder |
| — | FAQ | — | 具体异议（App Store 拒审） | 420 | 固定 6 题 |

**Estimated total**: ~2,450 words
```

---

## 5. 开篇 + TL;DR 样段（英文）

```markdown
# MeDo vs Lovable: Which AI Builder Ships Real Mobile Apps?

## TL;DR

- **Lovable** is the stronger choice for web SaaS, landing pages, and full-stack React + Supabase apps you plan to host on a URL.
- **MeDo** is the stronger choice for non-developers who want native iOS/Android output, QR-based device testing, and a guided App Store path.
- Lovable's mobile route means exporting a web app and wrapping it (Capacitor/Median.co) — faster to start, higher Guideline 4.2 rejection risk.
- MeDo generates Swift and Kotlin directly — younger integration catalog, but the binary is what App Store review expects.
- Neither tool removes store bureaucracy: developer accounts, privacy policies, and reviewer demo logins are still on you.

You want an app on someone's home screen — not another responsive website in a browser tab. **MeDo** and **Lovable** both show up in every "best AI app builder" list in 2026, but they solve different problems. Lovable is exceptional at turning prompts into deployable web apps with Supabase backends. MeDo targets a narrower promise: native Swift and Kotlin from conversation, tested on your phone via QR code, with a path to TestFlight without opening Xcode.

This comparison is written for the non-developer who has already decided the destination is the App Store, not a shareable URL. If you have not chosen a category yet, start with [best AI mobile app builders](/blog/best-ai-mobile-app-builders) — the three-way split (native, cross-platform, web wrapper) matters more than the brand names.
```

---

## 6. SelfCheck 填写示例（节选）

| # | 维度 | Result | Notes |
|---|------|--------|-------|
| 1 | Publishability | Pass | H0–H4 预检通过（G1–G7 + A1–A4 零触发） |
| 3 | Differentiation | Pass | Native vs wrap workflow 为 SERP 独有 |
| 7 | Objectivity | Pass | §6 含 "When Lovable is better" |
| 9 | SEO / SERP | Pass | BLUF 三处 Pass；title/desc 合规 |
| 11 | Slug Design | Pass | medo-vs-lovable Gate B 全 Pass |
| 12 | MeDo-Specific | Pass | 三分类一致；未抢 ai-mobile-app-builder title |

---

## 7. Phase 6 交付文件名

```
medo/blog/26-medo-vs-lovable.md
```

交付后提示人类更新 `blog/README.md` 文章表（#06 行）。
