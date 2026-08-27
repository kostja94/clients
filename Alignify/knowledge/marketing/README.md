# knowledgehub / marketing · 增长与独立开发者知识块分册

本目录存放**增长、获客、独立开发者（Indie Hacker）与冷启动**相关的非线性知识块：渠道选择、社区运营、Build in Public、定价与变现叙事等**问题域笔记**。**命名速查**：[README.md](../../../README.md) §十一（命名规范）。

---

## 与 [`knowledgehub/tools/`](../tools/README.md)、[`knowledgehub/seo/`](../seo/README.md) 的关系

| 位置 | 用途 |
|------|------|
| **`knowledge/tools/`** | 与 **`src/data/tools-pages-config.ts`** 中 **`slug` 同名**的 `*.md` 知识块，便于与 **`/tools/[slug]`**、`product/alignify-keywords-tools.md` 对照。 |
| **`knowledge/seo/`** | **不绑定** Tools slug 的 SEO 专册（经典 Web 搜索、technical SEO 等）。 |
| **`knowledge/marketing/`（本目录）** | **不绑定** Tools slug 的增长与 GTM 专册；**建议**与已上线的 **`/marketing/[slug]`** 采用**同名** `*.md`（kebab-case）；尚无对应页时可先用主题短名，上线后重命名以与路由对齐。**不要求**在 `tools-pages-config` 中存在对应项。 |
| **`skills/create-article/rules/`** | 站点内容与模板**规范**；本目录为**网摘与概念整理**，二者互补。 |

**正式文章创作**：[`skills/create-article/SKILL.md`](../../skills/create-article/SKILL.md)

**外部 SSOT（个人知识库 · 唯一维护处）**：增长策略类素材**只在** `E:\个人知识库\增长策略\` 维护，**禁止**在 `knowledge/marketing/` 再建同名 `{slug}.md` 副本。Brief 与 Step 02 登记绝对路径即可。

| slug（Alignify 文章） | 外部 SSOT 路径 |
|------------------------|----------------|
| `rate-limit-reset` | `E:\个人知识库\增长策略\定价促销\Agent限额与Reset促销.md` |
| `coding-plan` | `E:\个人知识库\增长策略\定价促销\Coding-Plan-开发者订阅.md` |
| `lifetime-deal` | `E:\个人知识库\增长策略\定价促销\Lifetime-Deal-终身买断.md` |
| `git-commit-attribution` | `E:\个人知识库\增长策略\产品内嵌\Git-Commit-Attribution-提交归因.md`（中文主称：**AI 提交署名**） |
| `embedded-virality` | `E:\个人知识库\增长策略\产品内嵌\Embedded-Virality-嵌入式病毒传播.md`（中文主称：**Powered-by Badge 与付费去标**） |
| `watermark-growth` | `E:\个人知识库\增长策略\产品内嵌\Pay-to-Remove-Watermark-付费去水印.md`（中文主称：**免费导出带 logo：AI 产品用水印做增长**；SSOT 文件名偏变现，文章主线=增长） |
| `platform-subdomain-gating` | `E:\个人知识库\增长策略\产品内嵌\Platform-Subdomain-平台子域名门控.md`（中文主称：**平台子域增长**） |
| `ugc-marketing` | `E:\个人知识库\增长策略\渠道分发\矩阵UGC-创作者网络.md` |
| `creator-challenge-program` | `E:\个人知识库\增长策略\渠道分发\Creator-Challenge-AI创作者挑战赛.md` · Brief：[`_briefs/creator-challenge-program.md`](./_briefs/creator-challenge-program.md) · Skills：[`marketing-slug-notes/creator-challenge-program.md`](../../skills/create-article/rules/marketing-slug-notes/creator-challenge-program.md) |
| `marketing-types` | `E:\个人知识库\增长策略\Marketing-Types-渠道平台与计划选型.md` · Brief：[`_briefs/marketing-types.md`](./_briefs/marketing-types.md) · Skills：[`marketing-slug-notes/marketing-types.md`](../../skills/create-article/rules/marketing-slug-notes/marketing-types.md) |
| `egc-marketing` | `E:\个人知识库\增长策略\渠道分发\EGC-员工发声-AI与DevTools.md` · Brief：[`_briefs/egc-marketing.md`](./_briefs/egc-marketing.md) · Skills：[`marketing-slug-notes/egc-marketing.md`](../../skills/create-article/rules/marketing-slug-notes/egc-marketing.md) |
| `wrapped-marketing` | `E:\个人知识库\增长策略\运营节奏\Wrapped-参考.md` |

**路由（2026-08-28）**：上表增长策略专题及所有**新 marketing 文**统一发布于 **`/blog/{slug}`**（正文 `content/blog/`）；存量 `/marketing/[slug]` 仅维护不重迁（如 `lifetime-deal`）。

**Alignify 本目录**：仅保留**无外部 SSOT**、或已与 `/marketing/[slug]` 长期对齐的 legacy 知识块（下表 12 篇）。新建增长策略主题 → 个人知识库 + `_briefs/{slug}.md` 登记路径，**不**复制正文到本目录。

---

## 文档结构

新建 `*.md` 时，章节骨架与文首声明沿用 [`../README.md`](../README.md) 中「知识块文档结构」；本专册**无** Tools 页对照时，可省略「站内对照」「Tools 关键词与 slug 映射」，改为：

- `**材料范围**：…`（网摘来源、日期）
- `**规范或长文对照**：…`（链到 `skills/create-article/rules/sections.md`、`insights` 长文或 Agent skill 路径，按需）

---

## 交叉引用（按需维护）

| 文档 | 状态 | 主题 |
|------|------|------|
| [indie-hackers.md](./indie-hackers.md) | ✅ 完整 | Indie Hacker 独立开发者增长（Insights 侧入口见 [../insights/indie-hackers.md](../insights/indie-hackers.md)） |
| [keyword-research.md](./keyword-research.md) | ✅ 完整 | 关键词研究 |
| [geo.md](./geo.md) | ✅ 完整 | GEO 生成式引擎优化 |
| [pricing-strategy.md](./pricing-strategy.md) | ✅ 完整 | 定价策略 |
| [lifetime-deal.md](./lifetime-deal.md) | ✅ 完整 | LTD 终身优惠 |
| [affiliate.md](./affiliate.md) | ✅ 完整 | 联盟营销 |
| [x-formerly-twitter.md](./x-formerly-twitter.md) | ✅ 完整 | X/Twitter 增长 |
| [reddit.md](./reddit.md) | ✅ 完整 | Reddit 营销 |
| [email-marketing.md](./email-marketing.md) | ✅ 完整 | 邮件营销 |
| [localization-strategy.md](./localization-strategy.md) | ✅ 完整 | 本地化策略 |
| [growth-case-studies.md](./growth-case-studies.md) | ✅ 完整 | 增长案例 |
| [competitive-analysis.md](./competitive-analysis.md) | ✅ 完整 | 竞品分析 |

共 12 个文件，其中 12 篇完整、0 篇待补充。

- 全站知识块总说明：[knowledgehub/README.md](../README.md)

---

*本 README 随 `knowledgehub/marketing` 约定变更而更新。*
