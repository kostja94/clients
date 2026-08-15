# Enter Pro — 功能分析

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[enter.md](./enter.md) | [enter-use-cases.md](./enter-use-cases.md) | [enter-site-structure.md](./enter-site-structure.md)

**Last updated**: 2026-06-25

---

## 1. 核心功能模块

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **Enter Workspace** | 浏览器内 AI 工作区：对话构建、预览、迭代、发布 | ★ 一体化 | `/`（应用内 `/app`） | ai dev agent, vibe coding |
| **Enter Code** | 终端本地 Super Agent：读代码库、规划、写码、跑测试 | ★ 本地验证闭环 | `/code` | ai coding terminal agent |
| **Enter CLI** | 一条 prompt 让 Claude Code/Cursor/Codex 构建并 publish live URL | ★ 与主流 IDE Agent 集成 | `/cli` | enter cli cursor |
| **Enter Desktop** | 原生桌面完整体验 | **待验证** | **待验证** | enter pro desktop |
| **AI ALL** | 统一 LLM 入口 / 模型聚合 | | `/ai-all` | unified llm api builder |
| **Native AI / Multi-LLM** | GPT、Claude、Gemini、Grok 等统一 API Key | ★ list price 无渠道费 | 首页 Feature.01 | ai app builder all models |
| **Custom Agents** | Design / Code / Plan Agent 及可扩展 Agent | ★ | 首页 | custom ai coding agents |
| **Cloud Backend** | Supabase DB/Storage/Functions/Cron；Stripe；GA | ★ 内置 BaaS | 首页 Feature.02 | ai app builder with database |
| **Visual Editor** | 实时预览上点选改字体/颜色/布局；AI 辅助微改 | ★ | `/features/visual-editor` | visual editor ai website |
| **Team Workspace** | 成员/角色（Owner–Viewer）、实时协作与评论 | ★ | `/features/collaborative-coding` | ai coding collaboration |
| **One-Click Deploy** | Edge 部署 + Custom Domain | ★ | FAQ / 功能页 | deploy ai built app |
| **Code Export** | 导出 React + Tailwind 标准代码 | ★ 反 lock-in | FAQ | export ai generated code |
| **Templates** | 网站/应用模板库 | | `/templates` | ai website templates |
| **Components** | 可复用 UI 组件 | | `/components` | ai ui components |
| **AI App Builder** | 自然语言 → 屏幕/导航/后端 → 测试发布 | ★ | `/features/ai-app-builder` | ai app builder no code |
| **AI Website Builder** | Landing、Blog、复杂 Web App | ★ | `/features/ai-website-builder` | ai website builder |
| **AI Agent Builder** | Chatbot、自动化工作流、智能助手 | ★ | `/features/ai-agent-builder` | build ai agent no code |
| **GitHub Sync** | 代码仓库同步（付费档） | | [pricing](https://converge.ai/pricing?product=enter) | ai builder github sync |

---

## 2. 用户流程

```
认知（SEO / YouTube / X / Discord）
  → 首页或 /features/ai-app-builder 理解能力
  → 注册领取 Daily Free Credits
  → 对话描述 idea → Agent 生成预览
  → Visual Editor 微调 / 或 Enter CLI 在 Cursor 中深化
  → 连接 Supabase / Stripe（Cloud 能力）
  → One-click Deploy → Custom Domain
  →（可选）导出代码 / GitHub Sync → 自有基础设施
```

**Enter CLI 路径**：在 Cursor/Claude Code 粘贴 prompt → Agent 在 enter.pro 构建 → 返回 live URL（无需打开 Dashboard）。

**Enter Code 路径**：本地 terminal → 读 repo → plan → implement → test → 交还已验证改动。

---

## 3. 技术指标

| 指标 | 数值 | 来源 |
|------|------|------|
| 生成栈 | React + Tailwind | 首页 FAQ 2026-06-25 |
| 后端 | Supabase + Stripe + GA | 首页 Feature.02 2026-06-25 |
| 模型 | GPT / Claude / Gemini / Grok 等 | 首页 2026-06-25 |
| 协作规模 | Workspace 最多 20 成员（Pro+） | pricing 2026-06-25 |
| 多会话并行 | Web Agent 单项目多 session（Changelog 叙事） | blog/enter-pro-multi-session **待验证** |
| 流量 / 用户量 | **待验证** | — |

---

## 4. 定价

统一定价于 [converge.ai/pricing?product=enter](https://converge.ai/pricing?product=enter)（Converge AI 账户，Credits 跨产品）。

| 套餐 | Credits / 月 | 有效期 | 要点 |
|------|-------------|--------|------|
| **Free** | 一次性额度 | 7 天 | 有限模型；无 GitHub/Custom Domain/导出 |
| **Basic** | 1,500 | 月周期 | 全模型、AI ALL、Cloud*、导出、去水印 |
| **Pro-1** | 4,000 | 月周期 | + Workspace 协作（≤20 人） |
| **Pro-2** | 8,200 | 月周期 | 同上 |
| **Ultimate** | 21,000 | 月周期 | + 新模型/功能优先、Priority Support |

*Cloud / Analytics 在促销期标注 Unlimited*（pricing 页脚注 2026-06-25）。

**Free 日常**：首页 FAQ — 登录即 **Daily Free Credits**，可每日生成与预览。

**美元月费**：pricing 页动态渲染，**待验证** 具体 $ 金额。

---

## 5. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| AI App Builder | MVP 验证 | Solo Founder |
| Visual Editor | 改文案/样式 | PM / 设计师 |
| Cloud + Stripe | 电商/订阅 SaaS | 小商家 |
| Enter CLI | IDE 内全自动 publish | Indie Dev |
| Team Workspace | PM+Dev 共建 | 初创团队 |
| AI Agent Builder | 客服/内部自动化 | Ops / HR |

---

## 6. 可构建产品类型（官网 Shipped with Enter）

| 类型 | 说明 |
|------|------|
| 响应式网站 | Landing、Blog、复杂 Web App |
| AI 应用 | Chatbot、自动化、智能助手 |
| Portfolio | 设计师/开发者作品站 |
| 移动 App | iOS/Android 跨平台叙事 |
| 电商 | 目录、购物车、结账 |
| 小程序 | 微信/支付宝等 mini program 叙事 |

---

*来源：[enter.converge.ai](https://enter.converge.ai/)、[pricing](https://converge.ai/pricing?product=enter)、[ai-app-builder](https://enter.converge.ai/features/ai-app-builder) 2026-06-25*
