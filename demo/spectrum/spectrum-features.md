# Spectrum Features 功能页总结

> 关联：[spectrum.md](./spectrum.md) | [spectrum-keywords.md](./spectrum-keywords.md) | [spectrum-use-cases.md](./spectrum-use-cases.md) | [spectrum-competitors.md](./spectrum-competitors.md)
> 基于官网 [photon.codes/spectrum](https://photon.codes/spectrum)

**Features 与 Use Cases 严格区分**：Features 回答「产品**能做什么**」；Use Cases 回答「**谁**在**什么情境**下用」。

---

## 一、功能概览与 URL

### Spectrum Framework

| 功能 | URL | 目标关键词 |
|------|-----|------------|
| **Cross Channel** | /spectrum | agent messaging framework, multi-channel agent |
| **Unified API** | /spectrum | agent API, unified messaging API |
| **iMessage** | /spectrum | iMessage agent, AI agent iMessage |
| **WhatsApp / Telegram / X / Discord / Instagram** | /spectrum | agent WhatsApp, agent Telegram |

### Designed for Production

| 功能 | URL | 目标关键词 |
|------|-----|------------|
| **Low latency** | /spectrum | agent latency, low latency messaging |
| **High reliability** | /spectrum | agent reliability, 99.9% uptime |
| **Adaptive Content** | /spectrum | adaptive messaging, native format |
| **Scale** | /spectrum | scale agent, zero config scale |
| **Observability** | /spectrum | agent observability, message audit |

### Photon SDK

| 功能 | URL | 目标关键词 |
|------|-----|------------|
| **Declarative Agent SDK** | /spectrum | agent SDK, declarative agent |
| **Human-Level Interactive Agents** | /spectrum | interactive agent, human-level agent |
| **Multipart Messaging** | /spectrum | multipart messaging agent |

### Agent Templates（Coming Soon）

| 模板 | URL | 目标关键词 |
|------|-----|------------|
| Manus Agent | /templates/manus | travel agent template |
| Customer Support | /templates/customer-support | support agent template |
| Companionship | /templates/companionship | companionship agent template |
| Productivity | /templates/productivity | productivity agent template |
| Concierge | /templates/concierge | concierge agent template |

---

## 二、核心功能详情

### 1. Spectrum Framework

**Cross Channel**
- iMessage、Telegram、WhatsApp、X、Discord、Instagram 等
- 统一 API，覆盖 DM、群组、位置更新等原生能力

**Unified API**
- `Spectrum(providers: [...], config: {...})`
- 按通道（如 `imessage(spectrum)`）限定事件处理
- `onMessage`、`onLocationUpdate` 等
- 支持 `space.send`、`space.updateGroupName` 等通道特有能力

**Ergonomics**
- 类型安全、声明式、易扩展

### 2. Designed for Production

**Low latency. High reliability.**
- <100ms 延迟
- <1s 投递 on Photon's edge network
- 99.9% uptime

**Adaptive Content**
- 各平台以最原生格式渲染消息

**Scale from 1 to millions**
- 零配置扩展

**Observability platform**
- 每条消息完整审计
- Human-in-the-loop 控制
- 成功率、入站/出站分布监控

### 3. Photon SDK

**Build Human-Level Interactive Agents effortlessly**
- 基于 Spectrum 的 Declarative Agent SDK
- 原生消息 Agent 的交互能力

**Perfectly Handle Multipart Messaging**
- 多部分消息（文本、图片、附件等）处理

---

## 三、技术指标（官网展示）

| 指标 | 数值 |
|------|------|
| Total Message | 128,432 |
| Active Agents | 14 |
| Success Rate | 99.87% |
| Inbound：iMessage | 46% |
| Inbound：Telegram | 31% |
| Inbound：other | 23% |
| Outbound：Delivered | 99.9% |
| Outbound：Retried | 0.08% |
| Outbound：Failed | 0.02% |

---

*文档生成日期：2026-03-16 | 来源：官网 [photon.codes/spectrum](https://photon.codes/spectrum)*
