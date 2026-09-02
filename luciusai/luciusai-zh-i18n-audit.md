# Lucius AI 中文页面 i18n 审计报告

> **审计日期**：2026-09-02  
> **范围**：luciusai.com 全部 `/zh` 及 `/zh/*` 页面  
> **方法**：实站抓取 + `site.js` 源码分析 + 多 agent 并行页面审计  
> **关联**：[luciusai-site-structure.md](./luciusai-site-structure.md)

---

## 1. 执行摘要

中文站存在 **三层** 未翻译问题，影响所有 89 个有 `/zh/` 版本的页面：

| 层级 | 位置 | 影响范围 | 严重度 |
|------|------|---------|--------|
| **全局 Shell** | `/pages/site.js` 导航/页脚（Lucius 自有文案） | 全站 89 页 | 🔴 Critical |
| **全局 Meta** | `og:description` 仍为英文 slogan | 全站 89 页 | 🔴 Critical |
| **页面正文** | 各 HTML 页面内嵌 copy | Docs 区最严重（~60+ 处 UI 标签）；`/zh/customer-support` 营销页次之 | 🔴 Critical ~ 🟡 Medium |
| **Blog** | 38 篇文章 + 列表页 | 正文 **100% 已翻译**；8 篇标题英文前缀；nav/footer 同全站 | 🟢 正文 / 🟡 标题 / 🔴 Shell |

**Meta**：已审计 **91 页**（营销 52 + Blog 39）；`<title>` 与 `description` 多为中文 ✅；但 **`og:description` 全站仍为 `Lucius AI teammates that get things done`**。中文站翻译质量：**Blog（~97%）> 功能/渠道页 > Docs UI 标签 > `/zh/customer-support` 营销页**。

### 1.1 翻译策略：保留英文（不纳入修复项）

以下类型 **刻意保留英文**，审计中不再计为 i18n 缺陷：

| 类别 | 示例 | 说明 |
|------|------|------|
| **渠道品牌名** | Discord、Slack、Telegram、WhatsApp、Lark | 全球统一品牌，nav/footer/正文出现英文属正常 |
| **飞书** | Feishu | 与 Lark 并用时可写「飞书 / Lark」；单独 Feishu 品牌名可保留 |
| **第三方控制台 UI 镜像** | Discord：`New Application`、`Server Members Intent`、`Save Changes` 等；Slack/Telegram 接入步骤中与实产品界面一致的按钮/菜单文案 | 与用户所见开发者后台一致，翻译反而增加对照成本 |
| **Blog / 文档中的渠道相关 SEO 词** | `Discord Poll Bot`、`Discord server rules`、正文中的 `Discord`、`poll bot` | 目标读者搜索英文词，标题可保留英文前缀 |
| **其他全球产品/竞品名** | ChatGPT、Claude、Ticket Tool、Gmail、Microsoft 365 | 同上 |

**仍需翻译**（与渠道品牌无关的用户面向文案）：

- Lucius 角色名：Customer Support → 客户支持、Community Operator → 社区运营 等
- 导航/页脚 Lucius 自有文案：Agents、Discover、案例卡片描述
- 营销页段落、CTA、Docs 侧栏与 Lucius 产品 UI 标签（非第三方镜像部分）
- 整句英文描述（如 `Deliver exceptional customer support…`），即使句中含 Discord 也须译成中文

---

## 2. 全局问题（site.js — 一次修复覆盖全站）

**文件**：`https://luciusai.com/pages/site.js?v=20260821-1`

### 2.1 `copy.zh` 对象中仍为英文的 key

| Key | 当前 zh 值 | 建议 |
|-----|-----------|------|
| `roles` | `Agents` | `AI 队友` 或 `Agents`（若保留品牌词需统一） |
| `roleSystem` | `Lucius Agents` | `Lucius AI 队友` |
| `customerSupport` | `Customer Support` | `客户支持` |
| `support` | `Community Operator` | `社区运营` |
| `moderator` | `Moderator` | `社区管理员` |
| `emailSupport` | `Email Assistant` | `邮件助手` |
| `website` | `Website` | `网站` |
| `discover` | `Discover` | `发现` |
| `spamCase` | `Moderator · 垃圾信息防护` | `社区管理员 · 垃圾信息防护` |

