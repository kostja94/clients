
# Bridge — 使用场景

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./bridge-surf.md) | [features](./bridge-surf-features.md) | [keywords](./bridge-surf-keywords.md) | [competitors](./bridge-surf-competitors.md) | [site-structure](./bridge-surf-site-structure.md) | [growth-strategy](./bridge-surf-growth-strategy.md)

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **P1: 独立开发者** | Solo dev / indie hacker，同时负责开发+运营+产品，Mac 用户 | 日常需在 VSCode → 终端 → 浏览器 → Figma → Slack 之间频繁切换；大量重复性操作（部署、测试、报告）占据时间 | 让 AI Agent 跨工具完成端到端开发任务：改 Bug、部署、发版通知、抓数据分析 | 高 |
| **P2: 技术创业者/Operator** | 早期创业公司 founder 或运营负责人，需同时管产品、数据、团队沟通 | 每天在多个 SaaS 工具间切换（Notion, Linear, Slack, 数据看板），手动汇总信息、生成报告耗时巨大 | 让 AI 自动汇总各工具信息生成周报、监控关键指标、执行标准化工作流 | 中高 |
| **P3: 创意工作者** | 设计师、视频创作者、摄影师，Mac 重度用户 | 桌面/下载文件夹长期混乱，素材库管理耗时；多版本文件难以追踪 | AI 自动整理素材库、按项目/时间/风格分类、管理版本 | 中 |
| **P4: 知识工作者** | 远程办公的产品经理、研究员、咨询顾问 | 文件系统混乱（"桌面全是截图和 PDF"），手动整理费时且难以坚持；缺乏统一的组织方法论 | 一键自动整理所有文件，AI 选择最优组织方法，后台持续维护 | 中低 |
| **P5: 开发团队** | 5–20 人技术团队，使用多种 AI 工具和内部系统 | 团队工作流需要标准化但缺乏统一 Agent 平台；不同成员用不同工具链 | 共享 Skills、统一 Agent 行为、安全管理文件操作 | 高 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| P1 | 周五下午，收到一个 Bug 报告，需要修复→部署→通知团队 | "我想告诉 AI '修复登录页的 500 错误，部署到 staging，然后在 Slack 开发频道发一条更新'" | Agent 循环 + Computer Use + 多工具操作 | AI agent fix bug deploy, AI automation developer |
| P1 | 有一个工具/小产品的 idea，想快速验证原型 | "我想对 AI 说 '建一个可以拖拽排序的 Todo 应用'，它自己搭好前端+后端+部署" | 编码 Agent + 沙盒 VM | AI build app prototype, AI code generation |
| P2 | 周一早晨，需要汇总上周各渠道数据生成周报 | "我想让 AI 打开 Linear 看完成的任务 → 打开 Metabase 截图数据 → 汇总成 Notion 周报 → 发 Slack" | Computer Use + Skills（周报 Skill） | AI weekly report automation, AI summarize workflow |
| P2 | 每天早晨，需要检查关键业务指标是否异常 | "我想到公司时 AI 已经检查完所有看板，告诉我有没有异常，有的话自动创建 Linear issue" | 定时任务 + Agent 监控 + 工具操作 | AI dashboard monitoring, AI automated check |
| P3 | 几个月没整理桌面，文件堆了上千个 | "我想一键让 AI 分析我所有文件，按项目/客户/类型自动分类，不用我学什么组织方法论" | 文件智能组织（AI 推荐方法） | AI organize desktop Mac, auto file sorter |
| P3 | 经常需要找某个项目几个月前的设计源文件 | "我想用自然语言搜索 '去年 Q3 为 Acme 客户做的 landing page 设计稿'" | AI 内容理解 + 语义搜索 | AI file search, AI asset management |
| P4 | 尝试过 PARA/GTD 但都半途而废，文件依然混乱 | "我不想学任何方法论，让 AI 帮我选最适合我的组织方式并自动执行" | AI 推荐组织方法 + 自动执行 | PARA method AI, GTD AI organizer |
| P4 | 下载文件夹每月新增 500+ 文件，永远整理不完 | "我设置一次规则后就不想再管了，新文件自动归类" | 后台持续自动化组织 | auto organize downloads, set and forget file organizer |
| P5 | 团队需要一个标准化的部署后检查流程 | "我想创建一个 'post-deploy-check' Skill，任何团队成员都可以让 Bridge 执行同样的检查步骤" | Skills 系统 + 团队共享 | AI skills sharing, team AI workflow |
| P5 | 需要让 AI 操作内部老旧系统（无 API） | "我们的财务系统是 10 年前的，没有 API，我想让 AI 像人一样打开它、读取屏幕、填写表单" | Computer Use（后台 GUI 操作） | AI operate legacy software, screen reading AI |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| Bug 修复→部署→通知 | P1 | Agent 循环 + Computer Use | AI agent developer workflow, AI deployment automation | `/` (待建 `/use-cases/developer`) |
| 原型快速构建 | P1 | 编码 Agent + 沙盒 VM | AI build app, AI code generation | `/` |
| 周报自动汇总 | P2 | Computer Use + Skills | AI weekly report, AI workflow automation | `/` (待建 `/use-cases/operator`) |
| 数据看板监控 | P2 | 定时任务 + Agent | AI dashboard monitor, automated business check | `/` |
| Mac 文件一键整理 | P3, P4 | 文件智能组织 | AI file organizer Mac, auto organize files | `/features` |
| 设计素材语义搜索 | P3 | AI 内容理解 | AI asset search, AI file finder | `/features` |
| 零学习成本文件管理 | P4 | AI 推荐组织方法 | PARA AI Mac, GTD file organizer | `/features` |
| 团队工作流标准化 | P5 | Skills 系统 | AI skills management, team AI workflow | 待建 `/skills` |
| 老旧系统 GUI 自动化 | P5 | Computer Use | AI legacy software, screen automation | `/blog/macos-two-cursors` |

