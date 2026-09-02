# AI 日程安排 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI scheduling / AI 日程安排**——用 AI/ML 替代或缩减人工排日程决策链路，从「双方翻日历找空档」迁移到 **AI 代理自动匹配、协商、预约、提醒、重排**；与纯 booking link 的分界见 §词汇锚点。本页为 **AI 日程安排 SSOT**（完整 URL 表仅此一处）；会议记录 → [note-taker.md](note-taker.md)；任务日历合一（Motion）→ 亦见 [project-management.md](project-management.md) Type E。

**材料范围**：公开网络检索（厂商官网、社区讨论、第三方评测与行业对比文摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 2026-05-10。

**站内对照**：待上线 Tools 页时对齐（建议 slug：`ai-scheduling`，路由 `/tools/ai-scheduling`、`/zh/tools/ai-scheduling`）。

**Tools 关键词与 slug 映射**：待 `tools-pages-config.ts` 收录后补 [`alignify-keywords-tools.md`](../../keywords/alignify-keywords-tools.md) 锚点。

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI 日程安排 / AI scheduling（本文件所指）**：用 AI/ML 替代或缩减人工排日程决策链路的产品类别。**与纯共享可用时段链接（booking link）** 的核心分界在于：后者仍是人发链接、人选时段，AI 只做了「可预约」端的结构化，而非「协调」端。
- **Booking link / 预订链接**：Calendly 式「分享你的空闲时段，让对方选」的模式——AI 程度低，但用户认知极深，常被混入「AI scheduling」检索结果。
- **Calendar optimization / 日历优化**：在已有日历上做冲突检测、焦点时间保护、团队协调——侧重**内部效率**而非外部约见。代表：Reclaim。
- **Agentic scheduling / 代理式排程**：AI 作为「数字秘书」主动参与邮件、Slack 线程协调时间，甚至两个 Blockit 用户的 Agent 直接协商。代表：Blockit、Lindy。
- **Task + calendar unification / 任务日历合一**：把待办任务自动塞进日历空档——是「排程」与「任务管理」的交叉品类。代表：Motion。
- **Smart availability / 智能可用时段**：不只暴露「日历有空」，而是根据优先级、通勤、偏好地点智能推荐时段。
- **Group scheduling / 群组排程**：多人 >3 的协调，难度指数上升。

---

## 专题对照 / 扩展定义

**AI Scheduling vs AI Note Taker**——解决问题根本不同；会议记录 SSOT → [note-taker.md](note-taker.md)。

| 维度 | **AI Scheduling（本页）** | **AI Note Taker** |
|------|------------------------|-------------------|
| **核心问题** | 何时、何地见面 | 会上说了什么 |
| **时机** | 会前协调 | 会中/会后处理 |
| **输出物** | 日历事件、确认 | 转写稿、纪要、行动项 |

产品规格 → **§外链索引**；形态路线 → **§形态谱系**。

---

## 问题域（为何会出现这类产品）

- **协调成本隐性膨胀**：知识工作者每周约 **4-6 小时**花在排日程上——AI scheduling 的直接价值主张就是回收这部分时间。
- **时间碎片化**：连续排程导致焦点时间被侵蚀——Calendar optimization 类工具正是针对这一痛点。
- **跨时区/跨组织协调复杂**：远程 + 全球分布的团队让「找一个大家都可以的时间」变成多约束优化——更适合机器。
- **任务管理断层**：任务列表和日历长期割裂——Motion 类产品填补这个 gap。
- **偏好隐式化**：传统排程靠人默认假设——AI 能学习并编码这些偏好，减少每次协调时的重复沟通。
- **个人助理的数字化替代**：高管助理本身就是一种「排程服务」，AI scheduling 试图将其部分能力产品化、规模化。

---

## 能力栈（概念拆分，非厂商功能表）

- **可用时段暴露**：日历同步 → 规则筛选（工作时间、缓冲、最大会议数）→ 生成可预约窗口——所有 scheduling 工具的最小公分母。
- **偏好模型**：个人级（安静时间、能量周期、通勤时间）vs 组织级（团队规范、会议日策略）。
- **冲突解决策略**：刚性（不可移动的事件）vs 柔性（AI 可建议重排）；跨人冲突时需协商协议。
- **智能建议**：「这周哪天适合 1v1？」「三周内最早能约到的时间？」——从暴露可用时段升级为主动推荐。
- **代理式协调**：Agent 通过邮件/Slack 代你回复、协商时间；Agent-to-agent 是最激进的形态。
- **任务→时间映射**：把任务清单中的 deadline、预估耗时、优先级 → 自动填进日历空档。
- **团队分析**：可视化「会议太多」「碎片化严重」「无会议日执行率」等团队级指标。
- **多平台集成深度**：Google Calendar、Outlook、Apple Calendar 的 API 能力不对称，限制了工具能做到的粒度。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | Booking link 型（低 AI）：分享链接、对方选时间 | Meeting scheduler / booking link | Calendly、Cal.com |
| **B** | 个人日历优化型（中 AI）：焦点时间保护、习惯安排 | Smart calendar / calendar AI | Reclaim |
| **C** | 任务日历统合型（高 AI）：AI 动态排程 | Task + calendar AI | Motion |
| **D** | Agent 代理型（最高 AI）：邮件/Slack 中协调时间 | Agentic scheduling | Blockit、Lindy |
| **E** | 全平台 AI 日历型：AI-native 产品 | AI-native calendar | Toki |
| **F** | 套件内置型：Google Calendar Gemini、Outlook Copilot | Suite-native scheduling | Microsoft / Google 生态 |