### 2.2 硬编码英文（未走 `t()` 函数）

**渠道品牌名 — 保留英文 ✅（见 §1.1，不修复）**

nav/footer 中的 Discord、Telegram、Lark、Slack、Email、WhatsApp 符合策略，**不计为缺陷**。

**仍需修复的硬编码：**

- `Utell · AI Tool`
- `Museon · KOL Operations`
- `Jarsy · Financial Product`

**页脚 AI Summary 区**（约 L340）：

- `aria-label="AI summary services"` 未本地化

**产品名/品牌**（见 §1.1，保留英文 ✅）：

- ChatGPT、Claude、Gemini、Perplexity、Discord、Slack 等
- Lucius AI logo alt 文本（品牌名可保留）

### 2.3 已正确翻译的全局项 ✅

- `bookDemo` → 预约演示
- `footerSummary` → AI 队友在你的团队工作现场工作。
- `footerLanguage` → 中文
- `mainNav` → 主导航
- `channels` → 渠道
- `features` → 功能
- `blog` → 博客
- `pricing` / `price` → 价格
- `legal` / `privacy` / `terms` / `dpa` → 已中文化
- 联系销售 mailto 模板（`contactSalesTemplates.zh`）→ 已中文化

### 2.4 全站 Open Graph meta（HTML `<head>`）

| 字段 | 当前值（zh 页） | 建议 | 严重度 |
|------|----------------|------|--------|
| `og:description` | `Lucius AI teammates that get things done` | 改为中文 slogan（如「能真正干活的 AI 队友」） | 🔴 Critical |
| `og:site_name` | `Lucius AI` | 可保留品牌名 | 🟡 Medium |
| `title` 后缀 | `— Lucius AI` / `— Lucius Docs` | 可保留 | 🟢 Low |

---

## 3. 首页 `/zh` 正文问题

| 区域 | 英文内容 | 严重度 |
|------|---------|--------|
| 产品演示 UI mock | Overview, Tasks, My Tasks, All Tasks, Unassigned, Schedule, CONTEXT, Conversation, CONFIG, Business Card, Integrations, Settings, Messages handled, Knowledge learned, Tasks created, Activities, View more, Lucius advice, Onboarding To-do, Credits usage, See details, Support Teammate Web Widget, Sales Teammate Calendar 等 | 🟡 Medium（演示截图/UI） |
| Agent 卡片标题 | Customer Support, Community Operator, Email Assistant | 🔴 High |
| 渠道 Lark | `Invite Lucius to Lark.`（Discord/Slack 等渠道名本身 ✅ 保留；此句为 Lucius 邀请文案，建议改中文） | 🟡 Medium |
| 客户评价 | 5 条 testimonial 全文英文 | 🟡 Medium |
| 其余 Hero/功能/定价/FAQ | 已中文化 ✅ | — |

---

## 4. 角色页问题

### 4.1 `/zh/customer-support`（用户报告页）

| 区域 | 英文内容示例 | 严重度 |
|------|------------|--------|
| Hero | `Deliver exceptional customer support at any scale` + 整段描述 | 🔴 High |
| 功能卡片 ×6 | `Answer customer questions`, `Collect the right details`, `Create support cases`, `Escalate with context`, `Keep customer history connected`, `Follow your support rules` + 各卡片正文 | 🔴 High |
| 能力列表 | `Troubleshoot access...`, `Create support cases for your team`, `Escalate billing...` 等 7 条英文 | 🔴 High |
| 工作流示例 ×7 | 6 个标题英文（Account access issue, Technical troubleshooting, Billing escalation, Refund and cancellation request, Urgent customer issue）+ 全部 Example 引语 + 描述段落 | 🟡 Medium |
| 人工交接 | `Human handoff when it matters` + 整节英文 | 🔴 High |
| 上手步骤 | `Start supporting customers in four steps` + 4 步英文 | 🔴 High |
| 持续学习 | `Gets better with every resolved case` + 部分卡片英文 | 🔴 High |
| 可见可控 | 标题已中文，但 `See why Lucius answered...` 等描述英文 | 🔴 High |
| CRM 层 | 标题已中文，但 `Ask Lucius to send follow-ups...` 等英文 | 🔴 High |
| 底部 CTA | `Give every customer a better answer` + 描述 | 🔴 High |
| 已翻译 ✅ | meta title、部分列表项（3 条中文 bullet）、`内置支持工作流`、`无答案交接`、`人工交接` 标签 | — |

