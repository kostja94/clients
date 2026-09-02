# Lucius AI 网站结构与 URL 架构

> **本文职责**：列举 luciusai.com 全部页面 URL 与网站结构。  
> **来源**：luciusai.com 实站分析（sitemap.xml + site.js 导航映射 + 逐 URL 状态码验证）  
> **更新日期**：2026-09-02

---

## 1. 页面清单

### 1.1 核心页面

| 路径 | 页面 | /zh/ 版 |
|------|------|---------|
| `/` | 首页 | ✅ `/zh` |
| `/features` | 功能总览 | ✅ |
| `/pricing` | 定价 | ✅ |
| `/roles` | 角色系统总览 | ✅ |
| `/discover` | Discover | ✅ |
| `/blog` | Blog 列表 | ✅ |
| `/docs` | 文档中心 | ✅ |
| `/profile` | AI Business Card | ✅ |
| `/privacy` | 隐私政策 | ❌ 仅英文 |
| `/terms` | 服务条款 | ❌ 仅英文 |
| `/security/dpa` | 数据处理协议 | ❌ 仅英文 |

### 1.2 角色页（Roles）

| 路径 | 页面 | /zh/ 版 |
|------|------|---------|
| `/customer-support` | Customer Support | ✅ |
| `/customer-support/community` | Community Support | ✅ |
| `/customer-support/email` | Email Support | ✅ |
| `/community-moderation` | Moderator | ✅ |
| `/administrator` | Administrator | ✅ |

### 1.3 渠道页（Channels）

| 路径 | 页面 | /zh/ 版 |
|------|------|---------|
| `/channels` | 渠道总览 | ✅ |
| `/channels/discord` | Discord | ✅ |
| `/channels/telegram` | Telegram | ✅ |
| `/channels/feishu` | Feishu / Lark | ✅ |
| `/channels/website` | Website | ✅ |
| `/channels/slack` | Slack | ✅ |
| `/channels/email` | Email | ✅ |
| `/channels/whatsapp` | WhatsApp | ✅ |

### 1.4 功能子页（Features）

| 路径 | 页面 | /zh/ 版 |
|------|------|---------|
| `/features/knowledge` | 知识引擎 | ✅ |
| `/features/customer-profile` | 客户画像 | ✅ |
| `/features/tasks` | 任务交接 | ✅ |
| `/features/data-analysis` | 数据分析 | ✅ |
| `/features/automation` | 自动化 | ✅ |

### 1.5 用例（Use Cases）

| 路径 | 页面 | /zh/ 版 |
|------|------|---------|
| `/use-cases` | 用例总览 | ✅ |
| `/use-cases/admin-governance` | Administrator · AI Team Governance | ✅ |
| `/use-cases/operations-analytics` | Data Analysis · Operations Insights | ✅ |
| `/use-cases/ai-sales-assistant` | Sales Assistant · Inbound Qualification | ✅ |
| `/use-cases/ai-spam-defense` | Moderator · AI Spam Defense | ✅ |

### 1.6 客户案例（Case Studies）

| 路径 | 页面 | /zh/ 版 |
|------|------|---------|
| `/case-studies` | 客户故事列表 | ✅ |
| `/case-studies/utell` | Utell · AI Tool | ✅ |
| `/case-studies/museon` | Museon · KOL Operations | ✅ |
| `/case-studies/jarsy` | Jarsy · Financial Product | ✅ |

### 1.7 Discover

| 路径 | 页面 | /zh/ 版 |
|------|------|---------|
| `/discover/social-content-community` | Social Content Community | ✅ |
| `/discover/automate-refund-email` | Automate Refund Email | ✅ |
| `/discover/smart-welcome-guide` | Smart Welcome Guide | ✅ |

### 1.8 文档（Docs）

