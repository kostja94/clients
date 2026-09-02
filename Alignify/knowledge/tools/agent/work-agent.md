# Work Agent（工作智能体）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Work Agent / 工作智能体**——用户描述**工作成果**，系统自主规划多步任务并交回**可交付物**（非聊天回复）；验收以**交付物格式、委派模式边界与沙箱/授权范围**为主。本页为 **Work Agent 产品 SSOT**（完整 URL 表仅此一处）；IM 协作面 → [ai-employee.md](ai-employee.md)；团队 playbook → [workspace-agent.md](workspace-agent.md)；本机/GUI 执行面 → [agent-for-desktop.md](agent-for-desktop.md)；确定性自动化 → [workflow.md](workflow.md)。

**材料范围**：公开网络检索（Anthropic / OpenAI / Microsoft / Google / Alibaba / Tencent / ByteDance 官方文档与公告、TechCrunch / 36氪 等 Tier 1 媒体、HN 社区讨论摘要）。**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-09-02**。簇边界见 [`skills/knowledge-block/references/work-agent-cluster.md`](../../skills/knowledge-block/references/work-agent-cluster.md)。

**站内对照**：**待**上线 · slug **`work-agent`** · 发文优先 **`/blog/work-agent`**

**Tools 关键词与 slug 映射**：`keywordEn`: **Work Agent / AI Work Agent** · `keywordZh`: **工作智能体 / AI 办公智能体** · 锚点 **`#work-agent-tools`**

**站内相邻**：[ai-employee.md](ai-employee.md) · [workspace-agent.md](workspace-agent.md) · [agent-for-desktop.md](agent-for-desktop.md) · [agent-sandbox.md](agent-sandbox.md) · [agent-skills.md](agent-skills.md) · [workflow.md](workflow.md) · [multi-agent.md](multi-agent.md) · [coding.md](../coding/coding.md) · [chatbot.md](../chat-social/chatbot.md)

---

## 与相邻 slug 分流

| 维度 | **`work-agent`（本页）** | **`ai-employee`** | **`workspace-agent`** | **`agent-for-desktop`** | **`workflow`** | **`coding`** | **`chatbot`** |
|------|--------------------------|-------------------|----------------------|-------------------------|----------------|--------------|---------------|
| **典型买家问题** | 「帮我把这份 deck/报告/文件夹整理做完」 | 「在 Slack 里雇一个能干活、全队可见的同事」 | 「把每周销售简报固化成全组用的 Agent」 | 「Agent 怎么读我电脑上的文件？」 | 「A 应用数据自动同步到 B」 | 「帮我在仓库里改代码、开 PR」 | 「帮我回答/起草一段话」 |
| **优化单位** | 个人 + **这一次交付物** | **IM 协作界面** | 团队 + **可重复 playbook** | **端点**：本机夹 / GUI / VM | **确定性**跨 SaaS 管道 | 代码库 / PR | **对话** |
| **成功标准** | 可编辑文件（xlsx/pptx/doc/文件夹） | thread 交活 + 审批 | 流程跑通 + RBAC + 审计 | 本机/GUI 操作成功 | 流程成功率 | 合并就绪的代码变更 | 满意回复 |
| **代表产品** | Cowork、ChatGPT Work、Manus | Viktor、Claude Tag | OpenAI Workspace Agents | Floatboat、Poly | Zapier、n8n | Cursor Agent、Codex | ChatGPT Chat |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Work Agent / 工作智能体**：面向**知识工作交付**的 Agent 产品品类——用户给出**成果描述**（goal/outcome），系统在沙箱或授权范围内**规划、调用工具、读写文件/浏览网页**，返回**可交付制品**；与「只输出建议文本」的 chat 相对。Anthropic/OpenAI 官方用语常作 **delegating（委派）**。
- **Outcome-first / 成果导向**：成功标准是「这份 deck 能发给董事会」，而非「聊清楚思路」。
- **Chat vs Work（模式分裂）**：同一套模型下的两种 UX——**Chat** = 回合制思考与对话；**Work/Cowork** = 长时多步、工具调用、后台运行、交稿。2026 年用户常见痛点是**模式边界不清**（HN 多次讨论）。
- **Deliverable vs transcript**：Work Agent 的产出应是**可打开的文件或结构化 artifact**；纯聊天 transcript 不算完成。
- **Task/session context vs living memory**：Work Agent 记忆以**任务、授权文件夹、连接器上下文**为主；与 **Personal Agent** 的跨日生活记忆不是同一产品轴。
- **Sub-agent / 并行子任务**：复杂交付物拆给子 Agent 并行（Cowork subagents、ChatGPT Work 多 agent 架构——以各官方说明为准）。
- **Scheduled Tasks / 计划任务**：同一 Work 会话内的**重复委派**；与 **workspace-agent** 的「组织级共享 playbook + API 触发」仍有治理深度差异。

---

## 专题对照 / 扩展定义

**Work vs Personal vs Coding vs Chatbot**（术语见 §词汇锚点）：

