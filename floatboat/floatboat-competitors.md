# Floatboat 竞品与赛道

> 本文档专注**竞品与品类**：Calendar-Driven AI / Proactive Agent OS 赛道、截流词、客观对比维度。  
> **关联**：[floatboat.md](./floatboat.md) · [floatboat-keywords.md](./floatboat-keywords.md) · [floatboat-site-structure.md](./floatboat-site-structure.md) · [floatboat-skills-ecosystem.md](./floatboat-skills-ecosystem.md)

**Last updated**: 2026-06-03（定位 pivot：Calendar-Driven Proactive Agent OS；此前 2026-05-06）

**文档结构**：§1 赛道与叙事轴 → §2 竞品速览表 + 重点产品摘录 → §3 对比维度 → §4 外链 → §5 截流词。

---

## 1. 赛道定义

| 品类词 | 说明 |
|--------|------|
| **Calendar-Driven AI** / **Proactive Agent OS** | Floatboat 主品类：AI 以日历为运行时，主动准备、执行、跟进——非被动等 prompt |
| **Agentic Calendar** | 日历即 Agent OS，非传统日程管理工具；竞争相对空白的新品类 |
| **Proactive AI Agent** | 主动式 Agent vs 被动式 Chat AI；强调"触发源是日历事件，不是聊天框" |
| **Desktop AI Agent** | 补充品类：强调本地应用、桌面操作系统级能力（Mac + Windows） |

Floatboat 官方自称 *The Proactive Agent OS that Runs Work from the Calendar*，与 **solopreneur / solo founder** 强绑定；核心差异化是 **Calendar-Driven（主动）vs Chat-Based（被动）**。

**常见叙事轴（写对比页时可用）**：
- **Calendar-Driven vs Chat-Based**：日历触发执行 vs 聊天框等待 prompt（Floatboat 核心叙事）
- **Proactive vs Reactive**：Agent 主动跑在日程上 vs 用户打开才干活
- **单人深度桌面 vs 团队频道协作**：本机日历驱动 vs 云端共享工作区
- **All Models Built In vs API Key Required**：免配置全模型内置 vs 需要自己接 API

---

## 2. 直接对标

以下名称来自内部选题与行业榜单，**不构成法律上的「竞品声明」**；功能、价格、地区以各产品官网为准。

### 2.1 竞品速览