### 4.2 `/zh/customer-support/community`

| 区域 | 英文内容 | 严重度 |
|------|---------|--------|
| 区块标题 | `Support 可以做什么`（Support 未译） | 🔴 High |
| 区块标题 | `Act on customers with Al`（全英文，且 Al 应为 AI） | 🔴 High |
| 描述/列表 | `Answer visitors in the website chat.`；3 条 bullet（Auto-reply to common FAQs 等） | 🟡 Medium |
| 角色/渠道标签 | Website, Discord, Slack 等 | ✅ 保留（§1.1） |

### 4.3 `/zh/customer-support/email`

正文主体已中文化；残留 **Email Assistant**、**Customer Support**、**Administrator** 等产品角色名混用（🟡 Medium）。

### 4.4 `/zh/community-moderation`

正文主体已中文化；**Moderator**、**Administrator** 作为角色名在标题与叙述中反复出现（🟡 Medium）。

### 4.5 `/zh/administrator`

正文主体已中文化；**Administrator**、Support、Moderator、Policy、Flow、Persona 等配置术语混用（🟡 Medium）。

---

## 5. Core / 渠道 / 功能页（25 页审计结果）

> 来源：[Audit zh core/roles/channels](a0182725-7b6c-435a-8317-5e478d059013)（2026-09-02）

### 5.1 正文已达标（除全局 nav/footer 外）

| 页面 | 备注 |
|------|------|
| `/zh/features` | 正文已基本全中文 |
| `/zh/pricing` | 正文中文；含 Role、Credit Dashboard、Flow SOP 等产品术语 |
| `/zh/administrator` | 正文中文；角色/配置术语混用 |
| `/zh/community-moderation` | 正文中文；Moderator/Administrator 混用 |
| `/zh/customer-support/email` | 正文中文；角色名混用 |
| `/zh/channels` + 7 个子页 | 正文中文；discord/telegram/feishu/slack/email/whatsapp 质量较好 |
| `/zh/features/knowledge` | 正文全中文 ✅ |
| `/zh/features/customer-profile` | 正文全中文 ✅ |
| `/zh/features/tasks` | 正文全中文 ✅ |
| `/zh/features/automation` | 正文全中文 ✅ |
| `/zh/features/data-analysis` | 正文中文；UI 标签 `Ask Lucius`、SQL 示例为英文（low） |

### 5.2 仍有正文问题的页面

| 页面 | 主要英文残留 | 严重度 |
|------|-------------|--------|
| `/zh` | 演示 UI mock 全文；Agent 卡片标题；Lark 邀请语（`Invite Lucius to Lark` 建议改）；5 条客户评价 | 🔴 High ~ 🟡 Low |
| `/zh/roles` | 卡片标题 Customer Support、Moderator | 🔴 High |
| `/zh/discover` | `Discover More about Lucius Agents` | 🔴 High |
| `/zh/profile` | `Who it's for` | 🔴 High |
| `/zh/channels/website` | 场景标题 Homepage / Product / Checkout；角色 Community Operator、Sales Assistant | 🔴 High |
| `/zh/customer-support` | **整页正文几乎全英文**（最严重单页） | 🔴 Critical |
| `/zh/customer-support/community` | 见 §4.2 | 🔴 High |

### 5.3 已审计：Use Cases / Case Studies / Discover 子页

> 来源：[Audit zh docs/use-cases pages](5afc6482-f821-4b62-8746-8b5abfa2536d)（2026-09-02）

