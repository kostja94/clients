# QVeris — 概览（Overview）

> 遵循 [客户文档规范](../../skills for clients/client-template.md)
> 关联：[site-structure](./qveris-site-structure.md)

**Last updated**: 2026-08-05（本轮基于官网最新结构重建，替代 2026-08-03 版）

---

## 文档范围

本项目按需求仅交付两份文档：

| 文档 | 职责 |
|------|------|
| [qveris.md](./qveris.md)（本页） | 品牌概览：定位、产品信息、定价、优化建议 |
| [qveris-site-structure.md](./qveris-site-structure.md) | 网站架构：核心路径、URL 层级、技术栈、Sitemap、内链枢纽、分阶段规划 |

> 关键词、竞品、使用场景、增长策略等维度未包含在本交付范围内，如需补充可后续扩展。

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2B 开发者基础设施 / AI Agent 工具层 / 金融数据 API |
| 网站 | https://qveris.ai/ |
| 当前阶段 | 增长期（2026 年 4 月以来产品面快速扩张：Playground、Tool Discovery、Hosted MCP、Application Center 相继上线） |
| 核心产品 | **QVeris**：能力路由网络（capability routing network）——让 AI 代理通过 Discover → Inspect → Call 统一协议，调用 10,000+ 真实世界已验证能力（金融数据、文档处理、视觉 API、媒体生成等），核心引擎托管、客户端工具开源 |
| 产品形态 | Web（官网 + Playground + Tool Discovery + Capability Map + Application Center）+ CLI + MCP Server + Python/TS SDK + REST API + Hosted MCP |
| 关键差异化 | 能力路由（多 Provider 自动 failover）、调用前 Inspect/Probe（延迟/成功率/成本质量信号，Probe 零成本预验证）、六大金融能力域纵深、按次计费 + 可审计账本、CLI 零 Token 调用 |
| 目标用户 | 构建 AI Agent 的开发者 / 量化与投资研究人员 / 金融科技产品团队 / 无代码自动化用户 |
| 目标市场 | 全球（英文为主，中文站与中文版文档同步布局） |
| 更新日期 | 2026-08-05 |

---

## 1. 产品定位

| 维度 | 内容 |
|------|------|
| 品类 | AI Agent 工具层 / 能力路由网络（介于 LLM 与外部 API/数据源之间的中介基础设施） |
| 价值主张 | "Every capability, one call away."——让 AI 代理一句话找到、检查并调用任何真实世界能力，无需为每个数据源硬编码集成 |
| 竞争替代 | 开发者从手写 API 集成、LangChain/Zapier 工具、单一数据 API（FMP/Alpha Vantage/Polygon）转向 QVeris，以获得统一协议 + 自动路由 + 预结算计费 + 可审计账本 |
| 差异化锚点 | ★ 能力路由（多 Provider failover）；★ Inspect/Probe 质量信号（Probe 零成本预验证，2026-07-21 上线）；★ 六大金融能力域纵深；★ 按次计费 + usage_history/credits_ledger 审计；★ CLI 零 Token 调用（子进程执行，比 MCP 省最高 80% prompt token） |
| 市场位置 | 垂直专家 + 平台型：金融数据是纵深护城河，15+ 分类走平台路线；定价按用量，入门免费（1,000 credits），Pro $19/月 |

### 1.1 定位简述

QVeris 处于"AI Agent 工具层"这个快速成形的品类中。这个品类的核心问题是：LLM 能推理，但无法直接接触真实世界的 API、数据源和外部服务。传统方案要么让开发者逐个为数据源写集成（成本高、schema 各异、维护量大），要么用通用自动化平台（面向简单业务流而非 Agent 调用）。QVeris 选择的位置是**能力路由网络**——作为中介层，把 10,000+ 已验证能力标准化为一个 Discover → Inspect → Call 协议，让 Agent 自己发现、检查、调用，并按质量信号自动路由到最合适的 Provider。

核心用户是两类人：一类是**构建 AI Agent 的开发者**（量化工程师、代理工程师、金融科技产品团队），需要稳定的金融数据与外部工具接入，又不愿被单一 API 供应商绑定；另一类是**投资研究从业者**，通过 QVerisBot / QVeris Lab 或 CLI 以对话方式获取股票、宏观、加密市场的结构化数据。官网对外的承诺是"Discover 与 Inspect 永远免费，只有在真正调用取得价值时才按次计费"，并配套 Usage & Execution History + Credits Ledger 让每一次扣费都可审计。

QVeris 存在的理由（raison d'être）：AI Agent 若只连接 LLM 自身知识，价值受限；连接真实世界数据与服务的能力将决定 Agent 的生产力上限。QVeris 把连接过程从"工程负担"变成"协议的一部分"，并在 2026 年持续推进平台化——Tool Discovery 统一入口（7/30）、Hosted MCP（7/15）、Application Center（7/30）与机器可读文档（/setup.md、/llms.txt）——让自己成为 Agent 时代的工具基础设施层。

## 2. 产品信息

**受众**：全球开发者、量化/投资研究团队、金融科技产品团队，以及需要无代码 AI 自动化的个人与中小企业。产品 UI 与文档以英文为主，中文站、中文版 Python SDK 文档与部分中文博客同步布局。

