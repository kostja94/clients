# 为什么 Datus 需要一个 Pricing 页面

> **归档说明**：本文档已于 2026-06-21 移入 `_archive/`，不再维护。活跃文档见 [_archive/README.md](./README.md)。

> 写给赵恒 · 2026-06-02  
> 这不是一个「放个价格表」的建议——而是一个关于**信任信号、企业采购流程、开源商业模式透明度**的讨论。

---

## 你的顾虑，我完全理解

Enterprise 定价差异太大，不同客户从 $10K 到 $100K+ 都有可能，放一个固定价格确实会限制谈判空间，也可能在还没讲清楚价值之前就把价格敏感的客户吓跑。

但问题不在「放不放价格数字」，而在**放不放定价信号**。这是两回事。

---

## Pricing 页面上线前 vs 不上线的三个现实风险

### 1. 你让企业采购经理在他们的 form 里填什么

LinkedIn、Expedia、Coinbase 的 POC 进行中，说明已经有企业采购经理介入。他们的流程里有一关叫 **vendor due diligence**——团队需要填：「该供应商是否有公开定价信息？」

- 有 `/pricing` 页 = checkbox 打勾，进入下一步
- 没有 = 采购经理需要写备忘录解释「我们为什么在做评估一个没有公开定价的开源产品」

这不是价格贵不贵的问题，是**采购流程摩擦力**的问题。在 Linkedin/Expedia 这种规模的公司，这个摩擦力可能是额外的 2-3 周审批周期。

### 2. 用户搜 "Datus pricing" 的时候，你给了他们什么

这是一个转化率极高的品牌搜索词——搜这个词的人已经了解你、在评估你、准备做决策。现在这个搜索词 100% 流失——因为没有页面承接。

B2B 买家在联系销售之前，**85% 已经自己完成了需求调研，69% 的购买决策过程在联系 vendor 之前就已经发生**（6sense, 2024）。你不在这个阶段给信息，等于自己退出竞争。

### 3. 开源产品的「没放定价」=「商业模式不清晰」在用户心中是一回事

开源产品用户最担心的不是价格，而是**「这东西会不会突然闭源？」「收费模式会不会随意变？」**。

有 pricing 页列出 Free + Cloud Personal + Enterprise = 你在告诉世界：「我们靠免费产品获取你，靠企业版赚钱」——这是开源公司最诚实的叙事，用户买账。

没有 pricing 页 = 用户默认想：「要么开源就是全部（商业化没戏，不敢依赖）」「要么收费模式不确定（更不敢依赖）」。两种都不利于 POC 转化。

---

## 活跃竞品是怎么做的

| 竞品 | Pricing 页 | 企业版定价方式 |
|------|:---:|------|
| **Cube.dev**（~20K stars，$7.9M ARR） | ✅ 有 | Open Source 免费 + Cloud "Starting at" + Enterprise "Contact Sales" |
| **Wren AI**（~9.8K stars） | ✅ 有 | Open Source 免费 + Cloud 有具体价格 |
| **TextQL / Ana**（$17M 融资） | ✅ 有 | Free ($100/mo) / Team ($250/mo) / Enterprise "Contact" |
| **Defog.ai** | ✅ 有 | $5K/月起，Enterprise "Contact" |
| **dbt Labs** | ✅ 有 | Developer 免费 + Team 有价 + Enterprise "Contact Sales" |
| **Databricks Genie Code** | ✅ 有 | 免费（仅收 compute） |

**6 家关键竞品，6 家都有 pricing 页。** 你们是目前唯一没有的。Enterprise 写 "Contact Us" 是行业标准做法，没人觉得奇怪。

---

## 你可以怎么做：Pricing 页 ≠ 放价格数字

### 核心原则：放价格信号，不放固定价格

用 3 列定价表明确你的商业模式结构：

```
┌─────────────────┬──────────────────┬─────────────────────┐
│   Open Source    │  Cloud Personal  │     Enterprise      │
│      Free        │      Free        │    Contact Us       │
│  Apache 2.0      │  云端免安装       │   SSO / 审计日志     │
│  pip install     │  快速探索试用      │   Shared Context    │
│  核心 CLI + CE   │  内置教程数据集    │   RBAC / SLA        │
│  多模型支持       │                   │   Long-Running Agent│
└─────────────────┴──────────────────┴─────────────────────┘
```