| 页面 | 主要英文残留 | 严重度 |
|------|-------------|--------|
| `/zh/use-cases` | 卡片标题 `Sales Assistant · …`、`Moderator · …` | 🟡 Medium |
| `/zh/use-cases/admin-governance` | `Tool Permissions`；Community Support / Administrator / Email Assistant 混用 | 🔴 High ~ 🟡 Medium |
| `/zh/use-cases/operations-analytics` | `Ask Lucius`；Administrator 混用 | 🟡 Medium |
| `/zh/use-cases/ai-sales-assistant` | `Sales Assistant`；整句英文 `WhatsApp, Discord, Slack, Telegram, and Feishu.`（渠道名可保留，**整句须改中文**） | 🔴 High |
| `/zh/use-cases/ai-spam-defense` | `Lucius Moderator`；整句英文渠道列举（同上） | 🔴 High |
| `/zh/case-studies` | 三案例卡片标题 `Utell · AI Tool` 等（与 footer 硬编码相同） | 🔴 High |
| `/zh/case-studies/utell` | `Community Operator`；`Website 和 Discord` 中 Discord 为品牌名 ✅ | 🔴 High（角色名） |
| `/zh/case-studies/museon` | KOL、FAQ（行业/技术缩写，低） | 🟢 Low |
| `/zh/case-studies/jarsy` | 引用占位符 `姓名 · Jarsy 职位` 未翻译 | 🔴 High |
| `/zh/discover/social-content-community` | `Community Operator` 标题/CTA | 🔴 High |
| `/zh/discover/automate-refund-email` | `Email Assistant` 标题/CTA | 🔴 High |
| `/zh/discover/smart-welcome-guide` | `Community Operator`；正文 `真正的 onboarding 应该…` | 🔴 High |

---

## 6. 文档页 `/zh/docs/*`（15 页）

> 来源：[Audit zh docs/use-cases pages](5afc6482-f821-4b62-8746-8b5abfa2536d)（2026-09-02）

**Docs 区是英文残留最严重的区域**（约 60+ 处纯英文 UI 标签），框架段落已中文化，但产品 UI 镜像文案大量未译。

### 6.1 技术问题：SSR 内容相同

**所有 `/zh/docs/*` 子页 SSR 返回相同正文**（221 项问题完全一致），仅 `<title>` 和 meta description 因路由不同而略有差异。子路径可能依赖客户端 JS 滚动定位，而非独立 SSR 内容——需工程侧修复，否则 SEO 与直接访问体验受损。

**涵盖 URL**（15 页，问题相同）：

```
/zh/docs, /zh/docs/ai-teammates, /zh/docs/channels,
/zh/docs/channels/{discord,email,feishu,slack,telegram,website},
/zh/docs/{customer-profile,faq,knowledge-base,reply-rules,self-learning,tasks-and-handoff}
```

实站存在但未进 sitemap：`/docs/channels/discord` → `/zh/docs/channels/discord`

### 6.2 Docs 侧栏（全 Docs 区）

| 英文文本 | 严重度 |
|---------|--------|
| `Getting started` | 🔴 High |
| `Start Guide` | 🔴 High |
| `Feishu / Lark` | 🔴 High（侧栏导航文案，建议「飞书 / Lark」） |

### 6.3 上线待办 / CTA

| 英文文本 | 严重度 |
|---------|--------|
| `Connect a platform` | 🔴 High |
| `Create an agent` | 🔴 High |
| `Upload knowledge` | 🔴 High |

### 6.4 Web Widget 配置 UI

`Allowed origins`、`Always enabled`、`Save branding`、`Script tag`、`npm package`、`Connected` / `Disable`、`Integrations → Web Widget` 等（🔴 High）

### 6.5 Email 集成 UI

`Add mailbox`、`Connected mailboxes`、`Discovered mailbox channels`、`Uninstall` / `Refresh`、`Connect Gmail` / `Connect Microsoft`、`Bot name`、`Mailbox address`、`IMAP host / port`、`Gmail / Google Workspace` 等（🔴 High，约 20+ 项）

### 6.6 各渠道接入步骤 UI（第三方控制台镜像 — 保留英文 ✅）

Discord / Slack / Telegram 开发者后台中的按钮、菜单、权限项（如 `New Application`、`OAuth & Permissions`、`Group Privacy`）**与实产品界面一致，不翻译**（§1.1）。

### 6.7 角色名混用（仍需处理）

`Website`、`Customer Support Agent` 等 Lucius 自有文案（🟡 Medium）；渠道品牌名 Discord/Slack 等（✅ 保留）

---

## 7. Blog `/zh/blog`（39 页，全量审计）

> 来源：[Audit zh blog pages sample](bb81bcf7-6e37-46f2-93f3-447b5d9c7a38)（2026-09-02）  
> 脚本：`temp/audit_lucius_zh_blog.py`