**产品线**：
1. **QVeris 核心协议**（Discover / Inspect / Probe / Call + 计费审计）——通过 CLI、MCP Server、Python SDK、TypeScript SDK、REST API、Hosted MCP 六种方式接入，适配 14+ Agent 平台（Claude Code、Cursor、OpenCode、OpenClaw、Hermes、Trae、VS Code 等）
2. **Tool Discovery / Provider Hub**——统一发现入口（2026-07-30 上线），10,000+ 能力、15+ 分类、六大金融能力域，附成功率和延迟等质量信号
3. **Application Center（`/apps`）**——围绕完整工作流的应用目录，首批为 Earnings Copilot（财报研究）与 Options Assistant（期权分析）
4. **QVeris Lab / QVerisBot**——无代码对话式 AI 代理工作区（beta）
5. **Skill 注册表**——5 个官方 Skill（qveris-official、stock-copilot-pro、chairman-daily-report、exchange-rate、x-founder-operations），Claude Code/Cursor/OpenClaw 可安装
6. **开源生态**——CLI、MCP、SDK 开源；多智能体工作流引擎 QVerisFlow（LangGraph）在 GitHub 开源
7. **终端工具页**——/tools 下 11 个即用工具（币价、汇率、天气、翻译等）

**定价摘要**（详见 [pricing](https://qveris.ai/pricing)，2026-08-05）：

| 档位 | 价格 | 包含 | 说明 |
|------|------|------|------|
| Free | $0 | 1,000 注册 credits + 100 每日登录 credits | 10 req/min |
| Pro | $19/月 | 10,000 credits | 100 req/min，超额 $0.002/credit |
| Scale On-Demand | $1+ | 按量充值 | $100→52,500（+5%）、$500→275,000（+10%）、$1,000→575,000（+15%） |

- Discover/Inspect 永远免费；Call 1–100 credits/次；credits 永不过期，无订阅强制
- 示例成本：实时行情 ~1 credit、OCR 一页 ~2、解析 PDF 3–10、分析财报 5–15、生成图片 5–20

## 3. 站点结构摘要

**技术栈**：Next.js 官网 + REST API（`qveris.ai/api/v1`）+ Hosted MCP（`mcp.qveris.ai`）；npm `@qverisai/cli` v0.10.0、`@qverisai/mcp` v0.13.0（六工具）、`@qverisai/sdk` v0.7.0；PyPI `qveris` v0.6.0；OpenClaw 插件 `@qverisai/qveris`。

**核心路径**：`/` 首页 → `/playground` → `/apps`（Application Center）→ `/pricing` → `/docs`（8 篇集成文档）→ `/capabilities/explore`（能力覆盖图）→ `/providers`（Tool Discovery）→ `/cli` → `/for-agents` → `/plugins` → `/skills` → `/ecosystem`。**内容中心**：`/guides/`（452 篇，SEO 主力）+ `/blog`（121 篇）。Sitemap 总量 **615 URL**，单 sitemap 无子 sitemap。完整见 [qveris-site-structure.md](./qveris-site-structure.md)。

## 4. 关键事实与指标

| 指标 | 数据 | 来源 |
|------|------|------|
| 能力/分类 | 10,000+ 能力 / 15+ 分类 / 14+ Agent 平台 | 官网首页 |
| 稳定性 | 99.99% 上线率、<500ms P95 延迟 | 官网首页 |
| 六大金融能力域 | 量化交易 / 宏观固收 / 风险合规 / 投资研究 / 加密与数字资产 / 另类信号 | 官网首页 |
| Sitemap | 615 URL（guides 452 / blog 121 / 其余 42） | sitemap.xml（2026-08-05） |
| 内容更新节奏 | guides 与 blog 最近 lastmod 均至 2026-08-04 | sitemap.xml |

## 5. 市场与竞品背景（简报）

- AI Agent 工具层处于品类教育窗口期，"能力路由 / 工具调用"为主流叙事，MCP 成为事实标准，托管 MCP 与能力目录定位放大
- 竞品分三层：工具集成平台（Composio/Toolhouse/Nango/Pipedream）、LLM 网关（OpenRouter/LiteLLM/Portkey/Eden AI）、金融数据 API（FMP/Alpha Vantage/Polygon/OpenBB）
- QVeris 差异化：能力路由 + 金融纵深 + 按次计费 + 可审计账本，尚无完全对位竞品（详细竞品分析未包含在本交付范围）

## 6. 优化建议

1. **修复页脚"View all applications"死链**：页脚与 What's New 指向的 `/applications` 返回 404，真实页面为 `/apps`；应统一改链并 301，同时把 `/apps` 补入 sitemap.xml。
2. **补齐两份"有名无页"的开发者文档**：官网已提供 TS SDK（`@qverisai/sdk`）与 Hosted MCP 服务，但 `/docs/typescript-sdk`、`/docs/hosted-mcp` 均为 404 且未入 sitemap；建议独立建页承接开发者意图词。
3. **刷新停滞的工具页与栏目**：`/tools/*` 11 个页面 lastmod 全部停留在 2025-12-26，与活跃内容矩阵（guides/blog 更新至 8 月）节奏脱节；建议按新能力目录扩充或做 301 归并，避免陈旧信号。
4. **规划 Application Center 的 SEO 落地**：Earnings Copilot / Options Assistant 目前仅有 `/apps` 单页且未入 sitemap；建议为每个应用建设独立 Landing 页（对应 "ai earnings research" 等词），承接金融场景搜索量。

---

## 待验证项

- [ ] Hosted MCP 端点（mcp.qveris.ai）的具体接入文档页 URL ⚠️ 待验证
- [ ] hreflang / 中文站 URL 结构 ⚠️ 待验证
- [ ] 官网 CDN 与托管服务商 ⚠️ 待验证
- [ ] 各平台安装入口数量（"13 tools" vs "14+ agent platforms"）表述差异 ⚠️ 待验证

---

*Last updated 2026-08-05 · 创建 2026-08-03（v1 快照）· 本轮重建 2026-08-05 · 数据来源：qveris.ai 官网、/pricing、/docs、/cli、/for-agents、/ecosystem、/whats-new、/apps、robots.txt、sitemap.xml（访问日期 2026-08-05）*