| 产品 / 概念 | 备注 |
|-------------|------|
| **Chat-Based AI（ChatGPT / Claude / Gemini 等）** | Floatboat 核心对比对象：**被动等 prompt vs 日历主动触发**。Calendar-Driven vs Chat-Based 是首要叙事轴 |
| **Claude Cowork** | 品类锚点；**Claude Cowork alternative** 为高意图流量词；对比维度：Calendar-Driven（主动）vs Chat-Driven（被动） |
| **Calendar 工具（Calendly / Motion / Reclaim 等）** | 组织时间但不做实际工作——Floatboat 对比强调「Calendar as Runtime, not just scheduler」 |
| **Manus** | 通用 Agent 产品语境中常被并列 |
| **Accomplish**、**Eigent**、**Foxl**、**Ghost**、**Lapu** | 桌面 / Agent 赛道候选；以各站为准 |
| **Slock** | 团队 IM 内多 Agent；本机 daemon、持久记忆。[slock.ai](https://slock.ai/)。vs Floatboat：团队频道 vs 单人日历驱动 |
| **Kollab** | 团队 AI-native 工作区：Skills、Bots、连接器。[kollab.im/product](https://kollab.im/product)。vs Floatboat：组织+IM vs 单人日历驱动。**kollab.im** ≠ kollab.ai |

### 2.2 重点产品摘录（维护笔记）

写长文或销售话术时可展开；与 §2.1 避免重复粘贴。

**Slock**（[slock.ai](https://slock.ai/)）

- 叙事：*Where humans and AI agents collaborate*；agent 作队友而非一次性工具。
- 流程概览：建 Server → 连本机 → 按角色 Spawn agents → 在频道协作；daemon 示例见官网（如 `npx @slock-ai/daemon`）。
- 能力关键词：跨 session 记忆（代码库、偏好、历史）；Always on（休眠 / 唤醒 / 上下文恢复）。
- **2026-04 最新动态**：创始人 RC 在播客中披露，Slock 团队内部使用 40 个 Agent + 7 名人类协作的模式运营；提出「Agent Dynamics」（Agent 动力学）概念，研究多 Agent 在团队中的协作、竞争与自组织行为。
- 对比 Floatboat 时一句话：**频道型多 Agent + 本机执行** 与 **单人桌面工作区** 是两条主线。

**Kollab**（[kollab.im/product](https://kollab.im/product)）

- **上线动态**：2026-04-23 在 Product Hunt 上线，获当日第 **#2 Product of the Day**。创始人汪兆飞（原 FlowUs 创始人）。
- 核心四组件：**Bots**（接入 Slack/飞书/Discord/Telegram）、**Skills**（可复用团队工作流，存为 GitHub 仓库）、**Connectors**（基于 MCP + HTTP API + OAuth）、**Memory**（持久化团队上下文，「组织复利」）。
- 连接器示例（官网展示）：Google Drive、Figma、Canva、Gmail、Linear 等（以官网为准）。
- 第三方：[Product Hunt · Kollab](https://www.producthunt.com/products/kollab-2)。
- 定价：Free + Premium 从 $20/月 起。
- 对比 Floatboat 时一句话：**共享工作区 + 组织知识 + IM** 与 **一人桌面闭环** 错位竞争。

### 2.3 品牌与域名混淆

| 易混项 | 说明 |
|--------|------|
| **kollab.im** vs **kollab.ai** | 本次竞品记录以 **.im** 为准；**.ai** 为另一品牌叙事（如 Playbooks），勿合并写进同一产品事实。 |

### 2.4 FloatIM 竞品与替代格局

| 象限 | 说明 | 备注 |
|------|------|------|
| **现有 IM + Agent** | 企业/协作产品内嵌智能体、机器人、应用市场 | 成熟渠道，FloatIM 需讲清「为 Agent 建网」的差异 |
| **AI-native 协作/聊天产品** | 各类「AI 团队/群聊/工作区」 | 能力差异大，名称易变，上线前须逐家核实 |
| **仅协议/基础设施** | A2A、MCP、编排框架等 | 多为不直接面向终端聊天 UX；FloatIM 是可感知产品 + 自研协议 |

**差异化主张**（需与证据链一致）：Agent 在群与规则下的一等设计；与 Floatboat 配合时的本机/主权叙事；IACT、Selfware 的开放与可组合故事。不宜过度承诺「首个 / 全球唯一 / 全开源 / 全免费用」等。

---

## 3. 对比页可用维度（客观、可验证）

撰写 `/vs/claude-cowork` 等页面时，建议表格化以下维度（每格需有产品事实支撑）：

| 维度 | 示例角度 |
|------|----------|
| **触发模型** | Calendar-Driven（主动）vs Chat-Based（被动等 prompt）— 核心差异化 |
| **日历接入** | Google Calendar / iCloud / Outlook / Lark / Notion Calendar / ICS feed |
| **形态** | 纯桌面 / Web+桌面 / 浏览器扩展 |
| **协作模型** | 单人 / 小队频道 / 企业租户；是否强依赖 IM |
| **模型内置** | 全模型内置免 API Key vs 需自己接 API — DeepSeek / GPT-5 / Claude / Gemini 等 |
| **本地文件** | 读写的深度、预览格式、是否需上传云端 |
| **技能复用** | Combo Skills（可按日历事件触发）vs 工作流/插件 |
| **集成数量** | 官网 3500+（需与后台一致）；MCP + IACT 原生协议 |
| **平台** | macOS / Windows / 芯片 |
| **定价** | 免费增值、订阅、席位（以各站 Pricing 为准） |
| **隐私与数据** | 本地处理范围、权限按日历事件授予、遥测、模型路由 |

---

## 4. 外链参考（行业内容，非官网）

用于监测「替代」话题与选题角度：

- [Gumloop: Claude Cowork alternatives](https://www.gumloop.com/blog/claude-cowork-alternatives)  
- [Eigent: Best Claude Cowork Alternatives 2026](https://www.eigent.ai/blog/best-claude-cowork-alternatives-2026)  
- [TabTabTab: Cowork alternatives for file automation](https://tabtabtab.ai/blog/cowork-alternatives)  
- [Reddit: alternative to Claude Cowork + Computer Use](https://www.reddit.com/r/ChatGPTCoding/comments/1s582h8/is_there_any_real_alternative_to_claude_cowork)  
- [Kollab 博客：AI workflow automation（官网观点）](https://kollab.im/blog/ai-workflow-automation-2026-why-processes-still-stalled)  
- [Product Hunt：Kollab（第三方讨论入口）](https://www.producthunt.com/products/kollab-2)  

---

## 5. SEO 截流词清单（维护用）

> 完整关键词梯队与截流词表见 [floatboat-keywords.md](./floatboat-keywords.md) §1.3。此处仅列竞品相关的截流方向：

- Claude Cowork alternative
- Manus / Accomplish / Eigent alternative（按需扩展）
- ChatGPT desktop alternative
- OpenClaw desktop workspace（若与产品事实一致）
- Slock alternative / Kollab alternative（详见 keywords.md 优先级说明）
