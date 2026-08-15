# SenseNova — 竞品分析

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./sensenova.md) | [features](./sensenova-features.md) | [keywords](./sensenova-keywords.md) | [site-structure](./sensenova-site-structure.md) | [use-cases](./sensenova-use-cases.md) | [growth-strategy](./sensenova-growth-strategy.md) | [README](./README.md)

**Last updated**: 2026-07-27  
**焦点产品**：SenseNova U1 / U1 Pro / U1 Fast + Flash-Lite 办公层

---

## 1. 竞品总览

| 竞品 | 定位 | 目标用户 | 核心功能 | 价格区间 | 与本品差异 |
|------|------|---------|---------|---------|-----------|
| **OpenAI GPT-4o / 后续多模态** | 通用多模态助手 + API | 全球开发者与企业 | 视觉理解、对话、工具调用、生图（产品线拆分演进中） | 订阅 + API 按量 | 生态与分发极强；U1 强调 **原生统一架构 + 开源 + 办公交付 Skills** |
| **Google Gemini** | 通用多模态 + Workspace | 消费者 / 企业 | 长上下文、多模态、Agent 能力 | 订阅 + API | Workspace 绑定；SenseNova 绑商汤视觉沉淀与中国合规/部署叙事 |
| **ByteDance BAGEL** | 开源统一多模态基座 | 研究 / 开发者 | 原生支持理解与生成（Seed 开源） | 开源为主 | 同「统一多模态」叙事；U1 叠加 **Token Plan 商业化 + Cowork-Skills 办公闭环 + U1 Pro 交付创图** |
| **DeepSeek Janus / Janus-Pro** | 统一多模态（解耦视觉编码等路线） | 研究 / 开源社区 | 理解+生成统一框架 | 开源 | 架构路线不同（解耦 vs NEO-unify 去拼接）；SenseNova 产品化更深 |
| **Midjourney / Flux 系** | 审美向文生图 | 创作者 | 高质量出图、风格社区 | 订阅 / 开源权重 | 弱在「高密度图文准确交付」；U1 Pro 打 **文字渲染 + 版式 + 长程可控** |
| **Canva / Venngage 等** | AI 信息图 / 设计工具 | 营销与办公 | 模板 + AI 排版 | Freemium | 工具层强、模型层弱；U1 是 **模型基座**，可被 Agent/应用调用 |

---

## 2. 直接竞品详细拆解

### 2.1 OpenAI 多模态（GPT-4o 等）

- **定位与能力**：默认全球通用助手；视觉理解与生成能力强，插件/Agent 生态成熟。
- **优势**：品牌心智、API 惯性、文档与第三方集成密度。
- **劣势（相对本品叙事）**：闭源；中国区可用性与合规因客户而异；「理解/生成/办公交付」未必同一原生架构叙事。
- **流量/SEO**：⚠️ 待验证（Semrush）；品类词被其内容生态占据。
- **与 U1**：海外独立域名战役需正面做 *native unified vs generalist API* 内容，而非纯参数对打。

### 2.2 Google Gemini

- **定位与能力**：多模态 + 搜索/Workspace 分发。
- **优势**：分发、企业套件、长上下文。
- **劣势**：开源社区叙事弱；高密度中文信息图/本土办公 Skills 非其主场。
- **与 U1**：企业办公场景可用 Token 效率 + Cowork-Skills 案例对比。

### 2.3 BAGEL（ByteDance Seed）

