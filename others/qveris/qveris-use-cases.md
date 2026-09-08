# QVeris — 使用场景

> 遵循 [客户文档规范](../../skills for clients/client-template.md)
> 关联：[主文档](./qveris.md) | [features](./qveris-features.md) | [keywords](./qveris-keywords.md)

**Last updated**: 2026-08-05（已同步 2026-08-05 官网快照）

> **结构说明**：官网 8 月改版移除了 `/use-cases/*` 栏目，本版承接页统一改为当前 sitemap 中的真实 URL（以 `/guides/`、`/skills/`、`/apps` 为主）。

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **量化工程师** | 私募/自营/散户量化策略开发者 | 行情与因子数据源分散、各 API schema 不一、维护量大、供应商宕机无备选 | 用一套协议稳定获取实时/历史行情与因子，低延迟低成本 | 高 |
| **投资研究分析师** | 券商/资管/独立研究机构的金融研究员 | 财报、SEC 文件、业绩电话会纪要需手动搜集，抓取信息不可靠、耗时长 | 快速产出股票研究简报、业绩分析、可比公司表 | 中高 |
| **代理工程师** | 构建生产级 AI Agent 的开发者（金融科技、SaaS） | 为每个数据源写集成、Token 消耗大、调用质量不可控、成本不可审计 | 让 Agent 自主发现并调用能力，成本可预测可审计 | 高 |
| **投资决策者/内容创作者** | 个人投资者、财经自媒体、运营人员 | 不懂代码但需要实时市场数据做决策与内容 | 用对话式助手（QVeris Lab）获取行情、生成日报、做内容运营 | 低 |

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| 量化工程师 | 开盘前拉取今日板块与个股实时行情 | 用一句话让 Agent 拿到最新行情并转成结构化数据 | Discover/Call + 金融数据域 | real-time stock price api |
| 量化工程师 | 策略回测需要多年历史数据 | 不用签多份数据合同，一个 API 拿到历史行情 | Call + Provider 路由 | historical stock price api |
| 量化工程师 | 某数据供应商宕机时 | 自动切换到备用 Provider，不让策略中断 | 能力路由（failover） | financial data api |
| 量化工程师 | 期权策略需要隐含波动率与风险收益结构 | 用现成工作流应用跑期权分析，不自己写回测框架 | Application Center（Options Assistant） | options analysis ai |
| 投资研究分析师 | 财报季密集期要追十几家公司 | 让 Agent 解析 SEC 文件并生成业绩摘要 | Call + SEC 文件能力 + skill | sec filing api for ai agents |
| 投资研究分析师 | 写个股深度报告前 | 拿到分析师共识、估值与可比公司数据 | Call + 投资研究域 | ai investment research |
| 投资研究分析师 | 需要对公司与财报做端到端研究 | 用 Earnings Copilot 一站式完成财报研究 | Application Center（Earnings Copilot） | ai earnings research |
| 代理工程师 | 给 Cursor/Claude Code 配工具 | 让编辑器内 Agent 直接 discover/call 外部能力 | MCP Server / Hosted MCP | qveris mcp、cursor mcp tools |
| 代理工程师 | 上线前核算调用成本 | 调用前看到单次成本并事后审计账本 | Inspect/Probe + credits_ledger | api cost calculator |
| 代理工程师 | 长上下文 Agent 频繁调用工具 | 用 CLI 子进程方式避免 schema 注入耗 Token | CLI 零 Token 调用 | qveris cli |
| 投资决策者 | 每天早上想知道持仓与市场动态 | 让 QVeris Lab 生成日报并推送 | QVeris Lab / QVerisBot | qverisbot |
| 内容创作者 | 做财经内容需要最新数据 | 让助手按主题聚合行情/事件并输出内容草稿 | QVeris Lab + 内容运营工作流 | ai finance agent |

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| 实时行情获取 | 量化工程师 | Discover + Call（金融域） | real-time stock price api | /guides/real-time-stock-price-api-for-ai-agents/ |
| 历史数据回测 | 量化工程师 | Call + 路由 | historical stock price api | /guides/historical-stock-price-api-for-ai-agents/ |
| 供应商故障切换 | 量化工程师 | 能力路由 | financial data api | /guides/capability-routing-network/ |
| 期权分析 | 量化工程师 | Application Center | options analysis | /apps |
| SEC 文件分析 | 投资研究分析师 | Call（SEC 能力） | sec filing api | /guides/financial-statements-api-fmp/ |
| 业绩电话会简报 | 投资研究分析师 | Call + skill（stock-copilot-pro） | earnings call brief | /skills/stock-copilot-pro |
| 投资研究报告 | 投资研究分析师 | Call + skill | equity research | /guides/skill-equity-research-report/ |
| 财报研究 | 投资研究分析师 | Application Center | earnings copilot | /apps |
| 编辑器内工具调用 | 代理工程师 | MCP Server / Hosted MCP | cursor mcp tools | /docs/mcp-server |
| 成本核算 | 代理工程师 | Inspect/Probe + 账本 | api cost calculator | /guides/api-cost-calculator/ |
| 零 Token 调用 | 代理工程师 | CLI | qveris cli | /cli |
| 无代码日报 | 投资决策者 | QVeris Lab / QVerisBot | ai agent no code | /qverisbot |
| 内容运营 | 内容创作者 | QVeris Lab 内容工作流 | ai content workflow | /guides/ai-content-workflow/ |

## 4. 用户旅程

```
认知            考虑            转化            留存
─────────────────────────────────────────────────────
Search "mcp   → 读 /guides/     → 注册 → 1000   → 每日 100 credits
server"         对比页(vs)       credits 免费     登录奖励
  │               │              试用               │
  ▼               ▼               ▼                 ▼
/blog 教程      /docs 文档      Playground →      usage_history
/guides 指南     /pricing 看价   首次 Call 成功    credits_ledger 审计
  │              格               │               │
  ▼               ▼               ▼               ▼
社区/GitHub      API key 申请    Free 转 Pro      skill/plugin
/ecosystem      （Dashboard）    或 Scale 充值      复用 + 内容中心续更
                    │            /apps 用完整
                    ▼            工作流应用
              /plugins 一键安装
```

**关键触达点**：SEO 对比页（认知）→ 文档 Quick start + /plugins 安装（考虑）→ 免费 credits + Playground（转化）→ 审计账本 + 内容中心 + Application Center（留存）。

## 5. 未覆盖场景

| 场景 | 缺口 | 机会 |
|------|------|------|
| 用户授权 SaaS 操作（代表用户发邮件/操作 Slack） | QVeris 无 OAuth 连接账户能力 | 与 Composio 式产品互补集成；或拓展 auth 层 |
| 定时任务与托管执行 | QVeris 不提供 Cron/托管 Agent 运行时 | 提供 Agent 调度服务或与托管平台合作 |
| 数据同步（RAG 长上下文） | 无 syncs/webhooks | 未来扩展数据管道能力 |
| 合规审计（SOC 2 报告公开化） | 有 /security 页但审计级别未公开 | 补齐合规认证材料以服务企业客户 |
| 应用目录深度 | Application Center 仅 2 个 BETA 应用（Earnings Copilot / Options Assistant），无独立 Landing 页 | 为每个应用建独立页面，承接"ai earnings research"类搜索意图 |

---

*Last updated 2026-08-05 · Persona 与场景基于官网产品功能推导 + sitemap 核对（2026-08-05）*
