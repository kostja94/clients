# Lucius AI 全站 Meta Title & Description 优化方案

> **本文职责**：梳理 luciusai.com 全站 meta 现状问题、评估重要性、给出符合 SEO 最佳实践的优化方向与页面级目标文案。
> **审计基线**：2026-08-13 实站抓取（38 个英文页面 + 4 个中文页面 + Blog 文章样本），逐 URL 验证
> **参考方案**：目标 meta 库（用户提供，收录于 §6，涵盖规划中页面结构）
> **创建日期**：2026-08-13
> **状态**：待评审

---

## 1. 方案概述

### 1.1 目标

全站 title 与 description 达到以下标准：

- **Title**：≤60 字符（Google SERP 不截断）、主关键词前置、每页唯一、品牌格式全站统一
- **Description**：140–160 字符、一句话价值主张 + 2–3 个具体卖点 + CTA、每页唯一
- **术语**：全站统一品牌叙事，消除 Agents / Teammate 混用
- **中文版**：全中文化（含 JSON-LD / OG / Twitter），无英中混排
- **结构覆盖**：补齐高意图搜索页面（chatbot / chat-widget / sales / glossary / comparison / personal chatbot）

### 1.2 审计范围

| 组 | 页面数 | 说明 |
|----|--------|------|
| 核心页 | 10 | `/` `/features` `/pricing` `/solutions` `/discover` `/blog` `/docs` 及法律页 |
| 角色页 | 6 | `/roles` `/customer-support*` `/community-moderation` `/administrator` |
| 渠道页 | 7 | `/channels/*` |
| 功能页 | 5 | `/features/*` |
| 用例/案例 | 7 | `/use-cases/*` `/case-studies/*` `/solutions/ai-spam-defense` |
| Discover | 4 | `/discover/*` |
| Blog | 38 | 全部文章 |
| 中文版 | 4+ | `/zh` `/zh/pricing` `/zh/features` `/zh/solutions` `/zh/docs` |

---

## 2. 问题诊断

### 2.1 P0 — 必须立即修复（影响品牌与 CTR）

| # | 问题 | 证据 | 影响 |
|---|------|------|------|
| P0-1 | **品牌术语混用：Agents vs Teammate** | `/roles` Title = "Lucius **Agents** — Lucius AI"，但 H1 是 "Give every repeatable job a clear AI **teammate**"，同一页 3 个词；`/roles` Description 同一句里 "Lucius **Agents** ... the AI **teammate** your team needs"；`/discover` Title/Desc/H1 全用 "Lucius **Agents**" | 品牌定位是 **AI teammates**（首页 Hero），"Agents" 稀释品牌词，SERP 展示不一致，影响品牌搜索与认知 |
| P0-2 | **Blog 标题严重超长** | `/blog/abolish-context-switching-not-gui` ≈92 字符、`/blog/ai-employees-arent-for-builders` ≈102 字符、多篇 >70 字符 | 超过 Google ~60 字符/580px 截断线，标题被截断，**品牌词 "Lucius AI" 被裁掉**，CTR 受损 |
| P0-3 | **首页 title 格式不统一** | `/` = "Lucius — AI teammates that get things done"（品牌无 "AI" 后缀）；其余 37 页均为 "X — Lucius AI" | 品牌词不一致；首页 title 与 H1（"Hire AI teammates that get things done"）几乎重复，浪费关键词位 |

### 2.2 P1 — 重要（影响排名与内容质量）

