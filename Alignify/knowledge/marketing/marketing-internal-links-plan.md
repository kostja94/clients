# Marketing 全站内链优化方案

> **生成**：2026-08-27  
> **规范 SSOT**：[`skills/create-article/rules/internal-links.md`](../../skills/create-article/rules/internal-links.md) Part 4.5（M1–M11）  
> **快照依据**：[`skills/optimize-internal-links/references/site-structure-internal-links.md`](../../skills/optimize-internal-links/references/site-structure-internal-links.md)  
> **部署正文**：`E:\自有部署项目\alignify production\content\marketing\{en,zh}\{slug}.md`

---

## 一、现状摘要

| 指标 | 数值 | 说明 |
|------|------|------|
| Marketing 页 | 17 slug × 2 语言 = **34** | 不含 blog 路由增长文 |
| 零出链（正文 MD） | **10 slug** EN 侧重 | affiliate, creator-*, influencer, reddit, x, localization, growth-case-studies, marketing-types |
| 出链过多 / 堆段 | **geo**, **lifetime-deal**, **ugc-marketing** | 单段 ≥3 链或全文 ≥8 链 |
| 高入链 Hub | pricing-strategy(21), geo(21), affiliate(26), competitive-analysis(18) | 需保持质量，非再加链 |
| 零入链 | **ugc-marketing**(0), **marketing-types**(0) | P0 补入链 |

**核心问题**：不是链太少，而是**分布极不均匀 + 点击意图弱 + 组合拳段堆链**（coding-plan 已修；geo/lifetime-deal/ugc 待修）。

---

## 二、Cluster 互链矩阵（应链向 · 应被链自）

> ✓ = 快照中已有出链 · △ = 入链薄 · ✗ = 零出链/零入链 · **粗体** = P0 待补

### 2.1 Research 基础

| slug | 类型 | 应链向（出） | 应被链自 | 现状 |
|------|------|-------------|----------|------|
| **keyword-research** | A | competitive-analysis, seo/learn-seo | competitive-analysis, geo, indie-hackers, reasons-you-need-seo | △ 仅 1 出链 |
| **competitive-analysis** | A | keyword-research, email-marketing | pricing, geo, lifetime-deal, keyword-research, blog/coding-plan | ✓ 2–3 出链 |

### 2.2 GTM 定价

| slug | 类型 | 应链向（出） | 应被链自 | 现状 |
|------|------|-------------|----------|------|
| **pricing-strategy** | A | competitive-analysis, lifetime-deal, blog/coding-plan | geo, lifetime-deal, indie-hackers, **coding-plan** | ✓ 已补 coding-plan |
| **lifetime-deal** | C | pricing-strategy, blog/rate-limit-reset, affiliate | pricing, ugc, indie-hackers | ⚠️ 10 出链，结论重复 |
| **growth-case-studies** | C | competitive-analysis, geo | indie-hackers | ✗ 零出链 |

### 2.3 Creator 生态

| slug | 类型 | 应链向（出） | 应被链自 | 现状 |
|------|------|-------------|----------|------|
| **creator-program** | C | creator-challenge-program, affiliate, ugc-marketing | geo, influencer, lifetime-deal, ugc | ✗ 零正文链 |
| **creator-challenge-program** | C | creator-program | ugc | △ 1 链 |
| **influencer** | C | creator-program, affiliate | geo, ugc, reddit | ✗ 零正文链 |
| **ugc-marketing** | C | creator-program, affiliate, influencer | **无** | ⚠️ 9 出链 0 入链 |
| **affiliate** | C | referral-program, creator-program | geo, influencer, ugc, lifetime-deal | ✗ 零正文链 |
| **referral-program** | C | affiliate, tools/referral-program, blog/coding-plan | ugc, lifetime-deal | △ 1–2 链 |

### 2.4 Channel 战术

