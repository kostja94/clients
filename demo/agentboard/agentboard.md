# AgentBoard - Product Marketing Context

> 主文档。基于官网 [agentboard.cc](https://agentboard.cc/)  
> 复制到 `.cursor/product-marketing-context.md` 或 `.claude/product-marketing-context.md` 供 AI Agent 使用。  
> **状态**：Demo 阶段 | **性质**：小项目、非商业化 | **构建**：Vibe Coding  
> **产品**：新产品，流程尚未完全调通

**关联**：[agentboard-features.md](./agentboard-features.md) · [agentboard-keywords.md](./agentboard-keywords.md) · [agentboard-competitors.md](./agentboard-competitors.md) · [agentboard-use-cases.md](./agentboard-use-cases.md) · [agentboard-project-tasks.md](./agentboard-project-tasks.md) · [元文档-通用文档规范.md](../../通用知识库/元文档-通用文档规范.md)

**Last updated**: 2026-03-30（文档优化：关联与去重）

---

## 项目定位（内部）

| 项目 | 说明 |
|------|------|
| **定位** | **The AI Coding Stats Leaderboard** — AI 编程数据追踪 + 全球排行榜；可类比「Vibe Coding 版的微信运动」 |
| **性质** | 小项目、非商业化；蹭 AI 编码工具热点 |
| **类比** | 微信运动、多邻国打卡、扇贝打卡——每日数据、全球排名、分享卡片 |
| **构建方式** | Vibe Coding |
| **主追踪** | **Claude Code**、**Codex**（官网首页并列展示）；文案另含 **「and more」**（其它工具以官网为准） |
| **产品阶段** | 新产品；流程尚未完全调通 |

---

## 当前需求与优先级（内部）

| 优先级 | 需求 | 说明 |
|--------|------|------|
| **P0** | **完整 SEO 审查** | 全站 SEO 审计；技术 SEO、On-page、索引、爬取等 |
| **P0** | **自建 Blog 页面** | 自己写 Blog 内容；作为内容入口与长尾流量来源 |
| **P1** | 细化 SEO 策略 | 审查完成后，基于结果制定落地策略 |

**最大需求**：SEO 审查 + 自建 Blog 页面。后续在审查基础上做策略细化。

---

## 0. 文档与报告语言策略（实施规则）

**原则**：官网 agentboard.cc 以英文为主；本文档面向中文读者，用于内部沟通与决策。

| 场景 | 语言 | 说明 |
|------|------|------|
| **官网 agentboard.cc** | 英文 | 主站、安装说明、排行榜、Blog、Methodology |
| **文档/报告** | 中文为主 | 策略、分析、解释、待办——给中国人看 |
| **产品原文** | 英文 | 定位、slogan、功能名——保留原文便于对照 |

---

## 1. Product Overview

**官网主标题 / Hero**（英文原文）：
- 副标题：**The AI Coding Stats Leaderboard**
- H1：**Tracked. Ranked. _Shared._**（Shared 为斜体强调）
- 支持句：**Auto-track your Claude Code and Codex sessions. See how you rank on the global leaderboard.**

**One-line description**:
```
AgentBoard is the AI coding stats leaderboard: auto-track Claude Code and Codex sessions, generate shareable stats cards, and rank globally on time, tokens, and productivity boost—one install command (`curl -sL agentboard.cc/install | bash`), optional sign-in to save.
```

**Category**: Developer Tools / AI Coding / Productivity / Leaderboard / DevRel  
**Business model**: 非商业化；免费、无付费计划  
**Pricing**: 免费使用

**产品形态**：
- **Web**：[agentboard.cc](https://agentboard.cc/) — Home、**Leaderboard**、**Resources**（导航）；子链：**Blog**、**Methodology**；登录/认领：**Sign in** → [onboarding](https://agentboard.cc/onboarding)
- **CLI / Install**：`curl -sL agentboard.cc/install | bash`
- **入口**：Sign in（GitHub、Google、X）；终端安装后可与页面自动衔接
- **核心功能**：自动追踪 **Claude Code + Codex** 会话、每日 **stats cards**（多种视觉风格）、**全球排行榜**、社区数据展示

**数据规模**（官网 Community 区）：**2,400+** Daily check-ins、**48M** Tokens tracked、**890** Active users  

**隐私主张**（官网 Privacy & Security）：**No source code ever leaves your machine** — 仅同步汇总统计（时长、Token、工具使用等）；**CLI 开源**，可自行检查上报内容。

---

### 1.1 解决的问题

越来越多人用 AI 写代码（**Claude Code、Codex** 等），但：
- **你每天用 AI 写了多少？** 需要可量化、可对比的数据
- **想晒一下成果？** 需要适合 X / GitHub 等渠道的 **stats cards**
- **谁在全平台最「ship」？** 需要 **公开排行榜**（Today / This Week / All Time）

AgentBoard 把会话数据变成 **Tracked · Ranked · Shared**。

---

### 1.2 怎么用（官网「How it works」三步）

| 步骤 | 英文标题 | 要点 |
|------|----------|------|
| **01** | Run one command | 扫描 **Claude Code** 历史、上传统计、打开个人分享卡片 — **no account needed** |
| **02** | Sign in to save | GitHub / Google / X 认领；**Your terminal auto-connects — no second step** |
| **03** | Code & compete | **Every future Claude Code session syncs automatically**；分享每日卡片、爬榜；`claude # just code normally` |

页内 CTA 链：**[Leaderboard](https://agentboard.cc/leaderboard)** · **[Blog](https://agentboard.cc/blog)** · **[Methodology](https://agentboard.cc/methodology)**

---

## 2. Positioning Statement

> **For** developers who use **Claude Code** and **Codex** and want measurable proof of AI-assisted shipping, **our** AgentBoard **is the** AI coding stats leaderboard **that** tracks sessions automatically, ranks you on **time, tokens, and productivity boost**, and outputs **shareable cards**—**unlike** private dashboards alone, **we** make stats **public, competitive, and shareable**.

---

## 3. Value Proposition & Key Messages

- **Primary value prop**：一行安装、自动追踪 **Claude Code + Codex**、分享卡片、全球榜；零账号可起步。
- **Key messages**（与官网对齐）：
  - "**Tracked. Ranked. Shared.**"
  - "**The AI Coding Stats Leaderboard**"
  - "**Auto-track your Claude Code and Codex sessions.**"
  - "**One command. That's it.**"
  - "**Takes 30 seconds. Works with Claude Code, Codex, and more.**"
  - "**Your code stays yours.**" / "**No source code ever leaves your machine.**"
  - "**Generate beautiful stats cards** from your Claude Code & Codex sessions. Share on X, GitHub, or anywhere."
- **Proof points**：2,400+ daily check-ins、48M tokens tracked、890 active users

---

## 4. Target Audience / ICP

**面向谁**：用 **Claude Code / Codex**（及「more」里其它 AI 编码工具）的开发者与重度用户。

| 类型 | 说明 |
|------|------|
| **专业开发者** | 主用 Claude Code、Codex CLI 等 |
| **Vibe Coding 人群** | 产品经理、设计师、创业者 |
| **共同点** | 需要 **可分享、可排名** 的 AI 编码数据 |

**Pain points**：产量难量化、缺少好看分享物、缺少轻量全球榜  
**Language / locale**：英文主站；全球开发者

---

## 5. Existing Website

- **URL**：https://agentboard.cc/
- **导航**：Home · Leaderboard · Resources（EN）
- **关键路径**：
  - `/` — 首页（Hero + Daily stats 示例 + How it works + Leaderboard 预览 + Community + Privacy + Footer CTA）
  - `/leaderboard` — 排行榜
  - `/blog` — 博客
  - `/methodology` — 方法论
  - `/onboarding` — 登录/认领流程
- **安装命令**：`$ curl -sL agentboard.cc/install | bash`
- **登录**：GitHub、Google、X
- **页脚**：GitHub · Privacy · Terms — **© 2026 AgentBoard**
- **Tech stack**：未公开；**构建方式**：Vibe Coding
- **Current state**：Demo / 早期；强调 **Claude Code + Codex**；新产品、流程尚未完全调通

*功能详情、指标口径、卡片类型 → [agentboard-features.md](./agentboard-features.md)*

---

## 6. Keywords

> 全文见 [agentboard-keywords.md](./agentboard-keywords.md)（§1–5 主表与待办；§7 扩展簇；§8 策略）。

**核心词**（摘录）：AgentBoard、AI coding stats leaderboard、Claude Code tracker、Codex stats、AI coding productivity boost。

---

## 7. Competitors

> 全文见 [agentboard-competitors.md](./agentboard-competitors.md)（含对比矩阵、§七 同受众非竞品）。

**差异化（摘录）**：公开排行榜 + 多风格 **stats cards** + 个人主页 + 一键安装；**双引擎（Claude Code + Codex）** 同日展示。

**同受众非竞品**（Wrapped / Year in Code 类）：非功能替代、可并列话题；产品列表与话术 → [agentboard-competitors.md §七](./agentboard-competitors.md)。

---

## 8. Brand & Voice

- **Voice**：极简、开发者友好、数据驱动、可分享
- **Tone**：强调 **Tracked / Ranked / Shared**、**One command**、**global leaderboard**、**privacy-first（code stays local）**
- **Avoid**：过度营销、企业腔
- **Preferred terms**："leaderboard"、"stats cards"、"AI equivalent"、"boost"、"Claude Code"、"Codex"

---

## 9. 产品功能（概要）

> 完整功能、追踪指标、安装流程 → [agentboard-features.md](./agentboard-features.md)

**核心流程**：Run one command → Sign in to save → Code & compete  
**核心能力**：
- **Stats cards**：多种风格（含 Daily Wrapped、终端风、复古 UI 等官网展示样式）
- **排行榜**：Today / This Week / All Time；维度含 **Human（Active Time）**、**AI Equivalent**、**Boost**、Tokens、Sessions
- **隐私叙事**：无源码上传、最小数据、CLI 开源可审计

---

## 10. 文档互引

> **本表为全项目文档索引的权威来源**；其它文档不重复粘贴同表，仅链回本节。撰写与维护规范 → [元文档-通用文档规范.md](../../通用知识库/元文档-通用文档规范.md)。

| 文档 | 用途 | 何时查阅 |
|------|------|----------|
| [README.md](./README.md) | 目录入口、《文档优化指导》链接 | 从文件夹进入、规范自检 |
| [agentboard.md](./agentboard.md) | 主文档、产品概览、定位、受众 | 了解产品全貌 |
| [agentboard-features.md](./agentboard-features.md) | 功能详情、追踪指标、安装流程 | 查功能、指标、安装 |
| [agentboard-keywords.md](./agentboard-keywords.md) | 关键词映射、URL、§7 扩展簇、§8 策略 | 写文案、SEO、Blog 选题 |
| [agentboard-competitors.md](./agentboard-competitors.md) | 竞品分析、差异化、§七同受众（Wrapped 类） | 对比、Alternatives、社群话术 |
| [agentboard-use-cases.md](./agentboard-use-cases.md) | 使用场景、角色、触发 | 写内容、Use cases 页 |
| [agentboard-project-tasks.md](./agentboard-project-tasks.md) | 项目任务、Phase 0–5 | 执行任务、更新进度 |

---

## Quick Reference

| Section | 用途 |
|---------|------|
| 项目定位 | 性质、类比、构建方式 |
| 当前需求与优先级 | P0：SEO 审查、Blog 页面；详见 [agentboard-project-tasks.md](./agentboard-project-tasks.md) |
| 1–4 | 产品概览、定位、受众 |
| 5 | 网站结构、安装命令、页内链接 |
| 6–7 | 关键词（含 [agentboard-keywords.md §7–8](./agentboard-keywords.md)）、竞品 → 见对应文档 |
| 8 | 文案、CTA、Brand Voice |
| 9 | 功能概要 → 详见 [agentboard-features.md](./agentboard-features.md) |

---

*来源：官网 [agentboard.cc](https://agentboard.cc/)（2026-03-30 核对）*  
*文档维护：[元文档-通用文档规范.md](../../通用知识库/元文档-通用文档规范.md)*