| # | 问题 | 证据 | 影响 |
|---|------|------|------|
| P1-1 | **渠道页 title 只有平台名，无关键词** | `/channels/discord` = "Discord — Lucius AI"，7 个渠道页全部如此 | 白白浪费高流量词（"Discord AI bot"、"AI chatbot for Slack" 等），页面与搜索意图不匹配，排名上限低 |
| P1-2 | **描述模板化、无 CTA、缺差异化** | Discord 与 Telegram 描述只差平台名；全部描述没有行动号召词（book/demo/try/start） | 描述虽不直接排名，但影响 CTR；雷同描述有重复内容嫌疑，信息传达弱 |
| P1-3 | **中文页本地化不彻底** | `/zh/solutions` 描述含英文 "**Customer Support**" 混排；`/zh` 首页 `og:image:alt` 仍为英文；`/zh/solutions` Breadcrumb JSON-LD 的 name 仍是英文 "Home / Case Studies and Use Cases" | 中文用户 SERP 展示劣质；本地化不完整降低中文站专业度与转化 |
| P1-4 | **`/solutions` 页面 title 残留旧名** | URL 已改为 `/solutions`（canonical 指向），title 仍是 "Case studies and use cases — Lucius AI" | URL 与 title/导航不一致，可能混淆用户与搜索引擎 |

### 2.3 P2 — 机会（结构性提升）

| # | 问题 | 影响 |
|---|------|------|
| P2-1 | **缺失高意图页面**：无 `/chatbot` `/chat-widget` `/customer-service` `/sales` `/glossary` `/comparison/*` `/personal-chatbot` | 错失 "AI chatbot for Discord/Slack/WhatsApp"、"AI sales assistant"、"claude tag alternative" 等大量商用意图流量 |
| P2-2 | **动态 meta 机制未规范**：Blog 用 `{{postTitle}}` 但无长度约束；个人聊天页（`/knockin/{username}`）meta 未说明模板 | 动态页面 meta 失控会导致截断与重复 |
| P2-3 | **分隔符混用**：参考方案同时出现 `—` 与 `\|` 两种品牌分隔符 | 品牌展示不统一，SERP 中视觉杂乱 |

---

## 3. 重要性评估

| 优先级 | 问题 | SEO 影响面 | 修复成本 | 建议 |
|--------|------|-----------|---------|------|
| P0 | 术语混用 | 品牌词搜索、全站一致性、SERP 信任 | 低（文案替换） | 今日完成 |
| P0 | Blog title 超长 | 38 篇文章的 CTR | 低（模板 + 标题裁剪） | 今日完成 |
| P0 | 首页 title 格式 | 品牌词 + 首页 CTR | 极低 | 今日完成 |
| P1 | 渠道页关键词单薄 | 7 个渠道页排名上限 | 低 | 今日完成 |
| P1 | 描述无 CTA/模板化 | 全站 CTR 与差异化 | 中（逐页撰写） | 今日完成 |
| P1 | 中文页本地化 | 中文 SERP 体验与转化 | 低 | 今日完成 |
| P1 | /solutions 旧名 | 单页一致性 | 极低 | 今日完成 |
| P2 | 缺失意图页面 | 新流量入口 | 高（需建页） | 今日完成 meta 预置，建页另排期 |
| P2 | 动态 meta 机制 | 长期可控性 | 中 | 今日完成规范定稿 |

---

## 4. SEO 最佳实践原则（优化方向）

### 4.1 Title 规则

1. **长度**：≤60 字符（或 ≤580px）；超过必须裁剪，品牌词放在安全区（末尾）
2. **关键词前置**：主关键词放最前（SERP 前 2 词权重与视觉最优先）；品牌放末尾
3. **品牌格式统一**：全站统一 `… — Lucius AI`（em dash）或 `… \| Lucius AI`（竖线），**只选一种**（参考方案两种混用，需统一——建议统一 em dash）
4. **每页唯一**：禁止两页共用同一 title
5. **避免重复 H1**：title 与 H1 避免完全同文，title 承担关键词、H1 承担叙事

### 4.2 Description 规则

1. **长度**：140–160 字符
2. **结构**：价值主张（谁 + 做什么）+ 2–3 个具体卖点 + CTA（如 "Start free" / "Book a demo"）
3. **唯一性**：每页独立撰写，禁止平台名替换式模板
4. **关键词**：自然融入 1–2 个主关键词，不做堆砌
5. **行动号召**：参考方案全部带 CTA，这是当前实站最大差距

### 4.3 品牌与术语策略