| 维度 | **Work Agent** | **Personal Agent** | **Coding Agent** | **Chatbot / Chat 模式** |
|------|----------------|-------------------|------------------|-------------------------|
| **服务谁** | 知识工作者的**这一次任务** | **一个人**的整周生活 | 工程师的**代码库** | 任意**问答/起草** |
| **成功指标** | 交付物文件名 + 截止日期 | 连续性、少丢球 | PR / 测试通过 | 回复质量 |
| **典型产品** | Cowork、ChatGPT Work、WorkBuddy | productivity 相邻块 | Cursor Agent、Codex | ChatGPT Chat |
| **本库 slug** | **本页** | 待建 / productivity | [coding.md](../coding/coding.md) | [chatbot.md](../chat-social/chatbot.md) |

**Work Agent 类型（Type A–E；产品规格见 §外链索引）**：

| Type | 特征 | 典型场景 | 代表 |
|------|------|----------|------|
| **A** | 一人当场发起；云/桌面沙箱 | board deck、研究综述、整理下载夹 | Claude Cowork、ChatGPT Work、Manus |
| **B** | 跑在 M365 / Workspace / 飞书 / 钉钉 | 跨邮件+文档+日历的端到端流程 | Copilot Cowork、Doubao Work+Feishu、QwenWork+DingTalk |
| **C** | 共享、定时、API——**详见 workspace-agent** | 销售简报、采购跟进 | OpenAI Workspace Agents、Notion Custom Agents |
| **D** | 绑定工种或业务系统 | 软件工程、CRM | Devin、Agentforce（本页仅索引） |
| **E** | BYOK / 本地模型 | 敏感文档 | Coworker、Eigent → [agent-for-desktop.md](agent-for-desktop.md) |

**易混淆**：**Cowork vs Code/Codex**（知识工作 vs 代码库）；**Copilot Agent mode vs Copilot Cowork**（Office 文档内多步 vs 跨 M365 长运行）；**Work vs Workspace vs AI Employee**（交付物 vs playbook vs IM 同事）——见 [ai-employee.md](ai-employee.md)。

---

## 问题域（为何会出现这类产品）

- **Coding Agent 外溢**：Claude Code、Codex 证明 agent harness 在**非编程**知识工作同样有效；Cowork/Work 是同一架构的产品化命名（TechCrunch 2026-01/07）。
- **Chat 不够「交稿」**：知识工作者要的是**文件**，不是「你可以这样做」的说明；上传/粘贴文件夹成本高。
- **2026 平台战争**：Microsoft Copilot Cowork（2026-06-16 GA）、OpenAI ChatGPT Work、Anthropic Cowork 扩 web/mobile；中国腾讯/阿里/字节 2026-07~08 整合 WorkBuddy / QwenWork / Doubao Work。
- **计费模型分化**：flat 订阅（Claude）vs **Copilot Credits**（Microsoft）vs 席位+Credits 池（WorkBuddy/QwenWork）——选型需读 ToS，本页不维护价格数字。
- **与 Personal Agent 检索混流**：用 **交付物 vs 生活连续性** 分流。

---

## 能力栈（概念拆分，非厂商功能表）

- **目标解析与计划**：自然语言 brief → 可见步骤列表（Plan 模式类产品可人工审 plan 再执行）。
- **文件与格式读写**：xlsx/pptx/doc/pdf、批量重命名、目录整理；常与 **Skills/Plugins** 模板化输出。
- **浏览器与表单**：云浏览器填多步表单、抓取网页——ChatGPT Work、Cowork in Chrome 等。
- **连接器 / MCP**：Gmail、Calendar、Drive、Jira、Slack 等——见 [agent-skills.md](agent-skills.md)。
- **沙箱与隔离**：[agent-sandbox.md](agent-sandbox.md)。
- **子 Agent 并行**：研究/写作/制表分工。
- **Human-in-the-loop**：发送邮件、删文件、对外分享前确认。
- **Scheduled Tasks**：个人/workspace 内的 cron 式重复——深度治理在 workspace-agent。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 桌面 + 授权文件夹 | Local folder Cowork | Claude Cowork、WorkBuddy 桌面、ChatGPT Work 桌面 |
| **B** | 纯云 sandbox VM | Cloud work session | Manus、ChatGPT Work 云会话、Copilot Cowork |
| **C** | 套件原生（Work IQ / 飞书 / 钉钉上下文） | Suite-embedded work agent | Copilot Cowork、QwenWork、Doubao Work |
| **D** | 开源本地 Cowork 替代 | Open-source Cowork | Coworker、Eigent → agent-for-desktop |

---

## 风险 · 合规 · 安全与隐私（非法律意见）

- **授权过宽**：家目录整盘授权 → 敏感文件进模型上下文；宜专用工作夹。
- **不可逆写操作**：批量删除/覆盖；要 diff、回收站、Plan 模式检查点。
- **模式混淆**：误在 Chat 模式期待 Work 级文件交付；或反之。
- **VM/磁盘占用**：Cowork 等本地 VM 体积与 ZTNA/DNS 冲突（社区反馈）。
- **生态锁定**：深度绑定 M365 / 飞书 / 钉钉后迁移成本高。
- **用量不可预测**：Copilot Credits、Credits 池需 admin 预算与 `/cost` 类监控。

