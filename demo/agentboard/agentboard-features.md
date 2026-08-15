# AgentBoard 功能详情

> 本文档专注**功能**：安装、追踪指标、分享卡片、排行榜、隐私、工作流。  
> **关联**：[agentboard.md](./agentboard.md)（主文档）| [agentboard-keywords.md](./agentboard-keywords.md) | [文档索引表 §10](./agentboard.md#10-文档互引)  
> 来源：[agentboard.cc](https://agentboard.cc/)（2026-03-30）

---

## 一、安装与接入

### 1.1 安装命令

```bash
$ curl -sL agentboard.cc/install | bash
```

- **行为**（官网）：扫描 **Claude Code** 历史、上传统计、打开个人分享卡片 — **no account needed**
- **认领**：[Sign in](https://agentboard.cc/onboarding)（GitHub / Google / X）；官网称终端可与页面 **auto-connect**，无需第二步

### 1.2 登录方式

- GitHub  
- Google  
- X (Twitter)

### 1.3 支持平台（与首页一致）

| 平台 | 状态 | 说明 |
|------|------|------|
| **Claude Code** | ✅ 主展示 | 步骤 03 写明 *Every future Claude Code session syncs automatically* |
| **Codex** | ✅ 主展示 | 与 Claude Code 并列出现在 **daily stats**、卡片分区（Claude Code / Codex） |
| **更多** | copy 用语 | 官网 CTA：**「Works with Claude Code, Codex, and more.」** — 其它工具以官网更新为准 |

---

## 二、追踪指标（官网用语）

### 2.1 汇总与时间

| 指标 | 说明 |
|------|------|
| **Active Time** | 总活跃/编码时长（示例：5h 51m） |
| **AI equiv**（AI Equivalent） | AI 等效时长（示例：10h 26m） |
| **Boost** | 生产力倍增（示例：1.8×）；与 **AI equiv**、人类时长联用 |
| **分引擎时长** | 示例：**Claude Code 5h 27m** · **Codex 22m** |

### 2.2 按引擎（Claude Code / Codex 分区）

对 **每个引擎** 展示（官网示例）：

| 指标 | 说明 |
|------|------|
| **Tokens** | 总量；**in · out** 拆分 |
| **Code** | +新增行 / −删除行 |
| **Messages** | 总量；可细分 **AI / User**（如 AI 780 · User 403） |
| **Tool Calls** | 工具调用次数 |
| **Sessions** | 会话数（如 39 sessions） |
| **Projects / Files** | 如 4 proj · 86 files |

### 2.3 官网示例数据（摘录，用于内部对齐文案）

- **Active Time**：5h 51m  
- **AI equiv**：10h 26m · **Boost** 1.8×  
- **Claude Code**：Tokens 432.6K（56.6K in · 432.6K out）；Code +29,093 / −4,917；Messages 1,183；Tool Calls 965；39 sessions；4 proj · 86 files  
- **Codex**：Tokens 56.6K（12.1K in · 44.5K out）；Messages 25；Tool Calls 22；3 sessions；1 proj · 6 files  

*旧版文档中的 Commits / Repos 等字段若与现网不一致，以官网与 CLI 实际输出为准。*

---

## 三、Stats Cards（分享卡片）

- **定位**（官网）：*Generate beautiful stats cards from your Claude Code & Codex sessions. Share on X, GitHub, or anywhere.*
- **内容**：当日（或周期）统计；含 **Active Time**、**AI equiv**、**Boost**、Claude Code / Codex 分块
- **风格**：首页展示多种视觉（终端列表、社交卡片、Daily Wrapped、复古窗口、AGENTBOARD v2.1 等）— 用于传播与品牌展示
- **触发**：安装后打开；后续可分享

---

## 四、排行榜（Leaderboard）

- **URL**：[agentboard.cc/leaderboard](https://agentboard.cc/leaderboard)
- **文案**：*Who's shipping the most?* — *AI coding leaderboard — ranked by **time, tokens, and productivity boost**.*（首页注明示例数据仅供 illustration）
- **周期**：**Today** · **This Week** · **All Time**
- **列表列**（官网表头）：**#** · **User** · **Human** · **AI Equivalent** · **Boost**（并含 sessions、tokens 等展示）
- **可见性**：公开浏览；完整参与需 **Sign in to see your rank**

---

## 五、Resources / 内容入口

| 链接 | 说明 |
|------|------|
| [ /blog ](https://agentboard.cc/blog) | Read the blog |
| [ /methodology ](https://agentboard.cc/methodology) | Our methodology |

---

## 六、隐私与安全（官网整段策略）

| 支柱 | 英文要点 |
|------|----------|
| **No source code uploaded** | Only read **aggregate stats** from local session logs; **Your code never leaves your machine.** |
| **Minimal data by design** | Only **coding time, token counts, and tool usage** synced. |
| **Open source CLI** | CLI fully open source — inspect what gets sent before you run it. |

---

## 七、社区数据（首页）

- **2,400+** Daily check-ins  
- **48M** Tokens tracked  
- **890** Active users  
- 文案：*Tracking their coding productivity across **Claude Code and Codex**.*

---

## 八、工作流（简）

1. `curl -sL agentboard.cc/install | bash` → 扫描 → 打开卡片  
2. Sign in → 认领统计  
3. 日常编码（`claude` 等）→ 自动同步 → 分享卡片、查看 [Leaderboard](https://agentboard.cc/leaderboard)

---

**文档索引**（全表）→ [agentboard.md §10 文档互引](./agentboard.md#10-文档互引)