### 7.1 覆盖率摘要

| 维度 | 结论 | 估计 |
|------|------|------|
| 文章正文 | 38/38 篇均有中文正文，**无整篇英文未译** | **100%** |
| 正文中文字主导 | 平均 zh_ratio 0.93–0.97 | **~97%** |
| 标题/H1 对用户友好 | 30/38 中文主导 | **~79%** |
| Meta description | 多数中文，但嵌入 SEO 英文词 | **~65%** |
| Nav/Footer | 与全站相同 site.js 问题 | **~40%** |
| **综合体验** | 中文站翻译完成度最高的区块 | **~85–90%** |

### 7.2 列表页 `/zh/blog`

| 字段 | 状态 |
|------|------|
| `<title>` `博客 — Lucius AI` | ✅ |
| Hero H1 / 副标题 | ✅ 中文 |
| 分类标签（AI 治理、社区、运营指南 等） | ✅ |
| Nav/Footer | 🔴 同 §2 |

### 7.3 8 篇标题英文前缀（可选优化，非必须）

以下标题含英文 SEO 词；其中 **Discord 相关 3 篇**（`discord-poll-bot`、`discord-security-bot`、`discord-server-rules`）按 §1.1 **可保留英文前缀**。

| Slug | 当前标题示例 | 是否必须改 |
|------|-------------|-----------|
| `human-in-the-loop-ai` | Human in the Loop AI：… | 建议改（非渠道品牌） |
| `agentic-ai-workforce` | Agentic AI Workforce：… | 建议改 |
| `automate-email-responses` | Automate Email Responses：… | 建议改 |
| `automate-repetitive-tasks` | Automate Repetitive Tasks：… | 建议改 |
| `how-to-automate-my-business` | How to Automate My Business：… | 建议改 |
| `how-to-build-an-online-community` | How to build an online community：… | 建议改 |
| `discord-poll-bot` | Discord Poll Bot：… | **可保留** |
| `discord-security-bot` | Discord security bot：… | **可保留** |
| `discord-server-rules` | Discord server rules：… | **可保留** |

非 Discord 类标题若改，建议中文主导，英文 SEO 词放括号或仅保留在 slug。

### 7.4 正文英文残留（策略保留 vs 应译未译）

以下属 **intentional 保留**（§1.1），非漏译：

- **渠道/产品/竞品名**：Discord、Ticket Tool、EasyPoll、Intercom Fin、OpenClaw
- SEO 嵌入词：`how to build an online community`、`automate email responses`
- 技术/学术术语：Task、Activity Log、RPA、RL、PPO、RBAC
- 英文学术原文引用（如 BCG 论文段落）

### 7.5 结论

Blog **不是「没翻译」**，而是壳层（nav/footer）+ 8 篇标题 SEO 混排拖后腿。只修 Blog 不修 `site.js`，用户读文章时仍会看到英文导航。

---

## 8. 无法语版页面（预期行为）

以下 3 页在 `site.js` 的 `englishOnlyPublicPaths` 中显式排除，**无 `/zh/` 版本**（符合设计）：

- `/privacy`
- `/terms`
- `/security/dpa`

---

## 9. Knockin 子站

| 路径 | zh 版 |
|------|-------|
| `/knockin` | ✅ `/zh/knockin` |
| `/knockin/*` 其余 7 页 | ❌ 无 zh |

Knockin 未收录 sitemap，中文覆盖极低。

---

## 10. 问题统计（91 页全量审计完成，2026-09-02）

| 严重度 | 数量 | 主要来源 |
|--------|------|---------|
| **Critical** | ~10 项 | site.js 未译 key（不含渠道名）；`og:description` |
| **High** | ~80+ 项 | Docs Lucius 自有 UI；`/zh/customer-support` 全文；角色名/整句英文 |
| **Medium** | ~40 项 | 非 Discord 类 Blog 标题；角色名混用 |
| **Low** | ~15 项 | 客户评价、SQL 示例 |
| **排除（不修复）** | — | Discord/Slack/Telegram/WhatsApp/Lark 品牌名；第三方控制台 UI 镜像；Discord 类 Blog 标题 |

