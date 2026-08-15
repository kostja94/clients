
# Bridge

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[keywords](./bridge-surf-keywords.md) | [features](./bridge-surf-features.md) | [competitors](./bridge-surf-competitors.md) | [site-structure](./bridge-surf-site-structure.md) | [use-cases](./bridge-surf-use-cases.md) | [growth-strategy](./bridge-surf-growth-strategy.md)

---

## 文档导航

| 文档 | 职责 | 引用 |
|------|------|------|
| [主文档](./bridge-surf.md)（本页） | 概览、ICP、文档索引 | — |
| [bridge-surf-keywords.md](./bridge-surf-keywords.md) | 关键词映射、目标页 | [features](./bridge-surf-features.md) |
| [bridge-surf-features.md](./bridge-surf-features.md) | 功能页：能力、URL | [use-cases](./bridge-surf-use-cases.md) |
| [bridge-surf-competitors.md](./bridge-surf-competitors.md) | 竞品分析、差异化 | [features](./bridge-surf-features.md) |
| [bridge-surf-site-structure.md](./bridge-surf-site-structure.md) | URL 层级、IA、技术栈 | 主文档 |
| [bridge-surf-use-cases.md](./bridge-surf-use-cases.md) | 场景、Persona | [features](./bridge-surf-features.md) |
| [bridge-surf-growth-strategy.md](./bridge-surf-growth-strategy.md) | 增长渠道、内容计划 | [keywords](./bridge-surf-keywords.md) |

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2C/B2B AI Agent 平台 — 桌面自动化与 Agent 操作系统 |
| 网站 | https://bridge.surf/ |
| 当前阶段 | Pre-release / Waitlist（极早期，builder-stage） |
| 核心产品 | Bridge — "The everything agent that works everywhere"：在 Mac 上跨应用执行任务的 AI Agent |
| 产品形态 | macOS 原生桌面应用 + 开源版（OpenBridge） |
| 关键差异化 | ① 本地优先 + BYOK（数据不出本机） ② 沙盒 VM 审查（先审后改） ③ 后台 Computer Use（不抢占焦点，双光标支持） ④ 多 Agent 协作 + Skills 系统 ⑤ 开源（MIT） |
| 目标用户 | 需要 AI 在桌面端"真正完成工作"的技术用户：开发者、创始人、运营人员、设计师、知识工作者 |
| 目标市场 | 全球（英语优先），macOS 用户 |
| 更新日期 | 2026-07-16 |

---

## 1. 产品定位

| 维度 | 内容 |
|------|------|
| 品类 | AI Agent 桌面操作系统 — 属于 "Computer Use Agent" 赛道，定位为 AI 与原生的中间层 |
| 价值主张 | 让 AI 不只回答问题，而是真正动手完成工作——跨应用操作、编码构建、文件整理，"Intent and Done"（意图即完成） |
| 竞争替代 | 用户从手动跨应用操作、Claude Code/Cursor 等纯代码 Agent、或 Zapier/n8n 等固定规则自动化转向 Bridge——核心理由是 **"能操作任意桌面软件"** + **"本地安全"** + **"多 Agent 并行"** |
| 差异化锚点 | ① 本地优先 + BYOK（数据安全不可替代） ② 沙盒审查机制（竞品无） ③ 后台双光标 Computer Use（业界首创） ④ 多 Agent 协作架构 |
| 市场位置 | **开源 + 本地优先 + 平台化**——既不像 Claude Cowork 的封闭订阅，也不像传统 RPA 的固定规则；定位于 "Agent 时代的操作系统层" |

### 1.1 定位简述

Bridge 占据 AI Agent 市场中「本地优先的桌面 Agent 平台」这一独特位置。与 Claude Cowork（云端订阅、封闭生态）和传统 RPA（固定规则、无 AI 理解力）不同，Bridge 以开源 + BYOK + 沙盒审查的组合模式切入——用户既拥有数据控制权（本地优先），又获得 Agent 的智能理解力（多模型支持），还能安全地让 Agent 操控桌面软件（沙盒审查 + 后台操作）。

核心用户是**那些希望 AI 不仅仅是聊天工具，而是真正能动手完成桌面工作流的技术用户**：独立开发者让 Bridge 搭建原型应用，运营人员让 Bridge 跨工具生成周报，设计师让 Bridge 自动整理素材库。Bridge 的 SKILL.md 技能系统意味着用户可以封装自己的重复工作流为可复用技能。

Bridge 存在的最深层原因是：AI 正在从"聊天窗口"走向"操作系统"，而当前市场缺少一个**安全的、开源的、能让用户掌控数据和模型的 Agent 运行环境**。Bridge 试图成为 AI 与 macOS 之间的"桥"——这也是名字 Bridge 的寓意。其开源策略（OpenBridge, MIT License, 412 stars）正在建立开发者社区信任，这是封闭竞品无法复制的护城河。

---

## 2. 产品信息

Bridge 是 AFK AI, Inc.（Away From Keyboard）旗下的 AI Agent 桌面平台，目前处于 pre-release waitlist 阶段。产品有两条线：

