# Lessie 资源工具与落地页映射

**文档职责**：本文是 **资源/工具型落地页的路径、门控、CTA、关键词意图与选题依据** 的维护入口；**不含**主产品能力详解（见 [lessie-features.md](./lessie-features.md) §五及全文）。

> **关联**：[lessie.md](./lessie.md) | [lessie-features.md](./lessie-features.md) | [lessie-keywords.md](./lessie-keywords.md)（**§2.11 及长尾、月搜、KD 的数字权威**）| [lessie-competitors.md](./lessie-competitors.md)（品牌格局与工具集总览）| [lessie-profile.md](./lessie-profile.md) | [lessie-lists.md](./lessie-lists.md) | [lessie-use-cases.md](./lessie-use-cases.md) | [lessie-investor-profile.md](./lessie-investor-profile.md) | [lessie-twitter-avatar-search.md](./lessie-twitter-avatar-search.md)  
> **分工**：竞品品牌与工具集格局以 [lessie-competitors.md](./lessie-competitors.md) 为准；**附录**为工具页专项素材与外链样本，**非上线承诺**。路径与实际上线 URL 以站点 sitemap / 内部 site-structure（若有）抓取为准。

**Last updated**: 2026-04-08 — 主表唯一详表化、关键词与附录去重、Toolkit 迁入附录。

---

## Tools vs Features（边界）

- **主产品功能、四步流程、Credits 逻辑** → [lessie-features.md](./lessie-features.md)。  
- **本文** → 仅「单点工具页」的路径、免费/登录边界、引流叙述与 SEO 选题；**Tools = 建联能力的轻量切片 + 漏斗**，非第二套产品说明。  
- **对外**：小工具写成「免费完成一件事」；各页 CTA 回 **People Search 核心**（如 app.lessie.ai）。  
- **小工具**：页内直接使用、无注册（文中已列上限为准）。**平台工具**：需登录或 Credits。

---

## 关键词与搜索量口径

- **主意图短语**见下表「主意图关键词」列；**扩展长尾、月搜、KD** 仅维护于 [lessie-keywords.md](./lessie-keywords.md) **§2.11**，本文**不重复**罗列。  
- 下表「搜索量梯队」为规划口径，**须 Semrush/Ahrefs/GKP 复核**后回填 keywords 文档。

---

## 主映射表（唯一详表）

| # | 工具（对外名） | 类型 | 状态 | 建议路径 | 门控 | 能力摘要（详述见 features） | 主意图关键词 | 搜索量梯队 | CTA / 备注 |
|---|----------------|------|------|----------|------|-----------------------------|--------------|------------|------------|
| 1 | Email Verifier | 小工具 | 上线 | `/email-verifier` | 无注册 | 单条/批量至多 500；RFC 5322、DNS、MX、disposable、role、deliverability 等校验 | email verifier, email verification, bulk email checker | 高（红海） | 强调 free、no signup、批量上限；CTA → 核心产品 |
| 2 | Email Permutator | 小工具 | 上线 | `/email-permutator` | 无注册 | 姓名+域名 → 20+ 格式变体（first.last、flast 等） | email permutator, email finder, find email address | 中 | 与 #1 串联「验证 → 猜邮」；CTA → 核心产品 |
| 3 | Twitter Profile Search | 小工具 | 上线 | `/twitter-profile-search` | 无注册 | 图/文搜索；CLIP 向量；10M+ 头像索引 | Twitter profile search, Twitter avatar search, find Twitter by photo | 待验证 | 深度竞品与生态见 [lessie-twitter-avatar-search.md](./lessie-twitter-avatar-search.md)；CTA → 核心产品 |
| 4 | AI Email Outreach Engine | 平台 | 上线 | `/email-marketing` | Credits | 千人千面；多场景（Influencer/Client/Investor 等） | AI email marketing, personalized email outreach | 中 | 落地页对齐高意向；数据声明与功能边界见 features |
| 5 | AI Email Outreach Tool | 平台 | 上线 | `/email-outreach` | Credits | 冷邮件规模化；研究 prospect、个性化、发送节奏 | AI email outreach tool, cold email, personalized cold email | 中 | 与 #4 分工清晰时在导航与内链避免语义完全重复 |
| 6 | Email Addresses List | 平台 | 上线 | `/email-addresses-list` | Credits | 大规模档案建表；行业/职位/公司/地域等维度 | email addresses list, email list builder, targeted email list | 中 | 工作流上游：建表 → #1 验证 → #2 补全 → 触达 |
| 7 | Calendar link generator | 小工具 | 备选 | `/calendar-link-generator`（规划） | 待定 | Add to Calendar / ICS，补「触达→预约」 | add to calendar link, calendar link generator | 待验证 | 见附录 A、B；与 [lessie-competitors.md](./lessie-competitors.md) §5 对照 |
| 8 | Mailto link generator | 小工具 | 备选 | `/mailto-generator`（规划） | 待定 | 带 subject/body/cc/bcc 的 mailto | mailto link generator, email link generator | 待验证 | 同上 |

