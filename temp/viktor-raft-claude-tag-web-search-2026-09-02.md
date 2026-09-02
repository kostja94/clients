# 深度搜索报告 — Viktor、Raft、Claude Tag

> **检索基准日**：2026-09-02  
> **时间范围**：2026 年以来（重点 2026-02 至 2026-09）  
> **检索约束**：按 web-deep-search-spec v1.4，**未读取**本地客户文档  
> **Loop 轮次**：6 轮  
> **来源统计**：Tier 0 8 · Tier 1 7 · Tier 2 4  
> **置信度摘要**：三者均为 2026 年活跃的 **Slack/协作面 Work Agent** 类产品；Raft 与物流 AI 公司 Raft、Raft 共识算法 **同名异物**，下文分节消歧。

---

## 1. 执行摘要

**Viktor**（Zeta Labs）是面向中小企业的 **「AI 员工」**：驻 Slack / Microsoft Teams，接 3,200+ SaaS，在云端沙箱写代码并端到端交付报表、仪表盘、应用等；2026 年 2 月 GA，5 月 Accel 领投 **$75M Series A**，按 credits 计费（约 $50/月/workspace 起）。

**Raft**（Botiverse，原 **Slock**）是 **人机共建的 Agent 原生协作平台**：Agent 有持久身份与记忆，通过本地 daemon 跑在用户机器上，在类 Slack 的 channel 里与人类并列协作；2026 年 6 月 12 日由 Slock 更名 Raft，7 月发布 **Raft 1.0**；创始人 Richard（RC）曾任 Moonshot **Kimi CLI** 负责人。

**Claude Tag**（Anthropic）是 **Slack 内的团队级 Claude Agent**：在频道 `@Claude` 委派任务，组织级身份与审计、频道记忆、异步/ambient 模式；2026-06-23 发布 beta，面向 Claude **Team / Enterprise**；Anthropic 内部称产品团队 **65% 代码** 由内部版 Claude Tag 产出；**2026-08-03** 旧版 Claude in Slack 切换为 Claude Tag。

三者同属 **Knowledge Work Agent / Slack 嵌入式委派** 赛道，但定位分化：**Viktor** = 托管 SaaS + 广集成 + 多模型；**Claude Tag** = Anthropic 栈 + 企业治理；**Raft** = 本地/自管 runtime + 多 Agent 团队编排（偏 builder / agent-native 团队）。

---

## 2. 搜索过程摘要

| 轮次 | 新增 query 示例 | 本轮增量发现 |
|------|----------------|--------------|
| R1 | `Viktor AI agent work automation 2026` | Viktor 官方定位 AI employee；Raft.build agent 平台；Claude Tag Anthropic 官方公告 |
| R2 | `Viktor Zeta Labs Accel Series A` | $75M 融资、Fortune/EU-Startups 互证；Raft 原名 Slock |
| R3 | `Raft Slock rename Botiverse Kimi CLI` | RC 创始人背景；2026-06-12 更名；与 Hashicorp/logistics Raft 歧义 |
| R4 | `Claude Tag vs Viktor comparison` | 集成数、平台、计费差异；Viktor 官方对比页 |
| R5 | `site:anthropic.com Claude Tag` | 官方四步 setup、ambient/async、Opus 4.8 |
| R6 | `Claude Tag Cowork Code 2026` | Anthropic 三产品矩阵：Code / Cowork / Tag |

---

## 3. 搜索意图拆解

| 意图 | 检索词示例 | 结果状态 |
|------|------------|----------|
| Q1：三者分别是什么 | 各产品官方 + Tier 1 | 已覆盖 |
| Q2：有哪些类型/品类 | Work Agent 子类对比 | 已覆盖 |
| Q3：知名产品/方案 | 三者 + Slackbot/Agentforce 对照 | 已覆盖 |
| 歧义：Raft 同名 | `Raft freight forwarder` / `hashicorp raft` | 已覆盖（分节消歧） |
| 关系：与 Claude 产品线 | Tag vs Cowork vs Code | 已覆盖 |
| 反响/争议 | Viktor vs Claude Tag 对比、社区 | 部分（无 HN 热帖级讨论） |

---

## 4. 核心发现（多源验证）

### 4.1 三者分别是什么