你已经有两列是确定的（Open Source 免费 + Cloud Personal 免费）——这两列本身就是强烈的价格信号。用户看到就知道「我可以从免费开始，需要企业功能时再联系你」。

Enterprise 那列只需要：
- **不写数字**，写 "Contact Us for Enterprise pricing"
- 列功能差异（SSO、审计日志、SLA、Shared Context）——这是企业买家真正关心的，不是价格
- 可以加一句 "Typically deployed at $X–$Y/month based on team size and usage"，如果连范围都不想写也可以省略

### FAQ 区解决企业买家的真正问题

定价表下面加 4-5 个 FAQ，比价格数字更重要：

- "How is Enterprise pricing structured?" → 按 Subagent 数量/团队规模/表数（说明结构即可，不写数字）
- "What kind of companies use Datus Enterprise?" → LinkedIn、Expedia、Coinbase POC 中 + 云器 Lakehouse 生产案例
- "Can I self-host the Enterprise version?" → Yes, contact us for deployment options
- "What's the difference between Cloud Personal and Enterprise?" → 功能对比 + 适用场景
- "Is there a free trial for Enterprise?" → Contact us to set up a POC

### Social proof 放在 Pricing 页底部

这是价格敏感度最高的页面——在这个位置放案例和客户 logo 效果最好：

- 云器 Lakehouse：自助率 15%→60%，查询 30min→3min
- GitHub stars 数、开源社区活跃度
- 创始人背景（阿里 + StarRocks TSC）

这些放在定价页 = 告诉企业买家「你不只是在买一个工具，你在加入一个已经被验证的开源运动」。

---

## 不上 Pricing 页的代价（一个测算）

假设 Datus 官网月活 5K（保守估计），pricing 页的访问占比通常为 10-15%，即 500-750 UV/月。

- 不上线：这 500-750 人 → 不知道收费模式 → 大概率流失
- 上线（纯 "Contact Us" 版）：500-750 人 → 其中 10-15% 会点击 "Contact Us" + 额外 20% 注册 Cloud Personal → **每月多 50-75 个企业线索 + 100-150 个免费用户**
- 6 个月后：300-450 个企业线索池——对于早期阶段的 Datus，这是可观的 pipeline

这不是假设——B2B SaaS 行业基准：pricing 页面的访客 → demo 请求转化率通常在 5-15% 之间。你现在是 0%，因为页面不存在。

---

## 总结

Pricing 页面不是报价单。它是：
- 企业采购流程中过审的必要条件（vendor due diligence checkbox）
- 品牌搜索词「Datus pricing」的接住者（高转化流量不能让它 100% 流失）
- 开源商业模式的「诚实信号」（我们靠免费获取、靠企业版变现——这是最值得信任的叙事）
- 企业线索收集器（"Contact Us" CTA = 每月稳定的 inbound pipeline）

**Enterprise 价格差异大不是不做 pricing 页的理由——恰恰说明你只需要放价格结构（免费 × 2 + 企业 Contact Us），不需要放价格数字。**

不做 pricing 页的竞品，一个都没有。你们做第一个吗？

---

*相关参考：*
- [SaaStr: Why B2B Vendors Don't Show Enterprise Prices — And Why It's Changing](https://www.saastr.com/dear-saastr-why-do-so-many-b2b-vendors-not-show-prices-for-enterprise-plans/)
- [Schematic Podcast: Supabase's Pricing Page — $200M ARR With Radical Transparency](https://schematichq.com/podcast/supabases-pricing-page-a-masterclass-in-predictable-pricing)
- [OpenCore Ventures: Pricing Page as Competitive Advantage for Open-Source Startups](https://handbook.opencoreventures.com/startup-manual/gtm/pricing/pricing-page)
- [6sense: 85% of B2B Buyers Complete Research Before Engaging Sales](https://6sense.com/)

*已归档 · Datus · https://datus.ai/*
