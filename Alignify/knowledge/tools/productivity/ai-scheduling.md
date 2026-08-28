# AI 日程安排 · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商官网、社区讨论、第三方评测与行业对比文摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 2026-05-10。

**站内对照**：待上线 Tools 页时对齐（建议 slug：`ai-scheduling`，路由 `/tools/ai-scheduling`、`/zh/tools/ai-scheduling`）。

**Tools 关键词与 slug 映射**：待 `tools-pages-config.ts` 收录后补 [`alignify-keywords-tools.md`](../../keywords/alignify-keywords-tools.md) 锚点；当前检索簇覆盖 **AI scheduling tools**、**AI scheduling assistant**、**AI calendar assistant**、**smart calendar**、**meeting scheduler AI**、**calendar automation**。

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI 日程安排 / AI scheduling（本文件所指）**：用 AI/ML 替代或缩减人工排日程决策链路的产品类别——从「双方翻日历找空档」的手工协作，迁移到 **AI 代理自动匹配可用时间、协商、预约、提醒、重排**。英文检索常混用 **AI scheduling assistant**、**AI calendar**、**smart scheduler**、**meeting scheduler AI**。**与纯共享可用时段链接（booking link）** 的核心分界在于：后者仍是人发链接、人选时段，AI 只做了「可预约」端的结构化，而非「协调」端。
- **Booking link / 预订链接**：Calendly 式「分享你的空闲时段，让对方选」的模式——AI 程度低，但用户认知极深，常被混入「AI scheduling」检索结果。
- **Calendar optimization / 日历优化**：在已有日历上做冲突检测、焦点时间保护、团队协调——侧重**内部效率**而非外部约见。代表：Reclaim、Clockwise。
- **Agentic scheduling / 代理式排程**：AI 作为「数字秘书」主动参与邮件、Slack 线程协调时间，甚至两个 Blockit 用户的 Agent 直接协商——不需人类来回沟通。代表：Blockit、Lindy。
- **Task + calendar unification / 任务日历合一**：把待办任务自动塞进日历空档，形成动态日程——是「排程」与「任务管理」的交叉品类。代表：Motion。
- **Smart availability / 智能可用时段**：不只暴露「日历有空」，而是根据优先级、通勤、偏好地点（咖啡店 / 办公室 / 居家）智能推荐时段。
- **Group scheduling / 群组排程**：多人 >3 的协调，难度指数上升；部分工具专做此场景（如 Doodle 被收购后方向变化，新玩家入场）。

---

## 专题对照 / 扩展定义

本文件讨论 **AI Scheduling / 日程安排**（AI 替代或增强排日程决策）。**AI 会议记录**（会中/会后转写、纪要、行动项）是相邻但独立品类，见 [note-taker.md](note-taker.md)。英文检索中 AI note taker 常与 meeting scheduler 出现在同一篇「top AI tools for meetings」盘点里，但解决问题根本不同：一个是「找到时间开这个会」，另一个是「开了会后做了什么」。

| 维度 | AI Scheduling（本文件） | AI Note Taker |
|------|------------------------|---------------|
| 核心问题 | 何时、何地见面 | 会上说了什么 |
| 时机 | 会前协调 | 会中/会后处理 |
| 输出物 | 日历事件、确认 | 转写稿、纪要、行动项 |
| 典型工具 | Reclaim, Motion, Calendly, Clockwise | Otter, Fireflies, Read |

---

## 问题域（为何会出现这类产品）

- **协调成本隐性膨胀**：知识工作者每周约 **4-6 小时**花在排日程上（发邮件、翻日历、等人回复），高管的数字更高。AI scheduling 的直接价值主张就是回收这部分时间。
- **时间碎片化**：连续排程导致「30 分钟会 → 15 分钟空档 → 1 小时会」的碎片日历，焦点时间被侵蚀。Calendar optimization 类工具正是针对这一痛点。
- **跨时区/跨组织协调复杂**：远程 + 全球分布的团队让「找一个大家都可以的时间」从公式可解变成多约束优化——更适合机器。
- **任务管理断层**：任务列表和日历长期割裂——人知道有事要做，但没决定「什么时候做」。Motion 类产品填补这个 gap。
- **偏好隐式化**：传统排程靠人默认假设（「上午不开会」「周二居家」），AI 能学习并编码这些偏好，减少每次协调时的重复沟通。
- **个人助理的数字化替代**：高管助理本身就是一种「排程服务」，AI scheduling 试图将其部分能力产品化、规模化。

---

## 能力栈（概念拆分，非厂商功能表）

