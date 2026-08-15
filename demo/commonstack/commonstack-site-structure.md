# Commonstack 网站结构

> **文档边界**：本文档仅含页面优先级、URL 规划、导航层级、与关键词/场景/增长的映射。功能参数见 [commonstack-features.md](./commonstack-features.md)；关键词映射见 [commonstack-keywords.md](./commonstack-keywords.md)；竞品见 [commonstack-competitors.md](./commonstack-competitors.md)；场景见 [commonstack-use-cases.md](./commonstack-use-cases.md)；增长策略见 [commonstack-growth-strategy.md](./commonstack-growth-strategy.md)。全量路由明细（sitemap 抓取、状态跟踪表）见 [commonstack-others.md](./commonstack-others.md)。
>
> 关联：[commonstack.md](./commonstack.md) | [commonstack-features.md](./commonstack-features.md) | [commonstack-keywords.md](./commonstack-keywords.md) | [commonstack-use-cases.md](./commonstack-use-cases.md) | [commonstack-growth-strategy.md](./commonstack-growth-strategy.md)

---

## 一、域名与导航架构

### 1.1 域名分布

| 域名 | 用途 | 当前状态 |
|------|------|----------|
| **commonstack.ai** | 主站 / 产品页 | ✓ 已上线 |
| **docs.commonstack.ai** | 开发者文档 / Quickstart / Playground | ✓ 已上线 |
| **api.commonstack.ai** | API 端点（OpenAI `/v1` + Anthropic 根路径） | ✓ 生产 |
| **github.com/CommonstackAI** | 开源组织（5 个公开仓库） | ✓ 活跃 |

### 1.2 主导航（建议结构）

```
commonstack.ai/
├── /                    # 首页：价值主张 + 快速开始
├── /model-library       # 模型目录与定价（已有）
├── /pricing             # 计费说明页（建议独立）
├── /docs                # → docs.commonstack.ai
├── /blog                # 博客（待建）
├── /compare             # 竞品对比页（待建）
├── /ecosystem           # Gradient 生态页（待建）
├── /open-source         # 开源项目聚合页（待建）
├── /use-cases/          # 场景落地页（待建）
│   ├── /use-cases/agents
│   ├── /use-cases/startups
│   └── /use-cases/multi-model
├── /for/                # Persona 页（待建）
│   ├── /for/developers
│   └── /for/startups
└── /security            # 安全与合规页（待建）
```

---

## 二、页面优先级与分阶段规划

### 2.1 Phase 0（已上线）

| 页面 | URL | 状态 | 当前内容 |
|------|-----|------|----------|
| 首页 | / | ✓ | 产品价值主张、Quickstart 入口 |
| 模型目录 | /model-library | ✓ | 模型列表与定价 |
| 开发者文档 | docs.commonstack.ai | ✓ | Quickstart、Playground、API 参考 |
| API 端点 | api.commonstack.ai/v1 | ✓ | OpenAI 兼容端点 |
| API 端点 | api.commonstack.ai（Anthropic 路径） | ✓ | Anthropic 兼容端点 |

### 2.2 Phase 1（建议优先——当前补齐）

| 页面 | 建议 URL | 理由 | 承接关键词 |
|------|----------|------|------------|
| **计费说明** | /pricing | 独立 pricing 页提升可发现性，当前计费信息散落在文档中 | token billing LLM, LLM API pricing, pay as you go LLM |
| **OpenAI 兼容详解** | /docs/openai-compatible | 承接迁移人群的搜索意图 | OpenAI compatible API, OpenAI base URL custom gateway |
| **Anthropic 兼容详解** | /docs/anthropic-compatible | 双协议差异化叙事 | Anthropic API gateway |
| **安全与合规** | /security | 企业客户必看，建立信任 | API key security, data handling LLM |

### 2.3 Phase 2（1-2 月）

| 页面 | 建议 URL | 理由 | 承接关键词 |
|------|----------|------|------------|
| **博客** | /blog | 内容营销主阵地，见 growth-strategy.md §2.2 | 多类长尾教程词 |
| **竞品对比** | /compare | 拦截竞品搜索意图 | OpenRouter alternative, Together AI vs, unified API vs direct OpenAI |
| **开源项目** | /open-source | 聚合 GitHub 仓库介绍，引流至 UncommonRoute 等 | Commonstack GitHub, local LLM router |
| **生态页** | /ecosystem | Gradient 产品线的统一叙事入口 | Gradient AI, Open Intelligence Stack |
| **Agent 场景页** | /use-cases/agents | 承接 Agentic AI 增长最快的负载类型 | multi-provider AI API, Agent architecture |

