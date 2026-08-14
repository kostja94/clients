# Clink — Writing Constraints

> 加载时机：Phase 4（Draft）· Phase 5（SelfCheck）
> 主文件：SKILL.md §3.4 指针

---

## 1. Voice

| 维度 | 要求 |
|------|------|
| Professional | 精确、数据导向，无空洞 hype |
| Evidence-led | 产品 claim 引用 clinkbill.com 或 docs |
| Fair | 竞品 describe differences, not deficiencies |

---

## 2. BLUF 三处

| # | 位置 | 要求 |
|---|------|------|
| **B1** | TL;DR bullet 1 | 40–60 词直接回答 primary keyword |
| **B2** | 每个 major H2 首段 | 先答后铺背景 |
| **B3** | FAQ 每问 | 首句即答；不得从正文复制粘贴 |

---

## 3. 段落优先协议

1. 每个 H2 第一稿必须是连续段落
2. 禁伪列表（`**Bold label.**` + 单句 × N 替代真列表）
3. 全文完成后：长段落（≥4 句）≥3；列表占比 ≤35%；段间衔接率 ≥70%

---

## 4. 引用分级

| 级别 | 要求 | 示例 |
|------|------|------|
| **P0** | 产品能力、客户名、数字 | 须 `[Source: URL]` 或 as-of clinkbill.com |
| **P1** | 行业估算、Gartner/McKinsey | 限定语 + 来源或年份 |
| **P2** | 内部观察 | `based on customer testimonials on clinkbill.com as of 2026-06` |

**Degraded 模式**（Phase 0R 标注）：无 P0 级未验证 claim。

---

## 5. 漏斗与产品提及

| 类型 | Clink 上限 | 首次出现位置 |
|------|:---:|------|
| BrandIntroduction | ≤30% | 四产品线节后 |
| Comparison | ≤35% | Third Option 节后 |
| Product | ≤40% | 案例节前可透明 |
| Opinion | ≤35% | Clink for Claw 节 |
| EvaluationComparison | ≤45% | 对比表后可透明 |

**规则**：前 60% 须可独立阅读为教育内容；禁止开篇即 sales pitch。

---

## 6. 竞品公平性

- 每主要竞品 ≥1 明确优势
- 禁 just / merely / only does X
- Stripe：承认生态与文档；Clink 定位为编排层非替代
- Paddle：承认 MoR 省心；Clink 强调品牌与便携数据
- Chargebee：承认复杂定价；Clink 强调 routing
- Spreedly：承认编排深度；Clink 含 billing + tax

---

## 7. 金融合规表述

| 场景 | 写法 |
|------|------|
| 定价 | Contact Sales；不写具体 Clink 费率 |
| MoR / tax | 「built-in tax calculation and filing capabilities — specific jurisdictions should be confirmed with Clink」 |
| 成功率/恢复率 | 客户案例须 as-of；3-5% 为行业区间 + 客户证言限定 |
| Clink for Claw | **Early Access** as of June 2026 |
| PCI | PCI DSS 4.0.1（官网宣称） |

---

## 8. 禁止

- revolutionary · game-changing · unlock · seamless · magic
- 「Clink replaces Stripe entirely」（应为 connects to / routes through）
- 无来源的「唯一」「全球首个」
- 编号 H2（`## 1.`）
- frontmatter 写入 `keywords` / `related` / `disclosure`
- FAQ 之后再写任何 H2
- 倒数第二节不是 `## Conclusion`（收束 / CTA / thesis 须写入 Conclusion）

---

*writing-constraints · v1.1.0 · 2026-07-21*
