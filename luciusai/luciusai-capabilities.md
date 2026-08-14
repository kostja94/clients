# Lucius Capabilities — 能力库

> 从各产品详情页 Why / What It Does 与引擎能力页抽取、去重后的**能力清单**。按能力本体组织，不绑定具体页面；生成文案时按主题挑选相关条目，可将「文案钩子」改写为页面标题。  
> **关联**：[luciusai-features.md](./luciusai-features.md) | [luciusai-personal-chatbot.md](./luciusai-personal-chatbot.md) | [luciusai-use-cases.md](./luciusai-use-cases.md)  
> **数据来源**：2026-07-28  
> - `lucius-ai.lovable.app` 五页轮播：[Personal Chatbot](https://lucius-ai.lovable.app/personal-chatbot) · [Chatbot](https://lucius-ai.lovable.app/chatbot) · [Chat Widget](https://lucius-ai.lovable.app/chat-widget) · [Slack](https://lucius-ai.lovable.app/chatbot/slack) · [Discord](https://lucius-ai.lovable.app/chatbot/discord)  
> - 新主站引擎页：[知识引擎](https://new-lucius-landing-production.up.railway.app/pages/knowledge.html) · [客户画像](https://new-lucius-landing-production.up.railway.app/pages/customer-profile.html) · [任务与交接](https://new-lucius-landing-production.up.railway.app/pages/tasks.html) · [数据分析](https://new-lucius-landing-production.up.railway.app/pages/data-analysis.html) · [自动化](https://new-lucius-landing-production.up.railway.app/pages/automation.html) · [角色](https://new-lucius-landing-production.up.railway.app/pages/roles.html)  
> **用法**：优先用「能力名」理解与组合；「文案钩子」仅供标题灵感；可变数字与合规主张见文末「可核验主张」。  
> **范围**：只收录系统能力；定价/Credit、角色营销文案、案例如有独立文档承接，不写入本库。

**Last updated**: 2026-07-28

---

## 字段说明

| 列 | 含义 |
|----|------|
| ID | 稳定引用键，文案/配置中引用此 ID |
| 能力名 | 中性动词短语：系统**能做什么** |
| 说明 | 能力边界与行为，不含营销口号 |
| 文案钩子 | 可选标题灵感；可改写，勿与能力名混用 |

近义条目勿在同一 Why / 能力轮播同时选用，见附录「忌同屏近义」。

---

## A · 知识接入、对账与学习

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-knowledge-product | 产品知识库接入 | 对接网站/帮助中心、文档站、PDF、Notion、历史对话与工单等并索引；支持在工作会话中直接告知「关于 X 的答案是 Y」即时生效。仅使用客户提供的知识源作答，无依据时走交接，不联网填空。 | Trained on Your Knowledge |
| cap-knowledge-personal | 个人语境包接入 | 接入简历、路演材料、个人网站、社交归档、访谈/播客稿，以及 Claude/ChatGPT memory 导出等，用于「代表本人」作答。 | Trained on the Whole You, Not Just Your FAQ |
| cap-knowledge-cite | 回答附带源引用 | 每条回复可回链到具体文档/条款位置，而非无出处意见。 | Answers With Sourced Context |
| cap-knowledge-reconcile | 知识冲突对账与处置 | 新资料入库时比对已有条目，发现直接冲突与口径不一致，并附双方原文、来源与时间。可按知识类别配置处置：采用较新并标过期、停答并转人、或整理成任务请人裁决；确认前不永久删除，可回溯。 | Knowledge That Reconciles Itself |
| cap-knowledge-learn-loop | 盲区检测与自学习回流 | 答后检查知识是否覆盖该问，未覆盖记入盲区清单；人工处理交接任务后，从处理过程提取知识回填，减少同类问题再次交接。 | Learns From Every Handoff |

---

## B · 应答与对话质量

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-reply-always-on | 全天候即时应答 | 跨时区、非工作时间持续应答，避免排队等待人工坐席。 | 24/7 Support |
| cap-reply-fast | 秒级首响 | 在已部署渠道上提供快速首次回复，支撑高峰流量。 | Instant AI Replies |
| cap-reply-brand-voice | 品牌/本人语调对齐 | 按站点品牌语气或个人写作风格生成回复，避免通用机器人腔。 | In Your Voice |
| cap-reply-multilingual | 多语言原生回复 | 按访客消息语言自动检测并回复，无需为每语种维护独立话术流。 | 50+ Languages |

---

## C · 触达表面（界面形态）

网站角标 Widget 与独立托管的 Personal Chatbot（Knockin'）属不同表面，共用同一引擎时可对照选用。Knockin' 条目来自 lovable 产品页；新主站未主推时仍可按此库选用。

### C1 · Chat Widget（嵌入站点）

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-widget-one-line | 单行脚本嵌入 | 在页面插入一段脚本即可出现角标聊天窗，无需单独构建或插件栈。 | One-Line Install |
| cap-widget-theme | 像素级品牌主题 | 控制强调色、启动器、头像、问候语、快捷回复与圆角等，仪表盘改完即全站生效。 | On-Brand, to the Pixel |
| cap-widget-any-stack | 多建站栈通用 | 同一片段可用于常见 CMS/建站工具与自建站；响应式适配移动与桌面。 | Works on Any Website |
| cap-widget-triggers | 智能触发规则 | 按停留时长、退出意图、URL、来源、地区等显示/隐藏或更换问候；支持问候与样式 A/B。 | Smart Triggers |

### C2 · Personal Chatbot / Knockin'（独立托管页）

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-knockin-hosted-url | 托管个人对话 URL | 开箱提供 `knockin…/@handle` 类可分享地址，托管/证书由平台处理，无需自建站。 | Knockin' Ships at Its Own URL, in Seconds |
| cap-knockin-identity | 具名个人身份页头 | 页头展示姓名、照片、头衔与外链，对话主体明确为「这个人」，而非匿名站点客服。 | A Personal Chatbot with Your Name on It |
| cap-knockin-fullpage | 全页对话布局 | 桌面分栏 / 移动全高聊天，非整页角标气泡；适合较长会话与更高意图入口。 | A Full-Page Conversation, in Your Voice |
| cap-knockin-share-everywhere | 一链多触点分发 | 同一 URL 可用于邮件签名、社交 bio、会议背景、名片二维码、DM 粘贴等入口。 | One Knockin' Link That Goes Everywhere |
| cap-knockin-seo | 可索引个人页 | 自动生成标题、描述与 Open Graph 等，使个人对话页可被搜索引擎收录。 | The First Google Result About You |

---

## D · 协作与社区渠道

渠道特有交互写在此；「知识、画像、工单、人工交接」等横切能力见 A / E / F / G，勿在渠道页重复堆砌同义条。多 IM 接入清单见 `cap-surface-one-engine`。

### D1 · 通用协作能力

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-channel-mention-answer | 频道内提及应答 | 在已邀请的频道/论坛/私信中经 @mention 或斜杠命令提问，线程内回复并引用知识源。 | Answers @mentions With Sourced Context |
| cap-channel-thread-summary | 线程/会议摘要 | 对长线程、论坛帖、Huddle 等生成决策、负责人与下一步摘要，可置顶或一键 TL;DR。 | Summaries For Threads, Huddles & Channels |
| cap-channel-dm-copilot | 成员私信副驾 | 每人可有私密 DM 副驾（起草回复、查政策/文档、会前准备等），个人记忆仅本人可见。与客户画像（G）不同：此处是**团队成员**私密副驾。 | DM Copilot For Every Teammate |

### D2 · Slack 特有

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-slack-connect-support | Slack Connect 客户支持 | 在共享 Connect 频道中应答客户问题、打标签，并在需要时带全文交接给 CSM。 | Slack Connect Customer Support |

### D3 · Discord / 社区审核

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-discord-forum-aware | Forum / Thread 结构感知 | 适配 Forum 帖顶摘要、普通 Thread TL;DR，以及 Stage 结束后的转写与决策整理等。 | Forum Channels & Thread Summaries |
| cap-discord-moderation | 社区审核与分档处置 | 识别广告、垃圾、诈骗模式、NSFW/跑题等；证据充分时可自主隐藏/限制，存疑则进复核队列并附判断理由与成员历史，由人决定。亦可答重复 FAQ、合并重复帖。 | Community Moderation Copilot |

---

## E · 业务动作与交接

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-action-triage-route | 会话分流与路由 | 自动分类、定优先级与指派，并回写至常见客服/CRM/工单系统。 | Ticket Triage & Routing |
| cap-action-ticket-sync | 工单创建与双向状态同步 | 从对话一键建 Jira/Linear/Zendesk 等工单并附线程；状态可同步回原频道。亦可整理为平台内任务/事件供团队处理。 | Tickets & Actions In Your Stack |
| cap-action-human-handoff | 边界触发与结构化交接 | 在证据不足、超出权限（退款/权限变更/删数等）、话题敏感、或用户明确要人工时停止自动回复；交接任务含问题摘要、账号/订单等已核对信息、附件、完整对话、初步判断与建议操作，并可附品牌语气草稿。边界规则由配置定义，非模型临场偏好。 | Human Handoff |
| cap-action-lead-book | 线索捕获与预约交接 | 在个人页/站点对话中完成提问、资料发送、预约或线索落入同一仪表盘/CRM；可识别合作/销售等高意向并通知负责人。 | Book, Send, Handoff |
| cap-action-rule-replay | 规则历史回放试跑 | 规则变更可对历史消息回放预判处置结果，确认后再启用上线。 | Test Rules Before They Go Live |

---

## F · 横切：权限、分析、自动化与扩展

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-trust-channel-acl | 渠道与角色权限边界 | 按 Slack 可见范围 / Discord 角色等继承渠道权限；未邀请频道与私密内容默认不可见。AI 角色可限定职责范围、可读知识、可调用工具与升级规则，运行时不可越权（如仅查数/发消息则不可退款）。 | Enterprise-Grade Permissions & Security |
| cap-trust-compliance | 企业合规与动作留痕 | SOC 2、GDPR、可选区域数据驻留、SSO、审计日志等（以实际开通项为准）。动作可追溯：触发者、依据知识、命中规则与时间可按成员/时间回溯。 | SOC 2 · GDPR · Audit Log |
| cap-analytics-ops | 运营分析与自然语言问数 | 跟踪解决率/分流、升级、CSAT、高频失败意图与知识缺口，支撑周报与文档修补。亦支持在对话中用自然语言提问社区数据：受控只读查询、工作区隔离、敏感字段不可读出，结果以结论与图表返回。 | Analytics That Matter |
| cap-automation-schedule | 定时触发已配置任务 | 按计划拉起已定义 Flow（如日报/周报、事件催办、知识盲区清单、链路自检、沉默用户唤醒、定时公告等）；「做什么」在 Flow，「何时」在定时，全局 Policy 约束权限；触发与运行状态可留档、失败可告警。 | Runs On Schedule |
| cap-surface-one-engine | 同一引擎多表面扩展 | Widget、Knockin'、Discord、Slack、Telegram、Feishu、Email、WhatsApp 等共用同一 AI 引擎与知识（具体开通以产品为准）；可从个人页或单一渠道长成多角色、多表面部署。 | Same Engine, Everywhere |

---

## G · 客户画像

引擎横切维度：与「成员私信副驾」记忆不同，此处是**面向客户/用户**的跨会话画像，影响答法与是否升级。

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-profile-context | 客户画像记忆与应答适配 | 记住用户是谁（账号/公司/方案/渠道等）、既往交互与未闭环问题、所处阶段（试用/活跃/临近续费/沉默等）及沟通偏好；据此调节答案深浅、是否提前人工、以及定价/部署等意向信号的串联判断。画像仅来自本工作区互动与客户系统数据；条目可溯源，支持导出/删除；支付信息、证件、密码等敏感内容默认不入库。 | Remembers Who Is Asking |

---

## 附录 A · 选能力示例

展示「按页面主题从库中挑选」；其他页面不必照搬。每页建议 5–6 条，优先选与该表面或引擎主题差异相关的条目。

### 示例 1 · Personal Chatbot / Knockin'

| 选用 ID | 能力名 |
|---------|--------|
| cap-knockin-hosted-url | 托管个人对话 URL |
| cap-knockin-identity | 具名个人身份页头 |
| cap-knockin-fullpage | 全页对话布局 |
| cap-knockin-share-everywhere | 一链多触点分发 |
| cap-knockin-seo | 可索引个人页 |
| cap-knowledge-personal | 个人语境包接入 |

### 示例 2 · Chatbot / 引擎总览（多渠道客服）

| 选用 ID | 能力名 |
|---------|--------|
| cap-knowledge-reconcile | 知识冲突对账与处置 |
| cap-profile-context | 客户画像记忆与应答适配 |
| cap-action-human-handoff | 边界触发与结构化交接 |
| cap-knowledge-learn-loop | 盲区检测与自学习回流 |
| cap-reply-always-on | 全天候即时应答 |
| cap-surface-one-engine | 同一引擎多表面扩展 |

### 示例 3 · Chat Widget

| 选用 ID | 能力名 |
|---------|--------|
| cap-widget-one-line | 单行脚本嵌入 |
| cap-widget-theme | 像素级品牌主题 |
| cap-widget-any-stack | 多建站栈通用 |
| cap-reply-fast | 秒级首响 |
| cap-widget-triggers | 智能触发规则 |
| cap-action-human-handoff | 边界触发与结构化交接 |

### 示例 4 · Slack

| 选用 ID | 能力名 |
|---------|--------|
| cap-channel-mention-answer | 频道内提及应答 |
| cap-channel-thread-summary | 线程/会议摘要 |
| cap-channel-dm-copilot | 成员私信副驾 |
| cap-slack-connect-support | Slack Connect 客户支持 |
| cap-action-ticket-sync | 工单创建与双向状态同步 |
| cap-trust-channel-acl | 渠道与角色权限边界 |

### 示例 5 · Discord / 社区

| 选用 ID | 能力名 |
|---------|--------|
| cap-channel-mention-answer | 频道内提及应答 |
| cap-discord-forum-aware | Forum / Thread 结构感知 |
| cap-discord-moderation | 社区审核与分档处置 |
| cap-action-ticket-sync | 工单创建与双向状态同步 |
| cap-trust-channel-acl | 渠道与角色权限边界 |
| cap-automation-schedule | 定时触发已配置任务 |

### 示例 6 · 知识引擎页

| 选用 ID | 能力名 |
|---------|--------|
| cap-knowledge-product | 产品知识库接入 |
| cap-knowledge-reconcile | 知识冲突对账与处置 |
| cap-knowledge-cite | 回答附带源引用 |
| cap-knowledge-learn-loop | 盲区检测与自学习回流 |
| cap-action-human-handoff | 边界触发与结构化交接 |

---

## 附录 B · 忌同屏近义

| 组 | 近义 ID | 建议 |
|----|---------|------|
| 知识训练对象 | `cap-knowledge-product` ↔ `cap-knowledge-personal` | 公司客服/Widget 用前者；Knockin' 用后者；总览页可各一条但文案写清对象 |
| 接入 vs 对账 | `cap-knowledge-product` ↔ `cap-knowledge-reconcile` | 可同页：一条写接入范围，一条写冲突发现与处置 |
| 引用 vs 知识接入 | `cap-knowledge-product` ↔ `cap-knowledge-cite` | 可同页：一条写接入范围，一条写引用行为 |
| 盲区回流 vs 对账 | `cap-knowledge-reconcile` ↔ `cap-knowledge-learn-loop` | 可同页：一条写冲突处置，一条写盲区与人工回流 |
| 响应速度叙事 | `cap-reply-always-on` ↔ `cap-reply-fast` | 「覆盖/不排队」用前者；「首响很快」用后者，勿堆两条口号 |
| Widget 安装 vs 任意栈 | `cap-widget-one-line` ↔ `cap-widget-any-stack` | 强调「60 秒上线」用前者；强调「Shopify/Webflow/…」用后者 |
| Knockin URL vs 无需建站 | `cap-knockin-hosted-url` 已含「无需自建站」 | 勿再单开「No Website Needed」类重复条；用钩子改写即可 |
| Knockin 身份 vs 全页 | `cap-knockin-identity` ↔ `cap-knockin-fullpage` | 身份名片感用前者；对比角标气泡用后者 |
| 摘要能力 | `cap-channel-thread-summary` ↔ `cap-discord-forum-aware` | Slack 页用前者；Discord 页用后者（或前者作通用 + 后者作 Forum 特写，勿双标题同义） |
| 成员记忆 vs 客户画像 | `cap-channel-dm-copilot` ↔ `cap-profile-context` | 协作/内部页用前者；客服/引擎页用后者，勿同屏当同一「记忆」讲 |
| 人工交接 | `cap-action-human-handoff` | 已含边界与结构化；渠道页若已写 escalate，勿再换标题重复；勿再单开「结构化交接」同义条 |
| 工单动作 | `cap-action-triage-route` ↔ `cap-action-ticket-sync` | 客服总览偏分流路由；Slack/Discord 偏「从线程建单同步」 |
| 权限 vs 合规 | `cap-trust-channel-acl` ↔ `cap-trust-compliance` | 渠道/角色页突出权限边界；合规数字放附录 C 或单独一条 |
| 分析看板 vs 问数 | `cap-analytics-ops` 已含 NL 问数 | 同页勿再拆「看板」「问数」两条口号；钩子改写即可突出其一 |
| 多表面 vs 渠道特写 | `cap-surface-one-engine` ↔ D 区条目 | 总览用前者；Slack/Discord 详情页用 D 区特写，勿双标题同义 |

---

## 附录 C · 可核验主张（易变，写文案前请核对产品）

以下数字与合规表述**不写入能力正文**；对外使用前以官网/合规文档为准。定价与 Credit 规则见独立定价文档，不以本附录为准。

| 主题 | 历史文案中出现过的主张 | 备注 |
|------|------------------------|------|
| 首响时间 | Under 30 seconds / 60 秒装上 Widget | 作体验量级，勿写成 SLA 除非有合同条款 |
| 语言数 | 50+ languages | 易变；写前核对实际支持列表 |
| 分流效果 | ~70% L1 deflection 等 | 案例/场景数字，非通用能力定义 |
| 免费额度 / 套餐价 | Free forever；亦见 Starter/Growth/Scale 等 | 以当前定价页为准，多源可能不一致 |
| 安全合规 | SOC 2 Type II、GDPR、EU residency、SSO | 以实际认证范围与套餐为准 |
| Knockin 域名 | `knockin.luciusai.com/@handle` | 域名/产品名可能调整，钩子可改写 |
| 集成清单 | Zendesk、Intercom、HubSpot、Linear、Jira… | 集成表易增删，正文写「常见客服/研发工具」即可 |
| 渠道开通 | Discord / Slack / Telegram / Feishu / Email / WhatsApp 等 | 首页展示与 FAQ「计划支持」可能不一致；写前核对 |

---

## 附录 D · 来源页 → 能力 ID 映射（抽取对照）

便于回溯原文；生成新页时不必按此表原样复用。

### D1 · lovable 产品轮播

| 来源页 | 轮播原标题（钩子） | 映射 ID |
|--------|-------------------|---------|
| personal-chatbot | Knockin' Ships at Its Own URL, in Seconds | `cap-knockin-hosted-url` |
| personal-chatbot | A Personal Chatbot with Your Name on It | `cap-knockin-identity` |
| personal-chatbot | A Full-Page Conversation, in Your Voice | `cap-knockin-fullpage` |
| personal-chatbot | One Knockin' Link That Goes Everywhere | `cap-knockin-share-everywhere` |
| personal-chatbot | The First Google Result About You | `cap-knockin-seo` |
| personal-chatbot | Trained on the Whole You, Not Just Your FAQ | `cap-knowledge-personal` |
| chatbot | 24/7 Support | `cap-reply-always-on` |
| chatbot | Trained on Your Knowledge | `cap-knowledge-product` |
| chatbot | 50+ Languages | `cap-reply-multilingual` |
| chatbot | Ticket Triage & Routing | `cap-action-triage-route` |
| chatbot | Human Handoff | `cap-action-human-handoff` |
| chatbot | Analytics That Matter | `cap-analytics-ops` |
| chat-widget | One-Line Install | `cap-widget-one-line` |
| chat-widget | On-Brand, to the Pixel | `cap-widget-theme` |
| chat-widget | Works on Any Website | `cap-widget-any-stack` |
| chat-widget | Instant AI Replies | `cap-reply-fast` (+ 知识/多语言见 B/A) |
| chat-widget | Smart Triggers | `cap-widget-triggers` |
| chat-widget | Human Handoff | `cap-action-human-handoff` |
| chatbot/slack | Answers @mentions With Sourced Context | `cap-channel-mention-answer` + `cap-knowledge-cite` |
| chatbot/slack | Summaries For Threads, Huddles & Channels | `cap-channel-thread-summary` |
| chatbot/slack | DM Copilot For Every Teammate | `cap-channel-dm-copilot` |
| chatbot/slack | Slack Connect Customer Support | `cap-slack-connect-support` |
| chatbot/slack | Tickets & Actions In Your Stack | `cap-action-ticket-sync` |
| chatbot/slack | Enterprise-Grade Permissions & Security | `cap-trust-channel-acl` + `cap-trust-compliance` |
| chatbot/discord | Answers @mentions & /lucius in Any Channel | `cap-channel-mention-answer` |
| chatbot/discord | Forum Channels & Thread Summaries | `cap-discord-forum-aware` |
| chatbot/discord | DM Copilot For Every Member | `cap-channel-dm-copilot` |
| chatbot/discord | Community Moderation Copilot | `cap-discord-moderation` |
| chatbot/discord | Tickets & Actions In Your Stack | `cap-action-ticket-sync` |
| chatbot/discord | Role-Aware Permissions & Server Safety | `cap-trust-channel-acl` |

### D2 · 新主站引擎页（合并映射）

| 来源页 | 主题要点 | 映射 ID |
|--------|----------|---------|
| pages/knowledge.html | 多源接入、仅客户知识、冲突对账与处置、盲区与回流 | `cap-knowledge-product` · `cap-knowledge-reconcile` · `cap-knowledge-learn-loop` |
| pages/customer-profile.html | 画像记忆、应答适配、隐私默认 | `cap-profile-context` |
| pages/tasks.html | 边界停答、结构化交接、分档处置、规则试跑、动作留痕 | `cap-action-human-handoff` · `cap-discord-moderation` · `cap-action-rule-replay` · `cap-trust-compliance` |
| pages/data-analysis.html | NL 问数、只读与审计 | `cap-analytics-ops` |
| pages/automation.html | 定时 Flow、失败可见 | `cap-automation-schedule` |
| pages/roles.html | 职责/知识/工具/升级边界 | `cap-trust-channel-acl` |
| 首页 / platforms | 多渠道同一引擎 | `cap-surface-one-engine` |
