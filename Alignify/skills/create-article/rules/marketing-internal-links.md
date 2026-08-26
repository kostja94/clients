# Marketing 频道内链规范

> **SSOT 位置**：`skills/create-article/rules/marketing-internal-links.md`  
> **全站共性**：[`internal-links.md`](./internal-links.md) Part 1–2（唯一性、样式、FAQ 禁链）  
> **逐页执行表**：[`knowledge/marketing/marketing-internal-links-plan.md`](../../../knowledge/marketing/marketing-internal-links-plan.md)  
> **快照刷新**：`python scripts/audit/build-site-internal-links-doc.py`  
> **Last updated**：2026-08-27

---

## 一、第一原则：读者想点（Click Intent）

内链优化的**最高优先级**不是 SEO 权重传递，而是：

> **读者读到此处，是否自然产生「我想继续搞清 X」的冲动——而 X 恰好是目标页主题？**

| 通过 | 不通过 |
|------|--------|
| 「触顶后开启 Extra Usage，把 panic 收成按量收入」→ 链 **生成式 AI 定价与包装** | 「详见 [定价策略](/zh/blog/pricing-strategy)」单独成句 |
| 「矩阵 UGC 的 performance 层往往就是联盟计划」→ 链 **联盟营销** | 段末「延伸阅读：A、B、C」清单 |
| 「Claude weekly cap 窗口里，stable Plan 可接迁移」→ 链 **Coding Plan** | 锚文本写「点击这里」「本文」「这篇文章」 |

**自检三问（每条链必过）：**

1. 删掉链接后，句子是否仍通顺？（自然性）
2. 读者点过去，能否在 10 秒内感到「来对了」？（相关性）
3. 若本段已有 1 条链，再加这条是否抢注意力？（分布）

---

## 二、Marketing 规则 M1–M11

| # | 规则 | 说明 |
|---|------|------|
| **M1** | **无硬性条数** | 以点击意图为准；长文通常 3–6 条 distinct 为参考，Hub 页可更少。**不**为凑数加链 |
| **M2** | **每段 ≤1 链** | 同段 2 链仅当不同 H3 子块且不同目标；**禁止 ≥3 链/段** |
| **M3** | 同 URL **全页仅 1 次** | 含正文首段 BLUF；hero 已废弃（E44） |
| **M4** | **FAQ / TL;DR / HowTo 步骤** 无链 | 与全站 §1.5 一致 |
| **M5** | **描述性锚文本** | 用策略名、任务名、平台名；禁 click here / 本文 / learn more |
| **M6** | **高度相关** | 同一 GTM 工作流、互补策略、或经批准的跨频道任务链（见 §四） |
| **M7** | **均匀分布** | 什么是 0–1 · 主体方法论 2–4 · 案例/框架 0–1 · 结论 0–1；**禁止**集中在「组合拳/延伸阅读」单段 |
| **M8** | **链进句子** | 禁止「**Coding Plan + 定价溢出**：[链接]…**+ 邀请裂变**：[链接]…」式标签堆链 |
| **M9** | **结论可含内链** | **0–2** 条；须承接上文未覆盖的**单一**下游任务；禁止清单式堆链（见 [`conclusion.md`](./conclusion.md) §4） |
| **M10** | **表格/列表默认无链** | 表格内链例外须逐条过 M6；优先改正文叙述 |
| **M11** | **只链已上线页** | Brief / Link Plan 禁止含未发布 slug；G6 阻断。姊妹篇、OSS 线等未上线 → 纯文字，不发 `href`；上线后再补反向链 |

---

## 三、推荐分布节奏（A/B/C 三类）

| 类型 | 代表 slug | 内链落点 |
|------|-----------|----------|
| **A 策略框架型** | pricing-strategy, competitive-analysis, keyword-research | 什么是：边界 1 · 框架节：互补方法论 1–2 · 实施/趋势：SEO 或 blog 1 · 结论：0–1 |
| **B 平台战术型** | geo, reddit, x-formerly-twitter, email-marketing | 什么是：平台机制 0 · 战术节：相邻渠道 1 · 测量/合规：SEO/blog 1 · 案例：0–1 |
| **C 项目运营型** | creator-program, referral-program, ugc-marketing, lifetime-deal | 什么是：与邻近策略区分 1 · 激励/招募：相关运营文 1–2 · 合规/定价：1 · 结论：0 |

