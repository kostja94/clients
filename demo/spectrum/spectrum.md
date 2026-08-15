# Spectrum

> **Spectrum 文档导航**（各文档独立、互相引用）：

| 文档 | 职责 | 引用 |
|------|------|------|
| [spectrum.md](./spectrum.md) | **本文档**：产品概览、定位、网站结构 | — |
| [spectrum-use-cases.md](./spectrum-use-cases.md) | Use Cases：场景、Persona、行业应用 | [spectrum.md] |
| [spectrum-features.md](./spectrum-features.md) | 功能页详情、产品能力 | [spectrum.md] |
| [spectrum-keywords.md](./spectrum-keywords.md) | 关键词映射、目标页、待办 | [spectrum.md]、[spectrum-use-cases.md] |
| [spectrum-competitors.md](./spectrum-competitors.md) | 竞品分析、差异化、Gaps | [spectrum.md] |

*产品入口*：Web [photon.codes/spectrum](https://photon.codes/spectrum)

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2B / 开发者工具 / AI Agent 基础设施 / 消息平台集成 |
| 网站 | https://photon.codes/spectrum |
| 产品形态 | **开源框架**：将 AI Agent 接入 iMessage、Telegram、WhatsApp、X、Discord、Instagram 等日常消息界面 |
| 当前阶段 | 早期（Get a Demo、Join Waitlist） |
| 核心产品 | **Spectrum**：Open-source framework for connecting agents to messaging interfaces |
| Slogan | Bring your agents to the interfaces millions already use |
| 使命 | 让 Agent 触达用户日常使用的消息渠道，统一 API、生产级可靠、可观测 |
| 更新日期 | 2026-03-16 |

---

## 1. 产品信息

### 产品摘要

**Spectrum** 是 Photon 推出的**开源框架**，用于将 AI Agent 接入 iMessage、Telegram、WhatsApp、X、Discord、Instagram 等消息平台。核心价值：**Simple, Powerful, Unified API with Excellent Ergonomics**——一套 API 覆盖多通道，支持 DM、群组、位置更新等原生能力，面向生产环境设计（低延迟、高可靠、可观测、自适应内容、零配置扩展）。

### 产品定位

**Spectrum** 面向**需要将 Agent 部署到消息渠道的开发者与 Agent 团队**，定位为「Agent 与消息界面的桥梁」——你构建 Agent，Spectrum 负责通道连接、投递、适配与可观测。与自建通道或单一平台 SDK 不同，Spectrum 强调：
- **Cross Channel**：iMessage、WhatsApp、Phone、Email、Telegram、X、Discord、Instagram 等
- **Designed for Production**：<100ms 延迟、99.9% 可用、自适应内容渲染、1 到百万用户零配置扩展
- **Observability**：每条消息完整审计、Human-in-the-loop 控制

### 目标受众

- **Agent 开发者**：需要将 Agent 接入 iMessage、WhatsApp 等渠道
- **AI 创业团队**：如 Ditto（iMessage 约会匹配，42k+ 用户）——专注 AI 引擎，通道交给 Spectrum
- **企业**：客服 Agent、旅行 Agent、生产力 Agent 等多通道部署

### 核心产品线

| 能力模块 | 说明 |
|----------|------|
| **Spectrum Framework** | 开源框架；统一 API；多通道（iMessage、Telegram、WhatsApp、X、Discord、Instagram 等） |
| **Photon SDK** | 基于 Spectrum 的 Declarative Agent SDK；Human-Level Interactive Agents；多部分消息处理 |
| **Agent Templates** | Manus、Customer Support、Companionship、Productivity、Concierge（Coming Soon） |
| **Observability** | 消息审计、Human-in-the-loop、成功率与投递监控 |

### 核心价值主张

- **Bring your agents to the interfaces millions already use**
- **Simple, Powerful, Unified API with Excellent Ergonomics**
- **Designed for Production**：Low latency、High reliability、Adaptive content、Scale from 1 to millions
- **Trusted by the world's best agent teams and developers**（Ditto 案例）

### 技术指标（官网展示）

- 延迟：<100ms；投递 <1s on Photon's edge network
- 可用性：99.9% uptime
- 规模：Total Message 128,432；Active Agents 14；Success Rate 99.87%
- 入站：iMessage 46%、Telegram 31%、other 23%
- 出站：Delivered 99.9%、Retried 0.08%、Failed 0.02%

---

## 2. 关键词

| 类型 | 示例 |
|------|------|
| **Primary** | agent messaging framework, AI agent iMessage, agent WhatsApp API, multi-channel agent |
| **Secondary** | iMessage bot framework, Telegram agent SDK, WhatsApp agent integration, agent to messaging |
| **Long-tail** | connect AI agent to iMessage, agent framework for messaging apps |
| **品牌** | Spectrum, Photon, Photon Spectrum |

*完整映射*：见 [spectrum-keywords.md](./spectrum-keywords.md)

---

## 3. 竞品

- **消息平台官方 API**：Apple Business Chat、WhatsApp Business API、Telegram Bot API
- **多通道消息平台**：Twilio、Vonage、MessageBird
- **Agent 基础设施**：LangGraph、CrewAI、AutoGen
- **聊天机器人框架**：Botpress、Rasa、Dialogflow

*详细拆解*：见 [spectrum-competitors.md](./spectrum-competitors.md)

---

## 4. 网站结构

| 路径 | 说明 |
|------|------|
| /spectrum | 首页：Bring your agents to the interfaces millions already use |
| /spectrum#product | 产品能力、API 示例、Designed for Production |
| /spectrum#sdk | Photon SDK、Agent Templates |
| /spectrum#customers | Ditto 案例 |
| /residency | Residency（Photon 其他产品） |
| /blog | 博客 |
| 外部 | Get a Demo（Calendly）、Follow on X、Join Waitlist、Talk to an Expert、Status（status.photon.codes） |

**当前状态**：Spectrum 落地页；Get a Demo、Join Waitlist 为主要转化入口；Agent Templates 标注 Coming Soon。

**待建**：文档站、API Reference、Use Case 页、Pricing、Alternatives 页

---

## 5. 内容营销

- **待建**：文档、Use Case 页、Agent Template 落地页、Blog、Alternatives 页
- **定位**：Agent 消息通道、多通道 Agent 框架、iMessage Agent、生产级 Agent 基础设施

---

## 6. 优化建议

### 页面落地顺序（基于产品定位）

| 阶段 | 页面 | 理由 |
|------|------|------|
| **Phase 0** | /spectrum | ✓ 已上线 |
| **Phase 1** | /docs、API Reference | 开发者获客、降低上手门槛 |
| **Phase 2** | /use-cases/* | 旅行、客服、陪伴、生产力、礼宾等 Agent 场景页 |
| **Phase 3** | /templates/* | Manus、Customer Support、Companionship、Productivity、Concierge 模板页 |
| **Phase 4** | /alternatives、/pricing | 竞品拦截、转化 |
| **Phase 5** | 博客：agent messaging、iMessage agent、multi-channel agent | 教育、SEO |

---

*文档生成日期：2026-03-16 | 来源：官网 [photon.codes/spectrum](https://photon.codes/spectrum)*
