# AI Employee（AI 员工）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI Employee / Chat-native AI Coworker**——Agent 作为**共享同事**驻在 Slack、Teams、企微等 IM 频道；全员 `@` 委派、thread 交活、组织身份与审计；验收以 **multiplayer 协作面、频道记忆、异步交稿与审批** 为主。本页为 **IM 驻场 AI Employee 产品 SSOT**（完整 URL 表仅此一处）；**这一次交付物** → [work-agent.md](work-agent.md)；**团队 playbook 资产** → [workspace-agent.md](workspace-agent.md)；纯对话 → [chatbot.md](../chat-social/chatbot.md)。

**材料范围**：公开网络检索（Anthropic Claude Tag、Viktor、Salesforce Slackbot、OpenAI Workspace Agents in Slack、腾讯 WorkBuddy 企微指南、TechCrunch / Fortune / The Verge、Process.st / Vellum 品类对比摘要）；调研底稿 `clients/temp/viktor-raft-claude-tag-web-search-2026-09-02.md`。**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-09-02**。簇边界见 [`skills/knowledge-block/references/ai-employee-cluster.md`](../../skills/knowledge-block/references/ai-employee-cluster.md)。

**站内对照**：**待**上线 · slug **`ai-employee`** · 发文优先 **`/blog/ai-employee`**

**Tools 关键词与 slug 映射**：`keywordEn`: **AI Employee / AI Coworker in Slack / Chat-native AI Teammate** · `keywordZh`: **AI 员工 / IM 里的 AI 同事 / 聊天软件里的数字员工** · 锚点 **`#ai-employee-tools`**（待写入 keywords 表）

**站内相邻**：[work-agent.md](work-agent.md) · [workspace-agent.md](workspace-agent.md) · [workflow.md](workflow.md) · [multi-agent.md](multi-agent.md) · [chatbot.md](../chat-social/chatbot.md) · [agent-skills.md](agent-skills.md)

---

## 与相邻 slug 分流

| 维度 | **`ai-employee`（本页）** | **`work-agent`** | **`workspace-agent`** | **`chatbot`** | **`workflow`** |
|------|---------------------------|------------------|----------------------|---------------|----------------|
| **典型买家问题** | 「在 Slack 里雇一个能干活、全队可见的同事」 | 「帮我把 deck/报告/文件夹做完」 | 「把这套流程固化成全组 Agent」 | 「回答/起草一段话」 | 「A 应用数据自动同步到 B」 |
| **优化单位** | **协作界面**：IM 里的共享 Agent | **这一次交付物** | **这一类 playbook** | **对话回合** | **确定性管道** |
| **入口** | Slack / Teams / 企微 **频道** | 桌面 Cowork / 云 Work 会话 | Admin 配 Agent + API/定时 | 私聊窗口 | Zapier / n8n |
| **身份** | **频道共享一个同事**（@Claude / @Viktor） | 多为个人会话（可多人见 thread） | 组织级 Agent **资产** | 每人一个 bot | 无身份 |
| **成功标准** | thread 交活 + 审批 + 审计 | 可编辑交付物文件 | RBAC + 流程可规模化 | 满意回复 | 流程成功率 |
| **代表产品** | Viktor、Claude Tag、Dash、Junior | Cowork、ChatGPT Work、Manus | OpenAI Workspace Agents、Notion Custom Agents | ChatGPT Chat | Make、Zapier |

**三分法（对外口径）**：`work-agent` = **怎么把这次活干完**；`workspace-agent` = **团队怎么把流程固化**；`ai-employee` = **Agent 怎么进 IM 和你们一起协作**。

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **AI Employee / AI 员工**：营销与 SEO 主词（~1K–2K/mo US 「AI employee」集群）——强调 **雇一个干活的**，非租一个 chat 窗口。厂商例：Viktor *Not a tool. A hire.*；Fortune 称 Claude Tag 为 *virtual employee*。
- **AI Coworker / AI Teammate**：同义轮换——coworker 品牌更安全；teammate 适合 Slack 副标题（*AI teammate in Slack*）。**AI Colleague** 搜索量弱，不作 slug 主词。
- **Chat-native / IM-embedded**：协作发生在**已有 IM**，而非单独打开 Cowork 桌面或 ChatGPT 标签页。
- **Multiplayer Agent**：频道内**一个**共享 Agent 实例，全员可见 thread、可接棒——与每人私聊 assistant 相对（Claude Tag 官方表述）。
- **@mention delegation**：在频道 `@` Agent → 异步多步 → thread 回帖交付物。
- **Org-level identity**：Slack 发 Claude App、GitHub 用 Claude GitHub App、各工具 **service account**——非个人 OAuth（Claude Tag docs）。
- **Ambient / proactive**：可选主动跟进频道、定时自查（Claude Tag ambient；Viktor 定时任务）。
- **Approval before act**：发邮件、改 CRM、花钱前人工 approve（Viktor、Dash 卖点）。

