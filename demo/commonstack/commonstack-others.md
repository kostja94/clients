# Commonstack Others（杂项汇编）

> **本文职责**：Sitemap 明细、Proof 与数据引用、Trust / 合规、定价备忘、Backlog、归档。不参与每轮必跑的六主文档联动循环，按需更新。
>
> 关联：[commonstack.md](./commonstack.md) | [commonstack-keywords.md](./commonstack-keywords.md) | [commonstack-competitors.md](./commonstack-competitors.md) | [commonstack-features.md](./commonstack-features.md) | [commonstack-use-cases.md](./commonstack-use-cases.md) | [commonstack-growth-strategy.md](./commonstack-growth-strategy.md) | [commonstack-site-structure.md](./commonstack-site-structure.md)

---

## 1. Sitemap 与路由明细

> 全量路由抓取与状态跟踪表。网站结构主文档 [commonstack-site-structure.md](./commonstack-site-structure.md) 写**策略与优先级**，本文档写**明细**。

### 1.1 Sitemap 索引（待抓取确认）

| Sitemap | URL | 状态 |
|---------|-----|------|
| 主站 | https://commonstack.ai/sitemap.xml | 待确认 |
| 文档 | https://docs.commonstack.ai/sitemap.xml | 待确认 |

### 1.2 已知页面清单

| URL | 类型 | 索引状态 | 备注 |
|-----|------|----------|------|
| commonstack.ai/ | 首页 | 待确认 | |
| commonstack.ai/model-library | 模型目录 | 待确认 | |
| docs.commonstack.ai/ | 文档首页 | 待确认 | |
| docs.commonstack.ai/overview/quickstart | 快速开始 | 待确认 | |
| docs.commonstack.ai/platform/playground | Playground | 待确认 | |
| api.commonstack.ai/v1 | API 端点 | N/A | |

---

## 2. Proof 与数据引用

### 2.1 市场数据（来源与日期）

| 数据点 | 数值 | 来源 | 日期 |
|--------|------|------|------|
| LLM 网关平台市场规模 | $4.23B（2026），CAGR 26.7% | GII Research / TBRC | 2026-Q1 |
| LLM 网关市场 2030 预测 | $11.01B | GII Research | 2026-Q1 |
| 企业平均使用模型数 | 4.7（2026），2.1（2025） | 行业报告 | 2026-Q1 |
| AI 组织采用率 | 78%（2026），55%（2025） | McKinsey | 2026-Q1 |
| OpenRouter 周 token 量 | ~12 万亿（2026-04） | OpenRouter 公开数据 | 2026-04 |
| 中国模型 token 份额 | 36%（2026-04） | OpenRouter 公开数据 | 2026-04 |
| Agent 负载占新增集成 | 41% | AI.cc 报告 | 2026-Q1 |
| API 集成 YoY 增长 | 300% | AI.cc | 2026-Q1 |

### 2.2 竞品数据

| 数据点 | 数值 | 来源 | 日期 |
|--------|------|------|------|
| OpenRouter 用户数 | 8M+ | OpenRouter 官网 | 2026-04 |
| OpenRouter 模型数 | 300-400+ | OpenRouter 官网 | 2026-04 |
| UncommonRoute GitHub stars | 519+ | SourcePulse / GitHub | 2026-05 |
| LiteLLM GitHub stars | 41.1k | GitHub | 2026-04 |
| Gradient Network 融资 | $10M Seed | CoinMarketCap / Messari | 2026-03 |
| DeepSeek V4-Flash 定价 | $0.14/$0.28 per M tokens | DeepSeek 官网 | 2026-04 |
| Claude Opus 4.7 定价 | $5/$25 per M tokens | Anthropic 官网 | 2026-04 |

### 2.3 Commonstack 自有数据

| 数据点 | 数值 | 来源 | 日期 |
|--------|------|------|------|
| UncommonRoute cost saving | 82% | UncommonRoute README | 2026-05 |
| UncommonRoute task pass rate | 93.4% | UncommonRoute README | 2026-05 |
| Quickstart 时间 | ~2 分钟 | docs.commonstack.ai | 2026-03 |
| 首充 bonus | 20%，上限 $500 | docs.commonstack.ai | 2026-03 |
| CommonstackAI 公开仓库数 | 5 | GitHub API | 2026-03 |