| 路径 | 页面 | /zh/ 版 | 备注 |
|------|------|---------|------|
| `/docs` | 文档首页 | ✅ | |
| `/docs/ai-teammates` | AI 队友配置 | ✅ | |
| `/docs/channels` | 渠道接入总览 | ✅ | |
| `/docs/channels/discord` | Discord 接入 | ✅ | ⚠️ 实站 200，有 hreflang，**未收录 sitemap** |
| `/docs/channels/email` | Email 接入 | ✅ | |
| `/docs/channels/feishu` | Feishu 接入 | ✅ | |
| `/docs/channels/slack` | Slack 接入 | ✅ | |
| `/docs/channels/telegram` | Telegram 接入 | ✅ | |
| `/docs/channels/website` | Website Widget | ✅ | |
| `/docs/customer-profile` | 客户画像 | ✅ | |
| `/docs/faq` | 常见问题 | ✅ | |
| `/docs/knowledge-base` | 知识库 | ✅ | |
| `/docs/reply-rules` | 回复规则 | ✅ | |
| `/docs/self-learning` | 自学习 | ✅ | |
| `/docs/tasks-and-handoff` | 任务与交接 | ✅ | |

**404**：`/docs/channels/whatsapp`（无此页）

### 1.9 Blog 文章（38 篇）

| 路径 | 标题 |
|------|------|
| `/blog/human-in-the-loop-ai` | Human in the Loop AI: A Control Model You Can Audit |
| `/blog/discord-ticket-bot` | Best Discord Ticket Bots: Ticket Tool, Tickets.bot & Tickety |
| `/blog/discord-poll-bot` | Discord Poll Bot: When Native Polls Are Enough |
| `/blog/discord-security-bot` | Discord Security Bot Setup for Servers That Get Attacked |
| `/blog/discord-server-rules` | Discord Server Rules: Templates and the Enforcement Gap |
| `/blog/how-to-build-an-online-community` | How to Build an Online Community Past the First 100 Members |
| `/blog/discord-verification-bot` | Best Discord Verification Bots: Captcha.bot vs Security Bot |
| `/blog/discord-welcome-bot` | Discord Welcome Bot Setup: Onboarding, Server Guide & Follow-Up |
| `/blog/how-to-automate-discord-moderation` | AutoMod Discord: How to Automate Your Server's Moderation |
| `/blog/discord-moderation-bot` | Discord Moderation Bots and the Limits of Rules |
| `/blog/ai-personal-assistant` | AI Personal Assistant: What It Does and Where It Stops |
| `/blog/ai-virtual-assistant` | AI Virtual Assistant: Which of the Three Kinds Do You Need? |
| `/blog/agentic-ai-workforce` | Agentic AI Workforce: A Definition You Can Act On |
| `/blog/automate-email-responses` | Automate Email Responses So They Actually Get Answered |
| `/blog/automate-repetitive-tasks` | Automate Repetitive Tasks Role by Role |
| `/blog/how-to-automate-my-business` | How to Automate My Business One Job at a Time |
| `/blog/ai-chatbot-vs-ai-agent` | AI Chatbot vs AI Agent: The Real Difference |
| `/blog/ai-workforce` | AI Workforce: What It Is, and How to Build One |
| `/blog/how-to-onboard-community-members` | How to Onboard New Community Members Who Stay |
| `/blog/how-to-reduce-support-tickets` | How to Reduce Support Tickets (Without Hiding Contact) |
| `/blog/automate-customer-onboarding` | Automate Customer Onboarding with an AI Employee |
| `/blog/outsource-back-office-operations` | Outsource Back Office Operations, or Hire an AI Employee? |
| `/blog/what-is-a-digital-employee` | The Digital Employee, Explained: AI Worker, Not a DEX Platform |
| `/blog/ai-assistant-for-business` | AI Assistant for Business — or an AI Employee? |
| `/blog/what-is-an-ai-analyst` | The AI Analyst, Explained: A Role You Can Hire, Not Just a Tool |
| `/blog/ai-paralegal` | What an AI Paralegal Does — and What Stays With Lawyers |
| `/blog/ai-customer-support-agent-vs-chatbot` | AI Customer Support Agent vs Chatbot: Why the Difference Matters |
| `/blog/ai-executive-assistant` | AI Executive Assistant: Full Breakdown of Capabilities and Limits |
| `/blog/what-is-an-ai-coworker` | What Is an AI Coworker? |
| `/blog/pm-middle-layer-repriced` | Product Managers Aren't Disappearing. The Middle Layer Is Being Repriced First. |
| `/blog/abolish-context-switching-not-gui` | Abolish Context Switching, Not the GUI: Why AI Employees Should Live Inside IM |
| `/blog/jagged-frontier-org-design` | The Jagged Technological Frontier: Novices Don't See the Error. Experts Don't Believe They Could Miss It. |
| `/blog/ai-skill-divergence` | From Scattered Skills to Monorepo: One Person Managing Skill Version Control Across 9 Bots |
| `/blog/blackbox-trust` | Defeating Black-Box Fear: How Progressive Delegation Builds Trust in AI Employees |
| `/blog/persona-that-speaks` | Your User Personas Are Complete. But They Can't Talk. |
| `/blog/from-memory-to-intuition` | From Memory to Intuition: Why AI Employees Evolve by Growing Instincts, Not Stacking Knowledge |
| `/blog/ai-employees-arent-for-builders` | AI Employees Aren't for Builders. They're for Everyone — If They're Worthy of the Title. |
| `/blog/openclaw-enterprise-postmortem` | We Wrapped an Enterprise Shell Around OpenClaw. Two Weeks Later, We Stopped. |

