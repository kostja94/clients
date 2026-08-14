# QVeris — 站点结构

> 遵循 [客户文档规范](../../skills for clients/client-template.md)
> 关联：[Overview](./qveris.md)

**Last updated**: 2026-08-05（本轮基于官网最新结构重建，替代 2026-08-03 版）

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 首页（Every capability, one call away + Run a task + 六金融能力域 + Live Demo） | QVeris、capability routing network | P0 |
| `/pricing` | 定价页（Free/Pro/Scale On-Demand 三档 + 示例成本 + FAQ） | QVeris pricing、ai agent api cost | P0 |
| `/playground` | Live Demo / Playground（单对话运行任务，可消耗 credits） | QVeris playground、try ai agent tools | P0 |
| `/docs` | 文档中心（What is QVeris + Quick start + Open Ecosystem） | QVeris docs、mcp server setup | P0 |
| `/docs/mcp-server` | 集成文档（MCP 六工具参考） | QVeris mcp、mcp server for ai agents | P0 |
| `/docs/rest-api` | 集成文档（REST 三接口 + OpenAPI） | QVeris api、ai tool api | P1 |
| `/docs/python-sdk` | 集成文档（Python SDK，含中文版） | QVeris python sdk | P1 |
| `/docs/claude-code-setup` | 集成文档（Claude Code 配置） | set up mcp in claude code | P1 |
| `/capabilities/explore` | Capability Coverage Map（六金融能力域覆盖图） | QVeris capabilities、financial data api | P0 |
| `/providers` | Tool Discovery（统一工具+Provider 发现入口） | QVeris providers、capability directory | P0 |
| `/providers/morningstar` | 单 Provider 资格页（Morningstar） | Morningstar data api | P2 |
| `/apps` | Application Center（Earnings Copilot / Options Assistant） | ai earnings copilot、ai options assistant | P1 |
| `/cli` | CLI 产品页（命令参考 + REPL + 安装） | QVeris cli、ai api cli | P1 |
| `/qverisbot` | QVeris Lab（beta，无代码 AI 代理工作区） | QVerisBot、ai agent no code | P2 |
| `/plugins` | 安装/集成页（各 Agent 平台一键配置） | install qveris、ai agent plugin | P1 |
| `/for-agents` | 面向 AI Agent 的说明页（协议 + 集成方式） | ai agent mcp、tool calling | P1 |
| `/ecosystem` | 开源生态页（CLI/QVerisFlow + SDK + 社区） | qveris open source、ai agent ecosystem | P2 |
| `/skills` | Skill 注册表（5 个官方 Skill） | qveris skill、openclaw skill | P2 |
| `/guides/` | 指南目录（SEO 内容中心，452 篇） | ai agent tools、financial data api | P0 |
| `/blog` | 博客目录（121 篇） | ai finance agent、qveris blog | P1 |
| `/whats-new` | 产品更新日志（月度里程碑） | qveris changelog、qveris whats new | P2 |
| `/security` | 信任与安全页 | ai agent security | P2 |
| `/help` | 帮助中心 | QVeris help | P2 |

