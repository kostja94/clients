# Commonstack 增长策略

> **文档边界**：本文档仅含增长渠道、内容策略、战役节奏与实验方向。产品概览见 [commonstack.md](./commonstack.md)；关键词映射见 [commonstack-keywords.md](./commonstack-keywords.md)；网站结构见 [commonstack-site-structure.md](./commonstack-site-structure.md)；竞品见 [commonstack-competitors.md](./commonstack-competitors.md)；功能见 [commonstack-features.md](./commonstack-features.md)；场景见 [commonstack-use-cases.md](./commonstack-use-cases.md)。
>
> **市场背景**：LLM API 网关市场 2026 年规模约 $4.23B，CAGR 26.7%；企业平均使用 4.7 个模型（较 2025 年翻倍）；OpenRouter 周 token 量 ~12 万亿；中国模型 token 份额从 10% 升至 36%（2026 Q1→Q2）。Agentic AI 是增长最快的负载类型，占新增集成的 41%。

---

## 一、增长渠道与战役方向

### 1.1 渠道总览

| 渠道 | 优先级 | 当前状态 | 核心策略 |
|------|--------|----------|----------|
| **开源社区 / GitHub** | P0 | 已有 5 仓库（UncommonRoute 519+ stars） | 以 UncommonRoute 为增长引擎，README 引流至托管 API；ClawBox 带动 Agent 生态 |
| **开发者内容 / SEO** | P0 | 已有 docs.commonstack.ai，博客待建 | 迁移指南 + 对比页 + 技术教程，承接长尾搜索意图 |
| **Gradient 生态互链** | P1 | 已有 ecosystem.md 梳理，官网互链待执行 | 同团队品牌互相导流：「Part of Gradient」→ Commonstack API，「自托管 Parallax ↔ 托管 Commonstack」 |
| **模型提供商合作** | P1 | 已有 7+ 提供商接入 | 联合博客 / case study，强化「覆盖最广」叙事 |
| **Product Hunt / Hacker News** | P2 | OpenClaw 已有 PH 发布经验 | 路线图功能上线时发布（caching、routing） |
| **付费广告 / 赞助** | P3 | 未启动 | 待 MRR 稳定后测试开发者社区赞助 |

### 1.2 战役节奏（建议）

| 阶段 | 时间 | 动作 | 目标 |
|------|------|------|------|
| **Phase 1** | 当前 | Model Library 可索引、Quickstart 示例完善、GitHub 仓库 README 优化 | 自然搜索覆盖品牌词 + 核心定位词 |
| **Phase 2** | 1-2 月 | 发布 3-5 篇技术博客（迁移指南、成本对比、Agent 集成），发布 `/compare` 对比页 | 拦截竞品词 + 长尾教程类搜索 |
| **Phase 3** | 3-4 月 | Prompt caching / Routing 上线时发布 Product Hunt + 技术解读 | 功能差异化叙事，获取新用户潮 |
| **Phase 4** | 5-6 月 | 案例研究 + 模型提供商联合推广 | 品牌信任 + 企业级客户获取 |

---

## 二、内容策略

### 2.1 内容主题与栏目

| 栏目 | 内容方向 | 目标关键词 | 承接 URL |
|------|----------|------------|----------|
| **迁移指南** | OpenAI → Commonstack 5 分钟迁移、Anthropic SDK 切换、LangChain 集成 | OpenAI compatible API, switch from OpenAI, Anthropic API gateway | /blog/migrate-from-openai, /docs/quickstart |
| **成本对比** | OpenRouter vs Commonstack、Together AI vs、直连 vs 聚合 | unified API pricing, LLM API cost comparison | /compare, /blog/llm-api-cost-comparison |
| **技术教程** | 多模型路由最佳实践、Agent 架构中的 API 网关、token 成本优化 | multi-model API, LLM router, API gateway best practices | /blog, /docs |
| **产品更新** | Prompt caching 上线、智能路由、新模型接入 | prompt caching API, LLM routing | /blog, /changelog |
| **生态故事** | Gradient OIS × Commonstack 全栈 AI、开源 vs 托管互补 | Gradient AI, Open Intelligence Stack | /ecosystem, 跨域博客 |

### 2.2 内容日历（建议首 6 篇）

