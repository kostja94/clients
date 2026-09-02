# 深度搜索报告 — Work Agent（办公/知识工作智能体）产品地图

> **检索基准日**：2026-09-02  
> **时间范围**：2026 年以来（含 2025 末起源产品）  
> **检索约束**：按 web-deep-search-spec v1.4，未读取本地客户文档  
> **Loop 轮次**：6 轮  
> **来源统计**：Tier 0 18 · Tier 1 12 · Tier 2 5  
> **置信度摘要**：Work Agent 作为 2026 品类已形成全球「三巨头 + 中国三巨头 + 垂直/开源」格局；核心定义与代表产品均有官方互证，市场份额数据仅中国桌面访问量为单源 Tier 1 报道。

---

## 1. 执行摘要

**Work Agent（工作智能体）** 在 2026 年指：用户描述**工作成果**（deck、报表、整理文件夹、跨应用流程），系统**自主规划多步任务**、调用工具/读写文件/浏览网页，在沙箱或授权范围内执行，并交回**可交付物**——而非一次性聊天回答。Anthropic [Claude Cowork](https://claude.com/docs/cowork/overview)、OpenAI [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) 与 Microsoft [Copilot Cowork](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/) 构成全球参照系；中国侧腾讯 **WorkBuddy**、阿里 **QwenWork（千问办公）**、字节 **Doubao Work（豆包工作）** 在 2026 年 7–8 月完成产品线整合，与飞书/钉钉/企业协作深度绑定。

**增量要点**：① TechCrunch 与 HN 均指出品类由 Claude Code/Codex 的 agent 架构「外溢」到非编程知识工作（Cowork 内测故事：腾讯产品经理受 Cowork 启发周末搭出 WorkBuddy 原型——**单源**，见 36氪）。② Microsoft Copilot Cowork 底层使用 Anthropic Claude 模型（Opus/Sonnet）+ 自研 Cowork 1，以 **Work IQ** 读取 M365 全量工作图谱，按 **Copilot Credits** 用量计费——与 Claude Cowork 的 flat 订阅形成商业模型分歧。③ 社区反响偏实用主义：知识工作者高度依赖 Cowork/Work 做文档与 MCP 集成，同时抱怨 Chat vs Work 模式混淆、Cowork macOS VM 占用约 10GB、企业 MCP 锁定。

---

## 2. 搜索过程摘要

| 轮次 | 新增 query 示例 | 本轮增量发现 |
|------|----------------|--------------|
| R1 | `site:claude.com Cowork overview` | 建立 Claude Cowork Tier 0 定义：delegating 模式、子 agent、MCP/Skills |
| R1 | `site:openai.com ChatGPT Work` | ChatGPT agent 已下线，由 Work + Workspace Agents 接替 |
| R1 | `Tencent WorkBuddy Enterprise AI work agent 2026` | 腾讯 WorkBuddy 桌面 agent 工作站定位 |
| R2 | `site:microsoft.com Copilot Cowork` | Copilot Cowork 2026-06-16 GA，Copilot Credits 计费 |
| R2 | `Doubao Work Feishu ByteDance 2026` | 豆包工作 2026-08-25 发布，飞书账号级集成 |
| R2 | `site:alibabagroup.com QwenWork` | 千问办公 2026-08-03 公测，整合 QoderWork/MuleRun/Wukong |
| R3 | `site:techcrunch.com Claude Cowork` | Tier 1：Cowork 扩至 web/mobile；与 coding agent 战争外溢 |
| R3 | `Manus AI agent deliverables site:manus.im` | Manus 云端 sandbox 通用 work agent |
| R4 | `Salesforce Agentforce autonomous` | 企业 CRM 垂直 work agent 平台 |
| R5 | `site:news.ycombinator.com ChatGPT Work` | HN：模式混淆、VM 体积、知识工作者采用率 |
| R6 | `work agent 办公智能体 36氪 WorkBuddy` | 中文：三国杀格局、桌面访问量 WorkBuddy 领先（单源） |

---

## 3. 搜索意图拆解

| 意图 | 检索词示例 | 结果状态 |
|------|------------|----------|
| 概念基线 Q1：Work Agent 是什么 | `work agent AI knowledge work delegated deliverables` | 已覆盖 |
| 概念基线 Q2：有哪些类型 | `Claude Cowork vs Copilot Cowork vs ChatGPT Work` | 已覆盖 |
| 概念基线 Q3：知名产品/方案 | 各厂商 `Cowork`/`WorkBuddy`/`QwenWork`/`Doubao Work` | 已覆盖 |
| 时间线与 GA 状态 | `Copilot Cowork generally available June 2026` | 已覆盖 |
| 中文语境 | `36氪 AI办公 WorkBuddy 豆包 千问` | 已覆盖 |
| 社区反响 | `site:news.ycombinator.com Cowork Work` | 已覆盖 |
| 开源/本地替代 | `accomplish-ai coworker github eigent` | 已覆盖 |

---

## 4. 核心发现（多源验证）

### 4.1 Work Agent 是什么

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| 用户描述**成果**，系统**规划并执行多步任务**，交回**文件/制品**，而非仅对话 | [Claude Cowork Overview](https://claude.com/docs/cowork/overview) T0 | [OpenAI ChatGPT Work 公告](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) T0 | 已确认 |
| 与「Chat 模式」对立：Chat = 思考/对话；Work/Cowork = **委派（delegating）** | [Claude Academy: What is Cowork](https://academy.claude.com/courses/introduction-to-claude-cowork/what-is-cowork) T0 | [OpenAI Help: ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) T0 | 已确认 |
| 典型执行环境：云端/本地沙箱、授权文件夹、MCP 连接器、子 agent 并行 | [Anthropic Cowork Architecture](https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview) T0 | [Microsoft Copilot Cowork 产品页](https://www.microsoft.com/en-us/microsoft-365-copilot/cowork) T0 | 已确认 |
| 与 **Personal Agent**（跨日记忆、生活连续性）边界：Work Agent 优化**单次/可重复工作交付物** | [TechCrunch Cowork 扩平台](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/) T1 | [Manus 官方文档](https://manus.im/docs/introduction/welcome.md) T0 | 很可能 |

**叙述**：2026 年「Work Agent」不是新的模型能力，而是 **Agent 架构 + 沙箱执行 + 连接器** 面向**知识工作者**的产品化命名。Anthropic 明确将 Cowork 定位为 Claude Code 同款 agent 架构的「非终端版」；OpenAI 将已弃用的 ChatGPT agent 模式收敛为 **ChatGPT Work**（个人委派）与 **Workspace Agents**（团队可复用流程）。

---

### 4.2 Work Agent 有哪些类型

**分类依据**：综合 Anthropic、OpenAI、Microsoft、Google 官方文档与 TechCrunch 对比稿，按 **部署边界 × 用户范围 × 集成栈** 划分（非自创 taxonomy）。

| 类型 | 特征 | 典型场景 | 代表产品 | 来源 |
|------|------|----------|----------|------|
| **A. 个人委派型（Outcome-first）** | 一人描述目标；云/桌面沙箱；交回 deck/表格/报告 | 整理文件夹、做 board deck、填表、研究综述 | Claude Cowork、ChatGPT Work、WorkBuddy、QwenWork、Doubao Work、Manus | T0 官方 |
| **B. 平台嵌入型（Suite-native）** | 跑在 M365 / Workspace / 钉钉飞书内；读取组织工作图谱 | 跨邮件+日历+文档的端到端流程 | Copilot Cowork、Gemini Enterprise App、Doubao Work+Feishu、QwenWork+DingTalk | T0/T1 |
| **C. 团队/workspace 可复用型** | 共享 agent、定时/API 触发、RBAC | 销售简报、采购审批、每周报告 | OpenAI Workspace Agents、Notion Custom Agents、Gemini Enterprise Agent Platform | T0 |
| **D. 垂直领域型** | 高阶目标绑定特定工种/系统 | 软件工程、CRM 服务 | Devin、Salesforce Agentforce | T0 |
| **E. 开源/本地优先型** | BYOK 或本地模型；数据不出机 | 敏感文档、合规场景 | Coworker (Accomplish)、Eigent | T0 GitHub |

**易混淆点**：
- **Cowork vs Code/Codex**：前者面向知识工作交付物，后者面向代码库（OpenAI/Anthropic 均三分：Chat / Work(Cowork) / Code(Codex)）。
- **Work Agent vs Workspace Agent**（OpenAI 术语）：Work = 个人长任务；Workspace Agents = 团队共享、可调度、可 API 触发。
- **Copilot「Agent mode」vs Copilot Cowork**：Agent mode 为 Word/Excel 内多步操作；Cowork 为跨 M365 应用的长运行 agentic 系统（Microsoft 365 Blog T0）。

---

### 4.3 知名产品 / 代表方案

#### 4.3.1 全球平台型（2026 主力）

| 产品 | 厂商 | 运行位置 | 状态（检索日） | 定位摘要 | 来源 |
|------|------|----------|----------------|----------|------|
| **Claude Cowork** | Anthropic | Desktop（本地文件夹+VM）+ Cloud beta（web/mobile） | 2026 持续扩展；插件/记忆与 Chat 打通 | 非技术用户可用的 Claude Code 式委派；MCP/Skills/Plugins | [Overview](https://claude.com/docs/cowork/overview) T0；[TechCrunch 2026-01-12](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/) T1 |
| **ChatGPT Work** | OpenAI | Web/mobile/desktop；云 Work + 桌面本地文件夹 | 2026 起逐步 rollout；替代 ChatGPT agent | 长时多步任务；GPT-5.6；内置 browser；Scheduled Tasks | [OpenAI 公告](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) T0；[Help Center](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) T0 |
| **Workspace Agents** | OpenAI | 云端；ChatGPT Business/Enterprise/Edu | GA | 团队共享、Slack/API 触发、Codex 驱动 | [OpenAI 公告](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) T0 |
| **Copilot Cowork** | Microsoft | M365 云；Work IQ 上下文 | **2026-06-16 GA** 全球 | 跨 Outlook/Teams/Word/Excel/SharePoint 多步执行；**Copilot Credits** 用量计费 | [M365 Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/) T0 |
| **Gemini Enterprise**（App + Agent Platform） | Google | Google Cloud 沙箱；Workspace 连接器 | 2026 持续 GA 功能 | 长运行 agent（最长约 7 天）；Projects 人机协作；agent-to-agent | [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise) T0 |
| **Notion Agent / Custom Agents** | Notion | Notion workspace + 连接器 | Custom Agents 2026-02-24 发布 | 个人 on-demand agent（约 20 分钟自治）+ 团队 24/7 触发式 Custom Agents | [Notion 3.3 Release](https://www.notion.com/releases/2026-02-24) T0 |

#### 4.3.2 中国生态型（2026 年 7–8 月整合潮）

| 产品 | 厂商 | 协作栈 | 状态 | 定位摘要 | 来源 |
|------|------|--------|------|----------|------|
| **WorkBuddy** | 腾讯 / 腾讯云 | 腾讯文档、企业 IM；可接 Slack/Telegram 远程触发桌面 | 2026-03 正式发布；Enterprise Workspace 2026-06 | 桌面 AI agent 工作站；Craft/Plan/Ask 权限模式；Team 席位+Credits | [Tencent Cloud Techpedia](https://www.tencentcloud.com/techpedia/145619?lang=en) T0；[36氪](https://www.36kr.com/p/3887715461003777) T1 |
| **QwenWork（千问办公 / Qianwen Office）** | 阿里 | 钉钉深度嵌入；独立 web/PC | **2026-08-03** 中国公测；国际 beta 跟进 | 整合 QoderWork + MuleRun + Wukong；Qwen3.8；订阅+Credits | [Alibaba Group 新闻稿](https://www.alibabagroup.com/en-US/document-2021039099929952256) T0；[TechNode Global](https://technode.global/2026/08/26/alibaba-qwenwork-international-public-beta/) T1 |
| **Doubao Work（豆包工作）** | 字节跳动 | **飞书账号级集成** | **2026-08-25** 发布 | 独立桌面客户端；继承飞书聊天/文档/日程权限；30 天订阅体验 | [Caixin Global](https://www.caixinglobal.com/2026-08-25/bytedance-consolidates-ai-office-tools-around-doubao-102477744.html) T1；[TechNode](https://technode.com/2026/08/25/bytedance-launches-doubao-work-with-feishu-integration-and-30-day-free-access/) T1 |

#### 4.3.3 通用云端 / 垂直 / 开源

| 产品 | 类型 | 说明 | 来源 |
|------|------|------|------|
| **Manus AI** | A 类通用云端 | 每任务独立 sandbox VM；交付 PPT/网站/报告；有 API | [manus.im/docs](https://manus.im/docs/introduction/welcome.md) T0 |
| **Devin** | D 类（软件工程） | 自主规划/写测/部署代码；Managed Devins 并行 | [cognition.com](https://cognition.com/) T0 |
| **Salesforce Agentforce** | D 类（CRM/服务） | Atlas Reasoning Engine；Flow/Apex 动作 | [salesforce.com/agentforce](https://www.salesforce.com/agentforce/) T0 |
| **Coworker**（原 Accomplish） | E 类开源 | 本地 Electron 桌面 agent；BYOK/Ollama；MIT | [GitHub accomplish-ai/coworker](https://github.com/accomplish-ai/accomplish) T0 |
| **Eigent** | E 类开源 | CAMEL-AI 多 agent 桌面；Developer/Browser/Document 分工 | [GitHub eigent-ai/eigent](https://github.com/eigent-ai/eigent) T0 |

**份额/采用度**：W3Techs 类统计**不适用**此品类。中国桌面访问：36氪引第三方称 2026-06 桌面 AI 办公 agent 合计访问 6000 万+，WorkBuddy 约 2097 万居首——**单源 Tier 1，待进一步互证**。

---

### 4.4 时间线（精选）

| 日期 | 事件 | 来源 |
|------|------|------|
| 2026-01-12 | Anthropic 发布 Claude Cowork（research preview） | TechCrunch T1 |
| 2026-01-30 | Cowork 插件/Plugins 上线 | TechCrunch T1 |
| 2026-03 | 腾讯 WorkBuddy 正式发布 | 36氪 T1 |
| 2026-06-05 | WorkBuddy Enterprise AI Workspace 发布 | 36氪 T1 |
| 2026-06-16 | **Microsoft Copilot Cowork GA** | Microsoft 365 Blog T0 |
| 2026-07-07 | Claude Cowork 扩至 web/mobile（Max 等） | TechCrunch T1 |
| 2026-07-10 | OpenAI 发布 ChatGPT Work（GPT-5.6） | 多家 T1 对比稿 |
| 2026-08-03 | 阿里 QwenWork 中国公测 | Alibaba T0 |
| 2026-08-25 | 字节 Doubao Work + 飞书深度集成发布 | Caixin / TechNode T1 |
| 2026-08-25 | Claude Cowork 与 Chat **记忆系统合并** | TechCrunch T1 |

---

## 5. 实体关系（简述）

```
模型/Agent 架构层          产品/work agent 层              协作/数据层
─────────────────────────────────────────────────────────────────
Anthropic Claude Agent SDK → Claude Cowork ──→ 本地文件夹 / MCP / M365 连接器
OpenAI Codex/Agents       → ChatGPT Work ──→ Connectors / Cloud Browser
                         → Workspace Agents → Slack / API / 团队 RBAC
Microsoft + Anthropic    → Copilot Cowork ─→ Work IQ (M365 全图谱)
Google Gemini            → Gemini Enterprise → Workspace / M365 连接器
腾讯 CodeBuddy 系         → WorkBuddy ────────→ 腾讯文档 / OAuth 工具
阿里 Qwen                → QwenWork ─────────→ 钉钉
字节 Doubao              → Doubao Work ──────→ 飞书
Butterfly Effect         → Manus ────────────→ 云端 VM sandbox
```

---

## 6. 增量信息

### 6.0 增量对照表（多源 diff）

| 增量主张 | 相对 Tier 0 的新增点 | 首见来源 | 互证来源 | 验证结果 | 置信度 |
|---------|---------------------|---------|---------|---------|--------|
| Copilot Cowork 底层用 Claude 模型 | Microsoft 产品页未强调模型供应商 | [Substack 分析](https://digitalstrategyai.substack.com/p/copilot-cowork-vs-claude-cowork) T1 | [cowork.tips 对比](https://www.cowork.tips/blog/claude-cowork-vs-copilot-cowork) T1 | 很可能（多源 T1） | 很可能 |
| WorkBuddy 原型受 Cowork 启发、周末搭建 | 腾讯官方 techpedia 未写起源故事 | [36氪](https://www.36kr.com/p/3928009738950530) T1 | 腾讯云负责人口径（36氪转引） | 很可能（单源细节） | 很可能（单源） |
| ChatGPT agent 已完全由 Work 替代 | Help 中心写明 | [OpenAI Help](https://help.openai.com/en/articles/11752874-chatgpt-agent) T0 | HN 用户反馈 agent 菜单消失 | 已确认 | 已确认 |
| Cowork macOS 默认下载 ~10GB VM | 官方未在 overview 强调体积 | HN [#47218288](https://news.ycombinator.com/item?id=47218288) T2 | Anthropic 员工 Felix 回复架构理由 T0 级回复 | 已确认（体积）+ 官方解释（原因） | 已确认 |
| 中国三巨头 2026-07~08 组织整合 | 各官方稿分散 | 36氪 / Caixin / Alibaba | TechNode / hellochinatech | 已确认 | 已确认 |

### 6.1 已验证增量信息

- **计费模型分歧**：Copilot Cowork = M365 Copilot 许可 + Copilot Credits（约 $0.01/credit，任务复杂度定价）；Claude Cowork 含在 Claude 付费计划；WorkBuddy/QwenWork 多为 **席位 + Credits 池**（hellochinatech T1 指出三家均未转向 pure outcome-based billing）。
- **HN 采用画像**：部分知识工作者（L&D、非技术团队）报告 2 个月几乎不用 Word/Excel 原生编辑，而以 Cowork/Work + MCP 为主——**观点类 T2**。
- **模式混淆**：Chat vs Work/Cowork 三分界面被 HN 多次批评为 UX 负担（[HN #48849059](https://news.ycombinator.com/item?id=48849059) T2）。

### 6.2 未通过验证的传闻

| 传闻/主张 | 来源 | 拒绝原因 |
|----------|------|---------|
| 「Poly.app / Floatboat 为 2026 主流 work agent」 | 本地笔记常见提及 | 本轮权威检索无 Tier 0/1 产品页互证；**未纳入产品地图** |
| Manus 已被 Meta 完成收购并运营 | 部分二级博客 | CNBC 等称 2026-04 中国监管阻断；Manus 仍独立运营——需单独事件追踪，本报告不列为当前 work agent 主力 |

### 6.3 权威媒体解读

- TechCrunch（2026-07）：「coding agent wars」外溢到办公室——Cowork 扩平台标志 agent 从开发者扩散到 everyday business work。
- 36氪（2026）：中国 AI 办公进入「堑壕战」，桌面入口 + 组织数据（飞书/钉钉/腾讯文档）是差异化核心，而非模型聊天能力。

### 6.4 社区与舆论反响（Tier 2）

- **支持**：Cowork/Work 对 Gmail/Calendar/Jira/Google Docs MCP 集成、多步表单填写、后台长任务评价高。
- **顾虑**：① Chat/Work 边界不清；② Cowork VM 磁盘占用与 ZTNA/DNS 冲突；③ 企业环境 MCP 锁定；④ Work 模式 cloud browser 对**已登录页面**控制能力弱于旧 agent（OpenAI Developer Community T2）。

### 6.5 争议与风险

- **安全**：Cowork 沙箱 vs 本地文件挂载边界；WorkBuddy Default/Full Access 模式；企业需 RBAC + 审批检查点（各 T0 均强调 human-in-the-loop）。
- **锁定**：Copilot Cowork 强依赖 M365；Doubao Work 强依赖飞书；QwenWork 强依赖钉钉生态。
- **成本可预测性**：Copilot Credits 用量随任务波动；管理员需 `/cost`、Cost Management dashboard（Microsoft Learn T0）。

### 6.6 竞品与行业对照

| 维度 | Claude Cowork | ChatGPT Work | Copilot Cowork | WorkBuddy | Doubao Work | QwenWork |
|------|---------------|--------------|----------------|-----------|-------------|----------|
| 核心数据 | 授权本地文件夹 + MCP | Connectors + 云浏览器 | M365 Work IQ | 本地文件夹 + OAuth 工具 | 飞书组织上下文 | 钉钉 + 桌面/云 |
| 计费 | Claude 订阅 | 计划内用量 | Credits 用量 | 席位+Credits | 订阅（细节待公布） | 订阅+Credits |
| 团队/agent 目录 | Enterprise RBAC | Workspace Agents（独立产品） | M365 管理台 | Team Admin Console | 企业版（飞书权限继承） | 企业级（钉钉百万客户） |

### 6.7 中文语境

- **36氪 / 晚点口径**：2026 夏，腾讯、字节、阿里「重做 Office」——不是 AI 嵌入旧套件，而是以 **Agent 为默认工作入口**。
- **产业判断（36氪引 IDC+腾讯云）**：至 2030 年 95% 工作角色将被重新定义——**行业预测，非已发生事实**。

---

## 7. 分歧与待核实

| 项 | 说法 A | 说法 B | 建议 |
|----|--------|--------|------|
| QwenWork 对外名称 | Alibaba 官方用 **QwenWork** | 中文媒体多用 **千问办公 / Qianwen Office** | 同一产品；引用时注明中英文 |
| Copilot Cowork GA vs Preview | Microsoft 2026-06-16 称 GA | 部分评论称 enterprise rollout 至 Q3 | 以 Microsoft T0 GA 为准；企业落地节奏因租户而异 |
| 桌面访问量排名 | 36氪：WorkBuddy 2097 万/月 | 无第二独立统计源 | 作趋势参考，不作份额定论 |

---

## 8. 对用户问题的直接回答

### 8.1 Work Agent 是什么？

**Work Agent** 是 2026 年面向**知识工作交付**的 AI 产品品类：你给出目标（如「把这些资料做成 board deck」），系统在沙箱或授权范围内**自主分解、调用工具、读写文件/浏览网页**，最终返回**可编辑的成品**（文档、表格、幻灯片、报告等）。它与普通聊天机器人的分界是 **delegate vs chat**（Anthropic/OpenAI 官方用语），与 Personal Agent 的分界是 **交付物 vs 跨日生活连续性**。

### 8.2 有哪些类型？

见 **§4.2**：个人委派型、平台嵌入型、团队 workspace 型、垂直领域型、开源本地型五类。

### 8.3 有哪些知名产品 / 代表方案？

**全球**：Claude Cowork、ChatGPT Work、OpenAI Workspace Agents、Microsoft Copilot Cowork、Google Gemini Enterprise（含 Agent Platform）、Notion Agent/Custom Agents、Manus AI。  

**中国（2026 整合后的三巨头）**：腾讯 **WorkBuddy**、阿里 **QwenWork/千问办公**、字节 **Doubao Work/豆包工作**。  

**垂直**：Devin（软件工程）、Salesforce Agentforce（CRM/服务）。  

**开源本地**：Coworker（原 Accomplish）、Eigent。

---

## 9. 参考链接（按 Tier 排序）

### Tier 0 官方
- https://claude.com/docs/cowork/overview  
- https://claude.com/product/cowork  
- https://openai.com/index/chatgpt-for-your-most-ambitious-work/  
- https://openai.com/index/introducing-workspace-agents-in-chatgpt/  
- https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex  
- https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/  
- https://www.microsoft.com/en-us/microsoft-365-copilot/cowork  
- https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise  
- https://www.alibabagroup.com/en-US/document-2021039099929952256  
- https://www.tencentcloud.com/techpedia/145619?lang=en  
- https://www.notion.com/releases/2026-02-24  
- https://manus.im/docs/introduction/welcome.md  
- https://www.salesforce.com/agentforce/  
- https://cognition.com/  
- https://github.com/accomplish-ai/accomplish  
- https://github.com/eigent-ai/eigent  

### Tier 1 权威媒体
- https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/  
- https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/  
- https://www.caixinglobal.com/2026-08-25/bytedance-consolidates-ai-office-tools-around-doubao-102477744.html  
- https://technode.com/2026/08/25/bytedance-launches-doubao-work-with-feishu-integration-and-30-day-free-access/  
- https://technode.global/2026/08/26/alibaba-qwenwork-international-public-beta/  
- https://www.36kr.com/p/3887715461003777  
- https://www.cowork.tips/blog/claude-cowork-vs-copilot-cowork  

### Tier 2 补充（社区）
- https://news.ycombinator.com/item?id=48849059  
- https://news.ycombinator.com/item?id=47218288  
- https://news.ycombinator.com/item?id=49260452  

---

*本报告按 web-deep-search-spec v1.4 生成，检索日 2026-09-02，共 6 轮 loop。*
