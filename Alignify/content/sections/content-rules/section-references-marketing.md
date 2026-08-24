# Marketing 文章 References 规则

> **关联**：[section-references.md](./section-references.md)（通用规范）· [template-marketing.md](../templates/template-marketing.md)（其他类目可参考此模板结构）

**适用范围**：`content/marketing/{en,zh}/*.md`；References 在 `references-data.json`。

通用规范（字段结构、展示规则、日期格式）见 [section-references.md](./section-references.md)。本文仅补充 Marketing 类目特有的引用策略。

---

## 一、引用定位

Marketing 文章的 references 服务于**策略验证与案例溯源**——读者在了解增长策略、定价模型、渠道打法后，应能通过引用直达案例原文、行业报告或分析框架，从而：

- 验证文中策略的数据依据
- 深入阅读完整案例研究
- 了解行业趋势的来源与方法论

Marketing references 以**案例研究 + 行业分析 + 厂商报告**为主，与 SEO 的「官方技术文档」风格不同。

---

## 二、每页引用数量与结构

| 页面类型 | 最少引用条数 | 建议结构 |
|---------|------------|---------|
| 策略指南类（pricing-strategy, sales-funnel, geo 等） | 3–5 条 | L3 行业分析 ×1–2 + L4 案例研究 ×1–2 + L5 数据 ×1 |
| 渠道/平台类（affiliate, influencer, x-formerly-twitter 等） | 3–5 条 | L3 专题分析 ×1 + L4 案例 ×1–2 + L5 平台官方 ×1 |
| 工具/操作类（keyword-research, competitive-analysis 等） | 3 条 | L3 指南 ×1 + L4 工具报告 ×1 + L5 数据 ×1 |
| 品牌/视觉类（brand-visual 等） | 2–3 条 | L3 设计系统引用 ×1–2 + L4 品牌案例 ×1 |

**底线**：每条引用必须有 `title` 和 `url`；建议填写 `source` 和 `description`。

---

## 三、Marketing 专属来源质量层级

| 层级 | 来源类型 | 适用场景 | 示例 |
|------|---------|---------|------|
| **L2 行业框架/官方** | a16z, First Round Review, Lenny's Newsletter, Reforge | 引用定价框架、增长模型、市场分析 | a16z 定价与包装框架、First Round 增长指南 |
| **L3 专业媒体/研究** | Backlinko, Influencer Marketing Hub, Statista, eMarketer | 引用行业趋势、策略对比、数据 | Backlinko SEO vs GEO 对比、Influencer Marketing Hub 报告 |
| **L4 案例研究** | Impact.com, Rewardful, ReferralRock, 各公司官方博客 | 引用具体案例、增长数据、实施方案 | Dropbox 推荐计划案例、Canva 联盟营销案例 |
| **L5 平台/工具数据** | Appsumo, Product Hunt, GitHub, G2, TrustRadius | 引用平台数据、定价模式、用户反馈 | Appsumo 上架指南、Product Hunt 发布数据 |

**不适用**：L1 学术论文（Marketing 属实践学科，极少需要论文引用）。

---

## 四、每页引用方向速查

### 4.1 已有 references 的页面

| slug | 当前条数 | 质量评估 | 建议 |
|------|---------|---------|------|
| `affiliate` | 12 (ZH+EN) | ✅ 好 — 案例丰富，source + description 齐全 | 维持，检查 URL 可访问性 |
| `brand-visual` | 已有 | ✅ 好 | 检查 URL 可访问性 |
| `sales-funnel` | 已有 | ✅ OK | 检查 URL 可访问性 |
| `geo` | 2 (ZH+EN) | ⚠️ 仅 2 条 | 补充 1–2 条：可加 Search Engine Journal GEO 专文、Google AI Overviews 白皮书 |
| `influencer` | 3 (ZH+EN) | ⚠️ 刚好 3 条 | 补充 1–2 条最新数据（2026 Creator Economy 报告） |
| `keyword-research` | 3 (ZH+EN) | ⚠️ 刚好 3 条 | 补充 1 条最新工具对比或趋势 |
| `lifetime-deal` | 8 (ZH+EN) | ✅ 好 | 维持 |
| `pricing-strategy` | 8 (ZH+EN) | ✅ 好 — a16z 框架引用扎实 | 维持 |
| `referral-program` | 8 (ZH+EN) | ✅ 好 — 案例丰富 | 维持 |
| `x-formerly-twitter` | 4 (ZH+EN) | ✅ OK — GitHub + Buffer 分析 | 补充 1 条最新平台数据 |