---

## 落地碎片（无先后）

- 先问：**这一次交付物**是什么格式、截止何时、输入在哪（文件夹 vs 套件内文档）。
- 再问：数据能否出租户/本机；决定 **Cowork 本地夹** vs **Copilot Cowork 云** vs **Manus 沙箱**。
- 团队重复流程成熟后，评估 [workspace-agent.md](workspace-agent.md) 而非无限加长 Work 会话 prompt。
- 工程师写代码 → [coding.md](../coding/coding.md)；不要强行用 Cowork 替代 Codex/Cursor。

---

## 行业注记（快变 · 2026）

> 季度复审区；框架段不依赖本节数字。

| 日期 | 事件 | 来源层级 |
|------|------|----------|
| 2026-01 | Anthropic 发布 Claude Cowork | T0/T1 |
| 2026-06-16 | Microsoft Copilot Cowork GA 全球 | T0 |
| 2026-07~10 | OpenAI ChatGPT Work rollout（GPT-5.6） | T0/T1 |
| 2026-03~06 | 腾讯 WorkBuddy 发布 / Enterprise Workspace | T0/T1 |
| 2026-08-03 | 阿里 QwenWork 中国公测 | T0 |
| 2026-08-25 | 字节 Doubao Work + 飞书深度集成 | T1 |
| 2026-08-25 | Claude Chat 与 Cowork **记忆系统合并** | T1 |

**中国桌面访问（单源 T1，待互证）**：36氪引第三方称 2026-06 桌面 AI 办公 agent 合计访问 6000 万+，WorkBuddy 约 2097 万居首——作趋势参考，不作份额定论。

**Copilot Cowork 增量（多源 T1）**：底层使用 Anthropic Claude 模型 + Microsoft Work IQ；用量计费 Copilot Credits。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 区域 | 一句话（据公开页面归纳） | URL |
|------|------|------|--------------------------|-----|
| **Claude Cowork** | A | 全球 | Claude Code 同源 harness；本地夹 + MCP/Skills/Plugins | [claude.com/docs/cowork/overview](https://claude.com/docs/cowork/overview) |
| **ChatGPT Work** | A/B | 全球 | 长任务 + 连接器 + 云浏览器；替代已下线 ChatGPT agent | [openai.com/index/chatgpt-for-your-most-ambitious-work/](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) · [Help](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) |
| **Copilot Cowork** | B/C | 全球 | 2026-06-16 GA；M365 云 · Work IQ；Copilot Credits 计费 | [microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/) |
| **Gemini Enterprise（App）** | B | 全球 | 长运行 agent、Projects 协作 | [cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise) |
| **Notion Agent** | A | 全球 | On-demand 多步（~20 分钟）；Custom Agents → workspace-agent | [notion.com](https://www.notion.com/) |
| **Manus AI** | B | 全球 | 每任务 cloud VM；通用交付 PPT/站点/报告；有 API | [manus.im/docs/introduction/welcome.md](https://manus.im/docs/introduction/welcome.md) |
| **WorkBuddy** | A/C | 中国 | 桌面 agent 工作站；Craft/Plan/Ask；Team Credits | [tencentcloud.com/techpedia/145619](https://www.tencentcloud.com/techpedia/145619?lang=en) |
| **QwenWork（千问办公）** | C | 中国 | 整合 QoderWork + MuleRun + Wukong；2026-08 公测 | [alibabagroup.com/en-US/document-2021039099929952256](https://www.alibabagroup.com/en-US/document-2021039099929952256) |
| **Doubao Work（豆包工作）** | C | 中国 | 2026-08-25 发布；飞书账号级；组织上下文继承飞书权限 | 见官方发布稿 |
| **Devin / Codex / Cursor Agent** | D | 全球 | 软件工程 | [coding.md](../coding/coding.md) |
| **Coworker（Accomplish）、Eigent** | E | 全球 | 开源本地 Cowork | [agent-for-desktop.md](agent-for-desktop.md) |

**团队共享 playbook** → [workspace-agent.md](workspace-agent.md)（OpenAI Workspace Agents、Notion Custom Agents 等）。

### 对比与测评（第三方；观点非官方）

- TechCrunch · Claude Cowork 扩平台：https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/
- HN · ChatGPT Work 模式讨论：https://news.ycombinator.com/item?id=48849059
- 36氪 · 中国 AI 办公整合：https://www.36kr.com/p/3887715461003777

---

## 延伸阅读 · 站内外

**站内**

- IM 协作面：[ai-employee.md](ai-employee.md)
- 簇边界（skills）：[`skills/knowledge-block/references/work-agent-cluster.md`](../../skills/knowledge-block/references/work-agent-cluster.md)
- 团队 playbook：[workspace-agent.md](workspace-agent.md)
- 本机执行面：[agent-for-desktop.md](agent-for-desktop.md)
- 沙箱：[agent-sandbox.md](agent-sandbox.md)