- **定位与能力**：开源统一多模态，理解与生成一体（[Seed 介绍](https://seed.bytedance.com/en/blog/seed-research-bagel-the-open-source-unified-multimodal-model-an-all-in-one-model)）。
- **优势**：字节开源影响力、统一多模态心智早一步占领英文技术圈部分讨论。
- **劣势**：⚠️ 待验证商业 API/办公 Skills 完整度；与 SenseNova 在「交付级创图 + Token Plan」产品化节奏不同。
- **与 U1**：技术受众会直接搜索 *BAGEL vs SenseNova U1* —— **必须建对比页**（见 keywords 缺口）。

### 2.4 Janus / Janus-Pro（DeepSeek 路线代表）

- **定位与能力**：统一多模态框架；文献中常与「解耦视觉编码」路线并提（[Janus arXiv](https://arxiv.org/abs/2410.13848)）。
- **优势**：开源社区、与 DeepSeek 品牌关联的研究关注。
- **劣势**：产品平台/Token 套餐/应用层不如日日新完整（初步判断）。
- **与 U1**：用 NEO-unify「去视觉编码器拼接」故事做架构差异化（需保持学术诚实，标引用）。

### 2.5 Midjourney（创图对照，场景竞品）

- **定位与能力**：社区驱动审美生图。
- **优势**：风格、社区、创作者心智。
- **劣势**：复杂中文/多栏信息图文字准确性、长程「交付修订」不如 U1 Pro 宣传点。
- **与 U1 Pro**：场景级对比「海报/信息图/科普图」而非「艺术插画」。

---

## 3. 场景级对比表

### 场景 A：高密度信息图 / 科普图解（文字必须可读）

| 能力维度 | SenseNova U1 / U1 Pro | GPT-4o 系 | Midjourney | BAGEL（开源） |
|----------|----------------------|-----------|------------|---------------|
| 图文准确排版 | ★ 主打（官网/U1 Pro 作品墙） | 中–强（产品迭代中） | 弱–中（文字常糊） | ⚠️ 待验证 |
| 8K / 超长画幅 | ★ U1 Pro 宣称原生 8K | 视产品线 | 有限 | ⚠️ 待验证 |
| 长程修订闭环 | ★ Agentic Generation Loop | Agent/对话可补 | 弱 | 研究向 |
| 开源可自部署 | ★ U1 开源 | 否 | 否（官方） | ★ |
| 本品优势 | 交付级叙事 + 开源 + 作品案例密度 | — | — | — |

### 场景 B：办公长链路（Excel → 分析 → 报告 → PPT）

| 能力维度 | Flash-Lite + Cowork-Skills | ChatGPT / Copilot | 纯文本 Agent + 工具 | Canva AI |
|----------|---------------------------|-------------------|---------------------|----------|
| 端到端交付物 | ★ 官网案例（docx/pptx） | 强（生态） | 中（编排成本高） | 偏设计页 |
| Token 效率叙事 | ★ 宣称约 60% | 一般按量 | 视实现 | N/A |
| 多模态读表读图 | ★ 原生 | 强 | 外挂 | 弱 |
| 可组合 Skills 开源 | ★ | 有限 | 视框架 | 否 |
| 本品优势 | Skills 产品化 + Token Plan 获客 | — | — | — |

---

## 4. 差异与机会

| 维度 | 内容 |
|------|------|
| **Strength** | NEO-unify 叙事清晰；U1 开源 + 应用（小浣熊）放量；U1 Pro WAIC 发布窗口；Token Plan 免费公测低门槛 |
| **Weakness** | 营销站 URL 极简、sitemap 不全；付费价未出；海外独立域名未上线；英文 SEO 落后通用大厂 |
| **Opportunity** | 统一多模态开源对比内容；信息图/PPT Agent 品类词；8 月 U1 Pro 正式定价战役；海外域冷启动 |
| **Threat** | BAGEL/Janus 等分流开源心智；GPT/Gemini 免费层体验；设计工具层截流「信息图」搜索 |

**可攻克增长切口（给 growth-strategy）**：

1. *Native unified multimodal* 教育内容 + vs BAGEL/Janus  
2. *Delivery-grade infographic / AI PPT agent* 场景 SEO（非纯艺术生图）  
3. 开源 → Token Plan → U1 Pro 付费的升级漏斗

---

*功能锚点来源* → [features](./sensenova-features.md) ★ 标记