| slug | 类型 | 应链向（出） | 应被链自 | 现状 |
|------|------|-------------|----------|------|
| **geo** | B | blog/ai-visibility, blog/ai-traffic-*, tools/geo, seo/search-engine | 全站高频 | ⚠️ 开篇堆 3 链 |
| **x-formerly-twitter** | B | blog/rate-limit-reset, influencer, indie-hackers | coding-plan, rate-limit-reset | ✗ EN 零链 |
| **reddit** | B | influencer, x-formerly-twitter | indie-hackers | △ 0–2 链 |
| **email-marketing** | B | competitive-analysis, keyword-research | competitive-analysis | ✓ 2 链 |
| **localization-strategy** | B | seo/navigation-menu, seo/submit-website | indie-hackers | ✗ 零链 |

### 2.5 Hub

| slug | 类型 | 应链向（出） | 应被链自 | 现状 |
|------|------|-------------|----------|------|
| **marketing-types** | Hub | pricing-strategy, geo, creator-program, keyword-research（各 1） | **无** | ✗ 零出零入 |

### 2.6 Blog 增长模式（`/blog/*`，category=marketing）

| slug | 应链向 | 组合拳节 |
|------|--------|----------|
| **coding-plan** | rate-limit-reset(×1), pricing, competitive-analysis, referral, x, geo | **零链**（已修） |
| **rate-limit-reset** | pricing(×1), coding-plan, affiliate, competitive-analysis, x | 组合拳 1–2 链，勿堆 |
| **ugc-marketing** | 见上 | 结论 2 链可保留，中段减堆 |

---

## 三、逐页优化指令（17 × EN/ZH 同步）

> 每页目标：**4–5 distinct 出链**，**每段 ≤1 链**，**同 slug 不重复**。  
> 下列「删/移/加」以 **ZH 段落逻辑**为准，EN 镜像。

---

### P0 — 堆链 / 重复 / 零入链

#### `geo`（当前 8–11 出链，2 段 ≥3 链）

| 动作 | 说明 |
|------|------|
| **删** | §什么是 段 1：affiliate + influencer + creator-program **只留 1 条**（建议留 creator-program，句意「GEO 为 creator 生态补可见度」） |
| **移** | affiliate / influencer 移到 **红人/联盟战术节** 各 1 链 |
| **移** | §价值段重复 affiliate+creator → **删重复**，保留纯文字 |
| **保留** | blog/ai-traffic, blog/ai-visibility, tools/geo, seo/search-engine 各 1，分处不同 H2 |
| **锚文本** | 「AI 流量与引用来源指南」「AI 可见度监测」而非 URL  slug |

#### `lifetime-deal`（当前 10 出链，结论段重复 pricing）

| 动作 | 说明 |
|------|------|
| **删** | 结论段 pricing-strategy 链（§什么是 已有） |
| **删** | 表格行内 affiliate 链 → 改正文一句 + 段末 1 链 |
| **移** | rate-limit-reset 仅保留 §专题对照 1 次 |
| **保留** | pricing-strategy, rate-limit-reset, referral-program, competitive-analysis, creator-program, affiliate, seo/landing-page — 共 **6**，分 6 个 H2 |
| **加** | §风险 链 **blog/coding-plan**（订阅 vs LTD 对照，1 句） |

#### `ugc-marketing`（9 出链，0 入链）

| 动作 | 说明 |
|------|------|
| **删** | §1 对比表 4 链 → 表无链，表前 §什么是 用 1 链区分 creator-program |
| **移** | affiliate+referral 合并段：段内 **1 链** affiliate，referral 纯文字 |
| **移** | lifetime-deal / creator-challenge 从结论堆叠 → 各在案例节 1 链 |
| **全局** | 其他 marketing 文至少 **1 处** 链入 ugc-marketing（pricing-strategy 不适用；**influencer**、**creator-program** 优先） |

#### `marketing-types`（Hub，0/0）

| 动作 | 说明 |
|------|------|
| **加** | 4 条：pricing-strategy, geo, creator-program, keyword-research — 分类介绍各 1 链，**无** fifth 堆在结论 |

---

### P1 — 零出链孤岛（10 slug）

每页 **4 条** 出链模板（按 M7 分布）：

