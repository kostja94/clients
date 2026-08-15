# AgentBoard 竞品分析

> 本文档专注**竞品**：直接竞品、间接竞品、替代方案、企业级、对比矩阵、差异化；另附 **同受众非竞品**（Year in Code / Wrapped 类）。  
> **关联**：[agentboard.md](./agentboard.md)（主文档）| [agentboard-use-cases.md](./agentboard-use-cases.md)（§五 场景差异）| [agentboard-keywords.md §7–8](./agentboard-keywords.md)（同受众关键词）| [文档索引表 §10](./agentboard.md#10-文档互引)

**Last updated**: 2026-03-30（文档优化：去重导航）

---

## 一、竞品分类

| 类型 | 说明 | 代表 |
|------|------|------|
| **直接竞品** | AI 编码统计 + 追踪；Claude Code / Codex 等 | Agent Stats、Code Insights、Cursor Stats Extension |
| **间接竞品** | 通用编码时间追踪；部分支持 AI | WakaTime、VibeLog |
| **替代方案** | 用量/限额监控；非统计导向 | OpenUsage、Price Per Token |
| **企业级** | 团队 AI 生产力分析；B2B | LinearB、DX、Harness |
| **同受众非竞品** | 关心编程/AI 用量、爱分享；形态为 **年度/月度 Wrapped**，非「日更 + 全球榜」 | 见 **§七** |

---

## 二、直接竞品

### 2.1 Agent Stats

| 项目 | 说明 |
|------|------|
| **URL** | [agentstats.dev](https://agentstats.dev/) |
| **形态** | VS Code 扩展 + Web Dashboard |
| **支持** | Claude Code、GitHub Copilot、Cursor；OpenAI、Anthropic、Google 等 |
| **核心** | 实时成本追踪、API 调用监控、项目管理、详细报告 |
| **数据** | 云端同步；需账号 |
| **定位** | 成本/用量分析；B2B 倾向 |

**与 AgentBoard 差异**：Agent Stats 偏成本/用量；AgentBoard 偏社交证明、排行榜、分享卡片。

---

### 2.2 Code Insights

| 项目 | 说明 |
|------|------|
| **URL** | [code-insights.app](https://code-insights.app/) |
| **形态** | CLI（npm）+ 本地 Web Dashboard |
| **支持** | Claude Code、Cursor、Codex CLI、Copilot CLI、VS Code Copilot Chat |
| **核心** | 会话知识提取、Prompt 质量评分、使用分析、成本拆解 |
| **数据** | 本地 SQLite；无账号、无云端 |
| **定位** | 个人知识库、Prompt 优化、会话分析 |

**与 AgentBoard 差异**：Code Insights 偏深度分析、决策提取；AgentBoard 偏轻量、分享、排行榜。

---

### 2.3 Cursor Stats Extension

| 项目 | 说明 |
|------|------|
| **URL** | [Chrome Web Store](https://alexerm.github.io/cursor-stats-extension/) |
| **形态** | Chrome 扩展 |
| **支持** | Cursor |
| **核心** | 交互图表、月度预算、Agent 消息日历、接受建议统计、Token 分析 |
| **数据** | 云端同步；需账号 |
| **定位** | Cursor 专用；成本/用量可视化 |

**与 AgentBoard 差异**：仅 Cursor；无 Claude Code；无排行榜、分享卡片。

---

### 2.4 CC Wrapped（Claude Code Wrapped）

| 项目 | 说明 |
|------|------|
| **来源** | [DEV.to 文章](https://dev.to/yurukusa/i-built-spotify-wrapped-for-claude-code-heres-what-3400-sessions-look-like-21e2) |
| **形态** | 个人项目/工具 |
| **支持** | Claude Code |
| **核心** | 7 张动画卡片；8 种人格类型（Night Owl、Weekend Warrior、Marathon Runner 等） |
| **定位** | 类 Spotify Wrapped；分享导向 |

**与 AgentBoard 差异**：CC Wrapped 为一次性/年度回顾；AgentBoard 为每日/持续、排行榜、社交竞争。

---

## 三、间接竞品与替代方案

### 3.1 WakaTime

| 项目 | 说明 |
|------|------|
| **URL** | [wakatime.com](https://wakatime.com/) |
| **形态** | 插件（89+ 编辑器）+ Web Dashboard |
| **支持** | VS Code、IntelliJ、Vim 等；**Claude Code 插件**（GitHub: wakatime/claude-code-wakatime） |
| **核心** | 自动编码时间；按项目/文件/分支/语言；私有排行榜；AI 生成行数追踪 |
| **数据** | 云端；需账号 |
| **定位** | 通用编码时间；500k+ 开发者 |

**与 AgentBoard 差异**：WakaTime 通用；AgentBoard 专注 **Claude Code / Codex** 等 AI 编码场景；AgentBoard 有公开排行榜、分享卡片。

---

### 3.2 OpenUsage

| 项目 | 说明 |
|------|------|
| **URL** | [openusage.ai](https://openusage.ai/) |
| **形态** | macOS 菜单栏；开源（Tauri + React + TypeScript） |
| **支持** | Cursor、Claude、Codex、Copilot、Gemini、Windsurf 等 15+ |
| **核心** | 用量/限额监控；Session/Weekly 剩余；重置时间 |
| **数据** | 本地；无云端 |
| **定位** | 防止超限；不关注统计/分享 |

**与 AgentBoard 差异**：OpenUsage 偏限额；AgentBoard 偏统计、分享、排行榜。

---

### 3.3 VibeLog

| 项目 | 说明 |
|------|------|
| **URL** | [vibelog.tech](https://vibelog.tech/) |
| **形态** | Session 追踪器 |
| **支持** | Cursor、GitHub Copilot、Claude Code |
| **核心** | 面向自由职业者/机构；客户报告；工时证明；审计轨迹 |
| **定位** | B2B；工时计费；客户证明 |

**与 AgentBoard 差异**：VibeLog 偏 B2B 计费；AgentBoard 偏个人社交、排行榜。

---

### 3.4 Price Per Token

| 项目 | 说明 |
|------|------|
| **URL** | [pricepertoken.com](https://pricepertoken.com/coding-tracker) |
| **形态** | 实时 LLM 定价 + 个人 Dashboard；MCP Server |
| **支持** | Claude Code、Cursor |
| **核心** | 成本/用量追踪；Dashboard |
| **定位** | 成本监控 |

**与 AgentBoard 差异**：偏成本；无排行榜、分享卡片。

---

## 四、企业级（非直接对标）

| 产品 | 说明 | 与 AgentBoard 关系 |
|------|------|-------------------|
| **LinearB** | 50+ AI 工具；AI 活动与交付指标（周期、吞吐、质量）关联 | 企业级；AgentBoard 个人级 |
| **DX** | Claude Code 组织级用量；团队结构、ROI 量化 | 企业级；AgentBoard 个人级 |
| **Harness AI Productivity Insights** | 对比 AI 用户 vs 非用户；速度、质量、问卷 | 企业级；AgentBoard 个人级 |

---

## 五、竞品对比矩阵

| 维度 | AgentBoard | Agent Stats | Code Insights | WakaTime | OpenUsage |
|------|------------|-------------|---------------|----------|-----------|
| **Claude Code** | ✅ | ✅ | ✅ | ✅（插件） | ✅ |
| **Codex** | ✅ | ❌ | ✅ | ❌ | ✅ |
| **Cursor** | ✅* | ✅ | ✅ | ❌ | ✅ |
| **公开排行榜** | ✅ | ❌ | ❌ | ❌（私有） | ❌ |
| **分享卡片** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **一键安装** | ✅ | 扩展 | npm | 插件 | 下载 |
| **无需账号** | ✅ | ❌ | ✅ | ❌ | ✅ |
| **数据** | 云端 | 云端 | 本地 | 云端 | 本地 |
| **定位** | 社交证明、排行榜 | 成本/用量 | 知识/分析 | 通用编码 | 限额监控 |

\* **AgentBoard** 现网首页主推广 **Claude Code + Codex**（[agentboard.cc](https://agentboard.cc/)）；文案 **「Claude Code, Codex, and more」** — Cursor 等归入 *more*，以产品更新为准。旧版矩阵中 AgentBoard「Codex 🔜」已过时。

---

## 六、AgentBoard 差异化总结

| 差异化点 | 说明 |
|----------|------|
| **定位** | Vibe Coding 排行榜平台；「Vibe Coding 版的微信运动」——每日数据、打卡式、排行榜、社交分享 |
| **唯一性** | 公开排行榜 + 分享卡片（多种风格）+ 个人主页（@用户名）+ 一键安装 + 零门槛 |
| **竞品空白** | 无直接竞品同时做「AI 编码统计 + 公开排行榜 + 分享卡片 + 个人主页」 |
| **目标** | 所有用 AI 写代码的人（开发者、产品经理、设计师、创业者）；社交证明；非商业化 |

---

## 七、同受众非竞品：Year in Code / 2025 Wrapped 类

**定位**：以下产品 **不算 AgentBoard 的竞品**（无同构的「持续同步 + Claude Code/Codex 双引擎 + 公开日/周/总榜」组合），但 **受众高度重叠**——**关注自己 coding / AI 用量、愿意在 X/GitHub 等渠道分享的开发者爱好者**；内容营销、社群语境中常与 AgentBoard 出现在同一讨论里。

| 项目 | URL | 形态与数据 | 与 AgentBoard 关系 |
|------|-----|------------|-------------------|
| **2025 Compiled** | [2025compiled.com](https://www.2025compiled.com/) | **Claude Code 插件**；本地约 **30 天** transcript；生成 **Wrapped 式**回顾（prompt、代码量、persona 等）；Parcha 社区项目，非 Anthropic 官方 | 同属「Claude Code 可视化 + 可分享」；**一次性/插件/月度窗口**，无 AgentBoard 式 **持续榜** |
| **Year in Code（独立站）** | [yearincode.xyz](https://yearincode.xyz/) | 浏览器内 **2025 Wrapped**；**GitHub** 或 **Claude Code JSON 上传**；强调数据不离开浏览器 | 「Spotify Wrapped for AI coding year」叙事；**单次生成**，非日更同步 |
| **Year in Code 2025（Graphite）** | [year-in-code.com](https://year-in-code.com/) | **GitHub 登录**；**commits / streaks / milestones**，与全球开发者对比 | **Git 年度维度**；非 Claude/Codex 会话日志主路径 |
| **Year in Code 2025（Cursor 官方）** | [cursor.com/2025](https://cursor.com/2025) | **Cursor 官方**年度数据入口；服务 **Cursor 用户** | 与 AgentBoard **数据源/品牌**不同；同属「Year in Code」营销品类 |

**小结**：

- **竞品判断**：按功能替代性，上表 **不作为直接/间接竞品** 进对比矩阵（§五）。  
- **受众判断**：同一批 **「用量可视化 + 社交分享」** 爱好者——适合在 **Blog、社群、Reddit/X** 中作为 **并列话题**（「除了 Wrapped，还有每日榜 / stats cards」），而非「二选一替代」话术。
- **SEO 关键词**（Wrapped 叙事、用量统计、排行榜等英文/中文词与策略）→ [agentboard-keywords.md §7–8](./agentboard-keywords.md)。

---

**文档索引**（全表）→ [agentboard.md §10 文档互引](./agentboard.md#10-文档互引)

---

*来源：网络搜索（2026-03）、OpenUsage、Code Insights、WakaTime、Agent Stats、DEV.to、2025compiled、yearincode.xyz、year-in-code.com、cursor.com/2025 等*
