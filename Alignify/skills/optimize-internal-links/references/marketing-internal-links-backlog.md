# Marketing / GTM 内链 Backlog（人工维护）

> **快照与逐页出/入链**：见 [`site-structure-internal-links.md`](./site-structure-internal-links.md) **§7.3**（脚本自动生成，勿在此重复写「现状」数字）  
> **规则 SSOT**：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) Part 4.5（M1–M11）

---

## 一、Cluster 互链矩阵（应链向 · 应被链自）

> **现状列**：以 §7.3 自动快照为准（✓ 2+ 出链且无堆链标记 · △ 薄链/EN-ZH 不对称 · ✗ 零出链或零入链 · ⚠ 出链过多或同篇重复）

### 1.1 `/marketing/*` — Research 基础

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **keyword-research** | A | competitive-analysis, seo/learn-seo | competitive-analysis, geo, indie-hackers, reasons-you-need-seo |
| **competitive-analysis** | A | keyword-research, email-marketing | pricing, geo, lifetime-deal, keyword-research, blog/coding-plan |

### 1.2 `/marketing/*` — GTM 定价

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **pricing-strategy** | A | competitive-analysis, lifetime-deal, blog/coding-plan | geo, lifetime-deal, indie-hackers, blog/coding-plan |
| **lifetime-deal** | C | pricing-strategy, blog/rate-limit-reset, affiliate | pricing, blog/ugc-marketing, indie-hackers |
| **growth-case-studies** | C | competitive-analysis, geo | indie-hackers |

### 1.3 `/marketing/*` — Creator 生态

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **creator-program** | C | creator-challenge-program, affiliate, blog/ugc-marketing | geo, influencer, lifetime-deal, blog/ugc-marketing |
| **creator-challenge-program** | C | creator-program, blog/ugc-marketing, blog/watermark-growth, blog/embedded-virality, affiliate | blog/ugc-marketing, wrapped-marketing |
| **influencer** | C | creator-program, affiliate, blog/ugc-marketing | geo, blog/ugc-marketing, reddit |
| **affiliate** | C | referral-program, creator-program | geo, influencer, blog/ugc-marketing, lifetime-deal |
| **referral-program** | C | affiliate, tools/referral-program, blog/coding-plan | blog/ugc-marketing, lifetime-deal |

### 1.4 `/marketing/*` — Channel 战术

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **geo** | B | blog/ai-visibility, blog/ai-traffic-and-citation-sources, tools/geo, seo/search-engine | 全站高频 |
| **x-formerly-twitter** | B | blog/rate-limit-reset, blog/egc-marketing, influencer, indie-hackers | blog/coding-plan, blog/rate-limit-reset, blog/egc-marketing |
| **reddit** | B | influencer, x-formerly-twitter | indie-hackers |
| **email-marketing** | B | competitive-analysis, keyword-research | competitive-analysis |
| **localization-strategy** | B | seo/navigation-menu, seo/submit-website | indie-hackers |

### 1.5 `/marketing/*` — Hub

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **marketing-types** | Hub | pricing-strategy, geo, creator-program, keyword-research（各 1） | 全站 Hub 页 |

### 1.6 `/blog/*` — 增长策略（GTM · category=marketing）

| slug | 应链向 | 组合拳节 |
|------|--------|----------|
| **coding-plan** | rate-limit-reset(×1), pricing, competitive-analysis, referral, x, geo | 各 H2 分散，gtm-combo **0 链** |
| **rate-limit-reset** | pricing(×1), coding-plan, affiliate, competitive-analysis, x | 组合拳 1–2 链，勿堆 |
| **ugc-marketing** | creator-program, affiliate, influencer, rate-limit-reset, lifetime-deal, creator-challenge, blog/egc-marketing | 表无链；结论 ≤2 链 |
| **egc-marketing** | blog/ugc-marketing, creator-challenge-program, blog/rate-limit-reset, x-formerly-twitter, marketing-types, creator-program | 案例 tweet embed；结论 ≤2 链 |
| **wrapped-marketing** | rate-limit-reset, creator-challenge-program, pricing-strategy, blog/ugc-marketing | Q4 仪式对照 |
| **embedded-virality** | git-commit-attribution, watermark-growth, platform-subdomain-gating, pricing-strategy | badge 族互链 |
| **watermark-growth** | embedded-virality, pricing-strategy, platform-subdomain-gating | 导出 watermark 轴 |
| **platform-subdomain-gating** | embedded-virality, watermark-growth, seo/subdomain-vs-subfolder | URL 门控轴 |
| **git-commit-attribution** | embedded-virality, blog/coding-plan, blog/github-for-marketing | 开发者向 embedded |

---