**注意**：Clockwise 已于 2026-03-27 关停（团队加入 Salesforce）——见 §外链索引。

---

## 风险 · 合规 · 隐私（外部框架可对照，非法律意见）

- **日历数据敏感度**：日历包含谁见谁、何时何地、议程标题——比邮件 metadata 更私密。
- **跨组织授权边界**：当 AI 对外部联系人发邮件/Slack 时，对方是否知道自己在跟 AI 协商？
- **日历访问权限膨胀**：部分工具要求全日历读写权限才能正常工作——如果账户被攻破，攻击者能读取并修改所有事件。
- **幻觉型日程**：AI 建议了不存在的时间段、错误的参与者、无中生有的地点。
- **公平性与可用时段**：AI scheduling 默认优先「先到先得」可能固化权力结构。
- **数据训练风险**：日历数据是否用于训练模型？B2B 企业采购的核心条款。

---

## 落地碎片（无先后）

- 先决定场景：**纯内部协调**还是**含外部客户/候选人**。外部场景默认更保守——booking link 比 agent 型风险低。
- 「AI 排日程」≠「不要人确认」。把 AI 输出当草稿，重要会议仍需人类最终确认。
- 选工具看日历生态：Google Workspace 团队用 Reclaim 更顺；Outlook 团队注意权限兼容性。
- 为团队设定偏好规则前先对齐：所有人的「无会议日」「缓冲时间」应该在 AI 排程之前就达成共识。
- 警惕权限累积：定期审计哪些应用有日历读写权限；离职前先撤销日历连接的 AI 工具。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| **Reclaim** | B | 日历优化 + 习惯/任务自动排程，侧重个人与团队焦点时间保护 | [reclaim.ai](https://reclaim.ai/) |
| **Motion** | C | 任务与日历统合的 AI 动态排程，输入优先级清单即自动安排 | [usemotion.com](https://www.usemotion.com/) |
| **Calendly** | A | 分享可用时段链接的品类定义者，2024 起加入 AI 功能 | [calendly.com](https://calendly.com/) |
| **Cal.com** | A | 开源 Calendly 替代品，自托管或 SaaS，可定制调度规则 | [cal.com](https://cal.com/) |
| **Toki** | E | AI-native 全平台日历：上下文记忆、Trigger 条件触发、Seed 模糊意图孵化 | [toki.com](https://toki.com/) |
| **Clockwise** | B | ⚠ 已于 2026-03-27 关停（团队加入 Salesforce，用户迁移至 Reclaim） | [getclockwise.com](https://www.getclockwise.com/)（已下线） |
| **Blockit** | D | AI Agent 代理式排程：邮件/Slack 中直接替你协调时间 | [blockit.com](https://www.blockit.com/) |
| **Lindy** | D | AI 工作流自动化平台，「调度 Agent」为多场景之一 | [lindy.ai](https://www.lindy.ai/) |
| **Doodle** | A | 群组投票式排程（经典产品） | [doodle.com](https://doodle.com/) |
| **Trevor AI** | C | 个人向 AI 任务排程，拖拽式日规划 + AI 建议 | [trevorai.com](https://trevorai.com/) |
| **Vimcal** | B | 快速日历 UI + AI 辅助，定位为「地球上最快的日历」 | [vimcal.com](https://www.vimcal.com/) |
| **Sidekick AI** | D | AI 预约与日程协调，侧重团队与外部联系人 | [sidekickai.com](https://www.sidekickai.com/) |

### 对比与测评（第三方；观点非官方）

社区与媒体最常讨论的对比组合是 **Calendly vs Cal.com** 和 **Reclaim vs Motion vs Clockwise**（后者已关停）。主流共识：

- **要最简单、最通用** → Calendly
- **要开源/自托管/数据主权** → Cal.com
- **要聚焦时间保护 + 习惯自动安排** → Reclaim
- **要任务和日历合一、AI 动态排程** → Motion（价格更贵，学习曲线更高）
- **要 AI 替你发邮件/Slack 协调** → Blockit 或 Lindy
- **要全新 AI-native 日历体验** → Toki（品类最年轻）

Reddit（r/productivity、r/ADHD）常见槽点：Motion 太贵、Reclaim 的 habit 安排有时不符合真实能耗周期。多数评测认为「没有全能冠军」——选工具前先决定「核心痛点是内部效率还是对外约人」。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- **Cirrus Insight · AI Scheduling Assistant 品类分析（2026-02）**：[cirrusinsight.com](https://www.cirrusinsight.com/blog/ai-scheduling-assistant-software)
- **Inc. · A New AI Agent Wants to Schedule Your Life（2026）**：[inc.com](https://www.inc.com/claire-cameron/ai-wants-to-schedule-your-life-and-you-may-want-to-let-it/91251800)
- **Reddit r/productivity / r/ADHD**：真实用户对 Reclaim、Motion 的长期使用反馈