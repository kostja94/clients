# 桌面智能体（Agent on Desktop）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Agent on desktop / 桌面智能体**——运行在桌面应用或本机运行时内、能按授权读写本地文件或在 GUI 上演进多步任务的 Agent；验收以**端点类型（本机夹 vs 云端 VM）、授权范围与 GUI 成功率**为主。本页为 **桌面 Agent 产品 SSOT**（完整 URL 表仅此一处）；知识工作委派·交付物 → [work-agent.md](work-agent.md)；技能生态 → [agent-skills.md](agent-skills.md)；AI 浏览器 → [browser.md](browser.md)。

**材料范围**：公开产品介绍（Anthropic、Simular、Floatboat、Accomplish、Eigent、Bytebot、Poly.app 等）、行业媒体与评测摘要、开发者社区讨论。**未**把 Alignify 站内 Tools 正文 JSON 当作独立事实来源。网摘整理日期 **2026-05-13**。

**站内对照**：**待**上线 · slug **`agent-for-desktop`**

**站内相邻**：[ai-employee.md](ai-employee.md) · [work-agent.md](work-agent.md) · [agent-skills.md](agent-skills.md) · [browser.md](browser.md) · [multi-agent.md](multi-agent.md)

---

## 与相邻 slug 分流

| 维度 | **`agent-for-desktop`（本页）** | **`ai-employee`** | **`work-agent`** | **`agent-skills`** | **`browser`** | **`multi-agent`** |
|------|-------------------------------|-------------------|------------------|---------------------|--------------|-------------------|
| **典型买家问题** | 「Agent 怎么在桌面操作我的文件？」 | 「在 Slack 里 @ 一个共享同事干活」 | 「怎么委派 deck/报告/整理文件夹？」 | 「Agent 怎么扩展能力/接工具？」 | 「要不要换 AI 浏览器上网？」 | 「多 Agent 怎么分工协作？」 |
| **核心能力** | 本机文件授权与 GUI 操作 | IM 频道协作与 thread 交活 | 成果导向多步委派与交稿 | MCP 服务器、技能包 | 浏览器内 AI 摘要与自动化 | 编排框架、任务路由 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Agent on desktop / 桌面智能体**：运行在**桌面应用或本机运行时**内的智能体，能按授权**读取、写入本地文件**或在**本机显示器级界面**上演进多步任务；与「网页里聊天、主要靠用户上传粘贴」的流程区分。
- **Cloud-only assistant（云端对话型助手）**：主要交互发生在浏览器或服务端会话中；若无显式集成本地目录或连接器，则**不**自动拥有「整盘文件系统」视角。
- **Computer use / GUI agent**：通过视窗、键鼠或无障碍 API 操作应用；可部署在**本机**或**远程虚拟机**里（Type A vs C，见 §形态谱系）。
- **Cloud-hosted virtual desktop（云端虚拟桌面上的智能体）**：智能体操作**供应商托管的隔离桌面**；与「直接操作你笔记本 `~/Documents`」的**本机**叙事不同。
- **Local-first file access（本地文件优先）**：经 **OS 权限**或应用内**显式选夹**授权后，对指定目录做读写。
- **Human-in-the-loop / 审批**：敏感操作前暂停确认；企业场景常与**策略、审计、文件夹范围**一起出现。
- **Desktop AI Agent / AI Coworker / Agentic Workspace**：检索常用英文化品类词——强调本地客户端、文件系统读写或多步任务链；**Agentic Workspace** 为产品与叙事词，**不等于**已实现深度本机挂载，须看是否真有本地运行时与权限模型。

---

## 专题对照 / 扩展定义

**本机 vs 云端聊天 vs 云端 VM**（术语见 §词汇锚点；产品规格见 §外链索引）：

| 维度 | **本机桌面智能体（Type A/B）** | **纯云端聊天** | **云端虚拟桌面（Type C）** |
|------|-------------------------------|----------------|------------------------------|
| **运行端点** | 用户 PC / Mac 上的客户端 | 远程模型 + 浏览器 | 供应商提供的隔离 VM |
| **本地文件** | 经授权直接访问用户选定目录 | 依赖上传、连接器或端侧插件 | 操作**远端盘** |
| **典型风险焦点** | 本机数据外泄、误删、越权路径 | 上下文上传范围、账号安全 | VM 侧隔离、供应商侧驻留数据 |

---

## 问题域（为何会出现这类产品）

- **知识工作留在文件系统里**：报告、表格、下载目录、项目仓在本地堆叠，用户希望「指向文件夹就做完」而非反复拖拽上传。
- **多步任务与异步执行**：整理、对账、跨应用汇总适合 **agent 循环**；与单轮 **chat** 互补。
- **与「只在云端」的张力**：组织关心**数据驻留**与**最小暴露面**；本机授权夹或企业托管桌面各走一条路线。
- **benchmark 推动**：**OSWorld**、**GAIA** 等强调**真实环境操作**，厂商用「接近或超过人类操作成功率」叙事推动 **computer-use** 品类可见度。
- **「聊天盲区」**：基于聊天界面的 Agent 看不到本地文件系统——桌面 Agent 以文件系统级授权解决「Agent 能自主定位、读取和操作本地文件」这一前提问题。

---

## 能力栈（概念拆分，非厂商功能表）