**Blog 多语言**：38 篇均有 `/zh/blog/{slug}`；其中 9 篇另有 `/pt-BR/blog/{slug}` 葡萄牙语版。

### 1.10 Knockin 子站（独立产品落地页）

| 路径 | /zh/ 版 |
|------|---------|
| `/knockin` | ✅ `/zh/knockin` |
| `/knockin/features/ai-agent` | ❌ |
| `/knockin/features/knowledge-engine` | ❌ |
| `/knockin/features/ai-contacts` | ❌ |
| `/knockin/templates` | ❌ |
| `/knockin/pricing` | ❌ |
| `/knockin/privacy` | ❌ |
| `/knockin/terms` | ❌ |

Knockin 子站 **未收录 sitemap**。

---

## 2. 网站树状结构

```
luciusai.com/  (根 — 首页)
├── /features                         功能总览
│   ├── /features/knowledge           知识引擎
│   ├── /features/customer-profile    客户画像
│   ├── /features/tasks               任务交接
│   ├── /features/data-analysis       数据分析
│   └── /features/automation          自动化
├── /pricing                          定价
├── /roles                            角色系统总览
│   ├── /customer-support             Customer Support
│   │   ├── /customer-support/community   Community Support
│   │   └── /customer-support/email       Email Support
│   ├── /community-moderation         Moderator
│   └── /administrator                Administrator
├── /channels                         渠道总览
│   ├── /channels/discord
│   ├── /channels/telegram
│   ├── /channels/feishu
│   ├── /channels/website
│   ├── /channels/slack
│   ├── /channels/email
│   └── /channels/whatsapp
├── /use-cases                        用例总览
│   ├── /use-cases/admin-governance
│   ├── /use-cases/operations-analytics
│   ├── /use-cases/ai-sales-assistant
│   └── /use-cases/ai-spam-defense
├── /case-studies                     客户故事
│   ├── /case-studies/utell
│   ├── /case-studies/museon
│   └── /case-studies/jarsy
├── /discover                         Discover
│   ├── /discover/social-content-community
│   ├── /discover/automate-refund-email
│   └── /discover/smart-welcome-guide
├── /blog                             Blog 列表
│   └── /blog/{slug}                  文章 ×38（见 §1.9）
├── /docs                             文档中心
│   ├── /docs/ai-teammates
│   ├── /docs/channels
│   │   ├── /docs/channels/discord    ⚠️ 未进 sitemap
│   │   ├── /docs/channels/email
│   │   ├── /docs/channels/feishu
│   │   ├── /docs/channels/slack
│   │   ├── /docs/channels/telegram
│   │   └── /docs/channels/website
│   ├── /docs/customer-profile
│   ├── /docs/faq
│   ├── /docs/knowledge-base
│   ├── /docs/reply-rules
│   ├── /docs/self-learning
│   └── /docs/tasks-and-handoff
├── /profile                          AI Business Card
├── /privacy                          隐私政策（仅英文）
├── /terms                            服务条款（仅英文）
├── /security/dpa                     数据处理协议（仅英文）
└── /knockin                          Knockin 子站（8 页，见 §1.10）
```

---

## 3. 多语言结构

| 语言 | URL 规则 | 示例 |
|------|---------|------|
| 英文（默认） | 无前缀 | `/pricing` |
| 简体中文 | `/zh` 前缀 | `/zh`、`/zh/pricing`、`/zh/docs` |
| 葡萄牙语 | `/pt-BR` 前缀 | `/pt-BR/blog`（仅 9 篇 blog） |