## 二、逐页优化指令（EN/ZH 同步）

> 每页目标：**4–5 distinct 出链**，**每段 ≤1 链**，**同 slug 不重复**。下列「删/移/加」以 **ZH 段落逻辑**为准，EN 镜像。

### P0 — 堆链 / 重复 / 零入链

#### `geo`

| 动作 | 说明 |
|------|------|
| **删** | §什么是 段 1：affiliate + influencer + creator-program **只留 1 条**（建议 creator-program） |
| **移** | affiliate / influencer 移到对应战术节各 1 链 |
| **保留** | blog/ai-traffic, blog/ai-visibility, tools/geo, seo/search-engine 各 1，分处不同 H2 |

#### `lifetime-deal`

| 动作 | 说明 |
|------|------|
| **删** | 结论段 pricing-strategy 链（§什么是 已有） |
| **移** | rate-limit-reset 仅 §专题对照 1 次 |
| **保留** | pricing, rate-limit-reset, referral, competitive-analysis, creator-program, affiliate — **6** 个 H2 分散 |
| **加** | §风险 链 **blog/coding-plan**（订阅 vs LTD，1 句） |

#### `blog/ugc-marketing`

| 动作 | 说明 |
|------|------|
| **删** | 对比表内链 → 表无链，§什么是 用 1 链区分 creator-program |
| **移** | affiliate+referral 合并段内 **1 链** |
| **全局** | influencer、creator-program 至少 1 处链入 |

#### `marketing-types`（Hub）

| 动作 | 说明 |
|------|------|
| **加** | pricing-strategy, geo, creator-program, keyword-research — 分类介绍各 1 链 |

### P1 — EN 零出链孤岛

| slug | 什么是 | 主体 1 | 主体 2 | 结论/案例 |
|------|--------|--------|--------|-----------|
| **affiliate** | vs referral-program | creator-program | competitive-analysis | tools/affiliate-marketing |
| **creator-program** | vs ugc-marketing | creator-challenge-program | affiliate | influencer |
| **creator-challenge-program** | vs creator-program | ugc-marketing | watermark-growth / embedded-virality | affiliate |
| **influencer** | vs creator-program | affiliate | ugc-marketing | tools/influencer-marketing |
| **reddit** | vs x-formerly-twitter | influencer | geo | — |
| **x-formerly-twitter** | vs reddit | blog/rate-limit-reset | influencer | — |
| **localization-strategy** | seo/navigation-menu | seo/submit-website | competitive-analysis | — |
| **growth-case-studies** | competitive-analysis | geo | blog/coding-plan 或 rate-limit-reset | — |
| **referral-program** | coding-plan | affiliate | tools/referral-program | — |
| **keyword-research**（EN） | competitive-analysis | seo/learn-seo | — | — |

### P2 — 微调

| slug | 动作 |
|------|------|
| **competitive-analysis** | 加 blog/coding-plan 于框架节 1 链 |
| **email-marketing** | 保持 2–3 链；keyword / competitive 不同段 |
| **pricing-strategy** | 已有 coding-plan + competitive + lifetime-deal；结论 **0 链** |

---

## 三、Blog × Marketing 组合拳（coding-plan / rate-limit-reset）

| 页 | reset | pricing | referral | competitive | geo | x |
|----|-------|---------|----------|-------------|-----|---|
| coding-plan | §什么是 ×1 | §架构 | §方舟 | §百炼 | §风险 | §vs OpenAI |
| rate-limit-reset | — | §什么是 ×1 | §banked | §benchmark | — | §X 节奏 |
| gtm-combo | **0** | **0** | **0** | **0** | **0** | **0** |

---

## 四、执行批次

| 批次 | 页面 | 验收 |
|------|------|------|
| **Batch 1** | geo, lifetime-deal, blog/ugc-marketing | 无段 ≥2 链；ugc 入链 ≥3 |
| **Batch 2** | affiliate, creator-program, influencer, creator-challenge（**EN 优先**） | 每页 4 distinct |
| **Batch 3** | reddit, x, localization, growth-case-studies, marketing-types | 零 EN 孤岛消除 |
| **Batch 4** | keyword-research, competitive-analysis, email, pricing, referral | 微调 + 去重 |
| **Batch 5** | blog 增长策略 8 篇互链 | embedded ↔ watermark ↔ platform-subdomain 三角 |

**Done 定义**：4–6 distinct 出链 · 段 ≤1 链 · 同 URL 1 次 · EN/ZH 同构 · 跑 `build-site-internal-links-doc.py` 刷新 §7

---

*维护：改版 Marketing / blog GTM 正文后更新矩阵「应链向」；快照数字只信 §7.3，勿写死在本文件。*
