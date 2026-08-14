# Internal & External Links 最佳实践 Checklist（Lessie Blog）

> **依据**：与 [Nori blog 内外链清单](../../nori/blog/INTERNAL-EXTERNAL-LINKS-CHECKLIST.md) 同一思路；对齐 [lessie-blog.md](../lessie-blog.md) 转化路径与 [lessie-tools.md](../lessie-tools.md) 工具落地页。  
> **站点**：生产以 **lessie.ai** 为准；正文为 **英文**，本规范为 **中文**。

---

## 链接分层（Lessie）

| 类型 | 路径 / 域名 | 用途 |
|------|-------------|------|
| **Blog 互链** | `/blog/{slug}` | 相关主题文章；**不**用裸域名拼文章 URL |
| **场景 / 产品主 CTA** | `https://lessie.ai/influencer-marketing` | 网红向主落地；其他场景见下表 |
| **邮件 / AI 触达** | `https://lessie.ai/email-marketing` | 网红触达邮件、规模化个性化（见 `influencer-outreach-email-templates` 等） |
| **注册** | `https://app.lessie.ai/login` | Sign up / 试用 |
| **程序化资产** | `https://profile.lessie.ai/`、`https://lists.lessie.ai/` | 公开画像、主题列表 |
| **免费工具** | `https://lessie.ai/tools` | 计算器、审计、对比等 |
| **定价等** | `https://lessie.ai/pricing`（若文中有需要） | 按需，避免堆砌 |

**其他场景页**（非网红主题稿件再启用）：以 [lessie-blog.md](../lessie-blog.md)、[lessie-use-cases.md](../lessie-use-cases.md) 为准，**有对应落地页再链**，无则只写产品名不链。

---

## Internal Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **首段** | ≥1 条 | **主 CTA**（如 influencer-marketing）或 **相关 /blog 文章**；网红线建议首段即点明 People Search Agent |
| **Blog 互链（Body）** | 每篇 **1–4 条**（随博文数量增长） | 仅链至 **`/blog/{slug}`**；相关主题互链（如「工具盘点 ↔ 类型科普」） |
| **产品 / 转化内链** | 按节分布 | **lists、profile、tools、sign-up** 宜在 **不同 H2** 各出现 **至多 1 次**（与 [01-best-ai-tools…](./01-best-ai-tools-influencer-marketing-2026.md) 节奏一致）；文末 **Related Resources** 再汇总 |
| **Related（正文块）** | 文末列表 | 同主题 **blog** + 核心产品 URL；篇数少时 **2–4 条** 即可 |
| **frontmatter `related`** | 数组 of slug | 供 CMS 用；与互链文章 slug 一致 |
| **锚文本** | 描述性 | 避免 "click here"、"learn more"；可混合 exact / partial / branded |
| **竞品官网** | 算 **外链** | 见下文 nofollow，**不算** Blog 互链 |

---

## External Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **权威 / 行业** | **2–8 条**（视篇幅） | 定义、分层、研究报告：如 Sprout Social、Salesforce、Statista、行业媒体 |
| **竞品 / 厂商** | 对比稿必备 | HTML：`<a href="https://…" rel="nofollow noopener">Name</a>`（与 01 稿 Grin/Aspire 等一致）；**锚文本用公司名或产品定位** |
| **锚文本** | 描述性 | 如 "Sprout Social’s breakdown"、"Statista — global influencer advertising market size" |
| **E-E-A-T** | 优先可核对来源 | 数据注明出处；避免不可验证的夸张 ROI |

---

## 可用外链来源（按主题，可扩展）