- 每个页面均配置 `rel="alternate" hreflang="en/zh/x-default"` 交替链接与 canonical，中英文为独立 URL。
- 首页中文版为 `/zh`，其余页面为 `/zh/{path}`。
- **无法语版页面**（`site.js` → `englishOnlyPublicPaths`）：`/privacy`、`/terms`、`/security/dpa`。
- 原「Cookie 切换、URL 不变」方案已废弃，详见 [luciusai-i18n-seo-migration.md](./luciusai-i18n-seo-migration.md)。
- **中文 i18n 质量审计**见 [luciusai-zh-i18n-audit.md](./luciusai-zh-i18n-audit.md)。

---

## 4. 遗留重定向

| 请求路径 | 最终 URL |
|---------|---------|
| `/solutions` | `/use-cases` |
| `/solutions/ai-spam-defense` | `/use-cases/ai-spam-defense` |
| `/resources/use-cases/ai-sales-assistant` | `/use-cases/ai-sales-assistant` |
| `/personal-chatbot` | `/channels/website` |
| `/pages/*.html` | 对应 clean URL（见 site.js `pageRoutes`） |

**404**：`/compare`、`/pages/solutions.html`、`/docs/channels/whatsapp`

---

## 5. 技术架构备注

| 项目 | 说明 |
|------|------|
| 部署 | Railway + Cloudflare |
| 导航/页脚 | JS 注入（`/pages/site.js`） |
| i18n | URL 前缀 + `copy.en` / `copy.zh` 对象 |
| Sitemap | 单文件 urlset，191 URL（含 en/zh/pt-BR），最后更新 2026-08-21 |
| 源码 | **不在本 repo**（e:\clients 仅含文档与 blog 写作工具） |

---

## 6. 统计摘要

| 类别 | 英文页数 | 有 /zh/ 版 |
|------|---------|-----------|
| 主站（不含 blog 文章） | 54 | 51 / 54（3 页仅英文） |
| Blog 文章 | 38 | 38 / 38 |
| Knockin 子站 | 8 | 1 / 8 |
| **合计** | **92 sitemap EN URL** + 1 遗漏 | **89 主站页有 zh** |

---

## 7. 与 2026-08-13 版差异

| 旧文档 | 当前实站 |
|--------|---------|
| `/solutions` 为主 URL | 已重定向至 `/use-cases` |
| `/resources/use-cases/ai-sales-assistant` | 重定向至 `/use-cases/ai-sales-assistant` |
| docs 子项无独立 URL | 已有 14 个 `/docs/*` 独立页 |
| 无 `/profile` | 新增 AI Business Card 页 |
| 无 Knockin | 新增 `/knockin/*` 子站（8 页） |
| 无 `/channels` 总览 | sitemap 含 `/channels` |
| 38 篇 blog | 仍为 38 篇 ✅ |
| 无 pt-BR | 9 篇 blog 有葡萄牙语版 |

---

*文档更新：2026-09-02 | 来源：[luciusai.com](https://luciusai.com/) sitemap.xml + site.js + 实站验证*

---

## 关联文档

- [luciusai.md](./luciusai.md) — 产品概览与定位
- [luciusai-features.md](./luciusai-features.md) — 功能分析
- [luciusai-keywords.md](./luciusai-keywords.md) — 关键词策略
- [luciusai-competitors.md](./luciusai-competitors.md) — 竞品分析
- [luciusai-use-cases.md](./luciusai-use-cases.md) — 使用场景
- [luciusai-growth-strategy.md](./luciusai-growth-strategy.md) — 增长策略
- [luciusai-personal-chatbot.md](./luciusai-personal-chatbot.md) — Personal Chatbot
- [luciusai-handoff-keywords.md](./luciusai-handoff-keywords.md) — Handoff 关键词专项
- [luciusai-capabilities.md](./luciusai-capabilities.md) — 能力库
- [luciusai-i18n-seo-migration.md](./luciusai-i18n-seo-migration.md) — i18n SEO 迁移
- [luciusai-zh-i18n-audit.md](./luciusai-zh-i18n-audit.md) — 中文页面 i18n 审计
- [luciusai-meta-optimization-plan.md](./luciusai-meta-optimization-plan.md) — Meta 优化方案
- [luciusai-breadcrumb-optimization-plan.md](./luciusai-breadcrumb-optimization-plan.md) — 面包屑优化方案
- [README.md](./README.md) — 文件索引