### 2.4 Phase 3（3-4 月——路线图能力上线后）

| 页面 | 建议 URL | 理由 | 承接关键词 |
|------|----------|------|------------|
| **Prompt Caching 页** | /features/caching | 路线图能力上线时配独立页 | prompt caching API aggregator |
| **智能路由页** | /features/routing | 同上，强化与 OpenRouter 的差异化 | LLM routing, AI API routing |
| **Persona 页** | /for/developers, /for/startups | 按受众讲故事 | unified API for developers/startups |
| **案例研究** | /customers | 上线客户案例后建立 | LLM API case study |

---

## 三、页面与六文档的交叉映射

### 3.1 页面 → 关键词

| 页面 | 核心承载的关键词 |
|------|-----------------|
| / | unified LLM API, single API key multiple models, Commonstack |
| /model-library | multi-provider AI API, LLM API list, per-model pricing |
| /pricing | token billing LLM, pay as you go LLM, LLM API cost |
| /docs/openai-compatible | OpenAI compatible API, OpenAI base URL custom gateway |
| /docs/anthropic-compatible | Anthropic API gateway, Claude API gateway |
| /compare | OpenRouter alternative, Together AI vs, unified API comparison |
| /blog/* | switch from OpenAI to multi model API, LLM cost optimization, Agent API |
| /use-cases/agents | multi-provider AI API, Agent architecture API |
| /open-source | Commonstack GitHub, UncommonRoute, local LLM router cost |
| /ecosystem | Gradient AI, Open Intelligence Stack, Parallax distributed serving |

### 3.2 页面 → 使用场景

| 页面 | 目标 Persona | 核心场景 |
|------|-------------|----------|
| /、/model-library | 后端工程师 | 多模型应用、单 Key 多厂商 |
| /pricing、/docs | 全栈/indie | 小团队商业化、按量付费 |
| /security、/compare | 技术负责人 | 供应商策略、成本可见性 |
| /use-cases/agents、/blog | AI 产品团队 | Agent 与自动化、快速试模型 |

### 3.3 页面 → 增长策略

| 页面 | 增长目标 | 对应的增长动作 |
|------|----------|---------------|
| /blog | 自然搜索流量 | 内容日历 §2.2 的 6 篇文章 |
| /compare | 竞品拦截 | 拦截 OpenRouter/Together 相关搜索 |
| /ecosystem | Gradient 生态导流 | 双向互链，「自托管 ↔ 托管」叙事 |
| /open-source | 开源社区转化 | GitHub → 托管 API 的转化路径 |

---

## 四、技术 SEO 检查项

| 项目 | 状态 | 备注 |
|------|------|------|
| Model Library 可索引 | 待验证 | 确保不被 noindex |
| title / description 独立 | 待检查 | 每页应有独立的 title 和 meta description |
| sitemap.xml | 待确认 | 需确认是否已提交 Search Console |
| 结构化数据 | 未实施 | Model Library 建议加 Product/SoftwareApplication schema |
| /docs 子域名 | 已有 | docs.commonstack.ai 作为独立子域名，注意跨域规范 |
| 博客 RSS | 待建 | 博客上线后配置 |

---

## 五、URL 规划原则

1. **独立页面优先**：/pricing、/compare、/security 等高价值页面独立建页，不嵌在文档内
2. **子目录非子域名**：博客用 /blog 而非 blog.commonstack.ai，利于主域权重积累
3. **场景页按需扩展**：/use-cases/ 下按负载类型（agents、multi-model、startups）逐步增加
4. **对比页保持客观**：/compare 只列维度对比，不攻击竞品
5. **生态页链接外链**：/ecosystem 链向 gradient.network、GitHub，强化品牌关联

---

*文档生成日期：2026-05-10 | 模式 A 冷启动扩充 | 来源：已有文档 + 联网检索 + 逻辑推演*