---

## 专题对照 / 扩展定义

**AI Employee vs Work vs Workspace vs Chat**：

| 维度 | **AI Employee** | **Work Agent** | **Workspace Agent** | **Chatbot** |
|------|-----------------|----------------|---------------------|-------------|
| **问什么** | Agent **在 IM 里像不像同事** | **交稿**了吗 | **流程资产**可审计吗 | **回复**满意吗 |
| **Claude Tag** | ✅ 主叙事 | 能力重叠 | 治理重叠 | ❌ |
| **Claude Cowork** | ❌（桌面，非 IM 主入口） | ✅ 主叙事 | ❌ | ❌ |
| **OpenAI Workspace Agents** | Slack **部署面**（本页 Type D） | 可触发 Work | ✅ playbook 主叙事 | ❌ |

**易混淆**：**Claude Tag**（IM 员工）≠ **Claude Cowork**（个人桌面 Work）；**Slackbot**（Salesforce 平台 Agent）≠ **ChatGPT for Slack**（个人 assistant）；**Raft**（Agent-native 协作 OS）→ [multi-agent.md](multi-agent.md)，**非**本页 IM Employee。

---

## 问题域（为何会出现这类产品）

- **Slack 变 Agent Hub**：Salesforce 将 Slackbot 升级为 agent（2026-01 GA）；Anthropic/OpenAI 把 Claude/ChatGPT **搬进频道**——协作面即入口。
- **私聊 AI 不够「全队看见」**：PM 在 ChatGPT 里写的简报，销售看不见；IM Employee 把执行过程放在 **thread**。
- **SEO 与采购语言**：「AI employee」成为品类词（Sintra、Viktor、Teammates.ai 抢位）；buyer 用 **headcount 隐喻**理解预算。
- **与 Work Agent 能力合流**：同一 harness（工具调用、沙箱、多步）——差异在 **surface（IM）与 multiplayer 治理**，非模型能力 alone。

---

## 能力栈（概念拆分）

- **频道驻场与 @ 路由**：安装 App → 指定频道 → `@` 触发任务。
- **Thread 异步执行**：长任务后台跑，checklist 更新，完成后 thread 交稿。
- **频道 / 组织记忆**：跨日上下文（Claude Tag channel memory；Viktor workspace memory）。
- **广集成**：Viktor 3,200+；Claude Tag admin 配 connectors + GitHub App。
- **Human-in-the-loop**：敏感操作 approve/reject in chat。
- **计费**：workspace credits（Viktor）vs org usage balance（Claude Tag）vs 平台订阅（Slackbot Enterprise+）。

---

## 形态谱系（Type A–F）

| Type | 特征 | 典型场景 | 代表 |
|------|------|----------|------|
| **A** | 托管 IM 员工；Slack + Teams | 运营/Agency 频道交活 | Viktor、Dash、Junior |
| **B** | 模型厂 Slack Agent；单模型栈 | Claude 企业客户 | Claude Tag |
| **C** | 平台原生 IM Agent | Salesforce / M365 租户 | Slackbot、Teams Copilot Agent |
| **D** | 企业 Agent **部署进** Slack | 已建 Workspace Agent 进频道 | OpenAI Workspace Agents |
| **E** | 中国 IM 桥接 | 企微/钉钉/飞书远程控桌面或托管 | WorkBuddy 企微、钉钉 Agent、飞书 Doubao |
| **F** | 岗位型 AI Employee（常非 IM 主入口） | SDR/支持虚拟员工 | Sintra、11x — 仅索引，深度不进主榜 |

---

## 营销话术（KB 内 · 发文可扩）

| 英文 | 用途 |
|------|------|
| **AI Employee** | SEO H1、品类页 |
| **AI Coworker** | 品牌安全正文 |
| **AI Teammate in Slack** | 副标题、Ads |
| **Virtual employee / Digital employee** | 媒体口径（Fortune、国内「数字员工」） |

**与私聊 Chat 一句差异**：Chat = 一个人一个窗口；AI Employee = **一个频道一个同事**，交付在 thread。

**伦理注记（非法律意见）**：MIT / IDE 2026 研究指出 *employee/coworker* framing 可能降低人类复核强度——对外宜强调 **同事 + 审批 + 人负责**，非「无人值守 FTE 替代」。

---

## 风险 · 合规 · 治理

- **频道权限 = 数据边界**：Agent 可见频道历史；private channel 需单独授权。
- **组织 vs 个人计费分裂**：Claude Tag 频道走 org usage，DM 走个人 seat（Help Center）。
- **过度自主**：ambient 模式可能打扰；需 admin 开关与 spend cap。
- **供应商锁定**：深度集成 Slack 生态；Teams 双栈需另选产品（Viktor 等）。

---

## 落地碎片