- **品牌叙事词统一为 "AI Teammate"**（与首页 Hero 一致）：`/roles`、`/discover`、全站文案不得出现 "Lucius Agents"
- **搜索词使用 "AI Chatbot / AI Agent" 允许**：这是**搜索意图词**而非品牌词——用户搜的是 "AI chatbot for Discord"，页面 title 用 chatbot 覆盖搜索，正文/品牌叙事用 teammate 保持品牌调性。两者并行不冲突
- 参考方案正是这种"**搜索词（chatbot）+ 品牌词（teammate）**"双轨策略，可作为全站范式

### 4.4 动态页面模板

| 页面 | 模板 | 约束 |
|------|------|------|
| Blog 文章 | `{{postTitle}} — Lucius AI` | postTitle 需控制在 ≤50 字符（含空格），超出则裁剪；另在 title 前 60 字符内保证关键词 |
| Glossary | `AI Customer Service Glossary — Lucius` | `{{termCount}}` 动态注入描述 |
| 个人聊天页 | `Chat with {{username}} — Knockin by Lucius` | 按用户名实时生成，需做长度上限与非法字符清洗 |

### 4.5 中文版与 hreflang

- **全中文化**：title、description、og:title、og:description、twitter:title、twitter:description、JSON-LD name/description、Breadcrumb name **七处同步翻译**
- **禁止英中混排**：如 "Customer Support" → "客户支持"
- **hreflang**：en/zh/x-default 三向标注已正确，保持；无语言前缀的旧 Cookie 方案已废弃
- **中文 title 长度**：按 40 字符（约 560px）控制

### 4.6 结构化数据同步

- meta 变更必须同步：`og:title` / `og:description` / `twitter:*` / JSON-LD `name` / `description`
- 审计已发现 JSON-LD 与 OG 存在英文残留（`/zh/solutions`），统一在 meta 更新流程中覆盖

---

## 5. 页面级优化方案（当前实站）

> 约定：全部建议统一品牌分隔符 `— Lucius AI`；长度均 ≤60 字符。

### 5.1 核心页面

| 路径 | 现状 Title | 优化后 Title | 说明 |
|------|-----------|-------------|------|
| `/` | Lucius — AI teammates that get things done | **Lucius AI — The AI Teammate for Your Community** | 品牌词 "Lucius AI" 前置 + 定位词 "AI Teammate" + 人群 "Community"（对应参考方案） |
| `/features` | How Lucius works — Lucius AI | **AI Teammate Features — Knowledge, Memory & Handoff \| Lucius AI** | "How Lucius works" 非搜索词；改为主关键词 + 三核能力 |
| `/pricing` | Pricing — Lucius AI | **Lucius AI Pricing — Pay Only for Results, Start Free \| Lucius AI** | 保留 "Pricing" 前置（品牌页习惯），CTA "Start Free"；注意与定价页实际模型（免费 500 credits + Starter/Growth/Scale）保持一致 |
| `/solutions` | Case studies and use cases — Lucius AI | **AI Teammate Use Cases & Customer Stories \| Lucius AI** | 与 URL `/solutions` 对齐，去掉旧名 |
| `/blog` | Blog — Lucius AI | **Lucius Blog — AI Teammates, Automation & Community Ops** | 注入品类关键词 |
| `/docs` | Documentation — Lucius AI | **Lucius AI Documentation — Roles, Platforms & Handoff** | 加入功能关键词 |
| `/privacy` | Privacy policy — Lucius AI | **Privacy Policy — Lucius AI** | 修正 Title Case（p/p 大写） |
| `/terms` | Terms of service — Lucius AI | **Terms of Service — Lucius AI** | 修正 Title Case |
| `/security/dpa` | Data processing agreement — Lucius AI | **Data Processing Agreement (DPA) — Lucius AI** | 补全缩写关键词 |

### 5.2 角色页