| 区块 | 本地化质量（高→低） |
|------|-------------------|
| Blog 正文 | ~97% ✅ |
| Features / Channels 营销页 | ~85% |
| Docs 框架段落 | ~80% |
| Docs UI 镜像标签 | ~30% |
| `/zh/customer-support` | ~15% |
| Nav/Footer（全站） | ~40% |

机器可读明细：`temp/zh_localization_audit.json`、`temp/audit_lucius_zh_blog.py`

---

## 11. 修复优先级建议

### P0 — 全站 meta + site.js

1. 将全站 `og:description` 改为中文 slogan
2. 补全 `copy.zh` 中 9 个英文 key（§2.1，**不含**渠道品牌名）
3. 页脚案例链接文案中文化

### P0 — 单页/单区最严重

- **`/zh/customer-support`**：整页正文翻译
- **Docs 区**：侧栏（Getting started 等）+ 上线待办三步骤 + Email/Widget 等 **Lucius 产品 UI** 标签
- **Docs SSR**：为各 `/zh/docs/*` 子页提供独立 SSR 内容
- ~~Discord/Slack/Telegram 接入步骤 UI~~ → **不译**（§1.1）

### P1 — 营销页角色名与整句英文

1. 统一本地化 `Community Operator`、`Email Assistant`、`Sales Assistant`、`Moderator`、`Tool Permissions`
2. 整句英文改中文（句内 Discord/Slack 等品牌名可保留）
3. `/zh` 首页、discover 子页、case-studies 卡片标题

### P2 — 零散 high 标题

- `Discover More about Lucius Agents`、`Who it's for`、`Act on customers with Al`、`Homepage/Product/Checkout`
- Agent/Moderator/Administrator 等产品角色名是否统一中文

### P3 — Blog（可选）

1. 非 Discord 类 5–6 篇标题可改中文主导（见 §7.3）
2. Discord 类 3 篇标题 **可保留** 英文前缀
3. Meta description 改纯中文（SEO 词保留 slug/正文）

---

## 12. 验证清单

上线后逐页检查：

- [ ] 导航 Lucius 自有项为中文（Agents、Discover、角色下拉等；**Discord/Slack 等品牌名除外**）
- [ ] 页脚案例列、法律区无应译未译英文（**渠道品牌名列除外**）
- [ ] `<html lang="zh">` 正确
- [ ] 页面正文无英文段落（Example 引语除外，若保留需标注）
- [ ] CTA 按钮「预约演示」等非 Book demo
- [ ] `og:description` 为中文
- [ ] GSC International Targeting hreflang 无报错

---

## 13. 审计进度

| 分组 | 页面数 | 状态 | 来源 |
|------|--------|------|------|
| Core + Roles + Channels + Features | 25 | ✅ | [Audit zh core/roles/channels](a0182725-7b6c-435a-8317-5e478d059013) |
| Docs + Use cases + Case studies + Discover 子页 | 27 | ✅ | [Audit zh docs/use-cases pages](5afc6482-f821-4b62-8746-8b5abfa2536d) |
| Blog（列表 + 38 篇，全量） | 39 | ✅ | [Audit zh blog pages sample](bb81bcf7-6e37-46f2-93f3-447b5d9c7a38) |

**审计状态**：主站 89 个 `/zh/*` URL **已全部覆盖**（含 Knockin 首页、profile 等未单独分组页已含在前两组）。Knockin 子站其余 7 页无 zh 版，未纳入。

---

## 14. 总结

中文站 i18n 问题 **不是均匀分布**：

1. **一次修复、全站受益**：`site.js` copy.zh（9 key，不含渠道名）+ 页脚案例 + `og:description`
2. **单页最严重**：`/zh/customer-support` 正文几乎全英文
3. **单区最严重**：Docs Lucius 自有 UI + SSR 子页内容相同（Discord 等第三方控制台镜像 **不译**）
4. **已完成最好**：Blog 38 篇正文 100% 中文化

**保留英文**：Discord / Slack / Telegram / WhatsApp / Lark 等品牌名，及第三方开发者后台 UI 镜像文案。

修复顺序建议：**P0 site.js/meta → P0 customer-support + Docs（Lucius UI）→ P1 角色名 → P3 Blog（仅非 Discord 标题，可选）**。

---

*最后更新：2026-09-02 | 策略：Discord 等渠道品牌名及第三方 UI 镜像保留英文*
