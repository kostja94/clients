# Tanka Use Cases 场景页总结

> **文档边界**：本文档仅含 Use Cases（谁在什么情境下用）。产品功能见 [tanka.md](./tanka.md)；关键词见 [tanka-keywords.md](./tanka-keywords.md)；竞品见 [tanka-competitors.md](./tanka-competitors.md)。
> 关联：[tanka.md](./tanka.md) | [tanka-keywords.md](./tanka-keywords.md) | [tanka-competitors.md](./tanka-competitors.md)
> 基于官网 [tanka.ai](https://www.tanka.ai/) 与产品功能

**Use Cases 与 Features 严格区分**：Use Cases 回答「**谁**在**什么情境**下用」；Features 回答「产品**能做什么**」。

---

## 一、场景概览

| 场景 | 目标用户 | 情境 | 目标关键词 | 对应功能 |
|------|----------|------|------------|----------|
| 智能回复邮件/消息 | 创始人、小团队 | 需快速回复大量邮件/Slack，且需上下文 | smart reply for teams, AI email reply | Smart Reply |
| 会议摘要与跟进 | 创始人、小团队 | 会议多、需摘要、需引用过往决策 | AI meeting summary, meeting notes AI | AI 助手 |
| 跨工具搜索 | 创始人、小团队 | 信息散落在 Slack/Gmail/Notion，难找 | semantic search for teams, search across Slack Gmail | 语义搜索 |
| 统一收件箱 | 创始人、小团队 | 邮件、Slack、WhatsApp 分散，切换成本高 | universal inbox, unified inbox AI | Universal Chat / Inbox |
| 任务分配与跟进 | 创始人、小团队 | 任务跨系统、需自动分配与跟进 | AI task routing, task assignment AI | 任务与路由 |
| Pitch deck / 商业计划 | 创始人 | 需快速产出 pitch、BP，需引用组织数据 | AI pitch deck, AI business plan | AI 助手 |
| 组织知识传承 | 创始人、小团队 | 关键人离职，决策与背景流失 | organizational memory, preserve knowledge when people leave | EverMemOS、数据管道 |
| 文档分析与研究 | 创始人、小团队 | 需分析文档、翻译、研究，基于已有知识 | AI document analysis, AI research assistant | AI 助手 |

*场景关键词完整列表见 [tanka-keywords.md](./tanka-keywords.md)*

---

## 二、按 Persona

| Persona | 典型情境 | 痛点 | 产品价值 | 目标关键词 |
|---------|----------|------|----------|------------|
| **创始人** | 邮件爆炸、会议多、决策分散 | 时间被沟通占满，关键信息难回溯 | 智能回复、会议摘要、组织记忆、少招人 | AI for founders, reduce team size with AI |
| **小团队 / 创业公司** | Slack+Gmail+Notion 切换、新人 onboarding | 上下文断裂、重复解释 | 统一 Inbox、语义搜索、AI 助手 | AI for startups, team memory for startups |
| **AI-Native 公司** | 高度自动化、意图与执行分离 | 执行自动化但意图易丢失 | EverMemOS 记忆层、意图保留 | AI-native company tools, operating base for AI companies |

---

## 三、Use Case 与功能映射

| Use Case | 调用的功能 | 说明 |
|----------|------------|------|
| **智能回复** | Smart Reply | 基于上下文与记忆的回复建议（邮件、Slack） |
| **会议摘要** | AI 助手 | 会议摘要、引用过往决策、行动项 |
| **跨工具搜索** | 语义搜索 | 跨 Slack、Gmail、Notion、Drive 等搜索，带来源引用 |
| **统一收件箱** | Universal Chat / Inbox | 邮件、Slack、WhatsApp 统一管理 |
| **任务分配** | 任务与路由 | 任务分配、跨系统自动跟进 |
| **Pitch / BP** | AI 助手 | 基于组织记忆生成 pitch deck、商业计划 |
| **知识传承** | EverMemOS、数据管道 | 持续采集、形成组织记忆，关键人离职不流失 |
| **文档分析** | AI 助手 | 文档分析、翻译、研究，基于存储记忆 |

---

## 四、典型场景描述

### 1. 智能回复邮件/消息

**谁**：创始人、小团队  
**情境**：每天需回复大量邮件和 Slack，需参考过往对话与决策，手动翻找耗时  
**功能**：Smart Reply  
**关键词**：smart reply for teams, AI email reply suggestions, context-aware reply

### 2. 会议摘要与跟进

**谁**：创始人、小团队  
**情境**：会议多，需快速产出摘要、行动项，且需引用过往会议决策  
**功能**：AI 助手  
**关键词**：AI meeting summary, meeting notes AI, AI that remembers context

### 3. 跨工具搜索

**谁**：创始人、小团队  
**情境**：信息散落在 Slack、Gmail、Notion、Drive，搜索需切换多工具  
**功能**：语义搜索  
**关键词**：semantic search for teams, search across Slack Gmail Notion, find anything in company data

### 4. 统一收件箱

**谁**：创始人、小团队  
**情境**：邮件、Slack、WhatsApp 分散，切换成本高，易漏消息  
**功能**：Universal Chat / Inbox  
**关键词**：universal inbox, unified inbox AI, combine Gmail Slack WhatsApp

### 5. 任务分配与跟进

**谁**：创始人、小团队  
**情境**：任务来自邮件、Slack、会议，需分配并跨系统跟进  
**功能**：任务与路由  
**关键词**：AI task routing, task assignment AI, cross-system follow-up

### 6. Pitch deck / 商业计划

**谁**：创始人  
**情境**：需快速产出 pitch deck、商业计划，需引用组织内已有数据与决策  
**功能**：AI 助手  
**关键词**：AI pitch deck, AI business plan, AI assistant for startups

### 7. 组织知识传承

**谁**：创始人、小团队  
**情境**：关键人离职，决策背景、历史讨论流失，新人 onboarding 困难  
**功能**：EverMemOS、数据管道  
**关键词**：organizational memory, preserve knowledge when people leave, team memory AI

### 8. 文档分析与研究

**谁**：创始人、小团队  
**情境**：需分析文档、翻译、做研究，希望 AI 基于组织已有知识回答  
**功能**：AI 助手  
**关键词**：AI document analysis, AI research assistant, AI that remembers context

---

## 五、URL 与页面规划

| 类型 | 页面 | URL | 目标关键词 | 竞品参考 |
|------|------|-----|------------|----------|
| **Persona** | For Founders | /for/founders | AI for founders, reduce team size with AI | Obvious /founders |
| **Persona** | For Startups | /for/startups | AI for startups, team memory for startups | — |
| **Persona** | For AI-Native Companies | /for/ai-native-companies | AI-native company tools | — |
| **场景** | Smart Reply | /use-cases/smart-reply | smart reply for teams, AI email reply | Maya /tools/smart-reply, EmailTree /smart-reply |
| **场景** | Meeting Summary | /use-cases/meeting-summary | AI meeting summary, meeting notes AI | Otter /features |
| **场景** | Semantic Search | /use-cases/semantic-search | semantic search for teams | Glean /product/workplace-search-ai |
| **场景** | Universal Inbox | /use-cases/universal-inbox | universal inbox, unified inbox AI | InboxCentral /features/unified-inbox |
| **场景** | Task Routing | /use-cases/task-routing | AI task routing | — |
| **场景** | Knowledge Preservation | /use-cases/knowledge-preservation | organizational memory, preserve knowledge | — |
| **通用** | 首页 | / | AI operating system, team memory AI | — |
| **通用** | About | /about | EverMemOS, memory-native OS | — |

---

## 六、可拓展场景（功能 × 维度）

| 功能 | 拓展维度 | 待建场景 | 示例 URL | 目标关键词 |
|------|----------|----------|----------|------------|
| Smart Reply | 渠道 | Slack 智能回复 | /use-cases/smart-reply/slack | smart reply Slack |
| Smart Reply | 渠道 | Gmail 智能回复 | /use-cases/smart-reply/gmail | smart reply Gmail AI |
| AI 助手 | 产出 | Pitch deck | /use-cases/pitch-deck | AI pitch deck |
| AI 助手 | 产出 | 商业计划 | /use-cases/business-plan | AI business plan |
| 语义搜索 | 场景 | 新人 onboarding | /use-cases/onboarding | AI onboarding, team knowledge for new hires |
| 任务与路由 | 场景 | 跨系统跟进 | /use-cases/cross-system-follow-up | cross-system task follow-up |

---

## 七、内链与 CTA

- 各 Use Case 页 → /about（产品详情）
- 各 Use Case 页 → 相关 Use Case（Related）
- 各 Persona 页 → 对应场景页
- 各 Use Case 页 → 首页 CTA（Get started / Early Access）
- 首页 → 各 Persona 页、场景页

---

## 八、文档导航

| 文档 | 用途 |
|------|------|
| [tanka.md](./tanka.md) | 主文档、产品概览、定位、网站结构、落地顺序 |
| [tanka-keywords.md](./tanka-keywords.md) | 关键词映射、目标页、待办、高价值页面建议 |
| [tanka-competitors.md](./tanka-competitors.md) | 竞品分析、差异化、Gaps、竞品页面结构 |