- **目录级读写**：在授权范围内列目录、读格式、批量重命名、生成报告。
- **应用与 GUI 自动化**：启动应用、填表、点击流程；部分产品与 **浏览器控制**、**终端/脚本**一起出现。
- **连接器与混合路径**：本机文件 + **SaaS**（邮件、日历、云盘）由产品定义。
- **并行与长时任务**：队列、计划任务、移动设备触发本机继续跑（视产品实现）。
- **隔离执行**：部分实现将 **shell/代码**放入 **VM 或沙箱**，与「直接改用户文档」分层（见 [agent-sandbox.md](agent-sandbox.md)）。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | macOS/Windows 客户端；本地文件夹 + 桌面工作流 | Local desktop agent / Cowork | Floatboat、Claude Cowork、Accomplish |
| **B** | AI 文件浏览器子型；文件搜索/整理/摘要，非全桌面操控 | File browser agent / Cursor for Files | Poly.app |
| **C** | 隔离 VM、远程桌面上的 GUI 自动化 | Remote / cloud desktop agent | Bytebot、Simular Sai |
| **D** | 终端里长时任务、仓库级操作 | CLI / coding agent | 见 [coding.md](../coding/coding.md) |
| **E** | 浏览器 + 本机扩展桥接 | Browser + local extension | 边界取决于扩展权限 |
| **F** | 团队频道 / IM 驱动的多 Agent 协作 | Agent workspace / team daemon | 主战场在 [multi-agent.md](multi-agent.md) L3 |

**Type A vs C**（体验均「能操作电脑」，底层不同）：A 为**宿主本机授权夹**；C 为**容器/VM 内磁盘**——对照见 §外链索引 Bytebot/Simular 条目。

---

## 风险 · 合规 · 安全与隐私（外部框架可对照，非法律意见）

- **权限与横向移动**：获准的文件夹一旦过宽，敏感表、密钥、令牌可能进入模型上下文；**最小权限**与**分类分级**是基础动作。
- **不可逆写操作**：批量改名、删除、覆盖需 **diff/回收站/备份**策略。
- **数据出境与处理条款**：即便文件在本地磁盘，推理是否经云端模型、日志与**保留时长**仍以各服务商 **ToS/DPA** 为准。
- **供应链与冒充**：与本机结合的插件、**connector**、第三方 **MCP** 扩大攻击面。
- **用工与自动化条款**：对部分网站或内部系统的自动操作可能触及 **服务条款** 或内规。

---

## 落地碎片（无先后）

- 先问清：要的是「**摸得到本机某几个夹**」还是「**云端里永远在线的一台干净机器**」——对照见 §专题对照。
- **Cowork / WorkBuddy 等知识工作委派**的产品地图、Chat vs Work 分流——见 [work-agent.md](work-agent.md)；本页只关心**执行面**（本机夹 / GUI / VM）。
- 为 **Cowork 类**产品单独划**工作夹**，避免把家目录整盘授权给 agent。
- 与 [agent-skills.md](agent-skills.md) 交叉：技能包描述「怎么做」；**桌面智能体**解决「在哪台机器、对哪些文件真的动手」。
- 与 [multi-agent.md](multi-agent.md) 交叉：Eigent/Floatboat 等可带多 Agent 叙事，但**团队 org 层与 L3 Workspace** 以 multi-agent 为准；本页主战场是**单人本机**闭环。
- **检索与品牌**：英文圈产品名相近易混（**bot**/**boat**/**byte** 等拼写）；以 **注册域名与 trademark 归属**为准。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **Floatboat** | A | **Mac/Windows 客户端** AI Workspace；本机文件与本地软件、模块化工作区、内置浏览器 | [floatboat.ai](https://floatboat.ai/) |
| **Poly.app** | B | YC S22，AI 智能文件浏览器（「Cursor for Files」）；Polyembed-v1 跨格式搜索与整理；**≠ PolyBuzz** | [poly.app](https://poly.app/) |
| **Claude Cowork** | A | Anthropic 知识工作 Work Agent；本机授权夹 + 桌面客户端——**品类地图**见 [work-agent.md](work-agent.md) | [claude.com/docs/cowork/overview](https://claude.com/docs/cowork/overview) |
| **Accomplish** | A | 开源（MIT）本机 computer-use agent；BYOK/Ollama；用户选择可见文件夹 | [accomplish.ai](https://www.accomplish.ai/) |
| **Eigent** | A | 开源 Cowork desktop 叙事；本地化部署与多智能体 | [eigent.ai](https://www.eigent.ai/) |
| **Bytebot** | C | 开源（Apache 2.0）；**沙箱 Linux 桌面（Docker）** 内操纵屏幕/键盘；**非**宿主家目录 | [bytebot.ai](https://www.bytebot.ai/) |
| **Simular（Sai / Simular Pro）** | C | **Sai** 多为**云端私有虚拟桌面**；与 Type A 分列 | [simular.ai](https://www.simular.ai/) |

### 对比与测评（第三方；观点非官方）

社区与科技媒体中较常见的对比轴包括：**本机夹授权 vs 云端 VM**（Type A vs C）、**是否必须桌面应用**、**与 Claude Code / Copilot 的分工**、以及 **benchmark 分数能否迁移到个人 messy 文件夹场景**。「**local-first**」宣传需细读——模型推理是否仍经云端、哪些元数据会进日志。**Computer-use** 在用户真实桌面上仍可能受制于权限弹窗、反自动化策略与异形 UI。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **Anthropic 官方**：[Claude Cowork 产品介绍](https://website.claude.com/product/cowork)
- **帮助中心**：[Getting started（Local agent / Cowork）](https://support.claude.com/en/articles/13345190-getting-started-with-local-agent-mode)

**站内**

- 委派交付物：[work-agent.md](work-agent.md)
- IM 协作面：[ai-employee.md](ai-employee.md)
- 技能与 MCP：[agent-skills.md](agent-skills.md)
- 浏览器侧 AI：[browser.md](browser.md)
- 远程浏览器：[headless-browser.md](../web-data/headless-browser.md)