| 主题 | 来源（示例） | 用途 |
|------|----------------|------|
| 网红分层 / 类型 | 篇 2 **References** 仅保留 [Wikipedia — Influencer marketing](https://en.wikipedia.org/wiki/Influencer_marketing)；正文不具名外链至其他 vendor | 脱敏后行业表述 |
| 市场规模 | [Statista — influencer advertising market](https://www.statista.com/statistics/1092819/global-influencer-market-size/) | 宏观体量（读 methodology） |
| B2B 网红 | [Demand Gen Report](https://www.demandgenreport.com/industry-news/news-brief/the-rise-of-b2b-influencers/49612) 等 | B2B 语境 |
| KOL / 大使 | [GRIN — KOLs and ambassadors](https://grin.co/blog/ambassadors-influencers-and-kols) 等 | 全球标签 |
| 通用背景 | [Wikipedia — Influencer marketing](https://en.wikipedia.org/wiki/Influencer_marketing) | 背景句；**不可替代合规建议** |
| 竞品盘点 | Grin、Aspire、CreatorIQ、Upfluence、HypeAuditor、Modash 等官网 | 对比类文章；**nofollow** |
| 定价 / 刊例 | 篇 3 **References** 仅保留 [Shopify](https://www.shopify.com/blog/influencer-pricing)、[Hootsuite](https://blog.hootsuite.com/influencer-pricing)、[Impact — usage rights](https://impact.com/influencer/how-much-to-charge-for-usage-rights-influencer/) | 正文已脱敏其他 vendor 外链 |

---

## 各篇链接状态（`blog/*.md`）

| # | 文件 / slug | Blog 互链 `/blog/*` | 产品内链（lessie.*） | 外链（权威+竞品） | 备注 |
|---|-------------|---------------------|----------------------|-------------------|------|
| 1 | `01-best-ai-tools…` / `best-ai-tools-for-influencer-marketing` | 正文 → 篇 2、篇 3（How to Choose 等）+ Related（含篇 4–8） | 多节分布 + Related Resources | Statista + 多竞品 nofollow | 竞品对比型；`related` 含篇 2、篇 3、篇 4–8 |
| 2 | `02-types…` / `types-of-influencers` | 正文 → 篇 1（多处）、篇 3（Campaign roles + Matrix）+ Related（含篇 4） | 多节分布 + Related Resources | **References 仅 Wikipedia**；正文 vendor 外链已脱敏 | 与篇 1、篇 3、篇 4 互链；`related` 已配置 |
| 3 | `03-influencer-pricing…` / `influencer-pricing` | 多篇 1、篇 2（正文 + Related，含篇 4） | 多节分布 + Related Resources | **References 仅 Shopify、Hootsuite、Impact**；正文已脱敏 | 定价与合同向；`related` 含篇 1、篇 2、篇 4 |
| 4 | `04-how-to-collaborate…` / `how-to-collaborate-with-influencers` | 正文 → 篇 1–3、篇 8（Fits the Series + Related） | 多节分布 + Related Resources | **References：Wikipedia、FTC Endorsement Guides** | 流程向 playbook；`related` 含篇 1–3、篇 8 |
| 5 | `05-modash-alternatives…` / `modash-alternatives` | 正文 → 篇 1–4、篇 6 + Related | 多节分布 + Related Resources | Statista + Modash/Upfluence/HypeAuditor/Grin/Aspire **nofollow** | Modash 替代方案；`related` 含篇 1–4、篇 6 |
| 6 | `06-how-to-find-influencers…` / `how-to-find-influencers` | 正文 → 篇 1–5、篇 7 + Related | 多节分布 + Related Resources | Wikipedia（influencer + affiliate） | 发现方法论；`related` 含篇 1–5、篇 7 |
| 7 | `07-influencer-marketing-checklist…` / `influencer-marketing-checklist` | 正文 → 篇 1–6、篇 8 + Related | 多节分布 + Related Resources | Wikipedia + FTC Endorsement Guides | 准备清单；`related` 含篇 1–6、篇 8 |
| 8 | `08-influencer-outreach-email-templates…` / `influencer-outreach-email-templates` | 正文 → 篇 2–7 + Related | **email-marketing** + influencer-marketing + tools + lists/profile + login + Related Resources | Wikipedia + FTC Endorsement Guides | 邮件模板与触达；`related` 含篇 2–7 |
| 12 | `12-tiktok-shop-influencer-marketing-guide-2026…` / `tiktok-shop-influencer-marketing-guide` | 正文 → 篇 4、6、7、3、2、5、10 + Related | influencer-marketing + lists/profile + tools + login + Related Resources | **seller.tiktok.com** 官方、**Modash** TikTok Shop guide 作参考、**LTK/ShopMy** nofollow | 社媒向 TikTok Shop 决策长文；`related` 含篇 2、3、4、5、6、7、10 |

**维护**：新增 `blog/*.md` 后在本表增行，并更新 [lessie-blog.md](../lessie-blog.md) §四。

---

## 规范总结

- **Blog 互链**：`/blog/{slug}`；篇 1–8 网红主题互链见上表（含 **influencer-outreach-email-templates**）。  
- **产品内链**：**influencer-marketing** 为主 CTA；**lists / profile / tools / app login** 分节嵌入，文末 **Related Resources** 汇总。  
- **外链**：权威来源 +（若需要）竞品 **nofollow**；锚文本描述性。  
- **锚文本**：避免 "click here"；品牌名与短语混合。

---

*与 [README.md](./README.md) 配合使用：新建文章时执行本清单 + 登记 `lessie-blog.md`。*
