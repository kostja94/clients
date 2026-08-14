# QVeris — 功能分析

> 遵循 [客户文档规范](../../skills for clients/client-template.md)
> 关联：[主文档](./qveris.md) | [use-cases](./qveris-use-cases.md) | [site-structure](./qveris-site-structure.md)

**Last updated**: 2026-08-05（已同步 2026-08-05 官网快照）

## 1. 核心功能模块

| 功能 | 描述（用户语言） | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **Discover 能力搜索** | 用自然语言描述"想要什么能力"，返回排序后的候选列表（含 tool_id、描述、预估成本），并解释推荐理由（categories/capabilities/why）。免费。 | ★ | /docs、/capabilities/explore | qveris discover、ai tool discovery |
| **Inspect 调用前检查** | 调用前查看某个能力的完整参数 schema、示例、延迟、成功率、credit 成本与 Provider 对比，避免盲调。免费，HTTP 200 恒定。 | ★ | /docs、/docs/mcp-server | inspect tool、mcp inspect |
| **Call 沙盒执行** | 用结构化参数执行能力，返回结构化 JSON + 预结算计费明细；超长输出自动截断并提供临时文件下载。 | ★ | /docs、/docs/rest-api | call ai tool、ai api call |
| **Probe 参数预验证** | 公共 Probe API（2026-07-21 上线）：不调用 Provider、不消耗 credits 的前提下验证参数合法性、覆盖率与价格报价（typed schema / quote / delegation 检查）。 | ★ | /docs/mcp-server、/docs/rest-api | mcp probe、api cost quote |
| **能力路由网络** | 同一能力映射多个 provider；依据延迟/成本/可靠性自动选择与故障切换，供应商不可用时自动 fallback。 | ★ | /providers、/ | capability routing、tool routing |
| **质量信号** | 每个能力附成功率、平均延迟、计费规则、call count 等质量指标，供调用前决策；搜索结果中直接展示。 | ★ | /providers | api success rate、reliable api |
| **六大金融能力域** | 量化交易、宏观与固收、风险合规、投资研究、加密与数字资产、另类信号——金融数据纵深覆盖。 | ★ | /capabilities/explore | financial data api、ai finance agent |
| **Application Center** | 围绕完整工作流的应用目录（2026-07-30 上线）：Earnings Copilot（财报研究）、Options Assistant（期权分析），均基于同一能力网络。 | ★ | /apps | ai earnings copilot、ai options assistant |
| **QVeris Lab / QVerisBot** | 无代码对话式 AI 代理工作区（beta）：模型、工具与证据在同一 workspace；股票研究、市场情报、内容运营工作流。 | ★ | /qverisbot | ai agent no code、qverisbot |
| **CLI 零 Token 调用** | 终端工具，子进程方式调用（不注入 schema 进 LLM 上下文），比 MCP 省最高 80% prompt token；支持 `--json`、`--codegen`、交互式 REPL、`qveris probe`、`qveris doctor`、`qveris usage/ledger` 计费审计。 | ★ | /cli | ai api cli、qveris cli |
| **MCP Server** | `@qverisai/mcp` 提供 6 个工具：discover/inspect/probe/call/usage_history/credits_ledger，适配 Cursor、Claude Desktop 等。 | ★ | /docs/mcp-server | mcp server、cursor mcp tools |
| **REST API / SDK** | Python SDK（pip install qveris，v0.6.0，async/typed/streaming）、TypeScript SDK（@qverisai/sdk v0.7.0，零依赖）、REST API（/search、/tools/by-ids、/tools/execute），统一协议。 |  | /docs/rest-api、/docs/python-sdk | ai api、python sdk |
| **Hosted MCP** | 官方托管 MCP 服务（2026-07-15 上线）：无需本地进程，隔离端点、环境级凭证、协议感知错误、就绪检查。 | ★ | /docs/mcp-server | hosted mcp |
| **Tool Discovery 统一入口** | 工具搜索与 Provider 目录合并为单一发现体验（2026-07-30），可按需求搜索或按类别浏览。 |  | /providers | qveris providers、tool directory |
| **计费与审计** | 每次调用预结算 + usage_history/credits_ledger 可审计账本（按 API key 归因）；Discover/Inspect 免费，Call 1-100 credits；执行结果区分 transport/provider/validity/billable 四类 outcome。 | ★ | /pricing | ai api pricing、api cost calculator |
| **机器可读文档** | 面向 Agent 的 `/setup.md`、`/llms.txt`、`/llms-full.txt`、`/guidelines.md`，Agent 可自行安装与解析协议。 | ★ | /for-agents | ai agent protocol、llms.txt |
| **即用工具页** | 面向终端的即用工具（/tools 下 11 个：币价、汇率、天气、翻译、地图等）。 |  | /tools/{slug} | crypto dashboard、stock app |

## 2. 用户流程

