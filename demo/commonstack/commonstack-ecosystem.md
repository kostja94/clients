# 生态关联：Gradient 与 Parallax（同团队产品线）

> **本文职责**：Gradient 品牌与 OIS、同团队产品分工、Parallax 技术摘要、互链建议；**不含** CommonstackAI 仓库清单（见 [commonstack-open-source.md](./commonstack-open-source.md)）。  
> 关联：[commonstack.md](./commonstack.md) | [commonstack-open-source.md](./commonstack-open-source.md) | [commonstack-competitors.md](./commonstack-competitors.md)  
> **团队关系（项目方已确认）**：**Commonstack** 与 **Gradient** 为**同一团队**；**[gradient.network](https://gradient.network/)** 为 Gradient 主站。

---

## 一、Gradient 主站与品牌叙事

| 项目 | 内容 |
|------|------|
| **主站** | **[gradient.network](https://gradient.network/)** — Gradient 对外品牌入口（页面以品牌展示为主，深度说明见文档站）。 |
| **文档总览** | **[Meet Gradient](https://docs.gradient.network/)**（与 `/meet-gradient` 同源内容）：阐述实验室定位与 **OIS（Open Intelligence Stack）**。 |

据 [Meet Gradient](https://docs.gradient.network/) 英文原文归纳：

- **Gradient** 定位为 **AI R&D lab**，通过**完全去中心化基础设施**构建 **open intelligence**；当前 **OIS** 覆盖分布式 **训练、推理（serving）、Agent 系统** 等。
- 提出的问题域：**Blockchain × AI** 交叉——如何在公网上 **训练/服务** 优质 LLM，能否在**无许可、自治网络**上构建可与 OpenAI 等竞争的能力。
- **当前 OIS 组成**（文档原文列举）：**Parallax**（distributed serving）、**Echo**（distributed reinforcement learning）、**Gradient Cloud**（enterprise solutions）。
- **Mission**：构建「世界首个 Open Intelligence Stack」——**sovereign、peer-powered** 的基础设施，使智能由人们托管、服务与拥有；目标是全球基础，支持智能的**分发、演化与具身**。

*以上引述用于营销与外链上下文；具体英文以官网为准。*

---

## 二、同团队下的产品分工（叙事建议）

| 产品线 | 代表入口 | 与 Commonstack 的分工 |
|--------|----------|------------------------|
| **Commonstack** | [commonstack.ai](https://commonstack.ai/) · [docs.commonstack.ai](https://docs.commonstack.ai/) | **托管侧统一 LLM API**：单 Key、OpenAI/Anthropic 双协议、多厂商模型、按 token 计费等（见主文档）。 |
| **Parallax** | [github.com/GradientHQ/parallax](https://github.com/GradientHQ/parallax) · [文档](https://docs.gradient.network/open-source/parallax) | **分布式推理 / 自建集群**：多机异构、主权部署、与 SGLang/vLLM/MLX 等栈结合。 |
| **Echo** | 见 [docs.gradient.network](https://docs.gradient.network/) 导航 | **分布式强化学习**（文档归类在 OIS 内）。 |
| **Gradient Cloud** | 如 [Gradient Cloud](https://docs.gradient.network/platform/gradient-cloud) | **企业级**交付与平台能力（以文档为准）。 |

**一句话**：同一团队下，**Parallax 偏「自有算力与分布式 serving」**，**Commonstack 偏「云端聚合与一钥多模型」**；对外可组合为「**主权推理 + 托管 API**」全栈故事。

---

## 三、Parallax 技术要点（README 与文档）

**一句话**：**分布式模型推理框架**——在多台异构设备上自建「AI 集群」；README 亦表述为 *distributed model serving framework* / Gradient 侧 *decentralized inference engine*。

**文档表述**（[Parallax · Gradient Docs](https://docs.gradient.network/open-source/parallax)）：面向 **sovereign AI** 的分布式运行时；多机编排为可追溯服务；**40+** 开源模型、多 OS 与 GPU / Apple Silicon 等（以文档为准）。

**README 能力摘要**（[README](https://github.com/GradientHQ/parallax?tab=readme-ov-file)）：本地托管 LLM、跨平台、**pipeline parallel sharding**、Mac 上 **paged KV / continuous batching**、**动态调度与路由**；后端涉及 **Lattica**（P2P）、**SGLang / vLLM**（GPU）、**MLX LM**（Mac）。**Apache-2.0**。

**动态**：News 中含 **OpenClaw** 集成、Product Hunt 成绩、版本发布等（见仓库）。

---

## 四、与 Commonstack 的互补叙事（已确认同团队）

| 维度 | Parallax | Commonstack |
|------|----------|-------------|
| **形态** | 自托管、分布式、多机推理 | 云端统一 API、多厂商路由与计费 |
| **典型用户** | 要主权与自有集群的团队 | 要快集成、少账户、合并账单的开发者 |

同团队可在 **官网页脚、About、博客、OpenClaw 相关页** 双向互链，避免用户误以为彼此无关。

---

## 五、互链与署名建议（同团队可直接推进）

| 位置 | 建议 |
|------|------|
| **[commonstack.ai](https://commonstack.ai/) / [docs.commonstack.ai](https://docs.commonstack.ai/)** | 增加「**Part of Gradient**」或「**Gradient 产品**」：链向 [gradient.network](https://gradient.network/)，并列出 **Parallax**、**OIS** 等（与设计一致即可）。 |
| **[gradient.network](https://gradient.network/)** | 在合适板块加入 **Commonstack**（统一 LLM API）与链接至 commonstack.ai / 文档。 |
| **Parallax README / [Gradient Docs](https://docs.gradient.network/)** | 在 Ecosystem / Related 中增加 **Commonstack**（托管 API 网关），形成「自托管 Parallax ↔ 托管 Commonstack」路径。 |
| **GitHub** | **CommonstackAI** 与 **GradientHQ** 可在 Org Profile 互相指向或通过官网统一说明「同属 Gradient 团队」。 |

---

## 六、参考链接

- [gradient.network](https://gradient.network/) — Gradient 主站  
- [Meet Gradient](https://docs.gradient.network/) — 实验室与 OIS 叙事  
- [Parallax · Gradient Documentation](https://docs.gradient.network/open-source/parallax)  
- [GradientHQ/parallax](https://github.com/GradientHQ/parallax) — 源码与 README  
- [Commonstack Docs](https://docs.commonstack.ai/) — 与上并列作互链  

---

*文档生成日期：2026-03-29 · 团队关系依据项目方确认；Gradient 引文摘自 [docs.gradient.network](https://docs.gradient.network/) 等公开页面。*
