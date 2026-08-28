# Agent Skills 生态 · 知识块（非线性笔记）

**材料范围**：公开站点说明（[skills.sh](https://skills.sh/)、[ClawHub](https://clawhub.ai/)）、社区文章与第三方盘点；归纳「技能目录 / 安装 CLI / 运行时发现 / MCP 与 Skill 分工」等并列概念。**未**把 Alignify 站内 Tools 正文 JSON 当作独立事实来源。网摘整理日期 **2026-04-21**。

**站内对照**：[alignify.co/tools/agent-skills](https://alignify.co/tools/agent-skills) · `/zh/tools/agent-skills` · `content/tools/en/agent-skills.md`、`content/tools/zh/agent-skills.md` · slug **`agent-skills`**

**站内相邻**：[agent-for-desktop.md](agent-for-desktop.md)（桌面执行端） · [multi-agent.md](multi-agent.md)（多 Agent 编排） · [openclaw-alternatives.md](openclaw-alternatives.md)（开源变体） · [agent-sandbox.md](agent-sandbox.md)（沙箱执行环境）

## 与相邻 slug 分流

| 维度 | **`agent-skills`（本页）** | **`agent-for-desktop`** | **`multi-agent`** | **`openclaw-alternatives`** |
|------|----------------------------|------------------------|-------------------|-----------------------------|
| **典型买家问题** | 「Agent 怎么扩展能力/接工具？」 | 「Agent 怎么在桌面操作文件？」 | 「多 Agent 怎么分工协作？」 | 「OpenClaw 有什么替代方案？」 |
| **核心能力** | MCP 服务器、技能包、插件生态 | 本机文件授权与 GUI 操作 | 编排框架、任务路由 | 开源 Gateway 与托管发行版 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Agent Skill（代理技能）**：在多数实现里指可复用的**程序性知识**——常以 `SKILL.md` 等形式描述触发条件、工作流步骤、与工具的配合方式；与「模型权重里的静态知识」区分。
- **SKILL.md**：社区广泛采用的技能描述载体；具体字段与约定因平台而异，常与「安装到某目录后由 Agent 按需加载」配合。
- **Skills Directory / Marketplace**：网站或榜单形态，聚合仓库链接、分类、安装量统计，便于**发现**技能；不等同于「官方规范制定方」。
- **安装 CLI**：例如通过 `npx` 一类命令将远程仓库中的技能装到本地 Agent 约定目录（各产品路径不同：`.cursor/skills`、`~/.claude/skills` 等）。
- **MCP（Model Context Protocol）**：Agent 与外部**工具/数据源**通信的协议层；**MCP Server 注册表**索引的是可调用工具，与「文档型 Skill」相邻但**不同层**。
- **运行时发现（runtime discovery）**：Agent 在任务当下向**注册表**发起查询，按语义检索匹配技能或工具，而非仅依赖启动前静态配置。
- **Gateway / Registry（网关型注册表）**：企业或社区实现的集中入口：统一鉴权、动态发现、工具调用代理；可单独讨论 **Skill 卡片**与 **MCP 工具** 的关联设计。
- **Plugin / Bundle**：IDE 或 CLI 中的「插件包」叙事，可能同时包含 slash 命令、预置 Agent 配置与技能集合（例如云厂商维护的大型单仓）。

---

## 专题对照 / 扩展定义

| 对象 | **侧重** | **典型产物** |
|------|----------|--------------|
| **Skill 目录站** | 浏览、搜索、榜单、外链到 GitHub | 网页索引、`npx skills add owner/repo` 入口 |
| **Skill 单仓 / 厂商合集** | 权威维护、版本与领域完整度 | 大量 `SKILL.md`、安装说明 |
| **MCP 注册表** | 可执行工具、传输方式、版本 | Server 清单、包名与配置片段 |
| **运行时技能注册表** | 自动爬取公开 `SKILL.md`、语义检索 | MCP 查询端点、claim/统计页 |
| **动态 MCP 市场（代理）** | 会话内安装/激活其它 MCP | 本地 SQLite、工具名命名空间 |

---

## 问题域（为何会出现这类产品）

- **碎片化**：Cursor、Claude Code、Copilot、Windsurf、Gemini CLI 等对「技能放哪、如何触发」路径不一，目录站用**同一批 Git 仓库**降低重复介绍成本。
- **可发现性**：没有索引时，用户只能 star 列表或搜 GitHub；**榜单与分类**承担冷启动与信任传递（安装量、作者组织）。
- **能力与上下文分离**：Skill 把「何时读这份说明」从主提示词里抽离，减少长 system prompt；**工具层（MCP）**再负责真实 I/O。
- **企业治理**：团队需要审计「允许哪些外部技能/工具、是否可外联」；网关型产品把**策略与日志**放在单一控制面。
- **从静态到动态**：预装列表无法覆盖长尾任务；**注册表 + 语义检索**试图把「找技能」也自动化。

---

## 能力栈（概念拆分，非厂商功能表）

- **编目与检索**：分类、标签、平台筛选、全文/语义搜索。
- **一键安装**：CLI 将远程技能同步到本地约定目录；多 Agent 并存时可能涉及 symlink 或 monorepo。
- **版本与出处**：指向固定 commit 或 tag；降低「上游改写 SKILL 导致行为漂移」风险。
- **与 MCP 协同**：Skill 文档描述「应调用哪些工具」；网关在注册层校验工具是否仍存在。
- **发布与贡献**：Submit / PR / 爬虫认领；维护者审核与恶意技能治理（供应链视角）。
- **使用度量**：安装次数、调用次数、排行（指标可信度因平台而异）。

---

## 形态谱系（与具体品牌解耦）

- **开放目录 + 排行榜**：聚合社区仓库，强调「Open Agent Skills Ecosystem」类叙事。
- **Curated 目录**：人工或规则筛选，强调跨平台兼容与 `SKILL.md` 标准说明。
- **厂商技能大包**：云/IDE 厂商维护的上百个领域技能 + MCP 配置 + Agent 模板。
- **MCP 工具注册 / 索引（各类实现）**：服务**工具发现**与集成；Skill 文档可描述拟配合的工具能力，具体注册形态因产品而异。
- **全局技能索引（爬虫）**：对公开仓库中的 `SKILL.md` 自动收录，配套查询接口（与静态「目录站」互补）。
- **会话内 MCP 市场代理**：单入口进程动态拉取、激活其它 MCP，合并工具列表（常带本地管理 UI）。
- **企业 MCP 网关**：OAuth、工具发现、与内部技能/工具联邦；设计文档中常单独定义 **Agent Skills** 数据模型。

---

## 风险 · 合规 · 供应链（外部框架可对照，非法律意见）

- **供应链**：技能即代码/说明文档，可能诱导 Agent 执行**危险命令**或泄露机密到不可信端点；来源宜限定组织与签名发布渠道。
- **过度放权**：「自动安装/自动发现」缩短路径的同时也扩大**攻击面**；企业环境应对接审批与隔离执行。
- **许可与版权**：仓库 LICENSE 与 SKILL 内嵌示例、第三方文档引用需一致；商用分发前核对条款。
- **指标操纵**：排行榜依赖安装或点击统计时，可能存在刷量；**不宜**把榜单名次当作安全或质量认证。
- **隐私**：运行时注册表若上传查询或仓库标识，需审 DPA 与数据留存；**私有技能**是否被索引要读清政策。

---

## 落地碎片（无先后）

- 先定**目标 Agent**与官方文档中的技能目录路径，再选安装方式（CLI vs 手动复制）。
- 区分「**我要装一个说明包（Skill）**」与「**我要接一个 API 工具（MCP Server）**」；复杂任务常两者并用。
- 优先从**可信组织**仓库安装；对小众技能阅读 `SKILL.md` 内触发条件与命令示例。
- 需要**可复现构建**时，锁定 git ref 并记录 CLI 版本。
- 企业场景评估：是否允许外网注册表、是否自建网关、审计日志字段是否满足内控。
- Skill 与 MCP 扩大**工具攻击面**；LLM 生成代码/命令的**执行边界**（沙箱、microVM、Devbox）见 **`agent-sandbox`** 知识块与站内 [`/blog/agent-sandbox`](https://alignify.co/blog/agent-sandbox)（与本文「接什么工具」不同层）。

---

## 工具与产品类型（「Agent Skills」「MCP」「技能安装」检索里常混在一起的品类；非穷尽）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **Web 技能目录 / Hub** | 搜索、分类、榜单、链到 GitHub | 本文外链索引仅列 [skills.sh](https://skills.sh/)、[ClawHub](https://clawhub.ai/) |
| **安装器 CLI** | `npx skills add <owner/repo>` 等 | 入口常印在目录站首页；实际命令以各 CLI `--help` 为准 |
| **Curated 技能列表（站内设「如何安装」）** | 平台标签、一键命令 | 与目录站边界模糊，侧重编辑精选 |
| **厂商技能 monorepo** | 领域技能 + MCP 片段 + IDE 配置 | 由云/IDE 等维护的大型单仓；选型时核对许可与更新节奏 |
| **MCP 工具索引 / 注册（实现各异）** | MCP Server 包、版本、元数据 | 与「文档型 Skill」相邻；具体入口因工具链而异 |
| **运行时技能注册表** | 爬取 `SKILL.md`、查询端点、认领/统计 | 与静态目录互补；政策与延迟需单独评估 |
| **动态 MCP 代理 / 市场** | 会话内 browse/install/activate | 开源叙事如 agent-discover（见延伸阅读） |
| **企业 MCP 网关 + Skill 模型** | 统一鉴权、工具发现、技能卡片存储 | 设计参考如 mcp-gateway-registry 文档 |

---

## 外链索引（工具与平台；非广告、无排序优先级）

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **Skills（skills.sh）** | 自称开放 Agent Skills 生态目录；展示多 Agent 支持列表与安装命令（如 `npx skills add <owner/repo>`）、排行榜 | [skills.sh](https://skills.sh/) |
| **ClawHub** | 社区工具与技能/插件发现站点（Skills、Plugins 等分区），强调搜索与发布 | [clawhub.ai](https://clawhub.ai/) |

### 对比与测评（第三方；观点非官方）

目录站与「一键安装」CLI 并存后，社区常见讨论集中在三点：**跨平台路径是否真的一致**（同一仓库在不同 Agent 的安装目录与触发策略仍可能不同）、**榜单/安装量能否代表质量**（组织号与刷量风险）、以及 **Skill 与 MCP 边界**——新手易把「文档型技能」当成「已接好的 API」，实际仍需本机工具链或网络权限配合。若使用「自动爬取 + 按需查询」类注册形态，还需核对**索引范围**、**延迟**与**隐私/出境**是否与内网政策一致。企业侧更关注网关（OAuth、审计、工具禁用列表）而非公共排行榜。

*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读与参考材料

- **Anthropic 技能参考仓库**（社区常作为模板来源）：[github.com/anthropics/skills](https://github.com/anthropics/skills)（与目录站「skill-creator」等条目交叉引用）。
- **运行时发现讨论**：[DEV · AI Agents Can Now Discover Skills at Runtime](https://dev.to/catalin_crisan_5685ca8fcf/ai-agents-can-now-discover-skills-at-runtime-without-any-human-intervention-36ih)（**数据点以原文日期为准**）。
- **动态工具发现（网关文档）**：[MCP Gateway Registry · Dynamic Tool Discovery](https://agentic-community.github.io/mcp-gateway-registry/dynamic-tool-discovery/) · [Agent Skills Architecture（设计稿）](https://github.com/agentic-community/mcp-gateway-registry/blob/main/docs/design/agent-skills-architecture.md)。
- **会话内 MCP 市场（实践文）**：[DEV · Dynamic MCP Marketplace / agent-discover](https://dev.to/keshrath/how-i-gave-my-ai-agents-a-dynamic-mcp-marketplace-d3a)（第三方实现叙事）。
- **MCP 规范入口**：[modelcontextprotocol.io](https://modelcontextprotocol.io/)（协议与实现生态）。
- **Alignify · A2A Agent Network**：[agent-to-agent.md](agent-to-agent.md)——Moltbook/AgentGram/EigenFlux 等 **Skill 接入的 Agent 相遇面**（与 MCP 工具层互补）。
- **Alignify · 多智能体系统**：[multi-agent.md](multi-agent.md)——MCP 管工具接入；multi-agent 管 **Agent 间 handoff 与团队 Workspace**（与 Skills 能力层互补）。