| 路径 | 现状 Title | 优化后 Title | 关键点 |
|------|-----------|-------------|--------|
| `/roles` | Lucius **Agents** — Lucius AI | **AI Teammates for Every Role — Community, Support & Sales \| Lucius AI** | **消除 Agents 术语**（P0-1） |
| `/customer-support` | Customer Support — Lucius AI | **AI Customer Support — Automate 70% of Tickets \| Lucius AI** | 参考 `/customer-service` 方向；"Automate Support at Scale" |
| `/customer-support/community` | Community Operator — Lucius AI | **AI Community Operator — Answer & Escalate In-Channel \| Lucius AI** | 关键词化 |
| `/customer-support/email` | Email Assistant — Lucius AI | **AI Email Assistant — Automate Replies & Handoffs \| Lucius AI** | 关键词化 |
| `/community-moderation` | Moderator — Lucius AI | **AI Community Moderator — Spam Detection & Rule Enforcement** | 关键词化 |
| `/administrator` | Administrator — Lucius AI | **AI Team Administrator — Govern Roles, Permissions & Workflows** | 关键词化 |

### 5.3 渠道页（P1-1 重点）

| 路径 | 现状 Title | 优化后 Title | 对应参考 |
|------|-----------|-------------|---------|
| `/channels/slack` | Slack — Lucius AI | **AI Chatbot for Slack — Answer & Automate In-Channel \| Lucius AI** | 参考 `/chatbot/slack` |
| `/channels/discord` | Discord — Lucius AI | **AI Chatbot for Discord — Community & Support Copilot \| Lucius AI** | 参考 `/chatbot/discord` |
| `/channels/website` | Website — Lucius AI | **AI Chat Widget — Add Live Chat to Any Website \| Lucius AI** | 参考 `/chat-widget` |
| `/channels/whatsapp` | WhatsApp — Lucius AI | **AI Chatbot for WhatsApp — Mobile Customer Support \| Lucius AI** | 参考风格延伸 |
| `/channels/telegram` | Telegram — Lucius AI | **AI Chatbot for Telegram — In-Group Community Support** | 参考风格延伸 |
| `/channels/email` | Email — Lucius AI | **AI Email Bot — Automate Support Replies & Escalations** | 参考风格延伸 |
| `/channels/feishu` | Feishu — Lucius AI | **AI Chatbot for Feishu (Lark) — Answer & Automate \| Lucius AI** | 参考风格延伸 |

> 渠道页描述优化方向：以 `/chatbot/slack` 为范式——"功能（@mention 即可用）+ 场景（渠道特有）+ 卖点（安全/合规/角色感知）+ CTA"，7 页逐页独立撰写，禁止平台名替换模板。

### 5.4 功能页

| 路径 | 现状 Title | 优化后 Title |
|------|-----------|-------------|
| `/features/knowledge` | Knowledge engine — Lucius AI | **Knowledge Engine — AI That Learns & Flags Conflicts \| Lucius AI** |
| `/features/customer-profile` | Customer profile — Lucius AI | **Customer Memory & Profile — Knows Who Is Asking \| Lucius AI** |
| `/features/tasks` | Tasks and handoff — Lucius AI | **Human Handoff & Task Creation — Knows When to Stop** |
| `/features/data-analysis` | Data analysis — Lucius AI | **AI Data Analysis for Communities — Ask in Plain Language** |
| `/features/automation` | Automation — Lucius AI | **AI Automation — Scheduled Reports & Workflows \| Lucius AI** |

### 5.5 用例与客户案例

| 路径 | 现状 Title | 优化后 Title |
|------|-----------|-------------|
| `/use-cases/admin-governance` | AI team governance use case — Lucius AI | **AI Team Governance — Deploy & Govern AI Teammates \| Lucius AI** |
| `/use-cases/operations-analytics` | Operations analytics use case — Lucius AI | **Community Operations Analytics — AI Weekly Reports \| Lucius AI** |
| `/resources/use-cases/ai-sales-assistant` | AI Sales Assistant for Inbound Leads — Lucius AI | **AI Sales Assistant — Qualify Leads & Book Meetings \| Lucius AI** |
| `/solutions/ai-spam-defense` | AI Spam Filter for Discord Communities — Lucius AI | **AI Spam Filter for Discord — Enforce Rules Automatically** |
| `/case-studies/utell` | Utell case study — Lucius AI | **Utell Case Study — Website & Discord AI Support \| Lucius AI** |
| `/case-studies/museon` | Museon case study — Lucius AI | **Museon Case Study — AI for KOL Operations \| Lucius AI** |
| `/case-studies/jarsy` | Jarsy case study — Lucius AI | **Jarsy Case Study — AI Moderation for Finance \| Lucius AI** |