- **Bridge（闭源托管版）**：面向普通用户，隐藏配置复杂性，提供一站式 Agent 体验
- **OpenBridge（开源版）**：面向开发者和高级用户，MIT License，本地运行，BYOK

技术架构深度整合 macOS：
- **SwiftUI + AppKit** 原生壳 → 产品状态管理
- **kwwk**（自研 Swift Agent SDK）→ Agent 循环与工具执行
- **React/TypeScript WebView** → 聊天与审查界面
- **Go + Virtualization.framework Linux VM** → 沙盒文件操作
- **macOS Accessibility + CGEvent** → 后台 Computer Use

支持 20+ 模型提供商（OpenAI, Anthropic, Google Gemini, DeepSeek 等），OAuth + API Key 双认证。凭据存储在本地 Application Support 目录，不上传任何云端。

> 完整功能清单见 [bridge-surf-features.md](./bridge-surf-features.md)

---

## 3. 关键词摘要

核心关键词围绕 "AI agent"、"computer use agent"、"desktop automation"、"macOS agent" 等品类词，辅以 "Claude Cowork alternative"、"Codex alternative" 等竞品对比词，以及 "AI file organizer Mac" 等功能场景词。

品牌词为 "Bridge"、"bridge.surf"、"OpenBridge"、"AFK AI"。当前内容策略几乎从零开始（仅 2 篇博客），SEO 基础设施（sitemap 500 错误、极简站点）亟待建设。

> 完整关键词策略见 [bridge-surf-keywords.md](./bridge-surf-keywords.md)

---

## 4. 竞品摘要

主要竞品：**Claude Cowork**（Anthropic 官方 Agent 桌面版）、**Codex/OpenAI Codex CLI**、**Open Cowork**（开源 Claude Cowork 替代）、**Cursor/Copilot**（代码 Agent）、传统 RPA 工具（UiPath 等）。

Bridge 核心差异：本地优先 + BYOK（vs 云端闭源）、沙盒审查 + 后台 Computer Use（vs 抢占焦点）、多 Agent 协作（vs 单 Agent）、开源 MIT（vs 闭源或 AGPL）。

> 完整竞品分析见 [bridge-surf-competitors.md](./bridge-surf-competitors.md)

---

## 5. 站点结构摘要

bridge.surf 为极简 pre-release 站点：首页（Waitlist + 一句话定位）、功能页（AI 文件组织）、定价页（结构但无金额）、博客（2 篇）。

开源的 OpenBridge 有独立子域名站点 (`openbridge.bridge.surf`) 和 GitHub 仓库（412 stars, MIT）。公司主页为 `afk.surf`。sitemap.xml 返回 500 错误。

> 完整站点结构见 [bridge-surf-site-structure.md](./bridge-surf-site-structure.md)

---

## 6. 使用场景摘要

主要 Persona：① 独立开发者（原型构建、跨工具开发工作流）、② 技术创业者/operator（周报汇总、数据看板、Slack 监控）、③ 创意工作者（素材库管理、版本控制）、④ 知识工作者（文件整理、信息检索）、⑤ 开发团队（共享 Skills、代码审查）。

核心 JTBD：让 AI 真正操作桌面应用完成端到端任务、安全地让 AI 修改文件、标准化重复工作流。

> 完整场景分析见 [bridge-surf-use-cases.md](./bridge-surf-use-cases.md)

---

## 7. 增长策略摘要

核心渠道（从零起步）：① 开源社区增长（GitHub stars → 开发者口碑 → Hacker News/Reddit） ② 技术内容营销（Computer Use 技术揭秘、"vs Claude Cowork" 对比） ③ X/Twitter 创始人 IP（目前 ~672 关注者，有增长空间） ④ macOS 工具推荐渠道。

当前最大增长瓶颈：产品未公开发布，仅 waitlist。开源版 OpenBridge 已成为主要认知入口。

> 完整增长策略见 [bridge-surf-growth-strategy.md](./bridge-surf-growth-strategy.md)

---

## 8. 优化建议

1. **修复 sitemap.xml 500 错误 + 补全基础 SEO 页面** — 当前站点无法被搜索引擎正常索引。应至少建立 `/about`（团队/愿景）、`/docs`（使用文档）、`/skills`（技能市场）页，并通过 sitemap 提交。

2. **建立 "Bridge vs Claude Cowork" 独立对比页** — 作为最早宣称"Claude Cowork 开源替代"的产品，应抢占此搜索意图。当前仅在 OpenBridge 子域标题提到，缺乏结构化对比内容。

3. **将文件组织功能打造为独立获客引擎** — `/features` 页是目前唯一有 SEO 价值的功能页（"AI file organizer Mac" 搜索意图明确），应单独优化其内容深度，作为从"文件整理"到"Agent 平台"的转化漏斗入口。

4. **加速博客内容生产** — 当前仅有 2 篇博客（2026-05），建议保持 ≥2 篇/月节奏，覆盖 Computer Use 技术原理、Skills 开发教程、Agent 工作流案例等开发者向内容。

---

*Last updated: 2026-07-16*
*创建日期: 2026-07-16*
