# Commonstack

> **本文职责**（见仓库根目录 [元文档-通用文档规范.md](../../通用知识库/元文档-通用文档规范.md)）：本文件只承担 **产品概览、定位、网站结构、增长与信息架构入口**；**不展开**关键词全表、竞品拆解、功能明细表、开源仓库清单、Gradient/Parallax 长文——上述内容以子文档为准，避免重复。

## 文档导航

| 文档 | 职责 |
|------|------|
| [commonstack-features.md](./commonstack-features.md) | 协议与端点、模型与计费、路线图、URL 建议 |
| [commonstack-use-cases.md](./commonstack-use-cases.md) | 场景、Persona、JTBD、不适用边界 |
| [commonstack-keywords.md](./commonstack-keywords.md) | 关键词映射、待办 |
| [commonstack-competitors.md](./commonstack-competitors.md) | 竞品类型、场景级对照表、差异化 |
| [commonstack-growth-strategy.md](./commonstack-growth-strategy.md) | 增长渠道、内容策略、战役节奏、话术实验 |
| [commonstack-site-structure.md](./commonstack-site-structure.md) | 页面优先级、URL 规划、导航层级、与关键词/场景/增长的映射 |
| [commonstack-others.md](./commonstack-others.md) | Sitemap 明细、Proof 数据、Trust/合规、定价备忘、Backlog |
| [commonstack-open-source.md](./commonstack-open-source.md) | GitHub 组织与仓库列表 |
| [commonstack-ecosystem.md](./commonstack-ecosystem.md) | Gradient 主站、OIS、Parallax、同团队互链 |

*产品入口*：[commonstack.ai](https://commonstack.ai/) · [docs.commonstack.ai](https://docs.commonstack.ai/) · [CommonstackAI](https://github.com/CommonstackAI) · [gradient.network](https://gradient.network/)

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2B / 开发者工具 / LLM API 聚合 / 推理网关 |
| 网站 | https://commonstack.ai/ |
| 产品形态 | **统一 LLM API 网关**：单 Key、双协议端点，多提供商模型接入 |
| 当前阶段 | 生产 API；Quickstart、Playground；路线图含 Prompt caching、智能路由与 fallback（详见 [commonstack-features.md](./commonstack-features.md)） |
| 核心产品 | **Commonstack**：Unified API gateway for large language models |
| 母品牌 / 团队 | **Gradient** — [gradient.network](https://gradient.network/) · [Meet Gradient](https://docs.gradient.network/)（OIS、Parallax、Echo、Gradient Cloud 等）；叙事与互链见 [commonstack-ecosystem.md](./commonstack-ecosystem.md) |
| 差异化摘要 | OpenAI + Anthropic 兼容同域同 Key；按 token 计费与合并账单；多模态；工程支持（详见官方 [About](https://docs.commonstack.ai/)） |
| GitHub 开源 | 见 [commonstack-open-source.md](./commonstack-open-source.md) |
| 更新日期 | 2026-03-29 |

---

## 1. 产品信息

### 摘要与定位

**Commonstack** 是 **大语言模型统一 API 网关**：一次集成即可用 **OpenAI 兼容** 或 **Anthropic 兼容** 端点调用多提供商模型，沿用常见 SDK。计费为 **按 token**；首充等政策以官网为准。

与 OpenRouter、Fal、Together 等同属 **统一模型接入层**；Commonstack 强调 **双协议同 Key**、标准参数透传、合并计费与支付渠道（见文档）。

**目标受众**：应用/后端开发者；Agent 与自动化团队；希望减少多供应商账户与对账成本的团队。

**能力明细、端点 URL、计费表、路线图**：见 [commonstack-features.md](./commonstack-features.md)。

### 关键外链

| 资源 | URL |
|------|-----|
| Model Library | https://commonstack.ai/model-library |
| Quickstart | https://docs.commonstack.ai/overview/quickstart |
| Playground | https://docs.commonstack.ai/platform/playground |
| 官方 About | https://docs.commonstack.ai/ |

---

## 2. 网站结构

> 完整网站结构（页面优先级、URL 规划、导航架构、与关键词/场景/增长的映射）见 [commonstack-site-structure.md](./commonstack-site-structure.md)。以下为摘要。

| 路径 / 资源 | 说明 |
|-------------|------|
| / | 主站 |
| /model-library | 模型与定价 |
| docs.commonstack.ai | 文档与 Playground |
| api.commonstack.ai/v1 | OpenAI 兼容 |
| api.commonstack.ai（Anthropic 路径） | Anthropic 兼容 |

**待建页面优先级**：见 [commonstack-site-structure.md §2](./commonstack-site-structure.md)。

---

## 3. 增长与信息架构

> 完整增长策略（渠道、内容日历、话术实验、指标追踪）见 [commonstack-growth-strategy.md](./commonstack-growth-strategy.md)。以下为摘要。

**关键词全表与页面待办**：见 [commonstack-keywords.md](./commonstack-keywords.md)。

**竞品分析**：见 [commonstack-competitors.md](./commonstack-competitors.md)。

**场景与 Persona**：见 [commonstack-use-cases.md](./commonstack-use-cases.md)。

**开源与 Gradient 产品线**：仓库清单见 [commonstack-open-source.md](./commonstack-open-source.md)；Gradient / Parallax / 互链见 [commonstack-ecosystem.md](./commonstack-ecosystem.md)。

### 内容与技术叙事

- 开发者教育：Quickstart、迁移 Checklist（与 Features 联动）。
- 开源联动：UncommonRoute、ClawBox 等仅指向 [commonstack-open-source.md](./commonstack-open-source.md)，不在此重复列举。
- 母品牌：Commonstack 与 Gradient 的组合叙事见 [commonstack-ecosystem.md](./commonstack-ecosystem.md)。

### 页面落地阶段（与关键词 P0–P3 对齐）

| 阶段 | 动作 |
|------|------|
| Phase 1 | Model Library、Quickstart、定价相关页可发现、可索引 |
| Phase 2 | 博客：多模型路由、成本、Agent 集成 |
| Phase 3 | `/alternatives` 或对比文，拦截竞品词 |
| Phase 4 | 路线图能力（caching、routing）上线后同步文档与竞品叙事 |

---

*文档生成日期：2026-03-29 | 最近更新：2026-05-10（v9 扩充：新增 growth-strategy、site-structure 子文档，更新导航表） | 主来源：[docs.commonstack.ai](https://docs.commonstack.ai/)、[commonstack.ai](https://commonstack.ai/)、[github.com/CommonstackAI](https://github.com/CommonstackAI)、[gradient.network](https://gradient.network/)、[docs.gradient.network](https://docs.gradient.network/)*