```
① 注册 → Dashboard 创建 API key（免费 1,000 credits + 100 每日 credits）
② 选集成方式：CLI / MCP / Hosted MCP / Python SDK / TS SDK / REST API / OpenClaw 插件
③ Discover   → 自然语言搜索能力（免费，如 "stock market real-time quotes"）
④ Inspect    → 查看参数/成功率/延迟/成本（免费，可选；多候选时建议）
⑤ Probe      → 零成本预验证参数与报价（可选，公共 API）
⑥ Call       → 沙盒执行 → 结构化 JSON + 预结算明细
⑦ 审计       → usage_history / credits_ledger（按 API key 归因）核对扣费
⑧ 复用       → 会话索引（30-min TTL）可直接 inspect 1 / call 2 按序号引用
```

**Agent 标准工作流**（官方推荐系统提示词）：先用 discover 描述能力 → 参考 success_rate 与 avg_execution_time 选候选 → call 传入 params_to_tool → 单轮可多次调用。

**产品入口分流**：开发者在 /playground 跑单任务 → 在 /apps 用完整工作流应用（Earnings Copilot / Options Assistant）→ 在 /plugins 一键安装到 Claude Code / Cursor / OpenClaw。

## 3. 技术指标

| 指标 | 数值 | 来源 |
|------|------|------|
| 能力总量 | 10,000+ 真实世界已验证能力 | 官网（2026-08-05） |
| 能力分类 | 15+ 分类，六大金融能力域纵深 | 官网（2026-08-05） |
| 上线率 | 99.99%（官网声明） | 官网（2026-08-05） |
| P95 延迟 | <500ms（官网声明）；示例能力 ~180ms | 官网（2026-08-05） |
| Agent 平台支持 | 14+（Claude Code/Cursor/OpenCode/Trae/VS Code/OpenClaw/Hermes 等） | 官网（2026-08-05） |
| 免费配额 | 1,000 注册 credits + 100 每日登录 credits（次日重置） | 定价页（2026-08-05） |
| 速率限制 | Free 10 req/min；Pro 100 req/min | 定价页（2026-08-05） |
| 单次调用成本 | 1–100 credits（示例：报价 ~1、OCR 页 ~2、PDF 3–10、财务报告分析 5–15、图片生成 5–20） | 定价页（2026-08-05） |
| CLI 版本 | v0.10.0（npm `@qverisai/cli`） | /cli、/for-agents（2026-08-05） |
| MCP 版本 | v0.13.0（npm `@qverisai/mcp`，六工具） | /ecosystem、/for-agents（2026-08-05） |
| Python SDK | v0.6.0（PyPI `qveris`，async/typed/streaming） | /ecosystem（2026-08-05） |
| TS SDK | v0.7.0（npm `@qverisai/sdk`，零依赖，Node 18+） | /ecosystem（2026-08-05） |
| 认证 | API Key（Bearer）+ CLI OAuth Device Flow（2026-07-18） | /whats-new（2026-08-05） |
| 响应输出上限 | 默认 20,480 字节，超出返回 truncated_content + full_content_file_url | 官方文档（2026-08-05） |

## 4. 定价

| 套餐 | 价格 | 包含 | 适合 |
|------|------|------|------|
| **Free** | $0 | 1,000 注册 credits + 100 每日登录 credits（每日重置）、10 req/min、基础工具、Live Demo、社区支持、标准队列 | 试用评估 |
| **Pro**（推荐） | $19/月 | 10,000 credits、100 req/min、$0.002/credit 超额、全部 10,000+ 工具、24h 邮件支持、使用分析、优先队列 | 个人开发者 |
| **Scale On-Demand** | $1+ | 按量充值无月度承诺：$100→52,500 credits(+5%)、$500→275,000(+10%)、$1,000→575,000(+15%)；包含 Pro 全部功能；可与 Pro 并存补充 | 高用量团队 |

**付费墙**：Discover/Inspect 永远免费；Call 消耗 credits（1–100/次）。credits 永不过期、无自动续费。企业版需联系销售（定制 SLA、专属支持、批量折扣）。

## 5. 功能 ↔ 场景映射简表

> 完整映射见 [qveris-use-cases.md](./qveris-use-cases.md#3-场景--功能--关键词全映射表)

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| Discover/Inspect/Probe/Call 协议 | 量化交易数据获取、财报研究 | 量化工程师、金融研究员 |
| 六大金融能力域 | 美股/A 股行情、SEC 文件、宏观指标、加密数据 | 投资研究分析师 |
| Application Center | Earnings Copilot 财报研究、Options Assistant 期权分析 | 投资研究分析师、量化工程师 |
| QVeris Lab / QVerisBot | 无代码股票研究、市场情报日报、内容运营 | 投资决策者、内容创作者 |
| CLI | 零 token 生产代理集成 | 代理工程师 |
| MCP / Hosted MCP | Cursor/Claude Code 内实时调用 | 开发者、代理工程师 |
| 计费与审计 | 成本控制、合规追溯 | 平台负责人、财务 |

---

*Last updated 2026-08-05 · 数据来源：官网首页/定价页/docs/cli/for-agents/ecosystem/whats-new/apps 抓取（2026-08-05）*
