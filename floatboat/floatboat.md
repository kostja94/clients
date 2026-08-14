# Floatboat - Product Marketing Context

> 主文档。基于官网 [floatboat.ai](https://floatboat.ai/)  
> 可复制到 `.cursor/product-marketing-context.md` 或 `.claude/product-marketing-context.md` 供 AI Agent 使用。  
> **状态**：桌面端产品 | **赛道**：Calendar-Driven AI / Proactive Agent OS / Agentic Calendar  
> **运营主体**（页脚）：AOE Tech Labs Limited（© 2026）  
> **创始人**：谭少卿（Tan Shaoqing）| **成立**：2025-11  
> **融资**：种子轮 ~$2M，红杉中国（HongShan）种子基金 + 微光创投（Weiguang Ventures），2026-03

**关联**：[README.md](./README.md) · [floatboat-features.md](./floatboat-features.md) · [floatboat-keywords.md](./floatboat-keywords.md) · [floatboat-competitors.md](./floatboat-competitors.md) · [floatboat-use-cases.md](./floatboat-use-cases.md) · [floatboat-site-structure.md](./floatboat-site-structure.md) · [floatboat-skills-ecosystem.md](./floatboat-skills-ecosystem.md) · [floatboat-obsidian.md](./floatboat-obsidian.md) · [floatboat-page-composition-guide.md](./floatboat-page-composition-guide.md)

**文档阅读顺序建议**：
1. 本文（全局定位 + 策略摘要）
2. [floatboat-features.md](./floatboat-features.md)（功能清单）
3. [floatboat-keywords.md](./floatboat-keywords.md)（关键词策略）
4. [floatboat-competitors.md](./floatboat-competitors.md)（竞品格局）
5. [floatboat-use-cases.md](./floatboat-use-cases.md)（人群与场景）
6. [floatboat-site-structure.md](./floatboat-site-structure.md)（路由实施）
7. [floatboat-skills-ecosystem.md](./floatboat-skills-ecosystem.md)（Skills 专项）
8. [floatboat-page-composition-guide.md](./floatboat-page-composition-guide.md) / [floatboat-obsidian.md](./floatboat-obsidian.md)（落地页）

**Last updated**: 2026-07-28（归档 world-cup blog plan、directory-submission；删除 brand-visual）

---

## 项目定位（内部）

| 项目 | 说明 |
|------|------|
| **一句话** | **Calendar-Driven Proactive Agent OS**：以日历为运行时——Agent 在日历视图上运行，会前准备、到期执行、会后跟进，自动完成。连接 Google Calendar / Notion Calendar / Lark / Outlook / iCloud / 任意 ICS feed。 |
| **官方品类表述** | *The Proactive Agent OS that Runs Work from the Calendar*；Hero 强调 *Calendar-Driven AI — Not Another Chat Box*、*Stop Prompting. Start Your Calendar.* |
| **目标用户** | Solopreneur / Solo Founder / Creator / Small Business Owner / 2-5 人 Studio。**英文站主词 solopreneur / solo founder**；中文站「一人公司 / 单人创始人」。 |
| **语言策略** | **英文站**：solopreneur / solo founder 为主词，避免 "one-person company" 作为英文主关键词。**中文站（`/zh/`）**：一人公司 / 单人创始人。参见 [floatboat-keywords.md](./floatboat-keywords.md) §0。 |
| **平台** | **Mac、Windows**（官网提供分芯片 Mac 下载说明）。 |
| **集成叙事** | 官网称与 **3500+** 工具打通；基于原生 **MCP + IACT** 协议，Agent 直接调用 API、读取本地文件（权限按日历事件授予）。 |
| **产品架构** | 以**日历为运行时的 Proactive Agent OS**：日历事件驱动 → Agent 读取节奏 → 自动准备/执行/跟进；**Combo Skills**（预置 Agent 配方）在日历事件上触发；**FloatIM**（Agent-Native 群聊）作为协作层；全模型内置（DeepSeek / MiniMax / GLM / Kimi / GPT-5 / Claude / Gemini，免 API Key）。 |

---

**文档语言约定**：本目录文档以中文为主（策略/关键词/执行清单）；官网 floatboat.ai 以英文为主；产品专有名词保留英文（Tacit Engine™、Combo Skills、Selfware 等）。

---

## 1. Product Overview（与官网对齐）

**Hero / 核心承诺（英文原文要点）**：

- *The Proactive Agent OS that Runs Work from the Calendar*
- *Calendar-Driven AI — Not Another Chat Box*
- *Stop Prompting. Start Your Calendar.*
- *What if your calendar could actually do the work?*

**One-line description（内部英文，可用于 Meta/PR）**：

```
Floatboat is the proactive agent OS where your calendar becomes the runtime — agents prep before meetings, execute on deadlines, and follow up after, automatically. Works with Google Calendar, Notion Calendar, Lark, Outlook, iCloud, or any ICS feed.
```

**核心差异化：Calendar-Driven vs Chat-Based AI（官网叙事）**：

| 维度 | Chat-Based AI（被动） | Floatboat（主动） |
|------|----------------------|-------------------|
| **触发方式** | 等你打字 prompt 才动 — 你忙或睡着时什么也不做 | 跟日历跑 — 会前准备、到期执行、会后跟进，自动触发 |
| **上下文** | 每次 session 重置 — 不记得你这周的会议、截止日、上次交付了什么 | 每个日历事件有独立 **Agent Workspace**，文件/运行历史/模型选择/决策持久化 |
| **存在方式** | 活在浏览器标签页里 — 不打开不输入，就没有产出 | 跨设备桌面应用（Mac + Windows）+ FloatIM 群聊同步 |
| **触发源** | 你，打字 | 你日历上的事件 |

**叙事锚点**：Work isn't a chat thread — it's a schedule. Chat-based AI waits for you to ask. Floatboat runs with your calendar, so the work is half done by the time you sit down.

---

## 2. 四步机制（From Calendar Event to Finished Work）

| Step | 官网模块名 | 要点 |
|------|------------|------|
| **01** | Your Schedule Becomes the Runtime | 日历是 Agent 的时钟 — 每个事件是带上下文的触发器。接入 Google Calendar、Notion Calendar、Lark、iCloud、Outlook、任意 ICS feed |
| **02** | Floatboat Reads the Rhythm | 会议、截止日、例行任务被分类为各自需要的准备类型 — 在正确的时间、带着正确的上下文 |
| **03** | Agents Prep and Execute | 会前 brief、截止日前 draft、会后 follow-up。Combo Skills 把碎片输入（语音笔记、ticket、散落文档）自动变成成品 |
| **04** | You Stay in the Loop | 每个事件有独立 Agent Workspace：文件、运行历史、模型选择、决策记录。随时调整 prompt、切换模型、重跑某一步 |

**支柱能力**：

- **Combo Skills**：预置 Agent 配方，一键安装 — 语音笔记→Deck、销售通话→跟进邮件、Linear ticket→PR 草稿，约 10 分钟/次跑完。可编辑，按日历事件触发。  
- **Every Frontier Model, Zero Setup**：DeepSeek、MiniMax、GLM、Kimi、GPT-5、Claude、Gemini — 全内置，免 API Key、免 VPN、免中国手机号。Auto Mode 按步骤自动路由模型（低成本模型解析 + 前沿模型推理），提供商限流时即时降级，运行不断。  
- **FloatIM**：Agent-Native 群聊 — Agent 在本地 Mac 上运行，自组织角色分工，交付成品而非纯文字。基于开放 IACT + Selfware 协议，本地优先。

---

## 3. Positioning Statement（内部）

> **For** solopreneurs, creators, and small teams who need a **proactive AI operator** that runs with their **calendar**—not a chat box that waits for prompts—**our** Floatboat **is a** calendar-driven agent OS **that** reads your schedule, prepares ahead, executes on deadlines, and follows up after **automatically**—**unlike** reactive chat-based AI or single-purpose scheduling tools, **we** turn your calendar from a list of time slots into the **runtime** that ships the work before you even sit down.

---

## 4. 外链与声量线索（检索快照，非官网承诺）

用于内容选题与竞品/替代词监控；具体数据以各平台为准。

| 类型 | 链接 | 备注 |
|------|------|------|
| 官网 | [floatboat.ai](https://floatboat.ai/) | 主站 |
| 博客 | [How one-person businesses work like a team with AI](https://floatboat.ai/blog/how-one-person-businesses-work-like-a-team-with-ai) | 2026-03 时间戳（SERP） |
| 博客 | [Should a Solo Operator Use an AI Agent?](https://floatboat.ai/blog/ai-agent-solo-operators) | 2026-04 SERP |
| 社区 | [Reddit: I built FloatBoat.ai…](https://www.reddit.com/r/alphaandbetausers/comments/1snnwl1/i_built_a_desktop_workspace_where_the_ai_learns) | 创始人/早期传播 |
| 第三方收录 | [Make.rs 项目页](https://make.rs/project/5610-floatboatai-ai-workspace-for-oneperson-companies) | 简介聚合 |
| 品类讨论 | [Gumloop: Claude Cowork alternatives](https://www.gumloop.com/blog/claude-cowork-alternatives) | 「替代」榜单类内容 |
| 品类讨论 | [Eigent: Best Claude Cowork Alternatives 2026](https://www.eigent.ai/blog/best-claude-cowork-alternatives-2026) | 竞品文常出现 OpenClaw 等 |
| 长文 | [DEV: What Solo Developers Actually Lack…](https://dev.to/bytewatcher/what-solo-developers-actually-lack-when-working-with-ai-ahj) | 提及 Combo Skills 叙事 |
| Demo 视频 | [Floatboat Demo](https://www.youtube.com/watch?v=SWMIbUBfhJY) | 产品功能演示 |

---

## 5. SEO 执行摘要（交给同事）

围绕四组核心词建设矩阵：**Proactive AI Agent**、**Calendar-Driven AI**、**Agentic Calendar**、**AI Agent for Solopreneurs**；以 **Claude Cowork alternative**、**chat AI alternative** 等商业意图长尾做截流。功能侧按 **Calendar Runtime（日历运行时）**、**Combo Skills（预置 Agent 配方）**、**All Frontier Models（全模型内置）**、**FloatIM（Agent-Native 群聊）** 拆独立路由与内容支柱。Skills 生态路线（Leaderboard + Submit + Store）提高长尾覆盖与站内互动。

详细关键词梯队、功能映射、建议 Title/Meta、路由与 JSON-LD → [floatboat-keywords.md](./floatboat-keywords.md)、[floatboat-site-structure.md](./floatboat-site-structure.md)。Skills 生态策略 → [floatboat-skills-ecosystem.md](./floatboat-skills-ecosystem.md)。

**语言说明**：英文站用 solopreneur / solo founder，避免 "one-person company" 做英文主关键词；OPC / 一人公司 走 `/zh/` 中文站。

---

## 6. 当前需求与优先级（内部草案）

| 优先级 | 需求 | 说明 |
|--------|------|------|
| **P0** | 全站定位同步：Desktop Workspace → Calendar-Driven Proactive Agent OS | 首页、功能页、对比页叙事统一更新 |
| **P0** | 对比页（`/vs/claude-cowork`、`/vs/chat-ai` 等） | Calendar-Driven vs Chat-Based 差异化截流 |
| **P0** | Skills 生态构建（Leaderboard + Submit + Store 优化 + 详情页重设计） | SEO + 社区互动双驱动 |
| **P0** | 导航站/目录站提交 | 历史清单已归档 → [_archive/floatboat-directory-submission.md](./_archive/floatboat-directory-submission.md) |
| **P0** | FloatIM 三路由（`/floatim`、`/floatim/protocols`、`/floatim/vs-floatboat`） | AGENT-NATIVE IM |
| **P1** | 人群页语言切换：英文站统一 solopreneur / solo founder | 修正 OPC 海外搜索盲点 |
| **P1** | 中文站 `/zh/use-cases/one-person-company` 等路由 | 承接 OPC 中文搜索 |
| **P1** | 扩展人群页（Solopreneur / Creator / SMB / Studio） | 覆盖率延展 |
| **P1** | Blog 内容 + 内链矩阵（Calendar-Driven AI 主题） | 中长尾承接 |
| **P1** | SoftwareApplication JSON-LD | 富摘要 |
| **P2** | Skills 教程系列 + 比赛策划 | 社区增长 |
| **P2（前瞻）** | Agent Skill Creator 工具调研 | 功能缺口，如趋势成立有先发价值 |

站点实施与路由 → [floatboat-site-structure.md](./floatboat-site-structure.md)。Skills 生态详细策略 → [floatboat-skills-ecosystem.md](./floatboat-skills-ecosystem.md)。

---

## 7. 姊妹产品：FloatIM（独立网络层）

| 项目 | 说明 |
|------|------|
| **产品** | **FloatIM** — Agent-Native IM；人-Agent 同群、与 Floatboat 本机 Agent 能力衔接；产品入口 [im.floatboat.ai](https://im.floatboat.ai) |
| **与 Floatboat** | Floatboat = 本机工作区/生产端；FloatIM = 网络/消费与协作面（「两 App 同一网络」叙事见对比页） |
| **产品与市场全文** | → 见 [floatboat-features.md](./floatboat-features.md) §1.5、[floatboat-competitors.md](./floatboat-competitors.md) §2.4、[floatboat-keywords.md](./floatboat-keywords.md) §6、[floatboat-use-cases.md](./floatboat-use-cases.md) §7 |

全站内链：首页 Pillars 区 → FloatIM；Header 顶栏 → `/floatim`；FloatIM ↔ Features（实施见 site-structure §2.4）。

---

## 8. Skills 生态策略（新增）

> Combo Store 关键词优化 + Skills Leaderboard + 用户提交 + 比赛 + Agent Skill Creator。详细策略 → [floatboat-skills-ecosystem.md](./floatboat-skills-ecosystem.md)

| 方向 | 说明 |
|------|------|
| **Combo Store 关键词优化** | 原路由不变，Title/Meta 对齐品类搜索词：Agent Skills Store / Skills Marketplace / Skills Platform |
| **Skills Leaderboard** | 纯 SEO 导向，参考 skills.sh 模式；首选按 Floatboat 安装/使用量排名，冷启动阶段可用 GitHub stars 填充 |
| **Skills 详情页重设计** | 原有模板需重新设计；选择高搜索量 skill 做独立落地页（如 Gstack、Lenny podcast skill 等） |
| **用户提交 / Submit** | `/combo-store/submit` 路由，支持社区提交 skills，含审核流程 |
| **Skills 比赛** | 参考 Youmind 技能比赛模式（内容营销驱动）；主题方向：一人公司效率 Skills |
| **Agent Skill Creator（前瞻）** | 本地文件/流程描述 → 规范 skills.md 的转换工具；当前搜索量不高（功能缺口），可能未来发展 |

**生态闭环**：Leaderboard → Store → Detail → Submit → Leaderboard（互相内链）。

---

## 10. 文档互引

| 文档 | 用途 |
|------|------|
| [README.md](./README.md) | 文件夹入口、结构说明、AI Agent 用法 |
| [floatboat-features.md](./floatboat-features.md) | 5 大 Agent 功能 + 产品支柱 + FloatIM 摘要 |
| [floatboat-keywords.md](./floatboat-keywords.md) | 关键词梯队、Title/Meta 建议、功能→词表 |
| [floatboat-competitors.md](./floatboat-competitors.md) | 赛道与竞品、截流词 |
| [floatboat-use-cases.md](./floatboat-use-cases.md) | Combo 场景与人群 |
| [floatboat-site-structure.md](./floatboat-site-structure.md) | 建议 URL、head()、结构化数据 |
| FloatIM | 分布见 [floatboat-features.md](./floatboat-features.md) §1.5 / [floatboat-competitors.md](./floatboat-competitors.md) §2.4 / [floatboat-keywords.md](./floatboat-keywords.md) §6 / [floatboat-use-cases.md](./floatboat-use-cases.md) §7 |
| [floatboat-skills-ecosystem.md](./floatboat-skills-ecosystem.md) | Skills 生态：Combo Store 优化、Leaderboard、提交、比赛、Agent Skill Creator |
| [floatboat-obsidian.md](./floatboat-obsidian.md) | Floatboat for Obsidian 落地页 + Integrations |
| [floatboat-page-composition-guide.md](./floatboat-page-composition-guide.md) | Landing 页面搭建规范 |