**Blog GTM / campaign 长文**（`coding-plan`, `rate-limit-reset`, `git-commit-attribution` 等）：内链按 M1–M10；**组合拳节零内链**为常见做法（非强制），链分布在架构/案例/风险节。**结构不套用固定骨架**，见 [`templates/marketing.md` §1.1](./templates/marketing.md#11-可选章节参考非骨架)。

---

## 四、Marketing Cluster 与跨频道节制

### 4.1 站内 Cluster（优先互链）

```
                    marketing-types (Hub)
                           │
     ┌─────────────────────┼─────────────────────┐
     │                     │                     │
 Research 基础          Creator 生态           GTM 定价
 keyword-research      creator-program        pricing-strategy
 competitive-analysis  creator-challenge      lifetime-deal
                       influencer             │
                       ugc-marketing          ├── blog/coding-plan
 affiliate ─────────── referral-program       └── blog/rate-limit-reset
     │
 Channel 战术
 geo · x-formerly-twitter · reddit · email-marketing
 localization-strategy · growth-case-studies
```

### 4.2 批准跨频道链（每页每目标 ≤1）

| 从 Marketing | 可链至 | 触发语境 |
|--------------|--------|----------|
| geo, keyword-research | `/seo/*` | 同一调研/实施任务（如 landing-page, search-engine） |
| geo, competitive-analysis | `/blog/ai-visibility`, `/blog/ai-traffic-*` | 测量 AI 可见度/引用 |
| affiliate, referral-program | `/tools/affiliate-marketing`, `/tools/referral-program` | 「工具选型」非策略定义 |
| pricing-strategy, lifetime-deal | `/blog/coding-plan`, `/blog/rate-limit-reset` | GTM 增长模式对照 |
| localization-strategy | `/seo/navigation-menu`, `/seo/submit-website` | 实施层站点结构 |

**禁止**：为凑数链 `/tools/llm`、无关 SEO 学习页、insights 泛览。

---

## 五、锚文本规范（ZH / EN）

| 场景 | 推荐锚文本 | 避免 |
|------|-----------|------|
| 策略对照 | 生成式 AI 定价与包装 / generative AI pricing and packaging | pricing-strategy 页、点这里 |
| 事件促销 | 用量限额重置 / usage limits reset | reset 文章、这篇 |
| 创作者 | 创作者计划、联盟营销、推荐奖励计划 | creator-program slug |
| 研究 | 关键词调研、竞品分析 | 详见竞品分析 |
| GEO | AI 可见度监测、AI 流量与引用来源 | GEO 工具（除非在工具选型段） |

---

## 六、反模式（立即改）

1. **组合拳段堆链** — `#gtm-combo`、结论「延伸阅读」段 ≥2 链  
2. **同段重复 cluster** — geo 开篇段同时链 affiliate + influencer + creator-program  
3. **表格当导航** — ugc-marketing 对比表 4 链；lifetime-deal 渠道表内嵌 affiliate  
4. **零出链孤岛** — affiliate、creator-program、influencer、reddit（EN）等 0 正文链  
5. **结论重复开篇** — lifetime-deal 结论再链 pricing-strategy（正文已链）  
6. **首节 BLUF + 正文双链同目标** — 如 rate-limit-reset 首节链 pricing，正文再链 pricing（M3 违规，须合并为 1 次）  
7. **机械指路链（M8 变体）** — 「对照 / 详见 / 见 XXX 指南 / 见 XXX 文章 / 系统方法见 / 可配合 XXX」单独成句；结论段为凑数堆「选题对接 A、并借 B」；Hub 自指或「访问 / 查看 XXX 页」。**改法**：链必须嵌在读者正在执行的任务句里——删掉链接后句子仍通顺，且读者点过去 10 秒内感到「来对了」。

**机械 ❌ → 自然 ✅ 示例**

| 机械（禁） | 自然（可） |
|-----------|-----------|
| 改价邮件前可先对照 [竞品分析] 里竞品的邮件节奏 | 改 tier 邮件前先看竞品 pricing 页有没有动过 seat/credits——和监测定价页变更是一轮 desk research（无链或链在「监测定价页」工作流句） |
| tier 与包装见 [定价策略] | reward 若是 credits 升级，得和 [定价策略] 里的 hybrid credits 结构对齐，否则用户算不清值不值 |
| 矩阵 UGC 见 [UGC 营销] 的 flat fee 披露 | 不少团队把 [UGC 营销] 的 flat fee 和 30% 佣金叠在同一合同里——两层须分别披露 |
| 结论：将邮件纳入整合体系，对接 [关键词调研]，并借 [竞品分析] | （删除整句；若需链，放在 Newsletter 选题那句：「选题应与 [关键词调研] 及 Topical Map 对齐」） |

## 七、新建 / 改版工作流

1. 查 [`marketing-internal-links-plan.md`](../../../knowledge/marketing/marketing-internal-links-plan.md) 该 slug 的「应链向 / 应被链自」  
2. 写 **Internal Link Plan** 表（见 [`07-internal-links.md`](../07-internal-links.md)）— 锚文本 / 目标 / 段落 / 点击意图  
3. 落稿：先写无链正文，再按 M7 节奏插入  
4. 自检：M1–M10 + 三问  
5. 刷新 [`../../optimize-internal-links/references/site-structure-internal-links.md`](../../optimize-internal-links/references/site-structure-internal-links.md)

---

## 八、与模板对齐

[`templates/marketing.md`](./templates/marketing.md) §内链 — 创建 checklist 须含 M1–M10。