> 注：`/apps`（Application Center）为当前真实 URL，官网页脚"View all applications"误链至 404 的 `/applications` —— 见 [qveris.md](./qveris.md#6-优化建议)。

## 2. URL 层级 / IA 树

```
qveris.ai/
├── /                              # 首页：定位 + Run a task + 六金融能力域 + Provider 网络 + 定价 + 安全
│
├── 产品与入口
│   ├── /playground                # Playground / Live Demo（首页任务直接带入）
│   ├── /apps                      # Application Center（Earnings Copilot / Options Assistant）
│   ├── /qverisbot                 # QVeris Lab（beta）
│   ├── /cli                       # QVeris CLI 产品页
│   ├── /capabilities/explore      # Capability Coverage Map
│   ├── /providers                 # Tool Discovery / Provider Hub
│   │   └── /providers/{slug}      # 单 Provider 页（当前仅 morningstar）
│   ├── /plugins                   # Agent 平台安装入口
│   └── /skills                    # Skill 注册表
│       └── /skills/{slug}         # 5 个官方 Skill（qveris-official 等）
│
├── 开发者转化
│   ├── /pricing                   # 定价
│   ├── /docs                      # 文档中心
│   │   ├── /docs/mcp-server       # MCP 集成
│   │   ├── /docs/rest-api         # REST API
│   │   ├── /docs/python-sdk       # Python SDK
│   │   ├── /docs/claude-code-setup
│   │   ├── /docs/opencode-setup
│   │   ├── /docs/ide-cli-setup
│   │   ├── /docs/openclaw-setup
│   │   └── /docs/cookbook
│   ├── /for-agents                # Agent 说明页（含机器可读协议）
│   │   ├── /setup.md              # 自安装指南（机器可读）
│   │   ├── /llms.txt              # 协议概述（机器可读）
│   │   ├── /llms-full.txt         # 完整协议参考（机器可读）
│   │   └── /guidelines.md         # Agent 行为指南（机器可读）
│   └── /ecosystem                 # 开源生态
│
├── 内容中心（SEO）
│   ├── /guides/                   # 指南目录（统一尾部斜杠）
│   │   └── /guides/{slug}/        # 452 篇指南文章
│   ├── /blog                      # 博客
│   │   └── /blog/{slug}           # 121 篇博客文章
│   └── /tools/{slug}              # 即用工具页（11 个：binance、coingecko 等）
│
└── 信任与运营
    ├── /security / /privacy / /terms
    ├── /whats-new                 # 产品更新
    └── /help                      # 帮助中心
```

## 3. 技术架构

| 维度 | 识别 | 方式 |
|------|------|------|
| 前端框架 | **Next.js**（`/_next/image` 静态资源、SSR/静态渲染） | HTML 资源路径（2026-08-05） |
| REST API | `https://qveris.ai/api/v1`（`/search`、`/tools/by-ids`、`/tools/execute` + Probe） | 官方文档（2026-08-05） |
| Hosted MCP | `mcp.qveris.ai`（官方托管 MCP 服务，2026-07-15 上线） | 官网 /whats-new（2026-08-05） |
| CLI | `@qverisai/cli` **v0.10.0**，`curl -fsSL https://qveris.ai/cli/install \| bash` 或 npm 全局 | 官网 /cli（2026-08-05） |
| MCP Server | `@qverisai/mcp` **v0.13.0**，六工具：discover / inspect / probe / call / usage_history / credits_ledger | 官方文档（2026-08-05） |
| Python SDK | PyPI `qveris` **v0.6.0**（async、typed、streaming） | /ecosystem（2026-08-05） |
| JS/TS SDK | `@qverisai/sdk` **v0.7.0**（零依赖、Node 18+） | /ecosystem（2026-08-05） |
| OpenClaw 生态 | 插件 `@qverisai/qveris`（npm）+ Skill（ClawHub `qveris-official`） | /for-agents（2026-08-05） |
| 多智能体框架 | **QVerisFlow**（LangGraph + QVeris，开源） | /ecosystem（2026-08-05） |
| 认证 | API Key（Bearer）+ CLI OAuth Device Flow（2026-07-18 上线） | /whats-new（2026-08-05） |
| 计费 | credits 账本，Discover/Inspect 免费，Call 1–100 credits/次，usage_history/credits_ledger 可审计 | 官网（2026-08-05） |
| 机器可读文档 | `/setup.md`、`/llms.txt`、`/llms-full.txt`、`/guidelines.md` | /for-agents（2026-08-05） |
| 托管/CDN | 具体 CDN ⚠️ 待验证 | — |

## 4. 多语言（如适用）

- 站内语言切换（EN / 中文）存在于导航；`discover` 支持 `lang: zh|en` 参数
- 内容中心以英文为主，存在中文博客与中文版 Python SDK 文档（官网 2026-05 声明）
- hreflang 结构 ⚠️ 待验证
- 整体本地化深度：产品 UI 与文档双语言，内容营销以英文为主

## 5. Sitemap 与 URL 模式

**来源**：`robots.txt` → `Sitemap: https://qveris.ai/sitemap.xml`（单 sitemap，无子 sitemap，抓取 2026-08-05）

| 来源 | 路径/模式 | 估算量级 | lastmod 范围 |
|------|----------|---------|-------------|
| sitemap.xml | `/` 首页 | 1 | 2025-12-26 |
| sitemap.xml | `/playground` `/pricing` `/cli` `/qverisbot` `/security` `/privacy` `/terms` `/help` `/whats-new` `/plugins` `/ecosystem` `/for-agents` `/capabilities/explore` | 13 | 2025-12-26 ~ 2026-07-10 |
| sitemap.xml | `/docs` + `/docs/{slug}`（8 篇：mcp-server、rest-api、python-sdk、claude-code-setup、opencode-setup、ide-cli-setup、openclaw-setup、cookbook） | 9 | 2025-12-26 ~ 2026-07-10 |
| sitemap.xml | `/guides/` + `/guides/{slug}/` | **452**（451 文章 + 1 索引） | 2026-07-03 ~ 2026-08-04 |
| sitemap.xml | `/blog` + `/blog/{slug}` | **121**（120 文章 + 1 索引） | 2026-03-13 ~ 2026-08-04 |
| sitemap.xml | `/tools/{slug}`（11 个） | 11 | 2025-12-26（⚠️ 长期未更新） |
| sitemap.xml | `/skills` + `/skills/{slug}`（5 个） | 6 | 2026-07-10 |
| sitemap.xml | `/providers` + `/providers/{slug}` | 2 | 2025-12-26 ~ 2026-07-10 |
| **合计** | | **~615** | 单 sitemap |
| 未入 sitemap（已核实在线） | `/apps`（Application Center） | 1 | — |

**URL 模式归纳**：
- 内容页统一 `/{section}/{slug}`：`/guides/{slug}/`（统一尾部斜杠，452/452 无混用）、`/blog/{slug}`、`/skills/{slug}`、`/docs/{slug}`
- 产品入口单层：`/playground`、`/pricing`、`/apps`、`/cli`、`/plugins`、`/ecosystem`
- 程序化页：`/tools/{slug}`
- **对比 2026-08-03 快照的变化**：`/use-cases/*`、`/scenarios/*`、`/alternative/*` 已从 sitemap 移除；guides 尾部斜杠已统一；总量从 ~1,300 → 615（栏目瘦身）

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| 首页 | 主导航（Explore/Integrate/Applications/Developers/Ecosystem）、Run a task→Playground、Quick install、Pricing CTA | Playground、Tool Discovery、Capability Map、文档、注册转化 |
| `/docs` | 各集成方式文档互链、Quick start | 开发者 onboarding |
| `/pricing` | 三档套餐、FAQ、Contact Sales、充值 | 转化 |
| `/for-agents` | 协议说明 + CLI/MCP/SDK/REST 各集成路径互链 | Agent 生态 onboarding |
| `/guides/` 指南目录 | 指南文章互链（教程、对比、场景） | SEO 内容分发 |
| `/blog` | 博客文章互链 + Skill 页 | 内容营销 + Skill 转化 |
| `/skills` | Skill 详情页 + 安装命令 + Blog-to-Skill 用例 | 生态分发 |
| `/ecosystem` | GitHub / npm / PyPI / ClawHub 外部入口 | 开源生态 |
| 页脚 | Pricing / Docs / GitHub / npm / ClawHub / Security / Terms / What's New / Help | 信任页 + 生态入口 |

## 7. URL 分阶段规划

| 阶段 | 新增/修复页面 | 对标的 keywords 优先级 |
|------|-------------|----------------------|
| 短期（0–3 月） | 修复页脚"View all applications" → `/apps`，并把 `/apps` + `/providers/*` 新栏目补入 sitemap | P0 品牌导航完整性 |
| 短期（0–3 月） | 补 `/docs/typescript-sdk`、`/docs/hosted-mcp` 独立页（官网已提供 TS SDK 与 Hosted MCP 服务，但无对应文档 URL） | P1 开发者词 |
| 中期（3–6 月） | 重启场景页栏目：以 guides 中的实用主题为基础建设 `/use-cases/{slug}`（earnings research、market monitor 等），或为 `/apps` 的两个应用各建 Landing 页 | P1 场景词 |
| 中期（3–6 月） | 刷新 `/tools/{slug}`（11 个工具页 lastmod 停滞于 2025-12-26），按新能力目录扩充或 301 归并 | 技术 SEO |
| 长期（6–12 月） | 中文内容中心（guides 中文本地化 + 中文博客扩量）；`/guides/` 指南按主题分簇（finance/data/compliance/agents）建立二级目录 | 中文市场长尾 |

---

*Last updated 2026-08-05 · 数据来源：robots.txt、sitemap.xml（615 URL 全量解析）、首页/定价/docs/cli/for-agents/ecosystem/whats-new/plugins/apps 抓取（访问日期 2026-08-05）*