---

## 4. 用户旅程

### 认知 → 考虑 → 转化 → 留存

```
认知阶段（当前主要入口：开源社区）
├─ GitHub trending → 发现 OpenBridge（412 stars）
├─ Hacker News / Reddit r/programming → "Claude Cowork 开源替代"
├─ X/Twitter → @bridge_surf 推文 + 技术博文传播
├─ Google 搜索 "Claude Cowork alternative" → OpenBridge 页面
└─ 技术媒体报道（The Agent Times 等）

考虑阶段
├─ 阅读 OpenBridge GitHub README → 了解技术架构
├─ 阅读博客 "macOS can support two cursors" → 认可技术深度
├─ 对比 Bridge vs Claude Cowork → 评估差异化
├─ 加入 Waitlist → 等待产品发布
└─ 编译/试用 OpenBridge → 体验 Computer Use + 沙盒审查

转化阶段（产品 GA 后）
├─ Waitlist → 获得邀请码 → 注册
├─ Interest 免费层 → 体验核心能力
├─ 首次完成端到端任务 → "Wow moment"（如 30 秒整理 1000 文件）
└─ 升级 Starter/Pro → 配额 + 高级功能

留存阶段
├─ 创建个人 Skills → 工作流固化
├─ 每天让 Bridge 执行例行任务 → 习惯养成
├─ 邀请团队成员 → 病毒传播
├─ 订阅模型成本通过 BYOK 控制 → 使用频率上升
└─ 参与 GitHub 社区 → 成为贡献者/布道者
```

---

## 5. 未覆盖场景

| 场景 | 当前状态 | 机会 |
|------|---------|------|
| **Windows/Linux 用户** | OpenBridge 仅 macOS（Open Cowork 已跨平台） | 跨平台是获客天花板，需在高优先级路线图中 |
| **非技术用户** | Bridge 需要一定技术能力（配置模型、理解 Agent 概念） | 闭源 Bridge 版应封装复杂性，降低 "5 分钟上手" 门槛 |
| **企业合规审计** | 仅提及安全，无 SOC2/ISO 等认证 | 企业版需推进合规认证 |
| **移动端远程控制** | 无 | 竞品 Open Cowork 已支持飞书/Slack 远程控制，Bridge 可补位 |
| **图片/视频 AI 理解** | Computer Use 目前为截图+坐标，无深度视觉理解 | 多模态模型集成后可增强 UI 理解能力 |

---

*Last updated: 2026-07-16*
*Persona 定义基于官网 FAQ 用户画像描述 + GitHub 开源社区特征 + 文件组织功能页使用场景*