### 5.6 Discover

| 路径 | 现状 Title | 优化后 Title |
|------|-----------|-------------|
| `/discover` | Discover — Lucius AI | **Discover AI Teammate Scenarios & Playbooks \| Lucius AI**（**消除 Agents 术语**） |
| `/discover/social-content-community` | Social content community scenario — Lucius AI | **Turn Social Content into Community Conversations \| Lucius AI** |
| `/discover/automate-refund-email` | Automated refund email handling — Lucius AI | **Automate Refund Emails — AI Review Workflow \| Lucius AI** |
| `/discover/smart-welcome-guide` | Smart welcome guide scenario — Lucius AI | **AI Welcome Guide — Onboard New Members Faster \| Lucius AI** |

### 5.7 Blog

| 项 | 现状 | 优化 |
|----|------|------|
| 模板 | `{{postTitle}} — Lucius AI`（无长度约束） | `{{postTitle}} — Lucius AI` + **postTitle ≤50 字符硬约束** |
| 超长标题 | ≥15 篇 >70 字符 | 逐篇裁剪至 ≤50 字符，品牌词必须保留 |
| 典型案例 | `/blog/abolish-context-switching-not-gui`（92）、`/blog/ai-employees-arent-for-builders`（102）、`/blog/openclaw-enterprise-postmortem`（84）、`/blog/from-memory-to-intuition`、`/blog/jagged-frontier-org-design` | 缩短主标题（可保留 H1 完整，仅 title 裁剪） |

### 5.8 中文版（P1-3 重点）

| 路径 | 现状 Title | 优化后 Title | 处理项 |
|------|-----------|-------------|--------|
| `/zh` | Lucius — 雇佣真正解决问题的 AI 队友 | **Lucius AI — 面向社区的 AI 队友**（或保留现有，但对齐英文 "AI Teammate" 定位） | 术语统一为"AI 队友"，禁用"智能体/Agents" |
| `/zh/pricing` | 价格 — Lucius AI | **Lucius AI 定价 — 免费起步，按产出付费** | 对齐英文定价模型表述 |
| `/zh/features` | Lucius 如何工作 — Lucius AI | **Lucius 功能 — 知识引擎、记忆与交接闭环** | 关键词化 |
| `/zh/solutions` | 案例与使用场景 — Lucius AI | **Lucius 使用场景与客户案例** | **描述删除 "Customer Support" 残留，改"客户支持"** |
| `/zh/docs` | （推断）文档 — Lucius AI | **Lucius 产品文档 — 角色、平台与人工升级** | 关键词化 |

**中文页同步修复**（无论 title 是否变更）：

- `/zh` 首页 `og:image:alt` → 中文
- `/zh/solutions` Breadcrumb JSON-LD `name` → 中文
- 全中文页检查七处同步（title/desc/og/twitter/JSON-LD）

---

## 6. 目标参考库（规划页面 meta 预置）

> 以下为参考方案提供的完整目标 meta，覆盖当前实站尚不存在的**规划页面结构**（`/chatbot*`、`/chat-widget`、`/customer-service`、`/sales`、`/glossary`、`/comparison/*`、`/knockin*`）。若这些页面按计划上线，meta 可直接采用；若仅在现有 URL 上优化，则 §5 已给出对应页面的建议。