### 4.2 完全缺失 references 的页面

| slug | 建议引用方向 |
|------|------------|
| `competitive-analysis` | CB Insights 竞争分析报告、Porter's Five Forces 框架文章、G2 竞品对比功能文档 |
| `creator-challenge-program` | 创作者经济报告（ConvertKit/Stripe）、挑战赛活动案例（Product Hunt/Appsumo）、社区运营研究 |
| `creator-program` | ConvertKit Creator Economy Report、Stripe Atlas 创作者指南、Kickstarter 众筹数据 |
| `email-marketing` | Litmus Email Analytics、HubSpot 邮件营销统计、Campaign Monitor 基准报告 |
| `localization-strategy` | CSA Research 本地化 ROI 报告、Nimdzi 语言服务市场、Unbabel 多语言内容研究 |
| `marketing-types` | HubSpot Marketing Statistics、Gartner CMO Spend Survey、Statista 数字营销支出 |
| `reddit` | Reddit 官方广告文档、Reddit 用户数据（Statista）、Reddit 营销案例研究 |

---

## 五、数据字段填写约定（Marketing 类目）

| 字段 | Marketing 页面约定 |
|------|-------------------|
| `title` | 采用案例/文章原标题。合理中英混用：官方名称保持英文，说明文字用中文。 |
| `url` | 优先稳定可访问的原文链接。案例研究通常来自 Impact.com / Rewardful 等平台。 |
| `source` | 填写发布机构的标准名称：`Andreessen Horowitz (a16z)`、`Backlinko`、`Impact.com`、`ReferralRock`。不写多余后缀如「官网」「博客」。 |
| `date` | 案例研究填写发布年份；持续更新的资源用 `持续更新`（中文）/ `Updated regularly`（英文）。 |
| `description` | 一句话说明参考价值（如「Dropbox 推荐奖励计划 15 个月内 3900% 增长的案例研究」），不超 60 字。 |

---

## 六、修复优先级

| 优先级 | 页面数 | 问题 | 方式 |
|--------|--------|------|------|
| **P0** | 7+7=14 | references block 完全缺失 | 逐页添加 3 条对口引用 |
| **P1** | 1+1=2 | geo 仅 2 条 | 补充到 3+ 条 |
| **P2** | 7+7=14 | 质量可接受 | 逐页检查 URL 可访问性 + 时效性 |

---

## 七、与 SEO References 规则的差异

| 维度 | SEO | Marketing |
|------|-----|-----------|
| 主要来源 | Google/Bing 官方文档、Schema.org | 行业分析（a16z）、案例研究（Impact.com） |
| 引用风格 | 技术规范导向 | 策略/案例导向 |
| L2 定义 | 官方平台文档 | 行业框架/权威分析 |
| 典型引用数 | 3–5 条 | 3–8 条（案例类可稍多） |
| URL 稳定性 | 高（官方文档极少变动） | 中（案例研究链接可能失效） |

---

## 八、审计与维护

- **审计脚本**：`D:\项目文档\Alignify项目上下文\scripts\audit-marketing-references.py`
- **频率**：新页面发布前检查；存量页面每季度检查 URL 可访问性与时效性
- **新增页面**：创建 Marketing JSON 时必须包含 `references` block，≥3 条对口引用
