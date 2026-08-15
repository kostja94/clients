
# Bridge — 站点结构

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./bridge-surf.md) | [features](./bridge-surf-features.md) | [keywords](./bridge-surf-keywords.md) | [competitors](./bridge-surf-competitors.md) | [use-cases](./bridge-surf-use-cases.md) | [growth-strategy](./bridge-surf-growth-strategy.md)

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 首页（Waitlist 落地页） | AI agent, computer use agent, AI automation | P0 |
| `/features` | 功能页（AI 文件组织） | AI file organizer Mac, auto file organization | P0 |
| `/pricing` | 定价页 | AI agent pricing, Bridge pricing | P0 |
| `/blog` | 博客首页 | AI agent blog, computer use tutorial | P1 |
| `/blog/macos-two-cursors` | 单篇博文 | macOS computer use, background automation | P1 |
| `/blog/bridge-everyday-life` | 单篇博文 | AI agent everyday work | P2 |
| `openbridge.bridge.surf/` | 子域名（OpenBridge 开源页） | open source Claude Cowork alternative, local AI agent | P0 |
| `github.com/AFK-surf/OpenBridge` | GitHub 仓库 | OpenBridge GitHub | P0 |
| `afk.surf/` | 公司主页 | AFK AI | P2 |

---

## 2. URL 层级

```
bridge.surf/
├── /                          # 首页："Bridge Intent and Done." + Waitlist CTA
├── /features                  # 功能页：AI File Organization for Mac
├── /pricing                   # 定价页：Interest / Starter / Pro + Team/Enterprise
├── /blog                      # 博客首页（2 篇文章）
│   ├── /blog/macos-two-cursors
│   └── /blog/bridge-everyday-life
└── [子域名] openbridge.bridge.surf/
    └── /                      # OpenBridge 开源产品页

afk.surf/                      # 公司主页（AFK AI, Inc.）
├── /                          # "We build agentic AI that actually works"
└── → bridge.surf              # 指向 Bridge 产品
```

> **注意**：bridge.surf 是极简的 pre-release 站点。无 `/about`、`/docs`、`/login`（仅 robots.txt 中 disallow）、`/skills` 等功能页。sitemap.xml 返回 500 错误。

---

## 3. 技术架构

| 维度 | 内容 | 识别方式 |
|------|------|---------|
| 平台 | **macOS only**（无 Windows/Linux/移动端） | 官网声明 + GitHub |
| 原生框架 | SwiftUI + AppKit | OpenBridge 源码 |
| 聊天界面 | React/TypeScript（WebView 嵌入） | OpenBridge 源码 |
| Agent 运行时 | kwwk（Swift-native agent SDK，自研/vendored） | GitHub |
| 沙盒 VM | Go 实现，基于 Virtualization.framework 的 Linux VM | OpenBridge 源码 |
| Computer Use | macOS Accessibility API + CGEvent 后台输入 | 博客 + GitHub |
| 模型支持 | OpenAI, Anthropic, Google Gemini, AWS Bedrock, Azure, DeepSeek, OpenRouter, xAI, Groq, Mistral, Cloudflare, Cerebras + 自定义 OpenAI-compatible | OpenBridge 文档 |
| 认证方式 | OAuth + API Key，凭据本地存储 | OpenBridge 文档 |
| 开源协议 | MIT License | GitHub |
| GitHub Stars | 412（2026-07） | GitHub |
| 网站技术栈 | 未确认（静态站点，疑似 Next.js/SSG） | 推测 |

---

## 4. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| robots.txt 声明 | `sitemap.xml` | 返回 500 | 不可用 |
| 首页导航 | `/`, `/features`, `/pricing`, `/blog` | 4 页 | 2026-07 |
| 博客 | `/blog/{slug}` | 2 篇 | 2026-05 |
| OpenBridge 子域名 | `openbridge.bridge.surf/` | 1 页 | 2026-05 |
| GitHub | `github.com/AFK-surf/OpenBridge` | 1 仓库 | 2026-05 |

> sitemap.xml 返回 HTTP 500 错误，无法获取完整 URL 清单。当前站点为 pre-release 阶段，页面极少。

---

## 5. robots.txt 要点

- **Allow**: `/`（全站开放）
- **Disallow**: `/login`, `/payment/`, `/skills/*/download`
- **AI Crawler 策略**: 未特别声明
- **Sitemap**: 声明 `https://bridge.surf/sitemap.xml`（但返回 500）

---

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| 首页 | Waitlist CTA、"Have Invite Code?" | 用户注册/邀请 |
| Features 页 | 方法介绍（PARA/GTD/Life Buckets）、FAQ、"Get Started"CTA | 功能认知、转化 |
| Pricing 页 | 三档定价 + Team/Enterprise 联系方式 | 付费转化 |
| Blog | 文章卡片 | 内容发现 |
| OpenBridge 页 | GitHub 链接、下载、Provider 列表 | 开发者获取 |
| AFK.surf | → bridge.surf 链接 | 品牌关联 |

---

## 7. 多语言

| 维度 | 内容 |
|------|------|
| 主语言 | 英语 |
| 其他语言 | 无 |
| hreflang | 无 |

---

## 8. URL 分阶段规划

| 阶段 | 建议新增页面 | 对标关键词优先级 |
|------|-------------|----------------|
| 短期 | `/about` 公司/团队页面 | P1 |
| 短期 | `/docs` 或 `/guide` 使用文档 | P0 |
| 短期 | `/skills` 技能市场/目录 | P1 |
| 短期 | `/compare/bridge-vs-claude-cowork` 对比页 | P0 |
| 中期 | `/use-cases` 或 `/solutions` 场景页 | P0 |
| 中期 | `/blog` 扩展至 10+ 篇 | P1 |
| 长期 | 多语言支持 | P2 |

---

*Last updated: 2026-07-16*
*来源：robots.txt 读取、网站抓取、GitHub 代码库分析、The Agent Times 报道*