| 路径 | Title | Description |
|------|-------|-------------|
| `/` | Lucius AI — The AI Teammate for Your Community | Lucius is one AI teammate across every community channel — answering questions, onboarding members, filtering spam, and handing off real signals to your team. |
| `/chatbot` | AI Chatbot for Slack, Discord, WhatsApp & Email \| Lucius | One AI chatbot across Slack, Discord, WhatsApp, Email and your helpdesk. Trained on your knowledge, replies in 50+ languages, with clean human handoff. |
| `/chatbot/slack` | AI Chatbot for Slack — Answer & Automate In-Channel \| Lucius | @mention Lucius in any Slack channel to get answers from your docs, tickets, and past threads. Private-channel aware, Enterprise Grid ready, SOC 2 Type II. |
| `/chatbot/discord` | AI Chatbot for Discord — Community & Support Copilot \| Lucius | @mention Lucius or /lucius in any Discord channel, forum, or DM to get answers from your docs, threads, and past questions. Role-aware, moderation-ready, SOC 2 Type II. |
| `/chat-widget` | AI Chat Widget — Add Live Chat to Any Website \| Lucius | Add an AI chat widget to your site in 60 seconds. Answer visitors 24/7 in 50+ languages on Shopify, WordPress, Webflow, Framer, and any website — with human handoff. |
| `/personal-chatbot` | Personal AI Chatbot — Introduce Yourself Once \| Lucius | Meet Knockin' — your personal AI chatbot at knockin.luciusai.com/@you. No website needed. Share one link; let visitors chat with you, book meetings, and get answers 24/7. |
| `/customer-service` | AI for Customer Service — Automate Support at Scale \| Lucius | Use AI to resolve 70% of support tickets 24/7 in 50+ languages. Cut cost-per-ticket, lift CSAT, and keep your team for the conversations that matter. |
| `/sales` | AI for Sales — Book More Meetings from Inbound \| Lucius | AI SDR that replies in under 30 seconds, qualifies leads with your criteria, and books meetings on your calendar — 24/7 in 50+ languages. Never lose a lead overnight. |
| `/pricing` | Pricing — Lucius AI Chatbot Plans | Simple, action-based pricing for Lucius AI. Free tier, unlimited seats, and plans that scale with AI actions — not per user. Start free, no credit card. |
| `/glossary` | AI Customer Service Glossary — Lucius | {{termCount}} plain-language definitions of AI customer service and AI agent terms — deflection, RAG, human handoff, tool permissions, chat widget, and more. |
| `/comparison/lucius-vs-claude-tag` | Lucius vs Claude Tag — Multi-Channel AI Teammate | Claude Tag lives only in Slack, for Claude Enterprise seats, for your team. Lucius brings the same @mention AI teammate to Slack, Discord, WhatsApp, Email, your website, and a personal chat page. |
| `/knockin` | Build Your Knockin' — Personal Chatbot in One Link \| Lucius | Drop a link, paste your bio, or upload a file. Knockin' turns it into a personal chatbot people can chat with 24/7. |
| `/blog/{slug}` | {{postTitle}} — Lucius | {{postDescription}}（动态取自文章标题/摘要） |
| `/knockin/{username}` | （动态）Chat with {{username}} — Knockin by Lucius | 按用户名实时生成，未收录集中数据源 |

**参考库使用注意**：

1. **分隔符统一**：参考库混用了 `—` 与 `\|`，落地时全站统一为一种（建议 em dash）
2. **URL 差异**：参考库 `/chatbot/*`、`/customer-service`、`/sales` 与当前实站 `/channels/*`、`/customer-support` 并存——若短期不改 URL，优先在现有 URL 应用 §5 建议，参考库保留为中长期目标
3. **`/pricing` 描述与实站不一致**：参考库描述是 "Free tier, unlimited seats, action-based pricing"，实站是 "免费 500 credits + Starter/Growth/Scale"——落地时**以实站定价为准改写描述**
4. **`/comparison/lucius-vs-claude-tag`** 与 `/blog/04-best-claude-tag-alternatives.md` 同主题，上线时注意 canonical 与互链，避免自相竞争

---

## 7. 今日执行清单

> 所有任务当日完成，按依赖顺序执行。P2-1 的「缺失页面」仅完成 meta 预置（§6 已提供），建页由产品/研发另行排期。