- 先问：团队 **主 IM** 是 Slack、Teams 还是企微？→ 缩 Type A/B/C/E。
- 要 **Claude 栈 + 企业审计** → Claude Tag（B）；要 **多模型 + 广 SaaS** → Viktor/Dash（A）。
- 已有 OpenAI Workspace Agents → Type D：playbook 在 [workspace-agent.md](workspace-agent.md)，Slack 驻场在本页。
- 一次性 heavy 交付（整盘文件夹 deck）且不必全队看见 → [work-agent.md](work-agent.md) Cowork 可能更顺。

---

## 行业注记（快变 · 2026）

| 日期 | 事件 | 来源层级 |
|------|------|----------|
| 2026-01 | Slackbot 升级为 AI agent GA | T0/T1 |
| 2026-02 | Viktor 公开；10 周 ~$15M ARR（公司口径） | T1 |
| 2026-05 | Viktor $75M Series A（Accel） | T1 |
| 2026-06-23 | Anthropic **Claude Tag** beta | T0 |
| 2026-08-03 | Claude in Slack → Claude Tag 切换 | T0 |
| 2026-07 | Raft 1.0 GA（Agent 协作 OS，非 IM Employee） | T1 |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 区域 | 一句话 | URL |
|------|------|------|--------|-----|
| **Viktor** | A | 全球 | Slack+Teams；3,200+ 工具；云端写代码交活；credits | [viktor.com](https://viktor.com/) |
| **Claude Tag** | B | 全球 | Slack；@Claude；Opus 4.8；Team/Enterprise；org identity | [anthropic.com/news/introducing-claude-tag](https://www.anthropic.com/news/introducing-claude-tag) · [Docs](https://claude.com/docs/claude-tag/overview) |
| **Dash** | A | 全球 | Slack+Teams；approve before send/post/spend | [dashpup.ai](https://dashpup.ai/) |
| **Junior** | A | 全球 | Slack+Teams AI employee；approval-gated | [junior.so](https://junior.so/) |
| **Slackbot** | C | 全球 | Salesforce；Business+/Enterprise+；MCP client | [TechCrunch 2026-01](https://techcrunch.com/2026/01/13/slackbot-is-an-ai-agent-now/) |
| **OpenAI Workspace Agents（Slack）** | D | 全球 | 共享 agent 部署进 Slack；playbook → workspace-agent | [openai.com/index/introducing-workspace-agents-in-chatgpt](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) |
| **Microsoft Copilot Studio → Teams** | C | 全球 | 低代码 agent 发布到 Teams | [microsoft.com/microsoft-copilot/microsoft-copilot-studio](https://www.microsoft.com/en-us/microsoft/copilot/microsoft-copilot-studio) |
| **WorkBuddy 企微助理** | E | 中国 | 企微 @ 机器人远程驱桌面 WorkBuddy | [workbuddy.cn/docs/workbuddy/Wecom-Guide](https://www.workbuddy.cn/docs/workbuddy/Wecom-Guide) |
| **Glean Agents** | — | 全球 | 企业知识 + agent；Slack 等入口 | 见官方 |
| **Dust** | — | 全球 | 共享 agent workspace + Slack | [dust.tt](https://dust.tt/) |
| **Lindy** | — | 全球 | 偏 web builder；Slack 集成 — assistant 向 | [lindy.ai](https://www.lindy.ai/) |

**桌面/云 Work 委派（非 IM 主叙事）** → [work-agent.md](work-agent.md)（Cowork、ChatGPT Work、Manus 等）。

**Agent 协作 OS（Raft / Multica）** → [multi-agent.md](multi-agent.md)。

### 对比与测评（第三方；观点非官方）

- **IM Employee vs Work Agent**：本页 Type A–E 为「在 Slack/Teams @ 即干活」；Cowork/Manus 等桌面/云委派见 [work-agent.md](work-agent.md)——勿混验收。
- **审批闸门是 2026 共识**：全自主 Type A vs approval-gated Type B——放权程度匹配组织信任（媒体观点见 §延伸阅读）。

*观点非官方。*

---

## 延伸阅读 · 站内外

**站内**

- 交付物轴：[work-agent.md](work-agent.md)
- Playbook 轴：[workspace-agent.md](workspace-agent.md)
- 簇边界（skills）：[`skills/knowledge-block/references/ai-employee-cluster.md`](../../skills/knowledge-block/references/ai-employee-cluster.md)
- 确定性管道：[workflow.md](workflow.md)

**站外（Tier 1/2）**

- Fortune · Claude Tag virtual employee：https://fortune.com/2026/06/23/anthropic-claude-tag-virtual-employee-tool-slack/
- The Verge · Claude Tag：https://www.theverge.com/ai-artificial-intelligence/954921/anthropic-introduced-claude-tag-a-new-ai-agent-slack-integration
- 调研底稿（非 SSOT）：`clients/temp/viktor-raft-claude-tag-web-search-2026-09-02.md`