- **可用时段暴露**：日历同步 → 规则筛选（工作时间、缓冲、最大会议数）→ 生成可预约窗口。这是所有 scheduling 工具的最小公分母，也是 Calendly 的起点。
- **偏好模型**：个人级（安静时间、能量周期、通勤时间、偏好的咖啡店地址）vs 组织级（团队规范、会议日策略）。Reclaim 用 habit/task 优先级建模，Blockit 用用户直接教导 + 隐式学习。
- **冲突解决策略**：刚性（不可移动的事件）vs 柔性（AI 可建议重排）；跨人冲突时需协商协议（先到先得、优先级加权、轮转）。
- **智能建议**：「这周哪天适合 1v1？」「三周内最早能约到的时间？」——从暴露可用时段升级为主动推荐具体时间。
- **代理式协调**：Agent 通过邮件/Slack 代你回复、协商时间；Agent-to-agent（两个 AI 直接谈）是最激进的形态。
- **任务→时间映射**：把任务清单中的 deadline、预估耗时、优先级 → 自动填进日历空档；需要日历双向同步 + 任务管理集成。
- **团队分析**：可视化「会议太多」「碎片化严重」「无会议日执行率」等团队级指标。
- **多平台集成深度**：Google Calendar、Outlook、Apple Calendar 的 API 能力不对称（Outlook 的某些字段权限就不如 Google），限制了工具能做到的粒度。

---

## 形态谱系（与具体品牌解耦）

- **Booking link 型（低 AI）**：分享链接、对方选时间、自动发确认和提醒。用户心智最强、市场最大，但 AI 成分最薄。Calendly、Cal.com 为代表。
- **个人日历优化型（中 AI）**：在已有日历上自动锁定焦点时间、安排习惯任务、智能缓冲。侧重「保护你的时间」，而非「帮别人约你」。Reclaim、Clockwise 为代表。
- **任务日历统合型（高 AI）**：把任务管理系统和日历合并，AI 动态排程。用户交互从「手动选时间」变成「给 AI 一个优先级清单，它每天给你排」。Motion 为代表。
- **Agent 代理型（最高 AI）**：AI 作为秘书直接参与邮件/Slack 的协调对话，不需要用户介入。Blockit、Lindy 为代表。
- **全平台 AI 日历型（全栈 AI）**：把日历做成一个 AI-native 产品——不只是优化现有日历，而是从底层重建日历体验。Toki（上下文记忆、Trigger、Seed 等概念）为代表。
- **套件内置型**：Google Calendar Gemini、Microsoft Copilot for Outlook/Teams 内置的排程辅助——优势是零额外安装，劣势是只能在该生态内工作。

---

## 风险 · 合规 · 隐私（外部框架可对照，非法律意见）

- **日历数据敏感度**：日历包含谁见谁、何时何地、议程标题——比邮件 metadata 更私密。AI scheduling 工具理论上能看到你**所有**事件，隐私风险远大于普通 SaaS。
- **跨组织授权边界**：当 AI 对外部联系人发邮件/Slack 时，它是否被正确标识为「bot」？对方是否知道自己在跟 AI 协商？多法域（EU AI Act、CCPA、PIPL）对自动化代理的透明度有不同要求。
- **日历访问权限膨胀**：部分工具（如 Blockit）要求全日历读写权限才能正常工作——如果账户被攻破，攻击者能读取并修改所有事件。
- **幻觉型日程**：AI 建议了不存在的时间段、错误的参与者、无中生有的地点；比会议纪要幻觉更危险——直接导致两人白跑一趟。
- **公平性与可用时段**：如果 AI scheduling 默认优先「先到先得」，热门同事的日历永远被更快的请求填满；如果按组织层级加权，可能固化权力结构。
- **数据训练风险**：日历数据是否用于训练模型？用户是否可选择 opt-out？B2B 企业采购的核心条款。

---

## 落地碎片（无先后）

- 先决定场景：**纯内部协调**还是**含外部客户/候选人**。外部场景默认更保守——booking link 比 agent 型风险低。
- 「AI 排日程」≠「不要人确认」。把 AI 输出当草稿，重要会议仍需人类最终确认——尤其是涉及外部人员时。
- 选工具看日历生态：Google Workspace 团队用 Reclaim/Clockwise 更顺；Outlook 团队注意权限兼容性。
- 为团队设定偏好规则前先对齐：所有人的「无会议日」「缓冲时间」「优先级排序」应该在 AI 排程之前就达成共识，而非让 AI 替你做这个决定。
- 警惕权限累积：定期审计哪些应用有日历读写权限；离职前先撤销日历连接的 AI 工具。

---