| 产品 | 一句话定义 | 来源 A | 来源 B | 置信度 |
|------|-----------|--------|--------|--------|
| **Viktor** | 驻 Slack/Teams 的 **AI 员工**：云端计算机写代码、连 3,200+ 工具、交付可执行成果 | [viktor.com](https://viktor.com/) T0 | [Fortune 2026-05-19](https://fortune.com/2026/05/19/viktor-ai-startup-raises-75-million-for-virtual-coworker-exclusive/) T1 | 已确认 |
| **Raft** | **人机共建**协作平台：持久 Agent 身份 + 频道 + 任务板，Agent 跑在用户自有机器 | [raft.build 博客](https://raft.build/resources/blog/introducing-raft-where-humans-and-agents-build-together/) T0 | [Testing Catalog Raft 1.0](https://www.testingcatalog.com/raft-1-0-puts-ai-agents-in-team-mode/) T1 | 已确认 |
| **Claude Tag** | Slack 内 **@Claude 团队 Agent**：组织身份、频道记忆、异步委派 | [Anthropic 公告 2026-06-23](https://www.anthropic.com/news/introducing-claude-tag) T0 | [The Verge](https://www.theverge.com/ai-artificial-intelligence/954921/anthropic-introduced-claude-tag-a-new-ai-agent-slack-integration) T1 | 已确认 |

**叙述**：三者都不是「聊天机器人」口径——都强调 **委派真实工作**（写 PR、查数据、出报表），且默认 **多人可见**（频道/thread），属于 2026 年爆发的 **Slack-as-agent-hub** 子品类。Viktor 与 Claude Tag 直接竞争 Slack 企业客户；Raft 更偏 **多 Agent 编排 + 本地 runtime**，与 Multica 等开源方案对照（CodePick 2026-08）。

### 4.2 有哪些类型（品类内分型）

| 类型（依据：部署与治理模型） | 特征 | 代表 | 来源 |
|------------------------------|------|------|------|
| **托管 SaaS 员工** | 厂商云沙箱、广 SaaS 集成、按 workspace/credits 计费 | Viktor | viktor.com · Fortune |
| **模型厂商团队 Agent** | 绑定 Claude 栈、组织级 service account、usage 计费 | Claude Tag | anthropic.com · claude.com/docs |
| **Agent-native 协作 OS** | 本地 daemon、多 runtime、频道+任务+多 Agent 互审 | Raft | raft.build · Botiverse |
| **平台原生 Agent**（相邻，非本次三主体） | Slackbot、Agentforce 等 | Salesforce Slack 2026 | TechCrunch |

**易混淆**：**Raft** 至少三个实体——(1) 本报告 **raft.build**；(2) 物流 AI **Raft**（原 Vector.ai，freight forwarders）；(3) **Raft 共识算法**（Hashicorp 等）。用户若只说「Raft AI」，需结合上下文（Slack/agent → raft.build；供应链 → vector.ai/raft）。

### 4.3 知名产品 / 代表方案（Work Agent 地图）

| 场景 | 产品 | 备注 | 来源 |
|------|------|------|------|
| Slack 托管 AI 员工 | Viktor | 20k+ Slack workspace（Testing Catalog 2026） | testingcatalog.com |
| Slack 团队 Claude | Claude Tag | Team/Enterprise beta | anthropic.com |
| 多 Agent 本地协作 | Raft | Beta 20k+ builder；人均 4 agents | testingcatalog.com |
| Slack 平台 Agent | Slackbot (Salesforce) | Business+/Enterprise+ GA 2026-01 | TechCrunch |
| 个人委派（非 Slack） | Claude Cowork | 桌面沙箱，单人 | anthropic.com/learn |

---

### 4.4 Viktor 详情

| 维度 | 内容 | 来源 |
|------|------|------|
| 公司 | **Zeta Labs** / Zeta AI, Inc.；华沙 + 慕尼黑；前 Meta 工程师 Fryderyk Wiatrowski（CEO）、Peter Albert（CTO） | Fortune · EU-Startups · viktor.com/blog |
| 前身 | **Jace**（邮件/浏览器 Agent），2025  pivot 至 Viktor | Leonis Cap · Nordic9 |
| 上线 | 2026 年 2 月公开；10 周内 ~$15M ARR（公司口径） | EU-Startups · viktor.com |
| 融资 | 2026-05 **$75M Series A**，Accel 领投；Slack 联合创始人 Butterfield/Henderson 等 angel | Fortune · The Next Web |
| 能力 | Slack + **Microsoft Teams**；3,200+ 集成；云端写代码；定时任务；敏感操作 approve/reject | viktor.com |
| 定价 | Credits；Team **$50/月** + 20k credits；注册 $100 免费 credits | viktor.com · 第三方评测 |
| 安全 | SOC 2 Type 1；Type 2 / ISO 27001 进行中 | viktor.com |
| 差异化 | **多模型可选**（非单模型锁定）；集成广度；Teams 已 GA（2026 夏） | viktor.com/compare |

### 4.5 Raft（raft.build）详情

| 维度 | 内容 | 来源 |
|------|------|------|
| 公司 | **Botiverse**（botiverse.dev）；2025 成立 | raft.build |
| 创始人 | **Richard**（@istdrc / RC）；前 **Moonshot Kimi CLI** 负责人 | LinkedIn · EarlyTerms · TopicDigg |
| 更名 | **Slock** → **Raft**，2026-06-12；隐喻 Raft 共识协议（分布式协调） | @istdrc · raft.build 上海 meetup |
| 1.0 | 2026-07 GA；免费档 + Pro **$8.80/人/月**（年付）；1 agent = 0.1 seat | Testing Catalog |
| 架构 | 本地 **daemon/CLI**；Agent 支持 Claude Code、Codex、Kimi 等 runtime | raft.build |
| 产品哲学 | 「One agent is one session」— 持久身份，非每次新实例；Agent 可 @mention、认领任务、互审 | 官方博客 |
| 自用案例 | 团队自称 10+ 人 + 100+ 命名 Agent，99% 工作在内跑 | LinkedIn |

### 4.6 Claude Tag 详情

| 维度 | 内容 | 来源 |
|------|------|------|
| 发布 | **2026-06-23** beta；模型 **Opus 4.8** | anthropic.com |
| 计划 | Claude **Team / Enterprise** only；**非** Free/Pro/Max | claude.com/docs |
| 能力 | 频道 **multiplayer** Claude；**频道记忆**；**ambient** 主动跟进；**异步** 数小时/数天任务；DM 走个人账号 | anthropic.com |
| 治理 | Admin 在 `claude.ai/admin-settings/claude-tag` 配工具/仓库/频道；**组织 usage 计费** + spend limit；Audit 页 | claude.com/docs |
| 身份 | Slack 发 Claude App；GitHub 用 Claude GitHub App；各工具 **service account** | claude.com/docs/audit |
| 迁移 | 替换旧 **Claude in Slack**；Enterprise/Team **2026-08-03** 切换 | support.claude.com |
| 产品线位置 | **Claude Code**（终端/IDE 工程）· **Cowork**（个人桌面知识工作）· **Tag**（Slack 团队） | anthropic.com/learn · claude.com/docs |

---

## 5. 时间线

| 日期 | 事件 | 来源 |
|------|------|------|
| 2023 | Zeta Labs 成立；Jace 产品 | EU-Startups |
| 2025 | Jace pivot → Viktor | Nordic9 |
| 2026-02 | Viktor 公开上线 | Leonis Cap |
| 2026-03-04 | Slock 公开发布（Raft 前身） | EarlyTerms |
| 2026-05-19 | Viktor **$75M Series A** | Fortune |
| 2026-05-21 | Raft（Botiverse）产品介绍文 | raft.build |
| 2026-06-12 | Slock 更名为 **Raft** | @istdrc |
| 2026-06-23 | **Claude Tag** 发布 beta | Anthropic |
| 2026-07 | **Raft 1.0** GA | Testing Catalog |
| 2026-08-03 | Claude in Slack → Claude Tag 切换 | Anthropic Help Center |

---

## 6. 实体关系

```
Anthropic ── Claude Tag ── Slack (Team/Enterprise)
Zeta Labs ── Viktor ── Slack + Microsoft Teams
Botiverse ── Raft (ex-Slock) ── app.raft.build + local daemon

相邻竞品/平台：
Salesforce ── Slackbot / Agentforce
OpenAI ── ChatGPT Work / Workspace Agents（未在本报告深搜）
```

---

## 7. 增量信息

### 7.0 增量对照表

| 增量主张 | 相对 Tier 0 的新增点 | 首见来源 | 互证 | 验证结果 | 置信度 |
|---------|---------------------|---------|------|---------|--------|
| Anthropic 产品团队 65% 代码由内部 Claude Tag 产出 | 官方博客量化内部采用 | Anthropic T0 | Anthropic webinar T0 | 已确认 | 已确认 |
| Viktor 10 周 $15M ARR | 增长曲线 | EU-Startups T1 | Fortune / TNW T1 | 很可能 | 很可能 |
| Raft beta 人均 4 agents | 使用形态 | Testing Catalog T1 | LinkedIn T2 | 很可能 | 很可能 |
| Claude Tag 首发 ~14 connectors | 集成规模小于 Viktor | Viktor compare T0（竞品） | 第三方对比 T2 | 很可能 | 很可能（单源官方未列全表） |
| 旧 Claude in Slack 2026-08-03 退役 | 迁移 deadline | Help Center T0 | DataCamp T1 | 已确认 | 已确认 |

### 7.1 已验证增量信息

- **Claude Tag = Claude Code 的团队演化**：官方明确「evolution of Claude Code」，multiplayer + proactive（Anthropic T0）。
- **Viktor 强调 model-agnostic**：可切换 frontier 模型并按任务选便宜/贵模型（viktor.com/business T0）。
- **Raft 命名有意呼应分布式 Raft 协议**：创始人 @istdrc 原话（TopicDigg 转引 T2，与官方「coordinate」叙事一致）。

### 7.2 未通过验证的传闻

| 传闻 | 来源 | 拒绝原因 |
|------|------|---------|
| Viktor 2026-08 已超 $30M ARR | 部分 SEO 评测 | 仅单源 T2/农场风，无 Tier 1 互证 |
| Claude Tag 仅 14 集成「官方定稿」 | 对比站 | 数字来自 Viktor 竞品页，Anthropic 未发布完整官方计数 |

### 7.3 权威媒体解读

- **The Verge**（2026-06-23）：Claude Tag 让 Claude 以 Slack 成员身份写/合并 PR、查销售数据、接委派任务（Hayden Field）。
- **Fortune**（2026-05-19）：Viktor 为「virtual coworker」，Accel 押注协作面嵌入 AI。
- **The Next Web**：Viktor 客户曲线为 Accel 大额 A 轮提供合理性（称 18 个月内分发速度罕见）。

### 7.4 社区与舆论反响

- **HN/Reddit**：检索范围内 **未见** 针对 Claude Tag 或 Raft 1.0 的显著热帖；Viktor 讨论分散在 SaaS 评测站。
- **中文语境**：PingWest 等报道 **Slock**（Raft 前身）为「Agent 社交/协作层」；Raft 上海 meetup（2026-06-14，60+ 人）显示国内 builder 社区关注。

### 7.5 争议与风险

| 产品 | 风险点 |
|------|--------|
| Viktor | 云-only、Slack/Teams 依赖；credits 成本不可预测；敏感操作需人工 approve |
| Claude Tag | Team/Enterprise 门槛；usage 计费；beta 功能变动；DM vs 频道计费分裂 |
| Raft | 需自管 daemon/API；闭源 SaaS；Enterprise SSO/私有部署「coming soon」 |

### 7.6 竞品与行业对照

| 维度 | Viktor | Claude Tag | Raft |
|------|--------|------------|------|
| 入口 | Slack, Teams | Slack（beta） | Raft app（类 Slack） |
| 集成 | 3,200+ | Admin 配置 connectors + GitHub 等 | 自带 channel/task；接 Claude/Codex/Kimi |
| 模型 | 多模型 | Claude Opus 4.8 | BYO subscription |
| 治理 | SOC2；channel approve | Service account + Audit + spend cap | 本地数据；Pro 定价 |
| 受众 | SMB / agency / ops | Claude 企业客户 | Agent-native 工程团队 |

### 7.7 中文语境

- **Slock/Raft**：中国 tech 媒体将此类产品称为「给 Agent 的 Slack」；与 **Multica** 等开源克隆对照讨论（CodePick 中文导向稿）。
- **Claude Tag / Viktor**：中文 Tier 1 深度稿检索范围内较少；概念主要通过英文官方 + 中文二手解读传播。

---

## 8. 分歧与待核实

| 项 | 说法 A | 说法 B | 建议 |
|----|--------|--------|------|
| Viktor workspace 数 | 官方/blog：12,000+ teams（2026-05） | 部分稿：20,000+ Slack workspaces | 以 **较新且可访问的官方/Testing Catalog** 为准；数字随增长变化 |
| Claude Tag 集成数量 | Viktor 称 launch ~14 | Anthropic 未给总数 | 以 **admin 可配 connectors 文档** 为准，不用竞品数字定稿 |

---

## 9. 对用户问题的直接回答

### 9.1 Viktor 是什么？

**Viktor** 是波兰/德国公司 **Zeta Labs** 推出的 **AI 员工（AI employee / AI coworker）**：安装进 **Slack 或 Microsoft Teams**，连接 **3,200+** 业务工具，在 **云端计算机** 里写代码、拉数据、生成 PDF/表格/小型 Web 应用，并支持定时自动化。2026 年 2 月上线后增长极快，5 月获 **Accel 领投 $75M A 轮**。计费为 **credits**（约 $50/月/workspace 起）。定位：**非技术团队也能用的托管型 Work Agent**。

### 9.2 Raft 是什么？

若指 **AI Agent 产品**（与 Viktor、Claude Tag 并列）：**Raft**（[raft.build](https://raft.build/)）是 **Botiverse** 的人机协作平台，前身 **Slock**（2026-03 发布，2026-06-12 更名）。Agent 作为 **有记忆、有身份的队友** 常驻 channel，通过 **本地 daemon** 运行在用户机器上，支持 Claude Code、Codex、Kimi 等 runtime；2026-07 **Raft 1.0** GA。创始人 **Richard（RC）** 曾任 Moonshot **Kimi CLI** 负责人。

**不是**：物流 AI 公司 Raft（原 Vector.ai）；也不是 Hashicorp **Raft 共识算法**。

### 9.3 Claude Tag 是什么？

**Claude Tag** 是 **Anthropic** 2026-06-23 发布的 **Slack 团队 Agent**：在频道 **@Claude** 委派任务，Claude 以 **组织级身份**（非个人 Claude 账号）异步执行，可连 GitHub、Datadog、Notion 等，具备 **频道记忆、ambient 主动模式、计划任务**。仅 **Claude Team / Enterprise** beta；跑 **Opus 4.8**；频道工作 **组织 usage 计费**。Anthropic 将其定位为 **Claude Code 向团队协作的演化**，与 **Cowork**（个人桌面）、**Code**（终端工程）并列。

### 9.4 三者如何放一起理解？

| | Viktor | Claude Tag | Raft |
|---|--------|------------|------|
| **谁做的** | Zeta Labs | Anthropic | Botiverse |
| **在哪用** | Slack + Teams | Slack | Raft 自有 workspace（+ Slack 式频道） |
| **典型用户** | 运营/市场/小团队 | 已购 Claude 企业版 | 多 Agent 工程团队 |
| **核心卖点** | 广集成 + 多模型 + 托管交付 | Claude 栈 + 企业审计/身份 | 本地 runtime + 多 Agent 编排 |

---

## 10. 参考链接（按 Tier）

### Tier 0 官方
- https://viktor.com/
- https://viktor.com/blog/viktor-series-a
- https://raft.build/
- https://raft.build/resources/blog/introducing-raft-where-humans-and-agents-build-together/
- https://www.anthropic.com/news/introducing-claude-tag
- https://claude.com/docs/claude-tag/overview
- https://support.claude.com/en/articles/15594475-what-is-claude-tag
- https://www.anthropic.com/learn

### Tier 1 权威媒体
- https://fortune.com/2026/05/19/viktor-ai-startup-raises-75-million-for-virtual-coworker-exclusive/
- https://www.eu-startups.com/2026/05/ai-coworker-startup-viktor-raises-e64-7-million-series-a-after-hitting-e12-9-million-revenue-run-rate-within-10-weeks-of-launch/
- https://thenextweb.com/news/viktor-75-million-series-a-accel-ai-coworker-slack-teams
- https://www.theverge.com/ai-artificial-intelligence/954921/anthropic-introduced-claude-tag-a-new-ai-agent-slack-integration
- https://www.testingcatalog.com/raft-1-0-puts-ai-agents-in-team-mode/
- https://www.testingcatalog.com/zeta-labs-brings-ai-employee-viktor-to-microsoft-teams/
- https://techcrunch.com/2026/01/13/slackbot-is-an-ai-agent-now/

### Tier 2 补充
- https://www.leoniscap.com/research/building-towards-ai-employees-our-journey-with-viktor
- https://viktor.com/compare/viktor-vs-claude-tag
- https://codepick.dev/en/guides/raft-agent-collaboration-intro/
- https://earlyterms.com/term/slock

---

*本报告按 web-deep-search-spec v1.4 生成，检索日 2026-09-02，共 6 轮 loop。*