| 序号 | 标题方向 | 类型 | 承接关键词 |
|------|----------|------|------------|
| 1 | 「从 OpenAI 迁移到 Commonstack：5 分钟切换指南」 | 教程 | OpenAI compatible API, switch from OpenAI |
| 2 | 「2026 LLM API 网关对比：OpenRouter vs Together vs Commonstack」 | 对比 | OpenRouter alternative, unified API vs |
| 3 | 「为什么你的 AI Agent 需要一个统一的 API 网关」 | 思想领导 | multi-model API, Agent architecture |
| 4 | 「LLM 成本优化实战：80% 的请求用便宜模型，20% 用旗舰模型」 | 教程 | LLM cost optimization, token billing |
| 5 | 「Commonstack × Gradient：从开源路由到托管 API 的全栈 AI 基础设施」 | 生态故事 | Gradient AI, AI infrastructure |
| 6 | 「DeepSeek + Claude 双模型架构：用 Commonstack 统一调度」 | 教程 | DeepSeek API unified, Claude API gateway |

---

## 三、话术与定位实验

### 3.1 核心叙事（当前）

> **One API key. All the models.** — 双协议（OpenAI + Anthropic）同域同 Key，多厂商模型统一接入。

### 3.2 可实验的替代叙事

| 叙事方向 | 一句话 | 目标受众 | 实验方式 |
|----------|--------|----------|----------|
| **成本优先** | "Switch models, not your code. Save up to 80% on LLM costs." | indie / 小团队 | 首页 A/B 测试 |
| **Agent 原生** | "The API gateway built for AI agents — route, cache, fallback automatically." | AI 产品团队 | 落地页 + 博客 |
| **开源 → 托管** | "Start with UncommonRoute (OSS), scale with Commonstack (cloud)." | 开发者社区 | GitHub README + 文档 |
| **支付宝 / 中国市场** | "首个支持支付宝的全球 LLM API 网关。" | 中国开发者 | 中文落地页 |

### 3.3 信任信号（目前可用的）

- **1,000,000+ users**（若官网展示）
- **519+ GitHub stars**（UncommonRoute）
- **MIT 开源**
- **Gradient 团队背书**（$10M 融资）
- **Quickstart：2 分钟首次调用**
- **支付宝 / 信用卡支付**

---

## 四、与关键词 / 网站结构的对齐

| 增长动作 | 关联关键词（详见 keywords.md） | 关联结构（详见 site-structure.md） |
|----------|-------------------------------|-----------------------------------|
| 迁移指南发布 | OpenAI compatible API, switch from OpenAI to multi model API | /blog/migrate-from-openai, /docs/openai-compatible |
| 对比页上线 | OpenRouter alternative, Together AI vs, unified API vs direct OpenAI | /compare |
| 成本教程 | token billing LLM, LLM API cost comparison | /blog, /pricing |
| Agent 教程 | multi-provider AI API, single API key multiple models | /docs, /use-cases/agents |
| 路由功能上线 | prompt caching API aggregator, LLM routing | /features/routing, /blog |
| GitHub 优化 | Commonstack GitHub, UncommonRoute, local LLM router cost | GitHub README, /open-source |
| Gradient 互链 | Gradient AI, Open Intelligence Stack, Parallax | /ecosystem, footer |

---

## 五、实验假设与待验证

| ID | 假设 | 验证方式 | 状态 |
|----|------|----------|------|
| G1 | 「迁移指南」类内容比「对比页」带来更多注册 | 分别发布，追踪转化 | 待验证 |
| G2 | GitHub README 中加「Try Managed API」链接可提升托管侧注册 | A/B README 文案 | 待验证 |
| G3 | 中文落地页（支付宝故事）可显著提升中国区注册 | 创建中文页后对比流量 | 待验证 |
| G4 | Product Hunt 发布（routing 功能上线时）可带来 ≥500 upvotes | 发布后追踪 | 待验证 |
| G5 | 与 DeepSeek / MiniMax 联合博客比单方面对比文效果好 | 尝试合作后对比效果 | 待验证 |

---

## 六、指标追踪（建议）

| 指标 | 当前基线 | 目标（3 月） | 目标（6 月） |
|------|----------|-------------|-------------|
| 自然搜索月流量 | 待测量 | +50% | +150% |
| 注册数（月） | 待测量 | 基准 | 2× |
| 首次调用 → 付费转化 | 待测量 | 基准 | 优化 20% |
| UncommonRoute GitHub stars | ~519 | 800 | 1500 |
| 博客文章数 | 0 | 5 | 12 |
| 竞品对比词排名 | 未上榜 | Top 20 | Top 10 |

---

*文档生成日期：2026-05-10 | 模式 A 冷启动扩充 | 来源：联网检索（OpenRouter 公开数据、LLM 网关市场报告、CommonstackAI GitHub、Gradient Network 公开信息）+ 逻辑推演*
