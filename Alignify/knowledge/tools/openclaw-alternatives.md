# OpenClaw 系谱与变体对照 · 知识块（非线性笔记）

**材料范围**：开源仓库自述（[openclaw/openclaw](https://github.com/openclaw/openclaw)）、官方 Gateway 安全文档、维基与科技媒体报道摘要、Moonshot/Kimi、MiniMax、Kilo、Nous Hermes、Pamir AI、PicoCluster Claw、Mac mini 载体叙事等公开发布物料、开发者社区讨论（HN、DEV、OpenClawsome 等）；归纳「网关型个人助理 / 托管发行版 / 硬件宿主 / 轻量化实现」等与 **OpenClaw** 同主题检索下同现的条线。**未**把 Alignify 站内 Tools JSON 正文当作独立事实来源。网摘整理日期 **2026-06-23**，若与站内正式页不一致，以 **`content/tools/*/*openclaw-alternatives.md`** 为准。

**站内对照**：**已上线** Alignify Tools · slug **`openclaw-alternatives`** → [`/tools/openclaw-alternatives`](https://alignify.co/tools/openclaw-alternatives) · [`/zh/tools/openclaw-alternatives`](https://alignify.co/zh/tools/openclaw-alternatives)；`src/data/tools-pages-config.ts` 已收录关键词 **OpenClaw 龙虾 智能体** / **OpenClaw & always-on AI agents**。

**Tools 关键词与 slug 映射**：[对齐入口](../../product/alignify-keywords-tools.md#openclaw-alternatives-tools)

**站内相邻**：[agent-skills.md](./agent-skills.md)（技能生态） · [agent-sandbox.md](./agent-sandbox.md)（沙箱执行） · [multi-agent.md](./multi-agent.md)（多 Agent 编排） · [agent-for-desktop.md](./agent-for-desktop.md)（桌面 Agent）

## 与相邻 slug 分流

| 维度 | **`openclaw-alternatives`（本页）** | **`agent-skills`** | **`agent-sandbox`** | **`multi-agent`** |
|------|------------------------------------|---------------------|---------------------|-------------------|
| **典型买家问题** | 「OpenClaw 有什么替代/相似方案？」 | 「Agent 怎么接工具/技能？」 | 「Agent 在哪安全跑？」 | 「多 Agent 怎么协作？」 |
| **核心能力** | 上游开源核、云上托管、并行开源对照 | MCP 技能生态 | 隔离执行环境 | Agent 编排层 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。**slug 取「openclaw-alternatives」** 为方便与检索词 *OpenClaw alternatives*、中文版「OpenClaw 替代」「类似 OpenClaw」对齐；表中厂商 **不全然是「替代品」**——内含 **上游开源核、云上托管发行版、并行开源**，请以「分层」读本表。

---

## 词汇锚点

- **OpenClaw**：主流叙述中的 **开源个人 AI 助理** / **网关型 agent 运行时**：自架设备或以 VPS 常驻；经 **Gateway** 接通多即时通讯与工作流；常与 **Skills**、龙虾 **🦞** 品牌并存（官方站 [openclaw.ai](https://openclaw.ai/)）。
- **Clawdbot → Moltbot → OpenClaw**：社区与媒体记载的 **沿革链**（中间名曾因商标等与 **Anthropic「Claude」字样**张力被讨论）；具体时间线以仓库 release note 为准。
- **Gateway（控制面）**：会话、通道、工具与事件的 **运行时枢纽**；区别于「仅在网页里单次对话」的 chat。
- **ClawHub / Skills**：对接 **SKILL.md** 等格式的 **扩展能力集市**（见 [agent-skills.md](./agent-skills.md)）；**不是**每条「*Claw」产品线都完全兼容同一套安装路径。
- **托管发行版（Managed *Claw）**：厂商在云侧 **替你跑** OpenClaw 兼容栈或等价能力——**不承担**你家目录直挂，但换得 **运维与 7×24**；与「自托管」对读（例：KiloClaw、Kimi Claw、MaxClaw）。
- **KiloClaw**：**Kilo Code** 团队提供的 **托管 OpenClaw**（页面叙述为 Firecracker VM、与上游兼容、经 **Kilo Gateway** 接大量模型等）；与 **自架 `openclaw onboard`** 对读，属 **Type B** 叙事。
- **轻量替代品 / 并行架构（非 *Claw 品牌）**：其它仓库实现的 **常驻 + 工具 + 网关** 组合；体量与栈与 OpenClaw **不必**同构，常与 **同检索意图** 并列，**≠** 官方 *Claw 系发行版（例：Hermes Agent）。
- **Agent Computer / 智能体专用机 / Agent host**：**不为 OpenClaw fork**，而是 **7×24 跑网关的物理载体**——Mac mini（2026 社区默认）、Pamir Distiller、PicoCluster Claw、Mini PC/VPS 等；买家问题「养在哪」先于「买哪版 *Claw」。
- **OpenClaw Foundation / 上游治理（2026 Q1–Q2）**：Peter Steinberger 加入 OpenAI 后项目迁入独立基金会叙事；选型时仍以 **github.com/openclaw/openclaw** 与官方 docs 为准，托管 *Claw 的 pin 版本可能滞后。
- **Personal Computer（Perplexity）**：macOS 商业栈 + 推荐 Mac mini 7×24；与 OpenClaw **网关运行时不同 SKU**，但 **载体与 always-on** 检索意图重叠。
- **ClawHavoc / 暴露实例 / 恶意技能**：2026 年安全讨论常同现；Gateway 勿绑 `0.0.0.0`、技能按供应链审、见官方 `security audit`（与 [agent-sandbox.md](./agent-sandbox.md) 执行隔离互补）。


## 专题对照 / 扩展定义

| 维度 | **自建 OpenClaw** | **云托管 *Claw（Kilo / Kimi / Max…）** | **并行开源 Agent（Hermes 等；非 OpenClaw fork）** |
|------|-------------------|--------------------------------------|--------------------------------|
| **部署** | 本机 npm/pnpm、`onboard`、daemon | 控制台一键开通 | clone、安装脚本、服务化 |
| **数据落点** | 你的磁盘与工作区条款 | 厂商云与 SLA | 默认亦为自建 |
| **与上游兼容** | 100% repo | 托管栈声称 **紧跟 OpenClaw 发行**，以服务商说明为准 | **独立路线图**；可能支持 MCP，与 ClawHub **无强制关系** |
| **典型买家** | 工程师、硬核玩家 | 免运维、「不想管 VM」 | 要 **学习与自进化技能**叙事、或多终端 **gateway** |

| 维度 | **Mac mini / 备用机自建** | **专用 Agent 硬件（Pamir / PicoCluster）** | **云托管 *Claw** |
|------|---------------------------|---------------------------------------------|------------------|
| **数据落点** | 你的磁盘（macOS 或 Linux） | 独立机器磁盘；常预装栈 | 厂商云与 SLA |
| **集成** | iMessage/Shortcuts 等 macOS 原生 | GPIO/USB/本地 LLM（视 SKU） | IM 连接器 + 厂商模型 |
| **运维** | 你或团队 patch Node/TLS | 厂商预装 + 远程隧道 | 免裸机运维 |
| **典型买家** | 开发者、OpenClaw 社区默认 | 要隔离于笔记本、物理 I/O | 不想当运维 |


---

## 问题域（为何会出现这类产品）

- **对话框不够**：用户要的是 **cron、heartbeat、多端回复**——与一次性网页 **chat** 分工不同；heartbeat 驱动的 **Moltbook 等 Agent 相遇面** 见 [agent-to-agent.md](./agent-to-agent.md)。
- **入口已在 IM**：办公沟通已落在 **Telegram / Slack / 微信** 等，agent 要跟 **会话同屏**而非另开控制台。
- **主权与运维的张力**：**自托管** 自由度高；**托管**省机器与穿透。
- **技能生态爆炸**：**Claude Code / MCP / SKILL.md** 并行后，**「装什么技能」与「在哪个宿主上跑」**被拆开讨论；OpenClaw 系是其中一条 **宿主** 轴线。
- **名称与商誉**：\*Claw 后缀成为 **可被联想营销** 的符号；检索时多与 **comparison / vs / alternative** 同现。
- **载体缺位（2026）**：云端缺本机 context、主力机抢资源/隐私、Mac mini 缺货涨价——催生 **Agent Computer** 品类；OpenClaw 系谱页需覆盖 **host 层**，不必单独 slug 也可写清边界。
- **中文「养龙虾」**：OpenClaw 口语；峰值检索在 2026-03，4 月后回落——内容仍应覆盖 **OpenClaw安装 / 教程 / 安全** 长尾。


---

## 能力栈（概念拆分，非厂商功能表）

- **会话与通道**：多账号、群隔离、routing；与 **网关**配置的权限模型耦合。
- **工具与编排**：浏览器、代码执行、cron、子 agent；对标 **skills** vs **原生工具**二分。
- **记忆与工件**：磁盘侧 **MEMORY/SOUL** 类文件约定（各发行版是否保留不同）。
- **语音与 Canvas**：部分主线支持 **语音唤醒、实时画布**；轻量实现常裁掉以控体积。
- **鉴权与配对**：IM 侧 **QR / OAuth**；企业场景常增 **审计、SSO**（上游 roadmap 以官方为准）。


---

## 形态谱系（与具体品牌解耦）

- **Type A — 上游开源核**：单仓库、MIT、社区贡献；**事实标准**用来说「兼容 OpenClaw」。
- **Type B — 云托管「*Claw」**：月费/点数 + 送存储 + 预装技能；**省运维**。
- **Type C — 轻量 reimplementation**：**千～万行**级 agent 循环 + 可选技能接入；偏 **教学与魔改**。
- **Type D — 宿主 Companion UI**：移动端 / 桌面侧 **菜单栏等与 Gateway 配套的壳**（以 OpenClaw 仓库自述为准）；与 **「本机文件夹 Cowork」** 仍可能不是同一 SKU，见 [agent-for-desktop.md](./agent-for-desktop.md)。
- **Type E — 硬件宿主 / Agent host**：**7×24 专用机器**，不一定改 OpenClaw 源码——**Mac mini**（社区参考）、**Pamir Distiller**（预装 Clawdbot/Claude Code、GPIO）、**PicoCluster Claw**（RPi5 + Jetson + Ollama + OpenClaw）；与 Type B 云托管对读：**磁盘在谁家、谁值班 patch**。


---

## 风险 · 合规 · 安全与工程治理（外部框架可对照，非法律意见）

- **技能供应链**：公开技能与 **任意代码** 同构；**ClawHub** 与第三方目录曾出现 **恶意包** 讨论；企业环境需 **签名单** 与执行隔离。
- **IM 账号与 ToS**：自动化、群发、商业号绑卡等受 **各平台政策**约束；**封号**与 **隐私**风险并存。
- **数据出境**：自托管若仍调 **海外 API**，合规问题未消失；云端托管需核对 **数据处理条款**。
- **指标与排名**：GitHub star、「一周暴涨」等 **易被刷**；作技术决策宜看 **issue 质量、发布节奏、安全公告**。
- **商标与命名**：**Claw / Claude** 等字样在部分法域敏感；产品文案与仓库 **license** 需自行核对。


---

## 落地碎片（无先后）

- 先定 **Type A–E** 要哪一层：要 **改源码**、**只买可用性**，还是 **先买载体**（Mac mini / Pamir / 托管）。
- **托管 vs 自建**：把「**OpenClaw alternatives**」检索意图理解成 **「不想自己当运维」** 时 B 更合适；理解成 **「不想用同一套 Node 仓库」** 时 C 更合适。
- 与 [agent-skills.md](./agent-skills.md) 联读：**ClawHub** 属技能层、**技能安装**不等于 **IM 已配对**；**Gateway** 属宿主层。
- 与 [agent-for-desktop.md](./agent-for-desktop.md) 联读：**「能控本机文件夹的 Cowork」** 与 **「能回你 Telegram 的 Gateway agent」** 常非同一 SKU。
- 与 [multi-agent.md](./multi-agent.md) 联读：**OpenClaw for Teams / Clawith** 与组织级 Crew、RBAC 属 multi-agent L3，非本页个人 Gateway 替代清单主战场。
- 与 [agent-sandbox.md](./agent-sandbox.md) 联读：**载体**解决「跑在哪」；**沙箱**解决「不可信代码边界在哪」——硬件不能替代 microVM/容器。
- **Mac mini 标准姿势（社区）**：无头、非 admin 用户、FileVault、Tailscale；勿把 Gateway 暴露公网。
- **版本号漂移**：各家 **「基于 OpenClaw x.x」** 的 marketing 与实际 pin 版本可能不一致；以 **部署界面或镜像 tag** 为准。


---

## 工具与产品类型（「OpenClaw」「Moltbot」「*Claw」检索里常混在一起的品类；非穷尽）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **上游** | GitHub **openclaw/openclaw**、 **[openclaw.ai](https://openclaw.ai/)** | 「The lobster way」等品牌线索 |
| **云托管发行** | **KiloClaw**、**Kimi Claw**、**MaxClaw** 等 | 免自架叙事；计费与模型路由以各产品为准 |
| **并行开源 Agent（非 claw 后缀）** | **Hermes Agent**（Nous Research）等 | 同货架常对比 **网关 + IM + 常驻**；代码库独立，见外链索引 |
| **技能集市** | **ClawHub** | [clawhub.ai](https://clawhub.ai/) 等 |
| **命名存疑的 SEO 页** | 复制站、wiki 镜像 | 以 **github.com/openclaw** 为准核 |
| **硬件宿主（Type E）** | **Pamir Distiller**、**PicoCluster Claw**、Mac mini 自建 | 预装或社区参考；**≠** OpenClaw fork |


---

## 外链索引（工具与产品；无排序优先级；与站内 Tools 页产品外链一致时使用相同 UTM）

| 名称 | 一句话（据公开页面或仓库归纳） | URL |
|------|--------------------------|-----|
| **OpenClaw** | 网关型个人助理、多通道运行；站点与仓库为权威入口 | [openclaw.ai](https://openclaw.ai/?utm_source=kostja&utm_medium=blog) · [GitHub openclaw/openclaw](https://github.com/openclaw/openclaw) |
| **ClawHub** | 社区技能/插件发现与搜索 | [clawhub.ai](https://clawhub.ai/) |
| **KiloClaw** | Kilo 侧 **Hosted OpenClaw**、Gateway 模型路由、兼容上游等叙事 | [kilo.ai/kiloclaw](https://kilo.ai/kiloclaw?utm_source=kostja&utm_medium=blog) |
| **Kimi Claw** | Kimi **一键云部署 OpenClaw**、7×24、模型与技能捆绑等叙事 | [kimi.com/bot](https://www.kimi.com/bot?utm_source=kostja&utm_medium=blog) |
| **MaxClaw** | MiniMax Agent 内托管、与自家模型与额度体系绑定 | [agent.minimaxi.com/max-claw](https://agent.minimaxi.com/max-claw?utm_source=kostja&utm_medium=blog) |
| **Hermes Agent** | **Nous Research**：常驻服务端、messaging gateway、记忆与技能闭环、MIT；**不是** OpenClaw fork，与 *Claw 系 **并列选型** | [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/?utm_source=kostja&utm_medium=blog) · [GitHub nousresearch/hermes-agent](https://github.com/NousResearch/hermes-agent) |
| **Pamir Distiller Alpha** | 专用 Linux **Agent Computer**；预装 OpenClaw/Clawdbot；GPIO/USB；远程 VS Code / iOS | [pamir.ai](https://www.pamir.ai/?utm_source=kostja&utm_medium=blog) |
| **PicoCluster Claw** | RPi5 + Jetson；OpenClaw + Ollama 本地 LLM 一体机；SMEEP 参考平台 | [picocluster.com/products/picocluster-claw](https://www.picocluster.com/products/picocluster-claw?utm_source=kostja&utm_medium=blog) |

### 对比与测评（第三方；观点非官方）

独立作者与论坛里，**OpenClaw** 常与 **「star 增速、攻击面、技能信任」** 一起出现：典型提醒是 **不要把「开源热」直接等同工程可维护性**——大仓库、快迭代与 **第三方技能** 组合时，**供应链接管** 压力显著。另一类讨论对比 **Claude Code / Codex** 与 **长期驻留 + IM 入口** 的 agent：前者偏 **交互式编程**，后者偏 **异步任务与多通道投递**，**替代关系** 并不对称。**Hermes Agent**（Nous）常与「自建网关还是托管 *Claw」同一话题并列，但其代码库 **并非** OpenClaw 衍生品，选型宜按 **运行时栈（Node vs Python）、技能格式与路线图**拆分。*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读与参考材料

- **百科式背景**（事实核对以官方仓库为准）：[维基 OpenClaw 条目](https://en.wikipedia.org/wiki/OpenClaw)（英）
- **社区 setup 叙事**：[DEV — Set Up OpenClaw as Your Personal AI Agent in 2026](https://dev.to/kfuras/set-up-openclaw-as-your-personal-ai-agent-in-2026-h5o)
- **托管 OpenClaw（Kilo）**：[kilo.ai/kiloclaw](https://kilo.ai/kiloclaw?utm_source=kostja&utm_medium=blog)
- **并行架构 Agent**：Hermes 安装见 [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/?utm_source=kostja&utm_medium=blog)
- **生态列表**：[awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw)（社区整理；**非**官方）
- **Mac mini 与 Agent 载体**：[OpenClawsome — Mac mini supply crunch](https://openclawsome.com/news/openclaw/mac-mini-supply-crunch-shows-agents-need-dedicated-hardware)
- **官方安全基线**：[OpenClaw Gateway Security](https://docs.openclaw.ai/gateway/security)
- **相邻知识块**：[agent-skills.md](./agent-skills.md) · [agent-for-desktop.md](./agent-for-desktop.md) · [agent-sandbox.md](./agent-sandbox.md) · [agent-to-agent.md](./agent-to-agent.md)（Moltbook/AgentGram 等 **跨用户 Agent 相遇面**）