---

## 工作流与信息架构

**邮件建联主路径**：Email Addresses List（#6）→ Email Verifier（#1）→ Email Permutator（#2）→ AI Email Outreach（#4/#5）。**Twitter Profile Search（#3）** 独立服务于「找 Twitter 账号」，可与 People Search 叙事交叉链。

**Resources 聚合**：下列路径建议在资源区并列展示，各页 CTA 指向 People Search / app。

```
Resources
  ├── /email-marketing
  ├── /email-outreach
  ├── /email-addresses-list
  ├── /twitter-profile-search
  ├── /email-verifier
  └── /email-permutator
```

---

## 转化与排序提示

- **#1–#2**：摩擦最低，适合作为自然搜索与外链落地首站；H1/meta 强化 *free*、*no signup*、批量与速度 proof。  
- **#6**：高意向上游；内链指向 #1/#2/#5，减少跳失。  
- **#4 vs #5**：若 SERP 与站内检索易混淆，在 title 与首屏区分「营销型千人千面」与「冷邮件规模化」。  
- **#3**：视觉/图搜意图杂，单独优化；竞品与合规叙事见 [lessie-twitter-avatar-search.md](./lessie-twitter-avatar-search.md)。  
- **#7–#8**：与 Outreach「预约/一键写信」叙事绑定后再上 P1；避免与核心 six 工具争抢维护带宽。

---

## SEO 顾问待办（避免重复上表）

- 用 Semrush/Ahrefs **拉主词、月搜、KD**，回填 [lessie-keywords.md](./lessie-keywords.md) §2.11，并同步调整上表「梯队」。  
- 六工具页 **独立 title/meta/H1**；sitemap 纳入已上线工具 URL。  
- **#7–#8**：定是否独立 URL、与 Verifier 子路径或聚合页的关系；参考附录与 [lessie-competitors.md](./lessie-competitors.md) §5。  
- 备选：email spam checker、blacklist checker、subject line generator 等是否并入 #1 或单页——见附录 C。

---

## 维护

- **上线 URL** 以站点 sitemap / 内部 site-structure 为准；新增或改路径后回写本文主表与 keywords。  
- **附录外链**每季或改版前抽样检查失效链接。  
- **Twitter / 邮箱类工具**合规与表述变更时同步 features 与对外页。

---

## 附录 A：需求侧证（独立工具页样本）

> 有**单独工具 URL** 通常表示存在工具型搜索需求；≠ 必须复制竞品路径。链接失效请自换。