### 7.1 文案批量更新（可直接落地线上）

| # | 任务 | 涉及问题 | 产出 |
|---|------|---------|------|
| 1 | 全站术语统一："Lucius Agents" → "AI Teammate"（/roles、/discover 及站点文案） | P0-1 | 术语替换对照表 + 全站替换 |
| 2 | Blog 标题长度约束：模板 + 38 篇标题裁剪至 ≤50 字符 | P0-2 | 38 篇标题裁剪清单 |
| 3 | 首页 title 改为品牌统一格式（`Lucius AI — The AI Teammate for Your Community`） | P0-3 | 首页 meta 定稿 |
| 4 | `/solutions` title 与 URL 对齐 | P1-4 | 单页 meta 定稿 |
| 5 | 渠道页 title 关键词化（7 页）+ 描述逐页重写 | P1-1 / P1-2 | 7 页 meta 定稿 |
| 6 | 角色页、功能页、用例页 title/description 批量更新 | P1-1 / P1-2 | 批量 meta 定稿表 |
| 7 | 中文页七处本地化修复 + 去除英中混排 | P1-3 | 中文页七处同步清单 |
| 8 | `/pricing` 描述与实际定价模型对齐（免费 500 credits + Starter/Growth/Scale） | — | 定价页 meta 定稿 |
| 9 | 全站分隔符统一（em dash）+ OG/Twitter/JSON-LD 三处同步核查 | P2-3 | 分隔符规范 + 核查清单 |

### 7.2 机制规范定稿

| # | 任务 | 涉及问题 | 产出 |
|---|------|---------|------|
| 10 | 动态 meta 模板规范化（blog / glossary / knockin） | P2-2 | 动态模板约束文档 |
| 11 | 缺失页面 meta 预置交付（/chatbot* /chat-widget /customer-service /sales /glossary /comparison/* /personal-chatbot /knockin） | P2-1 | §6 参考库定稿（建页另排期） |

### 7.3 上线前验证（当日）

- [ ] 每页 title ≤60 字符（中文 ≤40），无截断
- [ ] 每页 description 140–160 字符，含 CTA，全站无重复
- [ ] 全站无 "Agents" 术语残留（品牌叙事处）
- [ ] 中文页七处同步无英文残留
- [ ] hreflang en/zh/x-default 三向正确
- [ ] Google Search Console 重新提交受影响页面（Indexing API / sitemap 更新）

---

## 8. 长期维护规则

- 新页面发布走「title ≤60 / desc 140–160 / 含 CTA / 术语 Teammate」Checklist（可复用 `luciusai-blog-article` skill 的 gates 思路）
- 每月抽查 SERP 展示长度（SERP 截断 → 缩短 title）
- 每季度对比 Search Console 点击率，优先重写低 CTR 高曝光页面描述

---

*方案创建：2026-08-13 | 审计基线：luciusai.com 实站抓取 | 目标参考：用户提供 meta 库 | 落地后请按实站定价与 URL 现状复核 §6 参考库*

---

## 关联文档

- [luciusai.md](./luciusai.md) — 产品概览与定位
- [luciusai-features.md](./luciusai-features.md) — 功能分析
- [luciusai-keywords.md](./luciusai-keywords.md) — 关键词策略
- [luciusai-competitors.md](./luciusai-competitors.md) — 竞品分析
- [luciusai-use-cases.md](./luciusai-use-cases.md) — 使用场景
- [luciusai-growth-strategy.md](./luciusai-growth-strategy.md) — 增长策略
- [luciusai-site-structure.md](./luciusai-site-structure.md) — 网站结构
- [luciusai-personal-chatbot.md](./luciusai-personal-chatbot.md) — Personal Chatbot
- [luciusai-handoff-keywords.md](./luciusai-handoff-keywords.md) — Handoff 关键词专项
- [luciusai-capabilities.md](./luciusai-capabilities.md) — 能力库
- [luciusai-i18n-seo-migration.md](./luciusai-i18n-seo-migration.md) — i18n SEO 迁移
- [README.md](./README.md) — 文件索引
