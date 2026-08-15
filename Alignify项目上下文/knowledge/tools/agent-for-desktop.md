# 桌面智能体（Agent on Desktop）· 知识块（非线性笔记）

**材料范围**：公开产品介绍（Anthropic、[Simular](https://www.simular.ai/)、[Floatboat](https://floatboat.ai/)、[Accomplish](https://www.accomplish.ai/)、[Eigent](https://www.eigent.ai/)、[Bytebot](https://www.bytebot.ai/) 等）、行业媒体与评测摘要、开发者社区讨论；归纳「本机可操作文件 / GUI」「与纯云端对话的差异」「托管虚拟桌面型」等并列概念。品类检索词辨析曾对照竞品拆解中与**本主题**对齐的条目去重。**未**把 Alignify 站内 Tools 正文 JSON 当作独立事实来源。网摘整理日期 **2026-05-13**。补充：Poly.app（YC S22，AI 文件浏览器/智能体）加入品类对照。

**站内对照**：**待**上线 Tools 页时与 `slug` **`agent-for-desktop`**、`content/tools/*/*agent-for-desktop.json` 对齐；当前仅知识块占位。

**站内相邻**：[agent-skills.md](./agent-skills.md)（技能生态） · [browser.md](./browser.md)（AI 浏览器） · [multi-agent.md](./multi-agent.md)（多 Agent 编排）

## 与相邻 slug 分流

| 维度 | **`agent-for-desktop`（本页）** | **`agent-skills`** | **`browser`** | **`multi-agent`** |
|------|-------------------------------|---------------------|--------------|-------------------|
| **典型买家问题** | 「Agent 怎么在桌面操作我的文件？」 | 「Agent 怎么扩展能力/接工具？」 | 「要不要换 AI 浏览器上网？」 | 「多 Agent 怎么分工协作？」 |
| **核心能力** | 本机文件授权与 GUI 操作 | MCP 服务器、技能包、插件生态 | 浏览器内 AI 摘要与自动化 | 编排框架、任务路由 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Agent on desktop / 桌面智能体**：在讨论中常指运行在**桌面应用或本机运行时**内的智能体，能按授权**读取、写入本地文件**或在**本机显示器级界面**上演进多步任务；与「网页里聊天、主要靠用户上传粘贴」的流程区分。
- **Cloud-only assistant（云端对话型助手）**：主要交互发生在浏览器或服务端会话中；若无显式集成本地目录或连接器，则**不**自动拥有「整盘文件系统」视角，数据往往依赖用户**主动上传**或 **API 拉取云端仓库**。
- **Computer use / GUI agent**：通过视窗、键鼠或无障碍 API 操作应用；可部署在**本机**或**远程虚拟机**里，「是否算桌面智能体」取决于讨论语境是强调**端点**还是**能力形态**。
- **Cloud-hosted virtual desktop（云端虚拟桌面上的智能体）**：智能体操作的是**供应商托管的隔离桌面**（用户通过流式或远程会话使用），数据默认留在该环境；与「直接操作你笔记本 `~/Documents`」的**本机**叙事不同，但同属 **computer-use** 能力谱系。
- **Local-first file access（本地文件优先）**：经 **OS 权限**或应用内**显式选夹**授权后，对指定目录做读写；典型卖点是减少手工上传、支持批量整理与长任务。
- **Human-in-the-loop / 审批**：敏感操作前暂停确认；企业场景常与**策略、审计、文件夹范围**一起出现。
- **Desktop AI Agent（检索常用英文化品类词）**：强调 **本地应用客户端**、**文件系统读写**、「电脑级」多窗口与地面操作——与单次网页 **chat** 对照时常出现。
- **AI Coworker（检索常用）**：卖点是**多步任务链**、像同事一样推进与交付；可与 **desktop** 叠用，也可能以 Web/移动端触发，不一定等于「装了桌面exe」——以各产品形态为准。
- **Agentic Workspace（产品与叙事词）**：把 **Agent** 与工作区组件（浏览器、文件树、会话、连接器）放在一起设计的一类说法；常见于营销，**不等于**已实现深度本机挂载，须看是否真有本地运行时与权限模型。


## 专题对照 / 扩展定义

| 维度 | **本机桌面智能体**（常见讨论含义） | **纯云端聊天** | **云端虚拟桌面上的智能体** |
|------|----------------------------------|----------------|------------------------------|
| **运行端点** | 用户 PC / Mac 上的客户端或本机 agent 运行时 | 远程模型 + 浏览器 | 供应商提供的隔离 VM / 远程桌面 |
| **本地文件** | 经授权直接访问用户选定目录 | 依赖上传、连接器或端侧插件 | 操作**远端盘**；未必等于用户本机磁盘 |
| **离线** | 少数纯本地模型可部分离线；多数仍要联网调模型 | 通常全程联网 | 通常全程联网 |
| **典型风险焦点** | 本机数据外泄、误删、越权路径 | 上下文上传范围、账号安全 | VM 侧隔离、供应商侧驻留数据 |

---

## 问题域（为何会出现这类产品）

- **知识工作留在文件系统里**：报告、表格、下载目录、项目仓在本地堆叠，用户希望「指向文件夹就做完」而非反复拖拽上传。
- **多步任务与异步执行**：整理、对账、跨应用汇总适合 **agent 循环**；与单轮 **chat** 互补。
- **与「只在云端」的张力**：组织关心**数据驻留**与**最小暴露面**；本机授权夹或企业托管桌面各走一条路线。
- **benchmark 推动**：**OSWorld**、**GAIA** 等强调**真实环境操作**，厂商用「接近或超过人类操作成功率」叙事推动 **computer-use** 品类可见度。
- **「聊天盲区」**：基于聊天界面的 Agent 看不到本地文件系统的结构与内容——每次操作都需用户手动上传文件或描述路径。桌面 Agent 以文件系统级授权解决「Agent 能自主定位、读取和操作本地文件」这一前提问题，降低了人机之间的「上下文传递成本」。

---

## 能力栈（概念拆分，非厂商功能表）

- **目录级读写**：在授权范围内列目录、读格式、批量重命名、生成报告；常与 **文档/表格/代码**格式解析并列宣传。
- **应用与 GUI 自动化**：启动应用、填表、点击流程；部分产品与 **浏览器控制**、**终端/脚本**一起出现。
- **连接器与混合路径**：本机文件 + **SaaS**（邮件、日历、云盘）由产品定义；并非所有能力都等于「读本地盘」。
- **并行与长时任务**：队列、计划任务、移动设备触发本机继续跑（视产品实现）。
- **隔离执行**：部分实现将 **shell/代码**放入 **VM 或沙箱**，与「直接改用户文档」分层，降低误伤系统风险（具体以各产品为准）。

---

## 形态谱系（与具体品牌解耦）

- **本机桌面应用内智能体**：安装在 **macOS/Windows** 的客户端，强调**本地文件夹**与桌面工作流（与「浏览器打开同一服务」区分开）。其中 **AI 文件浏览器子型（如 Poly.app）** 聚焦文件搜索、整理、摘要与组织，Agent 能力落在文件系统层面，非全桌面操控——与 **Cowork 类**全桌面 Agent 在形态上有别但同属本机智能体光谱。
- **开发者向本机 CLI agent**：终端里长时任务、仓库级操作（与「知识工作者 GUI」买家不同但能力相邻）。
- **托管虚拟桌面 + computer-use**：隔离环境 **7×24**、远程会话；卖点是**与安全边界**，而非「用你的同一台机器的同一文件树」。
- **纯浏览器内的通用助手**：不配本机连接器时，更接近传统 **copilot**，**不归入**狭义的「可直读本地盘」桌面智能体，除非另装扩展。
- **RPA / 脚本自动化套件**：常与 **agent** 叙事融合；_buyer journey_ 更重企业流程与连接器市场。
- **团队频道 / IM 驱动的多 Agent 协作**：以**共享工作区**、频道、daemon、长期记忆为中心时，主矛盾常是「组织知识与协作流」；与「**单人**本机关闭环路（本地文件夹 + 本机预览）」的买家叙事可错位—选型时别看错赛道。



## 风险 · 合规 · 安全与隐私（外部框架可对照，非法律意见）

- **权限与横向移动**：获准的文件夹一旦过宽，敏感表、密钥、令牌可能进入模型上下文；**最小权限**与**分类分级**是基础动作。
- **不可逆写操作**：批量改名、删除、覆盖需 **diff/回收站/备份**策略；**预览再执行**比「全自动默认」更受控。
- **数据出境与处理条款**：即便文件在本地磁盘，推理是否经云端模型、日志与**保留时长**仍以各服务商 **ToS/DPA** 为准。
- **供应链与冒充**：与本机结合的插件、**connector**、第三方 **MCP** 扩大攻击面；宜固定来源与版本。
- **用工与自动化条款**：对部分网站或内部系统的自动操作可能触及 **服务条款** 或内规。

---

## 落地碎片（无先后）

- 先问清：要的是「**摸得到本机某几个夹**」还是「**云端里永远在线的一台干净机器**」——二者产品形态与合规故事不同。
- 为 **Cowork 类**产品单独划**工作夹**，避免把家目录整盘授权给 agent。
- 区分 **Chat** 与 **Cowork/Agent 模式**的官方说明：是否**必须桌面应用**、是否**持续联网**、会话与审计保留策略。
- 与 [agent-skills.md](./agent-skills.md) 交叉：技能包描述「怎么做」；**桌面智能体**解决「在哪台机器、对哪些文件真的动手」。
- 与 [multi-agent.md](./multi-agent.md) 交叉：Eigent/Floatboat 等可带多 Agent 叙事，但**团队 org 层与 L3 Workspace**（Multica、Clawith、Moxt）以 multi-agent 为准；本页主战场是**单人本机**闭环。
- **检索与品牌**：英文圈产品名相近易混（如 **bot**/**boat**/**byte** 等拼写）；写稿、建站与广告投放宜以 **注册域名与 trademark 归属**为准，避免误入他站竞品说明。


## 工具与产品类型（「desktop agent」「computer use」「local files」检索里常混在一起的品类；非穷尽）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **本机知识工作智能体** | 桌面应用、指向本地夹、多步任务 | 常与「免终端」叙事一起出现；含 **Cowork**（全桌面操控）和 **Poly**（文件浏览器型 Agent）两条子线 |
| **AI 文件浏览器 / File Browser Agent** | 智能文件搜索、摘要、组织；Agent 在文件系统层操作 | 不同于全桌面操控型，聚焦「找得到、理得清」；代表：**Poly.app** |
| **Remote / cloud desktop agent** | 隔离 VM、远程桌面上的 GUI 自动化 | 强调安全与可始终在线；**非**用户本机盘 |
| **CLI / 开发向 coding agent** | 仓库、终端、长时 job | 与 GUI **Cowork** 类买家不同 |
| **浏览器 + 本机扩展型** | 连接器桥接本机与网页 | 边界取决于扩展权限 |
| **传统 Copilot 套件** | 内嵌 Office/系统 | 生态锁定与「任意文件夹」灵活性常对比 |
| **AI Coworker / Agentic Workspace（话语层）** | 商业文案常叠加使用 | **Cowork** 偏重任务委派与交付形态；**Agentic Workspace** 偏产品与 UI 模组—均须落到「是否有本机运行时 / 宿主授权」才可等同 **desktop agent** |



## 外链索引（工具与产品；非广告、无排序优先级）

定价、平台与数据流以各官网为准。**Bytebot**、**Simular Sai** 等为**沙箱 / 托管虚拟桌面内的「桌面」**，与 **Floatboat / Cowork** 类「**宿主本机授权夹**」不同，见表内一句与专题对照表。

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **Floatboat** | **Mac/Windows 客户端**的一人公司 **AI Workspace**；自称可访问**本机文件与本地软件**、模块化工作区、内置浏览器、拖拽文件进对话 | [floatboat.ai](https://floatboat.ai/) |
| **Poly.app** | YC S22，AI 智能文件浏览器——定位「Cursor for Files」。自研多模态嵌入模型 **Polyembed-v1**，支持跨所有文件类型（文本文档、PDF、表格、图片、音视频、代码、URL）的自然语言搜索、AI Agent 自动整理/摘要/标记/重命名/组织文件、云端同步、MCP 集成。Agent 能力聚焦**文件系统层面**（搜索、整理、生成摘要、下载），非全桌面操控。免费 100GB，$10/月 2TB；$8M 种子轮（Felicis 领投，2025-11）。macOS + Web，Windows 开发中。**注意**：常与 **PolyBuzz**（AI 角色聊天 app，原 Poly.AI）混淆，实为完全不同的产品与公司。 | [poly.app](https://poly.app/) |
| **Claude Cowork** | Anthropic **agentic** 知识工作形态，在 **Claude 桌面应用**运行；对**授权本地文件夹**读写并完成多步任务；**付费计划**与**桌面端**为前提；部分执行在**隔离环境**（见支持文档） | [website.claude.com/product/cowork](https://website.claude.com/product/cowork) · [Anthropic](https://www.anthropic.com/product/claude-cowork) |
| **Accomplish** | **开源（MIT）**，**AI desktop agent / computer-use agent** 叙事：本机文件与文档、文件夹整理、浏览器类任务；可无 **API key** 使用内置模型，亦可 **BYOK** 或 **Ollama**；用户选择可见文件夹（平台与路线图以官网为准） | [accomplish.ai](https://www.accomplish.ai/) |
| **Eigent** | **开源 Cowork desktop**叙事（本地化部署与多智能体等以官网当期说明为准）；与 Claude Cowork **商业闭环**分叉选型 | [eigent.ai](https://www.eigent.ai/) |
| **Bytebot** | 官网与 FAQ：**开源（Apache 2.0）、AI desktop agent**；在 **沙箱 Linux 桌面（Docker 容器）** 内操纵 **屏幕 / 键盘 / 多应用**，支持本机 Compose 或自托管、横向 **parallel** 扩展（见 [首页与 FAQ](https://www.bytebot.ai/)）；能力落在**容器内磁盘与环境**，一般不视为直接读写宿主 **macOS/Windows 用户家目录**，与 **Floatboat / Claude Cowork**（宿主授权文件夹）分列两条轴线 | [bytebot.ai](https://www.bytebot.ai/) |
| **Simular（Sai / Simular Pro）** | **对照项（非狭义本机盘主叙事）**：**Sai** 多为**云端私有虚拟桌面**；**Simular Pro** 等为另一产品线—见上文 **「专题对照 / 扩展定义」** 表 | [simular.ai](https://www.simular.ai/) |

### 对比与测评（第三方；观点非官方）

社区与科技媒体中较常见的对比轴包括：**本机夹授权 vs 云端 VM**、**是否必须桌面应用**、**与 Claude Code / Copilot 的分工**、以及 **benchmark 分数能否迁移到个人 messy 文件夹场景**。一种典型批评是：「**local-first**」宣传需细读——模型推理是否仍经云端、哪些元数据会进日志。**另一种**是针对 **computer-use**：在 **OSWorld** 等评测上领先的方案，在用户真实桌面上仍可能受制于权限弹窗、反自动化策略与异形 UI。第三类讨论是「**远程虚拟桌面 agent**」（始终在线但不碰用户本机盘）与「**本机 Cowork**」谁更适合法务/创意文件—答案常取决于**数据不得出本机**还是**不得留存供应商环境**的组织策略。*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读与参考材料

- **Anthropic 官方**：Claude Cowork 产品介绍 [website.claude.com/product/cowork](https://website.claude.com/product/cowork)
- **帮助中心（能力边界、桌面端要求等）**：例如 [Getting started（Local agent / Cowork）](https://support.claude.com/en/articles/13345190-getting-started-with-local-agent-mode)（标题与条目以站点更新为准）
- **能力相邻知识块**：[agent-skills.md](./agent-skills.md)（技能与 MCP）、[browser.md](./browser.md)（浏览器侧 AI）、[headless-browser.md](./headless-browser.md)（远程浏览器会话）
- **第三方「Cowork / desktop agent」讨论与榜单**（观点非中立）：[Gumloop · Claude Cowork alternatives](https://www.gumloop.com/blog/claude-cowork-alternatives)、[reddit.com · alternative to Claude Cowork + Computer Use](https://www.reddit.com/r/ChatGPTCoding/comments/1s582h8/is_there_any_real_alternative_to_claude_cowork)（**数据与观点以帖内日期与原文为准**）