| # | 竞品独立页示例 | 侧证 | 备注 |
|---|----------------|------|------|
| 1 | [Hunter Email Verifier](https://hunter.io/email-verifier)、[NeverBounce](https://neverbounce.com/)、[ZeroBounce](https://www.zerobounce.net/) | 强 | 多为 Freemium/付费 |
| 2 | [Hunter Email Finder](https://hunter.io/email-finder)、[Snov.io](https://snov.io/email-finder)、[RocketReach](https://rocketreach.co/) | 强 | 与 permutator/finder 意图重叠 |
| 3 | 图搜/社交发现类（FaceCheck.ID、ProFaceFinder 等） | 中 | 详见 [lessie-twitter-avatar-search.md](./lessie-twitter-avatar-search.md) |
| 4–5 | [Mailmeteor AI Email Writer](https://mailmeteor.com/tools)、同类 cold email AI | 中 | 与平台 outreach 页竞合 |
| 6 | 各 B2B 数据/列表商列表页 | 中 | 与「list builder」意图重叠 |

---

## 附录 B：Toolkit  landscape（选题素材）

### B.1 Customer.io Free Email Tools

**来源**：[customer.io/tools](https://customer.io/tools)

| 工具 | 功能 | 关键词 | 是否适合 Lessie |
|------|------|--------|-----------------|
| **Calendar link generator** | Google/Outlook/Yahoo 等 Add to Calendar、ICS | add to calendar link, calendar link generator, ICS generator | ✅ 适合：预约闭环 |
| **Mailto link generator** | subject、body、cc、bcc | mailto link generator, email link generator | ✅ 适合：与触达互补 |
| **EML viewer** | 上传 EML 查看 | EML viewer | ⚪ 可选 |
| **Scroll my email / Email ipsum / Video thumbnail / Placeholder image** | 设计向 | — | ❌ 与建联弱相关 |
| **Carbon footprint / CORS / paste / Examine email** | ESG 或技术向 | — | ❌ 或 ⚪ 研究用 |

**建议优先**：Calendar、Mailto（与主表 #7–#8 一致）。

### B.2 其他 Toolkit 一览

| Toolkit | 网站 | 工具示例 | 与 Lessie 重叠/差异 |
|---------|------|----------|---------------------|
| **Customer.io** | [customer.io/tools](https://customer.io/tools) | 11+ 小工具 | Calendar、Mailto 互补 |
| **Mailmeteor** | [mailmeteor.com/tools](https://mailmeteor.com/tools) | Spam Checker、Finder、Checker、Permutator、Mailto、AI Writer、Blacklist 等 | **高重叠** #1/#2；可借鉴 Spam、Blacklist |
| **ZeroBounce** | [zerobounce.net/free-email-tools](https://zerobounce.net/free-email-tools) | Verification、BIMI、DMARC、DKIM/SPF、Blacklist | 重叠验证；认证类偏 deliverability |
| **Hunter.io** | [hunter.io](https://hunter.io) | Finder、Verifier、Bulk、Domain Search | **高重叠**；免费额度有限 |
| **Snov.io** | [snov.io](https://snov.io) | Finder、Verification、Bulk domain | 重叠 Finder/Verify |
| **Campaign Monitor** | [campaignmonitor.com/resources/tools](https://campaignmonitor.com/resources/tools) | CSS Inliner、按钮/背景、表单 | 偏开发/设计 |
| **HubSpot** | [hubspot.com/free-business-tools](https://www.hubspot.com/free-business-tools) | Signature、Persona、Grader 等 | 偏通用营销 |
| **Klaviyo** | [klaviyo.com/tools/email-subject-line-generator](https://www.klaviyo.com/tools/email-subject-line-generator) | Subject Line Generator | 与撰写相关，可选题 |
| **Litmus** | [litmus.com/resources/pre-send-toolkit](https://www.litmus.com/resources/pre-send-toolkit) | 预览、模板、客户端占比 | 偏测试 |
| **Mailchimp** | [mailchimp.com/resources](https://mailchimp.com/resources) | Subject helper、AI 内容 | 偏营销 |
| **Examine.email** | [examine.email](https://examine.email/) | ESP 识别 | 研究参考 |
| **Labnol / Calen.events** | labnol.org、calen.events | Add to Calendar | 与 #7 同类参考 |

---

## 附录 C：备选关键词与机会（非承诺排期）

| 关键词 | 意图 | 竞品覆盖 | Lessie 机会 |
|--------|------|----------|-------------|
| free email tools / email toolkit | 聚合 | 多家 Toolkit | 强化 Resources 聚合页 |
| email spam checker | 工具 | Mailmeteor 等 | 待建或并入 #1 |
| email finder free | 工具 | Hunter、Snov、Mailmeteor | 强化 #2 finder 语义 |
| email checker | 工具 | Hunter、ZeroBounce、Mailmeteor | 对齐 #1 |
| blacklist checker | 工具 | ZeroBounce、Mailmeteor | 并入 #1 或独立 |
| email subject line generator | 工具 | Klaviyo、CoSchedule 等 | 可选；与 #4/#5 撰写协同 |
| cold email AI | 工具 | Mailmeteor 等 | 已有 #5 |
| BIMI / DMARC / DKIM generator | 工具 | ZeroBounce 等 | 偏认证，与建联弱相关 |

---

## 文档导航

| 文档 | 用途 |
|------|------|
| [lessie-twitter-avatar-search.md](./lessie-twitter-avatar-search.md) | Twitter Profile Search 与 Nuwa、Sherlock 等对照 |
| [lessie.md](./lessie.md) | 主文档、定位、ICP |
| [lessie-features.md](./lessie-features.md) | 功能与资源工具总述 |
| [lessie-profile.md](./lessie-profile.md) | Profile Directory |
| [lessie-investor-profile.md](./lessie-investor-profile.md) | Investor Profile；CTA 可链 Outreach |
| [lessie-lists.md](./lessie-lists.md) | List Directory |
| [lessie-use-cases.md](./lessie-use-cases.md) | Use Cases、内链与 CTA |
| [lessie-keywords.md](./lessie-keywords.md) | 关键词与 §2.11 资源工具词 |
| [lessie-competitors.md](./lessie-competitors.md) | 竞品与 §5 工具集（与附录 B 呼应） |