## 工具与产品类型（「AI scheduling」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **AI scheduling assistant** | Agent 代你协调时间、在邮件/Slack 中协商 | Blockit、Lindy；与 booking link 最大差异在「主动性」 |
| **Smart calendar / calendar AI** | 日历优化、焦点锁定、习惯安排、团队分析 | Reclaim（Clockwise 已于 2026-03 关停，团队加入 Salesforce） |
| **Task + calendar AI** | 任务自动排进日历、动态优先级重排 | Motion；与任务管理工具竞争边界模糊 |
| **Meeting scheduler / booking link** | 分享可用时段链接、自动确认与提醒 | Calendly、Cal.com；AI 最薄但用户最多 |
| **AI-native calendar** | 从零建的新日历产品、上下文记忆、trigger | Toki（域名已迁至 toki.com）；品类最年轻、用户规模最小 |
| **Suite-native scheduling** | Google Calendar Gemini、Outlook Copilot | 生态锁定优势明显，功能迭代慢 |

---

## 外链索引（工具与产品；外链；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Reclaim** | 日历优化 + 习惯/任务自动排程，侧重个人与团队焦点时间保护 | [reclaim.ai](https://reclaim.ai/) |
| **Motion** | 任务与日历统合的 AI 动态排程，输入优先级清单即自动安排 | [usemotion.com](https://www.usemotion.com/) |
| **Calendly** | 分享可用时段链接的品类定义者，2024 起加入 AI 功能 | [calendly.com](https://calendly.com/) |
| **Cal.com** | 开源 Calendly 替代品，自托管或 SaaS，可定制调度规则 | [cal.com](https://cal.com/) |
| **Toki** | AI-native 全平台日历：上下文记忆、Trigger 条件触发、Seed 模糊意图孵化 | [toki.com](https://toki.com/) |
| **Clockwise** | ⚠ 已于 2026-03-27 关停（团队加入 Salesforce，产品下线，用户迁移至 Reclaim） | [getclockwise.com](https://www.getclockwise.com/)（已下线） |
| **Blockit** | AI Agent 代理式排程：邮件/Slack 中直接替你协调时间 | [blockit.com](https://www.blockit.com/) |
| **Lindy** | AI 工作流自动化平台，「调度 Agent」为多场景之一 | [lindy.ai](https://www.lindy.ai/) |
| **Doodle** | 群组投票式排程（经典产品），被收购后定位调整 | [doodle.com](https://doodle.com/) |
| **Trevor AI** | 个人向 AI 任务排程，拖拽式日规划 + AI 建议 | [trevorai.com](https://trevorai.com/) |
| **Vimcal** | 快速日历 UI + AI 辅助，定位为「地球上最快的日历」 | [vimcal.com](https://www.vimcal.com/) |
| **Sidekick AI** | AI 预约与日程协调，侧重团队与外部联系人 | [sidekickai.com](https://www.sidekickai.com/) |

### 对比与测评（第三方；观点非官方）

社区与媒体最常讨论的对比组合是 **Calendly vs Cal.com**（开源 vs 闭源 booking link）和 **Reclaim vs Motion vs Clockwise**（日历优化三重奏）。主流共识：

- **要最简单、最通用** → Calendly（用户心智最强，但 AI 少）
- **要开源/自托管/数据主权** → Cal.com
- **要聚焦时间保护 + 习惯自动安排** → Reclaim
- **要任务和日历合一、AI 动态排程** → Motion（价格更贵，学习曲线更高）
- **要团队日历优化、减少碎片化** → Clockwise
- **要 AI 替你发邮件/Slack 协调** → Blockit 或 Lindy
- **要全新 AI-native 日历体验** → Toki（品类最年轻）

Reddit（r/productivity、r/ADHD）常见槽点集中在：Motion 太贵、Clockwise 团队版价格不明朗、Reclaim 的 habit 安排有时不符合真实能耗周期。多数评测认为「没有全能冠军」——选工具前先决定「你的核心痛点是内部效率还是对外约人」，这两个方向对应完全不同的产品。

*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各厂商自有营销博文为论证主体。*

---

## 延伸阅读与参考材料

- **Cirrus Insight · AI Scheduling Assistant 品类分析（2026-02）**：对 AI scheduling assistant vs booking link vs calendar optimization 的三分类框架与工具对比表。见 [cirrusinsight.com](https://www.cirrusinsight.com/blog/ai-scheduling-assistant-software)。
- **Inc. · A New AI Agent Wants to Schedule Your Life—Should You Let It?（2026）**：对 Blockit 等 agent 型工具的媒体报道与隐私讨论。见 [inc.com](https://www.inc.com/claire-cameron/ai-wants-to-schedule-your-life-and-you-may-want-to-let-it/91251800)。
- **Reddit r/productivity / r/ADHD**：真实用户对 Reclaim、Motion、Clockwise 的长期使用反馈（适合收集槽点而非评测分数）。
