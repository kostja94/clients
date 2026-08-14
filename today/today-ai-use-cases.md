# Today AI — 使用场景

**Last updated**: 2026-08-12 | 来源：官网 Use Cases 滑动条（9 张卡片实况）

---

## 1. 官网 Use Cases 九角色（事实来源）

官网 Use Cases 滑动条共 9 张卡片，统一句式：**Today helped a [角色] + [动作]**。

| # | 角色 | 官方文案（动作） | 对应能力 | 资产 |
|---|------|-----------------|---------|------|
| 1 | **writer** | rebuild a research trail | Living Memory + Tasks | `writer-research.png` |
| 2 | **cat mom** | spot a quiet health pattern | Health 信号 + Proactive | `cat-mom-health.png` |
| 3 | **teacher** | make room for rest | Proactive + Morning Brief | `teacher-rest.png` |
| 4 | **marathoner** | keep race prep honest | Memory + Skills | `marathoner-race-prep.png` |
| 5 | **young parents**（无 a） | calm the daily routine | Memory + Tasks | `young-parents-routine.png` |
| 6 | **freelancer** | prepare for tax season | Tasks + Proactive | `freelancer-tax-season.png` |
| 7 | **couple** | track savings goals | Tasks + Memory | `couple-savings.png` |
| 8 | **musician** | keep practice moving | Memory + Routine | `musician-practice.png` |
| 9 | **founder** | turn chaos into next steps | Proactive + Execution | `founder-next-steps.png` |

**卡片结构**：人物实景图 + 底部两行叠加文字。第一行「Today helped a」+ 高亮色块角色词（每角色一种柔和底色：蓝/紫/粉/灰等）；第二行小图标 + 动作短语。卡片圆角约 24px，横向无限 marquee 滚动，两端渐隐遮罩。

> 实现现状（Lovable 项目）：9 张卡已存在于首页 Proactive 区块底部（`bottomCards`，assets 齐全），但为普通横向滚动；独立 `#use-cases` 区块目前仅标题、无卡片。

---

## 2. Persona 归纳（分析）

九角色可归纳为四个方向，官网以角色切片表达同一核心叙事（living memory + proactive）：

| 方向 | 角色 | 核心痛点 | 官网文案表达的承诺 |
|------|------|---------|-------------------|
| **创作者/知识工作** | writer、musician、teacher | 材料散落、练习/休息被挤压 | 重建研究脉络、保持练习推进、为休息腾出空间 |
| **健康/生活觉察** | cat mom、marathoner | 信号藏在一堆数据里 | 发现安静的健康模式、保持备赛诚实 |
| **家庭/财务管理** | young parents、couple | 日常琐碎多线程 | 安抚日常节奏、追踪储蓄目标 |
| **独立职业/创业者** | freelancer、founder | 事事亲为、易陷混乱 | 准备报税季、把混乱变成下一步 |

---

## 3. 场景 ↔ 功能 ↔ 关键词映射（分析）

| 场景 | 角色 | 功能 | 关键词 | 承接页 |
|------|------|------|--------|--------|
| 重建研究脉络 | writer | Living Memory + Tasks | AI with memory | `/landing#memories` |
| 健康模式觉察 | cat mom | Health 信号 + Proactive | AI health assistant | `/landing#proactive` |
| 休息优先级 | teacher | Proactive + Morning Brief | AI morning brief | `/landing#proactive` |
| 备赛诚实 | marathoner | Memory + Skills | — | `/landing#memories` |
| 日常安抚 | young parents | Memory + Tasks | — | `/landing#use-cases` |
| 报税准备 | freelancer | Tasks + Proactive | AI for freelancers | `/landing#capabilities` |
| 储蓄目标 | couple | Tasks + Memory | — | `/landing#use-cases` |
| 练习推进 | musician | Memory + Routine | — | `/landing#memories` |
| 混乱→下一步 | founder | Proactive + Execution | AI for founders | `/landing#proactive` |

---

*关联：[主文档](./today-ai.md) | [capabilities](./today-ai-capabilities.md) | [keywords](./today-ai-keywords.md) | [competitors](./today-ai-competitors.md) | [site-structure](./today-ai-site-structure.md) | [growth-strategy](./today-ai-growth-strategy.md)*

*Last updated: 2026-08-12*