| slug | 什么是 | 主体 1 | 主体 2 | 结论/案例 |
|------|--------|--------|--------|-----------|
| **affiliate** | vs referral-program | creator-program | competitive-analysis | tools/affiliate-marketing（工具选型段） |
| **creator-program** | vs ugc-marketing | creator-challenge-program | affiliate | influencer |
| **creator-challenge-program** | vs creator-program | ugc-marketing | — | — |
| **influencer** | vs creator-program | affiliate | ugc-marketing | tools/influencer-marketing |
| **reddit** | vs x-formerly-twitter | influencer | geo | — |
| **x-formerly-twitter** | vs reddit | blog/rate-limit-reset（事件首发） | influencer | — |
| **localization-strategy** | seo/navigation-menu | seo/submit-website | competitive-analysis | — |
| **growth-case-studies** | competitive-analysis | geo | blog/coding-plan 或 rate-limit-reset（二选一） | — |
| **referral-program** | 已有 coding-plan | affiliate | tools/referral-program | — |

**affiliate / creator-program / influencer EN**：若首节 BLUF 已有 1 条姊妹链，正文主体再补 **3 条**（M3：同 URL 全页 1 次）。

---

### P2 — 已尚可，微调

| slug | 动作 |
|------|------|
| **keyword-research** | 加 seo/learn-seo 或 seo/checklist（调研落地）；加 1 句链 competitive-analysis 若仅 1 链 |
| **competitive-analysis** | 加 blog/coding-plan（定价页竞品调研）1 链于框架节 |
| **email-marketing** | 保持 2–3 链；检查 competitive-analysis 与 keyword-research 不同段 |
| **pricing-strategy** | 已有 coding-plan + competitive-analysis + lifetime-deal；结论 **0 链** |
| **referral-program** | 已有 coding-plan；加 affiliate 于「双向奖励」段（若未重复） |

---

## 四、Blog × Marketing 组合拳（已落地标准）

**coding-plan / rate-limit-reset** 互链规则：

| 页 | reset 链 | pricing | referral | competitive | geo | x |
|----|---------|---------|----------|-------------|-----|---|
| coding-plan | §什么是 ×1 | §架构 | §方舟 | §百炼 | §风险 | §vs OpenAI |
| rate-limit-reset | — | §什么是 ×1 | §banked | §benchmark | — | §X 节奏 |
| gtm-combo | **0** | **0** | **0** | **0** | **0** | **0** |

---

## 五、执行批次与验收

| 批次 | 页面 | 工时 | 验收 |
|------|------|------|------|
| **Batch 1** | geo, lifetime-deal, ugc-marketing | 高 | 无段 ≥2 链；ugc 入链 ≥3 |
| **Batch 2** | affiliate, creator-program, influencer, creator-challenge | 中 | 每页 4 distinct |
| **Batch 3** | reddit, x, localization, growth-case-studies, marketing-types | 中 | 零孤岛消除 |
| **Batch 4** | keyword-research, competitive-analysis, email, pricing, referral | 低 | 微调 + 去重 |

**每页 Done 定义**：

- [ ] 4–6 distinct 出链（Hub 除外）
- [ ] 任意段落 ≤1 链（表格无链或 ≤1）
- [ ] 同 URL 全页 1 次
- [ ] TL;DR/HowTo 无链；FAQ **允许**内链（R4 全文 1 次）
- [ ] 锚文本通过「三问」
- [ ] EN/ZH 链接集合同构
- [ ] 跑 `build-site-internal-links-doc.py` 更新快照

---

## 六、Internal Link Plan 模板（单页填写示例）

**页面**：`/zh/marketing/geo`

| # | 锚文本 | 目标 | 段落/H2 | 点击意图 |
|---|--------|------|---------|----------|
| 1 | 创作者计划 | /zh/marketing/creator-program | 什么是 · 第 2 段 | 读者想知 GEO 与 creator 生态关系 |
| 2 | AI 流量与引用来源指南 | /zh/blog/ai-traffic-and-citation-sources | 测量框架 | 读者要查跨平台引用数据 |
| 3 | AI 可见度监测 | /zh/blog/ai-visibility | 工具栈 | 读者要选监测工具 |
| 4 | GEO 工具完整指南 | /zh/tools/geo | 实施 | 读者要选型 SaaS |
| 5 | 搜索引擎分析 | /zh/seo/search-engine | API 机制 | 读者要理解检索供给 |

---

*维护：改版 Marketing 页后更新本节「现状」列，并同步 SSOT。*