---

## 3. Trust / 合规

### 3.1 合规状态（待客户确认）

| 项目 | 状态 | 备注 |
|------|------|------|
| SOC 2 | 待确认 | 企业客户常问 |
| GDPR | 待确认 | 欧盟市场准入 |
| 数据驻留 | 待确认 | 强合规行业需明确 |
| DPA（数据处理协议） | 待确认 | |
| 等保 | 待确认 | 中国市场 |

### 3.2 高利害表述禁区

- **医疗/健康类**：不与任何诊断、治疗、处方等挂钩
- **金融建议**：不提供投资建议类表述
- **儿童数据**：不提及收集或处理未成年人数据
- **竞品攻击**：对比页只列客观维度，不使用贬损语言
- **性能承诺**：不保证 100% uptime，引用 SLA 时以官方条款为准

### 3.3 危机话术占位

如遇服务中断/数据事件，沟通要素：
- 确认事件范围与时间线
- 说明当前状态与修复进展
- 受影响用户的通知渠道
- 事后改进措施

*具体话术视事件性质由客户团队制定，本文档仅保留框架。*

---

## 4. 定价备忘

| 维度 | 内容 | 来源 | 备注 |
|------|------|------|------|
| 计费模式 | 按 token 用量 | docs.commonstack.ai | |
| 月费/订阅 | 文档表述为无强制月费类订阅 | docs.commonstack.ai | 以官网条款为准 |
| 支付方式 | 信用卡（Stripe）、支付宝 | docs.commonstack.ai | |
| 首充激励 | 20% bonus，上限 $500 | docs.commonstack.ai | 以官网最新为准 |
| 定价公开页 | /model-library（当前）| commonstack.ai | 建议建独立 /pricing |

---

## 5. Backlog（调研待办）

| ID | 从哪份文档哪条引出 | 需查证什么 | 优先级 | 计划来源 | 结果摘要 | 来源/日期 |
|----|-------------------|------------|--------|----------|----------|-----------|
| R1 | competitors.md §6.3 | Commonstack 是否已通过 SOC 2 / GDPR 认证 | P0 | 联网/客户确认 | | |
| R2 | site-structure.md §4 | commonstack.ai 是否已有 sitemap.xml 并提交 Search Console | P1 | 联网 | | |
| R3 | competitors.md §6.2 | Commonstack 当前各模型实际定价 vs OpenRouter 同模型定价 | P1 | 联网 | | |
| R4 | keywords.md Agent 分类 | Agent 相关的搜索量数据（AI agent API gateway 等） | P2 | 联网/SEO 工具 | | |
| R5 | growth-strategy.md §3.2 | UncommonRoute GitHub README 加「Try Managed API」的转化率 | P2 | 实验 | | |
| R6 | features.md §六 | Prompt caching / Routing 功能的具体上线时间 | P0 | 客户确认 | | |

---

## 6. 归档

> 被覆盖的旧判断、已弃用的表述移入此处，保留日期和来源以备追溯。

*当前无归档内容。*

---

## CHANGELOG 索引

| 文件 | Last updated |
|------|-------------|
| commonstack.md | 2026-03-29 |
| commonstack-keywords.md | 2026-05-10（扩充） |
| commonstack-competitors.md | 2026-05-10（扩充） |
| commonstack-features.md | 2026-03-29 |
| commonstack-use-cases.md | 2026-05-10（扩充） |
| commonstack-growth-strategy.md | 2026-05-10（新建） |
| commonstack-site-structure.md | 2026-05-10（新建） |
| commonstack-others.md | 2026-05-10（新建） |
| commonstack-open-source.md | 2026-03-29 |
| commonstack-ecosystem.md | 2026-03-29 |

---

*文档生成日期：2026-05-10 | 模式 A 冷启动扩充*
