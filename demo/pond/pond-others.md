# Pond — 杂项（数据来源 / 合规 / 待验证）

> 归档无法归入七核心文档的事实层内容。每区独立维护。

---

## 1. 站点抓取记录

| 日期 | URL | 状态 | 要点 |
|------|-----|------|------|
| 2026-08-12 | `https://joinpond.ai/` | 成功 | 定位、平台数据、Trending Tasks、Agent 案例、投资方、团队 |
| 2026-08-12 | `https://joinpond.ai/tasks` | 成功 | 任务市场实况、具体 bounty 列表 |
| 2026-08-12 | `https://joinpond.ai/discoveries` | 成功 | 排行榜、数据核验声明、在榜 startup 数据 |
| 2026-08-12 | `https://joinpond.ai/markets` | 成功 | 投资者名录、SAFE/token warrant FAQ、Vault 机制 |
| 2026-08-12 | `https://joinpond.ai/points` | 成功 | 每日积分任务（内容少） |
| 2026-08-12 | `https://joinpond.ai/pricing` | 404 | 无定价页 |
| 2026-08-12 | `https://joinpond.ai/sitemap.xml` | 500 | 无法抓取 |
| 2026-08-12 | `https://joinpond.ai/robots.txt` | 成功 | Cloudflare 模板 + Content-Signal + Disallow /llms-full.txt |
| 2026-08-12 | `https://joinpond.ai/llms.txt`、`/llms-full.txt` | 成功 | 官方 AI 内容声明与推荐关键词 |
| 2026-08-12 | `docs.joinpond.ai`（llms.txt） | 成功 | 14 篇文档清单（含 Bounties FAQs、Markets、Referral、法务） |

---

## 2. 数据来源与第三方信息

| 信息 | 来源 | 日期 |
|------|------|------|
| 融资 $7.5M Seed（Archetype 领投、Coinbase Ventures/Delphi/cyberFund/NEAR/Anagram + 30+ 天使） | 官网 "Backed by the Best" 区块；VCBacked、CoinCarp、fundz.net、vcpedia（多源存在日期口径差异：2024-11 / 2026-02 / 2026-08，`⚠️ 以官网团队页与平台叙事为准，具体官宣日期待验证`） | 2026-08-12 |
| Upwork 服务费（最高 15%）、Fiverr 抽成 20% | upwork.com / fiverr.com 公开费率 | 2026-08-12 |
| Kaggle 为 Google 旗下 | 行业公开事实 | 2026-08-12 |
| AngelList $170B+ AUM | eqvista.com | 2026-08 |
| Wefunder 2025 Reg CF $109M（份额 ~33%）、StartEngine $89M、Republic $20M | stackingtrades.com / angelinvestorsnetwork.com | 2026-08 |
| AITasker 未融资、2026 年悉尼成立 | tracxn.com / LinkedIn | 2026-08-12 |
| Pond 定价为 freemium、无公开高级套餐 | needaiforthis.com / stork.ai | 2026-08 |

---

## 3. 合规 / 法务要点

| 项目 | 内容 | 来源 |
|------|------|------|
| Terms of Use | Effective Date: 2026-04-27 | docs.joinpond.ai/docs/terms-of-use |
| Privacy Policy | Last Modified: 2026-01-25 | docs.joinpond.ai/docs/privacy-policy |
| Copyright Policy | Last Modified: 2025-02-03 | docs.joinpond.ai/docs/copyright-policy |
| General Disclaimer | 存在独立免责声明页 | docs.joinpond.ai/docs/general-disclaimer |
| Markets 免责声明 | 页内 "Pond provides tools and information only and does not constitute advice or endorsement. Please review carefully and make independent decisions" | `/markets` 2026-08-12 |
| robots 内容信号 | Content-Signal: search=yes, ai-train=no, use=reference；屏蔽 GPTBot/ClaudeBot/Google-Extended 等 AI 爬虫；Disallow `/llms-full.txt` | robots.txt 2026-08-12 |

> 注：robots.txt 屏蔽主流 AI 训练爬虫、但公开 llms-full.txt 供检索引用——其策略为"禁止训练、允许参考检索"。

---

## 4. 待验证项归档

| ID | 条目 | 来源文档 | 状态 |
|----|------|---------|------|
| P1 | 首页平台数据（252,317 用户 / 34 tasks / $30,715 paid out）与任务页/案例规模的量级矛盾 | [features](./pond-features.md) | `⚠️ 待验证：统计口径（如"已完成并付款的任务数"）需向官方确认` |
| P2 | 平台抽佣比例（任务发布侧 + Markets 融资侧） | [features](./pond-features.md) | `⚠️ 待验证` |
| P3 | sitemap.xml 有效性（当前 500）与任务详情 URL 模式 | [site-structure](./pond-site-structure.md) | `⚠️ 待验证` |
| P4 | 所有关键词搜索量/难度 | [keywords](./pond-keywords.md) | `⚠️ 待验证：Semrush/Ahrefs` |
| P5 | 融资官宣日期（多源 2024-11 / 2026-02 / 2026-08） | 主文档 §客户概览 | `⚠️ 待验证` |
| P6 | 提现方式与到账时效（Pond wallet / 指定钱包分发） | [features](./pond-features.md) | `⚠️ 待验证` |
| P7 | 多语言计划 | [site-structure](./pond-site-structure.md) | `⚠️ 待验证` |

---

> 关联：[主文档](./pond.md) | [site-structure](./pond-site-structure.md) | [features](./pond-features.md) | [keywords](./pond-keywords.md) | [competitors](./pond-competitors.md) | [use-cases](./pond-use-cases.md) | [growth-strategy](./pond-growth-strategy.md)

*Last updated: 2026-08-12*
